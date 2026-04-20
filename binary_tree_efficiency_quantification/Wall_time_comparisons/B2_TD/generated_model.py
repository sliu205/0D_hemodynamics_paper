"""Generated model"""
import numpy as np
from scipy.integrate import solve_ivp
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
PV1__R_constriction_final = 0.0
PV1__gamma_mirror = 0.1
PV1__l = 0.000015
PV1__mu_plasma = 0.001
PV1__one_mm3 = 1e-09
PV1__q_C_init = 0.0
PV1__r = 6e-06
PV1__t0 = 500.0
PV1__tau_H_down = 0.001
PV1__tau_H_mean = 0.001
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
PV2__tau_link = 0.001
PV2__tau_sig = 1.0
PV2__u_ext = 133.0
PV2__v_eps = 1e-30
PV2__v_scale = 1e-50
PV3__H_global_L = 0.45
PV3__H_global_R = 0.45
PV3__R_constriction_base = 0.0
PV3__R_constriction_final = 0.0
PV3__gamma_mirror = 0.1
PV3__l = 0.000015
PV3__mu_plasma = 0.001
PV3__one_mm3 = 1e-09
PV3__q_C_init = 0.0
PV3__r = 5.5e-06
PV3__t0 = 500.0
PV3__tau_H_down = 0.001
PV3__tau_H_mean = 0.001
PV3__tau_link = 0.001
PV3__tau_sig = 1.0
PV3__u_ext = 133.0
PV3__v_eps = 1e-30
PV3__v_scale = 1e-50
PV4__H_global_L = 0.45
PV4__H_global_R = 0.45
PV4__R_constriction_base = 0.0
PV4__R_constriction_final = 0.0
PV4__gamma_mirror = 0.1
PV4__l = 0.000015
PV4__mu_plasma = 0.001
PV4__one_mm3 = 1e-09
PV4__q_C_init = 0.0
PV4__r = 5.5e-06
PV4__t0 = 500.0
PV4__tau_H_down = 0.001
PV4__tau_H_mean = 0.001
PV4__tau_link = 0.001
PV4__tau_sig = 1.0
PV4__u_ext = 133.0
PV4__v_eps = 1e-30
PV4__v_scale = 1e-50
PV5__H_global_L = 0.45
PV5__H_global_R = 0.45
PV5__R_constriction_base = 0.0
PV5__R_constriction_final = 1e21
PV5__gamma_mirror = 0.1
PV5__l = 0.000015
PV5__mu_plasma = 0.001
PV5__one_mm3 = 1e-09
PV5__q_C_init = 0.0
PV5__r = 5.5e-06
PV5__t0 = 500.0
PV5__tau_H_down = 0.001
PV5__tau_H_mean = 0.001
PV5__tau_link = 0.001
PV5__tau_sig = 1.0
PV5__u_ext = 133.0
PV5__v_eps = 1e-30
PV5__v_scale = 1e-50
PV6__H_global_L = 0.45
PV6__H_global_R = 0.45
PV6__R_constriction_base = 0.0
PV6__R_constriction_final = 0.0
PV6__gamma_mirror = 0.1
PV6__l = 0.000015
PV6__mu_plasma = 0.001
PV6__one_mm3 = 1e-09
PV6__q_C_init = 0.0
PV6__r = 5.5e-06
PV6__t0 = 500.0
PV6__tau_H_down = 0.001
PV6__tau_H_mean = 0.001
PV6__tau_link = 0.001
PV6__tau_sig = 1.0
PV6__u_ext = 133.0
PV6__v_eps = 1e-30
PV6__v_scale = 1e-50
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
V1__tau_link = 0.001
V1__u_ext = 133.0
V1__v_eps = 1e-30
V1__v_scale = 1e-50
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
V2__tau_link = 0.001
V2__u_ext = 133.0
V2__v_eps = 1e-30
V2__v_scale = 1e-50
V3__H_L_out_RHS = 0.45
V3__H_global_L = 0.45
V3__H_global_R = 0.45
V3__gamma_mirror = 0.1
V3__l = 0.0002
V3__mu_plasma = 0.001
V3__one_mm3 = 1e-09
V3__q_C_init = 0.0
V3__r = 5e-06
V3__tau_H_down = 0.001
V3__tau_H_mean = 0.001
V3__tau_link = 0.001
V3__u_ext = 133.0
V3__u_out = 6599.44
V3__v_eps = 1e-30
V3__v_scale = 1e-50
V4__H_L_out_RHS = 0.45
V4__H_global_L = 0.45
V4__H_global_R = 0.45
V4__gamma_mirror = 0.1
V4__l = 0.0002
V4__mu_plasma = 0.001
V4__one_mm3 = 1e-09
V4__q_C_init = 0.0
V4__r = 5e-06
V4__tau_H_down = 0.001
V4__tau_H_mean = 0.001
V4__tau_link = 0.001
V4__u_ext = 133.0
V4__u_out = 6599.44
V4__v_eps = 1e-30
V4__v_scale = 1e-50
V5__H_L_out_RHS = 0.45
V5__H_global_L = 0.45
V5__H_global_R = 0.45
V5__gamma_mirror = 0.1
V5__l = 0.0002
V5__mu_plasma = 0.001
V5__one_mm3 = 1e-09
V5__q_C_init = 0.0
V5__r = 5e-06
V5__tau_H_down = 0.001
V5__tau_H_mean = 0.001
V5__tau_link = 0.001
V5__u_ext = 133.0
V5__u_out = 6599.44
V5__v_eps = 1e-30
V5__v_scale = 1e-50
V6__H_L_out_RHS = 0.45
V6__H_global_L = 0.45
V6__H_global_R = 0.45
V6__gamma_mirror = 0.1
V6__l = 0.0002
V6__mu_plasma = 0.001
V6__one_mm3 = 1e-09
V6__q_C_init = 0.0
V6__r = 5e-06
V6__tau_H_down = 0.001
V6__tau_H_mean = 0.001
V6__tau_link = 0.001
V6__u_ext = 133.0
V6__u_out = 6599.44
V6__v_eps = 1e-30
V6__v_scale = 1e-50
VV_junc1__C_conn2 = 8.51e-22
VV_junc1__H_global_L = 0.45
VV_junc1__H_global_R = 0.45
VV_junc1__H_to2 = 0.0
VV_junc1__R_VV_junc = 1000000000000000.0
VV_junc1__div_0 = 1e-25
VV_junc1__div_0y = 1e-08
VV_junc1__k = 1000.0
VV_junc1__l = 0.000001
VV_junc1__mu_plasma = 0.001
VV_junc1__one_mm3 = 1e-09
VV_junc1__q_C_init = 0.0
VV_junc1__r = 6e-06
VV_junc1__r_bc2 = 0.0
VV_junc1__u_ext = 133.0
VV_junc1__v_scale = 1e-50
VV_junc1__v_threshold = 1e-18
VV_junc1__vbc2 = 0.0
VV_junc2__C_conn2 = 8.51e-22
VV_junc2__H_global_L = 0.45
VV_junc2__H_global_R = 0.45
VV_junc2__H_to2 = 0.0
VV_junc2__R_VV_junc = 1000000000000000.0
VV_junc2__div_0 = 1e-25
VV_junc2__div_0y = 1e-08
VV_junc2__k = 1000.0
VV_junc2__l = 0.000001
VV_junc2__mu_plasma = 0.001
VV_junc2__one_mm3 = 1e-09
VV_junc2__q_C_init = 0.0
VV_junc2__r = 5.5e-06
VV_junc2__r_bc2 = 0.0
VV_junc2__u_ext = 133.0
VV_junc2__v_scale = 1e-50
VV_junc2__v_threshold = 1e-18
VV_junc2__vbc2 = 0.0
VV_junc3__C_conn2 = 8.51e-22
VV_junc3__H_global_L = 0.45
VV_junc3__H_global_R = 0.45
VV_junc3__H_to2 = 0.0
VV_junc3__R_VV_junc = 1000000000000000.0
VV_junc3__div_0 = 1e-25
VV_junc3__div_0y = 1e-08
VV_junc3__k = 1000.0
VV_junc3__l = 0.000001
VV_junc3__mu_plasma = 0.001
VV_junc3__one_mm3 = 1e-09
VV_junc3__q_C_init = 0.0
VV_junc3__r = 5.5e-06
VV_junc3__r_bc2 = 0.0
VV_junc3__u_ext = 133.0
VV_junc3__v_scale = 1e-50
VV_junc3__v_threshold = 1e-18
VV_junc3__vbc2 = 0.0
global__H_global_L = 0.45
global__H_global_R = 0.45
global__R_VV_junc = 1000000000000000.0
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
inlet__tau_link = 0.001
inlet__u_ext = 133.0
inlet__u_in = 6666.1
inlet__v_eps = 1e-30
inlet__v_scale = 1e-50

# State names
state_names = [
    'inlet__H_link_R',
    'inlet__H_link_L',
    'inlet__H_down',
    'inlet__RBC_volume',
    'inlet__q_C',
    'VV_junc1__RBC_volume',
    'VV_junc1__q_C',
    'VV_junc1__q_C_d',
    'PV1__H_link_R',
    'PV1__H_link_L',
    'PV1__H_down',
    'PV1__RBC_volume',
    'PV1__q_C',
    'PV2__H_link_R',
    'PV2__H_link_L',
    'PV2__H_down',
    'PV2__RBC_volume',
    'PV2__q_C',
    'V1__H_link_R',
    'V1__H_link_L',
    'V1__H_down',
    'V1__RBC_volume',
    'V1__q_C',
    'V2__H_link_R',
    'V2__H_link_L',
    'V2__H_down',
    'V2__RBC_volume',
    'V2__q_C',
    'VV_junc2__RBC_volume',
    'VV_junc2__q_C',
    'VV_junc2__q_C_d',
    'PV3__H_link_R',
    'PV3__H_link_L',
    'PV3__H_down',
    'PV3__RBC_volume',
    'PV3__q_C',
    'PV4__H_link_R',
    'PV4__H_link_L',
    'PV4__H_down',
    'PV4__RBC_volume',
    'PV4__q_C',
    'V3__H_link_R',
    'V3__H_link_L',
    'V3__H_down',
    'V3__RBC_volume',
    'V3__q_C',
    'V4__H_link_R',
    'V4__H_link_L',
    'V4__H_down',
    'V4__RBC_volume',
    'V4__q_C',
    'VV_junc3__RBC_volume',
    'VV_junc3__q_C',
    'VV_junc3__q_C_d',
    'PV5__H_link_R',
    'PV5__H_link_L',
    'PV5__H_down',
    'PV5__RBC_volume',
    'PV5__q_C',
    'PV6__H_link_R',
    'PV6__H_link_L',
    'PV6__H_down',
    'PV6__RBC_volume',
    'PV6__q_C',
    'V5__H_link_R',
    'V5__H_link_L',
    'V5__H_down',
    'V5__RBC_volume',
    'V5__q_C',
    'V6__H_link_R',
    'V6__H_link_L',
    'V6__H_down',
    'V6__RBC_volume',
    'V6__q_C',
]

# Initial conditions
y0 = np.array([
    0.16554533503524738,
    0.45,
    0.449999999005151,
    1.5269638949389773e-14,
    3.3304324226885967e-18,
    5.3129684920468425e-17,
    2.769272006972341e-18,
    2.764894767188325e-18,
    0.4499606157540015,
    0.4629569747141832,
    0.4494584270115804,
    7.635217082420872e-16,
    1.6593367921428482e-19,
    0.44996062342925724,
    0.4629455867731889,
    0.44945881826960615,
    7.635216829641695e-16,
    1.659336758114149e-19,
    0.16877102489882437,
    0.4498340144397035,
    0.4500038278206632,
    1.0692476758257886e-14,
    2.7654351283631478e-18,
    0.16877102492005452,
    0.4498340821456568,
    0.45000382704704384,
    1.0692476758081617e-14,
    2.7654351290434194e-18,
    4.5091178832564876e-17,
    2.7580055576032245e-18,
    2.7558170606915004e-18,
    0.45001259668412064,
    0.4616498943276744,
    0.4497385713914187,
    6.415547157656964e-16,
    1.653905004600027e-19,
    0.4500125966841176,
    0.46164989432758646,
    0.449738571391391,
    6.415547157656421e-16,
    1.6539050046000347e-19,
    0.45,
    0.44998862167485104,
    0.44999874157007946,
    7.069575833985925e-15,
    2.2051360761119726e-18,
    0.45,
    0.4499886216748402,
    0.44999874157007974,
    7.069575833985925e-15,
    2.2051360761119726e-18,
    4.509154804731749e-17,
    2.758005575811102e-18,
    2.7558170844178176e-18,
    0.4500126003633829,
    0.46165405002189513,
    0.44973848705000746,
    6.415546237201658e-16,
    1.6539042269352074e-19,
    0.45001259208841843,
    0.4616484826165441,
    0.4497385592079264,
    6.415546197280901e-16,
    1.6539042412527714e-19,
    0.45,
    0.4499886239845553,
    0.4499987412086233,
    7.069575834279371e-15,
    2.205136094950624e-18,
    0.45,
    0.4499886068011827,
    0.4499987420357697,
    7.069575834252539e-15,
    2.2051360949497965e-18,
])

def ode_rhs(t, y):
    # Unpack state
    inlet__H_link_R = y[0]
    inlet__H_link_L = y[1]
    inlet__H_down = y[2]
    inlet__RBC_volume = y[3]
    inlet__q_C = y[4]
    VV_junc1__RBC_volume = y[5]
    VV_junc1__q_C = y[6]
    VV_junc1__q_C_d = y[7]
    PV1__H_link_R = y[8]
    PV1__H_link_L = y[9]
    PV1__H_down = y[10]
    PV1__RBC_volume = y[11]
    PV1__q_C = y[12]
    PV2__H_link_R = y[13]
    PV2__H_link_L = y[14]
    PV2__H_down = y[15]
    PV2__RBC_volume = y[16]
    PV2__q_C = y[17]
    V1__H_link_R = y[18]
    V1__H_link_L = y[19]
    V1__H_down = y[20]
    V1__RBC_volume = y[21]
    V1__q_C = y[22]
    V2__H_link_R = y[23]
    V2__H_link_L = y[24]
    V2__H_down = y[25]
    V2__RBC_volume = y[26]
    V2__q_C = y[27]
    VV_junc2__RBC_volume = y[28]
    VV_junc2__q_C = y[29]
    VV_junc2__q_C_d = y[30]
    PV3__H_link_R = y[31]
    PV3__H_link_L = y[32]
    PV3__H_down = y[33]
    PV3__RBC_volume = y[34]
    PV3__q_C = y[35]
    PV4__H_link_R = y[36]
    PV4__H_link_L = y[37]
    PV4__H_down = y[38]
    PV4__RBC_volume = y[39]
    PV4__q_C = y[40]
    V3__H_link_R = y[41]
    V3__H_link_L = y[42]
    V3__H_down = y[43]
    V3__RBC_volume = y[44]
    V3__q_C = y[45]
    V4__H_link_R = y[46]
    V4__H_link_L = y[47]
    V4__H_down = y[48]
    V4__RBC_volume = y[49]
    V4__q_C = y[50]
    VV_junc3__RBC_volume = y[51]
    VV_junc3__q_C = y[52]
    VV_junc3__q_C_d = y[53]
    PV5__H_link_R = y[54]
    PV5__H_link_L = y[55]
    PV5__H_down = y[56]
    PV5__RBC_volume = y[57]
    PV5__q_C = y[58]
    PV6__H_link_R = y[59]
    PV6__H_link_L = y[60]
    PV6__H_down = y[61]
    PV6__RBC_volume = y[62]
    PV6__q_C = y[63]
    V5__H_link_R = y[64]
    V5__H_link_L = y[65]
    V5__H_down = y[66]
    V5__RBC_volume = y[67]
    V5__q_C = y[68]
    V6__H_link_R = y[69]
    V6__H_link_L = y[70]
    V6__H_down = y[71]
    V6__RBC_volume = y[72]
    V6__q_C = y[73]

    # Time variable
    environment__time = t

    # Algebraic equations
    inlet__H_L_in = inlet__H_link_L
    inlet__H_R_in = inlet__H_link_R
    inlet__q_us = np.pi*np.square(inlet__r)*inlet__l
    inlet__q = inlet__q_us+inlet__q_C
    inlet__C = np.pi*np.square(8.5e-9)*inlet__l/133.322
    inlet__Z = (0.8+np.exp(-0.075*2*inlet__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*inlet__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*inlet__r*1e6, 12))
    inlet__mu_45 = 6*np.exp(-0.085*2*inlet__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*inlet__r*1e6, 0.645))
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
    PV1__u = PV1__q_C/PV1__C+PV1__u_ext
    PV2__R_constriction = PV2__R_constriction_base+(PV2__R_constriction_final-PV2__R_constriction_base)/(1+np.exp(-(environment__time-PV2__t0)/PV2__tau_sig))
    PV2__H_L_in = PV2__H_link_L
    PV2__H_R_in = PV2__H_link_R
    PV2__q_us = np.pi*np.square(PV2__r)*PV2__l
    PV2__q = PV2__q_us+PV2__q_C
    PV2__C = np.pi*np.square(8.5e-9)*PV2__l/133.322
    PV2__Z = (0.8+np.exp(-0.075*2*PV2__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV2__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV2__r*1e6, 12))
    PV2__mu_45 = 6*np.exp(-0.085*2*PV2__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV2__r*1e6, 0.645))
    PV2__u = PV2__q_C/PV2__C+PV2__u_ext
    V1__H_L_in = V1__H_link_L
    V1__H_R_in = V1__H_link_R
    V1__q_us = np.pi*np.square(V1__r)*V1__l
    V1__q = V1__q_us+V1__q_C
    V1__C = np.pi*np.square(8.5e-9)*V1__l/133.322
    V1__Z = (0.8+np.exp(-0.075*2*V1__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V1__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V1__r*1e6, 12))
    V1__mu_45 = 6*np.exp(-0.085*2*V1__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V1__r*1e6, 0.645))
    V1__u = V1__q_C/V1__C+V1__u_ext
    V2__H_L_in = V2__H_link_L
    V2__H_R_in = V2__H_link_R
    V2__q_us = np.pi*np.square(V2__r)*V2__l
    V2__q = V2__q_us+V2__q_C
    V2__C = np.pi*np.square(8.5e-9)*V2__l/133.322
    V2__Z = (0.8+np.exp(-0.075*2*V2__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V2__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V2__r*1e6, 12))
    V2__mu_45 = 6*np.exp(-0.085*2*V2__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V2__r*1e6, 0.645))
    V2__u = V2__q_C/V2__C+V2__u_ext
    VV_junc2__vj2 = VV_junc2__vbc2
    VV_junc2__D1 = 2*V1__r
    VV_junc2__D2 = 2*VV_junc2__r_bc2
    VV_junc2__D3 = 2*PV3__r
    VV_junc2__D4 = 2*PV4__r
    VV_junc2__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc2__vj2/VV_junc2__v_scale)
    VV_junc2__w_out2 = 1-VV_junc2__w_in2
    VV_junc2__Qin2 = VV_junc2__w_in2*VV_junc2__vj2
    VV_junc2__Qout2 = VV_junc2__w_out2*-VV_junc2__vj2
    VV_junc2__q_us = np.pi*np.square(VV_junc2__r)*VV_junc2__l
    VV_junc2__q = VV_junc2__q_us+VV_junc2__q_C+VV_junc2__q_C_d
    VV_junc2__bc2_is_in = (1 if VV_junc2__Qin2 > VV_junc2__v_threshold else 0)
    VV_junc2__bc2_is_out = (1 if VV_junc2__Qout2 > VV_junc2__v_threshold else 0)
    VV_junc2__C_max12 = (V1__C if V1__C > VV_junc2__C_conn2 else (VV_junc2__C_conn2 if V1__C <= VV_junc2__C_conn2 else 0.0))
    PV3__R_constriction = PV3__R_constriction_base+(PV3__R_constriction_final-PV3__R_constriction_base)/(1+np.exp(-(environment__time-PV3__t0)/PV3__tau_sig))
    PV3__H_L_in = PV3__H_link_L
    PV3__H_R_in = PV3__H_link_R
    PV3__q_us = np.pi*np.square(PV3__r)*PV3__l
    PV3__q = PV3__q_us+PV3__q_C
    PV3__C = np.pi*np.square(8.5e-9)*PV3__l/133.322
    PV3__Z = (0.8+np.exp(-0.075*2*PV3__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV3__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV3__r*1e6, 12))
    PV3__mu_45 = 6*np.exp(-0.085*2*PV3__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV3__r*1e6, 0.645))
    PV3__u = PV3__q_C/PV3__C+PV3__u_ext
    PV4__R_constriction = PV4__R_constriction_base+(PV4__R_constriction_final-PV4__R_constriction_base)/(1+np.exp(-(environment__time-PV4__t0)/PV4__tau_sig))
    PV4__H_L_in = PV4__H_link_L
    PV4__H_R_in = PV4__H_link_R
    PV4__q_us = np.pi*np.square(PV4__r)*PV4__l
    PV4__q = PV4__q_us+PV4__q_C
    PV4__C = np.pi*np.square(8.5e-9)*PV4__l/133.322
    PV4__Z = (0.8+np.exp(-0.075*2*PV4__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV4__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV4__r*1e6, 12))
    PV4__mu_45 = 6*np.exp(-0.085*2*PV4__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV4__r*1e6, 0.645))
    PV4__u = PV4__q_C/PV4__C+PV4__u_ext
    V3__H_L_in = V3__H_link_L
    V3__H_R_in = V3__H_link_R
    V3__q_us = np.pi*np.square(V3__r)*V3__l
    V3__q = V3__q_us+V3__q_C
    V3__C = np.pi*np.square(8.5e-9)*V3__l/133.322
    V3__Z = (0.8+np.exp(-0.075*2*V3__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V3__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V3__r*1e6, 12))
    V3__mu_45 = 6*np.exp(-0.085*2*V3__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V3__r*1e6, 0.645))
    V3__u = V3__q_C/V3__C+V3__u_ext
    V4__H_L_in = V4__H_link_L
    V4__H_R_in = V4__H_link_R
    V4__q_us = np.pi*np.square(V4__r)*V4__l
    V4__q = V4__q_us+V4__q_C
    V4__C = np.pi*np.square(8.5e-9)*V4__l/133.322
    V4__Z = (0.8+np.exp(-0.075*2*V4__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V4__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V4__r*1e6, 12))
    V4__mu_45 = 6*np.exp(-0.085*2*V4__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V4__r*1e6, 0.645))
    V4__u = V4__q_C/V4__C+V4__u_ext
    VV_junc3__vj2 = VV_junc3__vbc2
    VV_junc3__D1 = 2*V2__r
    VV_junc3__D2 = 2*VV_junc3__r_bc2
    VV_junc3__D3 = 2*PV5__r
    VV_junc3__D4 = 2*PV6__r
    VV_junc3__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc3__vj2/VV_junc3__v_scale)
    VV_junc3__w_out2 = 1-VV_junc3__w_in2
    VV_junc3__Qin2 = VV_junc3__w_in2*VV_junc3__vj2
    VV_junc3__Qout2 = VV_junc3__w_out2*-VV_junc3__vj2
    VV_junc3__q_us = np.pi*np.square(VV_junc3__r)*VV_junc3__l
    VV_junc3__q = VV_junc3__q_us+VV_junc3__q_C+VV_junc3__q_C_d
    VV_junc3__bc2_is_in = (1 if VV_junc3__Qin2 > VV_junc3__v_threshold else 0)
    VV_junc3__bc2_is_out = (1 if VV_junc3__Qout2 > VV_junc3__v_threshold else 0)
    VV_junc3__C_max12 = (V2__C if V2__C > VV_junc3__C_conn2 else (VV_junc3__C_conn2 if V2__C <= VV_junc3__C_conn2 else 0.0))
    PV5__R_constriction = PV5__R_constriction_base+(PV5__R_constriction_final-PV5__R_constriction_base)/(1+np.exp(-(environment__time-PV5__t0)/PV5__tau_sig))
    PV5__H_L_in = PV5__H_link_L
    PV5__H_R_in = PV5__H_link_R
    PV5__q_us = np.pi*np.square(PV5__r)*PV5__l
    PV5__q = PV5__q_us+PV5__q_C
    PV5__C = np.pi*np.square(8.5e-9)*PV5__l/133.322
    PV5__Z = (0.8+np.exp(-0.075*2*PV5__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV5__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV5__r*1e6, 12))
    PV5__mu_45 = 6*np.exp(-0.085*2*PV5__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV5__r*1e6, 0.645))
    PV5__u = PV5__q_C/PV5__C+PV5__u_ext
    PV6__R_constriction = PV6__R_constriction_base+(PV6__R_constriction_final-PV6__R_constriction_base)/(1+np.exp(-(environment__time-PV6__t0)/PV6__tau_sig))
    PV6__H_L_in = PV6__H_link_L
    PV6__H_R_in = PV6__H_link_R
    PV6__q_us = np.pi*np.square(PV6__r)*PV6__l
    PV6__q = PV6__q_us+PV6__q_C
    PV6__C = np.pi*np.square(8.5e-9)*PV6__l/133.322
    PV6__Z = (0.8+np.exp(-0.075*2*PV6__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV6__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV6__r*1e6, 12))
    PV6__mu_45 = 6*np.exp(-0.085*2*PV6__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV6__r*1e6, 0.645))
    PV6__u = PV6__q_C/PV6__C+PV6__u_ext
    V5__H_L_in = V5__H_link_L
    V5__H_R_in = V5__H_link_R
    V5__q_us = np.pi*np.square(V5__r)*V5__l
    V5__q = V5__q_us+V5__q_C
    V5__C = np.pi*np.square(8.5e-9)*V5__l/133.322
    V5__Z = (0.8+np.exp(-0.075*2*V5__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V5__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V5__r*1e6, 12))
    V5__mu_45 = 6*np.exp(-0.085*2*V5__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V5__r*1e6, 0.645))
    V5__u = V5__q_C/V5__C+V5__u_ext
    V6__H_L_in = V6__H_link_L
    V6__H_R_in = V6__H_link_R
    V6__q_us = np.pi*np.square(V6__r)*V6__l
    V6__q = V6__q_us+V6__q_C
    V6__C = np.pi*np.square(8.5e-9)*V6__l/133.322
    V6__Z = (0.8+np.exp(-0.075*2*V6__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V6__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V6__r*1e6, 12))
    V6__mu_45 = 6*np.exp(-0.085*2*V6__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V6__r*1e6, 0.645))
    V6__u = V6__q_C/V6__C+V6__u_ext
    inlet__RBC_volume_init = inlet__H_global_L*inlet__q_us
    inlet__H_mean = inlet__RBC_volume/inlet__q
    inlet__hem_dep_u_rel = 1+(inlet__mu_45-1)*(safe_power(1-inlet__H_mean, inlet__Z)-1)/(safe_power(1-inlet__H_global_L, inlet__Z)-1)*np.square(2*inlet__r*1e6/(2*inlet__r*1e6-1.1))
    inlet__u_mmHg = inlet__u/133.322
    VV_junc1__RBC_volume_init = VV_junc1__H_global_L*VV_junc1__q_us
    VV_junc1__H_mean = VV_junc1__RBC_volume/(VV_junc1__q_us+VV_junc1__div_0)
    VV_junc1__C_max123 = (VV_junc1__C_max12 if VV_junc1__C_max12 > PV1__C else (PV1__C if VV_junc1__C_max12 <= PV1__C else 0.0))
    VV_junc1__C = (VV_junc1__C_max123 if VV_junc1__C_max123 > PV2__C else (PV2__C if VV_junc1__C_max123 <= PV2__C else 0.0))
    PV1__RBC_volume_init = PV1__H_global_L*PV1__q_us
    PV1__H_mean = PV1__RBC_volume/PV1__q
    PV1__hem_dep_u_rel = 1+(PV1__mu_45-1)*(safe_power(1-PV1__H_mean, PV1__Z)-1)/(safe_power(1-PV1__H_global_L, PV1__Z)-1)*np.square(2*PV1__r*1e6/(2*PV1__r*1e6-1.1))
    PV1__u_mmHg = PV1__u/133.322
    PV2__RBC_volume_init = PV2__H_global_L*PV2__q_us
    PV2__H_mean = PV2__RBC_volume/PV2__q
    PV2__hem_dep_u_rel = 1+(PV2__mu_45-1)*(safe_power(1-PV2__H_mean, PV2__Z)-1)/(safe_power(1-PV2__H_global_L, PV2__Z)-1)*np.square(2*PV2__r*1e6/(2*PV2__r*1e6-1.1))
    PV2__u_mmHg = PV2__u/133.322
    V1__RBC_volume_init = V1__H_global_L*V1__q_us
    V1__H_mean = V1__RBC_volume/V1__q
    V1__hem_dep_u_rel = 1+(V1__mu_45-1)*(safe_power(1-V1__H_mean, V1__Z)-1)/(safe_power(1-V1__H_global_L, V1__Z)-1)*np.square(2*V1__r*1e6/(2*V1__r*1e6-1.1))
    V1__u_mmHg = V1__u/133.322
    V2__RBC_volume_init = V2__H_global_L*V2__q_us
    V2__H_mean = V2__RBC_volume/V2__q
    V2__hem_dep_u_rel = 1+(V2__mu_45-1)*(safe_power(1-V2__H_mean, V2__Z)-1)/(safe_power(1-V2__H_global_L, V2__Z)-1)*np.square(2*V2__r*1e6/(2*V2__r*1e6-1.1))
    V2__u_mmHg = V2__u/133.322
    VV_junc2__RBC_volume_init = VV_junc2__H_global_L*VV_junc2__q_us
    VV_junc2__H_mean = VV_junc2__RBC_volume/(VV_junc2__q_us+VV_junc2__div_0)
    VV_junc2__C_max123 = (VV_junc2__C_max12 if VV_junc2__C_max12 > PV3__C else (PV3__C if VV_junc2__C_max12 <= PV3__C else 0.0))
    VV_junc2__C = (VV_junc2__C_max123 if VV_junc2__C_max123 > PV4__C else (PV4__C if VV_junc2__C_max123 <= PV4__C else 0.0))
    PV3__RBC_volume_init = PV3__H_global_L*PV3__q_us
    PV3__H_mean = PV3__RBC_volume/PV3__q
    PV3__hem_dep_u_rel = 1+(PV3__mu_45-1)*(safe_power(1-PV3__H_mean, PV3__Z)-1)/(safe_power(1-PV3__H_global_L, PV3__Z)-1)*np.square(2*PV3__r*1e6/(2*PV3__r*1e6-1.1))
    PV3__u_mmHg = PV3__u/133.322
    PV4__RBC_volume_init = PV4__H_global_L*PV4__q_us
    PV4__H_mean = PV4__RBC_volume/PV4__q
    PV4__hem_dep_u_rel = 1+(PV4__mu_45-1)*(safe_power(1-PV4__H_mean, PV4__Z)-1)/(safe_power(1-PV4__H_global_L, PV4__Z)-1)*np.square(2*PV4__r*1e6/(2*PV4__r*1e6-1.1))
    PV4__u_mmHg = PV4__u/133.322
    V3__RBC_volume_init = V3__H_global_L*V3__q_us
    V3__H_mean = V3__RBC_volume/V3__q
    V3__hem_dep_u_rel = 1+(V3__mu_45-1)*(safe_power(1-V3__H_mean, V3__Z)-1)/(safe_power(1-V3__H_global_L, V3__Z)-1)*np.square(2*V3__r*1e6/(2*V3__r*1e6-1.1))
    V3__u_mmHg = V3__u/133.322
    V4__RBC_volume_init = V4__H_global_L*V4__q_us
    V4__H_mean = V4__RBC_volume/V4__q
    V4__hem_dep_u_rel = 1+(V4__mu_45-1)*(safe_power(1-V4__H_mean, V4__Z)-1)/(safe_power(1-V4__H_global_L, V4__Z)-1)*np.square(2*V4__r*1e6/(2*V4__r*1e6-1.1))
    V4__u_mmHg = V4__u/133.322
    VV_junc3__RBC_volume_init = VV_junc3__H_global_L*VV_junc3__q_us
    VV_junc3__H_mean = VV_junc3__RBC_volume/(VV_junc3__q_us+VV_junc3__div_0)
    VV_junc3__C_max123 = (VV_junc3__C_max12 if VV_junc3__C_max12 > PV5__C else (PV5__C if VV_junc3__C_max12 <= PV5__C else 0.0))
    VV_junc3__C = (VV_junc3__C_max123 if VV_junc3__C_max123 > PV6__C else (PV6__C if VV_junc3__C_max123 <= PV6__C else 0.0))
    PV5__RBC_volume_init = PV5__H_global_L*PV5__q_us
    PV5__H_mean = PV5__RBC_volume/PV5__q
    PV5__hem_dep_u_rel = 1+(PV5__mu_45-1)*(safe_power(1-PV5__H_mean, PV5__Z)-1)/(safe_power(1-PV5__H_global_L, PV5__Z)-1)*np.square(2*PV5__r*1e6/(2*PV5__r*1e6-1.1))
    PV5__u_mmHg = PV5__u/133.322
    PV6__RBC_volume_init = PV6__H_global_L*PV6__q_us
    PV6__H_mean = PV6__RBC_volume/PV6__q
    PV6__hem_dep_u_rel = 1+(PV6__mu_45-1)*(safe_power(1-PV6__H_mean, PV6__Z)-1)/(safe_power(1-PV6__H_global_L, PV6__Z)-1)*np.square(2*PV6__r*1e6/(2*PV6__r*1e6-1.1))
    PV6__u_mmHg = PV6__u/133.322
    V5__RBC_volume_init = V5__H_global_L*V5__q_us
    V5__H_mean = V5__RBC_volume/V5__q
    V5__hem_dep_u_rel = 1+(V5__mu_45-1)*(safe_power(1-V5__H_mean, V5__Z)-1)/(safe_power(1-V5__H_global_L, V5__Z)-1)*np.square(2*V5__r*1e6/(2*V5__r*1e6-1.1))
    V5__u_mmHg = V5__u/133.322
    V6__RBC_volume_init = V6__H_global_L*V6__q_us
    V6__H_mean = V6__RBC_volume/V6__q
    V6__hem_dep_u_rel = 1+(V6__mu_45-1)*(safe_power(1-V6__H_mean, V6__Z)-1)/(safe_power(1-V6__H_global_L, V6__Z)-1)*np.square(2*V6__r*1e6/(2*V6__r*1e6-1.1))
    V6__u_mmHg = V6__u/133.322
    inlet__mu = inlet__hem_dep_u_rel*inlet__mu_plasma
    inlet__R = 8*inlet__mu*inlet__l/(np.pi*safe_power(inlet__r, 4))
    inlet__v = (inlet__u_in-inlet__u)/(inlet__R/2)
    VV_junc1__u = VV_junc1__q_C/(VV_junc1__C/2)+VV_junc1__u_ext
    VV_junc1__u_mmHg = VV_junc1__u/133.322
    VV_junc1__u_d = VV_junc1__q_C_d/(VV_junc1__C/2)+VV_junc1__u_ext
    VV_junc1__u_d_mmHg = VV_junc1__u_d/133.322
    PV1__mu = PV1__hem_dep_u_rel*PV1__mu_plasma
    PV1__R = 8*PV1__mu*PV1__l/(np.pi*safe_power(PV1__r, 4))+PV1__R_constriction
    PV1__v = (VV_junc1__u_d-PV1__u)/(PV1__R/2)
    PV1__v_d = (PV1__u-V1__u)/(PV1__R/2)
    PV2__mu = PV2__hem_dep_u_rel*PV2__mu_plasma
    PV2__R = 8*PV2__mu*PV2__l/(np.pi*safe_power(PV2__r, 4))+PV2__R_constriction
    PV2__v = (VV_junc1__u_d-PV2__u)/(PV2__R/2)
    PV2__v_d = (PV2__u-V2__u)/(PV2__R/2)
    V1__mu = V1__hem_dep_u_rel*V1__mu_plasma
    V1__R = 8*V1__mu*V1__l/(np.pi*safe_power(V1__r, 4))
    V2__mu = V2__hem_dep_u_rel*V2__mu_plasma
    V2__R = 8*V2__mu*V2__l/(np.pi*safe_power(V2__r, 4))
    VV_junc2__u = VV_junc2__q_C/(VV_junc2__C/2)+VV_junc2__u_ext
    VV_junc2__u_mmHg = VV_junc2__u/133.322
    VV_junc2__u_d = VV_junc2__q_C_d/(VV_junc2__C/2)+VV_junc2__u_ext
    VV_junc2__u_d_mmHg = VV_junc2__u_d/133.322
    PV3__mu = PV3__hem_dep_u_rel*PV3__mu_plasma
    PV3__R = 8*PV3__mu*PV3__l/(np.pi*safe_power(PV3__r, 4))+PV3__R_constriction
    PV3__v = (VV_junc2__u_d-PV3__u)/(PV3__R/2)
    PV3__v_d = (PV3__u-V3__u)/(PV3__R/2)
    PV4__mu = PV4__hem_dep_u_rel*PV4__mu_plasma
    PV4__R = 8*PV4__mu*PV4__l/(np.pi*safe_power(PV4__r, 4))+PV4__R_constriction
    PV4__v = (VV_junc2__u_d-PV4__u)/(PV4__R/2)
    PV4__v_d = (PV4__u-V4__u)/(PV4__R/2)
    V3__mu = V3__hem_dep_u_rel*V3__mu_plasma
    V3__R = 8*V3__mu*V3__l/(np.pi*safe_power(V3__r, 4))
    V3__v = (V3__u-V3__u_out)/V3__R
    V4__mu = V4__hem_dep_u_rel*V4__mu_plasma
    V4__R = 8*V4__mu*V4__l/(np.pi*safe_power(V4__r, 4))
    V4__v = (V4__u-V4__u_out)/V4__R
    VV_junc3__u = VV_junc3__q_C/(VV_junc3__C/2)+VV_junc3__u_ext
    VV_junc3__u_mmHg = VV_junc3__u/133.322
    VV_junc3__u_d = VV_junc3__q_C_d/(VV_junc3__C/2)+VV_junc3__u_ext
    VV_junc3__u_d_mmHg = VV_junc3__u_d/133.322
    PV5__mu = PV5__hem_dep_u_rel*PV5__mu_plasma
    PV5__R = 8*PV5__mu*PV5__l/(np.pi*safe_power(PV5__r, 4))+PV5__R_constriction
    PV5__v = (VV_junc3__u_d-PV5__u)/(PV5__R/2)
    PV5__v_d = (PV5__u-V5__u)/(PV5__R/2)
    PV6__mu = PV6__hem_dep_u_rel*PV6__mu_plasma
    PV6__R = 8*PV6__mu*PV6__l/(np.pi*safe_power(PV6__r, 4))+PV6__R_constriction
    PV6__v = (VV_junc3__u_d-PV6__u)/(PV6__R/2)
    PV6__v_d = (PV6__u-V6__u)/(PV6__R/2)
    V5__mu = V5__hem_dep_u_rel*V5__mu_plasma
    V5__R = 8*V5__mu*V5__l/(np.pi*safe_power(V5__r, 4))
    V5__v = (V5__u-V5__u_out)/V5__R
    V6__mu = V6__hem_dep_u_rel*V6__mu_plasma
    V6__R = 8*V6__mu*V6__l/(np.pi*safe_power(V6__r, 4))
    V6__v = (V6__u-V6__u_out)/V6__R
    inlet__w_v = 0.5+1/np.pi*np.arctan(inlet__v/inlet__v_scale)
    inlet__v_pos = inlet__w_v*inlet__v
    inlet__v_neg = (1-inlet__w_v)*-inlet__v
    inlet__v_mm3_s = inlet__v/inlet__one_mm3
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
    PV1__w_v_d = 0.5+1/np.pi*np.arctan(PV1__v_d/PV1__v_scale)
    PV1__H_up = PV1__w_v_d*PV1__H_L_in+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__s_v_d = np.abs(PV1__v_d)/(np.abs(PV1__v_d)+PV1__v_eps)
    PV1__H_L_out = (1-PV1__w_v_d)*PV1__H_down+PV1__w_v_d*PV1__H_L_in
    PV1__H_R_out = PV1__w_v_d*PV1__H_down+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__v_pos = PV1__w_v*PV1__v
    PV1__v_neg = (1-PV1__w_v)*-PV1__v
    PV1__v_d_pos = PV1__w_v_d*PV1__v_d
    PV1__v_d_neg = (1-PV1__w_v_d)*-PV1__v_d
    PV1__H_volume_L = PV1__w_v*PV1__H_L_in+(1-PV1__w_v)*PV1__H_L_out
    PV1__H_volume_R = PV1__w_v_d*PV1__H_R_out+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__v_mm3_s = PV1__v/PV1__one_mm3
    PV1__v_d_mm3_s = PV1__v_d/PV1__one_mm3
    PV2__w_v = 0.5+1/np.pi*np.arctan(PV2__v/PV2__v_scale)
    PV2__w_v_d = 0.5+1/np.pi*np.arctan(PV2__v_d/PV2__v_scale)
    PV2__H_up = PV2__w_v_d*PV2__H_L_in+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__s_v_d = np.abs(PV2__v_d)/(np.abs(PV2__v_d)+PV2__v_eps)
    PV2__H_L_out = (1-PV2__w_v_d)*PV2__H_down+PV2__w_v_d*PV2__H_L_in
    PV2__H_R_out = PV2__w_v_d*PV2__H_down+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__v_pos = PV2__w_v*PV2__v
    PV2__v_neg = (1-PV2__w_v)*-PV2__v
    PV2__v_d_pos = PV2__w_v_d*PV2__v_d
    PV2__v_d_neg = (1-PV2__w_v_d)*-PV2__v_d
    PV2__H_volume_L = PV2__w_v*PV2__H_L_in+(1-PV2__w_v)*PV2__H_L_out
    PV2__H_volume_R = PV2__w_v_d*PV2__H_R_out+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__v_mm3_s = PV2__v/PV2__one_mm3
    PV2__v_d_mm3_s = PV2__v_d/PV2__one_mm3
    V1__v = (V1__u-VV_junc2__u)/V1__R
    V2__v = (V2__u-VV_junc3__u)/V2__R
    VV_junc2__vj1 = V1__v
    VV_junc2__vj3 = -PV3__v
    VV_junc2__vj4 = -PV4__v
    VV_junc2__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc2__vj1/VV_junc2__v_scale)
    VV_junc2__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc2__vj3/VV_junc2__v_scale)
    VV_junc2__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc2__vj4/VV_junc2__v_scale)
    VV_junc2__w_out1 = 1-VV_junc2__w_in1
    VV_junc2__w_out3 = 1-VV_junc2__w_in3
    VV_junc2__w_out4 = 1-VV_junc2__w_in4
    VV_junc2__Qin1 = VV_junc2__w_in1*VV_junc2__vj1
    VV_junc2__Qin3 = VV_junc2__w_in3*VV_junc2__vj3
    VV_junc2__Qin4 = VV_junc2__w_in4*VV_junc2__vj4
    VV_junc2__Qout1 = VV_junc2__w_out1*-VV_junc2__vj1
    VV_junc2__Qout3 = VV_junc2__w_out3*-VV_junc2__vj3
    VV_junc2__Qout4 = VV_junc2__w_out4*-VV_junc2__vj4
    VV_junc2__Qin_tot = VV_junc2__Qin1+VV_junc2__Qin2+VV_junc2__Qin3+VV_junc2__Qin4
    VV_junc2__Qout_tot = VV_junc2__Qout1+VV_junc2__Qout2+VV_junc2__Qout3+VV_junc2__Qout4
    VV_junc2__v = (VV_junc2__u-VV_junc2__u_d)/VV_junc2__R_VV_junc
    VV_junc2__bc1_is_in = (1 if VV_junc2__Qin1 > VV_junc2__v_threshold else 0)
    VV_junc2__bc3_is_in = (1 if VV_junc2__Qin3 > VV_junc2__v_threshold else 0)
    VV_junc2__bc4_is_in = (1 if VV_junc2__Qin4 > VV_junc2__v_threshold else 0)
    VV_junc2__bc1_is_out = (1 if VV_junc2__Qout1 > VV_junc2__v_threshold else 0)
    VV_junc2__bc3_is_out = (1 if VV_junc2__Qout3 > VV_junc2__v_threshold else 0)
    VV_junc2__bc4_is_out = (1 if VV_junc2__Qout4 > VV_junc2__v_threshold else 0)
    PV3__w_v = 0.5+1/np.pi*np.arctan(PV3__v/PV3__v_scale)
    PV3__w_v_d = 0.5+1/np.pi*np.arctan(PV3__v_d/PV3__v_scale)
    PV3__H_up = PV3__w_v_d*PV3__H_L_in+(1-PV3__w_v_d)*PV3__H_R_in
    PV3__s_v_d = np.abs(PV3__v_d)/(np.abs(PV3__v_d)+PV3__v_eps)
    PV3__H_L_out = (1-PV3__w_v_d)*PV3__H_down+PV3__w_v_d*PV3__H_L_in
    PV3__H_R_out = PV3__w_v_d*PV3__H_down+(1-PV3__w_v_d)*PV3__H_R_in
    PV3__v_pos = PV3__w_v*PV3__v
    PV3__v_neg = (1-PV3__w_v)*-PV3__v
    PV3__v_d_pos = PV3__w_v_d*PV3__v_d
    PV3__v_d_neg = (1-PV3__w_v_d)*-PV3__v_d
    PV3__H_volume_L = PV3__w_v*PV3__H_L_in+(1-PV3__w_v)*PV3__H_L_out
    PV3__H_volume_R = PV3__w_v_d*PV3__H_R_out+(1-PV3__w_v_d)*PV3__H_R_in
    PV3__v_mm3_s = PV3__v/PV3__one_mm3
    PV3__v_d_mm3_s = PV3__v_d/PV3__one_mm3
    PV4__w_v = 0.5+1/np.pi*np.arctan(PV4__v/PV4__v_scale)
    PV4__w_v_d = 0.5+1/np.pi*np.arctan(PV4__v_d/PV4__v_scale)
    PV4__H_up = PV4__w_v_d*PV4__H_L_in+(1-PV4__w_v_d)*PV4__H_R_in
    PV4__s_v_d = np.abs(PV4__v_d)/(np.abs(PV4__v_d)+PV4__v_eps)
    PV4__H_L_out = (1-PV4__w_v_d)*PV4__H_down+PV4__w_v_d*PV4__H_L_in
    PV4__H_R_out = PV4__w_v_d*PV4__H_down+(1-PV4__w_v_d)*PV4__H_R_in
    PV4__v_pos = PV4__w_v*PV4__v
    PV4__v_neg = (1-PV4__w_v)*-PV4__v
    PV4__v_d_pos = PV4__w_v_d*PV4__v_d
    PV4__v_d_neg = (1-PV4__w_v_d)*-PV4__v_d
    PV4__H_volume_L = PV4__w_v*PV4__H_L_in+(1-PV4__w_v)*PV4__H_L_out
    PV4__H_volume_R = PV4__w_v_d*PV4__H_R_out+(1-PV4__w_v_d)*PV4__H_R_in
    PV4__v_mm3_s = PV4__v/PV4__one_mm3
    PV4__v_d_mm3_s = PV4__v_d/PV4__one_mm3
    V3__w_v = 0.5+1/np.pi*np.arctan(V3__v/V3__v_scale)
    V3__H_up = V3__w_v*V3__H_L_in+(1-V3__w_v)*V3__H_R_in
    V3__s_v = np.abs(V3__v)/(np.abs(V3__v)+V3__v_eps)
    V3__H_L_out = (1-V3__w_v)*V3__H_down+V3__w_v*V3__H_L_in
    V3__H_R_out = V3__w_v*V3__H_down+(1-V3__w_v)*V3__H_R_in
    V3__v_pos = V3__w_v*V3__v
    V3__v_neg = (1-V3__w_v)*-V3__v
    V3__H_volume_L = V3__w_v*V3__H_L_in+(1-V3__w_v)*V3__H_L_out
    V3__H_volume_R = V3__w_v*V3__H_R_out+(1-V3__w_v)*V3__H_R_in
    V3__v_mm3_s = V3__v/V3__one_mm3
    V4__w_v = 0.5+1/np.pi*np.arctan(V4__v/V4__v_scale)
    V4__H_up = V4__w_v*V4__H_L_in+(1-V4__w_v)*V4__H_R_in
    V4__s_v = np.abs(V4__v)/(np.abs(V4__v)+V4__v_eps)
    V4__H_L_out = (1-V4__w_v)*V4__H_down+V4__w_v*V4__H_L_in
    V4__H_R_out = V4__w_v*V4__H_down+(1-V4__w_v)*V4__H_R_in
    V4__v_pos = V4__w_v*V4__v
    V4__v_neg = (1-V4__w_v)*-V4__v
    V4__H_volume_L = V4__w_v*V4__H_L_in+(1-V4__w_v)*V4__H_L_out
    V4__H_volume_R = V4__w_v*V4__H_R_out+(1-V4__w_v)*V4__H_R_in
    V4__v_mm3_s = V4__v/V4__one_mm3
    VV_junc3__vj1 = V2__v
    VV_junc3__vj3 = -PV5__v
    VV_junc3__vj4 = -PV6__v
    VV_junc3__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc3__vj1/VV_junc3__v_scale)
    VV_junc3__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc3__vj3/VV_junc3__v_scale)
    VV_junc3__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc3__vj4/VV_junc3__v_scale)
    VV_junc3__w_out1 = 1-VV_junc3__w_in1
    VV_junc3__w_out3 = 1-VV_junc3__w_in3
    VV_junc3__w_out4 = 1-VV_junc3__w_in4
    VV_junc3__Qin1 = VV_junc3__w_in1*VV_junc3__vj1
    VV_junc3__Qin3 = VV_junc3__w_in3*VV_junc3__vj3
    VV_junc3__Qin4 = VV_junc3__w_in4*VV_junc3__vj4
    VV_junc3__Qout1 = VV_junc3__w_out1*-VV_junc3__vj1
    VV_junc3__Qout3 = VV_junc3__w_out3*-VV_junc3__vj3
    VV_junc3__Qout4 = VV_junc3__w_out4*-VV_junc3__vj4
    VV_junc3__Qin_tot = VV_junc3__Qin1+VV_junc3__Qin2+VV_junc3__Qin3+VV_junc3__Qin4
    VV_junc3__Qout_tot = VV_junc3__Qout1+VV_junc3__Qout2+VV_junc3__Qout3+VV_junc3__Qout4
    VV_junc3__v = (VV_junc3__u-VV_junc3__u_d)/VV_junc3__R_VV_junc
    VV_junc3__bc1_is_in = (1 if VV_junc3__Qin1 > VV_junc3__v_threshold else 0)
    VV_junc3__bc3_is_in = (1 if VV_junc3__Qin3 > VV_junc3__v_threshold else 0)
    VV_junc3__bc4_is_in = (1 if VV_junc3__Qin4 > VV_junc3__v_threshold else 0)
    VV_junc3__bc1_is_out = (1 if VV_junc3__Qout1 > VV_junc3__v_threshold else 0)
    VV_junc3__bc3_is_out = (1 if VV_junc3__Qout3 > VV_junc3__v_threshold else 0)
    VV_junc3__bc4_is_out = (1 if VV_junc3__Qout4 > VV_junc3__v_threshold else 0)
    PV5__w_v = 0.5+1/np.pi*np.arctan(PV5__v/PV5__v_scale)
    PV5__w_v_d = 0.5+1/np.pi*np.arctan(PV5__v_d/PV5__v_scale)
    PV5__H_up = PV5__w_v_d*PV5__H_L_in+(1-PV5__w_v_d)*PV5__H_R_in
    PV5__s_v_d = np.abs(PV5__v_d)/(np.abs(PV5__v_d)+PV5__v_eps)
    PV5__H_L_out = (1-PV5__w_v_d)*PV5__H_down+PV5__w_v_d*PV5__H_L_in
    PV5__H_R_out = PV5__w_v_d*PV5__H_down+(1-PV5__w_v_d)*PV5__H_R_in
    PV5__v_pos = PV5__w_v*PV5__v
    PV5__v_neg = (1-PV5__w_v)*-PV5__v
    PV5__v_d_pos = PV5__w_v_d*PV5__v_d
    PV5__v_d_neg = (1-PV5__w_v_d)*-PV5__v_d
    PV5__H_volume_L = PV5__w_v*PV5__H_L_in+(1-PV5__w_v)*PV5__H_L_out
    PV5__H_volume_R = PV5__w_v_d*PV5__H_R_out+(1-PV5__w_v_d)*PV5__H_R_in
    PV5__v_mm3_s = PV5__v/PV5__one_mm3
    PV5__v_d_mm3_s = PV5__v_d/PV5__one_mm3
    PV6__w_v = 0.5+1/np.pi*np.arctan(PV6__v/PV6__v_scale)
    PV6__w_v_d = 0.5+1/np.pi*np.arctan(PV6__v_d/PV6__v_scale)
    PV6__H_up = PV6__w_v_d*PV6__H_L_in+(1-PV6__w_v_d)*PV6__H_R_in
    PV6__s_v_d = np.abs(PV6__v_d)/(np.abs(PV6__v_d)+PV6__v_eps)
    PV6__H_L_out = (1-PV6__w_v_d)*PV6__H_down+PV6__w_v_d*PV6__H_L_in
    PV6__H_R_out = PV6__w_v_d*PV6__H_down+(1-PV6__w_v_d)*PV6__H_R_in
    PV6__v_pos = PV6__w_v*PV6__v
    PV6__v_neg = (1-PV6__w_v)*-PV6__v
    PV6__v_d_pos = PV6__w_v_d*PV6__v_d
    PV6__v_d_neg = (1-PV6__w_v_d)*-PV6__v_d
    PV6__H_volume_L = PV6__w_v*PV6__H_L_in+(1-PV6__w_v)*PV6__H_L_out
    PV6__H_volume_R = PV6__w_v_d*PV6__H_R_out+(1-PV6__w_v_d)*PV6__H_R_in
    PV6__v_mm3_s = PV6__v/PV6__one_mm3
    PV6__v_d_mm3_s = PV6__v_d/PV6__one_mm3
    V5__w_v = 0.5+1/np.pi*np.arctan(V5__v/V5__v_scale)
    V5__H_up = V5__w_v*V5__H_L_in+(1-V5__w_v)*V5__H_R_in
    V5__s_v = np.abs(V5__v)/(np.abs(V5__v)+V5__v_eps)
    V5__H_L_out = (1-V5__w_v)*V5__H_down+V5__w_v*V5__H_L_in
    V5__H_R_out = V5__w_v*V5__H_down+(1-V5__w_v)*V5__H_R_in
    V5__v_pos = V5__w_v*V5__v
    V5__v_neg = (1-V5__w_v)*-V5__v
    V5__H_volume_L = V5__w_v*V5__H_L_in+(1-V5__w_v)*V5__H_L_out
    V5__H_volume_R = V5__w_v*V5__H_R_out+(1-V5__w_v)*V5__H_R_in
    V5__v_mm3_s = V5__v/V5__one_mm3
    V6__w_v = 0.5+1/np.pi*np.arctan(V6__v/V6__v_scale)
    V6__H_up = V6__w_v*V6__H_L_in+(1-V6__w_v)*V6__H_R_in
    V6__s_v = np.abs(V6__v)/(np.abs(V6__v)+V6__v_eps)
    V6__H_L_out = (1-V6__w_v)*V6__H_down+V6__w_v*V6__H_L_in
    V6__H_R_out = V6__w_v*V6__H_down+(1-V6__w_v)*V6__H_R_in
    V6__v_pos = V6__w_v*V6__v
    V6__v_neg = (1-V6__w_v)*-V6__v
    V6__H_volume_L = V6__w_v*V6__H_L_in+(1-V6__w_v)*V6__H_L_out
    V6__H_volume_R = V6__w_v*V6__H_R_out+(1-V6__w_v)*V6__H_R_in
    V6__v_mm3_s = V6__v/V6__one_mm3
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
    PV1__H_down_target = PV1__s_v_d*(PV1__H_mean+PV1__gamma_mirror*(PV1__H_mean-PV1__H_up))+(1-PV1__s_v_d)*PV1__H_mean
    PV2__H_down_target = PV2__s_v_d*(PV2__H_mean+PV2__gamma_mirror*(PV2__H_mean-PV2__H_up))+(1-PV2__s_v_d)*PV2__H_mean
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
    VV_junc2__n_in = VV_junc2__bc1_is_in+VV_junc2__bc2_is_in+VV_junc2__bc3_is_in+VV_junc2__bc4_is_in
    VV_junc2__n_out = VV_junc2__bc1_is_out+VV_junc2__bc2_is_out+VV_junc2__bc3_is_out+VV_junc2__bc4_is_out
    VV_junc2__RBC_in = VV_junc2__Qin1*V1__H_R_out+VV_junc2__Qin2*VV_junc2__H_to2+VV_junc2__Qin3*PV3__H_L_out+VV_junc2__Qin4*PV4__H_L_out
    VV_junc2__v_mm3_s = VV_junc2__v/VV_junc2__one_mm3
    VV_junc2__junction_type = (1 if VV_junc2__n_in == 1 else (-1 if VV_junc2__n_in >= 2 else 0))
    VV_junc2__is_split = (1 if VV_junc2__junction_type == 1 else 0)
    VV_junc2__is_merge = (1 if VV_junc2__junction_type == -1 else 0)
    VV_junc2__feed1 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin1 >= VV_junc2__Qin2) and (VV_junc2__Qin1 >= VV_junc2__Qin3) and (VV_junc2__Qin1 >= VV_junc2__Qin4) else 0)
    VV_junc2__feed2 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin2 > VV_junc2__Qin1) and (VV_junc2__Qin2 >= VV_junc2__Qin3) and (VV_junc2__Qin2 >= VV_junc2__Qin4) else 0)
    VV_junc2__feed3 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin3 > VV_junc2__Qin1) and (VV_junc2__Qin3 > VV_junc2__Qin2) and (VV_junc2__Qin3 >= VV_junc2__Qin4) else 0)
    VV_junc2__feed4 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin4 > VV_junc2__Qin1) and (VV_junc2__Qin4 > VV_junc2__Qin2) and (VV_junc2__Qin4 > VV_junc2__Qin3) else 0)
    VV_junc2__alpha1 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc1_is_out == 1) and (VV_junc2__Qout1 >= VV_junc2__Qout2) and (VV_junc2__Qout1 >= VV_junc2__Qout3) and (VV_junc2__Qout1 >= VV_junc2__Qout4) else 0)
    VV_junc2__alpha2 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc2_is_out == 1) and (VV_junc2__Qout2 > VV_junc2__Qout1) and (VV_junc2__Qout2 >= VV_junc2__Qout3) and (VV_junc2__Qout2 >= VV_junc2__Qout4) else 0)
    VV_junc2__alpha3 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc3_is_out == 1) and (VV_junc2__Qout3 > VV_junc2__Qout1) and (VV_junc2__Qout3 > VV_junc2__Qout2) and (VV_junc2__Qout3 >= VV_junc2__Qout4) else 0)
    VV_junc2__alpha4 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc4_is_out == 1) and (VV_junc2__Qout4 > VV_junc2__Qout1) and (VV_junc2__Qout4 > VV_junc2__Qout2) and (VV_junc2__Qout4 > VV_junc2__Qout3) else 0)
    VV_junc2__Qout1_rem = (0 if VV_junc2__alpha1 == 1 else VV_junc2__Qout1)
    VV_junc2__Qout2_rem = (0 if VV_junc2__alpha2 == 1 else VV_junc2__Qout2)
    VV_junc2__Qout3_rem = (0 if VV_junc2__alpha3 == 1 else VV_junc2__Qout3)
    VV_junc2__Qout4_rem = (0 if VV_junc2__alpha4 == 1 else VV_junc2__Qout4)
    VV_junc2__beta1 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc1_is_out == 1) and (VV_junc2__alpha1 == 0) and (VV_junc2__Qout1_rem >= VV_junc2__Qout2_rem) and (VV_junc2__Qout1_rem >= VV_junc2__Qout3_rem) and (VV_junc2__Qout1_rem >= VV_junc2__Qout4_rem) else 0)
    VV_junc2__beta2 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc2_is_out == 1) and (VV_junc2__alpha2 == 0) and (VV_junc2__Qout2_rem > VV_junc2__Qout1_rem) and (VV_junc2__Qout2_rem >= VV_junc2__Qout3_rem) and (VV_junc2__Qout2_rem >= VV_junc2__Qout4_rem) else 0)
    VV_junc2__beta3 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc3_is_out == 1) and (VV_junc2__alpha3 == 0) and (VV_junc2__Qout3_rem > VV_junc2__Qout1_rem) and (VV_junc2__Qout3_rem > VV_junc2__Qout2_rem) and (VV_junc2__Qout3_rem >= VV_junc2__Qout4_rem) else 0)
    VV_junc2__beta4 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc4_is_out == 1) and (VV_junc2__alpha4 == 0) and (VV_junc2__Qout4_rem > VV_junc2__Qout1_rem) and (VV_junc2__Qout4_rem > VV_junc2__Qout2_rem) and (VV_junc2__Qout4_rem > VV_junc2__Qout3_rem) else 0)
    VV_junc2__D_F = (VV_junc2__D1 if VV_junc2__feed1 == 1 else (VV_junc2__D2 if VV_junc2__feed2 == 1 else (VV_junc2__D3 if VV_junc2__feed3 == 1 else (VV_junc2__D4 if VV_junc2__feed4 == 1 else VV_junc2__D1))))
    VV_junc2__D_alpha = (VV_junc2__D1 if VV_junc2__alpha1 == 1 else (VV_junc2__D2 if VV_junc2__alpha2 == 1 else (VV_junc2__D3 if VV_junc2__alpha3 == 1 else (VV_junc2__D4 if VV_junc2__alpha4 == 1 else VV_junc2__D3))))
    VV_junc2__D_beta = (VV_junc2__D1 if VV_junc2__beta1 == 1 else (VV_junc2__D2 if VV_junc2__beta2 == 1 else (VV_junc2__D3 if VV_junc2__beta3 == 1 else (VV_junc2__D4 if VV_junc2__beta4 == 1 else VV_junc2__D4))))
    VV_junc2__v_alpha = (VV_junc2__Qout1 if VV_junc2__alpha1 == 1 else (VV_junc2__Qout2 if VV_junc2__alpha2 == 1 else (VV_junc2__Qout3 if VV_junc2__alpha3 == 1 else (VV_junc2__Qout4 if VV_junc2__alpha4 == 1 else 0))))
    VV_junc2__v_beta = (VV_junc2__Qout1 if VV_junc2__beta1 == 1 else (VV_junc2__Qout2 if VV_junc2__beta2 == 1 else (VV_junc2__Qout3 if VV_junc2__beta3 == 1 else (VV_junc2__Qout4 if VV_junc2__beta4 == 1 else 0))))
    PV3__H_down_target = PV3__s_v_d*(PV3__H_mean+PV3__gamma_mirror*(PV3__H_mean-PV3__H_up))+(1-PV3__s_v_d)*PV3__H_mean
    PV4__H_down_target = PV4__s_v_d*(PV4__H_mean+PV4__gamma_mirror*(PV4__H_mean-PV4__H_up))+(1-PV4__s_v_d)*PV4__H_mean
    V3__H_down_target = V3__s_v*(V3__H_mean+V3__gamma_mirror*(V3__H_mean-V3__H_up))+(1-V3__s_v)*V3__H_mean
    V4__H_down_target = V4__s_v*(V4__H_mean+V4__gamma_mirror*(V4__H_mean-V4__H_up))+(1-V4__s_v)*V4__H_mean
    VV_junc3__n_in = VV_junc3__bc1_is_in+VV_junc3__bc2_is_in+VV_junc3__bc3_is_in+VV_junc3__bc4_is_in
    VV_junc3__n_out = VV_junc3__bc1_is_out+VV_junc3__bc2_is_out+VV_junc3__bc3_is_out+VV_junc3__bc4_is_out
    VV_junc3__RBC_in = VV_junc3__Qin1*V2__H_R_out+VV_junc3__Qin2*VV_junc3__H_to2+VV_junc3__Qin3*PV5__H_L_out+VV_junc3__Qin4*PV6__H_L_out
    VV_junc3__v_mm3_s = VV_junc3__v/VV_junc3__one_mm3
    VV_junc3__junction_type = (1 if VV_junc3__n_in == 1 else (-1 if VV_junc3__n_in >= 2 else 0))
    VV_junc3__is_split = (1 if VV_junc3__junction_type == 1 else 0)
    VV_junc3__is_merge = (1 if VV_junc3__junction_type == -1 else 0)
    VV_junc3__feed1 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin1 >= VV_junc3__Qin2) and (VV_junc3__Qin1 >= VV_junc3__Qin3) and (VV_junc3__Qin1 >= VV_junc3__Qin4) else 0)
    VV_junc3__feed2 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin2 > VV_junc3__Qin1) and (VV_junc3__Qin2 >= VV_junc3__Qin3) and (VV_junc3__Qin2 >= VV_junc3__Qin4) else 0)
    VV_junc3__feed3 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin3 > VV_junc3__Qin1) and (VV_junc3__Qin3 > VV_junc3__Qin2) and (VV_junc3__Qin3 >= VV_junc3__Qin4) else 0)
    VV_junc3__feed4 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin4 > VV_junc3__Qin1) and (VV_junc3__Qin4 > VV_junc3__Qin2) and (VV_junc3__Qin4 > VV_junc3__Qin3) else 0)
    VV_junc3__alpha1 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc1_is_out == 1) and (VV_junc3__Qout1 >= VV_junc3__Qout2) and (VV_junc3__Qout1 >= VV_junc3__Qout3) and (VV_junc3__Qout1 >= VV_junc3__Qout4) else 0)
    VV_junc3__alpha2 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc2_is_out == 1) and (VV_junc3__Qout2 > VV_junc3__Qout1) and (VV_junc3__Qout2 >= VV_junc3__Qout3) and (VV_junc3__Qout2 >= VV_junc3__Qout4) else 0)
    VV_junc3__alpha3 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc3_is_out == 1) and (VV_junc3__Qout3 > VV_junc3__Qout1) and (VV_junc3__Qout3 > VV_junc3__Qout2) and (VV_junc3__Qout3 >= VV_junc3__Qout4) else 0)
    VV_junc3__alpha4 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc4_is_out == 1) and (VV_junc3__Qout4 > VV_junc3__Qout1) and (VV_junc3__Qout4 > VV_junc3__Qout2) and (VV_junc3__Qout4 > VV_junc3__Qout3) else 0)
    VV_junc3__Qout1_rem = (0 if VV_junc3__alpha1 == 1 else VV_junc3__Qout1)
    VV_junc3__Qout2_rem = (0 if VV_junc3__alpha2 == 1 else VV_junc3__Qout2)
    VV_junc3__Qout3_rem = (0 if VV_junc3__alpha3 == 1 else VV_junc3__Qout3)
    VV_junc3__Qout4_rem = (0 if VV_junc3__alpha4 == 1 else VV_junc3__Qout4)
    VV_junc3__beta1 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc1_is_out == 1) and (VV_junc3__alpha1 == 0) and (VV_junc3__Qout1_rem >= VV_junc3__Qout2_rem) and (VV_junc3__Qout1_rem >= VV_junc3__Qout3_rem) and (VV_junc3__Qout1_rem >= VV_junc3__Qout4_rem) else 0)
    VV_junc3__beta2 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc2_is_out == 1) and (VV_junc3__alpha2 == 0) and (VV_junc3__Qout2_rem > VV_junc3__Qout1_rem) and (VV_junc3__Qout2_rem >= VV_junc3__Qout3_rem) and (VV_junc3__Qout2_rem >= VV_junc3__Qout4_rem) else 0)
    VV_junc3__beta3 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc3_is_out == 1) and (VV_junc3__alpha3 == 0) and (VV_junc3__Qout3_rem > VV_junc3__Qout1_rem) and (VV_junc3__Qout3_rem > VV_junc3__Qout2_rem) and (VV_junc3__Qout3_rem >= VV_junc3__Qout4_rem) else 0)
    VV_junc3__beta4 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc4_is_out == 1) and (VV_junc3__alpha4 == 0) and (VV_junc3__Qout4_rem > VV_junc3__Qout1_rem) and (VV_junc3__Qout4_rem > VV_junc3__Qout2_rem) and (VV_junc3__Qout4_rem > VV_junc3__Qout3_rem) else 0)
    VV_junc3__D_F = (VV_junc3__D1 if VV_junc3__feed1 == 1 else (VV_junc3__D2 if VV_junc3__feed2 == 1 else (VV_junc3__D3 if VV_junc3__feed3 == 1 else (VV_junc3__D4 if VV_junc3__feed4 == 1 else VV_junc3__D1))))
    VV_junc3__D_alpha = (VV_junc3__D1 if VV_junc3__alpha1 == 1 else (VV_junc3__D2 if VV_junc3__alpha2 == 1 else (VV_junc3__D3 if VV_junc3__alpha3 == 1 else (VV_junc3__D4 if VV_junc3__alpha4 == 1 else VV_junc3__D3))))
    VV_junc3__D_beta = (VV_junc3__D1 if VV_junc3__beta1 == 1 else (VV_junc3__D2 if VV_junc3__beta2 == 1 else (VV_junc3__D3 if VV_junc3__beta3 == 1 else (VV_junc3__D4 if VV_junc3__beta4 == 1 else VV_junc3__D4))))
    VV_junc3__v_alpha = (VV_junc3__Qout1 if VV_junc3__alpha1 == 1 else (VV_junc3__Qout2 if VV_junc3__alpha2 == 1 else (VV_junc3__Qout3 if VV_junc3__alpha3 == 1 else (VV_junc3__Qout4 if VV_junc3__alpha4 == 1 else 0))))
    VV_junc3__v_beta = (VV_junc3__Qout1 if VV_junc3__beta1 == 1 else (VV_junc3__Qout2 if VV_junc3__beta2 == 1 else (VV_junc3__Qout3 if VV_junc3__beta3 == 1 else (VV_junc3__Qout4 if VV_junc3__beta4 == 1 else 0))))
    PV5__H_down_target = PV5__s_v_d*(PV5__H_mean+PV5__gamma_mirror*(PV5__H_mean-PV5__H_up))+(1-PV5__s_v_d)*PV5__H_mean
    PV6__H_down_target = PV6__s_v_d*(PV6__H_mean+PV6__gamma_mirror*(PV6__H_mean-PV6__H_up))+(1-PV6__s_v_d)*PV6__H_mean
    V5__H_down_target = V5__s_v*(V5__H_mean+V5__gamma_mirror*(V5__H_mean-V5__H_up))+(1-V5__s_v)*V5__H_mean
    V6__H_down_target = V6__s_v*(V6__H_mean+V6__gamma_mirror*(V6__H_mean-V6__H_up))+(1-V6__s_v)*V6__H_mean
    inlet__H_down_target = inlet__s_v_d*(inlet__H_mean+inlet__gamma_mirror*(inlet__H_mean-inlet__H_up))+(1-inlet__s_v_d)*inlet__H_mean
    VV_junc1__FQB_alpha = (VV_junc1__v_alpha+VV_junc1__div_0)/(VV_junc1__v_alpha+VV_junc1__v_beta+2*VV_junc1__div_0)
    VV_junc1__B = 1+6.98*(1-VV_junc1__H_mean)/(VV_junc1__D_F*1e6)
    VV_junc1__A = -6.96*np.log(VV_junc1__D_alpha*1e6/(VV_junc1__D_beta*1e6))/(VV_junc1__D_F*1e6)
    VV_junc1__X_0 = 0.4/(VV_junc1__D_F*1e6)
    VV_junc1__y_raw = (VV_junc1__FQB_alpha-VV_junc1__X_0)/(1-2*VV_junc1__X_0+VV_junc1__div_0)
    VV_junc1__y = min(max(VV_junc1__y_raw, VV_junc1__div_0y), 1-VV_junc1__div_0y)
    V1__H_down_target = V1__s_v*(V1__H_mean+V1__gamma_mirror*(V1__H_mean-V1__H_up))+(1-V1__s_v)*V1__H_mean
    V2__H_down_target = V2__s_v*(V2__H_mean+V2__gamma_mirror*(V2__H_mean-V2__H_up))+(1-V2__s_v)*V2__H_mean
    VV_junc2__FQB_alpha = (VV_junc2__v_alpha+VV_junc2__div_0)/(VV_junc2__v_alpha+VV_junc2__v_beta+2*VV_junc2__div_0)
    VV_junc2__B = 1+6.98*(1-VV_junc2__H_mean)/(VV_junc2__D_F*1e6)
    VV_junc2__A = -6.96*np.log(VV_junc2__D_alpha*1e6/(VV_junc2__D_beta*1e6))/(VV_junc2__D_F*1e6)
    VV_junc2__X_0 = 0.4/(VV_junc2__D_F*1e6)
    VV_junc2__y_raw = (VV_junc2__FQB_alpha-VV_junc2__X_0)/(1-2*VV_junc2__X_0+VV_junc2__div_0)
    VV_junc2__y = min(max(VV_junc2__y_raw, VV_junc2__div_0y), 1-VV_junc2__div_0y)
    VV_junc3__FQB_alpha = (VV_junc3__v_alpha+VV_junc3__div_0)/(VV_junc3__v_alpha+VV_junc3__v_beta+2*VV_junc3__div_0)
    VV_junc3__B = 1+6.98*(1-VV_junc3__H_mean)/(VV_junc3__D_F*1e6)
    VV_junc3__A = -6.96*np.log(VV_junc3__D_alpha*1e6/(VV_junc3__D_beta*1e6))/(VV_junc3__D_F*1e6)
    VV_junc3__X_0 = 0.4/(VV_junc3__D_F*1e6)
    VV_junc3__y_raw = (VV_junc3__FQB_alpha-VV_junc3__X_0)/(1-2*VV_junc3__X_0+VV_junc3__div_0)
    VV_junc3__y = min(max(VV_junc3__y_raw, VV_junc3__div_0y), 1-VV_junc3__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc2__ph = np.log(VV_junc2__y/(1-VV_junc2__y))
    VV_junc3__ph = np.log(VV_junc3__y/(1-VV_junc3__y))
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
    VV_junc2__FQE_alpha = 1/(1+np.exp(-(VV_junc2__A+VV_junc2__B*VV_junc2__ph)))
    VV_junc2__H_VV_out_alpha = VV_junc2__H_mean*VV_junc2__FQE_alpha/(VV_junc2__FQB_alpha+VV_junc2__div_0)
    VV_junc2__H_VV_out_beta = VV_junc2__H_mean*(1-VV_junc2__FQE_alpha)/(1-VV_junc2__FQB_alpha+VV_junc2__div_0)
    VV_junc2__H_split1 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha1 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta1 == 1 else V1__H_R_out))
    VV_junc2__H_split2 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha2 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta2 == 1 else VV_junc2__H_to2))
    VV_junc2__H_split3 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha3 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta3 == 1 else PV3__H_L_out))
    VV_junc2__H_split4 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha4 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta4 == 1 else PV4__H_L_out))
    VV_junc2__H_daughter1 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split1 if VV_junc2__is_split == 1 else V1__H_R_out))
    VV_junc2__H_daughter2 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split2 if VV_junc2__is_split == 1 else VV_junc2__H_to2))
    VV_junc2__H_daughter3 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split3 if VV_junc2__is_split == 1 else PV3__H_L_out))
    VV_junc2__H_daughter4 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split4 if VV_junc2__is_split == 1 else PV4__H_L_out))
    VV_junc2__H_from1_target = (VV_junc2__H_daughter1 if VV_junc2__bc1_is_out == 1 else V1__H_R_out)
    VV_junc2__H_from2_target = (VV_junc2__H_daughter2 if VV_junc2__bc2_is_out == 1 else VV_junc2__H_to2)
    VV_junc2__H_from3_target = (VV_junc2__H_daughter3 if VV_junc2__bc3_is_out == 1 else PV3__H_L_out)
    VV_junc2__H_from4_target = (VV_junc2__H_daughter4 if VV_junc2__bc4_is_out == 1 else PV4__H_L_out)
    VV_junc3__FQE_alpha = 1/(1+np.exp(-(VV_junc3__A+VV_junc3__B*VV_junc3__ph)))
    VV_junc3__H_VV_out_alpha = VV_junc3__H_mean*VV_junc3__FQE_alpha/(VV_junc3__FQB_alpha+VV_junc3__div_0)
    VV_junc3__H_VV_out_beta = VV_junc3__H_mean*(1-VV_junc3__FQE_alpha)/(1-VV_junc3__FQB_alpha+VV_junc3__div_0)
    VV_junc3__H_split1 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha1 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta1 == 1 else V2__H_R_out))
    VV_junc3__H_split2 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha2 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta2 == 1 else VV_junc3__H_to2))
    VV_junc3__H_split3 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha3 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta3 == 1 else PV5__H_L_out))
    VV_junc3__H_split4 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha4 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta4 == 1 else PV6__H_L_out))
    VV_junc3__H_daughter1 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split1 if VV_junc3__is_split == 1 else V2__H_R_out))
    VV_junc3__H_daughter2 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split2 if VV_junc3__is_split == 1 else VV_junc3__H_to2))
    VV_junc3__H_daughter3 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split3 if VV_junc3__is_split == 1 else PV5__H_L_out))
    VV_junc3__H_daughter4 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split4 if VV_junc3__is_split == 1 else PV6__H_L_out))
    VV_junc3__H_from1_target = (VV_junc3__H_daughter1 if VV_junc3__bc1_is_out == 1 else V2__H_R_out)
    VV_junc3__H_from2_target = (VV_junc3__H_daughter2 if VV_junc3__bc2_is_out == 1 else VV_junc3__H_to2)
    VV_junc3__H_from3_target = (VV_junc3__H_daughter3 if VV_junc3__bc3_is_out == 1 else PV5__H_L_out)
    VV_junc3__H_from4_target = (VV_junc3__H_daughter4 if VV_junc3__bc4_is_out == 1 else PV6__H_L_out)
    VV_junc1__H_from1 = VV_junc1__w_out1*VV_junc1__H_from1_target
    VV_junc1__H_from2 = VV_junc1__w_out2*VV_junc1__H_from2_target
    VV_junc1__H_from3 = VV_junc1__w_out3*VV_junc1__H_from3_target
    VV_junc1__H_from4 = VV_junc1__w_out4*VV_junc1__H_from4_target
    VV_junc1__RBC_out = VV_junc1__Qout1*VV_junc1__H_from1+VV_junc1__Qout2*VV_junc1__H_from2+VV_junc1__Qout3*VV_junc1__H_from3+VV_junc1__Qout4*VV_junc1__H_from4
    VV_junc2__H_from1 = VV_junc2__w_out1*VV_junc2__H_from1_target
    VV_junc2__H_from2 = VV_junc2__w_out2*VV_junc2__H_from2_target
    VV_junc2__H_from3 = VV_junc2__w_out3*VV_junc2__H_from3_target
    VV_junc2__H_from4 = VV_junc2__w_out4*VV_junc2__H_from4_target
    VV_junc2__RBC_out = VV_junc2__Qout1*VV_junc2__H_from1+VV_junc2__Qout2*VV_junc2__H_from2+VV_junc2__Qout3*VV_junc2__H_from3+VV_junc2__Qout4*VV_junc2__H_from4
    VV_junc3__H_from1 = VV_junc3__w_out1*VV_junc3__H_from1_target
    VV_junc3__H_from2 = VV_junc3__w_out2*VV_junc3__H_from2_target
    VV_junc3__H_from3 = VV_junc3__w_out3*VV_junc3__H_from3_target
    VV_junc3__H_from4 = VV_junc3__w_out4*VV_junc3__H_from4_target
    VV_junc3__RBC_out = VV_junc3__Qout1*VV_junc3__H_from1+VV_junc3__Qout2*VV_junc3__H_from2+VV_junc3__Qout3*VV_junc3__H_from3+VV_junc3__Qout4*VV_junc3__H_from4

    # ODEs
    dydt = np.zeros(len(y))
    dydt[0] = (VV_junc1__H_from1-inlet__H_link_R)/inlet__tau_link
    dydt[1] = (inlet__H_R_out_LHS-inlet__H_link_L)/inlet__tau_link
    dydt[2] = (inlet__H_down_target-inlet__H_down)/inlet__tau_H_down
    dydt[3] = inlet__v*inlet__H_volume_L-inlet__v_d*inlet__H_volume_R
    dydt[4] = inlet__v-inlet__v_d
    dydt[5] = VV_junc1__RBC_in-VV_junc1__RBC_out
    dydt[6] = inlet__v_d+VV_junc1__vbc2-VV_junc1__v
    dydt[7] = VV_junc1__v-PV1__v-PV2__v
    dydt[8] = (V1__H_L_out-PV1__H_link_R)/PV1__tau_link
    dydt[9] = (VV_junc1__H_from3-PV1__H_link_L)/PV1__tau_link
    dydt[10] = (PV1__H_down_target-PV1__H_down)/PV1__tau_H_down
    dydt[11] = PV1__v*PV1__H_volume_L-PV1__v_d*PV1__H_volume_R
    dydt[12] = PV1__v-PV1__v_d
    dydt[13] = (V2__H_L_out-PV2__H_link_R)/PV2__tau_link
    dydt[14] = (VV_junc1__H_from4-PV2__H_link_L)/PV2__tau_link
    dydt[15] = (PV2__H_down_target-PV2__H_down)/PV2__tau_H_down
    dydt[16] = PV2__v*PV2__H_volume_L-PV2__v_d*PV2__H_volume_R
    dydt[17] = PV2__v-PV2__v_d
    dydt[18] = (VV_junc2__H_from1-V1__H_link_R)/V1__tau_link
    dydt[19] = (PV1__H_R_out-V1__H_link_L)/V1__tau_link
    dydt[20] = (V1__H_down_target-V1__H_down)/V1__tau_H_down
    dydt[21] = PV1__v_d*V1__H_volume_L-V1__v*V1__H_volume_R
    dydt[22] = PV1__v_d-V1__v
    dydt[23] = (VV_junc3__H_from1-V2__H_link_R)/V2__tau_link
    dydt[24] = (PV2__H_R_out-V2__H_link_L)/V2__tau_link
    dydt[25] = (V2__H_down_target-V2__H_down)/V2__tau_H_down
    dydt[26] = PV2__v_d*V2__H_volume_L-V2__v*V2__H_volume_R
    dydt[27] = PV2__v_d-V2__v
    dydt[28] = VV_junc2__RBC_in-VV_junc2__RBC_out
    dydt[29] = V1__v+VV_junc2__vbc2-VV_junc2__v
    dydt[30] = VV_junc2__v-PV3__v-PV4__v
    dydt[31] = (V3__H_L_out-PV3__H_link_R)/PV3__tau_link
    dydt[32] = (VV_junc2__H_from3-PV3__H_link_L)/PV3__tau_link
    dydt[33] = (PV3__H_down_target-PV3__H_down)/PV3__tau_H_down
    dydt[34] = PV3__v*PV3__H_volume_L-PV3__v_d*PV3__H_volume_R
    dydt[35] = PV3__v-PV3__v_d
    dydt[36] = (V4__H_L_out-PV4__H_link_R)/PV4__tau_link
    dydt[37] = (VV_junc2__H_from4-PV4__H_link_L)/PV4__tau_link
    dydt[38] = (PV4__H_down_target-PV4__H_down)/PV4__tau_H_down
    dydt[39] = PV4__v*PV4__H_volume_L-PV4__v_d*PV4__H_volume_R
    dydt[40] = PV4__v-PV4__v_d
    dydt[41] = (V3__H_L_out_RHS-V3__H_link_R)/V3__tau_link
    dydt[42] = (PV3__H_R_out-V3__H_link_L)/V3__tau_link
    dydt[43] = (V3__H_down_target-V3__H_down)/V3__tau_H_down
    dydt[44] = PV3__v_d*V3__H_volume_L-V3__v*V3__H_volume_R
    dydt[45] = PV3__v_d-V3__v
    dydt[46] = (V4__H_L_out_RHS-V4__H_link_R)/V4__tau_link
    dydt[47] = (PV4__H_R_out-V4__H_link_L)/V4__tau_link
    dydt[48] = (V4__H_down_target-V4__H_down)/V4__tau_H_down
    dydt[49] = PV4__v_d*V4__H_volume_L-V4__v*V4__H_volume_R
    dydt[50] = PV4__v_d-V4__v
    dydt[51] = VV_junc3__RBC_in-VV_junc3__RBC_out
    dydt[52] = V2__v+VV_junc3__vbc2-VV_junc3__v
    dydt[53] = VV_junc3__v-PV5__v-PV6__v
    dydt[54] = (V5__H_L_out-PV5__H_link_R)/PV5__tau_link
    dydt[55] = (VV_junc3__H_from3-PV5__H_link_L)/PV5__tau_link
    dydt[56] = (PV5__H_down_target-PV5__H_down)/PV5__tau_H_down
    dydt[57] = PV5__v*PV5__H_volume_L-PV5__v_d*PV5__H_volume_R
    dydt[58] = PV5__v-PV5__v_d
    dydt[59] = (V6__H_L_out-PV6__H_link_R)/PV6__tau_link
    dydt[60] = (VV_junc3__H_from4-PV6__H_link_L)/PV6__tau_link
    dydt[61] = (PV6__H_down_target-PV6__H_down)/PV6__tau_H_down
    dydt[62] = PV6__v*PV6__H_volume_L-PV6__v_d*PV6__H_volume_R
    dydt[63] = PV6__v-PV6__v_d
    dydt[64] = (V5__H_L_out_RHS-V5__H_link_R)/V5__tau_link
    dydt[65] = (PV5__H_R_out-V5__H_link_L)/V5__tau_link
    dydt[66] = (V5__H_down_target-V5__H_down)/V5__tau_H_down
    dydt[67] = PV5__v_d*V5__H_volume_L-V5__v*V5__H_volume_R
    dydt[68] = PV5__v_d-V5__v
    dydt[69] = (V6__H_L_out_RHS-V6__H_link_R)/V6__tau_link
    dydt[70] = (PV6__H_R_out-V6__H_link_L)/V6__tau_link
    dydt[71] = (V6__H_down_target-V6__H_down)/V6__tau_H_down
    dydt[72] = PV6__v_d*V6__H_volume_L-V6__v*V6__H_volume_R
    dydt[73] = PV6__v_d-V6__v

    return dydt

def compute_algebraics(t, y):
    """Compute all algebraic variables at a given time point."""
    # Unpack state
    inlet__H_link_R = y[0]
    inlet__H_link_L = y[1]
    inlet__H_down = y[2]
    inlet__RBC_volume = y[3]
    inlet__q_C = y[4]
    VV_junc1__RBC_volume = y[5]
    VV_junc1__q_C = y[6]
    VV_junc1__q_C_d = y[7]
    PV1__H_link_R = y[8]
    PV1__H_link_L = y[9]
    PV1__H_down = y[10]
    PV1__RBC_volume = y[11]
    PV1__q_C = y[12]
    PV2__H_link_R = y[13]
    PV2__H_link_L = y[14]
    PV2__H_down = y[15]
    PV2__RBC_volume = y[16]
    PV2__q_C = y[17]
    V1__H_link_R = y[18]
    V1__H_link_L = y[19]
    V1__H_down = y[20]
    V1__RBC_volume = y[21]
    V1__q_C = y[22]
    V2__H_link_R = y[23]
    V2__H_link_L = y[24]
    V2__H_down = y[25]
    V2__RBC_volume = y[26]
    V2__q_C = y[27]
    VV_junc2__RBC_volume = y[28]
    VV_junc2__q_C = y[29]
    VV_junc2__q_C_d = y[30]
    PV3__H_link_R = y[31]
    PV3__H_link_L = y[32]
    PV3__H_down = y[33]
    PV3__RBC_volume = y[34]
    PV3__q_C = y[35]
    PV4__H_link_R = y[36]
    PV4__H_link_L = y[37]
    PV4__H_down = y[38]
    PV4__RBC_volume = y[39]
    PV4__q_C = y[40]
    V3__H_link_R = y[41]
    V3__H_link_L = y[42]
    V3__H_down = y[43]
    V3__RBC_volume = y[44]
    V3__q_C = y[45]
    V4__H_link_R = y[46]
    V4__H_link_L = y[47]
    V4__H_down = y[48]
    V4__RBC_volume = y[49]
    V4__q_C = y[50]
    VV_junc3__RBC_volume = y[51]
    VV_junc3__q_C = y[52]
    VV_junc3__q_C_d = y[53]
    PV5__H_link_R = y[54]
    PV5__H_link_L = y[55]
    PV5__H_down = y[56]
    PV5__RBC_volume = y[57]
    PV5__q_C = y[58]
    PV6__H_link_R = y[59]
    PV6__H_link_L = y[60]
    PV6__H_down = y[61]
    PV6__RBC_volume = y[62]
    PV6__q_C = y[63]
    V5__H_link_R = y[64]
    V5__H_link_L = y[65]
    V5__H_down = y[66]
    V5__RBC_volume = y[67]
    V5__q_C = y[68]
    V6__H_link_R = y[69]
    V6__H_link_L = y[70]
    V6__H_down = y[71]
    V6__RBC_volume = y[72]
    V6__q_C = y[73]

    # Time variable
    environment__time = t

    # Algebraic equations
    inlet__H_L_in = inlet__H_link_L
    inlet__H_R_in = inlet__H_link_R
    inlet__q_us = np.pi*np.square(inlet__r)*inlet__l
    inlet__q = inlet__q_us+inlet__q_C
    inlet__C = np.pi*np.square(8.5e-9)*inlet__l/133.322
    inlet__Z = (0.8+np.exp(-0.075*2*inlet__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*inlet__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*inlet__r*1e6, 12))
    inlet__mu_45 = 6*np.exp(-0.085*2*inlet__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*inlet__r*1e6, 0.645))
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
    PV1__u = PV1__q_C/PV1__C+PV1__u_ext
    PV2__R_constriction = PV2__R_constriction_base+(PV2__R_constriction_final-PV2__R_constriction_base)/(1+np.exp(-(environment__time-PV2__t0)/PV2__tau_sig))
    PV2__H_L_in = PV2__H_link_L
    PV2__H_R_in = PV2__H_link_R
    PV2__q_us = np.pi*np.square(PV2__r)*PV2__l
    PV2__q = PV2__q_us+PV2__q_C
    PV2__C = np.pi*np.square(8.5e-9)*PV2__l/133.322
    PV2__Z = (0.8+np.exp(-0.075*2*PV2__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV2__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV2__r*1e6, 12))
    PV2__mu_45 = 6*np.exp(-0.085*2*PV2__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV2__r*1e6, 0.645))
    PV2__u = PV2__q_C/PV2__C+PV2__u_ext
    V1__H_L_in = V1__H_link_L
    V1__H_R_in = V1__H_link_R
    V1__q_us = np.pi*np.square(V1__r)*V1__l
    V1__q = V1__q_us+V1__q_C
    V1__C = np.pi*np.square(8.5e-9)*V1__l/133.322
    V1__Z = (0.8+np.exp(-0.075*2*V1__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V1__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V1__r*1e6, 12))
    V1__mu_45 = 6*np.exp(-0.085*2*V1__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V1__r*1e6, 0.645))
    V1__u = V1__q_C/V1__C+V1__u_ext
    V2__H_L_in = V2__H_link_L
    V2__H_R_in = V2__H_link_R
    V2__q_us = np.pi*np.square(V2__r)*V2__l
    V2__q = V2__q_us+V2__q_C
    V2__C = np.pi*np.square(8.5e-9)*V2__l/133.322
    V2__Z = (0.8+np.exp(-0.075*2*V2__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V2__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V2__r*1e6, 12))
    V2__mu_45 = 6*np.exp(-0.085*2*V2__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V2__r*1e6, 0.645))
    V2__u = V2__q_C/V2__C+V2__u_ext
    VV_junc2__vj2 = VV_junc2__vbc2
    VV_junc2__D1 = 2*V1__r
    VV_junc2__D2 = 2*VV_junc2__r_bc2
    VV_junc2__D3 = 2*PV3__r
    VV_junc2__D4 = 2*PV4__r
    VV_junc2__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc2__vj2/VV_junc2__v_scale)
    VV_junc2__w_out2 = 1-VV_junc2__w_in2
    VV_junc2__Qin2 = VV_junc2__w_in2*VV_junc2__vj2
    VV_junc2__Qout2 = VV_junc2__w_out2*-VV_junc2__vj2
    VV_junc2__q_us = np.pi*np.square(VV_junc2__r)*VV_junc2__l
    VV_junc2__q = VV_junc2__q_us+VV_junc2__q_C+VV_junc2__q_C_d
    VV_junc2__bc2_is_in = (1 if VV_junc2__Qin2 > VV_junc2__v_threshold else 0)
    VV_junc2__bc2_is_out = (1 if VV_junc2__Qout2 > VV_junc2__v_threshold else 0)
    VV_junc2__C_max12 = (V1__C if V1__C > VV_junc2__C_conn2 else (VV_junc2__C_conn2 if V1__C <= VV_junc2__C_conn2 else 0.0))
    PV3__R_constriction = PV3__R_constriction_base+(PV3__R_constriction_final-PV3__R_constriction_base)/(1+np.exp(-(environment__time-PV3__t0)/PV3__tau_sig))
    PV3__H_L_in = PV3__H_link_L
    PV3__H_R_in = PV3__H_link_R
    PV3__q_us = np.pi*np.square(PV3__r)*PV3__l
    PV3__q = PV3__q_us+PV3__q_C
    PV3__C = np.pi*np.square(8.5e-9)*PV3__l/133.322
    PV3__Z = (0.8+np.exp(-0.075*2*PV3__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV3__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV3__r*1e6, 12))
    PV3__mu_45 = 6*np.exp(-0.085*2*PV3__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV3__r*1e6, 0.645))
    PV3__u = PV3__q_C/PV3__C+PV3__u_ext
    PV4__R_constriction = PV4__R_constriction_base+(PV4__R_constriction_final-PV4__R_constriction_base)/(1+np.exp(-(environment__time-PV4__t0)/PV4__tau_sig))
    PV4__H_L_in = PV4__H_link_L
    PV4__H_R_in = PV4__H_link_R
    PV4__q_us = np.pi*np.square(PV4__r)*PV4__l
    PV4__q = PV4__q_us+PV4__q_C
    PV4__C = np.pi*np.square(8.5e-9)*PV4__l/133.322
    PV4__Z = (0.8+np.exp(-0.075*2*PV4__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV4__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV4__r*1e6, 12))
    PV4__mu_45 = 6*np.exp(-0.085*2*PV4__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV4__r*1e6, 0.645))
    PV4__u = PV4__q_C/PV4__C+PV4__u_ext
    V3__H_L_in = V3__H_link_L
    V3__H_R_in = V3__H_link_R
    V3__q_us = np.pi*np.square(V3__r)*V3__l
    V3__q = V3__q_us+V3__q_C
    V3__C = np.pi*np.square(8.5e-9)*V3__l/133.322
    V3__Z = (0.8+np.exp(-0.075*2*V3__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V3__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V3__r*1e6, 12))
    V3__mu_45 = 6*np.exp(-0.085*2*V3__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V3__r*1e6, 0.645))
    V3__u = V3__q_C/V3__C+V3__u_ext
    V4__H_L_in = V4__H_link_L
    V4__H_R_in = V4__H_link_R
    V4__q_us = np.pi*np.square(V4__r)*V4__l
    V4__q = V4__q_us+V4__q_C
    V4__C = np.pi*np.square(8.5e-9)*V4__l/133.322
    V4__Z = (0.8+np.exp(-0.075*2*V4__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V4__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V4__r*1e6, 12))
    V4__mu_45 = 6*np.exp(-0.085*2*V4__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V4__r*1e6, 0.645))
    V4__u = V4__q_C/V4__C+V4__u_ext
    VV_junc3__vj2 = VV_junc3__vbc2
    VV_junc3__D1 = 2*V2__r
    VV_junc3__D2 = 2*VV_junc3__r_bc2
    VV_junc3__D3 = 2*PV5__r
    VV_junc3__D4 = 2*PV6__r
    VV_junc3__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc3__vj2/VV_junc3__v_scale)
    VV_junc3__w_out2 = 1-VV_junc3__w_in2
    VV_junc3__Qin2 = VV_junc3__w_in2*VV_junc3__vj2
    VV_junc3__Qout2 = VV_junc3__w_out2*-VV_junc3__vj2
    VV_junc3__q_us = np.pi*np.square(VV_junc3__r)*VV_junc3__l
    VV_junc3__q = VV_junc3__q_us+VV_junc3__q_C+VV_junc3__q_C_d
    VV_junc3__bc2_is_in = (1 if VV_junc3__Qin2 > VV_junc3__v_threshold else 0)
    VV_junc3__bc2_is_out = (1 if VV_junc3__Qout2 > VV_junc3__v_threshold else 0)
    VV_junc3__C_max12 = (V2__C if V2__C > VV_junc3__C_conn2 else (VV_junc3__C_conn2 if V2__C <= VV_junc3__C_conn2 else 0.0))
    PV5__R_constriction = PV5__R_constriction_base+(PV5__R_constriction_final-PV5__R_constriction_base)/(1+np.exp(-(environment__time-PV5__t0)/PV5__tau_sig))
    PV5__H_L_in = PV5__H_link_L
    PV5__H_R_in = PV5__H_link_R
    PV5__q_us = np.pi*np.square(PV5__r)*PV5__l
    PV5__q = PV5__q_us+PV5__q_C
    PV5__C = np.pi*np.square(8.5e-9)*PV5__l/133.322
    PV5__Z = (0.8+np.exp(-0.075*2*PV5__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV5__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV5__r*1e6, 12))
    PV5__mu_45 = 6*np.exp(-0.085*2*PV5__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV5__r*1e6, 0.645))
    PV5__u = PV5__q_C/PV5__C+PV5__u_ext
    PV6__R_constriction = PV6__R_constriction_base+(PV6__R_constriction_final-PV6__R_constriction_base)/(1+np.exp(-(environment__time-PV6__t0)/PV6__tau_sig))
    PV6__H_L_in = PV6__H_link_L
    PV6__H_R_in = PV6__H_link_R
    PV6__q_us = np.pi*np.square(PV6__r)*PV6__l
    PV6__q = PV6__q_us+PV6__q_C
    PV6__C = np.pi*np.square(8.5e-9)*PV6__l/133.322
    PV6__Z = (0.8+np.exp(-0.075*2*PV6__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV6__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV6__r*1e6, 12))
    PV6__mu_45 = 6*np.exp(-0.085*2*PV6__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV6__r*1e6, 0.645))
    PV6__u = PV6__q_C/PV6__C+PV6__u_ext
    V5__H_L_in = V5__H_link_L
    V5__H_R_in = V5__H_link_R
    V5__q_us = np.pi*np.square(V5__r)*V5__l
    V5__q = V5__q_us+V5__q_C
    V5__C = np.pi*np.square(8.5e-9)*V5__l/133.322
    V5__Z = (0.8+np.exp(-0.075*2*V5__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V5__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V5__r*1e6, 12))
    V5__mu_45 = 6*np.exp(-0.085*2*V5__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V5__r*1e6, 0.645))
    V5__u = V5__q_C/V5__C+V5__u_ext
    V6__H_L_in = V6__H_link_L
    V6__H_R_in = V6__H_link_R
    V6__q_us = np.pi*np.square(V6__r)*V6__l
    V6__q = V6__q_us+V6__q_C
    V6__C = np.pi*np.square(8.5e-9)*V6__l/133.322
    V6__Z = (0.8+np.exp(-0.075*2*V6__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V6__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V6__r*1e6, 12))
    V6__mu_45 = 6*np.exp(-0.085*2*V6__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V6__r*1e6, 0.645))
    V6__u = V6__q_C/V6__C+V6__u_ext
    inlet__RBC_volume_init = inlet__H_global_L*inlet__q_us
    inlet__H_mean = inlet__RBC_volume/inlet__q
    inlet__hem_dep_u_rel = 1+(inlet__mu_45-1)*(safe_power(1-inlet__H_mean, inlet__Z)-1)/(safe_power(1-inlet__H_global_L, inlet__Z)-1)*np.square(2*inlet__r*1e6/(2*inlet__r*1e6-1.1))
    inlet__u_mmHg = inlet__u/133.322
    VV_junc1__RBC_volume_init = VV_junc1__H_global_L*VV_junc1__q_us
    VV_junc1__H_mean = VV_junc1__RBC_volume/(VV_junc1__q_us+VV_junc1__div_0)
    VV_junc1__C_max123 = (VV_junc1__C_max12 if VV_junc1__C_max12 > PV1__C else (PV1__C if VV_junc1__C_max12 <= PV1__C else 0.0))
    VV_junc1__C = (VV_junc1__C_max123 if VV_junc1__C_max123 > PV2__C else (PV2__C if VV_junc1__C_max123 <= PV2__C else 0.0))
    PV1__RBC_volume_init = PV1__H_global_L*PV1__q_us
    PV1__H_mean = PV1__RBC_volume/PV1__q
    PV1__hem_dep_u_rel = 1+(PV1__mu_45-1)*(safe_power(1-PV1__H_mean, PV1__Z)-1)/(safe_power(1-PV1__H_global_L, PV1__Z)-1)*np.square(2*PV1__r*1e6/(2*PV1__r*1e6-1.1))
    PV1__u_mmHg = PV1__u/133.322
    PV2__RBC_volume_init = PV2__H_global_L*PV2__q_us
    PV2__H_mean = PV2__RBC_volume/PV2__q
    PV2__hem_dep_u_rel = 1+(PV2__mu_45-1)*(safe_power(1-PV2__H_mean, PV2__Z)-1)/(safe_power(1-PV2__H_global_L, PV2__Z)-1)*np.square(2*PV2__r*1e6/(2*PV2__r*1e6-1.1))
    PV2__u_mmHg = PV2__u/133.322
    V1__RBC_volume_init = V1__H_global_L*V1__q_us
    V1__H_mean = V1__RBC_volume/V1__q
    V1__hem_dep_u_rel = 1+(V1__mu_45-1)*(safe_power(1-V1__H_mean, V1__Z)-1)/(safe_power(1-V1__H_global_L, V1__Z)-1)*np.square(2*V1__r*1e6/(2*V1__r*1e6-1.1))
    V1__u_mmHg = V1__u/133.322
    V2__RBC_volume_init = V2__H_global_L*V2__q_us
    V2__H_mean = V2__RBC_volume/V2__q
    V2__hem_dep_u_rel = 1+(V2__mu_45-1)*(safe_power(1-V2__H_mean, V2__Z)-1)/(safe_power(1-V2__H_global_L, V2__Z)-1)*np.square(2*V2__r*1e6/(2*V2__r*1e6-1.1))
    V2__u_mmHg = V2__u/133.322
    VV_junc2__RBC_volume_init = VV_junc2__H_global_L*VV_junc2__q_us
    VV_junc2__H_mean = VV_junc2__RBC_volume/(VV_junc2__q_us+VV_junc2__div_0)
    VV_junc2__C_max123 = (VV_junc2__C_max12 if VV_junc2__C_max12 > PV3__C else (PV3__C if VV_junc2__C_max12 <= PV3__C else 0.0))
    VV_junc2__C = (VV_junc2__C_max123 if VV_junc2__C_max123 > PV4__C else (PV4__C if VV_junc2__C_max123 <= PV4__C else 0.0))
    PV3__RBC_volume_init = PV3__H_global_L*PV3__q_us
    PV3__H_mean = PV3__RBC_volume/PV3__q
    PV3__hem_dep_u_rel = 1+(PV3__mu_45-1)*(safe_power(1-PV3__H_mean, PV3__Z)-1)/(safe_power(1-PV3__H_global_L, PV3__Z)-1)*np.square(2*PV3__r*1e6/(2*PV3__r*1e6-1.1))
    PV3__u_mmHg = PV3__u/133.322
    PV4__RBC_volume_init = PV4__H_global_L*PV4__q_us
    PV4__H_mean = PV4__RBC_volume/PV4__q
    PV4__hem_dep_u_rel = 1+(PV4__mu_45-1)*(safe_power(1-PV4__H_mean, PV4__Z)-1)/(safe_power(1-PV4__H_global_L, PV4__Z)-1)*np.square(2*PV4__r*1e6/(2*PV4__r*1e6-1.1))
    PV4__u_mmHg = PV4__u/133.322
    V3__RBC_volume_init = V3__H_global_L*V3__q_us
    V3__H_mean = V3__RBC_volume/V3__q
    V3__hem_dep_u_rel = 1+(V3__mu_45-1)*(safe_power(1-V3__H_mean, V3__Z)-1)/(safe_power(1-V3__H_global_L, V3__Z)-1)*np.square(2*V3__r*1e6/(2*V3__r*1e6-1.1))
    V3__u_mmHg = V3__u/133.322
    V4__RBC_volume_init = V4__H_global_L*V4__q_us
    V4__H_mean = V4__RBC_volume/V4__q
    V4__hem_dep_u_rel = 1+(V4__mu_45-1)*(safe_power(1-V4__H_mean, V4__Z)-1)/(safe_power(1-V4__H_global_L, V4__Z)-1)*np.square(2*V4__r*1e6/(2*V4__r*1e6-1.1))
    V4__u_mmHg = V4__u/133.322
    VV_junc3__RBC_volume_init = VV_junc3__H_global_L*VV_junc3__q_us
    VV_junc3__H_mean = VV_junc3__RBC_volume/(VV_junc3__q_us+VV_junc3__div_0)
    VV_junc3__C_max123 = (VV_junc3__C_max12 if VV_junc3__C_max12 > PV5__C else (PV5__C if VV_junc3__C_max12 <= PV5__C else 0.0))
    VV_junc3__C = (VV_junc3__C_max123 if VV_junc3__C_max123 > PV6__C else (PV6__C if VV_junc3__C_max123 <= PV6__C else 0.0))
    PV5__RBC_volume_init = PV5__H_global_L*PV5__q_us
    PV5__H_mean = PV5__RBC_volume/PV5__q
    PV5__hem_dep_u_rel = 1+(PV5__mu_45-1)*(safe_power(1-PV5__H_mean, PV5__Z)-1)/(safe_power(1-PV5__H_global_L, PV5__Z)-1)*np.square(2*PV5__r*1e6/(2*PV5__r*1e6-1.1))
    PV5__u_mmHg = PV5__u/133.322
    PV6__RBC_volume_init = PV6__H_global_L*PV6__q_us
    PV6__H_mean = PV6__RBC_volume/PV6__q
    PV6__hem_dep_u_rel = 1+(PV6__mu_45-1)*(safe_power(1-PV6__H_mean, PV6__Z)-1)/(safe_power(1-PV6__H_global_L, PV6__Z)-1)*np.square(2*PV6__r*1e6/(2*PV6__r*1e6-1.1))
    PV6__u_mmHg = PV6__u/133.322
    V5__RBC_volume_init = V5__H_global_L*V5__q_us
    V5__H_mean = V5__RBC_volume/V5__q
    V5__hem_dep_u_rel = 1+(V5__mu_45-1)*(safe_power(1-V5__H_mean, V5__Z)-1)/(safe_power(1-V5__H_global_L, V5__Z)-1)*np.square(2*V5__r*1e6/(2*V5__r*1e6-1.1))
    V5__u_mmHg = V5__u/133.322
    V6__RBC_volume_init = V6__H_global_L*V6__q_us
    V6__H_mean = V6__RBC_volume/V6__q
    V6__hem_dep_u_rel = 1+(V6__mu_45-1)*(safe_power(1-V6__H_mean, V6__Z)-1)/(safe_power(1-V6__H_global_L, V6__Z)-1)*np.square(2*V6__r*1e6/(2*V6__r*1e6-1.1))
    V6__u_mmHg = V6__u/133.322
    inlet__mu = inlet__hem_dep_u_rel*inlet__mu_plasma
    inlet__R = 8*inlet__mu*inlet__l/(np.pi*safe_power(inlet__r, 4))
    inlet__v = (inlet__u_in-inlet__u)/(inlet__R/2)
    VV_junc1__u = VV_junc1__q_C/(VV_junc1__C/2)+VV_junc1__u_ext
    VV_junc1__u_mmHg = VV_junc1__u/133.322
    VV_junc1__u_d = VV_junc1__q_C_d/(VV_junc1__C/2)+VV_junc1__u_ext
    VV_junc1__u_d_mmHg = VV_junc1__u_d/133.322
    PV1__mu = PV1__hem_dep_u_rel*PV1__mu_plasma
    PV1__R = 8*PV1__mu*PV1__l/(np.pi*safe_power(PV1__r, 4))+PV1__R_constriction
    PV1__v = (VV_junc1__u_d-PV1__u)/(PV1__R/2)
    PV1__v_d = (PV1__u-V1__u)/(PV1__R/2)
    PV2__mu = PV2__hem_dep_u_rel*PV2__mu_plasma
    PV2__R = 8*PV2__mu*PV2__l/(np.pi*safe_power(PV2__r, 4))+PV2__R_constriction
    PV2__v = (VV_junc1__u_d-PV2__u)/(PV2__R/2)
    PV2__v_d = (PV2__u-V2__u)/(PV2__R/2)
    V1__mu = V1__hem_dep_u_rel*V1__mu_plasma
    V1__R = 8*V1__mu*V1__l/(np.pi*safe_power(V1__r, 4))
    V2__mu = V2__hem_dep_u_rel*V2__mu_plasma
    V2__R = 8*V2__mu*V2__l/(np.pi*safe_power(V2__r, 4))
    VV_junc2__u = VV_junc2__q_C/(VV_junc2__C/2)+VV_junc2__u_ext
    VV_junc2__u_mmHg = VV_junc2__u/133.322
    VV_junc2__u_d = VV_junc2__q_C_d/(VV_junc2__C/2)+VV_junc2__u_ext
    VV_junc2__u_d_mmHg = VV_junc2__u_d/133.322
    PV3__mu = PV3__hem_dep_u_rel*PV3__mu_plasma
    PV3__R = 8*PV3__mu*PV3__l/(np.pi*safe_power(PV3__r, 4))+PV3__R_constriction
    PV3__v = (VV_junc2__u_d-PV3__u)/(PV3__R/2)
    PV3__v_d = (PV3__u-V3__u)/(PV3__R/2)
    PV4__mu = PV4__hem_dep_u_rel*PV4__mu_plasma
    PV4__R = 8*PV4__mu*PV4__l/(np.pi*safe_power(PV4__r, 4))+PV4__R_constriction
    PV4__v = (VV_junc2__u_d-PV4__u)/(PV4__R/2)
    PV4__v_d = (PV4__u-V4__u)/(PV4__R/2)
    V3__mu = V3__hem_dep_u_rel*V3__mu_plasma
    V3__R = 8*V3__mu*V3__l/(np.pi*safe_power(V3__r, 4))
    V3__v = (V3__u-V3__u_out)/V3__R
    V4__mu = V4__hem_dep_u_rel*V4__mu_plasma
    V4__R = 8*V4__mu*V4__l/(np.pi*safe_power(V4__r, 4))
    V4__v = (V4__u-V4__u_out)/V4__R
    VV_junc3__u = VV_junc3__q_C/(VV_junc3__C/2)+VV_junc3__u_ext
    VV_junc3__u_mmHg = VV_junc3__u/133.322
    VV_junc3__u_d = VV_junc3__q_C_d/(VV_junc3__C/2)+VV_junc3__u_ext
    VV_junc3__u_d_mmHg = VV_junc3__u_d/133.322
    PV5__mu = PV5__hem_dep_u_rel*PV5__mu_plasma
    PV5__R = 8*PV5__mu*PV5__l/(np.pi*safe_power(PV5__r, 4))+PV5__R_constriction
    PV5__v = (VV_junc3__u_d-PV5__u)/(PV5__R/2)
    PV5__v_d = (PV5__u-V5__u)/(PV5__R/2)
    PV6__mu = PV6__hem_dep_u_rel*PV6__mu_plasma
    PV6__R = 8*PV6__mu*PV6__l/(np.pi*safe_power(PV6__r, 4))+PV6__R_constriction
    PV6__v = (VV_junc3__u_d-PV6__u)/(PV6__R/2)
    PV6__v_d = (PV6__u-V6__u)/(PV6__R/2)
    V5__mu = V5__hem_dep_u_rel*V5__mu_plasma
    V5__R = 8*V5__mu*V5__l/(np.pi*safe_power(V5__r, 4))
    V5__v = (V5__u-V5__u_out)/V5__R
    V6__mu = V6__hem_dep_u_rel*V6__mu_plasma
    V6__R = 8*V6__mu*V6__l/(np.pi*safe_power(V6__r, 4))
    V6__v = (V6__u-V6__u_out)/V6__R
    inlet__w_v = 0.5+1/np.pi*np.arctan(inlet__v/inlet__v_scale)
    inlet__v_pos = inlet__w_v*inlet__v
    inlet__v_neg = (1-inlet__w_v)*-inlet__v
    inlet__v_mm3_s = inlet__v/inlet__one_mm3
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
    PV1__w_v_d = 0.5+1/np.pi*np.arctan(PV1__v_d/PV1__v_scale)
    PV1__H_up = PV1__w_v_d*PV1__H_L_in+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__s_v_d = np.abs(PV1__v_d)/(np.abs(PV1__v_d)+PV1__v_eps)
    PV1__H_L_out = (1-PV1__w_v_d)*PV1__H_down+PV1__w_v_d*PV1__H_L_in
    PV1__H_R_out = PV1__w_v_d*PV1__H_down+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__v_pos = PV1__w_v*PV1__v
    PV1__v_neg = (1-PV1__w_v)*-PV1__v
    PV1__v_d_pos = PV1__w_v_d*PV1__v_d
    PV1__v_d_neg = (1-PV1__w_v_d)*-PV1__v_d
    PV1__H_volume_L = PV1__w_v*PV1__H_L_in+(1-PV1__w_v)*PV1__H_L_out
    PV1__H_volume_R = PV1__w_v_d*PV1__H_R_out+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__v_mm3_s = PV1__v/PV1__one_mm3
    PV1__v_d_mm3_s = PV1__v_d/PV1__one_mm3
    PV2__w_v = 0.5+1/np.pi*np.arctan(PV2__v/PV2__v_scale)
    PV2__w_v_d = 0.5+1/np.pi*np.arctan(PV2__v_d/PV2__v_scale)
    PV2__H_up = PV2__w_v_d*PV2__H_L_in+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__s_v_d = np.abs(PV2__v_d)/(np.abs(PV2__v_d)+PV2__v_eps)
    PV2__H_L_out = (1-PV2__w_v_d)*PV2__H_down+PV2__w_v_d*PV2__H_L_in
    PV2__H_R_out = PV2__w_v_d*PV2__H_down+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__v_pos = PV2__w_v*PV2__v
    PV2__v_neg = (1-PV2__w_v)*-PV2__v
    PV2__v_d_pos = PV2__w_v_d*PV2__v_d
    PV2__v_d_neg = (1-PV2__w_v_d)*-PV2__v_d
    PV2__H_volume_L = PV2__w_v*PV2__H_L_in+(1-PV2__w_v)*PV2__H_L_out
    PV2__H_volume_R = PV2__w_v_d*PV2__H_R_out+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__v_mm3_s = PV2__v/PV2__one_mm3
    PV2__v_d_mm3_s = PV2__v_d/PV2__one_mm3
    V1__v = (V1__u-VV_junc2__u)/V1__R
    V2__v = (V2__u-VV_junc3__u)/V2__R
    VV_junc2__vj1 = V1__v
    VV_junc2__vj3 = -PV3__v
    VV_junc2__vj4 = -PV4__v
    VV_junc2__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc2__vj1/VV_junc2__v_scale)
    VV_junc2__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc2__vj3/VV_junc2__v_scale)
    VV_junc2__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc2__vj4/VV_junc2__v_scale)
    VV_junc2__w_out1 = 1-VV_junc2__w_in1
    VV_junc2__w_out3 = 1-VV_junc2__w_in3
    VV_junc2__w_out4 = 1-VV_junc2__w_in4
    VV_junc2__Qin1 = VV_junc2__w_in1*VV_junc2__vj1
    VV_junc2__Qin3 = VV_junc2__w_in3*VV_junc2__vj3
    VV_junc2__Qin4 = VV_junc2__w_in4*VV_junc2__vj4
    VV_junc2__Qout1 = VV_junc2__w_out1*-VV_junc2__vj1
    VV_junc2__Qout3 = VV_junc2__w_out3*-VV_junc2__vj3
    VV_junc2__Qout4 = VV_junc2__w_out4*-VV_junc2__vj4
    VV_junc2__Qin_tot = VV_junc2__Qin1+VV_junc2__Qin2+VV_junc2__Qin3+VV_junc2__Qin4
    VV_junc2__Qout_tot = VV_junc2__Qout1+VV_junc2__Qout2+VV_junc2__Qout3+VV_junc2__Qout4
    VV_junc2__v = (VV_junc2__u-VV_junc2__u_d)/VV_junc2__R_VV_junc
    VV_junc2__bc1_is_in = (1 if VV_junc2__Qin1 > VV_junc2__v_threshold else 0)
    VV_junc2__bc3_is_in = (1 if VV_junc2__Qin3 > VV_junc2__v_threshold else 0)
    VV_junc2__bc4_is_in = (1 if VV_junc2__Qin4 > VV_junc2__v_threshold else 0)
    VV_junc2__bc1_is_out = (1 if VV_junc2__Qout1 > VV_junc2__v_threshold else 0)
    VV_junc2__bc3_is_out = (1 if VV_junc2__Qout3 > VV_junc2__v_threshold else 0)
    VV_junc2__bc4_is_out = (1 if VV_junc2__Qout4 > VV_junc2__v_threshold else 0)
    PV3__w_v = 0.5+1/np.pi*np.arctan(PV3__v/PV3__v_scale)
    PV3__w_v_d = 0.5+1/np.pi*np.arctan(PV3__v_d/PV3__v_scale)
    PV3__H_up = PV3__w_v_d*PV3__H_L_in+(1-PV3__w_v_d)*PV3__H_R_in
    PV3__s_v_d = np.abs(PV3__v_d)/(np.abs(PV3__v_d)+PV3__v_eps)
    PV3__H_L_out = (1-PV3__w_v_d)*PV3__H_down+PV3__w_v_d*PV3__H_L_in
    PV3__H_R_out = PV3__w_v_d*PV3__H_down+(1-PV3__w_v_d)*PV3__H_R_in
    PV3__v_pos = PV3__w_v*PV3__v
    PV3__v_neg = (1-PV3__w_v)*-PV3__v
    PV3__v_d_pos = PV3__w_v_d*PV3__v_d
    PV3__v_d_neg = (1-PV3__w_v_d)*-PV3__v_d
    PV3__H_volume_L = PV3__w_v*PV3__H_L_in+(1-PV3__w_v)*PV3__H_L_out
    PV3__H_volume_R = PV3__w_v_d*PV3__H_R_out+(1-PV3__w_v_d)*PV3__H_R_in
    PV3__v_mm3_s = PV3__v/PV3__one_mm3
    PV3__v_d_mm3_s = PV3__v_d/PV3__one_mm3
    PV4__w_v = 0.5+1/np.pi*np.arctan(PV4__v/PV4__v_scale)
    PV4__w_v_d = 0.5+1/np.pi*np.arctan(PV4__v_d/PV4__v_scale)
    PV4__H_up = PV4__w_v_d*PV4__H_L_in+(1-PV4__w_v_d)*PV4__H_R_in
    PV4__s_v_d = np.abs(PV4__v_d)/(np.abs(PV4__v_d)+PV4__v_eps)
    PV4__H_L_out = (1-PV4__w_v_d)*PV4__H_down+PV4__w_v_d*PV4__H_L_in
    PV4__H_R_out = PV4__w_v_d*PV4__H_down+(1-PV4__w_v_d)*PV4__H_R_in
    PV4__v_pos = PV4__w_v*PV4__v
    PV4__v_neg = (1-PV4__w_v)*-PV4__v
    PV4__v_d_pos = PV4__w_v_d*PV4__v_d
    PV4__v_d_neg = (1-PV4__w_v_d)*-PV4__v_d
    PV4__H_volume_L = PV4__w_v*PV4__H_L_in+(1-PV4__w_v)*PV4__H_L_out
    PV4__H_volume_R = PV4__w_v_d*PV4__H_R_out+(1-PV4__w_v_d)*PV4__H_R_in
    PV4__v_mm3_s = PV4__v/PV4__one_mm3
    PV4__v_d_mm3_s = PV4__v_d/PV4__one_mm3
    V3__w_v = 0.5+1/np.pi*np.arctan(V3__v/V3__v_scale)
    V3__H_up = V3__w_v*V3__H_L_in+(1-V3__w_v)*V3__H_R_in
    V3__s_v = np.abs(V3__v)/(np.abs(V3__v)+V3__v_eps)
    V3__H_L_out = (1-V3__w_v)*V3__H_down+V3__w_v*V3__H_L_in
    V3__H_R_out = V3__w_v*V3__H_down+(1-V3__w_v)*V3__H_R_in
    V3__v_pos = V3__w_v*V3__v
    V3__v_neg = (1-V3__w_v)*-V3__v
    V3__H_volume_L = V3__w_v*V3__H_L_in+(1-V3__w_v)*V3__H_L_out
    V3__H_volume_R = V3__w_v*V3__H_R_out+(1-V3__w_v)*V3__H_R_in
    V3__v_mm3_s = V3__v/V3__one_mm3
    V4__w_v = 0.5+1/np.pi*np.arctan(V4__v/V4__v_scale)
    V4__H_up = V4__w_v*V4__H_L_in+(1-V4__w_v)*V4__H_R_in
    V4__s_v = np.abs(V4__v)/(np.abs(V4__v)+V4__v_eps)
    V4__H_L_out = (1-V4__w_v)*V4__H_down+V4__w_v*V4__H_L_in
    V4__H_R_out = V4__w_v*V4__H_down+(1-V4__w_v)*V4__H_R_in
    V4__v_pos = V4__w_v*V4__v
    V4__v_neg = (1-V4__w_v)*-V4__v
    V4__H_volume_L = V4__w_v*V4__H_L_in+(1-V4__w_v)*V4__H_L_out
    V4__H_volume_R = V4__w_v*V4__H_R_out+(1-V4__w_v)*V4__H_R_in
    V4__v_mm3_s = V4__v/V4__one_mm3
    VV_junc3__vj1 = V2__v
    VV_junc3__vj3 = -PV5__v
    VV_junc3__vj4 = -PV6__v
    VV_junc3__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc3__vj1/VV_junc3__v_scale)
    VV_junc3__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc3__vj3/VV_junc3__v_scale)
    VV_junc3__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc3__vj4/VV_junc3__v_scale)
    VV_junc3__w_out1 = 1-VV_junc3__w_in1
    VV_junc3__w_out3 = 1-VV_junc3__w_in3
    VV_junc3__w_out4 = 1-VV_junc3__w_in4
    VV_junc3__Qin1 = VV_junc3__w_in1*VV_junc3__vj1
    VV_junc3__Qin3 = VV_junc3__w_in3*VV_junc3__vj3
    VV_junc3__Qin4 = VV_junc3__w_in4*VV_junc3__vj4
    VV_junc3__Qout1 = VV_junc3__w_out1*-VV_junc3__vj1
    VV_junc3__Qout3 = VV_junc3__w_out3*-VV_junc3__vj3
    VV_junc3__Qout4 = VV_junc3__w_out4*-VV_junc3__vj4
    VV_junc3__Qin_tot = VV_junc3__Qin1+VV_junc3__Qin2+VV_junc3__Qin3+VV_junc3__Qin4
    VV_junc3__Qout_tot = VV_junc3__Qout1+VV_junc3__Qout2+VV_junc3__Qout3+VV_junc3__Qout4
    VV_junc3__v = (VV_junc3__u-VV_junc3__u_d)/VV_junc3__R_VV_junc
    VV_junc3__bc1_is_in = (1 if VV_junc3__Qin1 > VV_junc3__v_threshold else 0)
    VV_junc3__bc3_is_in = (1 if VV_junc3__Qin3 > VV_junc3__v_threshold else 0)
    VV_junc3__bc4_is_in = (1 if VV_junc3__Qin4 > VV_junc3__v_threshold else 0)
    VV_junc3__bc1_is_out = (1 if VV_junc3__Qout1 > VV_junc3__v_threshold else 0)
    VV_junc3__bc3_is_out = (1 if VV_junc3__Qout3 > VV_junc3__v_threshold else 0)
    VV_junc3__bc4_is_out = (1 if VV_junc3__Qout4 > VV_junc3__v_threshold else 0)
    PV5__w_v = 0.5+1/np.pi*np.arctan(PV5__v/PV5__v_scale)
    PV5__w_v_d = 0.5+1/np.pi*np.arctan(PV5__v_d/PV5__v_scale)
    PV5__H_up = PV5__w_v_d*PV5__H_L_in+(1-PV5__w_v_d)*PV5__H_R_in
    PV5__s_v_d = np.abs(PV5__v_d)/(np.abs(PV5__v_d)+PV5__v_eps)
    PV5__H_L_out = (1-PV5__w_v_d)*PV5__H_down+PV5__w_v_d*PV5__H_L_in
    PV5__H_R_out = PV5__w_v_d*PV5__H_down+(1-PV5__w_v_d)*PV5__H_R_in
    PV5__v_pos = PV5__w_v*PV5__v
    PV5__v_neg = (1-PV5__w_v)*-PV5__v
    PV5__v_d_pos = PV5__w_v_d*PV5__v_d
    PV5__v_d_neg = (1-PV5__w_v_d)*-PV5__v_d
    PV5__H_volume_L = PV5__w_v*PV5__H_L_in+(1-PV5__w_v)*PV5__H_L_out
    PV5__H_volume_R = PV5__w_v_d*PV5__H_R_out+(1-PV5__w_v_d)*PV5__H_R_in
    PV5__v_mm3_s = PV5__v/PV5__one_mm3
    PV5__v_d_mm3_s = PV5__v_d/PV5__one_mm3
    PV6__w_v = 0.5+1/np.pi*np.arctan(PV6__v/PV6__v_scale)
    PV6__w_v_d = 0.5+1/np.pi*np.arctan(PV6__v_d/PV6__v_scale)
    PV6__H_up = PV6__w_v_d*PV6__H_L_in+(1-PV6__w_v_d)*PV6__H_R_in
    PV6__s_v_d = np.abs(PV6__v_d)/(np.abs(PV6__v_d)+PV6__v_eps)
    PV6__H_L_out = (1-PV6__w_v_d)*PV6__H_down+PV6__w_v_d*PV6__H_L_in
    PV6__H_R_out = PV6__w_v_d*PV6__H_down+(1-PV6__w_v_d)*PV6__H_R_in
    PV6__v_pos = PV6__w_v*PV6__v
    PV6__v_neg = (1-PV6__w_v)*-PV6__v
    PV6__v_d_pos = PV6__w_v_d*PV6__v_d
    PV6__v_d_neg = (1-PV6__w_v_d)*-PV6__v_d
    PV6__H_volume_L = PV6__w_v*PV6__H_L_in+(1-PV6__w_v)*PV6__H_L_out
    PV6__H_volume_R = PV6__w_v_d*PV6__H_R_out+(1-PV6__w_v_d)*PV6__H_R_in
    PV6__v_mm3_s = PV6__v/PV6__one_mm3
    PV6__v_d_mm3_s = PV6__v_d/PV6__one_mm3
    V5__w_v = 0.5+1/np.pi*np.arctan(V5__v/V5__v_scale)
    V5__H_up = V5__w_v*V5__H_L_in+(1-V5__w_v)*V5__H_R_in
    V5__s_v = np.abs(V5__v)/(np.abs(V5__v)+V5__v_eps)
    V5__H_L_out = (1-V5__w_v)*V5__H_down+V5__w_v*V5__H_L_in
    V5__H_R_out = V5__w_v*V5__H_down+(1-V5__w_v)*V5__H_R_in
    V5__v_pos = V5__w_v*V5__v
    V5__v_neg = (1-V5__w_v)*-V5__v
    V5__H_volume_L = V5__w_v*V5__H_L_in+(1-V5__w_v)*V5__H_L_out
    V5__H_volume_R = V5__w_v*V5__H_R_out+(1-V5__w_v)*V5__H_R_in
    V5__v_mm3_s = V5__v/V5__one_mm3
    V6__w_v = 0.5+1/np.pi*np.arctan(V6__v/V6__v_scale)
    V6__H_up = V6__w_v*V6__H_L_in+(1-V6__w_v)*V6__H_R_in
    V6__s_v = np.abs(V6__v)/(np.abs(V6__v)+V6__v_eps)
    V6__H_L_out = (1-V6__w_v)*V6__H_down+V6__w_v*V6__H_L_in
    V6__H_R_out = V6__w_v*V6__H_down+(1-V6__w_v)*V6__H_R_in
    V6__v_pos = V6__w_v*V6__v
    V6__v_neg = (1-V6__w_v)*-V6__v
    V6__H_volume_L = V6__w_v*V6__H_L_in+(1-V6__w_v)*V6__H_L_out
    V6__H_volume_R = V6__w_v*V6__H_R_out+(1-V6__w_v)*V6__H_R_in
    V6__v_mm3_s = V6__v/V6__one_mm3
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
    PV1__H_down_target = PV1__s_v_d*(PV1__H_mean+PV1__gamma_mirror*(PV1__H_mean-PV1__H_up))+(1-PV1__s_v_d)*PV1__H_mean
    PV2__H_down_target = PV2__s_v_d*(PV2__H_mean+PV2__gamma_mirror*(PV2__H_mean-PV2__H_up))+(1-PV2__s_v_d)*PV2__H_mean
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
    VV_junc2__n_in = VV_junc2__bc1_is_in+VV_junc2__bc2_is_in+VV_junc2__bc3_is_in+VV_junc2__bc4_is_in
    VV_junc2__n_out = VV_junc2__bc1_is_out+VV_junc2__bc2_is_out+VV_junc2__bc3_is_out+VV_junc2__bc4_is_out
    VV_junc2__RBC_in = VV_junc2__Qin1*V1__H_R_out+VV_junc2__Qin2*VV_junc2__H_to2+VV_junc2__Qin3*PV3__H_L_out+VV_junc2__Qin4*PV4__H_L_out
    VV_junc2__v_mm3_s = VV_junc2__v/VV_junc2__one_mm3
    VV_junc2__junction_type = (1 if VV_junc2__n_in == 1 else (-1 if VV_junc2__n_in >= 2 else 0))
    VV_junc2__is_split = (1 if VV_junc2__junction_type == 1 else 0)
    VV_junc2__is_merge = (1 if VV_junc2__junction_type == -1 else 0)
    VV_junc2__feed1 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin1 >= VV_junc2__Qin2) and (VV_junc2__Qin1 >= VV_junc2__Qin3) and (VV_junc2__Qin1 >= VV_junc2__Qin4) else 0)
    VV_junc2__feed2 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin2 > VV_junc2__Qin1) and (VV_junc2__Qin2 >= VV_junc2__Qin3) and (VV_junc2__Qin2 >= VV_junc2__Qin4) else 0)
    VV_junc2__feed3 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin3 > VV_junc2__Qin1) and (VV_junc2__Qin3 > VV_junc2__Qin2) and (VV_junc2__Qin3 >= VV_junc2__Qin4) else 0)
    VV_junc2__feed4 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__Qin4 > VV_junc2__Qin1) and (VV_junc2__Qin4 > VV_junc2__Qin2) and (VV_junc2__Qin4 > VV_junc2__Qin3) else 0)
    VV_junc2__alpha1 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc1_is_out == 1) and (VV_junc2__Qout1 >= VV_junc2__Qout2) and (VV_junc2__Qout1 >= VV_junc2__Qout3) and (VV_junc2__Qout1 >= VV_junc2__Qout4) else 0)
    VV_junc2__alpha2 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc2_is_out == 1) and (VV_junc2__Qout2 > VV_junc2__Qout1) and (VV_junc2__Qout2 >= VV_junc2__Qout3) and (VV_junc2__Qout2 >= VV_junc2__Qout4) else 0)
    VV_junc2__alpha3 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc3_is_out == 1) and (VV_junc2__Qout3 > VV_junc2__Qout1) and (VV_junc2__Qout3 > VV_junc2__Qout2) and (VV_junc2__Qout3 >= VV_junc2__Qout4) else 0)
    VV_junc2__alpha4 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc4_is_out == 1) and (VV_junc2__Qout4 > VV_junc2__Qout1) and (VV_junc2__Qout4 > VV_junc2__Qout2) and (VV_junc2__Qout4 > VV_junc2__Qout3) else 0)
    VV_junc2__Qout1_rem = (0 if VV_junc2__alpha1 == 1 else VV_junc2__Qout1)
    VV_junc2__Qout2_rem = (0 if VV_junc2__alpha2 == 1 else VV_junc2__Qout2)
    VV_junc2__Qout3_rem = (0 if VV_junc2__alpha3 == 1 else VV_junc2__Qout3)
    VV_junc2__Qout4_rem = (0 if VV_junc2__alpha4 == 1 else VV_junc2__Qout4)
    VV_junc2__beta1 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc1_is_out == 1) and (VV_junc2__alpha1 == 0) and (VV_junc2__Qout1_rem >= VV_junc2__Qout2_rem) and (VV_junc2__Qout1_rem >= VV_junc2__Qout3_rem) and (VV_junc2__Qout1_rem >= VV_junc2__Qout4_rem) else 0)
    VV_junc2__beta2 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc2_is_out == 1) and (VV_junc2__alpha2 == 0) and (VV_junc2__Qout2_rem > VV_junc2__Qout1_rem) and (VV_junc2__Qout2_rem >= VV_junc2__Qout3_rem) and (VV_junc2__Qout2_rem >= VV_junc2__Qout4_rem) else 0)
    VV_junc2__beta3 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc3_is_out == 1) and (VV_junc2__alpha3 == 0) and (VV_junc2__Qout3_rem > VV_junc2__Qout1_rem) and (VV_junc2__Qout3_rem > VV_junc2__Qout2_rem) and (VV_junc2__Qout3_rem >= VV_junc2__Qout4_rem) else 0)
    VV_junc2__beta4 = (1 if (VV_junc2__is_split == 1) and (VV_junc2__bc4_is_out == 1) and (VV_junc2__alpha4 == 0) and (VV_junc2__Qout4_rem > VV_junc2__Qout1_rem) and (VV_junc2__Qout4_rem > VV_junc2__Qout2_rem) and (VV_junc2__Qout4_rem > VV_junc2__Qout3_rem) else 0)
    VV_junc2__D_F = (VV_junc2__D1 if VV_junc2__feed1 == 1 else (VV_junc2__D2 if VV_junc2__feed2 == 1 else (VV_junc2__D3 if VV_junc2__feed3 == 1 else (VV_junc2__D4 if VV_junc2__feed4 == 1 else VV_junc2__D1))))
    VV_junc2__D_alpha = (VV_junc2__D1 if VV_junc2__alpha1 == 1 else (VV_junc2__D2 if VV_junc2__alpha2 == 1 else (VV_junc2__D3 if VV_junc2__alpha3 == 1 else (VV_junc2__D4 if VV_junc2__alpha4 == 1 else VV_junc2__D3))))
    VV_junc2__D_beta = (VV_junc2__D1 if VV_junc2__beta1 == 1 else (VV_junc2__D2 if VV_junc2__beta2 == 1 else (VV_junc2__D3 if VV_junc2__beta3 == 1 else (VV_junc2__D4 if VV_junc2__beta4 == 1 else VV_junc2__D4))))
    VV_junc2__v_alpha = (VV_junc2__Qout1 if VV_junc2__alpha1 == 1 else (VV_junc2__Qout2 if VV_junc2__alpha2 == 1 else (VV_junc2__Qout3 if VV_junc2__alpha3 == 1 else (VV_junc2__Qout4 if VV_junc2__alpha4 == 1 else 0))))
    VV_junc2__v_beta = (VV_junc2__Qout1 if VV_junc2__beta1 == 1 else (VV_junc2__Qout2 if VV_junc2__beta2 == 1 else (VV_junc2__Qout3 if VV_junc2__beta3 == 1 else (VV_junc2__Qout4 if VV_junc2__beta4 == 1 else 0))))
    PV3__H_down_target = PV3__s_v_d*(PV3__H_mean+PV3__gamma_mirror*(PV3__H_mean-PV3__H_up))+(1-PV3__s_v_d)*PV3__H_mean
    PV4__H_down_target = PV4__s_v_d*(PV4__H_mean+PV4__gamma_mirror*(PV4__H_mean-PV4__H_up))+(1-PV4__s_v_d)*PV4__H_mean
    V3__H_down_target = V3__s_v*(V3__H_mean+V3__gamma_mirror*(V3__H_mean-V3__H_up))+(1-V3__s_v)*V3__H_mean
    V4__H_down_target = V4__s_v*(V4__H_mean+V4__gamma_mirror*(V4__H_mean-V4__H_up))+(1-V4__s_v)*V4__H_mean
    VV_junc3__n_in = VV_junc3__bc1_is_in+VV_junc3__bc2_is_in+VV_junc3__bc3_is_in+VV_junc3__bc4_is_in
    VV_junc3__n_out = VV_junc3__bc1_is_out+VV_junc3__bc2_is_out+VV_junc3__bc3_is_out+VV_junc3__bc4_is_out
    VV_junc3__RBC_in = VV_junc3__Qin1*V2__H_R_out+VV_junc3__Qin2*VV_junc3__H_to2+VV_junc3__Qin3*PV5__H_L_out+VV_junc3__Qin4*PV6__H_L_out
    VV_junc3__v_mm3_s = VV_junc3__v/VV_junc3__one_mm3
    VV_junc3__junction_type = (1 if VV_junc3__n_in == 1 else (-1 if VV_junc3__n_in >= 2 else 0))
    VV_junc3__is_split = (1 if VV_junc3__junction_type == 1 else 0)
    VV_junc3__is_merge = (1 if VV_junc3__junction_type == -1 else 0)
    VV_junc3__feed1 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin1 >= VV_junc3__Qin2) and (VV_junc3__Qin1 >= VV_junc3__Qin3) and (VV_junc3__Qin1 >= VV_junc3__Qin4) else 0)
    VV_junc3__feed2 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin2 > VV_junc3__Qin1) and (VV_junc3__Qin2 >= VV_junc3__Qin3) and (VV_junc3__Qin2 >= VV_junc3__Qin4) else 0)
    VV_junc3__feed3 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin3 > VV_junc3__Qin1) and (VV_junc3__Qin3 > VV_junc3__Qin2) and (VV_junc3__Qin3 >= VV_junc3__Qin4) else 0)
    VV_junc3__feed4 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__Qin4 > VV_junc3__Qin1) and (VV_junc3__Qin4 > VV_junc3__Qin2) and (VV_junc3__Qin4 > VV_junc3__Qin3) else 0)
    VV_junc3__alpha1 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc1_is_out == 1) and (VV_junc3__Qout1 >= VV_junc3__Qout2) and (VV_junc3__Qout1 >= VV_junc3__Qout3) and (VV_junc3__Qout1 >= VV_junc3__Qout4) else 0)
    VV_junc3__alpha2 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc2_is_out == 1) and (VV_junc3__Qout2 > VV_junc3__Qout1) and (VV_junc3__Qout2 >= VV_junc3__Qout3) and (VV_junc3__Qout2 >= VV_junc3__Qout4) else 0)
    VV_junc3__alpha3 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc3_is_out == 1) and (VV_junc3__Qout3 > VV_junc3__Qout1) and (VV_junc3__Qout3 > VV_junc3__Qout2) and (VV_junc3__Qout3 >= VV_junc3__Qout4) else 0)
    VV_junc3__alpha4 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc4_is_out == 1) and (VV_junc3__Qout4 > VV_junc3__Qout1) and (VV_junc3__Qout4 > VV_junc3__Qout2) and (VV_junc3__Qout4 > VV_junc3__Qout3) else 0)
    VV_junc3__Qout1_rem = (0 if VV_junc3__alpha1 == 1 else VV_junc3__Qout1)
    VV_junc3__Qout2_rem = (0 if VV_junc3__alpha2 == 1 else VV_junc3__Qout2)
    VV_junc3__Qout3_rem = (0 if VV_junc3__alpha3 == 1 else VV_junc3__Qout3)
    VV_junc3__Qout4_rem = (0 if VV_junc3__alpha4 == 1 else VV_junc3__Qout4)
    VV_junc3__beta1 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc1_is_out == 1) and (VV_junc3__alpha1 == 0) and (VV_junc3__Qout1_rem >= VV_junc3__Qout2_rem) and (VV_junc3__Qout1_rem >= VV_junc3__Qout3_rem) and (VV_junc3__Qout1_rem >= VV_junc3__Qout4_rem) else 0)
    VV_junc3__beta2 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc2_is_out == 1) and (VV_junc3__alpha2 == 0) and (VV_junc3__Qout2_rem > VV_junc3__Qout1_rem) and (VV_junc3__Qout2_rem >= VV_junc3__Qout3_rem) and (VV_junc3__Qout2_rem >= VV_junc3__Qout4_rem) else 0)
    VV_junc3__beta3 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc3_is_out == 1) and (VV_junc3__alpha3 == 0) and (VV_junc3__Qout3_rem > VV_junc3__Qout1_rem) and (VV_junc3__Qout3_rem > VV_junc3__Qout2_rem) and (VV_junc3__Qout3_rem >= VV_junc3__Qout4_rem) else 0)
    VV_junc3__beta4 = (1 if (VV_junc3__is_split == 1) and (VV_junc3__bc4_is_out == 1) and (VV_junc3__alpha4 == 0) and (VV_junc3__Qout4_rem > VV_junc3__Qout1_rem) and (VV_junc3__Qout4_rem > VV_junc3__Qout2_rem) and (VV_junc3__Qout4_rem > VV_junc3__Qout3_rem) else 0)
    VV_junc3__D_F = (VV_junc3__D1 if VV_junc3__feed1 == 1 else (VV_junc3__D2 if VV_junc3__feed2 == 1 else (VV_junc3__D3 if VV_junc3__feed3 == 1 else (VV_junc3__D4 if VV_junc3__feed4 == 1 else VV_junc3__D1))))
    VV_junc3__D_alpha = (VV_junc3__D1 if VV_junc3__alpha1 == 1 else (VV_junc3__D2 if VV_junc3__alpha2 == 1 else (VV_junc3__D3 if VV_junc3__alpha3 == 1 else (VV_junc3__D4 if VV_junc3__alpha4 == 1 else VV_junc3__D3))))
    VV_junc3__D_beta = (VV_junc3__D1 if VV_junc3__beta1 == 1 else (VV_junc3__D2 if VV_junc3__beta2 == 1 else (VV_junc3__D3 if VV_junc3__beta3 == 1 else (VV_junc3__D4 if VV_junc3__beta4 == 1 else VV_junc3__D4))))
    VV_junc3__v_alpha = (VV_junc3__Qout1 if VV_junc3__alpha1 == 1 else (VV_junc3__Qout2 if VV_junc3__alpha2 == 1 else (VV_junc3__Qout3 if VV_junc3__alpha3 == 1 else (VV_junc3__Qout4 if VV_junc3__alpha4 == 1 else 0))))
    VV_junc3__v_beta = (VV_junc3__Qout1 if VV_junc3__beta1 == 1 else (VV_junc3__Qout2 if VV_junc3__beta2 == 1 else (VV_junc3__Qout3 if VV_junc3__beta3 == 1 else (VV_junc3__Qout4 if VV_junc3__beta4 == 1 else 0))))
    PV5__H_down_target = PV5__s_v_d*(PV5__H_mean+PV5__gamma_mirror*(PV5__H_mean-PV5__H_up))+(1-PV5__s_v_d)*PV5__H_mean
    PV6__H_down_target = PV6__s_v_d*(PV6__H_mean+PV6__gamma_mirror*(PV6__H_mean-PV6__H_up))+(1-PV6__s_v_d)*PV6__H_mean
    V5__H_down_target = V5__s_v*(V5__H_mean+V5__gamma_mirror*(V5__H_mean-V5__H_up))+(1-V5__s_v)*V5__H_mean
    V6__H_down_target = V6__s_v*(V6__H_mean+V6__gamma_mirror*(V6__H_mean-V6__H_up))+(1-V6__s_v)*V6__H_mean
    inlet__H_down_target = inlet__s_v_d*(inlet__H_mean+inlet__gamma_mirror*(inlet__H_mean-inlet__H_up))+(1-inlet__s_v_d)*inlet__H_mean
    VV_junc1__FQB_alpha = (VV_junc1__v_alpha+VV_junc1__div_0)/(VV_junc1__v_alpha+VV_junc1__v_beta+2*VV_junc1__div_0)
    VV_junc1__B = 1+6.98*(1-VV_junc1__H_mean)/(VV_junc1__D_F*1e6)
    VV_junc1__A = -6.96*np.log(VV_junc1__D_alpha*1e6/(VV_junc1__D_beta*1e6))/(VV_junc1__D_F*1e6)
    VV_junc1__X_0 = 0.4/(VV_junc1__D_F*1e6)
    VV_junc1__y_raw = (VV_junc1__FQB_alpha-VV_junc1__X_0)/(1-2*VV_junc1__X_0+VV_junc1__div_0)
    VV_junc1__y = min(max(VV_junc1__y_raw, VV_junc1__div_0y), 1-VV_junc1__div_0y)
    V1__H_down_target = V1__s_v*(V1__H_mean+V1__gamma_mirror*(V1__H_mean-V1__H_up))+(1-V1__s_v)*V1__H_mean
    V2__H_down_target = V2__s_v*(V2__H_mean+V2__gamma_mirror*(V2__H_mean-V2__H_up))+(1-V2__s_v)*V2__H_mean
    VV_junc2__FQB_alpha = (VV_junc2__v_alpha+VV_junc2__div_0)/(VV_junc2__v_alpha+VV_junc2__v_beta+2*VV_junc2__div_0)
    VV_junc2__B = 1+6.98*(1-VV_junc2__H_mean)/(VV_junc2__D_F*1e6)
    VV_junc2__A = -6.96*np.log(VV_junc2__D_alpha*1e6/(VV_junc2__D_beta*1e6))/(VV_junc2__D_F*1e6)
    VV_junc2__X_0 = 0.4/(VV_junc2__D_F*1e6)
    VV_junc2__y_raw = (VV_junc2__FQB_alpha-VV_junc2__X_0)/(1-2*VV_junc2__X_0+VV_junc2__div_0)
    VV_junc2__y = min(max(VV_junc2__y_raw, VV_junc2__div_0y), 1-VV_junc2__div_0y)
    VV_junc3__FQB_alpha = (VV_junc3__v_alpha+VV_junc3__div_0)/(VV_junc3__v_alpha+VV_junc3__v_beta+2*VV_junc3__div_0)
    VV_junc3__B = 1+6.98*(1-VV_junc3__H_mean)/(VV_junc3__D_F*1e6)
    VV_junc3__A = -6.96*np.log(VV_junc3__D_alpha*1e6/(VV_junc3__D_beta*1e6))/(VV_junc3__D_F*1e6)
    VV_junc3__X_0 = 0.4/(VV_junc3__D_F*1e6)
    VV_junc3__y_raw = (VV_junc3__FQB_alpha-VV_junc3__X_0)/(1-2*VV_junc3__X_0+VV_junc3__div_0)
    VV_junc3__y = min(max(VV_junc3__y_raw, VV_junc3__div_0y), 1-VV_junc3__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc2__ph = np.log(VV_junc2__y/(1-VV_junc2__y))
    VV_junc3__ph = np.log(VV_junc3__y/(1-VV_junc3__y))
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
    VV_junc2__FQE_alpha = 1/(1+np.exp(-(VV_junc2__A+VV_junc2__B*VV_junc2__ph)))
    VV_junc2__H_VV_out_alpha = VV_junc2__H_mean*VV_junc2__FQE_alpha/(VV_junc2__FQB_alpha+VV_junc2__div_0)
    VV_junc2__H_VV_out_beta = VV_junc2__H_mean*(1-VV_junc2__FQE_alpha)/(1-VV_junc2__FQB_alpha+VV_junc2__div_0)
    VV_junc2__H_split1 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha1 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta1 == 1 else V1__H_R_out))
    VV_junc2__H_split2 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha2 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta2 == 1 else VV_junc2__H_to2))
    VV_junc2__H_split3 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha3 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta3 == 1 else PV3__H_L_out))
    VV_junc2__H_split4 = (VV_junc2__H_VV_out_alpha if VV_junc2__alpha4 == 1 else (VV_junc2__H_VV_out_beta if VV_junc2__beta4 == 1 else PV4__H_L_out))
    VV_junc2__H_daughter1 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split1 if VV_junc2__is_split == 1 else V1__H_R_out))
    VV_junc2__H_daughter2 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split2 if VV_junc2__is_split == 1 else VV_junc2__H_to2))
    VV_junc2__H_daughter3 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split3 if VV_junc2__is_split == 1 else PV3__H_L_out))
    VV_junc2__H_daughter4 = (VV_junc2__H_mean if VV_junc2__is_merge == 1 else (VV_junc2__H_split4 if VV_junc2__is_split == 1 else PV4__H_L_out))
    VV_junc2__H_from1_target = (VV_junc2__H_daughter1 if VV_junc2__bc1_is_out == 1 else V1__H_R_out)
    VV_junc2__H_from2_target = (VV_junc2__H_daughter2 if VV_junc2__bc2_is_out == 1 else VV_junc2__H_to2)
    VV_junc2__H_from3_target = (VV_junc2__H_daughter3 if VV_junc2__bc3_is_out == 1 else PV3__H_L_out)
    VV_junc2__H_from4_target = (VV_junc2__H_daughter4 if VV_junc2__bc4_is_out == 1 else PV4__H_L_out)
    VV_junc3__FQE_alpha = 1/(1+np.exp(-(VV_junc3__A+VV_junc3__B*VV_junc3__ph)))
    VV_junc3__H_VV_out_alpha = VV_junc3__H_mean*VV_junc3__FQE_alpha/(VV_junc3__FQB_alpha+VV_junc3__div_0)
    VV_junc3__H_VV_out_beta = VV_junc3__H_mean*(1-VV_junc3__FQE_alpha)/(1-VV_junc3__FQB_alpha+VV_junc3__div_0)
    VV_junc3__H_split1 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha1 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta1 == 1 else V2__H_R_out))
    VV_junc3__H_split2 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha2 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta2 == 1 else VV_junc3__H_to2))
    VV_junc3__H_split3 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha3 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta3 == 1 else PV5__H_L_out))
    VV_junc3__H_split4 = (VV_junc3__H_VV_out_alpha if VV_junc3__alpha4 == 1 else (VV_junc3__H_VV_out_beta if VV_junc3__beta4 == 1 else PV6__H_L_out))
    VV_junc3__H_daughter1 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split1 if VV_junc3__is_split == 1 else V2__H_R_out))
    VV_junc3__H_daughter2 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split2 if VV_junc3__is_split == 1 else VV_junc3__H_to2))
    VV_junc3__H_daughter3 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split3 if VV_junc3__is_split == 1 else PV5__H_L_out))
    VV_junc3__H_daughter4 = (VV_junc3__H_mean if VV_junc3__is_merge == 1 else (VV_junc3__H_split4 if VV_junc3__is_split == 1 else PV6__H_L_out))
    VV_junc3__H_from1_target = (VV_junc3__H_daughter1 if VV_junc3__bc1_is_out == 1 else V2__H_R_out)
    VV_junc3__H_from2_target = (VV_junc3__H_daughter2 if VV_junc3__bc2_is_out == 1 else VV_junc3__H_to2)
    VV_junc3__H_from3_target = (VV_junc3__H_daughter3 if VV_junc3__bc3_is_out == 1 else PV5__H_L_out)
    VV_junc3__H_from4_target = (VV_junc3__H_daughter4 if VV_junc3__bc4_is_out == 1 else PV6__H_L_out)
    VV_junc1__H_from1 = VV_junc1__w_out1*VV_junc1__H_from1_target
    VV_junc1__H_from2 = VV_junc1__w_out2*VV_junc1__H_from2_target
    VV_junc1__H_from3 = VV_junc1__w_out3*VV_junc1__H_from3_target
    VV_junc1__H_from4 = VV_junc1__w_out4*VV_junc1__H_from4_target
    VV_junc1__RBC_out = VV_junc1__Qout1*VV_junc1__H_from1+VV_junc1__Qout2*VV_junc1__H_from2+VV_junc1__Qout3*VV_junc1__H_from3+VV_junc1__Qout4*VV_junc1__H_from4
    VV_junc2__H_from1 = VV_junc2__w_out1*VV_junc2__H_from1_target
    VV_junc2__H_from2 = VV_junc2__w_out2*VV_junc2__H_from2_target
    VV_junc2__H_from3 = VV_junc2__w_out3*VV_junc2__H_from3_target
    VV_junc2__H_from4 = VV_junc2__w_out4*VV_junc2__H_from4_target
    VV_junc2__RBC_out = VV_junc2__Qout1*VV_junc2__H_from1+VV_junc2__Qout2*VV_junc2__H_from2+VV_junc2__Qout3*VV_junc2__H_from3+VV_junc2__Qout4*VV_junc2__H_from4
    VV_junc3__H_from1 = VV_junc3__w_out1*VV_junc3__H_from1_target
    VV_junc3__H_from2 = VV_junc3__w_out2*VV_junc3__H_from2_target
    VV_junc3__H_from3 = VV_junc3__w_out3*VV_junc3__H_from3_target
    VV_junc3__H_from4 = VV_junc3__w_out4*VV_junc3__H_from4_target
    VV_junc3__RBC_out = VV_junc3__Qout1*VV_junc3__H_from1+VV_junc3__Qout2*VV_junc3__H_from2+VV_junc3__Qout3*VV_junc3__H_from3+VV_junc3__Qout4*VV_junc3__H_from4

    # Return dictionary of all algebraic variables
    return {
        "inlet__H_L_in": inlet__H_L_in,
        "inlet__H_R_in": inlet__H_R_in,
        "inlet__q_us": inlet__q_us,
        "inlet__q": inlet__q,
        "inlet__C": inlet__C,
        "inlet__Z": inlet__Z,
        "inlet__mu_45": inlet__mu_45,
        "inlet__u": inlet__u,
        "VV_junc1__vj2": VV_junc1__vj2,
        "VV_junc1__D1": VV_junc1__D1,
        "VV_junc1__D2": VV_junc1__D2,
        "VV_junc1__D3": VV_junc1__D3,
        "VV_junc1__D4": VV_junc1__D4,
        "VV_junc1__w_in2": VV_junc1__w_in2,
        "VV_junc1__w_out2": VV_junc1__w_out2,
        "VV_junc1__Qin2": VV_junc1__Qin2,
        "VV_junc1__Qout2": VV_junc1__Qout2,
        "VV_junc1__q_us": VV_junc1__q_us,
        "VV_junc1__q": VV_junc1__q,
        "VV_junc1__bc2_is_in": VV_junc1__bc2_is_in,
        "VV_junc1__bc2_is_out": VV_junc1__bc2_is_out,
        "VV_junc1__C_max12": VV_junc1__C_max12,
        "PV1__R_constriction": PV1__R_constriction,
        "PV1__H_L_in": PV1__H_L_in,
        "PV1__H_R_in": PV1__H_R_in,
        "PV1__q_us": PV1__q_us,
        "PV1__q": PV1__q,
        "PV1__C": PV1__C,
        "PV1__Z": PV1__Z,
        "PV1__mu_45": PV1__mu_45,
        "PV1__u": PV1__u,
        "PV2__R_constriction": PV2__R_constriction,
        "PV2__H_L_in": PV2__H_L_in,
        "PV2__H_R_in": PV2__H_R_in,
        "PV2__q_us": PV2__q_us,
        "PV2__q": PV2__q,
        "PV2__C": PV2__C,
        "PV2__Z": PV2__Z,
        "PV2__mu_45": PV2__mu_45,
        "PV2__u": PV2__u,
        "V1__H_L_in": V1__H_L_in,
        "V1__H_R_in": V1__H_R_in,
        "V1__q_us": V1__q_us,
        "V1__q": V1__q,
        "V1__C": V1__C,
        "V1__Z": V1__Z,
        "V1__mu_45": V1__mu_45,
        "V1__u": V1__u,
        "V2__H_L_in": V2__H_L_in,
        "V2__H_R_in": V2__H_R_in,
        "V2__q_us": V2__q_us,
        "V2__q": V2__q,
        "V2__C": V2__C,
        "V2__Z": V2__Z,
        "V2__mu_45": V2__mu_45,
        "V2__u": V2__u,
        "VV_junc2__vj2": VV_junc2__vj2,
        "VV_junc2__D1": VV_junc2__D1,
        "VV_junc2__D2": VV_junc2__D2,
        "VV_junc2__D3": VV_junc2__D3,
        "VV_junc2__D4": VV_junc2__D4,
        "VV_junc2__w_in2": VV_junc2__w_in2,
        "VV_junc2__w_out2": VV_junc2__w_out2,
        "VV_junc2__Qin2": VV_junc2__Qin2,
        "VV_junc2__Qout2": VV_junc2__Qout2,
        "VV_junc2__q_us": VV_junc2__q_us,
        "VV_junc2__q": VV_junc2__q,
        "VV_junc2__bc2_is_in": VV_junc2__bc2_is_in,
        "VV_junc2__bc2_is_out": VV_junc2__bc2_is_out,
        "VV_junc2__C_max12": VV_junc2__C_max12,
        "PV3__R_constriction": PV3__R_constriction,
        "PV3__H_L_in": PV3__H_L_in,
        "PV3__H_R_in": PV3__H_R_in,
        "PV3__q_us": PV3__q_us,
        "PV3__q": PV3__q,
        "PV3__C": PV3__C,
        "PV3__Z": PV3__Z,
        "PV3__mu_45": PV3__mu_45,
        "PV3__u": PV3__u,
        "PV4__R_constriction": PV4__R_constriction,
        "PV4__H_L_in": PV4__H_L_in,
        "PV4__H_R_in": PV4__H_R_in,
        "PV4__q_us": PV4__q_us,
        "PV4__q": PV4__q,
        "PV4__C": PV4__C,
        "PV4__Z": PV4__Z,
        "PV4__mu_45": PV4__mu_45,
        "PV4__u": PV4__u,
        "V3__H_L_in": V3__H_L_in,
        "V3__H_R_in": V3__H_R_in,
        "V3__q_us": V3__q_us,
        "V3__q": V3__q,
        "V3__C": V3__C,
        "V3__Z": V3__Z,
        "V3__mu_45": V3__mu_45,
        "V3__u": V3__u,
        "V4__H_L_in": V4__H_L_in,
        "V4__H_R_in": V4__H_R_in,
        "V4__q_us": V4__q_us,
        "V4__q": V4__q,
        "V4__C": V4__C,
        "V4__Z": V4__Z,
        "V4__mu_45": V4__mu_45,
        "V4__u": V4__u,
        "VV_junc3__vj2": VV_junc3__vj2,
        "VV_junc3__D1": VV_junc3__D1,
        "VV_junc3__D2": VV_junc3__D2,
        "VV_junc3__D3": VV_junc3__D3,
        "VV_junc3__D4": VV_junc3__D4,
        "VV_junc3__w_in2": VV_junc3__w_in2,
        "VV_junc3__w_out2": VV_junc3__w_out2,
        "VV_junc3__Qin2": VV_junc3__Qin2,
        "VV_junc3__Qout2": VV_junc3__Qout2,
        "VV_junc3__q_us": VV_junc3__q_us,
        "VV_junc3__q": VV_junc3__q,
        "VV_junc3__bc2_is_in": VV_junc3__bc2_is_in,
        "VV_junc3__bc2_is_out": VV_junc3__bc2_is_out,
        "VV_junc3__C_max12": VV_junc3__C_max12,
        "PV5__R_constriction": PV5__R_constriction,
        "PV5__H_L_in": PV5__H_L_in,
        "PV5__H_R_in": PV5__H_R_in,
        "PV5__q_us": PV5__q_us,
        "PV5__q": PV5__q,
        "PV5__C": PV5__C,
        "PV5__Z": PV5__Z,
        "PV5__mu_45": PV5__mu_45,
        "PV5__u": PV5__u,
        "PV6__R_constriction": PV6__R_constriction,
        "PV6__H_L_in": PV6__H_L_in,
        "PV6__H_R_in": PV6__H_R_in,
        "PV6__q_us": PV6__q_us,
        "PV6__q": PV6__q,
        "PV6__C": PV6__C,
        "PV6__Z": PV6__Z,
        "PV6__mu_45": PV6__mu_45,
        "PV6__u": PV6__u,
        "V5__H_L_in": V5__H_L_in,
        "V5__H_R_in": V5__H_R_in,
        "V5__q_us": V5__q_us,
        "V5__q": V5__q,
        "V5__C": V5__C,
        "V5__Z": V5__Z,
        "V5__mu_45": V5__mu_45,
        "V5__u": V5__u,
        "V6__H_L_in": V6__H_L_in,
        "V6__H_R_in": V6__H_R_in,
        "V6__q_us": V6__q_us,
        "V6__q": V6__q,
        "V6__C": V6__C,
        "V6__Z": V6__Z,
        "V6__mu_45": V6__mu_45,
        "V6__u": V6__u,
        "inlet__RBC_volume_init": inlet__RBC_volume_init,
        "inlet__H_mean": inlet__H_mean,
        "inlet__hem_dep_u_rel": inlet__hem_dep_u_rel,
        "inlet__u_mmHg": inlet__u_mmHg,
        "VV_junc1__RBC_volume_init": VV_junc1__RBC_volume_init,
        "VV_junc1__H_mean": VV_junc1__H_mean,
        "VV_junc1__C_max123": VV_junc1__C_max123,
        "VV_junc1__C": VV_junc1__C,
        "PV1__RBC_volume_init": PV1__RBC_volume_init,
        "PV1__H_mean": PV1__H_mean,
        "PV1__hem_dep_u_rel": PV1__hem_dep_u_rel,
        "PV1__u_mmHg": PV1__u_mmHg,
        "PV2__RBC_volume_init": PV2__RBC_volume_init,
        "PV2__H_mean": PV2__H_mean,
        "PV2__hem_dep_u_rel": PV2__hem_dep_u_rel,
        "PV2__u_mmHg": PV2__u_mmHg,
        "V1__RBC_volume_init": V1__RBC_volume_init,
        "V1__H_mean": V1__H_mean,
        "V1__hem_dep_u_rel": V1__hem_dep_u_rel,
        "V1__u_mmHg": V1__u_mmHg,
        "V2__RBC_volume_init": V2__RBC_volume_init,
        "V2__H_mean": V2__H_mean,
        "V2__hem_dep_u_rel": V2__hem_dep_u_rel,
        "V2__u_mmHg": V2__u_mmHg,
        "VV_junc2__RBC_volume_init": VV_junc2__RBC_volume_init,
        "VV_junc2__H_mean": VV_junc2__H_mean,
        "VV_junc2__C_max123": VV_junc2__C_max123,
        "VV_junc2__C": VV_junc2__C,
        "PV3__RBC_volume_init": PV3__RBC_volume_init,
        "PV3__H_mean": PV3__H_mean,
        "PV3__hem_dep_u_rel": PV3__hem_dep_u_rel,
        "PV3__u_mmHg": PV3__u_mmHg,
        "PV4__RBC_volume_init": PV4__RBC_volume_init,
        "PV4__H_mean": PV4__H_mean,
        "PV4__hem_dep_u_rel": PV4__hem_dep_u_rel,
        "PV4__u_mmHg": PV4__u_mmHg,
        "V3__RBC_volume_init": V3__RBC_volume_init,
        "V3__H_mean": V3__H_mean,
        "V3__hem_dep_u_rel": V3__hem_dep_u_rel,
        "V3__u_mmHg": V3__u_mmHg,
        "V4__RBC_volume_init": V4__RBC_volume_init,
        "V4__H_mean": V4__H_mean,
        "V4__hem_dep_u_rel": V4__hem_dep_u_rel,
        "V4__u_mmHg": V4__u_mmHg,
        "VV_junc3__RBC_volume_init": VV_junc3__RBC_volume_init,
        "VV_junc3__H_mean": VV_junc3__H_mean,
        "VV_junc3__C_max123": VV_junc3__C_max123,
        "VV_junc3__C": VV_junc3__C,
        "PV5__RBC_volume_init": PV5__RBC_volume_init,
        "PV5__H_mean": PV5__H_mean,
        "PV5__hem_dep_u_rel": PV5__hem_dep_u_rel,
        "PV5__u_mmHg": PV5__u_mmHg,
        "PV6__RBC_volume_init": PV6__RBC_volume_init,
        "PV6__H_mean": PV6__H_mean,
        "PV6__hem_dep_u_rel": PV6__hem_dep_u_rel,
        "PV6__u_mmHg": PV6__u_mmHg,
        "V5__RBC_volume_init": V5__RBC_volume_init,
        "V5__H_mean": V5__H_mean,
        "V5__hem_dep_u_rel": V5__hem_dep_u_rel,
        "V5__u_mmHg": V5__u_mmHg,
        "V6__RBC_volume_init": V6__RBC_volume_init,
        "V6__H_mean": V6__H_mean,
        "V6__hem_dep_u_rel": V6__hem_dep_u_rel,
        "V6__u_mmHg": V6__u_mmHg,
        "inlet__mu": inlet__mu,
        "inlet__R": inlet__R,
        "inlet__v": inlet__v,
        "VV_junc1__u": VV_junc1__u,
        "VV_junc1__u_mmHg": VV_junc1__u_mmHg,
        "VV_junc1__u_d": VV_junc1__u_d,
        "VV_junc1__u_d_mmHg": VV_junc1__u_d_mmHg,
        "PV1__mu": PV1__mu,
        "PV1__R": PV1__R,
        "PV1__v": PV1__v,
        "PV1__v_d": PV1__v_d,
        "PV2__mu": PV2__mu,
        "PV2__R": PV2__R,
        "PV2__v": PV2__v,
        "PV2__v_d": PV2__v_d,
        "V1__mu": V1__mu,
        "V1__R": V1__R,
        "V2__mu": V2__mu,
        "V2__R": V2__R,
        "VV_junc2__u": VV_junc2__u,
        "VV_junc2__u_mmHg": VV_junc2__u_mmHg,
        "VV_junc2__u_d": VV_junc2__u_d,
        "VV_junc2__u_d_mmHg": VV_junc2__u_d_mmHg,
        "PV3__mu": PV3__mu,
        "PV3__R": PV3__R,
        "PV3__v": PV3__v,
        "PV3__v_d": PV3__v_d,
        "PV4__mu": PV4__mu,
        "PV4__R": PV4__R,
        "PV4__v": PV4__v,
        "PV4__v_d": PV4__v_d,
        "V3__mu": V3__mu,
        "V3__R": V3__R,
        "V3__v": V3__v,
        "V4__mu": V4__mu,
        "V4__R": V4__R,
        "V4__v": V4__v,
        "VV_junc3__u": VV_junc3__u,
        "VV_junc3__u_mmHg": VV_junc3__u_mmHg,
        "VV_junc3__u_d": VV_junc3__u_d,
        "VV_junc3__u_d_mmHg": VV_junc3__u_d_mmHg,
        "PV5__mu": PV5__mu,
        "PV5__R": PV5__R,
        "PV5__v": PV5__v,
        "PV5__v_d": PV5__v_d,
        "PV6__mu": PV6__mu,
        "PV6__R": PV6__R,
        "PV6__v": PV6__v,
        "PV6__v_d": PV6__v_d,
        "V5__mu": V5__mu,
        "V5__R": V5__R,
        "V5__v": V5__v,
        "V6__mu": V6__mu,
        "V6__R": V6__R,
        "V6__v": V6__v,
        "inlet__w_v": inlet__w_v,
        "inlet__v_pos": inlet__v_pos,
        "inlet__v_neg": inlet__v_neg,
        "inlet__v_mm3_s": inlet__v_mm3_s,
        "inlet__v_d": inlet__v_d,
        "VV_junc1__vj1": VV_junc1__vj1,
        "VV_junc1__vj3": VV_junc1__vj3,
        "VV_junc1__vj4": VV_junc1__vj4,
        "VV_junc1__w_in1": VV_junc1__w_in1,
        "VV_junc1__w_in3": VV_junc1__w_in3,
        "VV_junc1__w_in4": VV_junc1__w_in4,
        "VV_junc1__w_out1": VV_junc1__w_out1,
        "VV_junc1__w_out3": VV_junc1__w_out3,
        "VV_junc1__w_out4": VV_junc1__w_out4,
        "VV_junc1__Qin1": VV_junc1__Qin1,
        "VV_junc1__Qin3": VV_junc1__Qin3,
        "VV_junc1__Qin4": VV_junc1__Qin4,
        "VV_junc1__Qout1": VV_junc1__Qout1,
        "VV_junc1__Qout3": VV_junc1__Qout3,
        "VV_junc1__Qout4": VV_junc1__Qout4,
        "VV_junc1__Qin_tot": VV_junc1__Qin_tot,
        "VV_junc1__Qout_tot": VV_junc1__Qout_tot,
        "VV_junc1__v": VV_junc1__v,
        "VV_junc1__bc1_is_in": VV_junc1__bc1_is_in,
        "VV_junc1__bc3_is_in": VV_junc1__bc3_is_in,
        "VV_junc1__bc4_is_in": VV_junc1__bc4_is_in,
        "VV_junc1__bc1_is_out": VV_junc1__bc1_is_out,
        "VV_junc1__bc3_is_out": VV_junc1__bc3_is_out,
        "VV_junc1__bc4_is_out": VV_junc1__bc4_is_out,
        "PV1__w_v": PV1__w_v,
        "PV1__w_v_d": PV1__w_v_d,
        "PV1__H_up": PV1__H_up,
        "PV1__s_v_d": PV1__s_v_d,
        "PV1__H_L_out": PV1__H_L_out,
        "PV1__H_R_out": PV1__H_R_out,
        "PV1__v_pos": PV1__v_pos,
        "PV1__v_neg": PV1__v_neg,
        "PV1__v_d_pos": PV1__v_d_pos,
        "PV1__v_d_neg": PV1__v_d_neg,
        "PV1__H_volume_L": PV1__H_volume_L,
        "PV1__H_volume_R": PV1__H_volume_R,
        "PV1__v_mm3_s": PV1__v_mm3_s,
        "PV1__v_d_mm3_s": PV1__v_d_mm3_s,
        "PV2__w_v": PV2__w_v,
        "PV2__w_v_d": PV2__w_v_d,
        "PV2__H_up": PV2__H_up,
        "PV2__s_v_d": PV2__s_v_d,
        "PV2__H_L_out": PV2__H_L_out,
        "PV2__H_R_out": PV2__H_R_out,
        "PV2__v_pos": PV2__v_pos,
        "PV2__v_neg": PV2__v_neg,
        "PV2__v_d_pos": PV2__v_d_pos,
        "PV2__v_d_neg": PV2__v_d_neg,
        "PV2__H_volume_L": PV2__H_volume_L,
        "PV2__H_volume_R": PV2__H_volume_R,
        "PV2__v_mm3_s": PV2__v_mm3_s,
        "PV2__v_d_mm3_s": PV2__v_d_mm3_s,
        "V1__v": V1__v,
        "V2__v": V2__v,
        "VV_junc2__vj1": VV_junc2__vj1,
        "VV_junc2__vj3": VV_junc2__vj3,
        "VV_junc2__vj4": VV_junc2__vj4,
        "VV_junc2__w_in1": VV_junc2__w_in1,
        "VV_junc2__w_in3": VV_junc2__w_in3,
        "VV_junc2__w_in4": VV_junc2__w_in4,
        "VV_junc2__w_out1": VV_junc2__w_out1,
        "VV_junc2__w_out3": VV_junc2__w_out3,
        "VV_junc2__w_out4": VV_junc2__w_out4,
        "VV_junc2__Qin1": VV_junc2__Qin1,
        "VV_junc2__Qin3": VV_junc2__Qin3,
        "VV_junc2__Qin4": VV_junc2__Qin4,
        "VV_junc2__Qout1": VV_junc2__Qout1,
        "VV_junc2__Qout3": VV_junc2__Qout3,
        "VV_junc2__Qout4": VV_junc2__Qout4,
        "VV_junc2__Qin_tot": VV_junc2__Qin_tot,
        "VV_junc2__Qout_tot": VV_junc2__Qout_tot,
        "VV_junc2__v": VV_junc2__v,
        "VV_junc2__bc1_is_in": VV_junc2__bc1_is_in,
        "VV_junc2__bc3_is_in": VV_junc2__bc3_is_in,
        "VV_junc2__bc4_is_in": VV_junc2__bc4_is_in,
        "VV_junc2__bc1_is_out": VV_junc2__bc1_is_out,
        "VV_junc2__bc3_is_out": VV_junc2__bc3_is_out,
        "VV_junc2__bc4_is_out": VV_junc2__bc4_is_out,
        "PV3__w_v": PV3__w_v,
        "PV3__w_v_d": PV3__w_v_d,
        "PV3__H_up": PV3__H_up,
        "PV3__s_v_d": PV3__s_v_d,
        "PV3__H_L_out": PV3__H_L_out,
        "PV3__H_R_out": PV3__H_R_out,
        "PV3__v_pos": PV3__v_pos,
        "PV3__v_neg": PV3__v_neg,
        "PV3__v_d_pos": PV3__v_d_pos,
        "PV3__v_d_neg": PV3__v_d_neg,
        "PV3__H_volume_L": PV3__H_volume_L,
        "PV3__H_volume_R": PV3__H_volume_R,
        "PV3__v_mm3_s": PV3__v_mm3_s,
        "PV3__v_d_mm3_s": PV3__v_d_mm3_s,
        "PV4__w_v": PV4__w_v,
        "PV4__w_v_d": PV4__w_v_d,
        "PV4__H_up": PV4__H_up,
        "PV4__s_v_d": PV4__s_v_d,
        "PV4__H_L_out": PV4__H_L_out,
        "PV4__H_R_out": PV4__H_R_out,
        "PV4__v_pos": PV4__v_pos,
        "PV4__v_neg": PV4__v_neg,
        "PV4__v_d_pos": PV4__v_d_pos,
        "PV4__v_d_neg": PV4__v_d_neg,
        "PV4__H_volume_L": PV4__H_volume_L,
        "PV4__H_volume_R": PV4__H_volume_R,
        "PV4__v_mm3_s": PV4__v_mm3_s,
        "PV4__v_d_mm3_s": PV4__v_d_mm3_s,
        "V3__w_v": V3__w_v,
        "V3__H_up": V3__H_up,
        "V3__s_v": V3__s_v,
        "V3__H_L_out": V3__H_L_out,
        "V3__H_R_out": V3__H_R_out,
        "V3__v_pos": V3__v_pos,
        "V3__v_neg": V3__v_neg,
        "V3__H_volume_L": V3__H_volume_L,
        "V3__H_volume_R": V3__H_volume_R,
        "V3__v_mm3_s": V3__v_mm3_s,
        "V4__w_v": V4__w_v,
        "V4__H_up": V4__H_up,
        "V4__s_v": V4__s_v,
        "V4__H_L_out": V4__H_L_out,
        "V4__H_R_out": V4__H_R_out,
        "V4__v_pos": V4__v_pos,
        "V4__v_neg": V4__v_neg,
        "V4__H_volume_L": V4__H_volume_L,
        "V4__H_volume_R": V4__H_volume_R,
        "V4__v_mm3_s": V4__v_mm3_s,
        "VV_junc3__vj1": VV_junc3__vj1,
        "VV_junc3__vj3": VV_junc3__vj3,
        "VV_junc3__vj4": VV_junc3__vj4,
        "VV_junc3__w_in1": VV_junc3__w_in1,
        "VV_junc3__w_in3": VV_junc3__w_in3,
        "VV_junc3__w_in4": VV_junc3__w_in4,
        "VV_junc3__w_out1": VV_junc3__w_out1,
        "VV_junc3__w_out3": VV_junc3__w_out3,
        "VV_junc3__w_out4": VV_junc3__w_out4,
        "VV_junc3__Qin1": VV_junc3__Qin1,
        "VV_junc3__Qin3": VV_junc3__Qin3,
        "VV_junc3__Qin4": VV_junc3__Qin4,
        "VV_junc3__Qout1": VV_junc3__Qout1,
        "VV_junc3__Qout3": VV_junc3__Qout3,
        "VV_junc3__Qout4": VV_junc3__Qout4,
        "VV_junc3__Qin_tot": VV_junc3__Qin_tot,
        "VV_junc3__Qout_tot": VV_junc3__Qout_tot,
        "VV_junc3__v": VV_junc3__v,
        "VV_junc3__bc1_is_in": VV_junc3__bc1_is_in,
        "VV_junc3__bc3_is_in": VV_junc3__bc3_is_in,
        "VV_junc3__bc4_is_in": VV_junc3__bc4_is_in,
        "VV_junc3__bc1_is_out": VV_junc3__bc1_is_out,
        "VV_junc3__bc3_is_out": VV_junc3__bc3_is_out,
        "VV_junc3__bc4_is_out": VV_junc3__bc4_is_out,
        "PV5__w_v": PV5__w_v,
        "PV5__w_v_d": PV5__w_v_d,
        "PV5__H_up": PV5__H_up,
        "PV5__s_v_d": PV5__s_v_d,
        "PV5__H_L_out": PV5__H_L_out,
        "PV5__H_R_out": PV5__H_R_out,
        "PV5__v_pos": PV5__v_pos,
        "PV5__v_neg": PV5__v_neg,
        "PV5__v_d_pos": PV5__v_d_pos,
        "PV5__v_d_neg": PV5__v_d_neg,
        "PV5__H_volume_L": PV5__H_volume_L,
        "PV5__H_volume_R": PV5__H_volume_R,
        "PV5__v_mm3_s": PV5__v_mm3_s,
        "PV5__v_d_mm3_s": PV5__v_d_mm3_s,
        "PV6__w_v": PV6__w_v,
        "PV6__w_v_d": PV6__w_v_d,
        "PV6__H_up": PV6__H_up,
        "PV6__s_v_d": PV6__s_v_d,
        "PV6__H_L_out": PV6__H_L_out,
        "PV6__H_R_out": PV6__H_R_out,
        "PV6__v_pos": PV6__v_pos,
        "PV6__v_neg": PV6__v_neg,
        "PV6__v_d_pos": PV6__v_d_pos,
        "PV6__v_d_neg": PV6__v_d_neg,
        "PV6__H_volume_L": PV6__H_volume_L,
        "PV6__H_volume_R": PV6__H_volume_R,
        "PV6__v_mm3_s": PV6__v_mm3_s,
        "PV6__v_d_mm3_s": PV6__v_d_mm3_s,
        "V5__w_v": V5__w_v,
        "V5__H_up": V5__H_up,
        "V5__s_v": V5__s_v,
        "V5__H_L_out": V5__H_L_out,
        "V5__H_R_out": V5__H_R_out,
        "V5__v_pos": V5__v_pos,
        "V5__v_neg": V5__v_neg,
        "V5__H_volume_L": V5__H_volume_L,
        "V5__H_volume_R": V5__H_volume_R,
        "V5__v_mm3_s": V5__v_mm3_s,
        "V6__w_v": V6__w_v,
        "V6__H_up": V6__H_up,
        "V6__s_v": V6__s_v,
        "V6__H_L_out": V6__H_L_out,
        "V6__H_R_out": V6__H_R_out,
        "V6__v_pos": V6__v_pos,
        "V6__v_neg": V6__v_neg,
        "V6__H_volume_L": V6__H_volume_L,
        "V6__H_volume_R": V6__H_volume_R,
        "V6__v_mm3_s": V6__v_mm3_s,
        "inlet__w_v_d": inlet__w_v_d,
        "inlet__H_up": inlet__H_up,
        "inlet__s_v_d": inlet__s_v_d,
        "inlet__H_L_out": inlet__H_L_out,
        "inlet__H_R_out": inlet__H_R_out,
        "inlet__v_d_pos": inlet__v_d_pos,
        "inlet__v_d_neg": inlet__v_d_neg,
        "inlet__H_volume_L": inlet__H_volume_L,
        "inlet__H_volume_R": inlet__H_volume_R,
        "inlet__v_d_mm3_s": inlet__v_d_mm3_s,
        "VV_junc1__n_in": VV_junc1__n_in,
        "VV_junc1__n_out": VV_junc1__n_out,
        "VV_junc1__RBC_in": VV_junc1__RBC_in,
        "VV_junc1__v_mm3_s": VV_junc1__v_mm3_s,
        "VV_junc1__junction_type": VV_junc1__junction_type,
        "VV_junc1__is_split": VV_junc1__is_split,
        "VV_junc1__is_merge": VV_junc1__is_merge,
        "VV_junc1__feed1": VV_junc1__feed1,
        "VV_junc1__feed2": VV_junc1__feed2,
        "VV_junc1__feed3": VV_junc1__feed3,
        "VV_junc1__feed4": VV_junc1__feed4,
        "VV_junc1__alpha1": VV_junc1__alpha1,
        "VV_junc1__alpha2": VV_junc1__alpha2,
        "VV_junc1__alpha3": VV_junc1__alpha3,
        "VV_junc1__alpha4": VV_junc1__alpha4,
        "VV_junc1__Qout1_rem": VV_junc1__Qout1_rem,
        "VV_junc1__Qout2_rem": VV_junc1__Qout2_rem,
        "VV_junc1__Qout3_rem": VV_junc1__Qout3_rem,
        "VV_junc1__Qout4_rem": VV_junc1__Qout4_rem,
        "VV_junc1__beta1": VV_junc1__beta1,
        "VV_junc1__beta2": VV_junc1__beta2,
        "VV_junc1__beta3": VV_junc1__beta3,
        "VV_junc1__beta4": VV_junc1__beta4,
        "VV_junc1__D_F": VV_junc1__D_F,
        "VV_junc1__D_alpha": VV_junc1__D_alpha,
        "VV_junc1__D_beta": VV_junc1__D_beta,
        "VV_junc1__v_alpha": VV_junc1__v_alpha,
        "VV_junc1__v_beta": VV_junc1__v_beta,
        "PV1__H_down_target": PV1__H_down_target,
        "PV2__H_down_target": PV2__H_down_target,
        "V1__w_v": V1__w_v,
        "V1__H_up": V1__H_up,
        "V1__s_v": V1__s_v,
        "V1__H_L_out": V1__H_L_out,
        "V1__H_R_out": V1__H_R_out,
        "V1__v_pos": V1__v_pos,
        "V1__v_neg": V1__v_neg,
        "V1__H_volume_L": V1__H_volume_L,
        "V1__H_volume_R": V1__H_volume_R,
        "V1__v_mm3_s": V1__v_mm3_s,
        "V2__w_v": V2__w_v,
        "V2__H_up": V2__H_up,
        "V2__s_v": V2__s_v,
        "V2__H_L_out": V2__H_L_out,
        "V2__H_R_out": V2__H_R_out,
        "V2__v_pos": V2__v_pos,
        "V2__v_neg": V2__v_neg,
        "V2__H_volume_L": V2__H_volume_L,
        "V2__H_volume_R": V2__H_volume_R,
        "V2__v_mm3_s": V2__v_mm3_s,
        "VV_junc2__n_in": VV_junc2__n_in,
        "VV_junc2__n_out": VV_junc2__n_out,
        "VV_junc2__RBC_in": VV_junc2__RBC_in,
        "VV_junc2__v_mm3_s": VV_junc2__v_mm3_s,
        "VV_junc2__junction_type": VV_junc2__junction_type,
        "VV_junc2__is_split": VV_junc2__is_split,
        "VV_junc2__is_merge": VV_junc2__is_merge,
        "VV_junc2__feed1": VV_junc2__feed1,
        "VV_junc2__feed2": VV_junc2__feed2,
        "VV_junc2__feed3": VV_junc2__feed3,
        "VV_junc2__feed4": VV_junc2__feed4,
        "VV_junc2__alpha1": VV_junc2__alpha1,
        "VV_junc2__alpha2": VV_junc2__alpha2,
        "VV_junc2__alpha3": VV_junc2__alpha3,
        "VV_junc2__alpha4": VV_junc2__alpha4,
        "VV_junc2__Qout1_rem": VV_junc2__Qout1_rem,
        "VV_junc2__Qout2_rem": VV_junc2__Qout2_rem,
        "VV_junc2__Qout3_rem": VV_junc2__Qout3_rem,
        "VV_junc2__Qout4_rem": VV_junc2__Qout4_rem,
        "VV_junc2__beta1": VV_junc2__beta1,
        "VV_junc2__beta2": VV_junc2__beta2,
        "VV_junc2__beta3": VV_junc2__beta3,
        "VV_junc2__beta4": VV_junc2__beta4,
        "VV_junc2__D_F": VV_junc2__D_F,
        "VV_junc2__D_alpha": VV_junc2__D_alpha,
        "VV_junc2__D_beta": VV_junc2__D_beta,
        "VV_junc2__v_alpha": VV_junc2__v_alpha,
        "VV_junc2__v_beta": VV_junc2__v_beta,
        "PV3__H_down_target": PV3__H_down_target,
        "PV4__H_down_target": PV4__H_down_target,
        "V3__H_down_target": V3__H_down_target,
        "V4__H_down_target": V4__H_down_target,
        "VV_junc3__n_in": VV_junc3__n_in,
        "VV_junc3__n_out": VV_junc3__n_out,
        "VV_junc3__RBC_in": VV_junc3__RBC_in,
        "VV_junc3__v_mm3_s": VV_junc3__v_mm3_s,
        "VV_junc3__junction_type": VV_junc3__junction_type,
        "VV_junc3__is_split": VV_junc3__is_split,
        "VV_junc3__is_merge": VV_junc3__is_merge,
        "VV_junc3__feed1": VV_junc3__feed1,
        "VV_junc3__feed2": VV_junc3__feed2,
        "VV_junc3__feed3": VV_junc3__feed3,
        "VV_junc3__feed4": VV_junc3__feed4,
        "VV_junc3__alpha1": VV_junc3__alpha1,
        "VV_junc3__alpha2": VV_junc3__alpha2,
        "VV_junc3__alpha3": VV_junc3__alpha3,
        "VV_junc3__alpha4": VV_junc3__alpha4,
        "VV_junc3__Qout1_rem": VV_junc3__Qout1_rem,
        "VV_junc3__Qout2_rem": VV_junc3__Qout2_rem,
        "VV_junc3__Qout3_rem": VV_junc3__Qout3_rem,
        "VV_junc3__Qout4_rem": VV_junc3__Qout4_rem,
        "VV_junc3__beta1": VV_junc3__beta1,
        "VV_junc3__beta2": VV_junc3__beta2,
        "VV_junc3__beta3": VV_junc3__beta3,
        "VV_junc3__beta4": VV_junc3__beta4,
        "VV_junc3__D_F": VV_junc3__D_F,
        "VV_junc3__D_alpha": VV_junc3__D_alpha,
        "VV_junc3__D_beta": VV_junc3__D_beta,
        "VV_junc3__v_alpha": VV_junc3__v_alpha,
        "VV_junc3__v_beta": VV_junc3__v_beta,
        "PV5__H_down_target": PV5__H_down_target,
        "PV6__H_down_target": PV6__H_down_target,
        "V5__H_down_target": V5__H_down_target,
        "V6__H_down_target": V6__H_down_target,
        "inlet__H_down_target": inlet__H_down_target,
        "VV_junc1__FQB_alpha": VV_junc1__FQB_alpha,
        "VV_junc1__B": VV_junc1__B,
        "VV_junc1__A": VV_junc1__A,
        "VV_junc1__X_0": VV_junc1__X_0,
        "VV_junc1__y_raw": VV_junc1__y_raw,
        "VV_junc1__y": VV_junc1__y,
        "V1__H_down_target": V1__H_down_target,
        "V2__H_down_target": V2__H_down_target,
        "VV_junc2__FQB_alpha": VV_junc2__FQB_alpha,
        "VV_junc2__B": VV_junc2__B,
        "VV_junc2__A": VV_junc2__A,
        "VV_junc2__X_0": VV_junc2__X_0,
        "VV_junc2__y_raw": VV_junc2__y_raw,
        "VV_junc2__y": VV_junc2__y,
        "VV_junc3__FQB_alpha": VV_junc3__FQB_alpha,
        "VV_junc3__B": VV_junc3__B,
        "VV_junc3__A": VV_junc3__A,
        "VV_junc3__X_0": VV_junc3__X_0,
        "VV_junc3__y_raw": VV_junc3__y_raw,
        "VV_junc3__y": VV_junc3__y,
        "VV_junc1__ph": VV_junc1__ph,
        "VV_junc2__ph": VV_junc2__ph,
        "VV_junc3__ph": VV_junc3__ph,
        "VV_junc1__FQE_alpha": VV_junc1__FQE_alpha,
        "VV_junc1__H_VV_out_alpha": VV_junc1__H_VV_out_alpha,
        "VV_junc1__H_VV_out_beta": VV_junc1__H_VV_out_beta,
        "VV_junc1__H_split1": VV_junc1__H_split1,
        "VV_junc1__H_split2": VV_junc1__H_split2,
        "VV_junc1__H_split3": VV_junc1__H_split3,
        "VV_junc1__H_split4": VV_junc1__H_split4,
        "VV_junc1__H_daughter1": VV_junc1__H_daughter1,
        "VV_junc1__H_daughter2": VV_junc1__H_daughter2,
        "VV_junc1__H_daughter3": VV_junc1__H_daughter3,
        "VV_junc1__H_daughter4": VV_junc1__H_daughter4,
        "VV_junc1__H_from1_target": VV_junc1__H_from1_target,
        "VV_junc1__H_from2_target": VV_junc1__H_from2_target,
        "VV_junc1__H_from3_target": VV_junc1__H_from3_target,
        "VV_junc1__H_from4_target": VV_junc1__H_from4_target,
        "VV_junc2__FQE_alpha": VV_junc2__FQE_alpha,
        "VV_junc2__H_VV_out_alpha": VV_junc2__H_VV_out_alpha,
        "VV_junc2__H_VV_out_beta": VV_junc2__H_VV_out_beta,
        "VV_junc2__H_split1": VV_junc2__H_split1,
        "VV_junc2__H_split2": VV_junc2__H_split2,
        "VV_junc2__H_split3": VV_junc2__H_split3,
        "VV_junc2__H_split4": VV_junc2__H_split4,
        "VV_junc2__H_daughter1": VV_junc2__H_daughter1,
        "VV_junc2__H_daughter2": VV_junc2__H_daughter2,
        "VV_junc2__H_daughter3": VV_junc2__H_daughter3,
        "VV_junc2__H_daughter4": VV_junc2__H_daughter4,
        "VV_junc2__H_from1_target": VV_junc2__H_from1_target,
        "VV_junc2__H_from2_target": VV_junc2__H_from2_target,
        "VV_junc2__H_from3_target": VV_junc2__H_from3_target,
        "VV_junc2__H_from4_target": VV_junc2__H_from4_target,
        "VV_junc3__FQE_alpha": VV_junc3__FQE_alpha,
        "VV_junc3__H_VV_out_alpha": VV_junc3__H_VV_out_alpha,
        "VV_junc3__H_VV_out_beta": VV_junc3__H_VV_out_beta,
        "VV_junc3__H_split1": VV_junc3__H_split1,
        "VV_junc3__H_split2": VV_junc3__H_split2,
        "VV_junc3__H_split3": VV_junc3__H_split3,
        "VV_junc3__H_split4": VV_junc3__H_split4,
        "VV_junc3__H_daughter1": VV_junc3__H_daughter1,
        "VV_junc3__H_daughter2": VV_junc3__H_daughter2,
        "VV_junc3__H_daughter3": VV_junc3__H_daughter3,
        "VV_junc3__H_daughter4": VV_junc3__H_daughter4,
        "VV_junc3__H_from1_target": VV_junc3__H_from1_target,
        "VV_junc3__H_from2_target": VV_junc3__H_from2_target,
        "VV_junc3__H_from3_target": VV_junc3__H_from3_target,
        "VV_junc3__H_from4_target": VV_junc3__H_from4_target,
        "VV_junc1__H_from1": VV_junc1__H_from1,
        "VV_junc1__H_from2": VV_junc1__H_from2,
        "VV_junc1__H_from3": VV_junc1__H_from3,
        "VV_junc1__H_from4": VV_junc1__H_from4,
        "VV_junc1__RBC_out": VV_junc1__RBC_out,
        "VV_junc2__H_from1": VV_junc2__H_from1,
        "VV_junc2__H_from2": VV_junc2__H_from2,
        "VV_junc2__H_from3": VV_junc2__H_from3,
        "VV_junc2__H_from4": VV_junc2__H_from4,
        "VV_junc2__RBC_out": VV_junc2__RBC_out,
        "VV_junc3__H_from1": VV_junc3__H_from1,
        "VV_junc3__H_from2": VV_junc3__H_from2,
        "VV_junc3__H_from3": VV_junc3__H_from3,
        "VV_junc3__H_from4": VV_junc3__H_from4,
        "VV_junc3__RBC_out": VV_junc3__RBC_out,
    }