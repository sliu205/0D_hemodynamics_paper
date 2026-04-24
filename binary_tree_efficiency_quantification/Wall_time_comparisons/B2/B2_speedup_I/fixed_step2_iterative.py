"""
Complete CellML to Python Generator - ITERATIVE VARIANT (v5-iter1)

Base: v5 (global-param aware, sel-block safe, final-audit warning).

Iterative additions (see IT-* tags inline):
  IT-1 Detect "iterative vessel" components: any instance whose template is
       in ITERATIVE_VESSEL_TEMPLATES. In these components, `H_mean` is treated
       as an iterative unknown (not algebraic). The H_mean -> mu -> R -> v,v_d
       -> RBC_volume -> H_mean cycle is closed by scipy.optimize.root at each
       RHS evaluation of the integrator.
  IT-2 Remove `H_mean = RBC_volume/q` equations for iterative vessels from
       `all_equations`. These become the residual expressions instead.
  IT-3 Add `<comp>__H_mean` to the `predefined` set so topo-sort treats them
       as known (the solver provides them).
  IT-4 Emit `_iter_unknowns`, `_iter_residual(...)`, `_solve_iterative(...)`
       in the generated model, and call them first inside `ode_rhs` /
       `compute_algebraics` before evaluating the remaining algebraics.
  IT-5 Junction components (template == 'VV_junction_H_D_I') keep their
       existing ode(RBC_volume,t) and algebraic H_mean = RBC_volume/(q_us+div_0).
       They are NOT iterative unknowns.

Design goals:
  - Minimal diff vs. the time-dynamics generator, for fair benchmarking.
  - No hardcoding of component names (branch order agnostic).
  - scipy.optimize.root lives inside the generated model, so `ode_rhs(t, y)`
    stays a drop-in replacement the run-script can pass to solve_ivp.
"""

import re
import csv
from collections import defaultdict
import numpy as np

print("=" * 60)
print("Running step2_iter.py (v5-iter1 - iterative H_mean solver)")
print("=" * 60)

# Files
MAIN = "B2_speedup_I.txt"
MODULES = "B2_speedup_I_modules.txt"
PARAMS_CSV = "B2_speedup_I_parameters.csv"
INITIAL_CSV = "initial_params.csv"
OUTPUT = "generated_model_iter.py"

print("Reading files...")

# Read everything
with open(MAIN) as f:
    main_text = f.read()
with open(MODULES) as f:
    modules_text = f.read()

# ==============================================================================
# 1. Parse component instances
# ==============================================================================
comp_to_template = {}
comp_base_names = set()
for m in re.finditer(r'comp\s+(\w+)\s+using\s+comp\s+(\w+)', main_text):
    comp_inst = m.group(1)
    comp_template = m.group(2)
    comp_to_template[comp_inst] = comp_template
    base = comp_inst.replace('_module', '')
    comp_base_names.add(base)

print(f"Found {len(comp_to_template)} components")

# Parse variable mappings between components
# Format: def map between A and B for vars x and y; enddef;
var_mappings = {}  # {(comp_a, var_a): (comp_b, var_b)}

for m in re.finditer(r'def\s+map\s+between\s+(\w+)\s+and\s+(\w+)\s+for\s+(.*?)enddef', main_text, re.DOTALL):
    comp1 = m.group(1)
    comp2 = m.group(2)
    body = m.group(3)
    
    # Find all "vars x and y;" statements
    for vm in re.finditer(r'vars\s+(\w+)\s+and\s+(\w+)\s*;', body):
        var1 = vm.group(1)
        var2 = vm.group(2)
        
        # Create bidirectional mappings
        base1 = comp1.replace('_module', '')
        base2 = comp2.replace('_module', '')
        var_mappings[(base1, var1)] = (base2, var2)
        var_mappings[(base2, var2)] = (base1, var1)

print(f"Found {len(var_mappings)//2} variable mapping pairs")

# ==============================================================================
# 2. Parse templates to get variables and equations
# ==============================================================================
def convert_cases_to_ternary(cases):
    """Convert CellML case statements to Python ternary."""
    if not cases:
        return '0.0'
    cond, val = cases[0]
    cond = cond.strip()
    val = val.strip().rstrip(';')
    if cond.lower() == 'true':
        return val
    cond = cond.replace('==', ' == ').replace('>=', ' >= ').replace('<=', ' <= ')
    cond = re.sub(r'\s+', ' ', cond).strip()
    if len(cases) > 1:
        return f"({val} if {cond} else {convert_cases_to_ternary(cases[1:])})"
    else:
        return f"({val} if {cond} else 0.0)"


def parse_template(text, name):
    match = re.search(rf'def\s+comp\s+{name}\s+as(.*?)enddef', text, re.DOTALL)
    if not match:
        return None
    body = match.group(1)
    
    vars_info = {}
    for m in re.finditer(r'var\s+(\w+)\s*:\s*\w+(?:\s*\{([^}]*)\})?', body):
        vname = m.group(1)
        attrs = m.group(2) or ''
        init_m = re.search(r'init:\s*([^,;}]+)', attrs)
        is_input = 'pub: in' in attrs or 'pub:in' in attrs
        vars_info[vname] = {
            'init': init_m.group(1).strip() if init_m else None,
            'is_input': is_input
        }
    
    clean = re.sub(r'//.*', '', body)
    clean = re.sub(r'var\s+\w+[^;]*;', '', clean)
    
    odes = []
    for m in re.finditer(r'ode\s*\(\s*(\w+)\s*,\s*\w+\s*\)\s*=(.*?);', clean, re.DOTALL):
        odes.append((m.group(1).strip(), m.group(2).strip()))
    
    clean2 = re.sub(r'ode\s*\([^)]+\)\s*=[^;]*;', '', clean, flags=re.DOTALL)
    # Strip sel/case blocks before the algebraic regex so it doesn't capture
    # garbage from inside them (matches stop at the first ';').
    clean2 = re.sub(r'\w+\s*=\s*sel\s*.*?endsel\s*;', '', clean2, flags=re.DOTALL)
    alg = []
    for m in re.finditer(r'(\w+)\s*=(.*?);', clean2, re.DOTALL):
        lhs = m.group(1).strip()
        rhs = m.group(2).strip()
        if lhs in vars_info and not vars_info[lhs]['is_input'] and lhs != 't':
            alg.append((lhs, rhs))
    
    sel_cases = []
    for m in re.finditer(r'(\w+)\s*=\s*sel\s*(.*?)endsel\s*;', body, re.DOTALL):
        lhs = m.group(1).strip()
        cases_text = m.group(2).strip()
        if lhs in vars_info and not vars_info[lhs]['is_input']:
            cases = re.findall(r'case\s+(.*?)\s*:\s*(.*?)(?=case\s|$)', cases_text, re.DOTALL)
            ternary = convert_cases_to_ternary(cases)
            sel_cases.append((lhs, ternary))
    
    return {'vars': vars_info, 'odes': odes, 'alg': alg, 'sel': sel_cases}


templates = {}
for comp_inst, tmpl_name in comp_to_template.items():
    parsed = parse_template(modules_text, tmpl_name)
    if parsed:
        templates[comp_inst] = parsed

print(f"Parsed {len(templates)} templates")

# Debug: check what was parsed for inlet
if 'inlet_module' in templates:
    tmpl = templates['inlet_module']
    print(f"\nDEBUG inlet_module:")
    print(f"  Variables: {len(tmpl['vars'])}")
    for v in ['v', 'v_scale', 'v_d', 'l', 'r']:
        if v in tmpl['vars']:
            info = tmpl['vars'][v]
            print(f"    {v}: is_input={info.get('is_input', 'N/A')}, init={info.get('init', 'None')}")
        else:
            print(f"    {v}: NOT FOUND")
    print(f"  Algebraic equations: {len(tmpl['alg'])}")
    alg_names = [lhs for lhs, _ in tmpl['alg']]
    print(f"    Names: {alg_names}")
    if 'v' in alg_names:
        print(f"    ✓ v is algebraic")
    else:
        print(f"    ✗ v NOT algebraic")
    if 'v_d' in alg_names:
        print(f"    ✓ v_d is algebraic")
    else:
        print(f"    ✗ v_d NOT algebraic")
    print(f"  ODEs: {len(tmpl['odes'])}")
    for state, _ in tmpl['odes']:
        print(f"    {state}")

# ==============================================================================
# IT-1: Detect iterative vessel components
# ==============================================================================
# Any component whose template is in ITERATIVE_VESSEL_TEMPLATES has the
# algebraic cycle  H_mean -> mu -> R -> v, v_d -> RBC_volume -> H_mean
# and needs scipy.optimize.root to close it at each RHS evaluation.
#
# Junctions (VV_junction_H_D_I) are intentionally excluded: their H_mean comes
# from the state RBC_volume via ode(RBC_volume,t), so no fixed point there.
ITERATIVE_VESSEL_TEMPLATES = {
    'PP_capillary_H_D_I',
    'PP_pericyte_H_D_I',
    'VP_capillary_H_D_I',
}
# Template name we explicitly treat as a junction (for IT-5 bookkeeping).
JUNCTION_TEMPLATES = {'VV_junction_H_D_I'}

print("\nDetecting iterative vessel components...")
iter_vessel_comps = []   # list of base names (e.g. ['inlet', 'PV1', 'PV2', 'V1', 'V2'])
for comp_inst, tmpl_name in comp_to_template.items():
    if tmpl_name in ITERATIVE_VESSEL_TEMPLATES:
        cb = comp_inst.replace('_module', '')
        iter_vessel_comps.append(cb)
# Stable ordering so unknown-index is reproducible across runs.
iter_vessel_comps.sort()
iter_unknown_names = [f"{cb}__H_mean" for cb in iter_vessel_comps]
print(f"  {len(iter_vessel_comps)} iterative vessel(s): {iter_vessel_comps}")
print(f"  Unknowns: {iter_unknown_names}")

junction_comps = [
    comp_inst.replace('_module', '')
    for comp_inst, tmpl_name in comp_to_template.items()
    if tmpl_name in JUNCTION_TEMPLATES
]
print(f"  {len(junction_comps)} junction(s) (NOT iterative): {junction_comps}")

# ==============================================================================
# A "global" parameter is any variable that gets mapped from `parameters` or
# `parameters_global` to one or more component modules. These need to be
# replicated under each consuming component's namespace, regardless of whether
# the CSV row uses a `global/` prefix.
print("\nDetecting global parameters from CellML mappings...")
global_param_names = set()
global_param_consumers = defaultdict(set)
for (comp_a, var_a), (comp_b, var_b) in var_mappings.items():
    a_is_param = comp_a in ('parameters', 'parameters_global')
    b_is_param = comp_b in ('parameters', 'parameters_global')
    if a_is_param and not b_is_param:
        # var_a is the name on the parameters side; var_b is the local module name.
        # Both names get registered so a CSV row using either spelling works.
        global_param_names.add(var_a)
        global_param_names.add(var_b)
        global_param_consumers[var_a].add(comp_b)
        global_param_consumers[var_b].add(comp_b)
    elif b_is_param and not a_is_param:
        global_param_names.add(var_b)
        global_param_names.add(var_a)
        global_param_consumers[var_b].add(comp_a)
        global_param_consumers[var_a].add(comp_a)

# Belt-and-suspenders: also register every `pub:in` variable as potentially
# global. If the CSV has a bare row matching one of these names, it'll be
# replicated to all components that declare that variable as input.
for comp_inst, tmpl in templates.items():
    cb = comp_inst.replace('_module', '')
    if cb in ('parameters', 'parameters_global'):
        continue
    for vname, info in tmpl['vars'].items():
        if info.get('is_input'):
            global_param_names.add(vname)
            global_param_consumers[vname].add(cb)

print(f"  Found {len(global_param_names)} global variable name(s)")

# ==============================================================================
# 3. Load parameters from CSVs
# ==============================================================================
params = {}
unmatched_csv_rows = []   # rows from PARAMS_CSV we couldn't place anywhere

# From <model>_parameters.csv
with open(PARAMS_CSV) as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_name = row['variable_name'].strip()
        value = row['value'].strip()
        
        matched = False
        # Step 1: try to match a component suffix (e.g. r_PV1 -> PV1__r).
        # FIX: iterate from longest comp_base to shortest, and require a word
        # boundary on at least one side. Prevents `PV1` from matching inside
        # `l_PV10`, `r_PV12`, etc. — a real bug for B3+ trees with PV10..PV14.
        for comp_base in sorted(comp_base_names, key=len, reverse=True):
            # Match `<base>_...` (prefix), `..._<base>` (suffix), or
            # `..._<base>_...` (middle). Each form has _ on at least one side
            # of comp_base, so PV1 in l_PV10 fails (no _ after the 1).
            if (raw_name.startswith(f'{comp_base}_') or
                    raw_name.endswith(f'_{comp_base}') or
                    f'_{comp_base}_' in raw_name):
                var_part = raw_name.replace(f'_{comp_base}', '').replace(f'{comp_base}_', '')
                if var_part and var_part != raw_name:
                    params[f"{comp_base}__{var_part}"] = value
                    matched = True
                    break

        if matched:
            continue
        
        # Step 2: NEW — if the bare name is a known global parameter, replicate
        # it to every component that has it as `pub: in`.
        if raw_name in global_param_names:
            consumers = global_param_consumers.get(raw_name, set())
            if not consumers:
                consumers = {cb for cb in comp_base_names
                             if cb not in ('parameters', 'parameters_global')}
            for cb in consumers:
                params[f"{cb}__{raw_name}"] = value
            params[raw_name] = value  # also keep bare copy, harmless
            print(f"  [global] {raw_name} = {value}  -> replicated to {len(consumers)} component(s)")
            continue
        
        # Step 3: still nothing matched — keep it bare and remember for warning
        params[raw_name] = value
        unmatched_csv_rows.append(raw_name)

# From initial_params.csv  
with open(INITIAL_CSV) as f:
    reader = csv.DictReader(f)
    for row in reader:
        cat = row.get('category', '').strip()
        var = row['variable'].strip()
        value = row['value'].strip()
        
        if cat == 'constant':
            py_name = var.replace('/', '__').replace('_module', '')
            params[py_name] = value
            
            # If it's a global parameter (CSV uses 'global/' convention),
            # replicate it for each component that has it as pub:in. Falls back
            # to "all non-parameter components" if the consumer set is unknown.
            if var.startswith('global/'):
                var_name = var.replace('global/', '')
                consumers = global_param_consumers.get(var_name)
                if not consumers:
                    consumers = {cb for cb in comp_base_names
                                 if cb not in ('parameters', 'parameters_global', 'global')}
                for cb in consumers:
                    params[f"{cb}__{var_name}"] = value
        elif cat == 'state':
            # Store initial conditions separately
            py_name = var.replace('/', '__').replace('_module', '')
            params[f"INIT_{py_name}"] = value
        elif cat == 'algebraic':
            # IT-4a: keep initial algebraic values under an INITALG_ prefix.
            # Used as first-iteration guesses for iterative unknowns
            # (e.g. INITALG_PV1__H_mean for PV1__H_mean).
            py_name = var.replace('/', '__').replace('_module', '')
            params[f"INITALG_{py_name}"] = value

print(f"Loaded {len(params)} parameters")
if unmatched_csv_rows:
    print(f"  ⚠ {len(unmatched_csv_rows)} CSV row(s) didn't match any component or known global:")
    for n in unmatched_csv_rows[:10]:
        print(f"      {n}")
    if len(unmatched_csv_rows) > 10:
        print(f"      ... and {len(unmatched_csv_rows)-10} more")

# Debug: check if the problematic ones are in params
for check in ['inlet__v', 'inlet__v_scale', 'inlet__v_d', 'inlet__l', 'inlet__r']:
    if check in params:
        print(f"  ✓ {check} = {params[check]}")
    else:
        print(f"  ✗ {check} NOT in params")

# ==============================================================================
# 4. Build state list
# ==============================================================================
state_list = []
for comp_inst, tmpl in templates.items():
    comp_base = comp_inst.replace('_module', '')
    for state_var, rhs in tmpl['odes']:
        state_name = f"{comp_base}__{state_var}"
        init_key = f"INIT_{state_name}"
        if init_key in params:
            init_val = params[init_key]
        else:
            init_val = "0.0"
        state_list.append((state_name, init_val))

print(f"Found {len(state_list)} state variables")

# ==============================================================================
# 5. Collect all equations
# ==============================================================================
all_equations = []
ode_equations = []

param_vars = {name for name in params.keys() if '__' in name and not name.startswith('INIT_')}

for comp_inst, tmpl in templates.items():
    comp_base = comp_inst.replace('_module', '')
    
    if comp_base in ['parameters', 'parameters_global']:
        continue
    
    # ODEs
    for state_var, rhs in tmpl['odes']:
        state_name = f"{comp_base}__{state_var}"
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        ode_equations.append((state_name, ns_rhs))
    
    # Algebraic
    for lhs, rhs in tmpl['alg']:
        lhs_name = f"{comp_base}__{lhs}"
        if tmpl['vars'].get(lhs, {}).get('is_input', False):
            continue
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        all_equations.append((lhs_name, ns_rhs))
    
    # sel/case equations
    for lhs, rhs in tmpl.get('sel', []):
        lhs_name = f"{comp_base}__{lhs}"
        if tmpl['vars'].get(lhs, {}).get('is_input', False):
            continue
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        all_equations = [(l, r) for l, r in all_equations if l != lhs_name]
        all_equations.append((lhs_name, ns_rhs))

# Apply variable mappings to replace mapped variables
def apply_mappings(expr, var_mappings):
    """Replace variables in expression according to mappings."""
    # Phase 1: Component connections (neither side is parameters)
    for (comp_a, var_a), (comp_b, var_b) in var_mappings.items():
        if comp_a not in ['parameters', 'parameters_global'] and comp_b not in ['parameters', 'parameters_global']:
            old_name = f"{comp_a}__{var_a}"
            new_name = f"{comp_b}__{var_b}"
            if old_name in expr:
                expr = re.sub(rf'\b{re.escape(old_name)}\b', new_name, expr)
    
    # Phase 2: Remove parameters/parameters_global references
    for (comp_a, var_a), (comp_b, var_b) in var_mappings.items():
        if comp_a in ['parameters', 'parameters_global']:
            old_name = f"{comp_a}__{var_a}"
            new_name = f"{comp_b}__{var_b}"
            expr = re.sub(rf'\b{re.escape(old_name)}\b', new_name, expr)
        elif comp_b in ['parameters', 'parameters_global']:
            old_name = f"{comp_b}__{var_b}"
            new_name = f"{comp_a}__{var_a}"
            expr = re.sub(rf'\b{re.escape(old_name)}\b', new_name, expr)
    
    return expr

all_equations = [(lhs, apply_mappings(rhs, var_mappings)) for lhs, rhs in all_equations]
ode_equations = [(lhs, apply_mappings(rhs, var_mappings)) for lhs, rhs in ode_equations]

# Clean up expressions
def clean_expr(e):
    e = re.sub(r'\{[^}]+\}', '', e)
    e = e.replace('sqr(', 'np.square(')
    e = e.replace('pow(', 'safe_power(')
    e = e.replace('exp(', 'np.exp(')
    e = e.replace('abs(', 'np.abs(')
    e = e.replace('ln(', 'np.log(')
    e = e.replace('atan(', 'np.arctan(')
    e = re.sub(r'\bpi\b', 'np.pi', e)
    e = re.sub(r'safe_power\((\d+),', r'safe_power(\1.0,', e)
    return e

all_equations = [(l, clean_expr(r)) for l, r in all_equations]
ode_equations = [(l, clean_expr(r)) for l, r in ode_equations]

# ==============================================================================
# IT-2: Extract H_mean equations for iterative vessels, remove from all_equations.
# ==============================================================================
# For each iterative vessel, find the equation H_mean = RBC_volume/q and pull
# it out. The RHS becomes the "implied H_mean" used in the residual:
#   residual_j = implied_H_mean_j - trial_H_mean_j
# The equation is removed from all_equations because H_mean is now supplied by
# the solver, not computed in forward order.
iter_residual_rhs = {}  # { 'PV1__H_mean': 'PV1__RBC_volume/PV1__q', ... }
_iter_lhs_set = set(iter_unknown_names)
_new_all_equations = []
for lhs, rhs in all_equations:
    if lhs in _iter_lhs_set:
        iter_residual_rhs[lhs] = rhs
    else:
        _new_all_equations.append((lhs, rhs))
all_equations = _new_all_equations

# ==============================================================================
# IT-2b (BUG FIX): Override iter_residual_rhs with the correct flux-balance form.
# ==============================================================================
# The CellML template defines `H_mean = RBC_volume / q` and separately defines
# `RBC_volume = (v*H_vol_L - v_d*H_vol_R)/(v+v_d)` as an algebraic equation
# (see B2_speedup_I_modules.txt lines 1198-1200, 1385-1387, 1562-1564).
#
# The previous pipeline took `H_mean = RBC_volume/q` verbatim and multiplied
# through to get residual:
#     res = RBC_volume - H_mean * q
# Then _expand_divs substituted RBC_volume's algebraic definition, pulling the
# (v+v_d) denominator up onto the H_mean side, giving:
#     res = (v*H_vol_L - v_d*H_vol_R) - H_mean * q * (v + v_d)
#
# The user's specified residual (what the physics actually says at quasi-SS) is:
#     res = (v*H_vol_L - v_d*H_vol_R) - H_mean * (v + v_d)
# i.e. H_mean equals the flow-averaged hematocrit directly — no q.
#
# The simplest correct interpretation: for iterative vessels, bypass the
# spurious /q in `H_mean = RBC_volume/q` and use RBC_volume's own algebraic
# definition directly as the residual source:
#     H_mean = RBC_volume  (substituting RBC_volume = num/denom directly)
# which gives the desired residual shape after _expand_divs.
#
# We do this by looking up RBC_volume's algebraic equation in `all_equations`
# and rewriting iter_residual_rhs[comp__H_mean] to point at that RHS directly.
_alg_rhs_of_lookup = {lhs: rhs for lhs, rhs in all_equations}

_fixed_count = 0
iter_flow_terms = {}  # {comp_base: (flow_L_expr, flow_R_expr)} for anchor use later

def _extract_flow_terms_from_rbc_rhs(rhs_str):
    """
    Given an RBC_volume algebraic RHS like
        '(A*X__H_volume_L - B*X__H_volume_R) / (A + B)'
    or any equivalent bracketing, return (A, B) as strings so the anchor can
    use `abs(A) + abs(B)` for the flow magnitude. Returns None if the pattern
    doesn't match (we still keep the fix; the anchor just falls back).
    """
    # Remove outer parens pairs if present, then try to match the numerator
    # flow*H_L - flow*H_R pattern. We don't try to be fully general; we just
    # want to expose the two flow expressions for the anchor.
    s = rhs_str.strip()
    # Match '(num)/(den)' where num contains the pattern
    m = re.match(r'^\s*\((.*)\)\s*/\s*\(.*\)\s*$', s, re.DOTALL)
    inner = m.group(1) if m else s
    m2 = re.match(
        r'^\s*(.+?)\s*\*\s*[A-Za-z_]\w*__H_(?:mass|volume)_L\s*'
        r'-\s*(.+?)\s*\*\s*[A-Za-z_]\w*__H_(?:mass|volume)_R\s*$',
        inner
    )
    if not m2:
        return None
    return m2.group(1).strip(), m2.group(2).strip()

for comp_base in iter_vessel_comps:
    hmean_name = f"{comp_base}__H_mean"
    rbc_name   = f"{comp_base}__RBC_volume"
    rbc_rhs = _alg_rhs_of_lookup.get(rbc_name)
    if rbc_rhs is None:
        print(f"  ⚠ IT-2b: no RBC_volume algebraic equation found for iterative "
              f"vessel {comp_base}; leaving residual as-is (will be WRONG)")
        continue
    # Point the H_mean residual source directly at RBC_volume's algebraic RHS.
    # _expand_divs will then pull num up as numerator and denom up as the
    # (v+v_d) factor on the H_mean side — with NO extra q.
    iter_residual_rhs[hmean_name] = rbc_rhs
    # Extract the two flow terms so the zero-flow anchor uses the correct
    # flows (v_in+v for V*, v+v_d for PV*/inlet).
    terms = _extract_flow_terms_from_rbc_rhs(rbc_rhs)
    if terms is not None:
        iter_flow_terms[comp_base] = terms
    _fixed_count += 1

print(f"  IT-2b (fix): rewrote {_fixed_count}/{len(iter_vessel_comps)} residual "
      f"expression(s) to use RBC_volume's algebraic RHS directly (drops spurious /q)")

# Sanity: every declared iterative unknown must have had an equation.
_missing_iter = [n for n in iter_unknown_names if n not in iter_residual_rhs]
if _missing_iter:
    print(f"  ⚠ IT-2: iterative unknowns without an H_mean equation: {_missing_iter}")
    print(f"     These were declared as iterative but the template didn't emit")
    print(f"     an algebraic H_mean=...; check ITERATIVE_VESSEL_TEMPLATES.")
print(f"  IT-2: pulled {len(iter_residual_rhs)} H_mean equation(s) into residuals")

print(f"Found {len(all_equations)} algebraic equations")
print(f"Found {len(ode_equations)} ODE equations")

# ==============================================================================
# Sort algebraic equations topologically
# ==============================================================================
def topo_sort_equations(equations, defined_vars):
    defined = set(defined_vars)
    
    ordered = []
    remaining = list(equations)
    
    max_iterations = len(remaining) * 3
    for iteration in range(max_iterations):
        if not remaining:
            break
        next_rem = []
        progress = False
        
        for lhs, rhs in remaining:
            deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
            unmet = deps - defined
            if not unmet:
                ordered.append((lhs, rhs))
                defined.add(lhs)
                progress = True
            else:
                next_rem.append((lhs, rhs))
        
        remaining = next_rem
        if not progress:
            print(f"  WARNING: Topological sort stuck at iteration {iteration}")
            print(f"  Remaining equations: {len(remaining)}")
            rem_with_unmet = []
            for lhs, rhs in remaining:
                deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
                unmet = deps - defined
                rem_with_unmet.append((lhs, rhs, unmet))
            rem_with_unmet.sort(key=lambda x: len(x[2]))
            print(f"  --- First 10 stuck equations (fewest unmet deps first) ---")
            stuck_lhs = {x[0] for x in rem_with_unmet}
            for lhs, rhs, unmet in rem_with_unmet[:10]:
                cat = []
                for u in sorted(unmet):
                    if u in stuck_lhs:
                        cat.append(f"{u}[STUCK]")
                    else:
                        cat.append(f"{u}[TRULY-MISSING]")
                print(f"    {lhs}:")
                print(f"      RHS: {rhs[:120]}")
                print(f"      unmet: {cat}")
            truly_missing = set()
            for _, _, unmet in rem_with_unmet:
                truly_missing |= (unmet - stuck_lhs)
            if truly_missing:
                print(f"  --- Variables referenced but never defined: {len(truly_missing)} ---")
                for tm in sorted(truly_missing)[:30]:
                    print(f"    {tm}")
            break

    # FIX: do NOT dump leftover equations onto the end in declaration order.
    # The previous behavior masked the topo-sort failure: the generator emitted
    # broken code where some_var was used before its definition, surfacing as
    # UnboundLocalError at runtime. Bailing here makes the generator failure
    # match the Python failure (audit step at end will list missing vars).
    if remaining:
        print(f"  ⚠ topo-sort left {len(remaining)} equation(s) unsorted; "
              f"they are dropped from the generated model.")
        print(f"    Fix the missing parameters/equations listed above and re-run.")
    return ordered

# Build the predefined set
computed_lhs = {lhs for lhs, _ in all_equations}

predefined = set()
for name in params.keys():
    if '__' in name and not name.startswith('INIT_'):
        if name in computed_lhs:
            continue
        predefined.add(name)
for s, _ in state_list:
    predefined.add(s)
predefined.add('environment__time')

# IT-3: iterative H_mean unknowns are supplied by the solver at runtime, so
# topo-sort must treat them as already known. They're injected into the
# algebraic block the same way state unpacking is.
for _iu in iter_unknown_names:
    predefined.add(_iu)
print(f"IT-3: added {len(iter_unknown_names)} iterative unknown(s) to predefined")

print(f"Predefined variables: {len(predefined)}")
for check in ['inlet__v', 'inlet__v_scale', 'inlet__v_d', 'VV_junc1__w_in2',
              'VV_junc1__R_VV_junc']:
    if check in predefined:
        print(f"  ✓ {check}")
    else:
        in_computed = check in computed_lhs
        print(f"  ✗ {check} MISSING (in computed_lhs={in_computed})")

print("--- computed_lhs membership check ---")
for check in ['PV1__v', 'PV1__u', 'PV1__R', 'VV_junc1__u_d', 'VV_junc1__vj3',
              'VV_junc1__H_from1', 'VV_junc1__H_from1_target', 'VV_junc1__v']:
    in_computed = check in computed_lhs
    in_predef   = check in predefined
    print(f"  {check}: computed_lhs={in_computed}  predefined={in_predef}")
for lhs, rhs in all_equations:
    if lhs == 'PV1__v':
        print(f"  PV1__v RHS: {rhs}")
        _deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
        print(f"  PV1__v deps: {_deps}")
        break
else:
    print("  PV1__v: NO EQUATION FOUND in all_equations (!!)")

all_equations = topo_sort_equations(all_equations, predefined)

print("Equations sorted")
print(f"First 10 sorted equations:")
for i, (lhs, rhs) in enumerate(all_equations[:10]):
    deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
    print(f"  {i}: {lhs} (deps: {len(deps)})")

# ==============================================================================
# NEW (v5): Final dependency audit — warn loudly if anything is missing
# ==============================================================================
# Walk every emitted equation (sorted alg + ODE) and check that each name
# appearing on the RHS is either: predefined, a state, or computed earlier.
# Anything else means the generated_model.py will throw UnboundLocalError when
# someone tries to run it.
print("\n--- Final dependency audit ---")
known_at_runtime = set(predefined)
truly_missing_audit = set()
for lhs, rhs in all_equations:
    deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
    missing = deps - known_at_runtime
    if missing:
        for m in missing:
            truly_missing_audit.add(m)
    known_at_runtime.add(lhs)
# ODE RHSes are evaluated AFTER all algebraics, so their deps need to be in
# `known_at_runtime` as it stands at the end.
for state_name, rhs in ode_equations:
    deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
    missing = deps - known_at_runtime
    if missing:
        for m in missing:
            truly_missing_audit.add(m)

if truly_missing_audit:
    print(f"  ⚠⚠⚠ {len(truly_missing_audit)} variable(s) referenced but never defined:")
    for m in sorted(truly_missing_audit):
        print(f"      {m}")
    print(f"  The generated model WILL FAIL at runtime.")
    print(f"  Likely causes:")
    print(f"    - Missing entry in parameters CSV (add a row for the bare name).")
    print(f"    - Variable declared pub:in but no mapping ever resolves it.")
    print(f"    - CellML typo in the variable name vs. how it's referenced.")
else:
    print(f"  ✓ All references resolved — generated model should run.")

# ==============================================================================
# 6. Write output
# ==============================================================================
lines = [
    '"""Generated model (ITERATIVE variant - scipy.optimize.root on H_mean)"""',
    'import numpy as np',
    'from scipy.integrate import solve_ivp',
    'from scipy.optimize import root',
    'import matplotlib.pyplot as plt',
    '',
    '# Safe power function to handle negative bases with non-integer exponents',
    'def safe_power(base, exponent):',
    '    """',
    '    Safe version of np.power that handles edge cases:',
    '    - If base < 0 and exponent is non-integer, use absolute value',
    '    - Clips very small values to avoid numerical issues',
    '    """',
    '    base = np.clip(base, 1e-15, None)  # Avoid zero/negative',
    '    return np.power(base, exponent)',
    '',
    '# Parameters',
]

state_names = {s for s, _ in state_list}
computed_lhs_set = {lhs for lhs, _ in all_equations}
# IT-4: iterative H_mean names are supplied by the solver, never written as
# module-level constants, even if the CSV has an algebraic entry for them.
_iter_name_set = set(iter_unknown_names)

# ==============================================================================
# IT-6: Inlined algebraic block emitter (eval-free fast path).
# ==============================================================================
# Previously we emitted a shared function `_eval_algebraics` that returned
# locals() and used `eval()` in ode_rhs / _iter_residual to read values out of
# the returned dict. `eval()` parses + lookups dominated hot-loop wall time.
# The fast path inlines the algebraic block directly into every function that
# needs it, at 4-space indent. Each function gets its own unpacked local
# namespace: no dict, no eval, no shared helper call.
def _emit_algebraic_body(lines, emit_H_means=True):
    """Append state-unpack + time + (optional H_means inject) + all algebraics
    as indented Python lines into `lines`. All variables become locals of the
    enclosing function, so downstream expressions can reference them directly
    without eval or dict lookup.
    """
    lines.append('    # Unpack state')
    for i, (sname, _) in enumerate(state_list):
        lines.append(f'    {sname} = y[{i}]')
    lines.append('')
    lines.append('    # Time')
    lines.append('    environment__time = t')
    if emit_H_means and iter_unknown_names:
        lines.append('')
        lines.append('    # Inject iterative unknowns (supplied by caller)')
        for i, n in enumerate(iter_unknown_names):
            lines.append(f'    {n} = H_means[{i}]')
    lines.append('')
    lines.append('    # Algebraic equations (topo-sorted)')
    for lhs, rhs in all_equations:
        lines.append(f'    {lhs} = {rhs}')

for name, value in sorted(params.items()):
    if '__' in name and not name.startswith('INIT_') and not name.startswith('INITALG_'):
        if name in computed_lhs_set:
            continue
        if name in _iter_name_set:
            continue  # will be a solver unknown
        lines.append(f"{name} = {value}")

# IT-4: iterative solver metadata ---------------------------------------------
lines.extend([
    '',
    '# =========================================================================',
    '# Iterative H_mean solver (IT-4)',
    '# =========================================================================',
    '# One unknown per vessel with H_mean -> mu -> R -> v,v_d -> RBC_volume -> H_mean.',
    '# Residual = implied_H_mean - trial_H_mean; solved by scipy.optimize.root',
    '# once per RHS evaluation. The previous solution is cached as the initial',
    '# guess for the next call (solve_ivp typically takes small steps).',
    '',
    '# Zero-flow regularization (IT-4e).',
    '# When flow magnitude is near ZERO_FLOW_REG_EPS, the solver anchors H_mean',
    '# to H_global_L to break the degeneracy of a 0 = 0 residual.',
    '# ZERO_FLOW_REG_EPS is the flow scale at which the anchor activates',
    '# (units: m^3/s; pick comfortably below your smallest expected flow).',
    '# ZERO_FLOW_ANCHOR_STRENGTH is the magnitude of the anchor (unitless; pick',
    '# much bigger than residual noise at the fixed point, ~1e-10).',
    '# Set either to 0.0 to disable.',
    'ZERO_FLOW_REG_EPS = 1e-12',
    'ZERO_FLOW_ANCHOR_STRENGTH = 1e-10',
    '',
    '# Ordered list of iterative unknown names.',
    'iter_unknown_names = [',
])
for n in iter_unknown_names:
    lines.append(f"    '{n}',")
lines.append(']')

# Initial guess vector: prefer CSV 'algebraic' entries, else fall back to 0.45.
iter_initial_guess = []
for n in iter_unknown_names:
    key = f"INITALG_{n}"
    if key in params:
        iter_initial_guess.append(params[key])
    else:
        iter_initial_guess.append('0.45')  # hematocrit default
        print(f"  ⚠ no INITALG_ for {n}, defaulting to 0.45")

lines.extend([
    '',
    '# Initial guess (from CSV algebraic entries, fallback 0.45).',
    '_iter_initial_guess = np.array([',
])
for g in iter_initial_guess:
    lines.append(f"    {g},")
lines.extend([
    '])',
    '',
    '# Cached last solution (reused as warm-start on next call).',
    '_iter_last_solution = [_iter_initial_guess.copy()]',
    '',
])

# IT-6: _eval_algebraics helper function has been REMOVED.
# We now inline the algebraic block directly into every caller (ode_rhs,
# compute_algebraics, _iter_residual) via _emit_algebraic_body(). This kills
# the eval() + dict-lookup overhead that dominated wall time in prior versions.

# --- Residual function (IT-4b, IT-4c) ---
# For a "H_mean = X/Y" cycle, computing  residual = (X/Y) - H_mean  suffers from
# catastrophic cancellation when Y is tiny (v+v_d ~ 1e-15 near steady state).
# We reformulate it as  residual = X - H_mean*Y, which has the same root but is
# well-conditioned.
#
# IT-4c: One level is often not enough. In this model, X is itself of the form
# "(a)/(b)" (e.g. RBC_volume = (v*H_vL - v_d*H_vR)/(v+v_d)), so X/Y has the form
# a/(b*Y) and the implied residual = a - H_mean*b*Y is clean. We recursively
# substitute through computed-algebraic divisions up to MAX_SUBST_DEPTH levels.
MAX_SUBST_DEPTH = 3
import ast as _ast
def _split_div(rhs_str):
    """Return (num, denom) if rhs is a top-level division, else (rhs, '1')."""
    try:
        tree = _ast.parse(rhs_str, mode='eval').body
    except SyntaxError:
        return rhs_str, '1'
    if isinstance(tree, _ast.BinOp) and isinstance(tree.op, _ast.Div):
        depth = 0
        last_div = -1
        for i, ch in enumerate(rhs_str):
            if ch == '(': depth += 1
            elif ch == ')': depth -= 1
            elif ch == '/' and depth == 0:
                last_div = i
        if last_div > 0:
            return rhs_str[:last_div].strip(), rhs_str[last_div+1:].strip()
    return rhs_str, '1'

# Build a lookup: algebraic LHS -> RHS string, for substitution.
_alg_rhs_of = {lhs: rhs for lhs, rhs in all_equations}

def _expand_divs(expr, depth=0):
    """Pull top-level divisions up, returning (num_factors, denom_factors).
    expr is a string. If expr is a simple name whose equation is X/Y, recurse
    on X and Y. Otherwise treat expr as atomic (one numerator factor).
    Returns two lists of expression strings whose products equal the value.
    """
    if depth >= MAX_SUBST_DEPTH:
        return [f"({expr})"], []
    # Strip outermost parens & whitespace so "(PV1__RBC_volume)" -> "PV1__RBC_volume"
    stripped = expr.strip()
    while stripped.startswith('(') and stripped.endswith(')'):
        # only strip if the parens actually match (not like "(a)+(b)")
        depth_paren = 0
        matched = True
        for i, ch in enumerate(stripped):
            if ch == '(': depth_paren += 1
            elif ch == ')': depth_paren -= 1
            if depth_paren == 0 and i < len(stripped) - 1:
                matched = False
                break
        if matched:
            stripped = stripped[1:-1].strip()
        else:
            break
    num, den = _split_div(stripped)
    if den == '1':
        # Not a division. But it might be a single name whose equation is one.
        if stripped.isidentifier() and stripped in _alg_rhs_of:
            sub_rhs = _alg_rhs_of[stripped]
            sub_num, sub_den = _split_div(sub_rhs)
            if sub_den != '1':
                # stripped = (sub_num)/(sub_den). Expand each side recursively.
                n_list, d_list = _expand_divs(sub_num, depth+1)
                dn_list, dd_list = _expand_divs(sub_den, depth+1)
                # num_factors from top = n_list + dd_list (from denominator's denominator)
                # den_factors from top = dn_list + d_list
                return n_list + dd_list, dn_list + d_list
        return [f"({stripped})"], []
    # expr is itself a division num/den — recurse on both halves.
    n_list, d_list = _expand_divs(num, depth+1)
    dn_list, dd_list = _expand_divs(den, depth+1)
    return n_list + dd_list, dn_list + d_list

def _product(factors):
    """Join factors with '*', or return '1' if empty."""
    if not factors:
        return '1'
    return '*'.join(factors)

lines.extend([
    'def _iter_residual(H_means, t, y):',
    '    """F(H_means) = num - H_mean*denom  +  ZERO_FLOW_REG anchor.',
    '    ',
    '    The anchor term is  gate * ZERO_FLOW_ANCHOR_STRENGTH * (H_global_L - H_mean),',
    '    where gate = v_eps_reg**2 / (flow**2 + v_eps_reg**2). When flow >> v_eps_reg,',
    '    gate -> 0 and the anchor vanishes (true fixed point undisturbed). When',
    '    flow is near zero, gate -> 1 and the anchor pulls H_mean toward',
    '    H_global_L, breaking the degeneracy of 0 = 0.',
    '    ',
    '    Disable by setting ZERO_FLOW_REG_EPS = 0 below.',
    '    ',
    '    IT-6: algebraic block is INLINED here (no eval, no dict lookups).',
    '    """',
])
# Inline state unpack + H_means injection + all algebraics as local variables.
_emit_algebraic_body(lines, emit_H_means=True)
lines.extend([
    '',
    '    # Residuals + zero-flow regularization',
    '    res = np.empty(len(H_means))',
])
for i, n in enumerate(iter_unknown_names):
    rhs = iter_residual_rhs[n]
    # Component base name: PV1__H_mean -> "PV1"
    comp_base = n.split('__')[0]
    # Expand divisions recursively: rhs evaluates to product(num)/product(den).
    num_factors, den_factors = _expand_divs(rhs)
    num_expr = _product(num_factors)
    den_expr = _product(den_factors) if den_factors else '1'
    # Emit direct Python expressions; all algebraics are in scope as locals.
    if den_expr == '1':
        lines.append(f"    res[{i}] = ({num_expr}) - H_means[{i}]")
    else:
        lines.append(
            f"    res[{i}] = ({num_expr}) - H_means[{i}] * ({den_expr})"
        )
    # Zero-flow anchor (IT-4e). Flow vars are locals, not dict lookups.
    # Use the same flow terms that appear in the residual denominator (set up
    # by IT-2b fix) so the gate correctly detects when the residual becomes
    # degenerate. Falls back to the old v/v_d heuristic if flow_terms unset.
    if comp_base in iter_flow_terms:
        flow_L, flow_R = iter_flow_terms[comp_base]
        lines.append(f"    _flow = abs({flow_L}) + abs({flow_R})")
    else:
        v_name = f"{comp_base}__v"
        vd_name = f"{comp_base}__v_d"
        if v_name in computed_lhs_set and vd_name in computed_lhs_set:
            lines.append(f"    _flow = abs({v_name}) + abs({vd_name})")
        elif v_name in computed_lhs_set:
            lines.append(f"    _flow = abs({v_name})")
        else:
            lines.append(f"    _flow = 0.0")
    lines.append(
        f"    _gate = ZERO_FLOW_REG_EPS**2 / "
        f"(_flow**2 + ZERO_FLOW_REG_EPS**2 + 1e-300)"
    )
    lines.append(
        f"    res[{i}] += _gate * ZERO_FLOW_ANCHOR_STRENGTH * "
        f"({comp_base}__H_global_L - H_means[{i}])"
    )
lines.extend([
    '    return res',
    '',
])

# Module-level knob for the regularization strength. Users can set this to 0
# to disable, or tune to their expected minimum flow scale.
# NOTE: the bare name without component prefix means it's read via globals().
# Insert at module-constants section (done below in output ordering).
_iter_extra_module_constants = [
    '',
    '# Zero-flow regularization strength (IT-4e).',
    '# When flow magnitude ~ ZERO_FLOW_REG_EPS, the iterative solver anchors',
    '# H_mean to H_global_L to break the degeneracy of the 0 = 0 residual.',
    '# Set to 0.0 to disable.',
    'ZERO_FLOW_REG_EPS = 1e-12',
    '',
]

# --- Solver wrapper (IT-4d) ---
# Robustness: the residual can become degenerate when flow is near-zero (e.g.
# at t=0 with a cold-ish IC), in which case the residual is at machine-epsilon
# scale and scipy reports "not making progress" even though we're already at a
# valid root. We accept any result whose residual norm is below
# RES_ACCEPT_TOL, even if sol.success is False. If nothing converges, we fall
# back to the last known-good H_means — this degrades gracefully rather than
# crashing mid-integration.
lines.extend([
    'from scipy.optimize import least_squares',
    '',
    'RES_ACCEPT_TOL = 1e-10  # accept any x with ||F(x)|| below this',
    'H_MIN, H_MAX = 0.0, 1.0  # physical bounds on hematocrit',
    '_H_LO = np.full(len(iter_unknown_names), H_MIN)',
    '_H_HI = np.full(len(iter_unknown_names), H_MAX)',
    '',
    'def _solve_iterative(t, y):',
    '    """Solve the iterative H_mean fixed point at (t, y). Returns H_means array.',
    '    ',
    '    Uses scipy.optimize.least_squares with bounds [0, 1] on every H_mean.',
    '    This handles the common case where Jacobian-probing perturbations by',
    '    the ODE integrator produce states where the algebraic balance has no',
    '    exact root in [0, 1] (the bounded minimizer returns the best feasible',
    '    answer rather than wandering to spurious unbounded roots like H=1.0).',
    '    ',
    '    Warm-starts from _iter_last_solution for speed.',
    '    """',
    '    x0 = np.clip(_iter_last_solution[0], H_MIN, H_MAX)',
    '    # Levenberg-Marquardt under bounds via trust region reflective.',
    '    sol = least_squares(_iter_residual, x0, args=(t, y),',
    '                        bounds=(_H_LO, _H_HI),',
    '                        method="trf", xtol=1e-12, ftol=1e-12,',
    '                        max_nfev=50)',
    '    if sol.success or np.linalg.norm(sol.fun) < RES_ACCEPT_TOL:',
    '        _iter_last_solution[0] = sol.x.copy()',
    '        return sol.x',
    '    # Retry from CSV initial guess if warm start struggled.',
    '    sol2 = least_squares(_iter_residual, _iter_initial_guess, args=(t, y),',
    '                         bounds=(_H_LO, _H_HI),',
    '                         method="trf", xtol=1e-12, ftol=1e-12,',
    '                         max_nfev=50)',
    '    best = sol2 if np.linalg.norm(sol2.fun) < np.linalg.norm(sol.fun) else sol',
    '    if not hasattr(_solve_iterative, "_warned"):',
    '        _solve_iterative._warned = set()',
    '    key = round(t, 6)',
    '    if key not in _solve_iterative._warned:',
    '        import sys as _sys',
    '        print(f"[iter] t={t:.4g}: bounded LS imperfect, ||res||={np.linalg.norm(best.fun):.2e}",',
    '              file=_sys.stderr)',
    '        _solve_iterative._warned.add(key)',
    '    _iter_last_solution[0] = best.x.copy()',
    '    return best.x',
    '',
])
# --- end iterative section ---------------------------------------------------

lines.extend([
    '# State names',
    'state_names = [',
])
for sname, _ in state_list:
    lines.append(f"    '{sname}',")

lines.extend([
    ']',
    '',
    '# Initial conditions',
    'y0 = np.array([',
])
for _, init_val in state_list:
    lines.append(f"    {init_val},")

lines.extend([
    '])',
    '',
    'def ode_rhs(t, y):',
    '    """RHS for solve_ivp. Solves iterative H_mean, then evaluates ODEs.',
    '    ',
    '    IT-6: fast path — the algebraic block is INLINED below (no eval, no',
    '    shared helper call). All algebraics are bound as local variables so',
    '    the ODE RHS expressions can reference them directly.',
    '    """',
    '    # IT-4: resolve the algebraic cycle before evaluating ODE RHSes.',
    '    H_means = _solve_iterative(t, y)',
])
# Inline state unpack + H_means + all algebraics. All downstream references
# (state names, algebraic names, H_means) resolve to these locals.
_emit_algebraic_body(lines, emit_H_means=True)
lines.extend([
    '',
    '    # ODE right-hand sides',
    '    dydt = np.zeros(len(y))',
])
for i, (state_name, _) in enumerate(state_list):
    for ode_state, ode_rhs_expr in ode_equations:
        if ode_state == state_name:
            # Emit the ODE RHS expression directly; every name it can
            # reference (state vars, algebraics, H_means, module-level params)
            # is in scope. No eval, no dict lookup.
            lines.append(f'    dydt[{i}] = {ode_rhs_expr}')
            break
lines.extend([
    '    return dydt',
    '',
    'def compute_algebraics(t, y):',
    '    """Compute all algebraic variables at a given time point.',
    '    ',
    '    Returns a dict of algebraic name -> value. Uses the same inlined',
    '    evaluation path as ode_rhs (IT-6), so diagnostics are consistent.',
    '    """',
    '    H_means = _solve_iterative(t, y)',
])
_emit_algebraic_body(lines, emit_H_means=True)
lines.extend([
    '',
    '    # Package everything the caller might ask for into a dict.',
    '    out = {}',
])
# Direct variable references (not dict lookups) — all names are locals now.
for lhs, _ in all_equations:
    lines.append(f'    out["{lhs}"] = {lhs}')
for n in iter_unknown_names:
    lines.append(f'    out["{n}"] = {n}')
lines.extend([
    '    return out',
    '',
])

with open(OUTPUT, 'w') as f:
    f.write('\n'.join(lines))

print(f"\nGenerated {OUTPUT}")
print("Run with: python3 generated_model.py")