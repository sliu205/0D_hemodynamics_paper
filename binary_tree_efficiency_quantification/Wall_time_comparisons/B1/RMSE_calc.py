"""
RMSE comparison: OpenCor (ground truth) vs CellML-generated Python vs iterative version.

For each variable present in all three datasets, compute:
  - RMSE vs OpenCor for the generated-python run
  - RMSE vs OpenCor for the iterative run
  - NRMSE (RMSE / range of the OpenCor signal), as a unit-free comparison

Outputs a per-variable table to stdout and writes a CSV summary next to this script.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# =============================================================================
# USER-EDITABLE PATHS
# =============================================================================
# Ground truth
OPENCOR_CSV  = "/home/sliu205/0D_hemodynamics_paper/0D_hemodynamics_paper/binary_tree_efficiency_quantification/Wall_time_comparisons/B1/B1_TD_OpenCor_data.csv"

# CellML-generated pure-python run (non-iterative)
GENERATED_CSV = "/home/sliu205/0D_hemodynamics_paper/0D_hemodynamics_paper/binary_tree_efficiency_quantification/Wall_time_comparisons/B1/B1_TD/sim_results_constriction/simulation_plots_data.csv"

# Iterative version
ITERATIVE_CSV = "/home/sliu205/0D_hemodynamics_paper/0D_hemodynamics_paper/binary_tree_efficiency_quantification/Wall_time_comparisons/B1/B1_speedup_I/sim_results_constriction/simulation_plots_data.csv"

# Where to write the per-variable RMSE summary CSV
OUTPUT_CSV = "rmse_summary.csv"

# If True, resample all three datasets onto a common time grid before comparing.
# If False, assume they already have the same number of rows in the same order
# (the OpenCor CSV has no time column — rows are treated as sequential samples).
RESAMPLE_TO_COMMON_GRID = False

# Simulation time span — only used as a fallback if a CSV has no time column.
T_START = 0.0
T_END   = 1000.0

# Number of rows to drop from the start of each dataset before computing RMSE.
# Useful when the initial conditions differ between solvers (e.g. OpenCor's
# t=0 row is the literal IC while the Python runs may have already taken a
# tiny step). Set to 0 to keep everything.
SKIP_INITIAL_ROWS = 1

# =============================================================================


def normalize_var_name(col: str) -> str:
    """
    Map a column header from either file format into a canonical variable key.

    OpenCor style:      'PV1 | u_mmHg (dimensionless)'  -> 'PV1__u_mmHg'
    OpenCor time:       'environment | time (second)'   -> 'time'
    Simulation style:   'PV1__u_mmHg'                   -> 'PV1__u_mmHg'
    """
    s = col.strip()
    # Strip any trailing ' (units)' annotation from the OpenCor header
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s)
    # OpenCor uses ' | ' between component and variable; simulation uses '__'
    s = s.replace(" | ", "__").replace("|", "__")
    # Collapse any stray whitespace
    s = re.sub(r"\s+", "", s)
    # Any column representing time (e.g. 'environment__time') becomes just 'time'
    if s.lower() == "time" or s.lower().endswith("__time"):
        return "time"
    return s


def load_opencor(path: str) -> pd.DataFrame:
    """
    Load the OpenCor CSV. Uses its own time column if present
    ('environment | time (second)' is normalized to 'time'); otherwise
    synthesizes one from T_START/T_END.
    """
    df = pd.read_csv(path)
    df.columns = [normalize_var_name(c) for c in df.columns]
    if "time" not in df.columns:
        df.insert(0, "time", np.linspace(T_START, T_END, len(df)))
    return df


def load_simulation(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [normalize_var_name(c) for c in df.columns]
    if "time" not in df.columns:
        df.insert(0, "time", np.linspace(T_START, T_END, len(df)))
    return df


def align_on_time(truth: pd.DataFrame, other: pd.DataFrame, var: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Return truth and other values for `var`, aligned on a common time grid.

    If RESAMPLE_TO_COMMON_GRID is False and the two series already have the
    same length, we just return them as-is (fastest path, avoids interpolation
    noise when grids already match).
    """
    t_truth = truth["time"].to_numpy()
    y_truth = truth[var].to_numpy()
    t_other = other["time"].to_numpy()
    y_other = other[var].to_numpy()

    same_length = len(t_truth) == len(t_other)
    grids_match = same_length and np.allclose(t_truth, t_other, rtol=1e-9, atol=1e-9)

    if grids_match and not RESAMPLE_TO_COMMON_GRID:
        return y_truth, y_other

    # Interpolate `other` onto the truth time grid, restricted to overlap.
    t_lo = max(t_truth.min(), t_other.min())
    t_hi = min(t_truth.max(), t_other.max())
    mask = (t_truth >= t_lo) & (t_truth <= t_hi)
    y_truth_a = y_truth[mask]
    y_other_a = np.interp(t_truth[mask], t_other, y_other)
    return y_truth_a, y_other_a


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    diff = a - b
    # Ignore NaNs from either side
    mask = np.isfinite(diff)
    if not mask.any():
        return float("nan")
    return float(np.sqrt(np.mean(diff[mask] ** 2)))


def signal_range(a: np.ndarray) -> float:
    mask = np.isfinite(a)
    if not mask.any():
        return float("nan")
    return float(a[mask].max() - a[mask].min())


def compare(truth: pd.DataFrame, label: str, other: pd.DataFrame, shared_vars: list[str]) -> list[dict]:
    rows = []
    for var in shared_vars:
        y_truth, y_other = align_on_time(truth, other, var)
        err = rmse(y_truth, y_other)
        rng = signal_range(y_truth)
        nrmse = err / rng if rng and np.isfinite(rng) and rng > 0 else float("nan")
        rows.append({
            "variable": var,
            "dataset": label,
            "rmse": err,
            "range_truth": rng,
            "nrmse_pct": 100.0 * nrmse if np.isfinite(nrmse) else float("nan"),
            "n_samples": min(len(y_truth), len(y_other)),
        })
    return rows


def print_table(rows: list[dict]) -> None:
    """Pretty-print per-variable RMSE comparison side-by-side."""
    # Pivot into {var: {dataset: {rmse, nrmse_pct}}}
    per_var: dict[str, dict[str, dict]] = {}
    for r in rows:
        per_var.setdefault(r["variable"], {})[r["dataset"]] = r

    datasets = sorted({r["dataset"] for r in rows})
    var_w = max(len("variable"), max(len(v) for v in per_var))

    # Header
    header = f"{'variable'.ljust(var_w)}"
    for ds in datasets:
        header += f"  |  {ds + ' RMSE':>18}  {ds + ' NRMSE%':>14}"
    print(header)
    print("-" * len(header))

    # Rows — sort by worst RMSE across datasets, descending
    def worst_rmse(v):
        vals = [per_var[v][ds]["rmse"] for ds in datasets if ds in per_var[v]]
        vals = [x for x in vals if np.isfinite(x)]
        return max(vals) if vals else -1.0

    for var in sorted(per_var.keys(), key=worst_rmse, reverse=True):
        line = var.ljust(var_w)
        for ds in datasets:
            entry = per_var[var].get(ds)
            if entry is None:
                line += f"  |  {'—':>18}  {'—':>14}"
            else:
                line += f"  |  {entry['rmse']:>18.6g}  {entry['nrmse_pct']:>13.4f}%"
        print(line)


def main() -> int:
    for label, path in [("OpenCor", OPENCOR_CSV), ("generated", GENERATED_CSV), ("iterative", ITERATIVE_CSV)]:
        if not Path(path).is_file():
            print(f"ERROR: {label} CSV not found: {path}", file=sys.stderr)
            return 1

    print("Loading CSVs...")
    truth    = load_opencor(OPENCOR_CSV)
    gen      = load_simulation(GENERATED_CSV)
    itr      = load_simulation(ITERATIVE_CSV)
    print(f"  OpenCor  : {len(truth):>5d} rows, {len(truth.columns)-1} vars")
    print(f"  generated: {len(gen):>5d} rows, {len(gen.columns)-1} vars")
    print(f"  iterative: {len(itr):>5d} rows, {len(itr.columns)-1} vars")

    if SKIP_INITIAL_ROWS > 0:
        print(f"\nSkipping first {SKIP_INITIAL_ROWS} row(s) of each dataset "
              f"(initial conditions differ across solvers).")
        truth = truth.iloc[SKIP_INITIAL_ROWS:].reset_index(drop=True)
        gen   = gen.iloc[SKIP_INITIAL_ROWS:].reset_index(drop=True)
        itr   = itr.iloc[SKIP_INITIAL_ROWS:].reset_index(drop=True)
        print(f"  OpenCor  : {len(truth):>5d} rows remaining "
              f"(t = {truth['time'].iloc[0]:g} \u2192 {truth['time'].iloc[-1]:g})")
        print(f"  generated: {len(gen):>5d} rows remaining "
              f"(t = {gen['time'].iloc[0]:g} \u2192 {gen['time'].iloc[-1]:g})")
        print(f"  iterative: {len(itr):>5d} rows remaining "
              f"(t = {itr['time'].iloc[0]:g} \u2192 {itr['time'].iloc[-1]:g})")

    # Variables present in all three (excluding 'time')
    truth_vars = set(truth.columns) - {"time"}
    gen_vars   = set(gen.columns)   - {"time"}
    itr_vars   = set(itr.columns)   - {"time"}
    shared = sorted(truth_vars & gen_vars & itr_vars)

    only_truth = sorted(truth_vars - (gen_vars | itr_vars))
    only_sim   = sorted((gen_vars | itr_vars) - truth_vars)

    print(f"\nShared variables (comparable): {len(shared)}")
    if only_truth:
        print(f"  Only in OpenCor, skipped: {only_truth}")
    if only_sim:
        print(f"  Only in simulation CSVs, skipped: {only_sim}")

    if not shared:
        print("\nNo overlapping variables — nothing to compare.", file=sys.stderr)
        return 1

    rows: list[dict] = []
    rows += compare(truth, "generated", gen, shared)
    rows += compare(truth, "iterative", itr, shared)

    print("\nPer-variable RMSE vs OpenCor (ground truth)")
    print("=" * 80)
    print_table(rows)

    # Aggregate summary
    print("\nAggregate NRMSE% (mean across variables)")
    print("-" * 50)
    for ds in ("generated", "iterative"):
        nrmse_vals = [r["nrmse_pct"] for r in rows if r["dataset"] == ds and np.isfinite(r["nrmse_pct"])]
        if nrmse_vals:
            print(f"  {ds:<10s}  mean NRMSE = {np.mean(nrmse_vals):8.4f}%   "
                  f"median = {np.median(nrmse_vals):8.4f}%   "
                  f"max = {np.max(nrmse_vals):8.4f}%")

    # Write CSV
    out_path = Path(OUTPUT_CSV)
    if not out_path.is_absolute():
        out_path = Path(__file__).resolve().parent / out_path
    pd.DataFrame(rows).to_csv(out_path, index=False)
    print(f"\nWrote summary to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())