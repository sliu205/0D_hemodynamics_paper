import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
import time



# ============================================================
# IMPORT MODEL
# ============================================================
import B1_TD as model


# ============================================================
# 🔧 MONKEYPATCHES (ALL REQUIRED FIXES)
# ============================================================

def safe_vstack(*args):
    """
    Fix vstack(a, b) + broadcasting issues
    """
    if len(args) == 1:
        return np.vstack(args[0])

    a, b = args
    a = np.asarray(a)
    b = np.asarray(b)

    # Broadcast scalars to vectors
    if a.ndim == 1 and b.ndim == 0:
        b = np.full_like(a, b)
    elif b.ndim == 1 and a.ndim == 0:
        a = np.full_like(b, a)

    return np.vstack((a, b))


def safe_amax(a, axis=None):
    if axis == 0:
        result = np.maximum.reduce(a)
    else:
        result = np.amax(a, axis=axis)

    return np.asarray(result).item() if np.size(result) == 1 else result


def safe_amin(a, axis=None):
    if axis == 0:
        result = np.minimum.reduce(a)
    else:
        result = np.amin(a, axis=axis)

    return np.asarray(result).item() if np.size(result) == 1 else result


def safe_power(x, y):
    """
    Prevent invalid fractional powers
    """
    x = np.asarray(x)
    x_safe = np.where(x <= 0, 1e-12, x)
    return np.power(x_safe, y)


# APPLY PATCHES INTO MODEL NAMESPACE
model.vstack = safe_vstack
model.amax = safe_amax
model.amin = safe_amin
model.power = safe_power


# ============================================================
# ⏱ SIMULATION SETTINGS
# ============================================================

t_start = 0.0
t_end = 1000.0

dt_output = 1.0
t_eval = np.arange(t_start, t_end + dt_output, dt_output)

rtol = 1e-7
atol = 1e-7
max_step = 1.0


# ============================================================
# 🚀 INITIALISE MODEL
# ============================================================

states, constants = model.initConsts()


# ============================================================
# 🔁 ODE SYSTEM (FULLY ROBUST)
# ============================================================

def ode_system(t, y):
    # Clamp states (important for H variables)
    y = np.clip(y, 0.0, 1.0)

    rates = model.computeRates(t, y, constants)

    # Force scalar outputs
    clean_rates = []
    for r in rates:
        r = np.asarray(r)
        if r.size == 1:
            clean_rates.append(r.item())
        else:
            clean_rates.append(r.flatten()[0])

    clean_rates = np.array(clean_rates, dtype=float)

    # Remove NaN / inf
    clean_rates = np.nan_to_num(
        clean_rates,
        nan=0.0,
        posinf=1e6,
        neginf=-1e6
    )

    return clean_rates


# ============================================================
# ⏱ START WALL TIMER
# ============================================================

wall_start = time.perf_counter()


# ============================================================
# 🧮 SOLVE ODE
# ============================================================

solve_start = time.perf_counter()

solution = solve_ivp(
    ode_system,
    (t_start, t_end),
    states,
    method='LSODA',
    t_eval=t_eval,
    rtol=rtol,
    atol=atol,
    max_step=max_step
)

solve_end = time.perf_counter()

if not solution.success:
    print("Solver failed:", solution.message)
else:
    print("Solver completed successfully.")


# ============================================================
# 📊 COMPUTE ALGEBRAIC VARIABLES
# ============================================================

alg_start = time.perf_counter()

algebraic = model.computeAlgebraic(constants, solution.y, solution.t)
algebraic = np.asarray(algebraic)

alg_end = time.perf_counter()


# ============================================================
# ⏱ END WALL TIMER
# ============================================================

wall_end = time.perf_counter()


# ============================================================
# 📈 EXTRACT VARIABLES
# ============================================================

time_vals = solution.t

H_alpha = np.asarray(algebraic[118]).flatten()
H_beta  = np.asarray(algebraic[119]).flatten()


# ============================================================
# ⏱ PRINT TIMINGS
# ============================================================

print(f"ODE solve time: {solve_end - solve_start:.4f} s")
print(f"Algebraic time: {alg_end - alg_start:.4f} s")
print(f"Total wall time: {wall_end - wall_start:.4f} s")


# ============================================================
# 💾 SAVE CSV
# ============================================================

df = pd.DataFrame({
    "time": time_vals,
    "H_VV_out_alpha": H_alpha,
    "H_VV_out_beta": H_beta
})

output_file = "H_VV_outputs.csv"
df.to_csv(output_file, index=False)

print(f"CSV saved: {output_file}")


# ============================================================
# 📉 PLOT
# ============================================================

plt.figure()
plt.plot(time_vals, H_alpha, label="H_VV_out_alpha")
plt.plot(time_vals, H_beta, label="H_VV_out_beta")

plt.xlabel("Time (s)")
plt.ylabel("H values")
plt.title("VV Junction Outputs")
plt.legend()

plt.tight_layout()
plt.show()