"""
Complete CellML to Python Generator - PATCHED VERSION v4
Includes fixes for:
  1. pub:in skip check (not CSV-row check)
  2. sel block stripping before algebraic regex
  3. computed vars excluded from topo-sort predefined set
  4. computed vars not written as module-level constants
  5. environment__time registered as predefined (assigned at top of ode_rhs)
"""

import re
import csv
from collections import defaultdict
import numpy as np

print("=" * 60)
print("Running PATCHED step2.py (v4 - environment__time fix)")
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
def parse_template(text, name):
    # Find this template
    match = re.search(rf'def\s+comp\s+{name}\s+as(.*?)enddef', text, re.DOTALL)
    if not match:
        return None
    body = match.group(1)
    
    # Variables - track which are pub:in (constants) vs pub:out (computed)
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
    
    # ODEs
    clean = re.sub(r'//.*', '', body)
    clean = re.sub(r'var\s+\w+[^;]*;', '', clean)
    
    odes = []
    for m in re.finditer(r'ode\s*\(\s*(\w+)\s*,\s*\w+\s*\)\s*=(.*?);', clean, re.DOTALL):
        state = m.group(1).strip()
        rhs = m.group(2).strip()
        odes.append((state, rhs))
    
    # Algebraic equations - ONLY for variables that are NOT pub:in
    clean2 = re.sub(r'ode\s*\([^)]+\)\s*=[^;]*;', '', clean, flags=re.DOTALL)
    # Also strip sel/case blocks — they're parsed separately below. If left in,
    # the algebraic regex below would match partial content inside them (e.g.
    # "X = sel\n case cond: val_a" captured up to the first ";"), polluting the
    # algebraic equation list with garbage.
    clean2 = re.sub(r'\w+\s*=\s*sel\s*.*?endsel\s*;', '', clean2, flags=re.DOTALL)
    alg = []
    for m in re.finditer(r'(\w+)\s*=(.*?);', clean2, re.DOTALL):
        lhs = m.group(1).strip()
        rhs = m.group(2).strip()
        # Only include if it's a variable we know about and NOT an input
        if lhs in vars_info and not vars_info[lhs]['is_input'] and lhs != 't':
            alg.append((lhs, rhs))
    
    # sel/case statements
    sel_cases = []
    for m in re.finditer(r'(\w+)\s*=\s*sel\s*(.*?)endsel\s*;', body, re.DOTALL):
        lhs = m.group(1).strip()
        cases_text = m.group(2).strip()
        # Only if not an input variable
        if lhs in vars_info and not vars_info[lhs]['is_input']:
            # Parse case statements
            cases = re.findall(r'case\s+(.*?)\s*:\s*(.*?)(?=case\s|$)', cases_text, re.DOTALL)
            # Convert to ternary
            ternary = convert_cases_to_ternary(cases)
            sel_cases.append((lhs, ternary))
    
    return {'vars': vars_info, 'odes': odes, 'alg': alg, 'sel': sel_cases}

def convert_cases_to_ternary(cases):
    """Convert CellML case statements to Python ternary."""
    if not cases:
        return '0.0'
    cond, val = cases[0]
    cond = cond.strip()
    val = val.strip().rstrip(';')
    if cond.lower() == 'true':
        return val
    # Convert condition
    cond = cond.replace('==', ' == ').replace('>=', ' >= ').replace('<=', ' <= ')
    cond = re.sub(r'\s+', ' ', cond).strip()
    # Recurse for remaining cases
    if len(cases) > 1:
        return f"({val} if {cond} else {convert_cases_to_ternary(cases[1:])})"
    else:
        return f"({val} if {cond} else 0.0)"

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
# 3. Load parameters from CSVs
# ==============================================================================
params = {}

# From B1_TD_parameters.csv
with open(PARAMS_CSV) as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_name = row['variable_name'].strip()
        value = row['value'].strip()
        
        matched = False
        for comp_base in comp_base_names:
            if comp_base in raw_name:
                var_part = raw_name.replace(f'_{comp_base}', '').replace(f'{comp_base}_', '')
                if var_part and var_part != raw_name:
                    params[f"{comp_base}__{var_part}"] = value
                    matched = True
                    break
        
        if not matched:
            params[raw_name] = value

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
            
            # If it's a global parameter, replicate it for each component
            if var.startswith('global/'):
                var_name = var.replace('global/', '')
                for comp_base in comp_base_names:
                    if comp_base not in ['parameters', 'parameters_global', 'global']:
                        params[f"{comp_base}__{var_name}"] = value
        elif cat == 'state':
            # Store initial conditions separately
            py_name = var.replace('/', '__').replace('_module', '')
            params[f"INIT_{py_name}"] = value

print(f"Loaded {len(params)} parameters")

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
        # Get initial value
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

# Get set of variables that are already parameters (have values)
param_vars = {name for name in params.keys() if '__' in name and not name.startswith('INIT_')}

for comp_inst, tmpl in templates.items():
    comp_base = comp_inst.replace('_module', '')
    
    # Skip parameter holder components - they don't have real equations
    if comp_base in ['parameters', 'parameters_global']:
        continue
    
    # ODEs
    for state_var, rhs in tmpl['odes']:
        state_name = f"{comp_base}__{state_var}"
        # Namespace the RHS
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        ode_equations.append((state_name, ns_rhs))
    
    # Algebraic
    for lhs, rhs in tmpl['alg']:
        lhs_name = f"{comp_base}__{lhs}"
        # Only skip if this variable is a true input (pub:in) — NOT just because
        # it happens to have a row in the parameters CSV. Computed outputs
        # (pub:out) must keep their governing equations; any CSV value for
        # them is just a default/initial guess and should be overridden.
        if tmpl['vars'].get(lhs, {}).get('is_input', False):
            continue
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        all_equations.append((lhs_name, ns_rhs))
    
    # sel/case equations
    for lhs, rhs in tmpl.get('sel', []):
        lhs_name = f"{comp_base}__{lhs}"
        # Same rule as above: only skip true inputs.
        if tmpl['vars'].get(lhs, {}).get('is_input', False):
            continue
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        # Remove any duplicate algebraic equation for this variable
        all_equations = [(l, r) for l, r in all_equations if l != lhs_name]
        all_equations.append((lhs_name, ns_rhs))

# Apply variable mappings to replace mapped variables
def apply_mappings(expr, var_mappings):
    """Replace variables in expression according to mappings.
    Apply in two phases:
    1. Component-to-component connections
    2. Remove parameters/parameters_global references
    """
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
    e = e.replace('pow(', 'safe_power(')  # Use safe_power instead
    e = e.replace('exp(', 'np.exp(')
    e = e.replace('abs(', 'np.abs(')
    e = e.replace('ln(', 'np.log(')
    e = e.replace('atan(', 'np.arctan(')
    e = re.sub(r'\bpi\b', 'np.pi', e)
    # Fix integer literals in safe_power to be floats
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
    """Simple topological sort - defined_vars are already available."""
    # Start with provided defined vars
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
            # Find all variables used in RHS
            deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
            # Check if all dependencies are satisfied
            unmet = deps - defined
            if not unmet:
                ordered.append((lhs, rhs))
                defined.add(lhs)  # Now THIS variable is defined
                progress = True
            else:
                next_rem.append((lhs, rhs))
        
        remaining = next_rem
        if not progress:
            print(f"  WARNING: Topological sort stuck at iteration {iteration}")
            print(f"  Remaining equations: {len(remaining)}")
            # Detailed diagnostic: find equations that have MINIMUM unmet deps
            # — these show the true "root" of the blockage.
            rem_with_unmet = []
            for lhs, rhs in remaining:
                deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
                unmet = deps - defined
                rem_with_unmet.append((lhs, rhs, unmet))
            rem_with_unmet.sort(key=lambda x: len(x[2]))
            print(f"  --- First 10 stuck equations (fewest unmet deps first) ---")
            stuck_lhs = {x[0] for x in rem_with_unmet}
            for lhs, rhs, unmet in rem_with_unmet[:10]:
                # Classify each unmet dep
                cat = []
                for u in sorted(unmet):
                    if u in stuck_lhs:
                        cat.append(f"{u}[STUCK]")
                    else:
                        cat.append(f"{u}[TRULY-MISSING]")
                print(f"    {lhs}:")
                print(f"      RHS: {rhs[:120]}")
                print(f"      unmet: {cat}")
            # Also print all the TRULY-MISSING names (ones that aren't in `defined`
            # and aren't in `pending` either — i.e. nothing ever resolves them)
            truly_missing = set()
            for _, _, unmet in rem_with_unmet:
                truly_missing |= (unmet - stuck_lhs)
            if truly_missing:
                print(f"  --- Variables referenced but never defined: {len(truly_missing)} ---")
                for tm in sorted(truly_missing)[:30]:
                    print(f"    {tm}")
            break
    
    # Add remaining (circular dependencies) at the end
    ordered.extend(remaining)
    return ordered

# State variables and parameters are already defined
# Include ALL parameter names EXCEPT those that will be recomputed by an
# algebraic equation — if a variable is on the LHS of an equation we're about
# to emit inside ode_rhs, it's NOT predefined (it needs to be topo-sorted).
computed_lhs = {lhs for lhs, _ in all_equations}

predefined = set()
for name in params.keys():
    if '__' in name and not name.startswith('INIT_'):
        if name in computed_lhs:
            continue  # will be computed inside ode_rhs
        predefined.add(name)
# Add state variable names
for s, _ in state_list:
    predefined.add(s)
# The simulation time `environment__time` is assigned at the top of ode_rhs
# (as `environment__time = t`), so it's available to every equation. The topo
# sort doesn't know this on its own, so tell it explicitly.
predefined.add('environment__time')

print(f"Predefined variables: {len(predefined)}")
# Check if the problematic ones are there
for check in ['inlet__v', 'inlet__v_scale', 'inlet__v_d', 'VV_junc1__w_in2']:
    if check in predefined:
        print(f"  ✓ {check}")
    else:
        print(f"  ✗ {check} MISSING")

# Diagnostic: verify that equations we expect to be computed actually exist
print("--- computed_lhs membership check ---")
for check in ['PV1__v', 'PV1__u', 'PV1__R', 'VV_junc1__u_d', 'VV_junc1__vj3',
              'VV_junc1__H_from1', 'VV_junc1__H_from1_target']:
    in_computed = check in computed_lhs
    in_predef   = check in predefined
    print(f"  {check}: computed_lhs={in_computed}  predefined={in_predef}")
# Also verify PV1__v's RHS survived all transforms
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

# Write all parameters
state_names = {s for s, _ in state_list}
# Variables that get recomputed inside ode_rhs — don't emit a module-level
# value for them. Python would make them function-local anyway once they're
# assigned inside ode_rhs, so a top-level value would be misleading/unused.
computed_lhs_set = {lhs for lhs, _ in all_equations}

for name, value in sorted(params.items()):
    if '__' in name and not name.startswith('INIT_'):
        if name in computed_lhs_set:
            continue  # will be computed inside ode_rhs
        # Write ALL parameters - they'll be overridden if computed later
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

# Add all algebraic variables to return dict
for lhs, _ in all_equations:
    lines.append(f'        "{lhs}": {lhs},')

lines.append('    }')

# Don't include the if __name__ == "__main__" block in generated model
# Let run_generated_model.py handle execution

with open(OUTPUT, 'w') as f:
    f.write('\n'.join(lines))

print(f"\nGenerated {OUTPUT}")
print("Run with: python3 generated_model.py")