"""Generated model (ITERATIVE variant - scipy.optimize.root on H_mean)"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root
import matplotlib.pyplot as plt

# Safe power function to handle negative bases with non-integer exponents
def safe_power(base, exponent):
    """
    Safe version of np.power that handles edge cases:
    - If base < 0 and exponent is non-integer, use absolute value
    - Clips very small values to avoid numerical issues
    """
    base = np.clip(base, 1e-15, None)  # Avoid zero/negative
    return np.power(base, exponent)

# Parameters
PV1__H_global_L = 0.45
PV1__H_global_R = 0.45
PV1__R_constriction_base = 0.0
PV1__R_constriction_final = 1e21
PV1__gamma_mirror = 0.1
PV1__l = 0.000015
PV1__mu_plasma = 0.001
PV1__one_mm3 = 1e-09
PV1__q_C_init = 0.0
PV1__r = 6e-06
PV1__t0 = 500.0
PV1__tau_H_down = 0.001
PV1__tau_H_mean = 0.001
PV1__tau_junc = 0.0001
PV1__tau_link = 0.001
PV1__tau_sig = 1.0
PV1__u_ext = 133.0
PV1__v_eps = 1e-30
PV1__v_scale = 1e-50
PV2__H_global_L = 0.45
PV2__H_global_R = 0.45
PV2__R_constriction_base = 0.0
PV2__R_constriction_final = 0.0
PV2__gamma_mirror = 0.1
PV2__l = 0.000015
PV2__mu_plasma = 0.001
PV2__one_mm3 = 1e-09
PV2__q_C_init = 0.0
PV2__r = 6e-06
PV2__t0 = 500.0
PV2__tau_H_down = 0.001
PV2__tau_H_mean = 0.001
PV2__tau_junc = 0.0001
PV2__tau_link = 0.001
PV2__tau_sig = 1.0
PV2__u_ext = 133.0
PV2__v_eps = 1e-30
PV2__v_scale = 1e-50
V1__H_L_out_RHS = 0.45
V1__H_global_L = 0.45
V1__H_global_R = 0.45
V1__gamma_mirror = 0.1
V1__l = 0.00025
V1__mu_plasma = 0.001
V1__one_mm3 = 1e-09
V1__q_C_init = 0.0
V1__r = 5.5e-06
V1__tau_H_down = 0.001
V1__tau_H_mean = 0.001
V1__tau_junc = 0.0001
V1__tau_link = 0.001
V1__u_ext = 133.0
V1__u_out = 6632.7695
V1__v_eps = 1e-30
V1__v_scale = 1e-50
V2__H_L_out_RHS = 0.45
V2__H_global_L = 0.45
V2__H_global_R = 0.45
V2__gamma_mirror = 0.1
V2__l = 0.00025
V2__mu_plasma = 0.001
V2__one_mm3 = 1e-09
V2__q_C_init = 0.0
V2__r = 5.5e-06
V2__tau_H_down = 0.001
V2__tau_H_mean = 0.001
V2__tau_junc = 0.0001
V2__tau_link = 0.001
V2__u_ext = 133.0
V2__u_out = 6632.7695
V2__v_eps = 1e-30
V2__v_scale = 1e-50
VV_junc1__C_conn2 = 8.51e-22
VV_junc1__H_global_L = 0.45
VV_junc1__H_global_R = 0.45
VV_junc1__H_to2 = 0.0
VV_junc1__R = 1000000000000000.0
VV_junc1__R_VV_junc = 1000000000000000
VV_junc1__div_0 = 1e-25
VV_junc1__div_0y = 1e-08
VV_junc1__k = 1000.0
VV_junc1__l = 0.000001
VV_junc1__mu_plasma = 0.001
VV_junc1__one_mm3 = 1e-09
VV_junc1__q_C_init = 0.0
VV_junc1__r = 6e-06
VV_junc1__r_bc2 = 0.0
VV_junc1__tau_junc = 0.0001
VV_junc1__u_ext = 133.0
VV_junc1__v_scale = 1e-50
VV_junc1__v_threshold = 1e-18
VV_junc1__vbc2 = 0.0
global__H_global_L = 0.45
global__H_global_R = 0.45
global__R = 1000000000000000.0
global__R_VV_junc = 1000000000000000
global__R_constriction_base = 0.0
global__div_0 = 1e-25
global__div_0y = 1e-08
global__gamma_mirror = 0.1
global__k = 1000.0
global__mu_plasma = 0.001
global__one_mm3 = 1e-09
global__q_C_init = 0.0
global__t0 = 500.0
global__tau_H_down = 0.001
global__tau_H_mean = 0.001
global__tau_junc = 0.0001
global__tau_link = 0.001
global__tau_sig = 1.0
global__u_ext = 133.0
global__v_eps = 1e-30
global__v_scale = 1e-50
global__v_threshold = 1e-18
inlet__H_R_out_LHS = 0.45
inlet__H_global_L = 0.45
inlet__H_global_R = 0.45
inlet__gamma_mirror = 0.1
inlet__l = 0.0003
inlet__mu_plasma = 0.001
inlet__one_mm3 = 1e-09
inlet__q_C_init = 0.0
inlet__r = 6e-06
inlet__tau_H_down = 0.001
inlet__tau_H_mean = 0.001
inlet__tau_junc = 0.0001
inlet__tau_link = 0.001
inlet__u_ext = 133.0
inlet__u_in = 6666.1
inlet__v_eps = 1e-30
inlet__v_scale = 1e-50

# =========================================================================
# Iterative H_mean solver (IT-4)
# =========================================================================
# One unknown per vessel with H_mean -> mu -> R -> v,v_d -> RBC_volume -> H_mean.
# Residual = implied_H_mean - trial_H_mean; solved by scipy.optimize.root
# once per RHS evaluation. The previous solution is cached as the initial
# guess for the next call (solve_ivp typically takes small steps).

# Zero-flow regularization (IT-4e).
# When flow magnitude is near ZERO_FLOW_REG_EPS, the solver anchors H_mean
# to H_global_L to break the degeneracy of a 0 = 0 residual.
# ZERO_FLOW_REG_EPS is the flow scale at which the anchor activates
# (units: m^3/s; pick comfortably below your smallest expected flow).
# ZERO_FLOW_ANCHOR_STRENGTH is the magnitude of the anchor (unitless; pick
# much bigger than residual noise at the fixed point, ~1e-10).
# Set either to 0.0 to disable.
ZERO_FLOW_REG_EPS = 1e-12
ZERO_FLOW_ANCHOR_STRENGTH = 1e-10

# Ordered list of iterative unknown names.
iter_unknown_names = [
    'PV1__H_mean',
    'PV2__H_mean',
    'V1__H_mean',
    'V2__H_mean',
    'inlet__H_mean',
]

# Initial guess (from CSV algebraic entries, fallback 0.45).
_iter_initial_guess = np.array([
    0.4506081993303387,
    0.4506082579433263,
    0.4500038831722489,
    0.45000388368944083,
    0.45000000904182835,
])

# Cached last solution (reused as warm-start on next call).
_iter_last_solution = [_iter_initial_guess.copy()]

def _eval_algebraics(t, y, H_means):
    """Evaluate all algebraics given a trial H_means vector.
    Returns a dict of all computed algebraic variable values,
    also including the supplied H_means under their canonical names.
    """
    # Unpack state
    inlet__H_link_R = y[0]
    inlet__H_link_L = y[1]
    inlet__H_down = y[2]
    inlet__q_C = y[3]
    VV_junc1__RBC_volume = y[4]
    VV_junc1__q_C = y[5]
    VV_junc1__q_C_d = y[6]
    PV1__H_link_R = y[7]
    PV1__H_link_L = y[8]
    PV1__H_down = y[9]
    PV1__q_C = y[10]
    PV2__H_link_R = y[11]
    PV2__H_link_L = y[12]
    PV2__H_down = y[13]
    PV2__q_C = y[14]
    V1__H_link_R = y[15]
    V1__H_link_L = y[16]
    V1__H_down = y[17]
    V1__q_C = y[18]
    V2__H_link_R = y[19]
    V2__H_link_L = y[20]
    V2__H_down = y[21]
    V2__q_C = y[22]

    # Time
    environment__time = t

    # Inject iterative unknowns (supplied by caller)
    PV1__H_mean = H_means[0]
    PV2__H_mean = H_means[1]
    V1__H_mean = H_means[2]
    V2__H_mean = H_means[3]
    inlet__H_mean = H_means[4]

    # Algebraic equations (topo-sorted)
    inlet__H_L_in = inlet__H_link_L
    inlet__H_R_in = inlet__H_link_R
    inlet__q_us = np.pi*np.square(inlet__r)*inlet__l
    inlet__q = inlet__q_us+inlet__q_C
    inlet__C = np.pi*np.square(8.5e-9)*inlet__l/133.322
    inlet__Z = (0.8+np.exp(-0.075*2*inlet__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*inlet__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*inlet__r*1e6, 12))
    inlet__mu_45 = 6*np.exp(-0.085*2*inlet__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*inlet__r*1e6, 0.645))
    inlet__hem_dep_u_rel = 1+(inlet__mu_45-1)*(safe_power(1-inlet__H_mean, inlet__Z)-1)/(safe_power(1-inlet__H_global_L, inlet__Z)-1)*np.square(2*inlet__r*1e6/(2*inlet__r*1e6-1.1))
    inlet__u = inlet__q_C/inlet__C+inlet__u_ext
    VV_junc1__vj2 = VV_junc1__vbc2
    VV_junc1__D1 = 2*inlet__r
    VV_junc1__D2 = 2*VV_junc1__r_bc2
    VV_junc1__D3 = 2*PV1__r
    VV_junc1__D4 = 2*PV2__r
    VV_junc1__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc1__vj2/VV_junc1__v_scale)
    VV_junc1__w_out2 = 1-VV_junc1__w_in2
    VV_junc1__Qin2 = VV_junc1__w_in2*VV_junc1__vj2
    VV_junc1__Qout2 = VV_junc1__w_out2*-VV_junc1__vj2
    VV_junc1__q_us = np.pi*np.square(VV_junc1__r)*VV_junc1__l
    VV_junc1__q = VV_junc1__q_us+VV_junc1__q_C+VV_junc1__q_C_d
    VV_junc1__bc2_is_in = (1 if VV_junc1__Qin2 > VV_junc1__v_threshold else 0)
    VV_junc1__bc2_is_out = (1 if VV_junc1__Qout2 > VV_junc1__v_threshold else 0)
    VV_junc1__C_max12 = (inlet__C if inlet__C > VV_junc1__C_conn2 else (VV_junc1__C_conn2 if inlet__C <= VV_junc1__C_conn2 else 0.0))
    PV1__R_constriction = PV1__R_constriction_base+(PV1__R_constriction_final-PV1__R_constriction_base)/(1+np.exp(-(environment__time-PV1__t0)/PV1__tau_sig))
    PV1__H_L_in = PV1__H_link_L
    PV1__H_R_in = PV1__H_link_R
    PV1__q_us = np.pi*np.square(PV1__r)*PV1__l
    PV1__q = PV1__q_us+PV1__q_C
    PV1__C = np.pi*np.square(8.5e-9)*PV1__l/133.322
    PV1__Z = (0.8+np.exp(-0.075*2*PV1__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV1__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV1__r*1e6, 12))
    PV1__mu_45 = 6*np.exp(-0.085*2*PV1__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV1__r*1e6, 0.645))
    PV1__hem_dep_u_rel = 1+(PV1__mu_45-1)*(safe_power(1-PV1__H_mean, PV1__Z)-1)/(safe_power(1-PV1__H_global_L, PV1__Z)-1)*np.square(2*PV1__r*1e6/(2*PV1__r*1e6-1.1))
    PV1__u = PV1__q_C/PV1__C+PV1__u_ext
    PV2__R_constriction = PV2__R_constriction_base+(PV2__R_constriction_final-PV2__R_constriction_base)/(1+np.exp(-(environment__time-PV2__t0)/PV2__tau_sig))
    PV2__H_L_in = PV2__H_link_L
    PV2__H_R_in = PV2__H_link_R
    PV2__q_us = np.pi*np.square(PV2__r)*PV2__l
    PV2__q = PV2__q_us+PV2__q_C
    PV2__C = np.pi*np.square(8.5e-9)*PV2__l/133.322
    PV2__Z = (0.8+np.exp(-0.075*2*PV2__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV2__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV2__r*1e6, 12))
    PV2__mu_45 = 6*np.exp(-0.085*2*PV2__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV2__r*1e6, 0.645))
    PV2__hem_dep_u_rel = 1+(PV2__mu_45-1)*(safe_power(1-PV2__H_mean, PV2__Z)-1)/(safe_power(1-PV2__H_global_L, PV2__Z)-1)*np.square(2*PV2__r*1e6/(2*PV2__r*1e6-1.1))
    PV2__u = PV2__q_C/PV2__C+PV2__u_ext
    V1__H_L_in = V1__H_link_L
    V1__H_R_in = V1__H_link_R
    V1__q_us = np.pi*np.square(V1__r)*V1__l
    V1__q = V1__q_us+V1__q_C
    V1__C = np.pi*np.square(8.5e-9)*V1__l/133.322
    V1__Z = (0.8+np.exp(-0.075*2*V1__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V1__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V1__r*1e6, 12))
    V1__mu_45 = 6*np.exp(-0.085*2*V1__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V1__r*1e6, 0.645))
    V1__hem_dep_u_rel = 1+(V1__mu_45-1)*(safe_power(1-V1__H_mean, V1__Z)-1)/(safe_power(1-V1__H_global_L, V1__Z)-1)*np.square(2*V1__r*1e6/(2*V1__r*1e6-1.1))
    V1__u = V1__q_C/V1__C+V1__u_ext
    V2__H_L_in = V2__H_link_L
    V2__H_R_in = V2__H_link_R
    V2__q_us = np.pi*np.square(V2__r)*V2__l
    V2__q = V2__q_us+V2__q_C
    V2__C = np.pi*np.square(8.5e-9)*V2__l/133.322
    V2__Z = (0.8+np.exp(-0.075*2*V2__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V2__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V2__r*1e6, 12))
    V2__mu_45 = 6*np.exp(-0.085*2*V2__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V2__r*1e6, 0.645))
    V2__hem_dep_u_rel = 1+(V2__mu_45-1)*(safe_power(1-V2__H_mean, V2__Z)-1)/(safe_power(1-V2__H_global_L, V2__Z)-1)*np.square(2*V2__r*1e6/(2*V2__r*1e6-1.1))
    V2__u = V2__q_C/V2__C+V2__u_ext
    inlet__RBC_volume_init = inlet__H_global_L*inlet__q_us
    inlet__mu = inlet__hem_dep_u_rel*inlet__mu_plasma
    inlet__R = 8*inlet__mu*inlet__l/(np.pi*safe_power(inlet__r, 4))
    inlet__v = (inlet__u_in-inlet__u)/(inlet__R/2)
    inlet__u_mmHg = inlet__u/133.322
    VV_junc1__RBC_volume_init = VV_junc1__H_global_L*VV_junc1__q_us
    VV_junc1__H_mean = VV_junc1__RBC_volume/(VV_junc1__q_us+VV_junc1__div_0)
    VV_junc1__C_max123 = (VV_junc1__C_max12 if VV_junc1__C_max12 > PV1__C else (PV1__C if VV_junc1__C_max12 <= PV1__C else 0.0))
    VV_junc1__C = (VV_junc1__C_max123 if VV_junc1__C_max123 > PV2__C else (PV2__C if VV_junc1__C_max123 <= PV2__C else 0.0))
    PV1__RBC_volume_init = PV1__H_global_L*PV1__q_us
    PV1__mu = PV1__hem_dep_u_rel*PV1__mu_plasma
    PV1__R = 8*PV1__mu*PV1__l/(np.pi*safe_power(PV1__r, 4))+PV1__R_constriction
    PV1__u_mmHg = PV1__u/133.322
    PV1__v_d = (PV1__u-V1__u)/(PV1__R/2)
    PV2__RBC_volume_init = PV2__H_global_L*PV2__q_us
    PV2__mu = PV2__hem_dep_u_rel*PV2__mu_plasma
    PV2__R = 8*PV2__mu*PV2__l/(np.pi*safe_power(PV2__r, 4))+PV2__R_constriction
    PV2__u_mmHg = PV2__u/133.322
    PV2__v_d = (PV2__u-V2__u)/(PV2__R/2)
    V1__RBC_volume_init = V1__H_global_L*V1__q_us
    V1__mu = V1__hem_dep_u_rel*V1__mu_plasma
    V1__R = 8*V1__mu*V1__l/(np.pi*safe_power(V1__r, 4))
    V1__v = (V1__u-V1__u_out)/V1__R
    V1__u_mmHg = V1__u/133.322
    V2__RBC_volume_init = V2__H_global_L*V2__q_us
    V2__mu = V2__hem_dep_u_rel*V2__mu_plasma
    V2__R = 8*V2__mu*V2__l/(np.pi*safe_power(V2__r, 4))
    V2__v = (V2__u-V2__u_out)/V2__R
    V2__u_mmHg = V2__u/133.322
    inlet__w_v = 0.5+1/np.pi*np.arctan(inlet__v/inlet__v_scale)
    inlet__v_pos = inlet__w_v*inlet__v
    inlet__v_neg = (1-inlet__w_v)*-inlet__v
    inlet__v_mm3_s = inlet__v/inlet__one_mm3
    VV_junc1__u = VV_junc1__q_C/(VV_junc1__C/2)+VV_junc1__u_ext
    VV_junc1__u_mmHg = VV_junc1__u/133.322
    VV_junc1__u_d = VV_junc1__q_C_d/(VV_junc1__C/2)+VV_junc1__u_ext
    VV_junc1__u_d_mmHg = VV_junc1__u_d/133.322
    PV1__w_v_d = 0.5+1/np.pi*np.arctan(PV1__v_d/PV1__v_scale)
    PV1__H_up = PV1__w_v_d*PV1__H_L_in+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__s_v_d = np.abs(PV1__v_d)/(np.abs(PV1__v_d)+PV1__v_eps)
    PV1__H_L_out = (1-PV1__w_v_d)*PV1__H_down+PV1__w_v_d*PV1__H_L_in
    PV1__H_R_out = PV1__w_v_d*PV1__H_down+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__v_d_pos = PV1__w_v_d*PV1__v_d
    PV1__v_d_neg = (1-PV1__w_v_d)*-PV1__v_d
    PV1__H_volume_R = PV1__w_v_d*PV1__H_R_out+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__v = (VV_junc1__u_d-PV1__u)/(PV1__R/2)
    PV1__v_d_mm3_s = PV1__v_d/PV1__one_mm3
    PV2__w_v_d = 0.5+1/np.pi*np.arctan(PV2__v_d/PV2__v_scale)
    PV2__H_up = PV2__w_v_d*PV2__H_L_in+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__s_v_d = np.abs(PV2__v_d)/(np.abs(PV2__v_d)+PV2__v_eps)
    PV2__H_L_out = (1-PV2__w_v_d)*PV2__H_down+PV2__w_v_d*PV2__H_L_in
    PV2__H_R_out = PV2__w_v_d*PV2__H_down+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__v_d_pos = PV2__w_v_d*PV2__v_d
    PV2__v_d_neg = (1-PV2__w_v_d)*-PV2__v_d
    PV2__H_volume_R = PV2__w_v_d*PV2__H_R_out+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__v = (VV_junc1__u_d-PV2__u)/(PV2__R/2)
    PV2__v_d_mm3_s = PV2__v_d/PV2__one_mm3
    V1__w_v = 0.5+1/np.pi*np.arctan(V1__v/V1__v_scale)
    V1__H_up = V1__w_v*V1__H_L_in+(1-V1__w_v)*V1__H_R_in
    V1__s_v = np.abs(V1__v)/(np.abs(V1__v)+V1__v_eps)
    V1__H_L_out = (1-V1__w_v)*V1__H_down+V1__w_v*V1__H_L_in
    V1__H_R_out = V1__w_v*V1__H_down+(1-V1__w_v)*V1__H_R_in
    V1__v_pos = V1__w_v*V1__v
    V1__v_neg = (1-V1__w_v)*-V1__v
    V1__H_volume_L = V1__w_v*V1__H_L_in+(1-V1__w_v)*V1__H_L_out
    V1__H_volume_R = V1__w_v*V1__H_R_out+(1-V1__w_v)*V1__H_R_in
    V1__v_mm3_s = V1__v/V1__one_mm3
    V2__w_v = 0.5+1/np.pi*np.arctan(V2__v/V2__v_scale)
    V2__H_up = V2__w_v*V2__H_L_in+(1-V2__w_v)*V2__H_R_in
    V2__s_v = np.abs(V2__v)/(np.abs(V2__v)+V2__v_eps)
    V2__H_L_out = (1-V2__w_v)*V2__H_down+V2__w_v*V2__H_L_in
    V2__H_R_out = V2__w_v*V2__H_down+(1-V2__w_v)*V2__H_R_in
    V2__v_pos = V2__w_v*V2__v
    V2__v_neg = (1-V2__w_v)*-V2__v
    V2__H_volume_L = V2__w_v*V2__H_L_in+(1-V2__w_v)*V2__H_L_out
    V2__H_volume_R = V2__w_v*V2__H_R_out+(1-V2__w_v)*V2__H_R_in
    V2__v_mm3_s = V2__v/V2__one_mm3
    inlet__v_d = (inlet__u-VV_junc1__u)/(inlet__R/2)
    VV_junc1__vj1 = inlet__v_d
    VV_junc1__vj3 = -PV1__v
    VV_junc1__vj4 = -PV2__v
    VV_junc1__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc1__vj1/VV_junc1__v_scale)
    VV_junc1__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc1__vj3/VV_junc1__v_scale)
    VV_junc1__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc1__vj4/VV_junc1__v_scale)
    VV_junc1__w_out1 = 1-VV_junc1__w_in1
    VV_junc1__w_out3 = 1-VV_junc1__w_in3
    VV_junc1__w_out4 = 1-VV_junc1__w_in4
    VV_junc1__Qin1 = VV_junc1__w_in1*VV_junc1__vj1
    VV_junc1__Qin3 = VV_junc1__w_in3*VV_junc1__vj3
    VV_junc1__Qin4 = VV_junc1__w_in4*VV_junc1__vj4
    VV_junc1__Qout1 = VV_junc1__w_out1*-VV_junc1__vj1
    VV_junc1__Qout3 = VV_junc1__w_out3*-VV_junc1__vj3
    VV_junc1__Qout4 = VV_junc1__w_out4*-VV_junc1__vj4
    VV_junc1__Qin_tot = VV_junc1__Qin1+VV_junc1__Qin2+VV_junc1__Qin3+VV_junc1__Qin4
    VV_junc1__Qout_tot = VV_junc1__Qout1+VV_junc1__Qout2+VV_junc1__Qout3+VV_junc1__Qout4
    VV_junc1__v = (VV_junc1__u-VV_junc1__u_d)/VV_junc1__R_VV_junc
    VV_junc1__bc1_is_in = (1 if VV_junc1__Qin1 > VV_junc1__v_threshold else 0)
    VV_junc1__bc3_is_in = (1 if VV_junc1__Qin3 > VV_junc1__v_threshold else 0)
    VV_junc1__bc4_is_in = (1 if VV_junc1__Qin4 > VV_junc1__v_threshold else 0)
    VV_junc1__bc1_is_out = (1 if VV_junc1__Qout1 > VV_junc1__v_threshold else 0)
    VV_junc1__bc3_is_out = (1 if VV_junc1__Qout3 > VV_junc1__v_threshold else 0)
    VV_junc1__bc4_is_out = (1 if VV_junc1__Qout4 > VV_junc1__v_threshold else 0)
    PV1__w_v = 0.5+1/np.pi*np.arctan(PV1__v/PV1__v_scale)
    PV1__H_down_target = PV1__s_v_d*(PV1__H_mean+PV1__gamma_mirror*(PV1__H_mean-PV1__H_up))+(1-PV1__s_v_d)*PV1__H_mean
    PV1__v_pos = PV1__w_v*PV1__v
    PV1__v_neg = (1-PV1__w_v)*-PV1__v
    PV1__H_volume_L = PV1__w_v*PV1__H_L_in+(1-PV1__w_v)*PV1__H_L_out
    PV1__v_mm3_s = PV1__v/PV1__one_mm3
    PV2__w_v = 0.5+1/np.pi*np.arctan(PV2__v/PV2__v_scale)
    PV2__H_down_target = PV2__s_v_d*(PV2__H_mean+PV2__gamma_mirror*(PV2__H_mean-PV2__H_up))+(1-PV2__s_v_d)*PV2__H_mean
    PV2__v_pos = PV2__w_v*PV2__v
    PV2__v_neg = (1-PV2__w_v)*-PV2__v
    PV2__H_volume_L = PV2__w_v*PV2__H_L_in+(1-PV2__w_v)*PV2__H_L_out
    PV2__v_mm3_s = PV2__v/PV2__one_mm3
    V1__H_down_target = V1__s_v*(V1__H_mean+V1__gamma_mirror*(V1__H_mean-V1__H_up))+(1-V1__s_v)*V1__H_mean
    V1__RBC_volume = (PV1__v_d*V1__H_volume_L-V1__v*V1__H_volume_R)/(PV1__v_d+V1__v)
    V2__H_down_target = V2__s_v*(V2__H_mean+V2__gamma_mirror*(V2__H_mean-V2__H_up))+(1-V2__s_v)*V2__H_mean
    V2__RBC_volume = (PV2__v_d*V2__H_volume_L-V2__v*V2__H_volume_R)/(PV2__v_d+V2__v)
    inlet__w_v_d = 0.5+1/np.pi*np.arctan(inlet__v_d/inlet__v_scale)
    inlet__H_up = inlet__w_v_d*inlet__H_L_in+(1-inlet__w_v_d)*inlet__H_R_in
    inlet__s_v_d = np.abs(inlet__v_d)/(np.abs(inlet__v_d)+inlet__v_eps)
    inlet__H_L_out = (1-inlet__w_v_d)*inlet__H_down+inlet__w_v_d*inlet__H_L_in
    inlet__H_R_out = inlet__w_v_d*inlet__H_down+(1-inlet__w_v_d)*inlet__H_R_in
    inlet__v_d_pos = inlet__w_v_d*inlet__v_d
    inlet__v_d_neg = (1-inlet__w_v_d)*-inlet__v_d
    inlet__H_volume_L = inlet__w_v*inlet__H_L_in+(1-inlet__w_v)*inlet__H_L_out
    inlet__H_volume_R = inlet__w_v_d*inlet__H_R_out+(1-inlet__w_v_d)*inlet__H_R_in
    inlet__v_d_mm3_s = inlet__v_d/inlet__one_mm3
    VV_junc1__n_in = VV_junc1__bc1_is_in+VV_junc1__bc2_is_in+VV_junc1__bc3_is_in+VV_junc1__bc4_is_in
    VV_junc1__n_out = VV_junc1__bc1_is_out+VV_junc1__bc2_is_out+VV_junc1__bc3_is_out+VV_junc1__bc4_is_out
    VV_junc1__RBC_in = VV_junc1__Qin1*inlet__H_R_out+VV_junc1__Qin2*VV_junc1__H_to2+VV_junc1__Qin3*PV1__H_L_out+VV_junc1__Qin4*PV2__H_L_out
    VV_junc1__v_mm3_s = VV_junc1__v/VV_junc1__one_mm3
    VV_junc1__junction_type = (1 if VV_junc1__n_in == 1 else (-1 if VV_junc1__n_in >= 2 else 0))
    VV_junc1__is_split = (1 if VV_junc1__junction_type == 1 else 0)
    VV_junc1__is_merge = (1 if VV_junc1__junction_type == -1 else 0)
    VV_junc1__feed1 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin1 >= VV_junc1__Qin2) and (VV_junc1__Qin1 >= VV_junc1__Qin3) and (VV_junc1__Qin1 >= VV_junc1__Qin4) else 0)
    VV_junc1__feed2 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin2 > VV_junc1__Qin1) and (VV_junc1__Qin2 >= VV_junc1__Qin3) and (VV_junc1__Qin2 >= VV_junc1__Qin4) else 0)
    VV_junc1__feed3 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin3 > VV_junc1__Qin1) and (VV_junc1__Qin3 > VV_junc1__Qin2) and (VV_junc1__Qin3 >= VV_junc1__Qin4) else 0)
    VV_junc1__feed4 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin4 > VV_junc1__Qin1) and (VV_junc1__Qin4 > VV_junc1__Qin2) and (VV_junc1__Qin4 > VV_junc1__Qin3) else 0)
    VV_junc1__alpha1 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc1_is_out == 1) and (VV_junc1__Qout1 >= VV_junc1__Qout2) and (VV_junc1__Qout1 >= VV_junc1__Qout3) and (VV_junc1__Qout1 >= VV_junc1__Qout4) else 0)
    VV_junc1__alpha2 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc2_is_out == 1) and (VV_junc1__Qout2 > VV_junc1__Qout1) and (VV_junc1__Qout2 >= VV_junc1__Qout3) and (VV_junc1__Qout2 >= VV_junc1__Qout4) else 0)
    VV_junc1__alpha3 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc3_is_out == 1) and (VV_junc1__Qout3 > VV_junc1__Qout1) and (VV_junc1__Qout3 > VV_junc1__Qout2) and (VV_junc1__Qout3 >= VV_junc1__Qout4) else 0)
    VV_junc1__alpha4 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc4_is_out == 1) and (VV_junc1__Qout4 > VV_junc1__Qout1) and (VV_junc1__Qout4 > VV_junc1__Qout2) and (VV_junc1__Qout4 > VV_junc1__Qout3) else 0)
    VV_junc1__Qout1_rem = (0 if VV_junc1__alpha1 == 1 else VV_junc1__Qout1)
    VV_junc1__Qout2_rem = (0 if VV_junc1__alpha2 == 1 else VV_junc1__Qout2)
    VV_junc1__Qout3_rem = (0 if VV_junc1__alpha3 == 1 else VV_junc1__Qout3)
    VV_junc1__Qout4_rem = (0 if VV_junc1__alpha4 == 1 else VV_junc1__Qout4)
    VV_junc1__beta1 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc1_is_out == 1) and (VV_junc1__alpha1 == 0) and (VV_junc1__Qout1_rem >= VV_junc1__Qout2_rem) and (VV_junc1__Qout1_rem >= VV_junc1__Qout3_rem) and (VV_junc1__Qout1_rem >= VV_junc1__Qout4_rem) else 0)
    VV_junc1__beta2 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc2_is_out == 1) and (VV_junc1__alpha2 == 0) and (VV_junc1__Qout2_rem > VV_junc1__Qout1_rem) and (VV_junc1__Qout2_rem >= VV_junc1__Qout3_rem) and (VV_junc1__Qout2_rem >= VV_junc1__Qout4_rem) else 0)
    VV_junc1__beta3 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc3_is_out == 1) and (VV_junc1__alpha3 == 0) and (VV_junc1__Qout3_rem > VV_junc1__Qout1_rem) and (VV_junc1__Qout3_rem > VV_junc1__Qout2_rem) and (VV_junc1__Qout3_rem >= VV_junc1__Qout4_rem) else 0)
    VV_junc1__beta4 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc4_is_out == 1) and (VV_junc1__alpha4 == 0) and (VV_junc1__Qout4_rem > VV_junc1__Qout1_rem) and (VV_junc1__Qout4_rem > VV_junc1__Qout2_rem) and (VV_junc1__Qout4_rem > VV_junc1__Qout3_rem) else 0)
    VV_junc1__D_F = (VV_junc1__D1 if VV_junc1__feed1 == 1 else (VV_junc1__D2 if VV_junc1__feed2 == 1 else (VV_junc1__D3 if VV_junc1__feed3 == 1 else (VV_junc1__D4 if VV_junc1__feed4 == 1 else VV_junc1__D1))))
    VV_junc1__D_alpha = (VV_junc1__D1 if VV_junc1__alpha1 == 1 else (VV_junc1__D2 if VV_junc1__alpha2 == 1 else (VV_junc1__D3 if VV_junc1__alpha3 == 1 else (VV_junc1__D4 if VV_junc1__alpha4 == 1 else VV_junc1__D3))))
    VV_junc1__D_beta = (VV_junc1__D1 if VV_junc1__beta1 == 1 else (VV_junc1__D2 if VV_junc1__beta2 == 1 else (VV_junc1__D3 if VV_junc1__beta3 == 1 else (VV_junc1__D4 if VV_junc1__beta4 == 1 else VV_junc1__D4))))
    VV_junc1__v_alpha = (VV_junc1__Qout1 if VV_junc1__alpha1 == 1 else (VV_junc1__Qout2 if VV_junc1__alpha2 == 1 else (VV_junc1__Qout3 if VV_junc1__alpha3 == 1 else (VV_junc1__Qout4 if VV_junc1__alpha4 == 1 else 0))))
    VV_junc1__v_beta = (VV_junc1__Qout1 if VV_junc1__beta1 == 1 else (VV_junc1__Qout2 if VV_junc1__beta2 == 1 else (VV_junc1__Qout3 if VV_junc1__beta3 == 1 else (VV_junc1__Qout4 if VV_junc1__beta4 == 1 else 0))))
    PV1__RBC_volume = (PV1__v*PV1__H_volume_L-PV1__v_d*PV1__H_volume_R)/(PV1__v+PV1__v_d)
    PV2__RBC_volume = (PV2__v*PV2__H_volume_L-PV2__v_d*PV2__H_volume_R)/(PV2__v+PV2__v_d)
    inlet__H_down_target = inlet__s_v_d*(inlet__H_mean+inlet__gamma_mirror*(inlet__H_mean-inlet__H_up))+(1-inlet__s_v_d)*inlet__H_mean
    inlet__RBC_volume = (inlet__v*inlet__H_volume_L-inlet__v_d*inlet__H_volume_R)/(inlet__v+inlet__v_d)
    VV_junc1__FQB_alpha = (VV_junc1__v_alpha+VV_junc1__div_0)/(VV_junc1__v_alpha+VV_junc1__v_beta+2*VV_junc1__div_0)
    VV_junc1__B = 1+6.98*(1-VV_junc1__H_mean)/(VV_junc1__D_F*1e6)
    VV_junc1__A = -6.96*np.log(VV_junc1__D_alpha*1e6/(VV_junc1__D_beta*1e6))/(VV_junc1__D_F*1e6)
    VV_junc1__X_0 = 0.4/(VV_junc1__D_F*1e6)
    VV_junc1__y_raw = (VV_junc1__FQB_alpha-VV_junc1__X_0)/(1-2*VV_junc1__X_0+VV_junc1__div_0)
    VV_junc1__y = min(max(VV_junc1__y_raw, VV_junc1__div_0y), 1-VV_junc1__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc1__FQE_alpha = 1/(1+np.exp(-(VV_junc1__A+VV_junc1__B*VV_junc1__ph)))
    VV_junc1__H_VV_out_alpha = VV_junc1__H_mean*VV_junc1__FQE_alpha/(VV_junc1__FQB_alpha+VV_junc1__div_0)
    VV_junc1__H_VV_out_beta = VV_junc1__H_mean*(1-VV_junc1__FQE_alpha)/(1-VV_junc1__FQB_alpha+VV_junc1__div_0)
    VV_junc1__H_split1 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha1 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta1 == 1 else inlet__H_R_out))
    VV_junc1__H_split2 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha2 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta2 == 1 else VV_junc1__H_to2))
    VV_junc1__H_split3 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha3 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta3 == 1 else PV1__H_L_out))
    VV_junc1__H_split4 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha4 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta4 == 1 else PV2__H_L_out))
    VV_junc1__H_daughter1 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split1 if VV_junc1__is_split == 1 else inlet__H_R_out))
    VV_junc1__H_daughter2 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split2 if VV_junc1__is_split == 1 else VV_junc1__H_to2))
    VV_junc1__H_daughter3 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split3 if VV_junc1__is_split == 1 else PV1__H_L_out))
    VV_junc1__H_daughter4 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split4 if VV_junc1__is_split == 1 else PV2__H_L_out))
    VV_junc1__H_from1_target = (VV_junc1__H_daughter1 if VV_junc1__bc1_is_out == 1 else inlet__H_R_out)
    VV_junc1__H_from2_target = (VV_junc1__H_daughter2 if VV_junc1__bc2_is_out == 1 else VV_junc1__H_to2)
    VV_junc1__H_from3_target = (VV_junc1__H_daughter3 if VV_junc1__bc3_is_out == 1 else PV1__H_L_out)
    VV_junc1__H_from4_target = (VV_junc1__H_daughter4 if VV_junc1__bc4_is_out == 1 else PV2__H_L_out)
    VV_junc1__H_from1 = VV_junc1__w_out1*VV_junc1__H_from1_target
    VV_junc1__H_from2 = VV_junc1__w_out2*VV_junc1__H_from2_target
    VV_junc1__H_from3 = VV_junc1__w_out3*VV_junc1__H_from3_target
    VV_junc1__H_from4 = VV_junc1__w_out4*VV_junc1__H_from4_target
    VV_junc1__RBC_out = VV_junc1__Qout1*VV_junc1__H_from1+VV_junc1__Qout2*VV_junc1__H_from2+VV_junc1__Qout3*VV_junc1__H_from3+VV_junc1__Qout4*VV_junc1__H_from4

    return locals()

def _iter_residual(H_means, t, y):
    """F(H_means) = num - H_mean*denom  +  ZERO_FLOW_REG anchor.
    
    The anchor term is  gate * denom * (H_global_L - H_mean), where
    gate = v_eps_reg**2 / (flow**2 + v_eps_reg**2). When flow >> v_eps_reg,
    gate -> 0 and the anchor vanishes (true fixed point undisturbed). When
    flow is near zero, gate -> 1 and the anchor pulls H_mean toward
    H_global_L, breaking the degeneracy of 0 = 0.
    
    Disable by setting ZERO_FLOW_REG_EPS = 0 below.
    """
    loc = _eval_algebraics(t, y, H_means)
    res = np.empty(len(H_means))
    _num = eval('(PV1__v*PV1__H_volume_L-PV1__v_d*PV1__H_volume_R)', globals(), loc)
    _den = eval('(PV1__q)*(PV1__v+PV1__v_d)', globals(), loc)
    res[0] = _num - H_means[0] * _den
    _flow = abs(loc.get('PV1__v', 0.0)) + abs(loc.get('PV1__v_d', 0.0))
    _gate = ZERO_FLOW_REG_EPS**2 / (_flow**2 + ZERO_FLOW_REG_EPS**2 + 1e-300)
    res[0] += _gate * ZERO_FLOW_ANCHOR_STRENGTH * (PV1__H_global_L - H_means[0])
    _num = eval('(PV2__v*PV2__H_volume_L-PV2__v_d*PV2__H_volume_R)', globals(), loc)
    _den = eval('(PV2__q)*(PV2__v+PV2__v_d)', globals(), loc)
    res[1] = _num - H_means[1] * _den
    _flow = abs(loc.get('PV2__v', 0.0)) + abs(loc.get('PV2__v_d', 0.0))
    _gate = ZERO_FLOW_REG_EPS**2 / (_flow**2 + ZERO_FLOW_REG_EPS**2 + 1e-300)
    res[1] += _gate * ZERO_FLOW_ANCHOR_STRENGTH * (PV2__H_global_L - H_means[1])
    _num = eval('(PV1__v_d*V1__H_volume_L-V1__v*V1__H_volume_R)', globals(), loc)
    _den = eval('(V1__q)*(PV1__v_d+V1__v)', globals(), loc)
    res[2] = _num - H_means[2] * _den
    _flow = abs(loc.get('V1__v', 0.0)) + abs(loc.get('V1__v_d', 0.0))
    _gate = ZERO_FLOW_REG_EPS**2 / (_flow**2 + ZERO_FLOW_REG_EPS**2 + 1e-300)
    res[2] += _gate * ZERO_FLOW_ANCHOR_STRENGTH * (V1__H_global_L - H_means[2])
    _num = eval('(PV2__v_d*V2__H_volume_L-V2__v*V2__H_volume_R)', globals(), loc)
    _den = eval('(V2__q)*(PV2__v_d+V2__v)', globals(), loc)
    res[3] = _num - H_means[3] * _den
    _flow = abs(loc.get('V2__v', 0.0)) + abs(loc.get('V2__v_d', 0.0))
    _gate = ZERO_FLOW_REG_EPS**2 / (_flow**2 + ZERO_FLOW_REG_EPS**2 + 1e-300)
    res[3] += _gate * ZERO_FLOW_ANCHOR_STRENGTH * (V2__H_global_L - H_means[3])
    _num = eval('(inlet__v*inlet__H_volume_L-inlet__v_d*inlet__H_volume_R)', globals(), loc)
    _den = eval('(inlet__q)*(inlet__v+inlet__v_d)', globals(), loc)
    res[4] = _num - H_means[4] * _den
    _flow = abs(loc.get('inlet__v', 0.0)) + abs(loc.get('inlet__v_d', 0.0))
    _gate = ZERO_FLOW_REG_EPS**2 / (_flow**2 + ZERO_FLOW_REG_EPS**2 + 1e-300)
    res[4] += _gate * ZERO_FLOW_ANCHOR_STRENGTH * (inlet__H_global_L - H_means[4])
    return res

from scipy.optimize import least_squares

RES_ACCEPT_TOL = 1e-10  # accept any x with ||F(x)|| below this
H_MIN, H_MAX = 0.0, 1.0  # physical bounds on hematocrit
_H_LO = np.full(len(iter_unknown_names), H_MIN)
_H_HI = np.full(len(iter_unknown_names), H_MAX)

def _solve_iterative(t, y):
    """Solve the iterative H_mean fixed point at (t, y). Returns H_means array.
    
    Uses scipy.optimize.least_squares with bounds [0, 1] on every H_mean.
    This handles the common case where Jacobian-probing perturbations by
    the ODE integrator produce states where the algebraic balance has no
    exact root in [0, 1] (the bounded minimizer returns the best feasible
    answer rather than wandering to spurious unbounded roots like H=1.0).
    
    Warm-starts from _iter_last_solution for speed.
    """
    x0 = np.clip(_iter_last_solution[0], H_MIN, H_MAX)
    # Levenberg-Marquardt under bounds via trust region reflective.
    sol = least_squares(_iter_residual, x0, args=(t, y),
                        bounds=(_H_LO, _H_HI),
                        method="trf", xtol=1e-12, ftol=1e-12,
                        max_nfev=50)
    if sol.success or np.linalg.norm(sol.fun) < RES_ACCEPT_TOL:
        _iter_last_solution[0] = sol.x.copy()
        return sol.x
    # Retry from CSV initial guess if warm start struggled.
    sol2 = least_squares(_iter_residual, _iter_initial_guess, args=(t, y),
                         bounds=(_H_LO, _H_HI),
                         method="trf", xtol=1e-12, ftol=1e-12,
                         max_nfev=50)
    best = sol2 if np.linalg.norm(sol2.fun) < np.linalg.norm(sol.fun) else sol
    if not hasattr(_solve_iterative, "_warned"):
        _solve_iterative._warned = set()
    key = round(t, 6)
    if key not in _solve_iterative._warned:
        import sys as _sys
        print(f"[iter] t={t:.4g}: bounded LS imperfect, ||res||={np.linalg.norm(best.fun):.2e}",
              file=_sys.stderr)
        _solve_iterative._warned.add(key)
    _iter_last_solution[0] = best.x.copy()
    return best.x

# State names
state_names = [
    'inlet__H_link_R',
    'inlet__H_link_L',
    'inlet__H_down',
    'inlet__q_C',
    'VV_junc1__RBC_volume',
    'VV_junc1__q_C',
    'VV_junc1__q_C_d',
    'PV1__H_link_R',
    'PV1__H_link_L',
    'PV1__H_down',
    'PV1__q_C',
    'PV2__H_link_R',
    'PV2__H_link_L',
    'PV2__H_down',
    'PV2__q_C',
    'V1__H_link_R',
    'V1__H_link_L',
    'V1__H_down',
    'V1__q_C',
    'V2__H_link_R',
    'V2__H_link_L',
    'V2__H_down',
    'V2__q_C',
]

# Initial conditions
y0 = np.array([
    -1.9984014885135946e-16,
    0.45,
    0.45000000994816686,
    3.3326531138933488e-18,
    5.0899981016906383e-17,
    2.7729721054424635e-18,
    2.7701283341496695e-18,
    0.45066594907900703,
    0.45005807512155366,
    0.45066415426369355,
    1.6625090353096748e-19,
    0.4506660141504298,
    0.45005807347727317,
    0.4506642190463343,
    1.662509035300436e-19,
    0.45,
    0.45066506738583584,
    0.4499375638693855,
    2.7707624254559425e-18,
    0.45,
    0.4506651323127141,
    0.4499375579201643,
    2.770762425425145e-18,
])

def ode_rhs(t, y):
    """RHS for solve_ivp. Solves iterative H_mean, then evaluates ODEs."""
    # IT-4: resolve the algebraic cycle before evaluating ODE RHSes.
    H_means = _solve_iterative(t, y)
    loc = _eval_algebraics(t, y, H_means)

    dydt = np.zeros(len(y))
    dydt[0] = eval('(VV_junc1__H_from1-inlet__H_link_R)/inlet__tau_link', globals(), loc)
    dydt[1] = eval('(inlet__H_R_out_LHS-inlet__H_link_L)/inlet__tau_link', globals(), loc)
    dydt[2] = eval('(inlet__H_down_target-inlet__H_down)/inlet__tau_H_down', globals(), loc)
    dydt[3] = eval('inlet__v-inlet__v_d', globals(), loc)
    dydt[4] = eval('VV_junc1__RBC_in-VV_junc1__RBC_out', globals(), loc)
    dydt[5] = eval('inlet__v_d+VV_junc1__vbc2-VV_junc1__v', globals(), loc)
    dydt[6] = eval('VV_junc1__v-PV1__v-PV2__v', globals(), loc)
    dydt[7] = eval('(V1__H_L_out-PV1__H_link_R)/PV1__tau_link', globals(), loc)
    dydt[8] = eval('(VV_junc1__H_from3-PV1__H_link_L)/PV1__tau_link', globals(), loc)
    dydt[9] = eval('(PV1__H_down_target-PV1__H_down)/PV1__tau_H_down', globals(), loc)
    dydt[10] = eval('PV1__v-PV1__v_d', globals(), loc)
    dydt[11] = eval('(V2__H_L_out-PV2__H_link_R)/PV2__tau_link', globals(), loc)
    dydt[12] = eval('(VV_junc1__H_from4-PV2__H_link_L)/PV2__tau_link', globals(), loc)
    dydt[13] = eval('(PV2__H_down_target-PV2__H_down)/PV2__tau_H_down', globals(), loc)
    dydt[14] = eval('PV2__v-PV2__v_d', globals(), loc)
    dydt[15] = eval('(V1__H_L_out_RHS-V1__H_link_R)/V1__tau_link', globals(), loc)
    dydt[16] = eval('(PV1__H_R_out-V1__H_link_L)/V1__tau_link', globals(), loc)
    dydt[17] = eval('(V1__H_down_target-V1__H_down)/V1__tau_H_down', globals(), loc)
    dydt[18] = eval('PV1__v_d-V1__v', globals(), loc)
    dydt[19] = eval('(V2__H_L_out_RHS-V2__H_link_R)/V2__tau_link', globals(), loc)
    dydt[20] = eval('(PV2__H_R_out-V2__H_link_L)/V2__tau_link', globals(), loc)
    dydt[21] = eval('(V2__H_down_target-V2__H_down)/V2__tau_H_down', globals(), loc)
    dydt[22] = eval('PV2__v_d-V2__v', globals(), loc)
    return dydt

def compute_algebraics(t, y):
    """Compute all algebraic variables at a given time point."""
    H_means = _solve_iterative(t, y)
    loc = _eval_algebraics(t, y, H_means)
    # Return just the algebraic & iterative names (strip function-local noise).
    out = {}
    out["inlet__H_L_in"] = loc["inlet__H_L_in"]
    out["inlet__H_R_in"] = loc["inlet__H_R_in"]
    out["inlet__q_us"] = loc["inlet__q_us"]
    out["inlet__q"] = loc["inlet__q"]
    out["inlet__C"] = loc["inlet__C"]
    out["inlet__Z"] = loc["inlet__Z"]
    out["inlet__mu_45"] = loc["inlet__mu_45"]
    out["inlet__hem_dep_u_rel"] = loc["inlet__hem_dep_u_rel"]
    out["inlet__u"] = loc["inlet__u"]
    out["VV_junc1__vj2"] = loc["VV_junc1__vj2"]
    out["VV_junc1__D1"] = loc["VV_junc1__D1"]
    out["VV_junc1__D2"] = loc["VV_junc1__D2"]
    out["VV_junc1__D3"] = loc["VV_junc1__D3"]
    out["VV_junc1__D4"] = loc["VV_junc1__D4"]
    out["VV_junc1__w_in2"] = loc["VV_junc1__w_in2"]
    out["VV_junc1__w_out2"] = loc["VV_junc1__w_out2"]
    out["VV_junc1__Qin2"] = loc["VV_junc1__Qin2"]
    out["VV_junc1__Qout2"] = loc["VV_junc1__Qout2"]
    out["VV_junc1__q_us"] = loc["VV_junc1__q_us"]
    out["VV_junc1__q"] = loc["VV_junc1__q"]
    out["VV_junc1__bc2_is_in"] = loc["VV_junc1__bc2_is_in"]
    out["VV_junc1__bc2_is_out"] = loc["VV_junc1__bc2_is_out"]
    out["VV_junc1__C_max12"] = loc["VV_junc1__C_max12"]
    out["PV1__R_constriction"] = loc["PV1__R_constriction"]
    out["PV1__H_L_in"] = loc["PV1__H_L_in"]
    out["PV1__H_R_in"] = loc["PV1__H_R_in"]
    out["PV1__q_us"] = loc["PV1__q_us"]
    out["PV1__q"] = loc["PV1__q"]
    out["PV1__C"] = loc["PV1__C"]
    out["PV1__Z"] = loc["PV1__Z"]
    out["PV1__mu_45"] = loc["PV1__mu_45"]
    out["PV1__hem_dep_u_rel"] = loc["PV1__hem_dep_u_rel"]
    out["PV1__u"] = loc["PV1__u"]
    out["PV2__R_constriction"] = loc["PV2__R_constriction"]
    out["PV2__H_L_in"] = loc["PV2__H_L_in"]
    out["PV2__H_R_in"] = loc["PV2__H_R_in"]
    out["PV2__q_us"] = loc["PV2__q_us"]
    out["PV2__q"] = loc["PV2__q"]
    out["PV2__C"] = loc["PV2__C"]
    out["PV2__Z"] = loc["PV2__Z"]
    out["PV2__mu_45"] = loc["PV2__mu_45"]
    out["PV2__hem_dep_u_rel"] = loc["PV2__hem_dep_u_rel"]
    out["PV2__u"] = loc["PV2__u"]
    out["V1__H_L_in"] = loc["V1__H_L_in"]
    out["V1__H_R_in"] = loc["V1__H_R_in"]
    out["V1__q_us"] = loc["V1__q_us"]
    out["V1__q"] = loc["V1__q"]
    out["V1__C"] = loc["V1__C"]
    out["V1__Z"] = loc["V1__Z"]
    out["V1__mu_45"] = loc["V1__mu_45"]
    out["V1__hem_dep_u_rel"] = loc["V1__hem_dep_u_rel"]
    out["V1__u"] = loc["V1__u"]
    out["V2__H_L_in"] = loc["V2__H_L_in"]
    out["V2__H_R_in"] = loc["V2__H_R_in"]
    out["V2__q_us"] = loc["V2__q_us"]
    out["V2__q"] = loc["V2__q"]
    out["V2__C"] = loc["V2__C"]
    out["V2__Z"] = loc["V2__Z"]
    out["V2__mu_45"] = loc["V2__mu_45"]
    out["V2__hem_dep_u_rel"] = loc["V2__hem_dep_u_rel"]
    out["V2__u"] = loc["V2__u"]
    out["inlet__RBC_volume_init"] = loc["inlet__RBC_volume_init"]
    out["inlet__mu"] = loc["inlet__mu"]
    out["inlet__R"] = loc["inlet__R"]
    out["inlet__v"] = loc["inlet__v"]
    out["inlet__u_mmHg"] = loc["inlet__u_mmHg"]
    out["VV_junc1__RBC_volume_init"] = loc["VV_junc1__RBC_volume_init"]
    out["VV_junc1__H_mean"] = loc["VV_junc1__H_mean"]
    out["VV_junc1__C_max123"] = loc["VV_junc1__C_max123"]
    out["VV_junc1__C"] = loc["VV_junc1__C"]
    out["PV1__RBC_volume_init"] = loc["PV1__RBC_volume_init"]
    out["PV1__mu"] = loc["PV1__mu"]
    out["PV1__R"] = loc["PV1__R"]
    out["PV1__u_mmHg"] = loc["PV1__u_mmHg"]
    out["PV1__v_d"] = loc["PV1__v_d"]
    out["PV2__RBC_volume_init"] = loc["PV2__RBC_volume_init"]
    out["PV2__mu"] = loc["PV2__mu"]
    out["PV2__R"] = loc["PV2__R"]
    out["PV2__u_mmHg"] = loc["PV2__u_mmHg"]
    out["PV2__v_d"] = loc["PV2__v_d"]
    out["V1__RBC_volume_init"] = loc["V1__RBC_volume_init"]
    out["V1__mu"] = loc["V1__mu"]
    out["V1__R"] = loc["V1__R"]
    out["V1__v"] = loc["V1__v"]
    out["V1__u_mmHg"] = loc["V1__u_mmHg"]
    out["V2__RBC_volume_init"] = loc["V2__RBC_volume_init"]
    out["V2__mu"] = loc["V2__mu"]
    out["V2__R"] = loc["V2__R"]
    out["V2__v"] = loc["V2__v"]
    out["V2__u_mmHg"] = loc["V2__u_mmHg"]
    out["inlet__w_v"] = loc["inlet__w_v"]
    out["inlet__v_pos"] = loc["inlet__v_pos"]
    out["inlet__v_neg"] = loc["inlet__v_neg"]
    out["inlet__v_mm3_s"] = loc["inlet__v_mm3_s"]
    out["VV_junc1__u"] = loc["VV_junc1__u"]
    out["VV_junc1__u_mmHg"] = loc["VV_junc1__u_mmHg"]
    out["VV_junc1__u_d"] = loc["VV_junc1__u_d"]
    out["VV_junc1__u_d_mmHg"] = loc["VV_junc1__u_d_mmHg"]
    out["PV1__w_v_d"] = loc["PV1__w_v_d"]
    out["PV1__H_up"] = loc["PV1__H_up"]
    out["PV1__s_v_d"] = loc["PV1__s_v_d"]
    out["PV1__H_L_out"] = loc["PV1__H_L_out"]
    out["PV1__H_R_out"] = loc["PV1__H_R_out"]
    out["PV1__v_d_pos"] = loc["PV1__v_d_pos"]
    out["PV1__v_d_neg"] = loc["PV1__v_d_neg"]
    out["PV1__H_volume_R"] = loc["PV1__H_volume_R"]
    out["PV1__v"] = loc["PV1__v"]
    out["PV1__v_d_mm3_s"] = loc["PV1__v_d_mm3_s"]
    out["PV2__w_v_d"] = loc["PV2__w_v_d"]
    out["PV2__H_up"] = loc["PV2__H_up"]
    out["PV2__s_v_d"] = loc["PV2__s_v_d"]
    out["PV2__H_L_out"] = loc["PV2__H_L_out"]
    out["PV2__H_R_out"] = loc["PV2__H_R_out"]
    out["PV2__v_d_pos"] = loc["PV2__v_d_pos"]
    out["PV2__v_d_neg"] = loc["PV2__v_d_neg"]
    out["PV2__H_volume_R"] = loc["PV2__H_volume_R"]
    out["PV2__v"] = loc["PV2__v"]
    out["PV2__v_d_mm3_s"] = loc["PV2__v_d_mm3_s"]
    out["V1__w_v"] = loc["V1__w_v"]
    out["V1__H_up"] = loc["V1__H_up"]
    out["V1__s_v"] = loc["V1__s_v"]
    out["V1__H_L_out"] = loc["V1__H_L_out"]
    out["V1__H_R_out"] = loc["V1__H_R_out"]
    out["V1__v_pos"] = loc["V1__v_pos"]
    out["V1__v_neg"] = loc["V1__v_neg"]
    out["V1__H_volume_L"] = loc["V1__H_volume_L"]
    out["V1__H_volume_R"] = loc["V1__H_volume_R"]
    out["V1__v_mm3_s"] = loc["V1__v_mm3_s"]
    out["V2__w_v"] = loc["V2__w_v"]
    out["V2__H_up"] = loc["V2__H_up"]
    out["V2__s_v"] = loc["V2__s_v"]
    out["V2__H_L_out"] = loc["V2__H_L_out"]
    out["V2__H_R_out"] = loc["V2__H_R_out"]
    out["V2__v_pos"] = loc["V2__v_pos"]
    out["V2__v_neg"] = loc["V2__v_neg"]
    out["V2__H_volume_L"] = loc["V2__H_volume_L"]
    out["V2__H_volume_R"] = loc["V2__H_volume_R"]
    out["V2__v_mm3_s"] = loc["V2__v_mm3_s"]
    out["inlet__v_d"] = loc["inlet__v_d"]
    out["VV_junc1__vj1"] = loc["VV_junc1__vj1"]
    out["VV_junc1__vj3"] = loc["VV_junc1__vj3"]
    out["VV_junc1__vj4"] = loc["VV_junc1__vj4"]
    out["VV_junc1__w_in1"] = loc["VV_junc1__w_in1"]
    out["VV_junc1__w_in3"] = loc["VV_junc1__w_in3"]
    out["VV_junc1__w_in4"] = loc["VV_junc1__w_in4"]
    out["VV_junc1__w_out1"] = loc["VV_junc1__w_out1"]
    out["VV_junc1__w_out3"] = loc["VV_junc1__w_out3"]
    out["VV_junc1__w_out4"] = loc["VV_junc1__w_out4"]
    out["VV_junc1__Qin1"] = loc["VV_junc1__Qin1"]
    out["VV_junc1__Qin3"] = loc["VV_junc1__Qin3"]
    out["VV_junc1__Qin4"] = loc["VV_junc1__Qin4"]
    out["VV_junc1__Qout1"] = loc["VV_junc1__Qout1"]
    out["VV_junc1__Qout3"] = loc["VV_junc1__Qout3"]
    out["VV_junc1__Qout4"] = loc["VV_junc1__Qout4"]
    out["VV_junc1__Qin_tot"] = loc["VV_junc1__Qin_tot"]
    out["VV_junc1__Qout_tot"] = loc["VV_junc1__Qout_tot"]
    out["VV_junc1__v"] = loc["VV_junc1__v"]
    out["VV_junc1__bc1_is_in"] = loc["VV_junc1__bc1_is_in"]
    out["VV_junc1__bc3_is_in"] = loc["VV_junc1__bc3_is_in"]
    out["VV_junc1__bc4_is_in"] = loc["VV_junc1__bc4_is_in"]
    out["VV_junc1__bc1_is_out"] = loc["VV_junc1__bc1_is_out"]
    out["VV_junc1__bc3_is_out"] = loc["VV_junc1__bc3_is_out"]
    out["VV_junc1__bc4_is_out"] = loc["VV_junc1__bc4_is_out"]
    out["PV1__w_v"] = loc["PV1__w_v"]
    out["PV1__H_down_target"] = loc["PV1__H_down_target"]
    out["PV1__v_pos"] = loc["PV1__v_pos"]
    out["PV1__v_neg"] = loc["PV1__v_neg"]
    out["PV1__H_volume_L"] = loc["PV1__H_volume_L"]
    out["PV1__v_mm3_s"] = loc["PV1__v_mm3_s"]
    out["PV2__w_v"] = loc["PV2__w_v"]
    out["PV2__H_down_target"] = loc["PV2__H_down_target"]
    out["PV2__v_pos"] = loc["PV2__v_pos"]
    out["PV2__v_neg"] = loc["PV2__v_neg"]
    out["PV2__H_volume_L"] = loc["PV2__H_volume_L"]
    out["PV2__v_mm3_s"] = loc["PV2__v_mm3_s"]
    out["V1__H_down_target"] = loc["V1__H_down_target"]
    out["V1__RBC_volume"] = loc["V1__RBC_volume"]
    out["V2__H_down_target"] = loc["V2__H_down_target"]
    out["V2__RBC_volume"] = loc["V2__RBC_volume"]
    out["inlet__w_v_d"] = loc["inlet__w_v_d"]
    out["inlet__H_up"] = loc["inlet__H_up"]
    out["inlet__s_v_d"] = loc["inlet__s_v_d"]
    out["inlet__H_L_out"] = loc["inlet__H_L_out"]
    out["inlet__H_R_out"] = loc["inlet__H_R_out"]
    out["inlet__v_d_pos"] = loc["inlet__v_d_pos"]
    out["inlet__v_d_neg"] = loc["inlet__v_d_neg"]
    out["inlet__H_volume_L"] = loc["inlet__H_volume_L"]
    out["inlet__H_volume_R"] = loc["inlet__H_volume_R"]
    out["inlet__v_d_mm3_s"] = loc["inlet__v_d_mm3_s"]
    out["VV_junc1__n_in"] = loc["VV_junc1__n_in"]
    out["VV_junc1__n_out"] = loc["VV_junc1__n_out"]
    out["VV_junc1__RBC_in"] = loc["VV_junc1__RBC_in"]
    out["VV_junc1__v_mm3_s"] = loc["VV_junc1__v_mm3_s"]
    out["VV_junc1__junction_type"] = loc["VV_junc1__junction_type"]
    out["VV_junc1__is_split"] = loc["VV_junc1__is_split"]
    out["VV_junc1__is_merge"] = loc["VV_junc1__is_merge"]
    out["VV_junc1__feed1"] = loc["VV_junc1__feed1"]
    out["VV_junc1__feed2"] = loc["VV_junc1__feed2"]
    out["VV_junc1__feed3"] = loc["VV_junc1__feed3"]
    out["VV_junc1__feed4"] = loc["VV_junc1__feed4"]
    out["VV_junc1__alpha1"] = loc["VV_junc1__alpha1"]
    out["VV_junc1__alpha2"] = loc["VV_junc1__alpha2"]
    out["VV_junc1__alpha3"] = loc["VV_junc1__alpha3"]
    out["VV_junc1__alpha4"] = loc["VV_junc1__alpha4"]
    out["VV_junc1__Qout1_rem"] = loc["VV_junc1__Qout1_rem"]
    out["VV_junc1__Qout2_rem"] = loc["VV_junc1__Qout2_rem"]
    out["VV_junc1__Qout3_rem"] = loc["VV_junc1__Qout3_rem"]
    out["VV_junc1__Qout4_rem"] = loc["VV_junc1__Qout4_rem"]
    out["VV_junc1__beta1"] = loc["VV_junc1__beta1"]
    out["VV_junc1__beta2"] = loc["VV_junc1__beta2"]
    out["VV_junc1__beta3"] = loc["VV_junc1__beta3"]
    out["VV_junc1__beta4"] = loc["VV_junc1__beta4"]
    out["VV_junc1__D_F"] = loc["VV_junc1__D_F"]
    out["VV_junc1__D_alpha"] = loc["VV_junc1__D_alpha"]
    out["VV_junc1__D_beta"] = loc["VV_junc1__D_beta"]
    out["VV_junc1__v_alpha"] = loc["VV_junc1__v_alpha"]
    out["VV_junc1__v_beta"] = loc["VV_junc1__v_beta"]
    out["PV1__RBC_volume"] = loc["PV1__RBC_volume"]
    out["PV2__RBC_volume"] = loc["PV2__RBC_volume"]
    out["inlet__H_down_target"] = loc["inlet__H_down_target"]
    out["inlet__RBC_volume"] = loc["inlet__RBC_volume"]
    out["VV_junc1__FQB_alpha"] = loc["VV_junc1__FQB_alpha"]
    out["VV_junc1__B"] = loc["VV_junc1__B"]
    out["VV_junc1__A"] = loc["VV_junc1__A"]
    out["VV_junc1__X_0"] = loc["VV_junc1__X_0"]
    out["VV_junc1__y_raw"] = loc["VV_junc1__y_raw"]
    out["VV_junc1__y"] = loc["VV_junc1__y"]
    out["VV_junc1__ph"] = loc["VV_junc1__ph"]
    out["VV_junc1__FQE_alpha"] = loc["VV_junc1__FQE_alpha"]
    out["VV_junc1__H_VV_out_alpha"] = loc["VV_junc1__H_VV_out_alpha"]
    out["VV_junc1__H_VV_out_beta"] = loc["VV_junc1__H_VV_out_beta"]
    out["VV_junc1__H_split1"] = loc["VV_junc1__H_split1"]
    out["VV_junc1__H_split2"] = loc["VV_junc1__H_split2"]
    out["VV_junc1__H_split3"] = loc["VV_junc1__H_split3"]
    out["VV_junc1__H_split4"] = loc["VV_junc1__H_split4"]
    out["VV_junc1__H_daughter1"] = loc["VV_junc1__H_daughter1"]
    out["VV_junc1__H_daughter2"] = loc["VV_junc1__H_daughter2"]
    out["VV_junc1__H_daughter3"] = loc["VV_junc1__H_daughter3"]
    out["VV_junc1__H_daughter4"] = loc["VV_junc1__H_daughter4"]
    out["VV_junc1__H_from1_target"] = loc["VV_junc1__H_from1_target"]
    out["VV_junc1__H_from2_target"] = loc["VV_junc1__H_from2_target"]
    out["VV_junc1__H_from3_target"] = loc["VV_junc1__H_from3_target"]
    out["VV_junc1__H_from4_target"] = loc["VV_junc1__H_from4_target"]
    out["VV_junc1__H_from1"] = loc["VV_junc1__H_from1"]
    out["VV_junc1__H_from2"] = loc["VV_junc1__H_from2"]
    out["VV_junc1__H_from3"] = loc["VV_junc1__H_from3"]
    out["VV_junc1__H_from4"] = loc["VV_junc1__H_from4"]
    out["VV_junc1__RBC_out"] = loc["VV_junc1__RBC_out"]
    out["PV1__H_mean"] = loc["PV1__H_mean"]
    out["PV2__H_mean"] = loc["PV2__H_mean"]
    out["V1__H_mean"] = loc["V1__H_mean"]
    out["V2__H_mean"] = loc["V2__H_mean"]
    out["inlet__H_mean"] = loc["inlet__H_mean"]
    return out
