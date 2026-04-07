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
SIM_TIME = 1000
PRE_TIME = 10.0
SOLVER_INFO = {'MaximumStep': 1, 'MaximumNumberOfSteps': 10000}
OUTPUT_DIR = "cellml_run_outputs"
# ------------------------------------------------


def display_name(name, unit):
    return f"{name} [{unit}]" if unit else name


def strip_unit_suffix(s):
    return re.sub(r"\s+\[[^\]]+\]\s*$", "", s.strip())


def make_safe_filename(name):
    return name.replace('/', '__').replace(' ', '_')


def build_variable_metadata(helper):
    states = helper.list_states()
    algebraics = helper.list_algebraics()
    constants = helper.list_constants()
    all_vars = states + algebraics + constants
    all_params = helper.list_all_parameters()  # states (init vals) + constants

    units = {}
    for x in all_vars:
        units[x] = helper.get_variable_unit(x)

    return {
        "states": states,
        "algebraics": algebraics,
        "constants": constants,
        "all_vars": all_vars,
        "all_params": all_params,
        "units": units,
    }


def write_variable_lists(helper, meta, outdir):
    raw_txt_path = os.path.join(outdir, "available_variables_raw.txt")
    pretty_txt_path = os.path.join(outdir, "available_variables.txt")
    params_txt_path = os.path.join(outdir, "available_parameters.txt")

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

    with open(params_txt_path, "w", encoding="utf-8") as f:
        f.write(f"SETTABLE PARAMETERS ({len(meta['all_params'])})\n")
        f.write("(state initial values + constants — these can be changed between runs)\n")
        f.write("-" * 80 + "\n")
        for x in meta["all_params"]:
            f.write(f"{x}\n")

    return raw_txt_path, pretty_txt_path, params_txt_path


def resolve_requested_names(requested, all_vars):
    valid, invalid = [], []
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
            "(raw names like TC1/H_mean or names copied from available_variables.txt):\n> "
        ).strip()
        requested = [x.strip() for x in raw.split(",") if x.strip()]
        if not requested:
            print("Please enter at least one variable.")
            continue
        valid, invalid = resolve_requested_names(requested, meta["all_vars"])
        if invalid:
            print_invalid_with_suggestions(invalid, meta["all_vars"], meta["units"])
            print(f"\nSee: {os.path.join(OUTPUT_DIR, 'available_variables.txt')}")
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
        groups.append({"name": group_name, "variables": selected})
        more = prompt_yes_no("\nDo you want to add another set? (yes/no): ")
        if not more:
            break
        idx += 1
    return groups


def prompt_for_param_changes(meta, params_txt_path):
    """
    Prompt for one or more param=value pairs.
    Returns list of (param_name, new_value) tuples, or None if user cancels.
    Each run is always from the BASELINE — only the params you list here are changed.
    """
    all_params_set = set(meta["all_params"])

    while True:
        print("\nEnter parameter changes as comma-separated name=value pairs.")
        print("Example:  TC1/R=0.5, TC2/C=1.2")
        print("Each run starts from BASELINE — list all params you want changed.")
        print(f"(Available parameters: {params_txt_path})")
        print("Leave blank and press Enter to cancel.")
        raw = input("> ").strip()

        if not raw:
            return None

        pairs = [x.strip() for x in raw.split(",") if x.strip()]
        parsed = []
        errors = []

        for pair in pairs:
            if "=" not in pair:
                errors.append(f"  '{pair}' — missing '=' sign")
                continue
            name, _, val_str = pair.partition("=")
            name = name.strip()
            val_str = val_str.strip()

            if name not in all_params_set:
                matches = difflib.get_close_matches(name, meta["all_params"], n=5, cutoff=0.4)
                msg = f"  '{name}' — not a settable parameter"
                if matches:
                    msg += f"\n    Did you mean: {', '.join(matches)}?"
                errors.append(msg)
                continue

            try:
                value = float(val_str)
            except ValueError:
                errors.append(f"  '{pair}' — '{val_str}' is not a valid number")
                continue

            parsed.append((name, value))

        if errors:
            print("\nErrors:")
            for e in errors:
                print(e)
            continue

        if not parsed:
            return None

        # Confirm what will be changed
        print("\nParameter changes for next run (all others reset to baseline):")
        for name, value in parsed:
            print(f"  {name} = {value:g}")

        if prompt_yes_no("Proceed? (yes/no): "):
            return parsed


def apply_param_changes(helper, param_changes):
    names = [p[0] for p in param_changes]
    values = [p[1] for p in param_changes]
    helper.set_param_vals(names, values)


def run_simulation(helper, all_selected):
    success = helper.run()
    if not success:
        raise RuntimeError("Simulation failed.")
    results = helper.get_results(['time'] + all_selected)
    time = results[0][0]
    results_by_var = {var: results[i][0] for i, var in enumerate(all_selected, start=1)}
    return time, results_by_var


# ------------------------------------------------------------------ #
#  Naming helpers
# ------------------------------------------------------------------ #

def make_run_label(run_index, param_changes):
    if run_index == 1:
        return "baseline"
    changes_str = ", ".join(f"{n}={v:g}" for n, v in param_changes)
    return f"run_{run_index}: {changes_str}"


def make_run_dir(outdir, run_index, param_changes):
    if run_index == 1:
        folder = "run_01_baseline"
    else:
        changes_str = "__".join(
            f"{make_safe_filename(n)}={v:g}" for n, v in param_changes
        )
        folder = f"run_{run_index:02d}__{changes_str}"
    path = os.path.join(outdir, folder)
    os.makedirs(path, exist_ok=True)
    return path


# ------------------------------------------------------------------ #
#  CSV
# ------------------------------------------------------------------ #

def save_csv(time, time_unit, groups, results_by_var, units, run_dir, run_label):
    csv_path = os.path.join(run_dir, "outputs.csv")
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
            row = [str(time[i])] + [str(results_by_var[var][i]) for var in all_selected]
            f.write(",".join(row) + "\n")

    return csv_path


# ------------------------------------------------------------------ #
#  Per-run plots
# ------------------------------------------------------------------ #

def plot_group_single_run(time, time_unit, group, results_by_var, units, run_dir, run_label):
    plt.figure(figsize=(12, 6))
    for var in group["variables"]:
        plt.plot(time, results_by_var[var], label=var)
    plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
    plt.ylabel("Value")
    plt.title(f"{group['name']} — {run_label}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    outpath = os.path.join(run_dir, f"{make_safe_filename(group['name'])}_combined.png")
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_all_sets_single_run(time, time_unit, groups, results_by_var, run_dir, run_label):
    plt.figure(figsize=(14, 7))
    for group in groups:
        for var in group["variables"]:
            plt.plot(time, results_by_var[var], label=f"{group['name']}: {var}")
    plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
    plt.ylabel("Value")
    plt.title(f"All Sets Combined — {run_label}")
    plt.grid(True)
    plt.legend(fontsize=8)
    plt.tight_layout()
    outpath = os.path.join(run_dir, "all_sets_combined.png")
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_individuals_single_run(time, time_unit, groups, results_by_var, units, run_dir):
    saved = []
    for group in groups:
        group_subdir = os.path.join(run_dir, make_safe_filename(group["name"]))
        os.makedirs(group_subdir, exist_ok=True)
        for var in group["variables"]:
            unit = units.get(var, "")
            plt.figure(figsize=(10, 5))
            plt.plot(time, results_by_var[var])
            plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
            plt.ylabel(f"{var}{' (' + unit + ')' if unit else ''}")
            plt.title(f"{var}")
            plt.grid(True)
            plt.tight_layout()
            outpath = os.path.join(group_subdir, f"{make_safe_filename(var)}.png")
            plt.savefig(outpath, dpi=300)
            plt.close()
            saved.append(outpath)
    return saved


# ------------------------------------------------------------------ #
#  Overlay plots (regenerated after every run)
# ------------------------------------------------------------------ #

def plot_overlay_group(time_unit, group, all_runs, overlay_dir):
    plt.figure(figsize=(12, 6))
    for run in all_runs:
        for var in group["variables"]:
            plt.plot(run["time"], run["results_by_var"][var],
                     label=f"{run['label']}: {var}")
    plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
    plt.ylabel("Value")
    plt.title(f"{group['name']} — All Runs Overlay")
    plt.grid(True)
    plt.legend(fontsize=8)
    plt.tight_layout()
    outpath = os.path.join(overlay_dir, f"{make_safe_filename(group['name'])}_overlay.png")
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_overlay_all_sets(time_unit, groups, all_runs, overlay_dir):
    plt.figure(figsize=(14, 8))
    for run in all_runs:
        for group in groups:
            for var in group["variables"]:
                plt.plot(run["time"], run["results_by_var"][var],
                         label=f"{run['label']} | {group['name']}: {var}")
    plt.xlabel(f"Time{' (' + time_unit + ')' if time_unit else ''}")
    plt.ylabel("Value")
    plt.title("All Sets, All Runs — Overlay")
    plt.grid(True)
    plt.legend(fontsize=7, bbox_to_anchor=(1.01, 1), loc='upper left')
    plt.tight_layout()
    outpath = os.path.join(overlay_dir, "all_sets_all_runs_overlay.png")
    plt.savefig(outpath, dpi=300, bbox_inches='tight')
    plt.close()
    return outpath


def regenerate_overlay_plots(time_unit, groups, all_runs, outdir):
    overlay_dir = os.path.join(outdir, "overlay")
    os.makedirs(overlay_dir, exist_ok=True)
    group_overlay_paths = []
    for group in groups:
        p = plot_overlay_group(time_unit, group, all_runs, overlay_dir)
        group_overlay_paths.append(p)
    all_sets_overlay_path = plot_overlay_all_sets(time_unit, groups, all_runs, overlay_dir)
    return overlay_dir, group_overlay_paths, all_sets_overlay_path


# ------------------------------------------------------------------ #
#  Main
# ------------------------------------------------------------------ #

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    helper = SimulationHelper(
        CELLML_FILE, DT, SIM_TIME,
        solver_info=SOLVER_INFO,
        pre_time=PRE_TIME,
    )

    meta = build_variable_metadata(helper)
    raw_txt_path, pretty_txt_path, params_txt_path = write_variable_lists(
        helper, meta, OUTPUT_DIR
    )

    print(f"\nVariable list written to:   {pretty_txt_path}")
    print(f"Raw variable list:          {raw_txt_path}")
    print(f"Settable parameter list:    {params_txt_path}")
    print(f"Time unit: {helper.get_time_unit() or '<unknown>'}\n")

    # --- Choose variable sets once (fixed for all runs) ---
    groups = prompt_for_multiple_groups(meta)

    all_selected = []
    seen = set()
    for group in groups:
        for var in group["variables"]:
            if var not in seen:
                seen.add(var)
                all_selected.append(var)

    time_unit = helper.get_time_unit()
    all_runs = []
    run_index = 1
    current_param_changes = []  # empty = baseline

    while True:
        run_label = make_run_label(run_index, current_param_changes)
        run_dir = make_run_dir(OUTPUT_DIR, run_index, current_param_changes)

        print(f"\n{'='*60}")
        print(f"  Run {run_index}: {run_label}")
        print(f"{'='*60}")

        # Reset to clean baseline for every run after the first
        if run_index > 1:
            helper.reset_and_clear()
            apply_param_changes(helper, current_param_changes)

        print("Running simulation...")
        time, results_by_var = run_simulation(helper, all_selected)

        # Store run for overlay
        all_runs.append({
            "label": run_label,
            "time": time,
            "results_by_var": results_by_var,
            "param_changes": list(current_param_changes),
        })

        # Per-run outputs
        for group in groups:
            plot_group_single_run(
                time, time_unit, group, results_by_var, meta["units"], run_dir, run_label
            )
        plot_all_sets_single_run(time, time_unit, groups, results_by_var, run_dir, run_label)
        plot_individuals_single_run(time, time_unit, groups, results_by_var, meta["units"], run_dir)
        csv_path = save_csv(
            time, time_unit, groups, results_by_var, meta["units"], run_dir, run_label
        )

        # Overlay plots — regenerated to include this run
        overlay_dir, _, _ = regenerate_overlay_plots(time_unit, groups, all_runs, OUTPUT_DIR)

        print(f"\n  Per-run folder : {run_dir}")
        print(f"  Overlay folder : {overlay_dir}  (updated)")
        print(f"  CSV            : {csv_path}")

        # --- Ask to continue ---
        more = prompt_yes_no(
            "\nDo you want to change parameters and run again? (yes/no): "
        )
        if not more:
            break

        param_changes = prompt_for_param_changes(meta, params_txt_path)
        if param_changes is None:
            print("No parameter changes entered. Stopping.")
            break

        current_param_changes = param_changes
        run_index += 1

    helper.close_simulation()

    print("\n" + "=" * 60)
    print(f"All done!  Total runs: {len(all_runs)}")
    print(f"Output root : {OUTPUT_DIR}")
    for run in all_runs:
        print(f"  [{run['label']}]")
    print(f"\nFinal overlay plots : {overlay_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
