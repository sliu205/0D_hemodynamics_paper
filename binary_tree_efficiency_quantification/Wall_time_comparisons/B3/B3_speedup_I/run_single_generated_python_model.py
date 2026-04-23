"""
Run the generated model with configurable solver settings and plotting.

Supports both the time-dynamics model (generated_model.py) and the iterative
model (generated_model_iter.py). Toggle with MODEL_VARIANT below. Solver
settings are held constant across variants so wall-time and accuracy are
directly comparable.

Plot configuration:
  The PLOTS list below defines subplots as {title, ylabel, vars, ...} dicts.
  Each `vars` entry is plotted as its own line on the subplot. Variables can
  be any state name or any algebraic variable name (e.g. "PV1__u_mmHg",
  "VV_junc1__H_VV_out_alpha"). Missing variables trigger a warning and are
  skipped; the script continues.

Output files (all under OUTPUT_DIR):
  simulation_results.csv       -- all states + default u_mmHg + H_VV_out
  simulation_plots_data.csv    -- time + every variable referenced in PLOTS
  simulation_results.png       -- the plot figure
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

try:
    generated_model = importlib.import_module(_variant_module)
    ode_rhs = generated_model.ode_rhs
    y0 = generated_model.y0
    state_names = generated_model.state_names
    print(f"Loaded {_variant_module}.py successfully")
except ImportError as e:
    print(f"ERROR: Could not import {_variant_module}.py: {e}")
    print("Make sure you've run the generator first!")
    sys.exit(1)

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
# Output directory + filenames
# =============================================================================
# All outputs go into this folder; it's created if it doesn't exist.
OUTPUT_DIR = "sim_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSV_OUTPUT       = os.path.join(OUTPUT_DIR, "simulation_results.csv")        # All states + default algebraics
CSV_PLOTS_OUTPUT = os.path.join(OUTPUT_DIR, "simulation_plots_data.csv")    # All variables from PLOTS
PLOT_OUTPUT      = os.path.join(OUTPUT_DIR, "simulation_results.png")       # Plot figure

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
                   "VV_junc3__H_VV_out_alpha", "VV_junc3__H_VV_out_beta",
                   "VV_junc4__H_VV_out_alpha", "VV_junc4__H_VV_out_beta",
                   "VV_junc5__H_VV_out_alpha", "VV_junc5__H_VV_out_beta",
                   "VV_junc6__H_VV_out_alpha", "VV_junc6__H_VV_out_beta",
                   "VV_junc7__H_VV_out_alpha", "VV_junc7__H_VV_out_beta"],
    },
    {
        "title":  "Pressures (u_mmHg)",
        "ylabel": "Pressure (mmHg)",
        "vars": [
            "inlet__u_mmHg",
            "V1__u_mmHg", "V2__u_mmHg", "V3__u_mmHg",
            "V4__u_mmHg", "V5__u_mmHg", "V6__u_mmHg",
            "V7__u_mmHg", "V8__u_mmHg", "V9__u_mmHg",
            "V10__u_mmHg", "V11__u_mmHg", "V12__u_mmHg","V13__u_mmHg", "V14__u_mmHg"
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
            "V1__v_mm3_s", "V2__v_mm3_s", "V3__v_mm3_s",
            "V4__v_mm3_s", "V5__v_mm3_s", "V6__v_mm3_s",
            "V7__v_mm3_s", "V8__v_mm3_s", "V9__v_mm3_s",
            "V10__v_mm3_s", "V11__v_mm3_s", "V12__v_mm3_s",
            "V13__v_mm3_s", "V14__v_mm3_s"
        ],
    },
    {
        "title":  "Pericyte Resistance",
        "ylabel": "R (Js/m^6)",
        "vars":   ["PV7__R_constriction"],
        "yscale": "log",
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
# Run Simulation
# =============================================================================
print(f"\n{'='*60}")
print(f"Simulation Configuration [variant={MODEL_VARIANT}]")
print(f"{'='*60}")
print(f"Method: {SOLVER_METHOD}")
print(f"Time span: {T_START} to {T_END} seconds")
print(f"Output points: {N_POINTS}")
print(f"Tolerances: rtol={RTOL}, atol={ATOL}")
print(f"Max step: {MAX_STEP if MAX_STEP != np.inf else 'unlimited'}")
print(f"Number of states: {len(y0)}")
print(f"Output dir: {OUTPUT_DIR}/")
print(f"Plots defined: {len(PLOTS)} (layout: {PLOT_COLS} cols)")
if MODEL_VARIANT == "iter":
    print(f"Iterative unknowns: {generated_model.iter_unknown_names}")
print(f"{'='*60}\n")

# Test RHS at t=0
print("Testing RHS at t=0...")
try:
    dydt0 = ode_rhs(0, y0)
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

# Run simulation with timing
print(f"\nRunning simulation...")
start_time = time.time()

# =============================================================================
# Live progress tracker
# =============================================================================
# Wrap ode_rhs to print t, nfev, wall-time, and (for iter variant) last H_means
# roughly once per second. Tiny overhead, huge QoL gain during long runs.
PROGRESS_INTERVAL = 1.0  # seconds between updates

_progress = {
    "nfev": 0,
    "last_print": time.time(),
    "last_nfev": 0,
    "last_t": 0.0,
    "last_len": 0,
}

BAR_WIDTH = 30  # number of characters in the visual progress bar

def _format_eta(seconds):
    """Format seconds as h:mm:ss / m:ss, or '--:--' if unknown."""
    if not np.isfinite(seconds) or seconds < 0:
        return "--:--"
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h > 0:
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:d}:{s:02d}"

def tracked_rhs(t, y):
    _progress["nfev"] += 1
    now = time.time()
    if now - _progress["last_print"] >= PROGRESS_INTERVAL:
        elapsed = now - start_time
        pct = 100.0 * (t - T_START) / (T_END - T_START) if T_END > T_START else 0.0
        pct = max(0.0, min(100.0, pct))
        d_nfev = _progress["nfev"] - _progress["last_nfev"]
        d_wall = now - _progress["last_print"]
        rate = d_nfev / d_wall if d_wall > 0 else 0.0
        dt_sim = t - _progress["last_t"]
        sim_rate = dt_sim / d_wall if d_wall > 0 else 0.0
        remaining = (T_END - t) / sim_rate if sim_rate > 0 else float("inf")

        # Build a visual bar like [██████████░░░░░░░░░░]
        filled = int(BAR_WIDTH * pct / 100.0)
        bar = "█" * filled + "░" * (BAR_WIDTH - filled)

        msg = (f"  |{bar}| {pct:5.1f}%  "
               f"t={t:8.2f}/{T_END:g}  "
               f"nfev={_progress['nfev']:>7d}  "
               f"{rate:5.0f} rhs/s  "
               f"elapsed={_format_eta(elapsed)}  "
               f"ETA={_format_eta(remaining)}")
        if MODEL_VARIANT == "iter":
            H = generated_model._iter_last_solution[0]
            msg += f"  H=[{' '.join(f'{h:.3f}' for h in H)}]"

        # Pad to overwrite any leftover characters from a previous, longer line,
        # then return the cursor to the start of the line with \r (no newline).
        line = msg.ljust(_progress["last_len"])
        sys.stdout.write("\r" + line)
        sys.stdout.flush()

        _progress["last_print"] = now
        _progress["last_nfev"] = _progress["nfev"]
        _progress["last_t"] = t
        _progress["last_len"] = len(msg)
    return ode_rhs(t, y)

sol = solve_ivp(
    tracked_rhs,
    [T_START, T_END],
    y0,
    method=SOLVER_METHOD,
    t_eval=np.linspace(T_START, T_END, N_POINTS),
    rtol=RTOL,
    atol=ATOL,
    max_step=MAX_STEP,
)

# Move to a new line so subsequent prints don't overwrite the progress bar
sys.stdout.write("\n")
sys.stdout.flush()

wall_time = time.time() - start_time

# =============================================================================
# Print Results
# =============================================================================
print(f"\n{'='*60}")
print(f"Simulation Results [variant={MODEL_VARIANT}]")
print(f"{'='*60}")
if sol.success:
    print(f"✓ SUCCESS!")
    print(f"Wall time: {wall_time:.4f} seconds")
    print(f"Points computed: {sol.t.shape[0]}")
    print(f"Function evaluations: {sol.nfev}")
    print(f"Jacobian evaluations: {sol.njev}")
    print(f"LU decompositions: {sol.nlu if hasattr(sol, 'nlu') else 'N/A'}")
else:
    print(f"✗ FAILED: {sol.message}")
    sys.exit(1)

print(f"{'='*60}\n")

# =============================================================================
# Resolve all variables we need: defaults (for the existing CSV) + PLOTS vars.
# =============================================================================
# Build a single set of variables to pull out of compute_algebraics so we only
# compute each algebraic once per time point. States are read directly from sol.y.
state_index = {name: i for i, name in enumerate(state_names)}

# Default algebraics (unchanged from original script)
default_u_mmHg_vars = [
    "inlet__u_mmHg",
    "VV_junc1__u_mmHg",
    "VV_junc1__u_d_mmHg",
    "PV1__u_mmHg", "PV2__u_mmHg",
    "V1__u_mmHg",  "V2__u_mmHg",
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

# time_series[var] = list of values over sol.t. Empty list means not found in
# the first call -> variable is missing (we'll warn once at the end).
time_series = {v: [] for v in alg_vars_to_harvest}
missing_vars = set()

for i, t in enumerate(sol.t):
    alg = generated_model.compute_algebraics(t, sol.y[:, i])
    for v in alg_vars_to_harvest:
        if v in alg:
            time_series[v].append(alg[v])
        else:
            # Mark as missing on the first pass; don't append anything.
            if i == 0:
                missing_vars.add(v)

# Drop missing vars from time_series so downstream code doesn't hit IndexError.
for v in missing_vars:
    time_series.pop(v, None)

# Warn about missing vars (non-fatal).
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
# Export Results to CSV 1: existing states + default algebraics (untouched)
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
# Export Results to CSV 2: raw data for every variable referenced in PLOTS
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

plt.suptitle(f"{MODEL_VARIANT} variant  |  wall={wall_time:.2f}s  |  "
             f"nfev={sol.nfev}",
             fontsize=11, y=1.0)
plt.savefig(PLOT_OUTPUT, dpi=150, bbox_inches="tight")
print(f"✓ Plot saved as: {PLOT_OUTPUT}")
plt.show()

print(f"\n{'='*60}")
print("Done!")
print(f"  States + default algebraics: {CSV_OUTPUT}")
print(f"  Plot data:                   {CSV_PLOTS_OUTPUT}")
print(f"  Figure:                      {PLOT_OUTPUT}")
print(f"{'='*60}")