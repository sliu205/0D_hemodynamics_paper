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

# Run simulation with timing
print(f"\nRunning simulation...")
start_time = time.time()

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

wall_time = time.time() - start_time

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
    sys.exit(1)

print(f"{'='*60}\n")

# =============================================================================
# Compute Algebraic Variables for Plotting AND CSV Export
# =============================================================================
print("Computing algebraic variables (u_mmHg, H_VV_out, etc.)...")

# Check if compute_algebraics exists in the generated model
if not hasattr(generated_model, 'compute_algebraics'):
    print("ERROR: generated_model.py doesn't have compute_algebraics function")
    print("Please regenerate the model using the latest generate_model.py")
    sys.exit(1)

# Storage for u_mmHg values
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

# Compute algebraic variables at each time point
for i, t in enumerate(sol.t):
    alg_vars = generated_model.compute_algebraics(t, sol.y[:, i])
    
    # Extract u_mmHg values
    for var in u_mmHg_vars:
        if var in alg_vars:
            u_mmHg_data[var].append(alg_vars[var])
    
    # Extract H_VV_out values
    if 'VV_junc1__H_VV_out_alpha' in alg_vars:
        H_VV_out_alpha_vals.append(alg_vars['VV_junc1__H_VV_out_alpha'])
    if 'VV_junc1__H_VV_out_beta' in alg_vars:
        H_VV_out_beta_vals.append(alg_vars['VV_junc1__H_VV_out_beta'])

# Check which variables were successfully computed
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
    
    # Build header: time + states + algebraics we're plotting
    header = ['time'] + state_names
    
    # Add H_VV_out if available
    if H_VV_out_alpha_vals:
        header.append('VV_junc1__H_VV_out_alpha')
    if H_VV_out_beta_vals:
        header.append('VV_junc1__H_VV_out_beta')
    
    # Add u_mmHg variables that were computed
    for var in u_mmHg_vars:
        if len(u_mmHg_data[var]) > 0:
            header.append(var)
    
    writer.writerow(header)
    
    # Write data
    for i in range(len(sol.t)):
        row = [sol.t[i]] + list(sol.y[:, i])
        
        # Add H_VV_out values
        if H_VV_out_alpha_vals:
            row.append(H_VV_out_alpha_vals[i])
        if H_VV_out_beta_vals:
            row.append(H_VV_out_beta_vals[i])
        
        # Add u_mmHg values
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

# Plot 1: H_VV_out alpha and beta
ax1 = fig.add_subplot(gs[0, :])
if H_VV_out_alpha_vals:
    ax1.plot(sol.t, H_VV_out_alpha_vals, label="H_VV_out_alpha", linewidth=2)
if H_VV_out_beta_vals:
    ax1.plot(sol.t, H_VV_out_beta_vals, label="H_VV_out_beta", linewidth=2)
ax1.set_xlabel("Time (s)", fontsize=12)
ax1.set_ylabel("Hematocrit", fontsize=12)
ax1.set_title("VV Junction Hematocrit (H_VV_out)", fontsize=14, fontweight="bold")
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: All u_mmHg values
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

# Plot 3: State variables (first 4)
ax3 = fig.add_subplot(gs[2, 0])
for i in range(min(4, len(state_names))):
    ax3.plot(sol.t, sol.y[i, :], label=state_names[i], linewidth=2)
ax3.set_xlabel("Time (s)", fontsize=11)
ax3.set_ylabel("State Value", fontsize=11)
ax3.set_title("State Variables (1-4)", fontsize=12, fontweight="bold")
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Plot 4: Summary text
ax4 = fig.add_subplot(gs[2, 1])
ax4.axis('off')
summary_text = f"""
Simulation Summary
{'='*35}

Method: {SOLVER_METHOD}
Wall Time: {wall_time:.4f} s
Points: {sol.t.shape[0]}
States: {len(y0)}

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

plt.savefig("simulation_results.png", dpi=150, bbox_inches="tight")
print("✓ Plot saved as: simulation_results.png")
plt.show()

print(f"\n{'='*60}")
print("Done!")
print(f"{'='*60}")