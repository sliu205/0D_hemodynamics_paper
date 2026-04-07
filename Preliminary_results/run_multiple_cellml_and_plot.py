#!/usr/bin/env python3
import os
import re
import difflib

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from opencor_helper import SimulationHelper

# ---------------- user settings ----------------
CELLML_FILE = "/home/sliu205/0D_hemodynamics_paper/Preliminary_results/generated_models/H_D_network/H_D_network.cellml"
DT = 1
SIM_TIME = 200
PRE_TIME = 10.0
SOLVER_INFO = {'MaximumStep': 1, 'MaximumNumberOfSteps': 10000}
OUTPUT_DIR = "cellml_run_outputs"
# ------------------------------------------------


def display_name(name, unit):
    return f"{name} [{unit}]" if unit else name


def strip_unit_suffix(s):
    # turns "TC1/H_mean [dimensionless]" into "TC1/H_mean"
    return re.sub(r"\s+\[[^\]]+\]\s*$", "", s.strip())


def make_safe_filename(name):
    return name.replace('/', '__').replace(' ', '_')


def build_variable_metadata(helper):
    states = helper.list_states()
    algebraics = helper.list_algebraics()
    constants = helper.list_constants()

    all_vars = states + algebraics + constants
    units = {}

    for x in all_vars:
        units[x] = helper.get_variable_unit(x)

    return {
        "states": states,
        "algebraics": algebraics,
        "constants": constants,
        "all_vars": all_vars,
        "units": units,
    }


def write_variable_lists(helper, meta, outdir):
    raw_txt_path = os.path.join(outdir, "available_variables_raw.txt")
    pretty_txt_path = os.path.join(outdir, "available_variables.txt")

    with open(raw_txt_path, "w", encoding="utf-8") as f:
        for x in meta["all_vars"]:
            f.write(f"{x}\n")

    with open(pretty_txt_path, "w", encoding="utf-8") as f:
        f.write(f"CellML file: {helper.cellml_path}\n")
        f.write(f"Time unit: {helper.get_time_unit() or '<unknown>'}\n\n")

        f.write(f"STATES ({len(meta['states'])})\n")
        f.write("-" * 80 + "\n")
        for x in meta["states"]:
            f.write(display_name(x, meta["units"].get(x, "")) + "\n")

        f.write(f"\nALGEBRAICS ({len(meta['algebraics'])})\n")
        f.write("-" * 80 + "\n")
        for x in meta["algebraics"]:
            f.write(display_name(x, meta["units"].get(x, "")) + "\n")

        f.write(f"\nCONSTANTS ({len(meta['constants'])})\n")
        f.write("-" * 80 + "\n")
        for x in meta["constants"]:
            f.write(display_name(x, meta["units"].get(x, "")) + "\n")

        f.write(f"\nALL VARIABLES ({len(meta['all_vars'])})\n")
        f.write("-" * 80 + "\n")
        for x in meta["all_vars"]:
            f.write(display_name(x, meta["units"].get(x, "")) + "\n")

    return raw_txt_path, pretty_txt_path


def print_full_variable_list(meta):
    print(f"\nAvailable variables ({len(meta['all_vars'])} total):")
    for x in meta["all_vars"]:
        print(f"  {display_name(x, meta['units'].get(x, ''))}")


def resolve_requested_names(requested, all_vars):
    valid = []
    invalid = []

    all_vars_set = set(all_vars)

    for item in requested:
        raw = strip_unit_suffix(item)
        if raw in all_vars_set:
            valid.append(raw)
        else:
            invalid.append(item)

    return valid, invalid


def print_invalid_with_suggestions(invalid, all_vars, units):
    print("\nThese variable names were not found:")
    for bad in invalid:
        print(f"  {bad}")
        cleaned = strip_unit_suffix(bad)
        matches = difflib.get_close_matches(cleaned, all_vars, n=8, cutoff=0.4)
        if matches:
            print("    Close matches:")
            for m in matches:
                print(f"      {display_name(m, units.get(m, ''))}")


def prompt_for_single_group(meta, group_index):
    while True:
        raw = input(
            f"\nEnter comma-separated variables for set {group_index}\n"
            "(you can use either raw names like TC1/H_mean\n"
            "or names copied from available_variables.txt):\n> "
        ).strip()

        requested = [x.strip() for x in raw.split(",") if x.strip()]
        if not requested:
            print("Please enter at least one variable.")
            continue

        valid, invalid = resolve_requested_names(requested, meta["all_vars"])

        if invalid:
            print_invalid_with_suggestions(invalid, meta["all_vars"], meta["units"])
            print("\nSee these files:")
            print(f"  {os.path.join(OUTPUT_DIR, 'available_variables.txt')}")
            print(f"  {os.path.join(OUTPUT_DIR, 'available_variables_raw.txt')}")
            print_full_variable_list(meta)
            continue

        return valid


def prompt_yes_no(message):
    while True:
        answer = input(message).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter yes/y or no/n.")


def prompt_for_group_name(default_name):
    raw = input(f"Enter name for this set [{default_name}]: ").strip()
    return raw if raw else default_name


def prompt_for_multiple_groups(meta):
    groups = []
    idx = 1

    while True:
        default_name = f"set_{idx}"
        group_name = prompt_for_group_name(default_name)
        selected = prompt_for_single_group(meta, idx)

        groups.append({
            "name": group_name,
            "variables": selected,
        })

        more = prompt_yes_no("\nDo you want to add another set? (yes/no): ")
        if not more:
            break
        idx += 1

    return groups


def save_csv(time, time_unit, groups, results_by_var, units, outdir):
    csv_path = os.path.join(outdir, "selected_outputs_all_sets.csv")
    all_selected = []
    seen = set()

    for group in groups:
        for var in group["variables"]:
            if var not in seen:
                seen.add(var)
                all_selected.append(var)

    with open(csv_path, "w", encoding="utf-8") as f:
        header = [f"time{(' [' + time_unit + ']') if time_unit else ''}"]
        for var in all_selected:
            header.append(display_name(var, units.get(var, "")))
        f.write(",".join(header) + "\n")

        for i in range(len(time)):
            row = [str(time[i])]
            for var in all_selected:
                row.append(str(results_by_var[var][i]))
            f.write(",".join(row) + "\n")

    return csv_path


def plot_group_combined(time, time_unit, group, results_by_var, units, outdir):
    plt.figure(figsize=(12, 6))
    for var in group["variables"]:
        plt.plot(time, results_by_var[var], label=var)

    plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
    plt.ylabel("Value")
    plt.title(f"Selected CellML Outputs - {group['name']}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    outpath = os.path.join(outdir, f"{make_safe_filename(group['name'])}_combined.png")
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_all_groups_combined(time, time_unit, groups, results_by_var, outdir):
    plt.figure(figsize=(14, 7))

    for group in groups:
        for var in group["variables"]:
            label = f"{group['name']}: {var}"
            plt.plot(time, results_by_var[var], label=label)

    plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
    plt.ylabel("Value")
    plt.title("All Selected Sets Combined")
    plt.grid(True)
    plt.legend(fontsize=8)
    plt.tight_layout()

    outpath = os.path.join(outdir, "all_sets_combined.png")
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_individuals(time, time_unit, groups, results_by_var, units, outdir):
    saved = []

    for group in groups:
        group_dir = os.path.join(outdir, make_safe_filename(group["name"]))
        os.makedirs(group_dir, exist_ok=True)

        for var in group["variables"]:
            unit = units.get(var, "")
            plt.figure(figsize=(10, 5))
            plt.plot(time, results_by_var[var])
            plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
            plt.ylabel(f"{var}{' (' + unit + ')' if unit else ''}")
            plt.title(f"{group['name']} - {var}")
            plt.grid(True)
            plt.tight_layout()

            outpath = os.path.join(group_dir, f"{make_safe_filename(var)}.png")
            plt.savefig(outpath, dpi=300)
            plt.close()
            saved.append(outpath)

    return saved


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    helper = SimulationHelper(
        CELLML_FILE,
        DT,
        SIM_TIME,
        solver_info=SOLVER_INFO,
        pre_time=PRE_TIME,
    )

    meta = build_variable_metadata(helper)
    raw_txt_path, pretty_txt_path = write_variable_lists(helper, meta, OUTPUT_DIR)

    print(f"Available variable list written to: {pretty_txt_path}")
    print(f"Raw variable list written to:       {raw_txt_path}")
    print(f"Time unit: {helper.get_time_unit() or '<unknown>'}")

    groups = prompt_for_multiple_groups(meta)

    # Flatten variables across all groups, preserving order and uniqueness
    all_selected = []
    seen = set()
    for group in groups:
        for var in group["variables"]:
            if var not in seen:
                seen.add(var)
                all_selected.append(var)

    print("\nRunning simulation...")
    success = helper.run()
    if not success:
        helper.close_simulation()
        raise RuntimeError("Simulation failed.")

    results = helper.get_results(['time'] + all_selected)
    time = results[0][0]
    time_unit = helper.get_time_unit()

    results_by_var = {}
    for i, var in enumerate(all_selected, start=1):
        results_by_var[var] = results[i][0]

    csv_path = save_csv(time, time_unit, groups, results_by_var, meta["units"], OUTPUT_DIR)

    group_combined_paths = []
    for group in groups:
        p = plot_group_combined(time, time_unit, group, results_by_var, meta["units"], OUTPUT_DIR)
        group_combined_paths.append(p)

    all_sets_combined_path = plot_all_groups_combined(time, time_unit, groups, results_by_var, OUTPUT_DIR)
    individual_paths = plot_individuals(time, time_unit, groups, results_by_var, meta["units"], OUTPUT_DIR)

    helper.close_simulation()

    print("\nDone.")
    print(f"Pretty variable list: {pretty_txt_path}")
    print(f"Raw variable list:    {raw_txt_path}")
    print(f"CSV output:           {csv_path}")
    print("\nGroup combined plots:")
    for p in group_combined_paths:
        print(f"  {p}")
    print(f"\nAll sets combined plot:\n  {all_sets_combined_path}")
    print(f"\nIndividual plots saved under: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
