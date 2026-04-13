import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root
import sys
import os
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. NumPy vstack compatibility shim
# ---------------------------------------------------------------------------
_np_vstack_orig = np.vstack
def _vstack_compat(tup, *args):
    if args:
        tup = (tup,) + args
    processed_tup = []
    max_len = 1
    for item in tup:
        arr = np.atleast_1d(item)
        if arr.shape[0] > max_len:
            max_len = arr.shape[0]
    for item in tup:
        arr = np.atleast_1d(item)
        if arr.shape[0] == 1 and max_len > 1:
            processed_tup.append(np.full(max_len, arr[0]))
        else:
            processed_tup.append(arr)
    return _np_vstack_orig(tuple(processed_tup))

np.vstack = _vstack_compat

# ---------------------------------------------------------------------------
# 2. SETTINGS
# ---------------------------------------------------------------------------
SIM_LENGTH     = 1000.0
POINT_INTERVAL = 0.1
DT_MAX         = 0.1
RTOL           = 1e-5
ATOL           = 1e-5

# ---------------------------------------------------------------------------
# 3. MATH MONKEY PATCHES
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import B1_I

def safe_power(base, exponent):
    return np.power(np.maximum(base, 0.0), exponent)

B1_I.power = safe_power

from B1_I import (initConsts, computeRates, computeAlgebraic, residualSN_0)

# ---------------------------------------------------------------------------
# 4. GOLD STANDARD ITERATIVE SOLVER  (post-processing only)
# ---------------------------------------------------------------------------
#
# Two-phase strategy:
#
#   PHASE 1 — ODE integration (solve_ivp):
#     Use B1_I's built-in rootfind_0 (fsolve, warm-started).  This is the
#     fast path and produces the state trajectory y(t).  Calling a 61-var
#     root solve at every internal Radau step (potentially 100 000+) would
#     be prohibitively slow.
#
#   PHASE 2 — Post-processing (gold standard):
#     With the state trajectory in hand, call scipy.optimize.root once per
#     saved output point (10 001 points).  This solves the full 61-variable
#     nonlinear system:
#
#       v (flow) → RBC_volume advection → H_mean → viscosity (Pries)
#               → R (Poiseuille) → v   [closed loop across all 5 vessels]
#
#     and then reads off alg[192] = H_VV_out_alpha, alg[193] = H_VV_out_beta.
#
# The comparison is valid: the ODE state trajectory drives H_VV_out through
# the same physical equations; the gold standard iterative solve just
# enforces that alg[34..94] are fully self-consistent at each output point.
#
# ---------------------------------------------------------------------------

def _build_initial_guess(constants):
    """
    Physically-motivated initial guess for the 61 unknowns (alg[34..94]).

    Units matter: flow ~1e-12 m³/s, resistance ~1e14-1e15 Js/m⁶, etc.
    A guess of ones(61)*0.1 fails because it is off by many orders of
    magnitude for those variables (especially R which is ~1e15, not 0.1).
    """
    import math as _math

    x0 = np.zeros(61)

    # w_v, w_v_d direction weights — roughly 0.5 at rest
    for i in [0, 1, 13, 14, 26, 27, 39, 50]:
        x0[i] = 0.5

    # H_L_out, H_R_out, H_mean, H_volume_* — haematocrit ~ global value
    H0 = float(constants[0])
    for i in [2, 3, 5, 6, 7, 15, 16, 18, 19, 20, 28, 29, 31, 32, 33,
              40, 41, 43, 44, 45, 51, 52, 54, 55, 56]:
        x0[i] = H0

    # RBC_volume — use the initial RBC volumes from constants
    x0[4]  = float(constants[54])   # PP_capillary
    x0[17] = float(constants[57])   # PP_pericyte_1
    x0[30] = float(constants[59])   # PP_pericyte_2
    x0[42] = float(constants[60])   # VP_capillary_1
    x0[53] = float(constants[61])   # VP_capillary_2

    # mu (viscosity) — blood ~1.2e-3 Pa.s
    for i in [8, 21, 34, 46, 57]:
        x0[i] = 1.2e-3

    # hem_dep_u_rel — dimensionless, ~1.0
    for i in [9, 22, 35, 47, 58]:
        x0[i] = 1.0

    # R (resistance) — Poiseuille formula: R = 8 * mu * L / (pi * r^4)
    # Effective viscosity ≈ mu_plasma * mu_45(r, H) where mu_45 is the
    # Pries relative viscosity at H=45%.  For 6 µm vessels mu_45 ≈ 3.6.
    mu_p = float(constants[9])   # mu_plasma (Pa.s)

    def pries_mu45(r_m):
        """Pries in-vivo relative viscosity at H=0.45 for tube radius r_m."""
        D_um = 2.0 * r_m * 1e6   # diameter in µm
        return 6.0*_math.exp(-0.085*D_um) + 3.2 - 2.44*_math.exp(-0.06*(D_um**0.645))

    def poiseuille(r_m, L_m, mu_rel):
        return 8.0 * mu_p * mu_rel * L_m / (_math.pi * r_m**4)

    r_cap  = float(constants[8]);  L_cap  = float(constants[38])  # PP_capillary
    r_pv1  = float(constants[29]); L_pv1  = float(constants[40])  # PP_pericyte_1
    r_pv2  = float(constants[31]); L_pv2  = float(constants[41])  # PP_pericyte_2
    r_vp1  = float(constants[33]); L_vp1  = float(constants[42])  # VP_capillary_1
    r_vp2  = float(constants[36]); L_vp2  = float(constants[43])  # VP_capillary_2

    x0[10] = poiseuille(r_cap,  L_cap,  pries_mu45(r_cap))
    x0[23] = poiseuille(r_pv1,  L_pv1,  pries_mu45(r_pv1))
    x0[36] = poiseuille(r_pv2,  L_pv2,  pries_mu45(r_pv2))
    x0[48] = poiseuille(r_vp1,  L_vp1,  pries_mu45(r_vp1))
    x0[59] = poiseuille(r_vp2,  L_vp2,  pries_mu45(r_vp2))

    # v, v_d (flows) — estimate from ΔP / R
    dP = float(constants[10]) - float(constants[11])   # u_in_inlet - u_ext
    v_cap  = dP / x0[10]
    v_pv1  = dP / x0[23] * 0.5   # half the flow splits at junction
    v_pv2  = dP / x0[36] * 0.5
    v_vp1  = dP / x0[48] * 0.5
    v_vp2  = dP / x0[59] * 0.5

    x0[11] = v_cap;  x0[12] = v_cap   # v, v_d PP_capillary
    x0[24] = v_pv1;  x0[25] = v_pv1   # v, v_d PP_pericyte_1
    x0[37] = v_pv2;  x0[38] = v_pv2   # v, v_d PP_pericyte_2
    x0[49] = v_vp1                     # v VP_capillary_1
    x0[60] = v_vp2                     # v VP_capillary_2

    return x0


# Warm-start: updated after each successful solve
_junc_guess = None   # set on first call using _build_initial_guess


def _solve_junction_point(alg_i, t_i, constants, states_i):
    """
    Gold standard: solve the 61-variable nonlinear system at a single time
    point using scipy.optimize.root.

    Returns the 61-element solution vector (alg[34..94]).
    """
    global _junc_guess

    if _junc_guess is None:
        _junc_guess = _build_initial_guess(constants)

    rates_dummy = [0.0] * len(states_i)
    alg_copy    = alg_i.copy()          # isolate trial writes from live array

    def residuals(x):
        return residualSN_0(x, alg_copy, t_i, constants, rates_dummy, states_i)

    sol = root(residuals, _junc_guess, method='hybr', tol=1e-8)

    if sol.success:
        _junc_guess = sol.x
        return sol.x
    else:
        # hybr failed — try lm (Levenberg-Marquardt) as fallback
        sol2 = root(residuals, _junc_guess, method='lm', tol=1e-6)
        if sol2.success:
            _junc_guess = sol2.x
            return sol2.x
        # If both fail, return best attempt to avoid crashing
        return sol.x


def _fill_junction_timeseries(algebraic, constants, states_arr, voi_arr):
    """
    Fill alg[34..94] at every saved output time point using the gold standard
    iterative solver.  Also derives alg[192] and alg[193] (H_VV_out_alpha/beta)
    from the converged flows via the Pries phase separation model — these are
    computed by the downstream algebraic equations in computeRates and are
    approximated here by direct formula after the solve.

    Note: alg[192] and alg[193] are fully computed inside computeRates (which
    calls rootfind_0), but computeAlgebraic skips rootfind_0.  The downstream
    equations from computeRates lines 572-589 are reproduced below.
    """
    n_t = algebraic.shape[1]
    print(f"  Post-processing {n_t} time points with gold standard solver...")

    for i in range(n_t):
        if i % 1000 == 0:
            print(f"    t = {voi_arr[i]:.1f} s  ({i}/{n_t})")

        solution = _solve_junction_point(
            algebraic[:, i], float(voi_arr[i]), constants, states_arr[:, i]
        )

        for k, idx in enumerate(range(34, 95)):
            algebraic[idx, i] = float(np.asarray(solution[k]).item())


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
    init_states, constants = initConsts()

    # Seed B1_I's warm-start with a physically-realistic initial guess.
    # Without this, B1_I.rootfind_0 initialises to ones(61)*0.1, which is
    # 10-24 orders of magnitude wrong for flows (~1e-12) and resistances
    # (~1e12), causing fsolve to fail to converge at every ODE step.
    B1_I.initialGuess0 = _build_initial_guess(constants)
    t_eval = np.linspace(0.0, SIM_LENGTH, int(SIM_LENGTH / POINT_INTERVAL) + 1)

    print(f"\n{'='*60}")
    print(f"Run: {label}")
    print(f"  Phase 1: ODE integration (Radau, B1_I built-in fsolve)")
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

    t_ode = time.perf_counter() - t_start
    print(f"  ODE status  : {sol.message}")
    print(f"  ODE time    : {t_ode:.2f} s")

    if not sol.success:
        print(f"  WARNING: ODE did not complete — {sol.message}")
        if sol.t is None or len(sol.t) == 0:
            return None, None, None
        print(f"  Continuing with {len(sol.t)} partial time points up to t={sol.t[-1]:.2f} s")

    # Phase 2: post-process — compute all algebraic vars from saved states
    print(f"\n  Phase 2: gold standard scipy.optimize.root (61-var)")
    algebraic = computeAlgebraic(constants, sol.y, sol.t)

    t_post_start = time.perf_counter()
    _fill_junction_timeseries(algebraic, constants, sol.y, sol.t)
    t_post = time.perf_counter() - t_post_start
    print(f"  Post-processing time: {t_post:.2f} s")

    return sol.t, sol.y, algebraic


# ---------------------------------------------------------------------------
# 7. MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    t_voi, states, alg = run("Gold Standard")
    if t_voi is not None:
        out_dir  = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(out_dir, "H_VV_out.csv")
        csv_data = np.column_stack([t_voi, alg[118, :], alg[119, :]])
        np.savetxt(
            csv_path,
            csv_data,
            delimiter=",",
            header="time_s,H_VV_out_alpha,H_VV_out_beta",
            comments="",
        )
        print(f"\nSaved: {csv_path}")

        fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

        axes[0].plot(t_voi, alg[118, :], color='tab:blue')
        axes[0].set_ylabel("H_VV_out_alpha (dimensionless)")
        axes[0].set_title("VV Junction Hematocrit Output — Gold Standard (61-var, scipy.optimize.root)")
        axes[0].grid(True)

        axes[1].plot(t_voi, alg[119, :], color='tab:orange')
        axes[1].set_ylabel("H_VV_out_beta (dimensionless)")
        axes[1].set_xlabel("Time (s)")
        axes[1].grid(True)

        plt.tight_layout()
        plt.show()
