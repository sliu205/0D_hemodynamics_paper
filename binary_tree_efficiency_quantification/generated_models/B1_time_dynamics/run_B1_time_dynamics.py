"""
Runner script for B1_time_dynamics model.

SOLVER NOTES
------------
This model (no circular dependency):
    Uses scipy solve_ivp with method='Radau' — a fully implicit Runge-Kutta
    solver well-suited for stiff ODE systems like this one. No iterative
    solving is required between states.

Your circular-dependency model:
    Also use solve_ivp with method='Radau'. The iterative resolution of the
    algebraic loop (e.g. via scipy.optimize.fsolve or root) should be embedded
    inside computeRates, called at each timestep. Using the same outer solver
    (Radau) for both models keeps the comparison fair — any runtime difference
    you observe will reflect the cost of the iterative solve, not differences
    in the integration scheme.
"""

import time
import numpy as np
from scipy.integrate import solve_ivp
import sys
import os

# ---------------------------------------------------------------------------
# NumPy compatibility shim for OpenCOR-generated models.
# Older generated code calls vstack(a, b) with two positional args; modern
# NumPy only accepts vstack((a, b)).  Patch it before importing any model so
# that 'from numpy import *' inside the model picks up the fixed version.
# ---------------------------------------------------------------------------
_np_vstack_orig = np.vstack
def _vstack_compat(tup, *args):
    if args:
        tup = (tup,) + args
    return _np_vstack_orig(tup)
np.vstack = _vstack_compat

# ---------------------------------------------------------------------------
# SETTINGS — edit these
# ---------------------------------------------------------------------------
SIM_LENGTH      = 1000.0   # Total simulation time (seconds)
POINT_INTERVAL  = 1.0      # Time between saved/plotted output points (seconds)
DT_MAX          = 1.0      # Maximum step size the solver is allowed to take (seconds)
RTOL            = 1e-7     # Relative tolerance
ATOL            = 1e-7     # Absolute tolerance
# ---------------------------------------------------------------------------

# Import model functions from the original file (assumed to be in the same
# directory, or on the Python path)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from B1_time_dynamics import initConsts, computeRates, computeAlgebraic, sizeStates

def run():
    # Initialise constants and initial states
    init_states, constants = initConsts()

    # Time vector for output evaluation
    n_out_steps = int(round(SIM_LENGTH / POINT_INTERVAL)) + 1
    t_eval = np.linspace(0.0, SIM_LENGTH, n_out_steps)
    t_span = (t_eval[0], t_eval[-1])

    # Wrap computeRates so it matches solve_ivp's expected signature (t, y)
    def rhs(t, y):
        return computeRates(t, y, constants)

    print(f"Running simulation: t=0 → {SIM_LENGTH}s, "
          f"max_step={DT_MAX}s, point_interval={POINT_INTERVAL}s ({n_out_steps} output points)")
    print(f"Solver: Radau  |  rtol={RTOL}  atol={ATOL}")
    print("-" * 60)

    t_start = time.perf_counter()

    sol = solve_ivp(
        fun=rhs,
        t_span=t_span,
        y0=init_states,
        method="Radau",       # Implicit Runge-Kutta; stiff-safe, no iteration needed
        t_eval=t_eval,
        max_step=DT_MAX,
        rtol=RTOL,
        atol=ATOL,
        dense_output=False,
    )

    t_end = time.perf_counter()
    elapsed = t_end - t_start

    # -----------------------------------------------------------------------
    # Report
    # -----------------------------------------------------------------------
    print(f"Solver status : {sol.status}  ({sol.message})")
    print(f"Steps taken   : {sol.t.shape[0]} output points recorded")
    print(f"RHS evaluations: {sol.nfev}")
    print(f"Simulation wall-clock time: {elapsed:.4f} s")

    if not sol.success:
        print("WARNING: solver did not converge successfully.")
        return None, None, None

    # Recover algebraic variables at each recorded time point
    states = sol.y                          # shape: (sizeStates, N_OUT_STEPS)
    voi    = sol.t                          # shape: (N_OUT_STEPS,)
    algebraic = computeAlgebraic(constants, states, voi)

    return voi, states, algebraic


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    voi, states, algebraic = run()

    if voi is not None:
        H_mean = algebraic[4, :]
        v_mm3s = algebraic[10, :] * 1e9  # m3/s → mm3/s

        print(f"{'time (s)':>12}  {'H_mean':>12}  {'v (mm3/s)':>12}")
        print("-" * 42)
        for t, h, v in zip(voi, H_mean, v_mm3s):
            print(f"{t:12.4f}  {h:12.6f}  {v:12.6e}")

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

        ax1.plot(voi, H_mean)
        ax1.set_ylabel("H_mean (dimensionless)")
        ax1.set_title("Inlet vessel — H_mean")
        ax1.ticklabel_format(useOffset=False)

        ax2.plot(voi, v_mm3s)
        ax2.set_ylabel("v (mm³/s)")
        ax2.set_xlabel("time (s)")
        ax2.set_title("Inlet vessel — flow v")

        plt.tight_layout()
        plt.show()