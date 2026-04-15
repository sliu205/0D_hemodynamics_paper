"""
cellml_to_python.py
===================
Reads a B1_TD-style CellML model (text format) and its modules file,
then writes a self-contained Python/NumPy ODE model with:
  - All variables namespaced as  <comp>__<var>
  - Inter-component mappings resolved (aliases collapsed)
  - ode() calls converted to a dydt vector
  - Algebraic equations as plain assignments
  - A scipy.integrate.solve_ivp driver at the bottom

Configure the paths in the CONFIG block below, then run:
    python cellml_to_python.py
"""

import re
import sys
from collections import defaultdict

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG  —  edit these paths before running
# ══════════════════════════════════════════════════════════════════════════════

MAIN_CELLML    = "B1_TD.txt"            # main model file
MODULES_CELLML = "B1_TD_modules.txt"    # modules/components file
PARAMS_FILE    = "B1_TD_params.py"                 # optional: "model_params.py" or None
OUTPUT_FILE    = "generated_model.py"   # where to write the output

# ══════════════════════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────────────────────────────
# 1.  PARSE THE MAIN MODEL FILE  (B1_TD.txt)
# ──────────────────────────────────────────────────────────────────────────────

def parse_main_model(text):
    """
    Returns:
      comp_to_module : dict  comp_name -> module_template_name
      access_comps   : set of accessor/shim component names
      mappings       : list of (comp_a, var_a, comp_b, var_b)
    """

    # ── component → module template ──────────────────────────────────────────
    comp_to_module = {}
    for m in re.finditer(r'comp\s+(\w+)\s+using\s+comp\s+(\w+)\s*;', text):
        comp_to_module[m.group(1)] = m.group(2)

    # ── accessor shim components (pub:in only, no odes) ───────────────────────
    access_comps = set()
    for m in re.finditer(r'def\s+comp\s+(\w+)\s+as\s+(.*?)enddef', text, re.DOTALL):
        cname = m.group(1)
        body  = m.group(2)
        if ('pub: in' in body and 'pub: out' not in body
                and 'ode(' not in body
                and cname not in ('environment', 'terminal_venous_connection',
                                  'generic_junction_connection',
                                  'sum_blood_volume')):
            access_comps.add(cname)

    # ── map blocks ────────────────────────────────────────────────────────────
    mappings = []
    for block in re.finditer(
            r'def\s+map\s+between\s+(\w+)\s+and\s+(\w+)\s+for(.*?)enddef',
            text, re.DOTALL):
        ca, cb = block.group(1), block.group(2)
        for pair in re.finditer(r'vars\s+(\w+)\s+and\s+(\w+)\s*;',
                                block.group(3)):
            mappings.append((ca, pair.group(1), cb, pair.group(2)))

    return comp_to_module, access_comps, mappings


# ──────────────────────────────────────────────────────────────────────────────
# 2.  PARSE THE MODULES FILE  (B1_TD_modules.txt)
# ──────────────────────────────────────────────────────────────────────────────

def parse_modules(text):
    """
    Returns dict: template_name -> {
        'vars'  : { var_name: {'init': str|None, 'pub': str|None} },
        'odes'  : [ (state_var, rhs_expr) ],
        'alg'   : [ (lhs_var,  rhs_expr) ],
        'raw'   : str
    }
    """
    templates = {}
    for m in re.finditer(r'def\s+comp\s+(\w+)\s+as(.*?)enddef', text, re.DOTALL):
        name = m.group(1)
        body = m.group(2)
        if name in ('zero_flow',):
            continue
        templates[name] = _parse_comp_body(name, body)
    return templates


def _parse_comp_body(name, body):
    # ── variable declarations ─────────────────────────────────────────────
    var_info = {}
    for m in re.finditer(r'var\s+(\w+)\s*:\s*\w+(?:\s*\{([^}]*)\})?\s*;', body):
        vname = m.group(1)
        attrs = m.group(2) or ''
        init_m = re.search(r'init:\s*([^,;}]+)', attrs)
        pub_m  = re.search(r'pub:\s*(\w+)',      attrs)
        var_info[vname] = {
            'init': init_m.group(1).strip() if init_m else None,
            'pub' : pub_m.group(1).strip()  if pub_m  else None,
        }

    # ── strip comments and var declarations ──────────────────────────────
    clean = re.sub(r'//.*', '', body)
    clean = re.sub(r'var\s+\w+\s*:\s*\w+[^;]*;', '', clean)

    # ── ODE statements  ode(state, t) = rhs; ─────────────────────────────
    odes = []
    for m in re.finditer(r'ode\s*\(\s*(\w+)\s*,\s*\w+\s*\)\s*=(.*?);',
                          clean, re.DOTALL):
        odes.append((m.group(1).strip(), _clean_expr(m.group(2))))
    clean2 = re.sub(r'ode\s*\([^)]+\)\s*=.*?;', '', clean, flags=re.DOTALL)

    # ── plain assignments  lhs = rhs; ────────────────────────────────────
    alg = []
    for m in re.finditer(r'(\w+)\s*=(.*?);', clean2, re.DOTALL):
        lhs = m.group(1).strip()
        rhs = _clean_expr(m.group(2))
        if lhs and rhs:
            alg.append((lhs, rhs))

    return {'vars': var_info, 'odes': odes, 'alg': alg, 'raw': body}


def _clean_expr(expr):
    """Convert CellML expression syntax to Python/NumPy."""
    e = expr.strip()
    e = re.sub(r'\{[^}]+\}', '', e)      # remove unit annotations
    e = e.replace('sqr(',    'np.square(')
    e = e.replace('pow(',    'np.power(')
    e = e.replace('exp(',    'np.exp(')
    e = e.replace('abs(',    'np.abs(')
    e = e.replace('ln(',     'np.log(')
    e = e.replace('atan(',   'np.arctan(')
    e = e.replace('min(',    'np.minimum(')
    e = e.replace('max(',    'np.maximum(')
    e = re.sub(r'\bpi\b',    'np.pi', e)
    e = re.sub(r'\s+', ' ', e).strip()
    return e


# ──────────────────────────────────────────────────────────────────────────────
# 3.  RESOLVE VARIABLE MAPPINGS
# ──────────────────────────────────────────────────────────────────────────────

def build_alias_map(comp_to_module, access_comps, mappings):
    module_instances = set(comp_to_module.keys())
    shim_to_mod = {}
    inter_mod   = {}

    for ca, va, cb, vb in mappings:
        a_is_mod = ca in module_instances
        b_is_mod = cb in module_instances
        if a_is_mod and b_is_mod:
            inter_mod[(ca, va)] = (cb, vb)
            inter_mod[(cb, vb)] = (ca, va)
        elif ca in access_comps and b_is_mod:
            shim_to_mod[(ca, va)] = (cb, vb)
        elif cb in access_comps and a_is_mod:
            shim_to_mod[(cb, vb)] = (ca, va)

    return shim_to_mod, inter_mod


def ns(comp, var):
    """Namespace a variable: comp__var (strip trailing _module)."""
    cname = re.sub(r'_module$', '', comp)
    return f"{cname}__{var}"


# ──────────────────────────────────────────────────────────────────────────────
# 4.  BUILD INTER-MODULE SUBSTITUTION MAP
# ──────────────────────────────────────────────────────────────────────────────

def build_substitution_maps(comp_to_module, inter_mod, templates):
    subs = defaultdict(dict)
    for (ca, va), (cb, vb) in inter_mod.items():
        tmpl_a = comp_to_module.get(ca)
        tmpl_b = comp_to_module.get(cb)
        # Skip if either side has no module template (e.g. parameters,
        # parameters_global, environment — wired in map blocks but not
        # equation-bearing components in the modules file).
        if not tmpl_a or not tmpl_b:
            continue
        if tmpl_a not in templates or tmpl_b not in templates:
            continue
        info_a = templates[tmpl_a]['vars'].get(va, {})
        info_b = templates[tmpl_b]['vars'].get(vb, {})
        if info_a.get('pub') == 'out' and info_b.get('pub') == 'in':
            subs[cb][vb] = ns(ca, va)
        elif info_b.get('pub') == 'out' and info_a.get('pub') == 'in':
            subs[ca][va] = ns(cb, vb)
    return subs


# ──────────────────────────────────────────────────────────────────────────────
# 5.  CONVERT sel/case TO PYTHON TERNARY CHAINS
# ──────────────────────────────────────────────────────────────────────────────

def convert_sel_cases(raw_body, comp_prefix):
    results = []
    for m in re.compile(r'(\w+)\s*=\s*sel\s*(.*?)endsel\s*;',
                        re.DOTALL).finditer(raw_body):
        lhs   = m.group(1).strip()
        parts = re.findall(
            r'case\s+(.*?)\s*:\s*(.*?)(?=case\s|$)',
            m.group(2).strip(), re.DOTALL)
        results.append((lhs, _cases_to_ternary(parts)))
    return results


def _cases_to_ternary(parts):
    if not parts:
        return '0.0'
    cond, val = parts[0]
    cond = cond.strip()
    val  = _clean_expr(val.strip().rstrip(';'))
    if cond.lower() == 'true':
        return val
    py_cond = _convert_condition(cond)
    return f"({val} if {py_cond} else {_cases_to_ternary(parts[1:])})"


def _convert_condition(cond):
    c = re.sub(r'\{[^}]+\}', '', cond.strip())
    c = c.replace('==', ' == ').replace('>=', ' >= ').replace('<=', ' <= ')
    c = c.replace('and', ' and ')
    return re.sub(r'\s+', ' ', c).strip()


# ──────────────────────────────────────────────────────────────────────────────
# 6.  TOPOLOGICAL SORT OF ALGEBRAIC EQUATIONS
# ──────────────────────────────────────────────────────────────────────────────

def topo_sort(equations, state_vars=None, param_vars=None):
    """
    Topologically sort algebraic equations.
    Returns: (ordered_equations, circular_equations)
    
    state_vars: set of state variable names that are already defined (from y vector)
    param_vars: set of parameter names that are already defined (from params file)
    """
    if state_vars is None:
        state_vars = set()
    if param_vars is None:
        param_vars = set()
    
    defined   = set(state_vars) | set(param_vars)  # Both states and params are pre-defined
    ordered   = []
    remaining = list(equations)
    skip_kw   = {'np', 't', 'True', 'False', 'if', 'else', 'and', 'or',
                 'not', 'minimum', 'maximum', 'power', 'square', 'exp',
                 'log', 'abs', 'arctan', 'pi'}

    max_iterations = len(remaining) * 2  # Allow more iterations for complex dependencies
    
    for iteration in range(max_iterations):
        if not remaining:
            break
        next_rem = []
        progress_made = False
        
        for lhs, rhs in remaining:
            deps  = set(re.findall(r'\b([a-zA-Z_]\w*)\b', rhs))
            unmet = {d for d in deps
                     if d not in defined
                     and not d.startswith('np')
                     and d not in skip_kw}
            if not unmet:
                ordered.append((lhs, rhs))
                defined.add(lhs)
                progress_made = True
            else:
                next_rem.append((lhs, rhs))
        
        remaining = next_rem
        
        # If we made no progress, we have a circular dependency
        if not progress_made and remaining:
            break

    # Return both ordered and circular equations separately
    circular = []
    if remaining:
        print(f"WARNING: {len(remaining)} equations have circular dependencies and will be solved iteratively")
        for lhs, rhs in remaining:
            deps = set(re.findall(r'\b([a-zA-Z_]\w*)\b', rhs))
            unmet = {d for d in deps if d not in defined and not d.startswith('np') and d not in skip_kw}
            if unmet:  # Only print if there are truly undefined variables
                print(f"  {lhs} depends on: {unmet}")
            circular.append((lhs, rhs))
            defined.add(lhs)  # Add to defined so we can continue

    return ordered, circular


# ──────────────────────────────────────────────────────────────────────────────
# 7.  NAMESPACE AN EXPRESSION
# ──────────────────────────────────────────────────────────────────────────────

NUMPY_FUNCS = {
    'np', 'minimum', 'maximum', 'power', 'square', 'exp', 'log', 'abs',
    'arctan', 'pi', 'zeros', 'array', 'linspace',
}
PYTHON_KW = {
    'if', 'else', 'elif', 'and', 'or', 'not', 'True', 'False', 'None',
    'in', 'is', 'return', 'for', 'while', 'import', 'from', 'def', 'class',
}


def _namespace_expr(expr, comp_inst, inter_subs, local_vars):
    full_subs = {}
    for bare, mapped in inter_subs.items():
        full_subs[bare] = mapped
    for vname in local_vars:
        if vname not in full_subs:
            full_subs[vname] = ns(comp_inst, vname)

    result = expr
    for k in sorted(full_subs.keys(), key=len, reverse=True):
        if k in NUMPY_FUNCS or k in PYTHON_KW or k == 't':
            continue
        result = re.sub(rf'\b{re.escape(k)}\b', full_subs[k], result)

    return result


# ──────────────────────────────────────────────────────────────────────────────
# 8.  MAIN CODE GENERATION
# ──────────────────────────────────────────────────────────────────────────────

def generate_python_model(main_text, modules_text, params_file=None):

    comp_to_module, access_comps, mappings = parse_main_model(main_text)
    templates = parse_modules(modules_text)
    shim_to_mod, inter_mod = build_alias_map(comp_to_module, access_comps, mappings)
    subs_map = build_substitution_maps(comp_to_module, inter_mod, templates)

    param_subs = defaultdict(dict)
    for ca, va, cb, vb in mappings:
        if ca in ('parameters', 'parameters_global') and cb in comp_to_module:
            param_subs[cb][vb] = va
        elif cb in ('parameters', 'parameters_global') and ca in comp_to_module:
            param_subs[ca][va] = vb

    lines = []

    # ── Extract parameter names ──────────────────────────────────────────
    param_names = set()
    if params_file:
        try:
            with open(params_file) as f:
                ptext = f.read()
            for pl in ptext.splitlines():
                m = re.match(r'^\s*(\w+__\w+)\s*=', pl)
                if m:
                    param_names.add(m.group(1))
        except FileNotFoundError:
            pass
    
    # Also add parameters that are mapped through param_subs
    # These are variables in components that are mapped to global parameters
    for comp_inst, param_map in param_subs.items():
        for local_var, param_name in param_map.items():
            # The local variable in the component will refer to the parameter
            # So mark it as defined
            full_name = ns(comp_inst, local_var)
            param_names.add(full_name)
            # Also add the parameter name itself (in case it's referenced directly)
            param_names.add(param_name)

    # ── header ───────────────────────────────────────────────────────────
    lines += [
        '"""',
        'generated_model.py',
        '===================',
        'Auto-generated from CellML by cellml_to_python.py',
        'DO NOT EDIT BY HAND – re-run the generator instead.',
        '"""',
        '',
        'import numpy as np',
        'from scipy.integrate import solve_ivp',
        'import matplotlib.pyplot as plt',
        '',
    ]

    # ── parameters block ─────────────────────────────────────────────────
    if params_file:
        lines += [
            '# ================================================================',
            '# PARAMETERS  (from model_params.py)',
            '# ================================================================',
            f'# Generated from: {params_file}',
            '',
        ]
        try:
            with open(params_file) as f:
                ptext = f.read()
            for pl in ptext.splitlines():
                if re.match(r'^\s*\w+__\w+\s*=', pl) or pl.strip() == '':
                    lines.append(pl)
        except FileNotFoundError:
            lines.append(f'# WARNING: {params_file} not found')
        lines.append('')

    # ── state variables and initial conditions ───────────────────────────
    lines += [
        '# ================================================================',
        '# STATE VARIABLES  &  INITIAL CONDITIONS',
        '# ================================================================',
        '',
        'state_names = [',
    ]

    state_list    = []
    all_equations = []
    ode_equations = []

    for comp_inst, tmpl_name in comp_to_module.items():
        if tmpl_name not in templates:
            continue
        tmpl = templates[tmpl_name]
        comp_subs = dict(subs_map.get(comp_inst, {}))

        for local_v, param_v in param_subs.get(comp_inst, {}).items():
            for (shim, sv), (mi, mv) in shim_to_mod.items():
                if mi == comp_inst and mv == local_v:
                    comp_subs[local_v] = ns(shim, sv)
                    break

        for vname, vinfo in tmpl['vars'].items():
            if vinfo['init'] is not None:
                full_name = ns(comp_inst, vname)
                init_val  = vinfo['init']
                if re.match(r'^[A-Za-z_]', init_val):
                    init_val = (ns(comp_inst, init_val)
                                if init_val in tmpl['vars'] else init_val)
                state_list.append((full_name, init_val))
                lines.append(f"    '{full_name}',")

        for state_v, rhs in tmpl['odes']:
            ns_state = ns(comp_inst, state_v)
            ns_rhs   = _namespace_expr(rhs, comp_inst, comp_subs, tmpl['vars'])
            ode_equations.append((ns_state, ns_rhs))

        for lhs, rhs in tmpl['alg']:
            if lhs == 't':
                continue
            ns_lhs = ns(comp_inst, lhs)
            ns_rhs = _namespace_expr(rhs, comp_inst, comp_subs, tmpl['vars'])
            all_equations.append((ns_lhs, ns_rhs))

        for lhs, py_expr in convert_sel_cases(tmpl['raw'], comp_inst):
            if lhs == 't':
                continue
            ns_lhs  = ns(comp_inst, lhs)
            ns_expr = _namespace_expr(py_expr, comp_inst, comp_subs, tmpl['vars'])
            all_equations = [(l, r) for l, r in all_equations if l != ns_lhs]
            all_equations.append((ns_lhs, ns_expr))

    lines.append(']')
    lines.append('')

    lines.append('# Initial condition vector (order matches state_names)')
    lines.append('y0 = np.array([')
    for sname, sinit in state_list:
        lines.append(f'    {sinit},  # {sname}')
    lines.append('])')
    lines.append('')

    # ── ODE function ──────────────────────────────────────────────────────
    lines += [
        '# ================================================================',
        '# ODE FUNCTION',
        '# ================================================================',
        '',
        'def ode_rhs(t, y):',
        '    """',
        '    RHS of the ODE system.',
        '    State vector y is ordered as per state_names.',
        '    """',
        '    # -- unpack states -------------------------------------------',
    ]
    for i, (sname, _) in enumerate(state_list):
        lines.append(f'    {sname} = y[{i}]')
    lines.append('')

    state_var_names = {sname for sname, _ in state_list}
    sorted_alg, circular_alg = topo_sort(all_equations, state_var_names, param_names)

    lines.append('    # -- algebraic equations (auto-sorted) ---------------')
    for lhs, rhs in sorted_alg:
        lines.append(f'    {lhs} = {rhs}')
    lines.append('')

    if circular_alg:
        # Generate iterative solver for circular dependencies
        lines.append('    # -- circular algebraic equations (solved iteratively) --')
        lines.append('    # Initialize circular variables with guess values')
        for lhs, rhs in circular_alg:
            lines.append(f'    {lhs} = 0.0  # initial guess')
        lines.append('')
        lines.append('    # Fixed-point iteration to resolve circular dependencies')
        lines.append('    for _iter in range(10):  # max 10 iterations')
        for lhs, rhs in circular_alg:
            lines.append(f'        {lhs} = {rhs}')
        lines.append('')

    lines.append('    # -- assemble dydt -----------------------------------')
    lines.append('    dydt = np.zeros(len(y))')
    state_index = {sname: i for i, (sname, _) in enumerate(state_list)}
    for ns_state, ns_rhs in ode_equations:
        if ns_state in state_index:
            lines.append(f'    dydt[{state_index[ns_state]}] = {ns_rhs}  # d({ns_state})/dt')
        else:
            lines.append(f'    # WARNING: state {ns_state} not in state_list')
    lines.append('')
    lines.append('    return dydt')
    lines.append('')

    # ── solver driver ─────────────────────────────────────────────────────
    lines += [
        '# ================================================================',
        '# SOLVER DRIVER',
        '# ================================================================',
        '',
        'if __name__ == "__main__":',
        '    t_start = 0.0',
        '    t_end   = 1000.0',
        '    t_eval  = np.linspace(t_start, t_end, 10001)',
        '',
        '    print("Running simulation ...")',
        '    sol = solve_ivp(',
        '        ode_rhs,',
        '        [t_start, t_end],',
        '        y0,',
        '        method="LSODA",',
        '        t_eval=t_eval,',
        '        rtol=1e-8,',
        '        atol=1e-12,',
        '        max_step=0.1,',
        '    )',
        '',
        '    if sol.success:',
        '        print(f"Solved OK.  {sol.t.shape[0]} time points.")',
        '        idx_v = (state_names.index("inlet__q_C")',
        '                 if "inlet__q_C" in state_names else 0)',
        '        plt.figure()',
        '        plt.plot(sol.t, sol.y[idx_v])',
        '        plt.xlabel("Time (s)")',
        '        plt.ylabel(state_names[idx_v])',
        '        plt.title("State variable trace")',
        '        plt.tight_layout()',
        '        plt.savefig("simulation_output.png", dpi=150)',
        '        print("Plot saved to simulation_output.png")',
        '    else:',
        '        print(f"Solver failed: {sol.message}")',
        '',
    ]

    return '\n'.join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# 9.  ENTRY POINT  (no argparse – paths come from CONFIG block above)
# ──────────────────────────────────────────────────────────────────────────────

def main():
    print(f"Reading main model : {MAIN_CELLML}")
    print(f"Reading modules    : {MODULES_CELLML}")
    if PARAMS_FILE:
        print(f"Reading params     : {PARAMS_FILE}")
    print(f"Writing output     : {OUTPUT_FILE}")
    print()

    try:
        with open(MAIN_CELLML) as f:
            main_text = f.read()
    except FileNotFoundError:
        sys.exit(f"ERROR: main model file not found: {MAIN_CELLML}")

    try:
        with open(MODULES_CELLML) as f:
            modules_text = f.read()
    except FileNotFoundError:
        sys.exit(f"ERROR: modules file not found: {MODULES_CELLML}")

    code = generate_python_model(main_text, modules_text, PARAMS_FILE)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(code)

    n_lines  = code.count('\n')
    n_states = code.count('dydt[')
    print(f"Done.")
    print(f"  Output : {OUTPUT_FILE}")
    print(f"  Lines  : {n_lines}")
    print(f"  States : {n_states}")


if __name__ == '__main__':
    main()