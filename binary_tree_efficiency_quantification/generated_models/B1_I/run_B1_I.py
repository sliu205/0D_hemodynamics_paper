import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root
import sys
import os
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. FIXED NumPy vstack compatibility shim
# ---------------------------------------------------------------------------
_np_vstack_orig = np.vstack
def _vstack_compat(tup, *args):
    if args:
        tup = (tup,) + args

    # Handle the OpenCOR/NumPy dimension mismatch during computeAlgebraic
    # If one item is a full array (time series) and another is a single float/scalar (constant),
    # we broadcast the scalar to match the array length.
    processed_tup = []
    max_len = 1
    for item in tup:
        arr = np.atleast_1d(item)
        if arr.shape[0] > max_len:
            max_len = arr.shape[0]

    for item in tup:
        arr = np.atleast_1d(item)
        if arr.shape[0] == 1 and max_len > 1:
            # Broadcast the scalar constant to the length of the simulation
            processed_tup.append(np.full(max_len, arr[0]))
        else:
            processed_tup.append(arr)

    return _np_vstack_orig(tuple(processed_tup))

np.vstack = _vstack_compat

# ---------------------------------------------------------------------------
# 2. SETTINGS
# ---------------------------------------------------------------------------
SIM_LENGTH      = 1000.0
POINT_INTERVAL  = 0.1
DT_MAX          = 0.1      # Forgiving step size
RTOL            = 1e-5
ATOL            = 1e-5

# ---------------------------------------------------------------------------
# 3. MATH MONKEY PATCHES (Runner level) makes sure powers are greater than 0 to prevent NaNs
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import B1_I

# Patch power to prevent NaNs from negative bases
def safe_power(base, exponent):
    return np.power(np.maximum(base, 0.0), exponent)

B1_I.power = safe_power

from B1_I import (initConsts, computeRates, computeAlgebraic)

# ---------------------------------------------------------------------------
# 4. GOLD STANDARD ITERATIVE SOLVER for H_VV_out at the VV junction
# ---------------------------------------------------------------------------
# The VV junction has nonlinear coupling:
#   H → viscosity → resistance → flow → FQB_alpha (blood flow fraction)
#     → FQE_alpha (RBC flow fraction, Pries sigmoidal model)
#     → H_VV_out_alpha, H_VV_out_beta
#
# We solve for both H_VV_out_alpha (alg[118]) and H_VV_out_beta (alg[119])
# simultaneously, enforcing two constraints:
#
#   [1] Phase separation (Pries):  FQB_alpha * H_out_alpha = H_mean * FQE_alpha
#   [2] RBC mass conservation:     FQB_alpha * H_out_alpha
#                                + (1 - FQB_alpha) * H_out_beta = H_mean
#
# scipy.optimize.root is used to solve this 2x2 nonlinear system at every
# ODE function evaluation (i.e., every internal Radau step).
# ---------------------------------------------------------------------------

# Warm-start initial guess, updated each call to accelerate convergence
_h_out_guess = np.array([0.45, 0.45])

def _solve_H_VV_out(H_mean, FQB_alpha, FQE_alpha, eps):
    """
    Gold standard: solve for H_VV_out_alpha and H_VV_out_beta using
    scipy.optimize.root (hybr method = modified Powell hybrid, equivalent
    to MINPACK's HYBRD).

    Residuals:
      r1 = FQB_alpha * H_out_alpha - H_mean * FQE_alpha          [phase separation]
      r2 = FQB_alpha * H_out_alpha + (1-FQB_alpha)*H_out_beta - H_mean  [mass conservation]
    """
    global _h_out_guess

    def residuals(x):
        H_a, H_b = x
        r1 = (FQB_alpha + eps) * H_a - H_mean * FQE_alpha
        r2 = FQB_alpha * H_a + (1.0 - FQB_alpha) * H_b - H_mean
        return [r1, r2]

    sol = root(residuals, _h_out_guess, method='hybr', tol=1e-8)
    if sol.success:
        _h_out_guess = sol.x  # warm-start next call
        return float(sol.x[0]), float(sol.x[1])
    else:
        # Fallback to direct formula if root-finder fails
        H_a = H_mean * FQE_alpha / (FQB_alpha + eps)
        H_b = H_mean * (1.0 - FQE_alpha) / ((1.0 - FQB_alpha) + eps)
        return H_a, H_b


def _rootfind_handler(voi, constants, rates, states, algebraic):
    """
    Called by computeRates at each ODE step.
    Solves for alg[118] = H_VV_out_alpha using the gold standard iterative solver.
    alg[119] = H_VV_out_beta is set here too; computeRates will re-compute it
    with its own explicit formula right after, which is consistent.
    """
    H_mean   = float(np.asarray(algebraic[15]).item())
    FQB      = float(np.asarray(algebraic[110]).item())
    FQE      = float(np.asarray(algebraic[117]).item())
    eps      = float(constants[15])

    H_a, _H_b = _solve_H_VV_out(H_mean, FQB, FQE, eps)
    algebraic[118] = H_a


def _fill_H_VV_out_timeseries(algebraic, constants):
    """
    computeAlgebraic does not call rootfind_0, so alg[118] stays 0 for the
    entire time series.  This function fills it in using the gold standard
    iterative solver, point by point.

    alg[119] is already computed explicitly inside computeAlgebraic, so we
    only need to handle alg[118] here.
    """
    eps = float(constants[15])
    n_t = algebraic.shape[1]
    for i in range(n_t):
        H_mean = float(algebraic[15, i])
        FQB    = float(algebraic[110, i])
        FQE    = float(algebraic[117, i])
        H_a, _ = _solve_H_VV_out(H_mean, FQB, FQE, eps)
        algebraic[118, i] = H_a


# ---------------------------------------------------------------------------
# 5. ODE RIGHT-HAND SIDE
# ---------------------------------------------------------------------------

def make_rhs(constants):
    def rhs(t, y):
        raw = computeRates(t, y, constants)
        return np.array([np.asarray(r).item() for r in raw], dtype=float)
    return rhs


# ---------------------------------------------------------------------------
# 6. RUN
# ---------------------------------------------------------------------------

def run(label):
    B1_I.rootfind_0 = _rootfind_handler
    init_states, constants = initConsts()
    t_eval = np.linspace(0.0, SIM_LENGTH, int(SIM_LENGTH / POINT_INTERVAL) + 1)

    print(f"\n{'='*60}")
    print(f"Run: {label}  (Radau + scipy.optimize.root junction solver)")
    print('='*60)

    t_start = time.perf_counter()

    sol = solve_ivp(
        fun=make_rhs(constants),
        t_span=(0.0, SIM_LENGTH),
        y0=init_states,
        method='Radau',
        t_eval=t_eval,
        max_step=DT_MAX,
        rtol=RTOL,
        atol=ATOL
    )

    elapsed = time.perf_counter() - t_start
    print(f"Solver status : {sol.message}")
    print(f"Wall time     : {elapsed:.4f} s")

    if not sol.success:
        return None, None, None

    algebraic = computeAlgebraic(constants, sol.y, sol.t)

    # computeAlgebraic never calls rootfind_0, so alg[118] is all zeros.
    # Fill in H_VV_out_alpha using the gold standard solver.
    _fill_H_VV_out_timeseries(algebraic, constants)

    return sol.t, sol.y, algebraic


# ---------------------------------------------------------------------------
# 7. MAIN: plot H_VV_out_alpha and H_VV_out_beta
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    t_voi, states, alg = run("Gold Standard")
    if t_voi is not None:
        # Save H_VV_out_alpha and H_VV_out_beta to CSV
        out_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(out_dir, "H_VV_out.csv")
        csv_data = np.column_stack([t_voi, alg[118, :], alg[119, :]])
        np.savetxt(
            csv_path,
            csv_data,
            delimiter=",",
            header="time_s,H_VV_out_alpha,H_VV_out_beta",
            comments="",
        )
        print(f"Saved: {csv_path}")

        fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

        axes[0].plot(t_voi, alg[118, :], color='tab:blue')
        axes[0].set_ylabel("H_VV_out_alpha (dimensionless)")
        axes[0].set_title("VV Junction Hematocrit Output — Gold Standard Iterative Solver")
        axes[0].grid(True)

        axes[1].plot(t_voi, alg[119, :], color='tab:orange')
        axes[1].set_ylabel("H_VV_out_beta (dimensionless)")
        axes[1].set_xlabel("Time (s)")
        axes[1].grid(True)

        plt.tight_layout()
        plt.show()
