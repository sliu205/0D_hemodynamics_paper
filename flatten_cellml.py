#!/usr/bin/env python3
"""
Flatten a CellML 1.1 model that uses <import> into a single self-contained file.

Each <import> element in the main model is replaced, in place, by copies of the
imported <units> and <component> definitions from the referenced file. Imported
components/units are renamed to the local name given in the import (so e.g.
component_ref="PP_capillary_H_D" name="inlet_module" becomes a component named
"inlet_module"). The same source component can be imported multiple times under
different local names - each import gets its own copy.

Limitations (fine for circulatory_autogen output, which this was written for):
  * Assumes imported units are not renamed relative to their source names
    (unit references inside copied components are not rewritten). The script
    checks this and warns if it isn't true.
  * Does not handle encapsulation groups inside imported files.

Usage:
    python3 flatten_cellml.py switching_test.cellml [-o switching_test_flat.cellml]
"""

import argparse
import copy
import os
import sys

from lxml import etree

CELLML_NS = "http://www.cellml.org/cellml/1.1#"
XLINK_NS = "http://www.w3.org/1999/xlink"
NS = {"c": CELLML_NS, "xlink": XLINK_NS}


def load(path):
    parser = etree.XMLParser(remove_blank_text=False)
    return etree.parse(path, parser)


def flatten(main_path, out_path):
    base_dir = os.path.dirname(os.path.abspath(main_path))
    tree = load(main_path)
    root = tree.getroot()

    # cache parsed imported files so each href is read once
    file_cache = {}

    def get_source_root(href):
        if href not in file_cache:
            file_cache[href] = load(os.path.join(base_dir, href)).getroot()
        return file_cache[href]

    inlined_units = {}       # local units name -> source (for duplicate check)
    inlined_components = []  # local component names added

    imports = root.findall("c:import", NS)
    if not imports:
        print("No <import> elements found - nothing to flatten.")

    for imp in imports:
        href = imp.get(f"{{{XLINK_NS}}}href")
        src_root = get_source_root(href)

        replacements = []

        # ---- imported units ----
        for u in imp.findall("c:units", NS):
            local_name = u.get("name")
            ref = u.get("units_ref")
            if local_name != ref:
                print(f"WARNING: units renamed on import ({ref} -> {local_name}); "
                      f"unit references inside copied components are NOT rewritten.")
            src = src_root.find(f"c:units[@name='{ref}']", NS)
            if src is None:
                sys.exit(f"ERROR: units '{ref}' not found in {href}")
            if local_name in inlined_units:
                # already inlined (e.g. two files both import the same units) - skip
                continue
            cpy = copy.deepcopy(src)
            cpy.set("name", local_name)
            inlined_units[local_name] = href
            replacements.append(cpy)

        # ---- imported components ----
        for comp in imp.findall("c:component", NS):
            local_name = comp.get("name")
            ref = comp.get("component_ref")
            src = src_root.find(f"c:component[@name='{ref}']", NS)
            if src is None:
                sys.exit(f"ERROR: component '{ref}' not found in {href}")
            cpy = copy.deepcopy(src)
            cpy.set("name", local_name)
            inlined_components.append(f"{local_name} (from {href}:{ref})")
            replacements.append(cpy)

        # ---- splice the copies in where the <import> was ----
        parent = imp.getparent()
        idx = parent.index(imp)
        comment = etree.Comment(f" inlined from {href} ")
        comment.tail = "\n"
        parent.insert(idx, comment)
        idx += 1
        for node in replacements:
            node.tail = "\n"
            parent.insert(idx, node)
            idx += 1
        parent.remove(imp)

    tree.write(out_path, xml_declaration=True, encoding="UTF-8")

    print(f"Wrote {out_path}")
    print(f"  inlined units:      {len(inlined_units)}")
    print(f"  inlined components: {len(inlined_components)}")
    for c in inlined_components:
        print(f"    - {c}")

    # ---- sanity checks on the flattened file ----
    check(out_path)


BUILTIN_UNITS = {
    "ampere", "farad", "katal", "lux", "pascal", "tesla", "becquerel", "gram",
    "kelvin", "meter", "radian", "volt", "candela", "gray", "kilogram", "metre",
    "second", "watt", "celsius", "henry", "liter", "mole", "siemens", "weber",
    "coulomb", "hertz", "litre", "newton", "sievert", "dimensionless", "joule",
    "lumen", "ohm", "steradian",
}


def check(path):
    root = load(path).getroot()
    problems = 0

    defined_units = {u.get("name") for u in root.findall("c:units", NS)} | BUILTIN_UNITS
    comp_names = [c.get("name") for c in root.findall("c:component", NS)]

    # duplicate component names?
    dupes = {n for n in comp_names if comp_names.count(n) > 1}
    if dupes:
        problems += 1
        print(f"CHECK FAIL: duplicate component names: {sorted(dupes)}")

    # every variable's units defined?
    missing = set()
    for comp in root.findall("c:component", NS):
        for var in comp.findall("c:variable", NS):
            u = var.get("units")
            if u and u not in defined_units:
                missing.add(u)
        # cn units in math
        for cn in comp.iter("{http://www.w3.org/1998/Math/MathML}cn"):
            u = cn.get(f"{{{CELLML_NS}}}units")
            if u and u not in defined_units:
                missing.add(u)
    if missing:
        problems += 1
        print(f"CHECK FAIL: units referenced but not defined: {sorted(missing)}")

    # every connection's components exist?
    comp_set = set(comp_names)
    for conn in root.findall("c:connection", NS):
        mc = conn.find("c:map_components", NS)
        for attr in ("component_1", "component_2"):
            name = mc.get(attr)
            if name not in comp_set:
                problems += 1
                print(f"CHECK FAIL: connection references unknown component '{name}'")

    # any imports left?
    if root.findall("c:import", NS):
        problems += 1
        print("CHECK FAIL: <import> elements remain in output")

    if problems == 0:
        print("All checks passed: no remaining imports, no duplicate components, "
              "all units and connection targets resolve.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Flatten CellML 1.1 imports into one file")
    ap.add_argument("model", help="main .cellml file containing the <import> elements")
    ap.add_argument("-o", "--output", help="output path (default: <model>_flat.cellml)")
    args = ap.parse_args()
    out = args.output or os.path.splitext(args.model)[0] + "_flat.cellml"
    flatten(args.model, out)
