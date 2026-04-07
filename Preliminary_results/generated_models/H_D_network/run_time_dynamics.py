"""
run_HD_network.py
-----------------
Runner script for H_D_network.py — microvascular hemodynamic network model.

What this model is:
  - A microvascular network with physically-motivated hematocrit (H) dynamics
  - State variables : hematocrit in capillaries/junctions, RBC volume, compliance volumes
  - Algebraic vars  : viscosity (mu), resistance (R), flow (v), pressure (u)
  - ODE solver      : scipy vode/bdf (implicit, stiff)
  - Time span       : 0 to 10 seconds, 500 time points

Context — the circular dependency this solves:
  H -> mu (Fahraeus-Lindqvist) -> R (Poiseuille) -> Q (Kirchhoff) -> H (Zweifach-Fung)
  Rather than iterating to algebraic closure, hematocrit advects in physical time
  and the steady state emerges as a natural equilibrium.

Usage:
  python run_HD_network.py

Compatibility fix applied automatically:
  numpy >= 1.24 removed the 2-arg form of vstack(a, b).
  All occurrences in the model are replaced with clip(x, lo, hi)
  which is the mathematically intended operation.

Outputs:
  HD_network_results.png  -- 6-panel figure
  HD_network_results.csv  -- key variables vs time
"""

import sys
import re
import time
import warnings
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# =============================================================================
# 1. LOAD AND PATCH THE MODEL FOR NUMPY COMPATIBILITY
# =============================================================================
# numpy >= 1.24 requires vstack((a, b)) -- the CellML export used old 2-arg API.
# The pattern is always a clamp: amin(vstack(amax(vstack(x,lo),0),hi),0)
# which is mathematically equivalent to clip(x, lo, hi).

_MODEL_SRC = "/home/sliu205/0D_hemodynamics_paper/Preliminary_results/generated_models/H_D_network/H_D_network.py"

with open(_MODEL_SRC, "r") as f:
    src = f.read()

_VSTACK_PATTERN = (
    r'amin\(vstack\(amax\(vstack\((algebraic\[\d+\]), constants\[16\]\),0\),'
    r' 1\.00000-constants\[16\]\),0\)'
)
src_fixed, n_fixed = re.subn(
    _VSTACK_PATTERN,
    r'clip(\1, constants[16], 1.00000-constants[16])',
    src
)

# Execute patched source into an isolated namespace
_ns = {}
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    exec(compile(src_fixed, _MODEL_SRC, "exec"), _ns)

sizeStates    = _ns["sizeStates"]
sizeAlgebraic = _ns["sizeAlgebraic"]
sizeConstants = _ns["sizeConstants"]
solve_model   = _ns["solve_model"]

# =============================================================================
# 2. RUN THE MODEL
# =============================================================================

print("=" * 62)
print("  Microvascular H-D Network Solver")
print("=" * 62)
print(f"  numpy compat patches applied : {n_fixed} vstack -> clip")
print(f"  State variables              : {sizeStates}")
print(f"  Algebraic variables          : {sizeAlgebraic}")
print(f"  Constants                    : {sizeConstants}")
print()
print("  Solving ODE (vode/bdf)  t in [0, 10] s ...")

t_wall_start = time.perf_counter()
with warnings.catch_warnings():
    warnings.simplefilter("ignore")   # suppress transient divide-by-zero
    voi, states, algebraic = solve_model()
elapsed = time.perf_counter() - t_wall_start

print(f"  Solved.  Wall time: {elapsed:.2f} s\n")

# =============================================================================
# 3. EXTRACT VARIABLES
#    Index references verified against createLegends() in H_D_network.py
# =============================================================================

# Hematocrit -- PP capillary (first segment, dimensionless 0-1)
H_link_R_cap  = states[0]     # right hematocrit link
H_link_L_cap  = states[1]     # left hematocrit link
H_down_cap    = states[2]     # downstream hematocrit
H_mean_cap    = algebraic[12] # mean hematocrit (algebraic)

# Hematocrit -- VV junction 1 inputs (Zweifach-Fung splitting)
H_from1       = states[5]
H_from2       = states[6]
H_from3       = states[7]
H_from4       = states[8]

# VV junction 1 -- alpha branch output after splitting rule
H_VV1_alpha   = states[9]

# Pressure [mmHg]
u_cap_mmHg    = algebraic[17]
u_VV1_mmHg    = algebraic[25]

# Flow [mm3/s]
v_cap_mm3s    = algebraic[19]
v_VV1_mm3s    = algebraic[48]

# Viscosity and Resistance -- PP capillary
mu_cap        = algebraic[14]  # Fahraeus-Lindqvist viscosity [Js/m3]
R_cap         = algebraic[15]  # Poiseuille resistance [Js/m6]

# =============================================================================
# 4. STEADY-STATE SUMMARY
# =============================================================================

print("  Steady-state values at t = 10 s")
print("  " + "-" * 46)
print(f"  H_link_R  (PP cap)   : {H_link_R_cap[-1]:.4f}  (dimensionless)")
print(f"  H_link_L  (PP cap)   : {H_link_L_cap[-1]:.4f}  (dimensionless)")
print(f"  H_down    (PP cap)   : {H_down_cap[-1]:.4f}  (dimensionless)")
print(f"  H_mean    (PP cap)   : {H_mean_cap[-1]:.4f}  (dimensionless)")
print(f"  H_VV1_alpha (split)  : {H_VV1_alpha[-1]:.4f}  (dimensionless)")
print(f"  Pressure  (PP cap)   : {u_cap_mmHg[-1]:.2f} mmHg")
print(f"  Flow      (PP cap)   : {v_cap_mm3s[-1]:.4f} mm3/s")
print(f"  Viscosity (PP cap)   : {mu_cap[-1]:.4e} Js/m3")
print(f"  Resistance(PP cap)   : {R_cap[-1]:.4e} Js/m6")
print()

# =============================================================================
# 5. FIGURE -- 6 PANELS
# =============================================================================

COLORS = {
    "blue":   "#2563eb",
    "orange": "#ea580c",
    "green":  "#16a34a",
    "purple": "#7c3aed",
    "red":    "#dc2626",
    "gray":   "#374151",
}

def style_ax(ax, title, xlabel, ylabel):
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6, color="#111827")
    ax.set_xlabel(xlabel, fontsize=8, color="#374151")
    ax.set_ylabel(ylabel, fontsize=8, color="#374151")
    ax.tick_params(labelsize=7)
    ax.grid(True, alpha=0.25, linestyle="--")
    ax.set_facecolor("#ffffff")
    for spine in ax.spines.values():
        spine.set_edgecolor("#d1d5db")

fig = plt.figure(figsize=(16, 12))
fig.patch.set_facecolor("#f8fafc")
fig.suptitle(
    "Microvascular H-D Network -- Physical Time Dynamics\n"
    f"vode/bdf  |  {sizeStates} states  |  {sizeAlgebraic} algebraic vars"
    f"  |  wall time {elapsed:.2f} s",
    fontsize=12, fontweight="bold", y=0.99, color="#111827"
)

gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.50, wspace=0.35)

# Panel A -- Hematocrit in PP capillary
ax = fig.add_subplot(gs[0, 0])
ax.plot(voi, H_link_R_cap, label="H_link_R", lw=1.8, color=COLORS["blue"])
ax.plot(voi, H_link_L_cap, label="H_link_L", lw=1.8, color=COLORS["orange"], ls="--")
ax.plot(voi, H_down_cap,   label="H_down",   lw=1.8, color=COLORS["green"],  ls=":")
ax.plot(voi, H_mean_cap,   label="H_mean",   lw=2.0, color=COLORS["gray"],   ls="-.")
ax.set_ylim([-0.05, 1.05])
ax.legend(fontsize=7, loc="best", framealpha=0.8)
ax.text(0.98, 0.05, "H advects with transit time t = L/v",
        transform=ax.transAxes, fontsize=6.5, color="#6b7280",
        ha="right", style="italic")
style_ax(ax, "A  |  Hematocrit -- PP Capillary", "Time (s)", "Hematocrit (--)")

# Panel B -- Hematocrit at VV Junction 1 (Zweifach-Fung)
ax = fig.add_subplot(gs[0, 1])
ax.plot(voi, H_from1,    label="H_from1",        lw=1.6, color=COLORS["blue"])
ax.plot(voi, H_from2,    label="H_from2",        lw=1.6, color=COLORS["orange"], ls="--")
ax.plot(voi, H_from3,    label="H_from3",        lw=1.6, color=COLORS["green"],  ls=":")
ax.plot(voi, H_from4,    label="H_from4",        lw=1.6, color=COLORS["purple"], ls="-.")
ax.plot(voi, H_VV1_alpha,label="H_out_alpha (split)", lw=2.2, color=COLORS["red"])
ax.set_ylim([-0.05, 1.05])
ax.legend(fontsize=7, loc="best", framealpha=0.8)
ax.text(0.98, 0.05, "red = output after Zweifach-Fung bifurcation split",
        transform=ax.transAxes, fontsize=6.5, color="#6b7280",
        ha="right", style="italic")
style_ax(ax, "B  |  Hematocrit -- VV Junction 1 (Zweifach-Fung)",
         "Time (s)", "Hematocrit (--)")

# Panel C -- Pressure
ax = fig.add_subplot(gs[1, 0])
ax.plot(voi, u_cap_mmHg, label="PP capillary",  lw=1.8, color=COLORS["blue"])
ax.plot(voi, u_VV1_mmHg, label="VV junction 1", lw=1.8, color=COLORS["orange"], ls="--")
ax.legend(fontsize=8)
style_ax(ax, "C  |  Pressure", "Time (s)", "Pressure (mmHg)")

# Panel D -- Flow
ax = fig.add_subplot(gs[1, 1])
ax.plot(voi, v_cap_mm3s, label="PP capillary",  lw=1.8, color=COLORS["blue"])
ax.plot(voi, v_VV1_mm3s, label="VV junction 1", lw=1.8, color=COLORS["orange"], ls="--")
ax.legend(fontsize=8)
style_ax(ax, "D  |  Volumetric Flow", "Time (s)", "Flow (mm3/s)")

# Panel E -- Viscosity
ax = fig.add_subplot(gs[2, 0])
ax.plot(voi, mu_cap, lw=1.8, color=COLORS["purple"])
ax.text(0.98, 0.05, "mu = f(H, d) via Fahraeus-Lindqvist",
        transform=ax.transAxes, fontsize=6.5, color="#6b7280",
        ha="right", style="italic")
style_ax(ax, "E  |  Viscosity -- PP Capillary\n(H drives mu -- F-L law)",
         "Time (s)", "Viscosity (Js/m3)")

# Panel F -- Resistance
ax = fig.add_subplot(gs[2, 1])
ax.plot(voi, R_cap, lw=1.8, color=COLORS["red"])
ax.text(0.98, 0.05, "R = 128*mu*L / (pi*d^4)",
        transform=ax.transAxes, fontsize=6.5, color="#6b7280",
        ha="right", style="italic")
style_ax(ax, "F  |  Resistance -- PP Capillary\n(mu drives R -- Poiseuille)",
         "Time (s)", "Resistance (Js/m6)")

plt.savefig(
    "/home/sliu205/0D_hemodynamics_paper/Preliminary_results/generated_models/H_D_network/run_time_dynamics_results/HD_network_results.png",
    dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor()
)
print("  Figure saved -> HD_network_results.png")

# =============================================================================
# 6. SAVE CSV
# =============================================================================

header = (
    "time_s,"
    "H_link_R_cap,H_link_L_cap,H_down_cap,H_mean_cap,"
    "H_from1_junc1,H_from2_junc1,H_from3_junc1,H_from4_junc1,"
    "H_VV1_alpha,"
    "pressure_cap_mmHg,pressure_VV1_mmHg,"
    "flow_cap_mm3s,flow_VV1_mm3s,"
    "viscosity_cap_Jsm3,resistance_cap_Jsm6"
)

np.savetxt(
    "/home/sliu205/0D_hemodynamics_paper/Preliminary_results/generated_models/H_D_network/run_time_dynamics_results/HD_network_results.csv",
    np.column_stack([
        voi,
        H_link_R_cap, H_link_L_cap, H_down_cap, H_mean_cap,
        H_from1, H_from2, H_from3, H_from4,
        H_VV1_alpha,
        u_cap_mmHg, u_VV1_mmHg,
        v_cap_mm3s, v_VV1_mm3s,
        mu_cap, R_cap
    ]),
    delimiter=",", header=header, comments=""
)
print("  Data   saved -> HD_network_results.csv")
print()
print("=" * 62)
print("  Complete.")
print("=" * 62)