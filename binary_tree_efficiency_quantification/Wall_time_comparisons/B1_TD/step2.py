"""
Complete CellML to Python Generator - Simple Working Version
"""

import re
import csv
from collections import defaultdict
import numpy as np

# Files
MAIN = "B1_TD.txt"
MODULES = "B1_TD_modules.txt"
PARAMS_CSV = "B1_TD_parameters.csv"
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
        # Skip if this variable already has a parameter value
        if lhs_name in param_vars:
            continue
        ns_rhs = rhs
        for var in tmpl['vars']:
            ns_rhs = re.sub(rf'\b{var}\b', f'{comp_base}__{var}', ns_rhs)
        all_equations.append((lhs_name, ns_rhs))
    
    # sel/case equations
    for lhs, rhs in tmpl.get('sel', []):
        lhs_name = f"{comp_base}__{lhs}"
        # Skip if this variable already has a parameter value
        if lhs_name in param_vars:
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
    e = e.replace('pow(', 'np.power(')
    e = e.replace('exp(', 'np.exp(')
    e = e.replace('abs(', 'np.abs(')
    e = e.replace('ln(', 'np.log(')
    e = e.replace('atan(', 'np.arctan(')
    e = re.sub(r'\bpi\b', 'np.pi', e)
    # Fix integer literals in np.power to be floats
    e = re.sub(r'np\.power\((\d+),', r'np.power(\1.0,', e)
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
            if remaining:
                # Show first few problematic equations
                for lhs, rhs in remaining[:3]:
                    deps = set(re.findall(r'\b([a-zA-Z_]\w*__\w+)\b', rhs))
                    unmet = deps - defined
                    print(f"    {lhs} depends on: {unmet}")
            break
    
    # Add remaining (circular dependencies) at the end
    ordered.extend(remaining)
    return ordered

# State variables and parameters are already defined
# Include ALL parameter names (even if they're for states)
predefined = set()
for name in params.keys():
    if '__' in name and not name.startswith('INIT_'):
        predefined.add(name)
# Add state variable names
for s, _ in state_list:
    predefined.add(s)

print(f"Predefined variables: {len(predefined)}")
# Check if the problematic ones are there
for check in ['inlet__v', 'inlet__v_scale', 'inlet__v_d', 'VV_junc1__w_in2']:
    if check in predefined:
        print(f"  ✓ {check}")
    else:
        print(f"  ✗ {check} MISSING")

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
    '# Parameters',
]

# Write all parameters
state_names = {s for s, _ in state_list}

for name, value in sorted(params.items()):
    if '__' in name and not name.startswith('INIT_'):
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
    'if __name__ == "__main__":',
    '    print("Running simulation...")',
    '    print(f"Initial conditions: {y0[:5]}...")',
    '    ',
    '    # Test at t=0',
    '    try:',
    '        dydt0 = ode_rhs(0, y0)',
    '        print(f"RHS at t=0: {dydt0[:5]}...")',
    '        if np.any(np.isnan(dydt0)) or np.any(np.isinf(dydt0)):',
    '            print("ERROR: NaN or Inf in initial RHS!")',
    '            import sys',
    '            sys.exit(1)',
    '    except Exception as e:',
    '        print(f"ERROR evaluating RHS at t=0: {e}")',
    '        import sys',
    '        sys.exit(1)',
    '    ',
    '    sol = solve_ivp(',
    '        ode_rhs,',
    '        [0, 1000],',
    '        y0,',
    '        method="BDF",  # More robust for stiff systems',
    '        t_eval=np.linspace(0, 1000, 1001),  # Fewer points initially',
    '        rtol=1e-6,  # Looser tolerances',
    '        atol=1e-9,',
    '    )',
    '    if sol.success:',
    '        print(f"Success! {sol.t.shape[0]} points")',
    '        print(f"Final state: {sol.y[:, -1][:5]}...")',
    '    else:',
    '        print(f"Failed: {sol.message}")',
])

with open(OUTPUT, 'w') as f:
    f.write('\n'.join(lines))

print(f"\nGenerated {OUTPUT}")
print("Run with: python3 generated_model.py")