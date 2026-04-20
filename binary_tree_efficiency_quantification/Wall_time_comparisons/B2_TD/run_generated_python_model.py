"""
Run the generated model with configurable solver settings and plotting.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time
import sys

# Import the generated model
try:
    from generated_model import ode_rhs, y0, state_names
    import generated_model
    print("Loaded generated_model.py successfully")
except ImportError as e:
    print(f"ERROR: Could not import generated_model.py: {e}")
    print("Make sure you've run the generator first!")
    sys.exit(1)

# =============================================================================
# Solver Configuration
# =============================================================================
SOLVER_METHOD = "Radau"  # Options: "BDF", "LSODA", "Radau", "RK45"
T_START = 0
T_END = 1000
N_POINTS = 1001  # Number of output points

RTOL = 1e-7  # Relative tolerance
ATOL = 1e-7  # Absolute tolerance
MAX_STEP = 5  # Maximum step size (use np.inf for unlimited)

# CSV output filename
CSV_OUTPUT = "simulation_results.csv"

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
        "vars":   ["VV_junc1__H_VV_out_alpha", "VV_junc1__H_VV_out_beta"],
    },
    {
        "title":  "Pressures (u_mmHg)",
        "ylabel": "Pressure (mmHg)",
        "vars": [
            "inlet__u_mmHg",
            "VV_junc1__u_mmHg",
            "VV_junc1__u_d_mmHg",
            "PV1__u_mmHg",
            "PV2__u_mmHg",
            "V1__u_mmHg",
            "V2__u_mmHg",
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
        "vars":   state_names[:4],
    },
]

# =============================================================================
# Components to probe for R, C, r, l values (edit to match your model's comps)
# =============================================================================
PROBE_COMPONENTS = ['PV1', 'PV2', 'PV3', 'PV4', 'PV5', 'PV6',
                    'V1', 'V2', 'V5', 'V6',
                    'VV_junc1', 'VV_junc3']

# =============================================================================
# Run Simulation
# =============================================================================
print(f"\n{'='*60}")
print(f"Simulation Configuration")
print(f"{'='*60}")
print(f"Method: {SOLVER_METHOD}")
print(f"Time span: {T_START} to {T_END} seconds")
print(f"Output points: {N_POINTS}")
print(f"Tolerances: rtol={RTOL}, atol={ATOL}")
print(f"Max step: {MAX_STEP if MAX_STEP != np.inf else 'unlimited'}")
print(f"Number of states: {len(y0)}")
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
except Exception as e:
    print(f"  ✗ ERROR evaluating RHS at t=0: {e}")
    sys.exit(1)

# =============================================================================
# Diagnostic: Jacobian diagonal at t=0 (exposes stiff states)
# =============================================================================
print("\nProbing Jacobian at initial condition...")
eps = 1e-8
f0 = ode_rhs(0, y0)
diag = np.zeros(len(y0))
for i in range(len(y0)):
    yp = y0.copy()
    h = max(abs(y0[i]) * eps, 1e-20)
    yp[i] += h
    diag[i] = (ode_rhs(0, yp)[i] - f0[i]) / h

print("Diagonal Jacobian (top 10 by magnitude):")
order = np.argsort(-np.abs(diag))
for i in order[:10]:
    tau = -1.0/diag[i] if diag[i] < 0 else np.inf
    print(f"  {state_names[i]:40s} dJ/dy = {diag[i]:+.3e}   tau = {tau:.3e}s   y = {y0[i]:+.3e}")

# =============================================================================
# Diagnostic: R, C, r, l, and R*C time constants per component
# =============================================================================
print("\nProbing R, C, and R*C per component at t=0...")
# compute_algebraics gives us the live values of R and any other pub:out
# algebraics, which matters because R is recomputed each step.
alg_t0 = generated_model.compute_algebraics(0, y0)


def _get(name):
    """Look up a value, first in compute_algebraics output, then as module-level
    constant in generated_model."""
    if name in alg_t0:
        return alg_t0[name]
    if hasattr(generated_model, name):
        return getattr(generated_model, name)
    return None


def _fmt(x):
    if isinstance(x, (int, float)) and x is not None and np.isfinite(x):
        return f"{x:.3e}"
    return "     -    "


print(f"{'component':<15}{'r':>12}{'l':>12}{'mu':>12}{'R':>15}{'C':>15}{'R*C (s)':>15}")
print("-" * 96)
for comp in PROBE_COMPONENTS:
    r  = _get(f"{comp}__r")
    l  = _get(f"{comp}__l")
    mu = _get(f"{comp}__mu")
    if mu is None:
        mu = _get(f"{comp}__mu_plasma")
    R  = _get(f"{comp}__R")
    C  = _get(f"{comp}__C")
    RC = R * C if (isinstance(R, (int, float)) and isinstance(C, (int, float))) else None
    print(f"{comp:<15}{_fmt(r):>12}{_fmt(l):>12}{_fmt(mu):>12}{_fmt(R):>15}{_fmt(C):>15}{_fmt(RC):>15}")

print("\nNote: R*C is the natural time constant of q_C dynamics.")
print("Values below ~1e-6 s indicate an unphysically stiff component that the")
print("solver cannot integrate over 1-second timescales.\n")

# =============================================================================
# Progress tracker
# =============================================================================
# solve_ivp doesn't expose a step callback, but it calls the RHS many times per
# step. We wrap ode_rhs to watch how far `t` has advanced and print a progress
# bar when it ticks past a threshold. Cheap — just a few comparisons per call.
class ProgressTracker:
    def __init__(self, t_start, t_end, bar_width=40, update_interval=0.5):
        self.t_start = t_start
        self.t_end = t_end
        self.span = max(t_end - t_start, 1e-30)
        self.bar_width = bar_width
        self.update_interval = update_interval  # wall-clock seconds between redraws
        self.max_t_seen = t_start
        self.last_print = 0.0
        self.wall_start = time.time()
        self.nfev = 0

    def wrap(self, rhs_fn):
        def wrapped(t, y):
            self.nfev += 1
            # RHS can be called at both accepted and trial points; track the max
            if t > self.max_t_seen:
                self.max_t_seen = t
            now = time.time()
            if now - self.last_print >= self.update_interval:
                self._print(now)
                self.last_print = now
            return rhs_fn(t, y)
        return wrapped

    def _print(self, now):
        frac = min(max((self.max_t_seen - self.t_start) / self.span, 0.0), 1.0)
        filled = int(frac * self.bar_width)
        bar = "█" * filled + "░" * (self.bar_width - filled)
        elapsed = now - self.wall_start
        # ETA based on linear extrapolation of progress so far
        if frac > 1e-6:
            eta = elapsed * (1 - frac) / frac
            eta_str = f"ETA {eta:6.1f}s"
        else:
            eta_str = "ETA   --- "
        # \r rewrites the same line; flush so it shows up promptly
        sys.stdout.write(
            f"\r  [{bar}] {frac*100:5.1f}%  t={self.max_t_seen:9.3f}/{self.t_end:g}"
            f"  nfev={self.nfev:7d}  elapsed {elapsed:6.1f}s  {eta_str}"
        )
        sys.stdout.flush()

    def finalize(self, success):
        # Force one last redraw at 100% (or wherever it actually got to) and newline
        self.max_t_seen = self.t_end if success else self.max_t_seen
        self._print(time.time())
        sys.stdout.write("\n")
        sys.stdout.flush()


print(f"\nRunning simulation...")
tracker = ProgressTracker(T_START, T_END)
wrapped_rhs = tracker.wrap(ode_rhs)

start_time = time.time()
sol = solve_ivp(
    wrapped_rhs,
    [T_START, T_END],
    y0,
    method=SOLVER_METHOD,
    t_eval=np.linspace(T_START, T_END, N_POINTS),
    rtol=RTOL,
    atol=ATOL,
    max_step=MAX_STEP,
)
wall_time = time.time() - start_time
tracker.finalize(sol.success)

# =============================================================================
# Print Results
# =============================================================================
print(f"\n{'='*60}")
print(f"Simulation Results")
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
    print(f"Last successful t: {sol.t[-1] if len(sol.t) else 'never started'}")
    sys.exit(1)

print(f"{'='*60}\n")

# =============================================================================
# Compute ALL algebraics so any plotted/exported variable is available
# =============================================================================
print("Computing algebraic variables at every output time...")

if not hasattr(generated_model, 'compute_algebraics'):
    print("ERROR: generated_model.py doesn't have compute_algebraics function")
    sys.exit(1)

# Collect every algebraic variable requested by any plot AND the default u_mmHg
# set for backward-compatible CSV export. We evaluate compute_algebraics once
# per time point and pull everything we need from the returned dict.
requested_vars = set()
for p in PLOTS:
    requested_vars.update(p["vars"])
# Keep the historical CSV columns so downstream scripts don't break
csv_algebraic_vars = [
    "inlet__u_mmHg", "VV_junc1__u_mmHg", "VV_junc1__u_d_mmHg",
    "PV1__u_mmHg", "PV2__u_mmHg", "V1__u_mmHg", "V2__u_mmHg",
    "VV_junc1__H_VV_out_alpha", "VV_junc1__H_VV_out_beta",
]
requested_vars.update(csv_algebraic_vars)

# Remove state names from the algebraic-fetch list (they come straight from sol.y)
state_set = set(state_names)
alg_names_to_fetch = [v for v in requested_vars if v not in state_set]

# Build {var: array} for algebraics. Figure out which names are actually
# returned by compute_algebraics on the first call; skip missing ones w/ warn.
first_alg = generated_model.compute_algebraics(sol.t[0], sol.y[:, 0])
available = set(first_alg.keys())
missing = [v for v in alg_names_to_fetch if v not in available]
if missing:
    print(f"  ⚠ {len(missing)} requested variable(s) not found in compute_algebraics():")
    for m in missing:
        if m not in state_set:
            print(f"      {m}")
alg_names_to_fetch = [v for v in alg_names_to_fetch if v in available]

alg_data = {v: np.empty(len(sol.t)) for v in alg_names_to_fetch}
alg_data_for_t0_cached = first_alg
for i, t in enumerate(sol.t):
    a = alg_data_for_t0_cached if i == 0 else generated_model.compute_algebraics(t, sol.y[:, i])
    for v in alg_names_to_fetch:
        alg_data[v][i] = a[v]
print(f"  ✓ Extracted {len(alg_names_to_fetch)} algebraic variables\n")


def series_for(name):
    """Return the time series for a variable, whether it's a state or algebraic."""
    if name in state_set:
        idx = state_names.index(name)
        return sol.y[idx, :]
    if name in alg_data:
        return alg_data[name]
    return None


# =============================================================================
# Export Results to CSV (states + algebraics)
# =============================================================================
print(f"Exporting results to {CSV_OUTPUT}...")
import csv

with open(CSV_OUTPUT, 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['time'] + list(state_names)
    csv_alg_cols = [v for v in csv_algebraic_vars if v in alg_data]
    header.extend(csv_alg_cols)
    writer.writerow(header)
    for i in range(len(sol.t)):
        row = [sol.t[i]] + list(sol.y[:, i]) + [alg_data[v][i] for v in csv_alg_cols]
        writer.writerow(row)
print(f"✓ Exported {len(sol.t)} time points")
print(f"  - {len(state_names)} state variables")
print(f"  - {len(csv_alg_cols)} algebraic variables")
print(f"  File: {CSV_OUTPUT}\n")

# =============================================================================
# Plotting
# =============================================================================
print("Creating plots...")
n_plots = len(PLOTS)
n_cols = max(1, min(PLOT_COLS, n_plots))
n_rows = int(np.ceil(n_plots / n_cols))

fig, axes = plt.subplots(n_rows, n_cols, figsize=(7 * n_cols, 4 * n_rows),
                         squeeze=False)
axes_flat = axes.flatten()

for idx, spec in enumerate(PLOTS):
    ax = axes_flat[idx]
    cmap = plt.cm.tab10(np.linspace(0, 1, max(len(spec["vars"]), 1)))
    plotted_any = False
    for v, color in zip(spec["vars"], cmap):
        series = series_for(v)
        if series is None:
            print(f"  ⚠ [{spec['title']}] variable not found: {v}")
            continue
        label = v.replace("__", " ")
        ax.plot(sol.t, series, label=label, linewidth=1.8, color=color)
        plotted_any = True
    ax.set_title(spec.get("title", ""), fontsize=13, fontweight="bold")
    ax.set_xlabel("Time (s)", fontsize=11)
    ax.set_ylabel(spec.get("ylabel", ""), fontsize=11)
    ax.set_yscale(spec.get("yscale", "linear"))
    if "xlim" in spec:
        ax.set_xlim(spec["xlim"])
    ax.grid(True, alpha=0.3)
    if plotted_any:
        ax.legend(fontsize=8, ncol=1 if len(spec["vars"]) <= 4 else 2)

# Hide any unused subplots (if n_plots doesn't fill the grid)
for j in range(n_plots, len(axes_flat)):
    axes_flat[j].axis("off")

plt.tight_layout()
plt.savefig("simulation_results.png", dpi=150, bbox_inches="tight")
print("✓ Plot saved as: simulation_results.png")
plt.show()

print(f"\n{'='*60}")
print("Done!")
print(f"{'='*60}")