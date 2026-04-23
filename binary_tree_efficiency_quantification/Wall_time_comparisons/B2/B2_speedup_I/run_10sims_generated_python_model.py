"""
Run the generated model N_RUNS times and keep the fastest run for plotting.

Supports both the time-dynamics model (generated_model.py) and the iterative
model (generated_model_iter.py). Toggle with MODEL_VARIANT below. Solver
settings are held constant across variants so wall-time and accuracy are
directly comparable.

Benchmarking:
  - Runs the simulation N_RUNS times.
  - Each run reimports the model module fresh (importlib.reload) so the
    iterative solver's warm-start cache does not give later runs an unfair
    advantage.
  - Keeps only the fastest run's results; CSVs and PNG correspond to that run.

Output files (all under OUTPUT_DIR):
  simulation_results_<variant>.csv        -- all states + default algebraics
  simulation_plots_data_<variant>.csv     -- time + every variable in PLOTS
  simulation_results_<variant>.png        -- the plot figure
"""

import os
import sys
import time
import csv
import importlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# =============================================================================
# Model selection
# =============================================================================
# "time" -> generated_model.py          (original time-dynamics formulation)
# "iter" -> generated_model_iter.py     (scipy.optimize.root on H_mean)
MODEL_VARIANT = "iter"

_variant_module = {
    "time": "generated_model",
    "iter": "generated_model_iter",
}[MODEL_VARIANT]

# =============================================================================
# Solver Configuration (IDENTICAL across variants for fair benchmarking)
# =============================================================================
SOLVER_METHOD = "Radau"  # Options: "BDF", "LSODA", "Radau", "RK45"
T_START = 0
T_END = 1000
N_POINTS = 1001  # Number of output points

RTOL = 1e-7  # Relative tolerance
ATOL = 1e-7  # Absolute tolerance
MAX_STEP = 5  # Maximum step size (use np.inf for unlimited)

# =============================================================================
# Benchmarking config
# =============================================================================
N_RUNS = 10  # number of repeated runs; fastest wins
SHOW_PROGRESS = False  # live per-second progress lines during each run (noisy for N_RUNS>1)

# =============================================================================
# Output directory + filenames (variant-tagged so runs don't clobber each other)
# =============================================================================
OUTPUT_DIR = "sim_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSV_OUTPUT       = os.path.join(OUTPUT_DIR, f"simulation_results_{MODEL_VARIANT}.csv")      # states + default algebraics
CSV_PLOTS_OUTPUT = os.path.join(OUTPUT_DIR, f"simulation_plots_data_{MODEL_VARIANT}.csv")  # every var in PLOTS
PLOT_OUTPUT      = os.path.join(OUTPUT_DIR, f"simulation_results_{MODEL_VARIANT}.png")     # figure

# =============================================================================
# Initial import (used only for the plot config and sanity check).
# =============================================================================
try:
    generated_model = importlib.import_module(_variant_module)
    print(f"Loaded {_variant_module}.py successfully")
except ImportError as e:
    print(f"ERROR: Could not import {_variant_module}.py: {e}")
    print("Make sure you've run the generator first!")
    sys.exit(1)

state_names = generated_model.state_names
y0_initial  = generated_model.y0

# =============================================================================
# PLOT CONFIGURATION
# =============================================================================
# Define each subplot as a dict with:
#   - "title":   plot title
#   - "ylabel":  y-axis label
#   - "vars":    list of variable names to plot (state names OR algebraic names)
#   - "yscale":  optional, "linear" (default) or "log"
#   - "xlim":    optional, tuple (t_min, t_max), else uses full range
#
# Variable names can be ANY state in state_names OR any algebraic variable
# returned by compute_algebraics() (e.g. "PV1__u_mmHg", "VV_junc1__H_VV_out_alpha").
# If a variable isn't found, you get a warning but the script continues.
#
# Layout: PLOT_COLS controls columns; rows are computed from the number of plots.
PLOT_COLS = 2

PLOTS = [
    {
        "title":  "VV Junction Hematocrit",
        "ylabel": "Hematocrit",
        "vars":   ["VV_junc1__H_VV_out_alpha", "VV_junc1__H_VV_out_beta",
                   "VV_junc2__H_VV_out_alpha", "VV_junc2__H_VV_out_beta",
                   "VV_junc3__H_VV_out_alpha", "VV_junc3__H_VV_out_beta"],
    },
    {
        "title":  "Pressures (u_mmHg)",
        "ylabel": "Pressure (mmHg)",
        "vars": [
            "inlet__u_mmHg",
            "VV_junc1__u_mmHg",
            "VV_junc1__u_d_mmHg",
            "PV1__u_mmHg", "PV2__u_mmHg", "PV3__u_mmHg",
            "PV4__u_mmHg", "PV5__u_mmHg", "PV6__u_mmHg",
            "V1__u_mmHg", "V2__u_mmHg", "V3__u_mmHg",
            "V4__u_mmHg", "V5__u_mmHg", "V6__u_mmHg",
        ],
    },
    {
        "title":  "Flows (mm3/s)",
        "ylabel": "Flows (mm3/s)",
        "vars": [
            "inlet__u_mmHg",
            "VV_junc1__u_mmHg",
            "VV_junc1__u_d_mmHg",
            "PV1__v_mm3_s", "PV2__v_mm3_s", "PV3__v_mm3_s",
            "PV4__v_mm3_s", "PV5__v_mm3_s", "PV6__v_mm3_s",
            "V1__v_mm3_s",  "V2__v_mm3_s",  "V3__v_mm3_s",
            "V4__v_mm3_s",  "V5__v_mm3_s",  "V6__v_mm3_s",
        ],
    },
    {
        "title":  "Pericyte Resistance",
        "ylabel": "R (Js/m^6)",
        "vars":   ["PV1__R_constriction", "PV2__R_constriction"],
        "yscale": "log",
    },
    {
        "title":  "Example state variables",
        "ylabel": "State value",
        # Fall back to the first few state names if you haven't decided yet
        "vars":   list(state_names[:4]),
    },
]

# =============================================================================
# Components to probe for R, C, r, l values (edit to match your model's comps)
# =============================================================================
# Loaded but not yet consumed — reserved for a future summary-table feature.
PROBE_COMPONENTS = ['PV1', 'PV2', 'PV3', 'PV4', 'PV5', 'PV6',
                    'V1', 'V2', 'V5', 'V6',
                    'VV_junc1', 'VV_junc3']

# =============================================================================
# Configuration printout
# =============================================================================
print(f"\n{'='*60}")
print(f"Simulation Configuration [variant={MODEL_VARIANT}]")
print(f"{'='*60}")
print(f"Method: {SOLVER_METHOD}")
print(f"Time span: {T_START} to {T_END} seconds")
print(f"Output points: {N_POINTS}")
print(f"Tolerances: rtol={RTOL}, atol={ATOL}")
print(f"Max step: {MAX_STEP if MAX_STEP != np.inf else 'unlimited'}")
print(f"Number of states: {len(y0_initial)}")
print(f"Output dir: {OUTPUT_DIR}/")
print(f"Plots defined: {len(PLOTS)} (layout: {PLOT_COLS} cols)")
print(f"Number of benchmark runs: {N_RUNS}")
print(f"Live progress tracker: {'ON' if SHOW_PROGRESS else 'OFF'}")
if MODEL_VARIANT == "iter":
    print(f"Iterative unknowns: {generated_model.iter_unknown_names}")
print(f"{'='*60}\n")

# Sanity-check RHS at t=0 once before benchmarking.
print("Testing RHS at t=0...")
try:
    dydt0 = generated_model.ode_rhs(0, y0_initial)
    print(f"  ✓ RHS computed successfully")
    print(f"  First 5 derivatives: {dydt0[:5]}")
    if np.any(np.isnan(dydt0)) or np.any(np.isinf(dydt0)):
        print("  ✗ ERROR: NaN or Inf in initial RHS!")
        sys.exit(1)
    if MODEL_VARIANT == "iter":
        print(f"  iterative solution at t=0: {generated_model._iter_last_solution[0]}")
except Exception as e:
    print(f"  ✗ ERROR evaluating RHS at t=0: {e}")
    import traceback; traceback.print_exc()
    sys.exit(1)

# =============================================================================
# Live progress tracker (opt-in via SHOW_PROGRESS).
# =============================================================================
# Wraps ode_rhs to print t, nfev, wall-time, and (for iter variant) last H_means
# roughly once per second. Tiny overhead, useful for long single runs but noisy
# when N_RUNS > 1 (multiplies output by N_RUNS). State is reset per run.
PROGRESS_INTERVAL = 1.0

def _make_tracked_rhs(module, start_time):
    """Build a fresh tracker + wrapped RHS for one run."""
    progress = {"nfev": 0, "last_print": time.time(),
                "last_nfev": 0, "last_t": 0.0}
    ode_rhs = module.ode_rhs

    def tracked_rhs(t, y):
        progress["nfev"] += 1
        now = time.time()
        if now - progress["last_print"] >= PROGRESS_INTERVAL:
            elapsed = now - start_time
            pct = 100.0 * (t - T_START) / (T_END - T_START) if T_END > T_START else 0.0
            d_nfev = progress["nfev"] - progress["last_nfev"]
            d_wall = now - progress["last_print"]
            rate = d_nfev / d_wall if d_wall > 0 else 0.0
            dt_sim = t - progress["last_t"]
            sim_rate = dt_sim / d_wall if d_wall > 0 else 0.0
            remaining = (T_END - t) / sim_rate if sim_rate > 0 else float("inf")
            msg = (f"    [t={t:9.3f}/{T_END}  "
                   f"{pct:5.1f}%  "
                   f"nfev={progress['nfev']:>7d}  "
                   f"{rate:6.0f} rhs/s  "
                   f"elapsed={elapsed:6.1f}s  "
                   f"ETA={remaining:6.0f}s]")
            if MODEL_VARIANT == "iter":
                H = module._iter_last_solution[0]
                msg += f"  H=[{' '.join(f'{h:.3f}' for h in H)}]"
            print(msg, flush=True)
            progress["last_print"] = now
            progress["last_nfev"] = progress["nfev"]
            progress["last_t"] = t
        return ode_rhs(t, y)
    return tracked_rhs


def run_once():
    """Import the module fresh, run one simulation, return (wall_time, sol, module).

    Reimporting resets any module-level caches (e.g. the iterative solver's
    _iter_last_solution warm-start), so each run starts from identical state.
    """
    if _variant_module in sys.modules:
        module = importlib.reload(sys.modules[_variant_module])
    else:
        module = importlib.import_module(_variant_module)

    y0 = module.y0
    t0 = time.time()
    rhs = _make_tracked_rhs(module, t0) if SHOW_PROGRESS else module.ode_rhs

    sol = solve_ivp(
        rhs,
        [T_START, T_END],
        y0,
        method=SOLVER_METHOD,
        t_eval=np.linspace(T_START, T_END, N_POINTS),
        rtol=RTOL,
        atol=ATOL,
        max_step=MAX_STEP,
    )
    wall = time.time() - t0
    return wall, sol, module


# =============================================================================
# Benchmark loop: keep fastest run's (wall_time, sol, module)
# =============================================================================
print(f"\nRunning {N_RUNS} simulations (keeping fastest)...")
all_times = []
best = None   # (wall, sol, module)

for run_idx in range(1, N_RUNS + 1):
    try:
        wall, sol, module = run_once()
    except Exception as e:
        print(f"  run {run_idx}/{N_RUNS}: FAILED with {type(e).__name__}: {e}")
        all_times.append(float('inf'))
        continue

    status = "✓" if sol.success else "✗"
    tag = ""
    if best is None or (sol.success and wall < best[0]):
        if sol.success:
            best = (wall, sol, module)
            tag = "  (new best)"
    print(f"  run {run_idx}/{N_RUNS}: {status} wall={wall:.4f}s  "
          f"nfev={sol.nfev}  njev={sol.njev}{tag}")
    all_times.append(wall)

if best is None:
    print("\n✗ All runs failed; no successful simulation to save.")
    sys.exit(1)

wall_time, sol, generated_model = best

# =============================================================================
# Print benchmark summary
# =============================================================================
successful = [t for t in all_times if t != float('inf')]
print(f"\n{'='*60}")
print(f"Benchmark Summary [variant={MODEL_VARIANT}]")
print(f"{'='*60}")
print(f"Runs:        {N_RUNS}  ({len(successful)} successful)")
if successful:
    print(f"Min wall:    {min(successful):.4f} s   (saved)")
    print(f"Max wall:    {max(successful):.4f} s")
    print(f"Median wall: {float(np.median(successful)):.4f} s")
    print(f"Mean wall:   {float(np.mean(successful)):.4f} s")
    print(f"Std wall:    {float(np.std(successful)):.4f} s")
print(f"{'='*60}\n")

# =============================================================================
# Print saved-run details
# =============================================================================
print(f"Saved run (fastest):")
print(f"  Wall time: {wall_time:.4f} seconds")
print(f"  Points computed: {sol.t.shape[0]}")
print(f"  Function evaluations: {sol.nfev}")
print(f"  Jacobian evaluations: {sol.njev}")
print(f"  LU decompositions: {sol.nlu if hasattr(sol, 'nlu') else 'N/A'}")
print()

# =============================================================================
# Resolve all variables we need: defaults (for the existing CSV) + PLOTS vars.
# =============================================================================
# Build a single set of variables to pull out of compute_algebraics so we only
# compute each algebraic once per time point. States are read directly from sol.y.
state_index = {name: i for i, name in enumerate(state_names)}

# Default algebraics (same set the old 10sims script exported).
default_u_mmHg_vars = [
    "inlet__u_mmHg",
    "VV_junc1__u_mmHg",
    "VV_junc1__u_d_mmHg",
    "PV1__u_mmHg", "PV2__u_mmHg",
    "PV3__u_mmHg", "PV4__u_mmHg", "PV5__u_mmHg", "PV6__u_mmHg",
    "V1__u_mmHg",  "V2__u_mmHg",
    "V3__u_mmHg",  "V4__u_mmHg",  "V5__u_mmHg",  "V6__u_mmHg",
]
default_H_VV_out_vars = [
    "VV_junc1__H_VV_out_alpha",
    "VV_junc1__H_VV_out_beta",
]

# Collect every variable referenced by PLOTS (deduped, preserving order).
plot_vars_ordered = []
_seen = set()
for p in PLOTS:
    for v in p["vars"]:
        if v not in _seen:
            plot_vars_ordered.append(v)
            _seen.add(v)

# All non-state variables we need to harvest from compute_algebraics.
alg_vars_to_harvest = set()
for v in default_u_mmHg_vars + default_H_VV_out_vars + plot_vars_ordered:
    if v not in state_index:
        alg_vars_to_harvest.add(v)

print("Computing algebraic variables needed for CSVs and plots...")
if not hasattr(generated_model, 'compute_algebraics'):
    print("ERROR: module doesn't have compute_algebraics function")
    sys.exit(1)

# time_series[var] = list of values over sol.t. Empty list on first pass means
# the variable is missing — we warn and skip it downstream.
time_series = {v: [] for v in alg_vars_to_harvest}
missing_vars = set()

for i, t in enumerate(sol.t):
    alg = generated_model.compute_algebraics(t, sol.y[:, i])
    for v in alg_vars_to_harvest:
        if v in alg:
            time_series[v].append(alg[v])
        else:
            if i == 0:
                missing_vars.add(v)

for v in missing_vars:
    time_series.pop(v, None)

if missing_vars:
    print(f"  ⚠ {len(missing_vars)} variable(s) referenced in PLOTS/defaults "
          f"were not found in compute_algebraics() or state_names:")
    for v in sorted(missing_vars):
        print(f"      {v}")
    print(f"  These will be skipped in plots and CSVs.")

present_defaults_u = [v for v in default_u_mmHg_vars if v in time_series]
present_defaults_H = [v for v in default_H_VV_out_vars if v in time_series]
present_plot_vars  = [v for v in plot_vars_ordered
                      if v in state_index or v in time_series]
print(f"✓ Resolved {len(present_plot_vars)}/{len(plot_vars_ordered)} "
      f"plot variables")
print()

def series_for(var):
    """Return a numpy array of values over sol.t for any state or algebraic var."""
    if var in state_index:
        return sol.y[state_index[var], :]
    return np.asarray(time_series[var])

# =============================================================================
# Export CSV 1: all states + default algebraics (same shape as the original 10sims CSV)
# =============================================================================
print(f"Exporting default results to {CSV_OUTPUT}...")

with open(CSV_OUTPUT, 'w', newline='') as f:
    writer = csv.writer(f)

    header = ['time'] + list(state_names)
    header.extend(present_defaults_H)
    header.extend(present_defaults_u)
    writer.writerow(header)

    for i in range(len(sol.t)):
        row = [sol.t[i]] + list(sol.y[:, i])
        for v in present_defaults_H:
            row.append(time_series[v][i])
        for v in present_defaults_u:
            row.append(time_series[v][i])
        writer.writerow(row)

n_alg_in_default = len(present_defaults_H) + len(present_defaults_u)
print(f"✓ Exported {len(sol.t)} time points")
print(f"  - {len(state_names)} state variables")
print(f"  - {n_alg_in_default} algebraic variables")
print(f"  File: {CSV_OUTPUT}")

# =============================================================================
# Export CSV 2: raw data for every variable referenced in PLOTS
# =============================================================================
print(f"\nExporting plot data to {CSV_PLOTS_OUTPUT}...")

with open(CSV_PLOTS_OUTPUT, 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['time'] + present_plot_vars
    writer.writerow(header)
    for i in range(len(sol.t)):
        row = [sol.t[i]] + [series_for(v)[i] for v in present_plot_vars]
        writer.writerow(row)

print(f"✓ Exported {len(sol.t)} time points x {len(present_plot_vars)} variables")
print(f"  File: {CSV_PLOTS_OUTPUT}")

# =============================================================================
# Plotting: one subplot per entry in PLOTS
# =============================================================================
print("\nCreating plots...")

n_plots = len(PLOTS)
n_cols = max(1, PLOT_COLS)
n_rows = (n_plots + n_cols - 1) // n_cols  # ceil

fig = plt.figure(figsize=(8 * n_cols, 4 * n_rows))
gs = fig.add_gridspec(n_rows, n_cols, hspace=0.35, wspace=0.25)

for idx, plot in enumerate(PLOTS):
    r, c = divmod(idx, n_cols)
    ax = fig.add_subplot(gs[r, c])

    vars_this = [v for v in plot["vars"]
                 if v in state_index or v in time_series]
    skipped = [v for v in plot["vars"] if v not in vars_this]

    # Line colors from tab20 (works for up to ~20 lines; wraps after that).
    cmap = plt.cm.tab20
    for i, v in enumerate(vars_this):
        ax.plot(sol.t, series_for(v),
                label=v.replace("__", " "),
                linewidth=1.8,
                color=cmap(i % cmap.N))

    ax.set_title(plot.get("title", ""), fontsize=13, fontweight="bold")
    ax.set_xlabel("Time (s)", fontsize=11)
    ax.set_ylabel(plot.get("ylabel", ""), fontsize=11)
    ax.grid(True, alpha=0.3)
    if plot.get("yscale") == "log":
        ax.set_yscale("log")
    if "xlim" in plot:
        ax.set_xlim(plot["xlim"])
    if vars_this:
        ax.legend(fontsize=8, ncol=2 if len(vars_this) > 6 else 1,
                  loc="best")
    else:
        ax.text(0.5, 0.5, "(no variables resolved)",
                transform=ax.transAxes, ha="center", va="center",
                fontsize=11, color="gray")
    if skipped:
        ax.text(0.02, 0.02,
                f"skipped: {len(skipped)} var(s)",
                transform=ax.transAxes, fontsize=7, color="gray",
                ha="left", va="bottom")

plt.suptitle(
    f"{MODEL_VARIANT} variant  |  fastest of {N_RUNS}: wall={wall_time:.2f}s  |  "
    f"median={float(np.median(successful)):.2f}s  |  nfev={sol.nfev}",
    fontsize=11, y=1.0,
)
plt.savefig(PLOT_OUTPUT, dpi=150, bbox_inches="tight")
print(f"✓ Plot saved as: {PLOT_OUTPUT}")
plt.show()

print(f"\n{'='*60}")
print("Done!")
print(f"  States + default algebraics: {CSV_OUTPUT}")
print(f"  Plot data:                   {CSV_PLOTS_OUTPUT}")
print(f"  Figure:                      {PLOT_OUTPUT}")
print(f"{'='*60}")