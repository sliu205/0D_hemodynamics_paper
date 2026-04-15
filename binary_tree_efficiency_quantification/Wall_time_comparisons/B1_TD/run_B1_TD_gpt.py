"""
inspect_B1_TD.py
================
Initialises B1_TD, prints every initial state / constant / algebraic
variable, then highlights every variable whose legend contains a pressure
keyword (u, mmHg, J_per_m3) or a flow keyword (v, m3_per_s, mm3_per_s).
"""

import numpy as _np
import B1_TD as model


# ============================================================
# MONKEYPATCHES  (required before any model call)
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


model.vstack = vstack
model.amax   = amax
model.amin   = amin
model.power  = power


# ============================================================
# HELPERS
# ============================================================

COL_W = 72   # width of label column

def section(title):
    print()
    print("=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_table(rows, header=("index", "variable", "value")):
    """rows: list of (index, label, value)"""
    print(f"  {header[0]:<7}  {header[1]:<{COL_W}}  {header[2]}")
    print(f"  {'-'*7}  {'-'*COL_W}  {'-'*20}")
    for idx, label, val in rows:
        try:
            print(f"  {idx:<7}  {label:<{COL_W}}  {val:.6g}")
        except (TypeError, ValueError):
            print(f"  {idx:<7}  {label:<{COL_W}}  {val}")


def is_pressure(label):
    """True when the legend entry describes a pressure variable."""
    lbl = label.lower()
    keywords = ("j_per_m3", "mmhg", "_u ", "_u_", " u ", " u_", "pressure",
                "u in component", "u_d in component", "u_mmhg")
    return any(k in lbl for k in keywords)


def is_flow(label):
    """True when the legend entry describes a flow variable."""
    lbl = label.lower()
    keywords = ("m3_per_s", "mm3_per_s", "_v ", "_v_", " v ", " v_",
                "v in component", "v_d in component", "v_mm3_s", "flow",
                "qin", "qout", "rbc_in", "rbc_out")
    return any(k in lbl for k in keywords)


# ============================================================
# INITIALISE
# ============================================================

states, constants = model.initConsts()
legends = model.createLegends()
legend_states    = legends[0]
legend_algebraic = legends[1]
legend_constants = legends[2]

# Compute algebraic at t = 0
alg0 = model.computeAlgebraic(
    constants,
    _np.array(states).reshape(-1, 1),
    _np.array([0.0])
)
alg0 = _np.asarray(alg0).flatten()


# ============================================================
# 1.  ALL INITIAL STATES
# ============================================================

section("INITIAL STATE VARIABLES")
rows = [(i, legend_states[i] if i < len(legend_states) else f"state_{i}", states[i])
        for i in range(len(states))]
print_table(rows)


# ============================================================
# 2.  ALL CONSTANTS
# ============================================================

section("CONSTANTS")
rows = [(i, legend_constants[i] if i < len(legend_constants) else f"constant_{i}", constants[i])
        for i in range(len(constants))]
print_table(rows)


# ============================================================
# 3.  ALL ALGEBRAIC VARIABLES AT t = 0
# ============================================================

section("ALGEBRAIC VARIABLES AT t = 0")
rows = [(i, legend_algebraic[i] if i < len(legend_algebraic) else f"algebraic_{i}", alg0[i])
        for i in range(len(alg0))]
print_table(rows)


# ============================================================
# 4.  PRESSURES  (algebraic + states)
# ============================================================

section("PRESSURES  (J_per_m3 / mmHg / u variables)")

pressure_rows = []

# from algebraic
for i, lbl in enumerate(legend_algebraic):
    if lbl and is_pressure(lbl):
        pressure_rows.append((f"alg[{i}]", lbl, alg0[i]))

# from states
for i, lbl in enumerate(legend_states):
    if lbl and is_pressure(lbl):
        pressure_rows.append((f"state[{i}]", lbl, states[i]))

if pressure_rows:
    print_table(pressure_rows, header=("source", "variable", "value"))
else:
    print("  (none found)")


# ============================================================
# 5.  FLOWS  (algebraic + constants)
# ============================================================

section("FLOWS  (m3_per_s / mm3_per_s / v / Q variables)")

flow_rows = []

# from algebraic
for i, lbl in enumerate(legend_algebraic):
    if lbl and is_flow(lbl):
        flow_rows.append((f"alg[{i}]", lbl, alg0[i]))

# from constants (some boundary flows are constants)
for i, lbl in enumerate(legend_constants):
    if lbl and is_flow(lbl):
        flow_rows.append((f"const[{i}]", lbl, constants[i]))

if flow_rows:
    print_table(flow_rows, header=("source", "variable", "value"))
else:
    print("  (none found)")


# ============================================================
# 6.  SUMMARY
# ============================================================

section("SUMMARY")
print(f"  States     : {len(states)}")
print(f"  Constants  : {len(constants)}")
print(f"  Algebraic  : {len(alg0)}")
print(f"  Pressures identified : {len(pressure_rows)}")
print(f"  Flows identified     : {len(flow_rows)}")
print()