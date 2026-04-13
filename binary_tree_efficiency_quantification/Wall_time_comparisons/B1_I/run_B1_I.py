#!/usr/bin/env python3
import sys
import traceback

# Force all output to appear immediately — needed inside OpenCOR's Python
def p(msg=""):
    print(msg, flush=True)

p("=== run_B1_I.py starting ===")

try:
    import time
    from pathlib import Path
    from datetime import datetime
    p("  stdlib OK")

    import numpy as np
    p(f"  numpy {np.__version__} OK")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    p("  matplotlib OK")

    from scipy.integrate import solve_ivp
    from scipy.optimize import root
    p("  scipy OK")

    THIS_DIR = Path(__file__).resolve().parent
    sys.path.insert(0, str(THIS_DIR))
    p(f"  THIS_DIR = {THIS_DIR}")

    p("  importing hybrid_simulation_helper...")
    from hybrid_simulation_helper import HybridSimulationHelper
    p("  HybridSimulationHelper OK")

    # ── Settings ──────────────────────────────────────────────────────────────
    MODEL_PY   = str(THIS_DIR / "B1_I.py")
    OUTPUT_DIR = THIS_DIR / "B1_I_results"
    SIM_LENGTH = 10.0
    DT         = 1.0

    SOLVER_INFO = {
        "MaximumStep":       1.0,
        "AbsoluteTolerance": 1e-6,
        "RelativeTolerance": 1e-6,
        "RootMethod":        "lm",
        "RootTolerance":     1e-6,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    p(f"  Loading model: {MODEL_PY}")
    sim = HybridSimulationHelper(
        model_py_path=MODEL_PY,
        dt=DT,
        sim_time=SIM_LENGTH,
        solver_info=SOLVER_INFO,
        pre_time=0.0,
    )
    p("  Model loaded OK")

    sim.reset_and_clear()
    sim.update_times(dt=DT, start_time=0.0, sim_time=SIM_LENGTH, pre_time=0.0)

    p("  Running simulation...")
    ok   = sim.run()
    wall = sim.last_wall_time

    p()
    p("─" * 45)
    p(f"  Wall time : {wall:.3f} s  ({wall/60:.2f} min)")
    p(f"  Status    : {'OK' if ok else 'FAILED'}")
    p("─" * 45)
    p()

    if not ok:
        p("ERROR: Simulation failed — see warnings above.")
        sys.exit(1)

    # ── Extract results ───────────────────────────────────────────────────────
    res     = sim.get_results(["time",
                                "VV_junc1/H_VV_out_alpha",
                                "VV_junc1/H_VV_out_beta"])
    t       = res[0][0]
    H_alpha = res[1][0]
    H_beta  = res[2][0]

    p(f"  H_VV_out_alpha  final = {H_alpha[-1]:.6f}")
    p(f"  H_VV_out_beta   final = {H_beta[-1]:.6f}")

    # ── Plot ──────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, H_alpha, label=r"$H^\alpha_\mathrm{VV,out}$",
            linewidth=2, dashes=(10, 6))
    ax.plot(t, H_beta,  label=r"$H^\beta_\mathrm{VV,out}$",
            linewidth=2, dashes=(5, 6))
    ax.set_xlabel("Time (s)", fontsize=14)
    ax.set_ylabel("Haematocrit (−)", fontsize=14)
    ax.set_title("B1_I — VV junction outflow haematocrit\n"
                 "(scipy BDF + scipy.optimize.root)", fontsize=13)
    ax.legend(frameon=False, fontsize=13)
    ax.grid(True, linestyle="--", alpha=0.25)
    fig.tight_layout()

    plot_path = OUTPUT_DIR / f"H_VV_out_{ts}.png"
    fig.savefig(plot_path, dpi=300)
    plt.close(fig)
    p(f"  Plot → {plot_path}")

    # ── CSV ───────────────────────────────────────────────────────────────────
    csv_path = OUTPUT_DIR / f"H_VV_out_{ts}.csv"
    np.savetxt(csv_path,
               np.column_stack([t, H_alpha, H_beta]),
               delimiter=",",
               header="time_s,H_VV_out_alpha,H_VV_out_beta",
               comments="")
    p(f"  CSV  → {csv_path}")
    p()
    p("=== Done. ===")

except Exception:
    p()
    p("=== EXCEPTION ===")
    traceback.print_exc(file=sys.stdout)
    sys.stdout.flush()
    sys.exit(1)
