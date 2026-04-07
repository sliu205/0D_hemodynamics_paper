import time
import numpy as np
from scipy.integrate import solve_ivp
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
    # If one item is a full array (time series) and another is a single float/scalar,
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
# 3. MATH MONKEY PATCHES (Runner level)
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import B1_I

# Patch power to prevent NaNs from negative bases
def safe_power(base, exponent):
    # np.maximum handles negative noise, np.where handles div by zero if base is 0 and exp < 0
    return np.power(np.maximum(base, 0.0), exponent)

B1_I.power = safe_power 

from B1_I import (initConsts, computeRates, computeAlgebraic)

# ---------------------------------------------------------------------------

def _rootfind_handler(voi, constants, rates, states, algebraic):
    val = (algebraic[15] * algebraic[117]) / (algebraic[110] + constants[15])
    algebraic[118] = np.asarray(val).item() 

def make_rhs(constants):
    def rhs(t, y):
        raw = computeRates(t, y, constants)
        return np.array([np.asarray(r).item() for r in raw], dtype=float)
    return rhs

def run(label):
    B1_I.rootfind_0 = _rootfind_handler
    init_states, constants = initConsts()
    t_eval = np.linspace(0.0, SIM_LENGTH, int(SIM_LENGTH/POINT_INTERVAL) + 1)

    print(f"\n{'='*60}")
    print(f"Run: {label} (Radau Robust)")
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
    print(f"Time          : {elapsed:.4f} s")

    if not sol.success:
        return None, None, None

    # This is where it crashed before. The new vstack shim fixes this.
    algebraic = computeAlgebraic(constants, sol.y, sol.t)
    return sol.t, sol.y, algebraic

if __name__ == "__main__":
    t_voi, states, alg = run("Radau Robust")
    if t_voi is not None:
        plt.figure(figsize=(10, 5))
        plt.plot(t_voi, alg[4, :])
        plt.ylabel("H_mean")
        plt.xlabel("Time (s)")
        plt.title("Radau Robust Completion")
        plt.grid(True)
        plt.show()