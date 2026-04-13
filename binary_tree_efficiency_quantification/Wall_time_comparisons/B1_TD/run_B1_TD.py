#!/usr/bin/env python3
"""
Run B1_I.cellml with OpenCOR and plot H_VV_out_alpha / H_VV_out_beta
from the VV junction component.

Outputs (written to OUTPUT_DIR):
  H_VV_out_<timestamp>.png   — single figure, both curves
  H_VV_out_<timestamp>.csv   — time + both curves

Wall time (time for sim.run() only, not full script) is printed to stdout.

Usage:
  python3 run_B1_I.py
  python3 run_B1_I.py --cellml /path/to/B1_I.cellml
"""

import sys
import argparse
import time
from pathlib import Path
from datetime import datetime

import numpy as np
import matplotlib
matplotlib.use("Agg")          # no display needed; remove for interactive use
import matplotlib.pyplot as plt

# ── opencor_helper must be on the path ────────────────────────────────────────
THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
from opencor_helper import SimulationHelper


# ══════════════════════════════════════════════════════════════════════════════
# SETTINGS  ← edit these to change the run without touching anything else
# ══════════════════════════════════════════════════════════════════════════════
SETTINGS = {
    # Path to the CellML file (can also be overridden via --cellml argument)
    "CELLML_FILE": str(THIS_DIR / "B1_TD.cellml"),

    # Where to write outputs
    "OUTPUT_DIR": str(THIS_DIR / "B1_TD_results"),

    # ── Solver ───────────────────────────────────────────────────────────────
    # CVODE time step for data storage (seconds)
    "DT": 1.0,
    # CVODE internal maximum step (seconds); smaller = more accurate but slower
    "MAX_STEP": 1.0,
    # Maximum number of internal CVODE steps between outputs
    "MAX_NSTEPS": 50000,
    # Total simulation length (seconds)
    "SIM_LENGTH": 1000.0,

    # ── Plot appearance ───────────────────────────────────────────────────────
    "FONT_SIZE":        20,
    "AXIS_LABEL_SIZE":  20,
    "LEGEND_SIZE":      16,
    "LINEWIDTH":        2.5,
    "HALO_LINEWIDTH":   5.0,    # white halo behind each curve for readability
    "GRID_ALPHA":       0.25,
    "FIG_SIZE":         (11, 6),
    "DPI":              300,
}

# ══════════════════════════════════════════════════════════════════════════════
# VARIABLES TO FETCH
# Format: "component_name/variable_name"  (from the CellML access components)
# H_VV_out_alpha and H_VV_out_beta are declared in the "VV_junc1" component.
# ══════════════════════════════════════════════════════════════════════════════
VARS = [
    "time",
    "VV_junc1/H_VV_out_alpha",
    "VV_junc1/H_VV_out_beta",
]

# Display labels for the two curves (order matches VARS[1:])
LABELS = [
    r"$H_\mathrm{VV,out}^{\alpha}$  (alpha branch)",
    r"$H_\mathrm{VV,out}^{\beta}$   (beta branch)",
]

# Dash patterns: large spacing so overlapping curves stay distinguishable
DASH_PATTERNS = [
    (12, 8),        # alpha
    (6,  8),        # beta
]


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def write_csv(path: Path, t: np.ndarray, series: list[np.ndarray]) -> None:
    """Write time + all series to a CSV file."""
    header = "time_s,H_VV_out_alpha,H_VV_out_beta"
    data   = np.column_stack([t] + series)
    with open(path, "w") as fh:
        fh.write(header + "\n")
        np.savetxt(fh, data, delimiter=",", fmt="%.10g")
    print(f"  CSV  → {path}")


def plot_H_VV(t: np.ndarray,
              series: list[np.ndarray],
              out_path: Path) -> None:
    """
    Plot H_VV_out_alpha and H_VV_out_beta on one figure.
    Each curve gets a white halo first (zorder=1) then the coloured line
    (zorder=2) so overlapping regions remain readable.
    """
    fig, ax = plt.subplots(figsize=SETTINGS["FIG_SIZE"])

    for y, label, dashes in zip(series, LABELS, DASH_PATTERNS):
        # white halo
        ax.plot(t, y,
                color="white",
                linewidth=SETTINGS["HALO_LINEWIDTH"],
                dashes=dashes,
                zorder=1)
        # coloured curve
        ax.plot(t, y,
                label=label,
                linewidth=SETTINGS["LINEWIDTH"],
                dashes=dashes,
                zorder=2)

    ax.set_xlabel("Time  (s)",        fontsize=SETTINGS["AXIS_LABEL_SIZE"])
    ax.set_ylabel("Haematocrit  (−)", fontsize=SETTINGS["AXIS_LABEL_SIZE"])
    ax.set_title("VV Junction outflow haematocrit — B1_I model",
                 fontsize=SETTINGS["FONT_SIZE"])

    ax.grid(True, linestyle="--",
            alpha=SETTINGS["GRID_ALPHA"], linewidth=0.8)
    ax.legend(loc="best", frameon=False,
              fontsize=SETTINGS["LEGEND_SIZE"])

    fig.tight_layout()
    fig.savefig(out_path, dpi=SETTINGS["DPI"])
    plt.close(fig)
    print(f"  Plot → {out_path}")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main(cellml_path: str) -> None:
    plt.rcParams.update({
        "font.size":       SETTINGS["FONT_SIZE"],
        "legend.fontsize": SETTINGS["LEGEND_SIZE"],
    })

    cellml = Path(cellml_path).resolve()
    if not cellml.exists():
        sys.exit(f"ERROR: CellML file not found: {cellml}")

    out_dir = Path(SETTINGS["OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    # ── Build simulation object ───────────────────────────────────────────────
    print(f"Opening simulation: {cellml.name}")
    sim = SimulationHelper(
        str(cellml),
        dt=SETTINGS["DT"],
        sim_time=SETTINGS["SIM_LENGTH"],
        solver_info={
            "MaximumStep":          SETTINGS["MAX_STEP"],
            "MaximumNumberOfSteps": SETTINGS["MAX_NSTEPS"],
        },
        pre_time=0.0,
    )

    sim.reset_and_clear()
    sim.update_times(
        dt=SETTINGS["DT"],
        start_time=0.0,
        sim_time=SETTINGS["SIM_LENGTH"],
        pre_time=0.0,
    )

    # ── Run — measure wall time of sim.run() only ─────────────────────────────
    print("Running simulation …")
    t_wall_start = time.perf_counter()
    success = sim.run()
    t_wall_end   = time.perf_counter()

    wall_time_s = t_wall_end - t_wall_start

    if not success:
        sim.close_simulation()
        sys.exit("ERROR: OpenCOR simulation failed to converge.")

    # Print wall time immediately after the run finishes
    print(f"\n{'─'*45}")
    print(f"  Simulation wall time : {wall_time_s:.3f} s  "
          f"({wall_time_s/60:.2f} min)")
    print(f"{'─'*45}\n")

    # ── Extract results ───────────────────────────────────────────────────────
    res    = sim.get_results(VARS)
    t      = res[0][0]                        # time array
    series = [r[0] for r in res[1:]]         # [H_VV_out_alpha, H_VV_out_beta]

    # ── Save outputs ──────────────────────────────────────────────────────────
    plot_H_VV(t, series, out_dir / f"H_VV_out_{ts}.png")
    write_csv(out_dir / f"H_VV_out_{ts}.csv", t, series)

    # ── Quick sanity summary ──────────────────────────────────────────────────
    for name, y, label in zip(VARS[1:], series, LABELS):
        print(f"  {name}")
        print(f"    initial : {y[0]:.6f}")
        print(f"    final   : {y[-1]:.6f}")
        print(f"    min/max : {y.min():.6f} / {y.max():.6f}")

    sim.close_simulation()
    print("\nDone.")


# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run B1_I.cellml and plot H_VV_out_alpha / H_VV_out_beta")
    parser.add_argument(
        "--cellml",
        default=SETTINGS["CELLML_FILE"],
        help="Path to B1_I.cellml  (default: %(default)s)",
    )
    args = parser.parse_args()
    main(args.cellml)
