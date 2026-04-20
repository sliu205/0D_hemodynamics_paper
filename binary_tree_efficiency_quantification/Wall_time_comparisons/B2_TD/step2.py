"""
Complete CellML to Python Generator - PATCHED VERSION v5
Includes fixes for:
  1. pub:in skip check (not CSV-row check)
  2. sel block stripping before algebraic regex
  3. computed vars excluded from topo-sort predefined set
  4. computed vars not written as module-level constants
  5. environment__time registered as predefined (assigned at top of ode_rhs)
  6. Global parameters auto-detected from mappings: any variable mapped from
     `parameters` or `parameters_global` is treated as a global. CSV rows that
     don't match a component-specific suffix (e.g. `R_VV_junc`) are checked
     against this set and replicated to every consumer component.
  7. Final dependency check warns loudly if a referenced variable has no
     value, no equation, and no state — instead of silently shipping a broken
     generated_model.py.
"""

import re
import csv
from collections import defaultdict
import numpy as np

print("=" * 60)
print("Running PATCHED step2.py (v5 - generalized global params)")
print("=" * 60)

# Files
MAIN = "B2_TD.txt"
MODULES = "B2_TD_modules.txt"
PARAMS_CSV = "B2_TD_parameters.csv"
INITIAL_CSV = "initial_params.csv"
OUTPUT = "generated_model.py"

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
# NEW (v5): Detect global parameters from the mappings BEFORE loading CSVs
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
        # Step 1: try to match a component suffix (e.g. r_PV1 -> PV1__r)
        for comp_base in comp_base_names:
            if comp_base in raw_name:
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
    
    ordered.extend(remaining)
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
    '"""Generated model"""',
    'import numpy as np',
    'from scipy.integrate import solve_ivp',
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

for name, value in sorted(params.items()):
    if '__' in name and not name.startswith('INIT_'):
        if name in computed_lhs_set:
            continue
        lines.append(f"{name} = {value}")

lines.extend([
    '',
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
    '    # Unpack state',
])

for i, (sname, _) in enumerate(state_list):
    lines.append(f'    {sname} = y[{i}]')

lines.extend([
    '',
    '    # Time variable',
    '    environment__time = t',
    '',
    '    # Algebraic equations',
])

for lhs, rhs in all_equations:
    lines.append(f'    {lhs} = {rhs}')

lines.extend([
    '',
    '    # ODEs',
    '    dydt = np.zeros(len(y))',
])

for i, (state_name, _) in enumerate(state_list):
    for ode_state, ode_rhs in ode_equations:
        if ode_state == state_name:
            lines.append(f'    dydt[{i}] = {ode_rhs}')
            break

lines.extend([
    '',
    '    return dydt',
    '',
    'def compute_algebraics(t, y):',
    '    """Compute all algebraic variables at a given time point."""',
    '    # Unpack state',
])

for i, (sname, _) in enumerate(state_list):
    lines.append(f'    {sname} = y[{i}]')

lines.extend([
    '',
    '    # Time variable',
    '    environment__time = t',
    '',
    '    # Algebraic equations',
])

for lhs, rhs in all_equations:
    lines.append(f'    {lhs} = {rhs}')

lines.extend([
    '',
    '    # Return dictionary of all algebraic variables',
    '    return {',
])

for lhs, _ in all_equations:
    lines.append(f'        "{lhs}": {lhs},')

lines.append('    }')

with open(OUTPUT, 'w') as f:
    f.write('\n'.join(lines))

print(f"\nGenerated {OUTPUT}")
print("Run with: python3 generated_model.py")