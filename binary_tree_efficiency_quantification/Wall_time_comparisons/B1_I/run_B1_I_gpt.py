import time
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp

import numpy as _np

# ============================================================
# SAFE EXP
# ============================================================

def exp(x):
    return _np.exp(_np.clip(x, -50, 50))


# ============================================================
# IMPORT MODEL
# ============================================================

import B1_I as model


# ============================================================
# 🔧 MONKEYPATCHES (MUST COME BEFORE ANY MODEL CALLS)
# ============================================================

def vstack(*args):

    if len(args) == 1:
        return _np.vstack(args[0])

    a, b = args
    a = _np.asarray(a)
    b = _np.asarray(b)

    if a.ndim == 1 and b.ndim == 0:
        b = _np.full_like(a, b)
    elif b.ndim == 1 and a.ndim == 0:
        a = _np.full_like(b, a)

    return _np.vstack((a, b))


def amax(a, axis=None):

    if axis == 0:
        result = _np.maximum.reduce(a)
    else:
        result = _np.amax(a, axis=axis)

    return _np.asarray(result).item() if _np.size(result) == 1 else result


def amin(a, axis=None):

    if axis == 0:
        result = _np.minimum.reduce(a)
    else:
        result = _np.amin(a, axis=axis)

    return _np.asarray(result).item() if _np.size(result) == 1 else result


def power(x, y):

    x = _np.asarray(x)
    x_safe = _np.where(x <= 0, 1e-12, x)

    return _np.power(x_safe, y)


# Apply patches BEFORE using model
model.vstack = vstack
model.amax = amax
model.amin = amin
model.power = power


# ============================================================
# 🚀 INITIALISE MODEL
# ============================================================

states, constants = model.initConsts()

# ============================================================
# GET LEGENDS (human readable variable names)
# ============================================================

legend_states = model.createLegends()[0]
legend_algebraic = model.createLegends()[1]
legend_constants = model.createLegends()[2]


# ============================================================
# SAVE INITIAL STATES (READABLE)
# ============================================================

states_file = "initial_states_readable.csv"

with open(states_file, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["variable", "value"])

    for i, val in enumerate(states):

        name = legend_states[i] if i < len(legend_states) else f"state_{i}"

        writer.writerow([name, val])

print("Initial states saved:", os.path.abspath(states_file))


# ============================================================
# SAVE INITIAL CONSTANTS (READABLE)
# ============================================================

constants_file = "initial_constants_readable.csv"

with open(constants_file, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["variable", "value"])

    for i, val in enumerate(constants):

        name = legend_constants[i] if i < len(legend_constants) else f"constant_{i}"

        writer.writerow([name, val])

print("Initial constants saved:", os.path.abspath(constants_file))


# ============================================================
# COMPUTE ALGEBRAIC VARIABLES AT t=0
# ============================================================

alg0 = model.computeAlgebraic(
    constants,
    np.array(states).reshape(-1,1),
    np.array([0])
)

alg0 = np.asarray(alg0).flatten()


# ============================================================
# SAVE INITIAL ALGEBRAIC VARIABLES (READABLE)
# ============================================================

alg_file = "initial_algebraic_readable.csv"

with open(alg_file, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["variable", "value"])

    for i, val in enumerate(alg0):

        name = legend_algebraic[i] if i < len(legend_algebraic) else f"algebraic_{i}"

        writer.writerow([name, val])

print("Initial algebraic variables saved:", os.path.abspath(alg_file))
# ============================================================
# COMPUTE ALGEBRAIC VARIABLES AT t=0
# ============================================================

alg0 = model.computeAlgebraic(constants, np.array(states).reshape(-1,1), np.array([0]))
alg0 = np.asarray(alg0).flatten()

alg_file = "initial_algebraic_values.csv"

with open(alg_file, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["index", "value"])

    for i,val in enumerate(alg0):
        writer.writerow([i,val])

print("Initial algebraic values saved to:", os.path.abspath(alg_file))


print("\nModel size")
print("States:",len(states))
print("Constants:",len(constants))
print("Algebraic:",len(alg0))


# ============================================================
# SIMULATION SETTINGS
# ============================================================

t_start = 0
t_end = 1000

t_eval = np.arange(t_start,t_end+1,1)

rtol = 1e-7
atol = 1e-7


# ============================================================
# ODE SYSTEM
# ============================================================

def ode_system(t,y):

    y = np.nan_to_num(y,nan=0,posinf=1e6,neginf=-1e6)

    rates = model.computeRates(t,y,constants)

    clean_rates = []

    for r in rates:

        r = np.asarray(r)

        if r.size == 1:
            clean_rates.append(r.item())
        else:
            clean_rates.append(r.flatten()[0])

    clean_rates = np.array(clean_rates,dtype=float)

    clean_rates = np.nan_to_num(clean_rates,nan=0,posinf=1e6,neginf=-1e6)

    return clean_rates


# ============================================================
# WALL TIMER START
# ============================================================

wall_start = time.perf_counter()


# ============================================================
# SOLVE ODE
# ============================================================

solve_start = time.perf_counter()

solution = solve_ivp(
    ode_system,
    (t_start,t_end),
    states,
    method="BDF",
    t_eval=t_eval,
    rtol=rtol,
    atol=atol,
    max_step=1
)

solve_end = time.perf_counter()

print("Solver success:",solution.success)


# ============================================================
# COMPUTE ALGEBRAIC VARIABLES
# ============================================================

alg_start = time.perf_counter()

algebraic = model.computeAlgebraic(constants,solution.y,solution.t)
algebraic = np.asarray(algebraic)

alg_end = time.perf_counter()


wall_end = time.perf_counter()


# ============================================================
# EXTRACT VARIABLES
# ============================================================

time_vals = solution.t

H_alpha = algebraic[118]
H_beta = algebraic[119]


# ============================================================
# PRINT TIMINGS
# ============================================================

print("\nTiming summary")

print("ODE solve:",solve_end-solve_start,"s")
print("Algebraic:",alg_end-alg_start,"s")
print("Total wall:",wall_end-wall_start,"s")


# ============================================================
# SAVE CSV
# ============================================================

df = pd.DataFrame({
    "time":time_vals,
    "H_VV_out_alpha":H_alpha,
    "H_VV_out_beta":H_beta
})

csv_file = "H_VV_outputs.csv"

df.to_csv(csv_file,index=False)

print("CSV saved:",os.path.abspath(csv_file))


# ============================================================
# PLOT
# ============================================================

plt.figure()

plt.plot(time_vals,H_alpha,label="H_VV_out_alpha")
plt.plot(time_vals,H_beta,label="H_VV_out_beta")

plt.xlabel("Time (s)")
plt.ylabel("Hematocrit")
plt.title("VV Junction Outputs")

plt.legend()

plot_file = "H_VV_outputs.png"

plt.savefig(plot_file,dpi=300)

print("Plot saved:",os.path.abspath(plot_file))

plt.show()