"""
generate_model_params.py
========================
Reads a CellML (.cellml) file, a modules file, plus TWO CSV files, 
then generates model_params.py with every component variable populated where possible.

CSV FORMAT 1  –  initial_params.csv
    category,variable,value
    state,inlet/H_link_R,0.45          ← format:  comp/var

CSV FORMAT 2  –  parameters.csv
    variable_name,units,value,data_reference
    l_inlet,metre,0.0003,...           ← format:  var_comp   (comp name at the END)
    gamma_mirror,dimensionless,0.1,...   ← no comp suffix → treated as global

Resolution priority for each CellML variable (comp/var):
    1. initial_params.csv  (exact  comp/var  key)
    2. parameters.csv      (var_comp  key, e.g.  l_inlet → comp=inlet, var=l)
    3. parameters.csv      (global entry – no comp suffix, matches any component)
    4. None  +  *** NOT FOUND ***  comment

Usage:
    python generate_model_params.py  [cellml]  [modules]  [initial_params.csv]  [parameters.csv]  [output]

Defaults:
    cellml           = B1_TD_txt.cellml
    modules          = B1_TD_modules.txt
    initial_params   = initial_params.csv
    parameters_csv   = B1_TD_parameters.csv
    output           = model_params.py
"""

import re
import csv
import sys
import os


# ============================================================
# CLI / DEFAULT PATHS
# ============================================================

cellml_path = sys.argv[1] if len(sys.argv) > 1 else "B1_TD.txt"
modules_path = sys.argv[2] if len(sys.argv) > 2 else "B1_TD_modules.txt"  # NEW
csv1_path   = sys.argv[3] if len(sys.argv) > 3 else "initial_params.csv"
csv2_path   = sys.argv[4] if len(sys.argv) > 4 else "B1_TD_parameters.csv"
out_path    = sys.argv[5] if len(sys.argv) > 5 else "model_params.py"

for p in (cellml_path,):
    if not os.path.isfile(p):
        print(f"ERROR: file not found: {p}")
        sys.exit(1)

for p in (modules_path, csv1_path, csv2_path):
    if not os.path.isfile(p):
        print(f"WARNING: file not found, skipping: {p}")


# ============================================================
# HELPER – clean numeric representation
# ============================================================

def to_value_repr(raw: str) -> str:
    """Return a Python literal for raw string, keeping numeric types numeric."""
    raw = raw.strip()
    try:
        numeric = float(raw)
        # Keep as int if it genuinely is a whole number with no exponent/dot
        if numeric == int(numeric) and "e" not in raw.lower() and "." not in raw:
            return str(int(numeric))
        return repr(numeric)
    except ValueError:
        return repr(raw)


# ============================================================
# STEP 1 – LOAD initial_params.csv   {comp/var → {category, value}}
# ============================================================

lookup1 = {}   # "inlet/H_link_R"  →  {"category": "state", "value": "0.45"}

if os.path.isfile(csv1_path):
    with open(csv1_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row["variable"].strip()
            lookup1[key] = {
                "category": row.get("category", "").strip(),
                "value":    row["value"].strip(),
                "source":   os.path.basename(csv1_path),
            }
    print(f"Loaded {len(lookup1)} entries from {csv1_path}  (format: comp/var)")


# ============================================================
# STEP 2 – PARSE THE CELLML  →  components dict
# (Must happen before resolving parameters.csv so we know comp names)
# ============================================================

with open(cellml_path, "r") as f:
    cellml_text = f.read()

comp_block_re = re.compile(
    r'def\s+comp\s+(\w+)\s+as\s+(.*?)enddef\s*;',
    re.DOTALL
)
var_line_re = re.compile(
    r'var\s+(\w+)\s*:\s*([\w_]+)\s*\{[^}]*\}\s*;'
)

components = {}   # {comp_name: [(var_name, unit)]}

for m in comp_block_re.finditer(cellml_text):
    comp_name  = m.group(1)
    block      = m.group(2)
    vars_found = var_line_re.findall(block)
    if not vars_found:
        continue
    components[comp_name] = [(v, u) for v, u in vars_found]

# Also parse module instances (comp X using comp Y;)
comp_using_re = re.compile(r'comp\s+(\w+)\s+using\s+comp\s+(\w+)\s*;')
comp_to_module = {}  # {instance_name: template_name}
for m in comp_using_re.finditer(cellml_text):
    comp_to_module[m.group(1)] = m.group(2)

# Remove any module templates from components (they end with _module typically)
# Keep only the actual instances that will be used
instances = set(comp_to_module.keys())
components = {k: v for k, v in components.items() if k in instances or not k.endswith('_module')}

known_comps = set(components.keys())

print(f"\nFound {len(components)} component instances in {cellml_path}")
for c, vs in components.items():
    print(f"  {c}: {len(vs)} variables")

# ============================================================
# STEP 2b – PARSE B1_TD_modules.txt to get template variables
# ============================================================

module_templates = {}  # {template_name: [(var_name, unit)]}

if os.path.isfile(modules_path):
    with open(modules_path, "r") as f:
        modules_text = f.read()
    
    for m in comp_block_re.finditer(modules_text):
        template_name = m.group(1)
        block = m.group(2)
        vars_found = var_line_re.findall(block)
        if vars_found:
            module_templates[template_name] = [(v, u) for v, u in vars_found]
    
    print(f"\nFound {len(module_templates)} module templates in {modules_path}")
    
    # Now expand INSTANCE components based on their module templates
    # We DON'T add the template itself to components, only expand instances
    for comp_inst, tmpl_name in comp_to_module.items():
        if tmpl_name in module_templates:
            # Create or expand the instance component
            if comp_inst not in components:
                components[comp_inst] = []
            
            # Merge module template variables into the instance
            existing_vars = {v for v, u in components[comp_inst]}
            added_count = 0
            for var, unit in module_templates[tmpl_name]:
                if var not in existing_vars:
                    components[comp_inst].append((var, unit))
                    added_count += 1
            print(f"  Expanded instance '{comp_inst}' with {added_count} vars from template '{tmpl_name}'")
    
    # Update known_comps to only include actual instances, not templates
    known_comps = set(components.keys())


# ============================================================
# STEP 3 – LOAD parameters.csv  and  resolve var_comp naming
#
# Given a raw name like "l_inlet" or "r_VV_junc1":
#   Try progressively longer suffixes (from the right, split on "_")
#   as a candidate component name.  Use the LONGEST suffix that matches
#   a known component.  Everything before it becomes the variable name.
#   If no suffix matches a known comp → global constant.
#
# Examples:
#   "l_inlet"      → comp=inlet,     var=l
#   "r_VV_junc1"   → comp=VV_junc1,  var=r
#   "gamma_mirror" → no match        → global (var=gamma_mirror)
# ============================================================

lookup2_comp   = {}   # "comp/var"  →  {value, source}
lookup2_global = {}   # "var"       →  {value, source}

if os.path.isfile(csv2_path):
    with open(csv2_path, newline="") as f:
        content = f.read().lstrip("\ufeff")   # strip BOM if present

    reader = csv.DictReader(content.splitlines())

    raw_rows = []
    for row in reader:
        row = {k.strip(): v.strip() for k, v in row.items()}
        # Accept several possible column names
        var_col = (
            row.get("variable_name") or
            row.get("variable") or
            row.get("name") or ""
        ).strip()
        val_col = row.get("value", "").strip()
        if not var_col or not val_col:
            continue
        raw_rows.append({"raw_name": var_col, "value": val_col,
                         "source": os.path.basename(csv2_path)})

    for entry in raw_rows:
        raw = entry["raw_name"]
        val = entry["value"]
        src = entry["source"]

        parts = raw.split("_")
        resolved = False

        # Try all split points from the right, longest comp first
        for split_i in range(len(parts) - 1, 0, -1):
            candidate_comp = "_".join(parts[split_i:])
            candidate_var  = "_".join(parts[:split_i])

            if candidate_comp in known_comps and candidate_var:
                key = f"{candidate_comp}/{candidate_var}"
                lookup2_comp[key] = {"value": val, "source": src}
                resolved = True
                break

        if not resolved:
            # No known comp suffix → global constant
            lookup2_global[raw] = {"value": val, "source": src}

    print(f"\nparameters.csv resolved:")
    print(f"  comp-specific entries : {len(lookup2_comp)}")
    print(f"  global entries        : {len(lookup2_global)}")
    if lookup2_global:
        print(f"  global keys: {list(lookup2_global.keys())}")


# ============================================================
# STEP 4 – RESOLVE a single (comp, var) with priority order
# ============================================================

def resolve(comp_name: str, var_name: str):
    """
    Returns (value_repr, tag_string) or (None, None) if not found anywhere.
    """
    key = f"{comp_name}/{var_name}"

    # Priority 1: initial_params.csv  (exact comp/var)
    if key in lookup1:
        e   = lookup1[key]
        tag = f"({e['category']})  [{e['source']}]  {key}"
        return to_value_repr(e["value"]), tag

    # Priority 2: parameters.csv  comp-specific
    if key in lookup2_comp:
        e   = lookup2_comp[key]
        tag = f"(parameter)  [{e['source']}]  {key}"
        return to_value_repr(e["value"]), tag

    # Priority 3: parameters.csv  global (matched on var name alone)
    if var_name in lookup2_global:
        e   = lookup2_global[var_name]
        tag = f"(global)  [{e['source']}]  {var_name}"
        return to_value_repr(e["value"]), tag

    return None, None


# ============================================================
# STEP 5 – GENERATE model_params.py
# ============================================================

n_matched      = 0
n_unmatched    = 0
unmatched_keys = []

lines = []

lines.append('"""')
lines.append("model_params.py")
lines.append("=" * 68)
lines.append("Auto-generated by generate_model_params.py")
lines.append("")
lines.append(f"Source CellML      : {os.path.basename(cellml_path)}")
lines.append(f"initial_params CSV : {os.path.basename(csv1_path)}")
lines.append(f"parameters CSV     : {os.path.basename(csv2_path)}")
lines.append("")
lines.append("Resolution priority:")
lines.append("  1. initial_params.csv  (comp/var key)")
lines.append("  2. parameters.csv      (var_comp key)")
lines.append("  3. parameters.csv      (global – no comp suffix)")
lines.append("  4. None  +  *** NOT FOUND ***")
lines.append("")
lines.append("Each parameter is named   <comp>__<var>  to avoid clashes.")
lines.append('"""')
lines.append("")
lines.append("# fmt: off  (keep the column-aligned assignments)")
lines.append("")

for comp_name, var_list in components.items():
    lines.append(f"# {'=' * 66}")
    lines.append(f"# Component: {comp_name}")
    lines.append(f"# {'=' * 66}")
    lines.append("")

    for var_name, unit in var_list:
        py_name    = f"{comp_name}__{var_name}"
        value_repr, tag = resolve(comp_name, var_name)

        if value_repr is not None:
            lines.append(
                f"{py_name:<55} = {value_repr:<25}"
                f"  # [{unit}]  {tag}"
            )
            n_matched += 1
        else:
            lines.append(
                f"{py_name:<55} = None"
                f"                           "
                f"  # [{unit}]  *** NOT FOUND ***  {comp_name}/{var_name}"
            )
            n_unmatched += 1
            unmatched_keys.append(f"{comp_name}/{var_name}")

    lines.append("")

lines.append("# fmt: on")
lines.append("")
lines.append(f"# {'=' * 66}")
lines.append(f"# SUMMARY")
lines.append(f"# {'=' * 66}")
lines.append(f"# Matched   : {n_matched}")
lines.append(f"# Not found : {n_unmatched}")
if unmatched_keys:
    lines.append("#")
    lines.append("# Variables not found in either CSV (set to None):")
    for k in unmatched_keys:
        lines.append(f"#   {k}")

output_text = "\n".join(lines) + "\n"

with open(out_path, "w") as f:
    f.write(output_text)

print(f"\nGenerated : {os.path.abspath(out_path)}")
print(f"  Matched   : {n_matched}")
print(f"  Not found : {n_unmatched}")

if n_unmatched:
    print("\n  Variables not found in either CSV (set to None):")
    for k in unmatched_keys:
        print(f"    {k}")