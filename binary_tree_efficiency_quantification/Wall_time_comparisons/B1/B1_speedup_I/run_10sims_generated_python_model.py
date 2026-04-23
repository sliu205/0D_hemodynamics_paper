"""
Run the generated model multiple times and report the shortest wall time.

Supports both the time-dynamics model (generated_model.py) and the iterative
model (generated_model_iter.py). Toggle with MODEL_VARIANT below. Solver
settings are held constant across variants so wall-time and accuracy are
directly comparable.

Benchmarking:
  - Runs the simulation N_RUNS times.
  - Each run reimports the model module fresh (importlib.reload) so the
    iterative solver's warm-start cache does not give later runs an unfair
    advantage.
  - Keeps only the fastest run's results; CSV and PNG correspond to that run.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time
import sys
import importlib

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

# Output directory (created next to this script if it doesn't exist).
OUTPUT_DIR = "sim-results"
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Variant-tagged output filenames so runs don't clobber each other.
CSV_OUTPUT = os.path.join(OUTPUT_DIR, f"simulation_results_{MODEL_VARIANT}.csv")
PNG_OUTPUT = os.path.join(OUTPUT_DIR, f"simulation_results_{MODEL_VARIANT}.png")


def run_once():
    """Import the module fresh, run one simulation, return (wall_time, sol, module).

    Reimporting resets any module-level caches (e.g. the iterative solver's
    _iter_last_solution warm-start), so each run starts from identical state.
    """
    if _variant_module in sys.modules:
        module = importlib.reload(sys.modules[_variant_module])
    else:
        module = importlib.import_module(_variant_module)

    ode_rhs = module.ode_rhs
    y0 = module.y0

    t0 = time.time()
    sol = solve_ivp(
        ode_rhs,
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
# Startup: import once just to validate and print config.
# =============================================================================
try:
    generated_model = importlib.import_module(_variant_module)
    print(f"Loaded {_variant_module}.py successfully")
except ImportError as e:
    print(f"ERROR: Could not import {_variant_module}.py: {e}")
    print("Make sure you've run the generator first!")
    sys.exit(1)

state_names = generated_model.state_names
y0_initial = generated_model.y0

print(f"\n{'='*60}")
print(f"Simulation Configuration [variant={MODEL_VARIANT}]")
print(f"{'='*60}")
print(f"Method: {SOLVER_METHOD}")
print(f"Time span: {T_START} to {T_END} seconds")
print(f"Output points: {N_POINTS}")
print(f"Tolerances: rtol={RTOL}, atol={ATOL}")
print(f"Max step: {MAX_STEP if MAX_STEP != np.inf else 'unlimited'}")
print(f"Number of states: {len(y0_initial)}")
print(f"Number of benchmark runs: {N_RUNS}")
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
except Exception as e:
    print(f"  ✗ ERROR evaluating RHS at t=0: {e}")
    import traceback; traceback.print_exc()
    sys.exit(1)

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
# Compute Algebraic Variables for Plotting AND CSV Export
# =============================================================================
print("Computing algebraic variables (u_mmHg, H_VV_out, etc.)...")

if not hasattr(generated_model, 'compute_algebraics'):
    print("ERROR: module doesn't have compute_algebraics function")
    sys.exit(1)

u_mmHg_vars = [
    "inlet__u_mmHg",
    "VV_junc1__u_mmHg",
    "VV_junc1__u_d_mmHg",
    "PV1__u_mmHg",
    "PV2__u_mmHg",
    "V1__u_mmHg",
    "V2__u_mmHg"
]

u_mmHg_data = {var: [] for var in u_mmHg_vars}
H_VV_out_alpha_vals = []
H_VV_out_beta_vals = []

for i, t in enumerate(sol.t):
    alg_vars = generated_model.compute_algebraics(t, sol.y[:, i])

    for var in u_mmHg_vars:
        if var in alg_vars:
            u_mmHg_data[var].append(alg_vars[var])

    if 'VV_junc1__H_VV_out_alpha' in alg_vars:
        H_VV_out_alpha_vals.append(alg_vars['VV_junc1__H_VV_out_alpha'])
    if 'VV_junc1__H_VV_out_beta' in alg_vars:
        H_VV_out_beta_vals.append(alg_vars['VV_junc1__H_VV_out_beta'])

computed_vars = [var for var, data in u_mmHg_data.items() if len(data) > 0]
print(f"✓ Computed {len(computed_vars)} u_mmHg variables")
print(f"✓ Computed H_VV_out_alpha: {len(H_VV_out_alpha_vals) > 0}")
print(f"✓ Computed H_VV_out_beta: {len(H_VV_out_beta_vals) > 0}\n")

# =============================================================================
# Export Results to CSV (states + algebraics)
# =============================================================================
print(f"Exporting results to {CSV_OUTPUT}...")

import csv

with open(CSV_OUTPUT, 'w', newline='') as f:
    writer = csv.writer(f)

    header = ['time'] + state_names
    if H_VV_out_alpha_vals:
        header.append('VV_junc1__H_VV_out_alpha')
    if H_VV_out_beta_vals:
        header.append('VV_junc1__H_VV_out_beta')
    for var in u_mmHg_vars:
        if len(u_mmHg_data[var]) > 0:
            header.append(var)
    writer.writerow(header)

    for i in range(len(sol.t)):
        row = [sol.t[i]] + list(sol.y[:, i])
        if H_VV_out_alpha_vals:
            row.append(H_VV_out_alpha_vals[i])
        if H_VV_out_beta_vals:
            row.append(H_VV_out_beta_vals[i])
        for var in u_mmHg_vars:
            if len(u_mmHg_data[var]) > 0:
                row.append(u_mmHg_data[var][i])
        writer.writerow(row)

n_algebraics = len(header) - len(state_names) - 1  # -1 for time column
print(f"✓ Exported {len(sol.t)} time points")
print(f"  - {len(state_names)} state variables")
print(f"  - {n_algebraics} algebraic variables")
print(f"  File: {CSV_OUTPUT}")

# =============================================================================
# Plotting
# =============================================================================
print("Creating plots...")

fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

ax1 = fig.add_subplot(gs[0, :])
if H_VV_out_alpha_vals:
    ax1.plot(sol.t, H_VV_out_alpha_vals, label="H_VV_out_alpha", linewidth=2)
if H_VV_out_beta_vals:
    ax1.plot(sol.t, H_VV_out_beta_vals, label="H_VV_out_beta", linewidth=2)
ax1.set_xlabel("Time (s)", fontsize=12)
ax1.set_ylabel("Hematocrit", fontsize=12)
ax1.set_title(f"VV Junction Hematocrit (H_VV_out)  [{MODEL_VARIANT}]",
              fontsize=14, fontweight="bold")
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

ax2 = fig.add_subplot(gs[1, :])
colors = plt.cm.tab10(np.linspace(0, 1, len(u_mmHg_vars)))
for (var, data), color in zip(u_mmHg_data.items(), colors):
    if len(data) > 0:
        clean_name = var.replace("__", " ").replace("_", " ")
        ax2.plot(sol.t[:len(data)], data, label=clean_name, linewidth=2, color=color)
ax2.set_xlabel("Time (s)", fontsize=12)
ax2.set_ylabel("Pressure (mmHg)", fontsize=12)
ax2.set_title("Pressures at All Locations (u_mmHg)", fontsize=14, fontweight="bold")
ax2.legend(fontsize=9, ncol=2)
ax2.grid(True, alpha=0.3)

ax3 = fig.add_subplot(gs[2, 0])
for i in range(min(4, len(state_names))):
    ax3.plot(sol.t, sol.y[i, :], label=state_names[i], linewidth=2)
ax3.set_xlabel("Time (s)", fontsize=11)
ax3.set_ylabel("State Value", fontsize=11)
ax3.set_title("State Variables (1-4)", fontsize=12, fontweight="bold")
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

ax4 = fig.add_subplot(gs[2, 1])
ax4.axis('off')
_successful = [t for t in all_times if t != float('inf')]
summary_text = f"""
Simulation Summary (fastest of {N_RUNS} runs)
{'='*36}

Variant: {MODEL_VARIANT}
Module:  {_variant_module}

Method: {SOLVER_METHOD}
Min wall time: {wall_time:.4f} s
Median wall:   {float(np.median(_successful)):.4f} s
Mean wall:     {float(np.mean(_successful)):.4f} s
Points: {sol.t.shape[0]}
States: {len(y0_initial)}

Function Evals: {sol.nfev}
Jacobian Evals: {sol.njev}

Tolerances:
  rtol = {RTOL}
  atol = {ATOL}
  max_step = {MAX_STEP if MAX_STEP != np.inf else 'unlimited'}

Time: [{T_START}, {T_END}] s
Output: {CSV_OUTPUT}
"""
ax4.text(0.05, 0.5, summary_text, fontsize=10, family='monospace',
        verticalalignment='center')

plt.savefig(PNG_OUTPUT, dpi=150, bbox_inches="tight")
print(f"✓ Plot saved as: {PNG_OUTPUT}")
plt.show()

print(f"\n{'='*60}")
print("Done!")
print(f"{'='*60}")