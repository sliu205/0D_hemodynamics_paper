import time
import numpy as np
from scipy.integrate import solve_ivp
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
# 2. SETTINGS (identical to run_B1_I.py for fair wall-time comparison)
# ---------------------------------------------------------------------------
SIM_LENGTH     = 1000.0
POINT_INTERVAL = 0.1
DT_MAX         = 0.1
RTOL           = 1e-5
ATOL           = 1e-5

# ---------------------------------------------------------------------------
# 3. IMPORT B1_TD AND APPLY PATCHES
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import B1_TD

# FIX 1: safe_power
# Original used maximum(base, 0.0) which gives 0^negative_exponent = inf.
# Using abs + tiny floor prevents that without changing results for normal values.
def safe_power(base, exponent):
    return np.power(np.maximum(np.abs(base), 1e-300), exponent)

B1_TD.power = safe_power

# FIX 2: safe_exp
# The Pries bifurcation formula exp(A + B*ph) overflows when ph blows up
# (ph = log(y/(1-y)) diverges as y -> 0 or 1).
# Clipping at +-700 keeps values in float64 range (exp(709) ~ max float64).
_orig_exp = np.exp
def safe_exp(x):
    return _orig_exp(np.clip(x, -700.0, 700.0))

B1_TD.exp = safe_exp

from B1_TD import initConsts, computeRates, computeAlgebraic

# ---------------------------------------------------------------------------
# 4. ODE RIGHT-HAND SIDE
# ---------------------------------------------------------------------------

def make_rhs(constants):
    def rhs(t, y):
        raw = computeRates(t, y, constants)
        return np.array([np.asarray(r).item() for r in raw], dtype=float)
    return rhs

# ---------------------------------------------------------------------------
# 5. RUN
# ---------------------------------------------------------------------------

def run(label):
    init_states, constants = initConsts()
    t_eval = np.linspace(0.0, SIM_LENGTH, int(SIM_LENGTH / POINT_INTERVAL) + 1)

    print(f"\n{'='*60}")
    print(f"Run: {label}")
    print(f"  No iterative solver — H_mean computed directly from ODE state")
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
        atol=ATOL,
    )

    t_ode = time.perf_counter() - t_start
    print(f"  ODE status : {sol.message}")
    print(f"  ODE time   : {t_ode:.2f} s")

    if not sol.success:
        return None, None, None

    t_post_start = time.perf_counter()
    algebraic = computeAlgebraic(constants, sol.y, sol.t)
    t_post = time.perf_counter() - t_post_start
    print(f"  Post-processing time: {t_post:.2f} s")
    print(f"  Total wall time     : {t_ode + t_post:.2f} s")

    return sol.t, sol.y, algebraic

# ---------------------------------------------------------------------------
# 6. MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    t_voi, states, alg = run("No iterative solver (B1_TD)")
    if t_voi is not None:

        # If indices look wrong, confirm with:
        #   from B1_TD import createLegends
        #   _, _, leg_alg, _, _ = createLegends()
        #   for i, s in enumerate(leg_alg): 
        #       if 'H_VV_out' in s: print(i, s)
        alpha_idx = 192
        beta_idx  = 193

        out_dir  = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(out_dir, "H_VV_out_TD.csv")
        csv_data = np.column_stack([t_voi, alg[alpha_idx, :], alg[beta_idx, :]])
        np.savetxt(
            csv_path,
            csv_data,
            delimiter=",",
            header="time_s,H_VV_out_alpha,H_VV_out_beta",
            comments="",
        )
        print(f"\nSaved: {csv_path}")

        fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
        axes[0].plot(t_voi, alg[alpha_idx, :], color='tab:blue')
        axes[0].set_ylabel("H_VV_out_alpha (dimensionless)")
        axes[0].set_title("VV Junction Hematocrit — No iterative solver (B1_TD)")
        axes[0].grid(True)
        axes[1].plot(t_voi, alg[beta_idx, :], color='tab:orange')
        axes[1].set_ylabel("H_VV_out_beta (dimensionless)")
        axes[1].set_xlabel("Time (s)")
        axes[1].grid(True)
        plt.tight_layout()
        plt.show()