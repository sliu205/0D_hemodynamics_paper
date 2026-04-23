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
PV10__H_global_L = 0.45
PV10__H_global_R = 0.45
PV10__R_constriction_base = 0.0
PV10__R_constriction_final = 0.0
PV10__gamma_mirror = 0.1
PV10__l = 0.000015
PV10__mu_plasma = 0.001
PV10__one_mm3 = 1e-09
PV10__q_C_init = 0.0
PV10__r = 5e-06
PV10__t0 = 500.0
PV10__tau_H_down = 0.001
PV10__tau_H_mean = 0.001
PV10__tau_link = 0.001
PV10__tau_sig = 1.0
PV10__u_ext = 133.0
PV10__v_eps = 1e-30
PV10__v_scale = 1e-50
PV11__H_global_L = 0.45
PV11__H_global_R = 0.45
PV11__R_constriction_base = 0.0
PV11__R_constriction_final = 0.0
PV11__gamma_mirror = 0.1
PV11__l = 0.000015
PV11__mu_plasma = 0.001
PV11__one_mm3 = 1e-09
PV11__q_C_init = 0.0
PV11__r = 5e-06
PV11__t0 = 500.0
PV11__tau_H_down = 0.001
PV11__tau_H_mean = 0.001
PV11__tau_link = 0.001
PV11__tau_sig = 1.0
PV11__u_ext = 133.0
PV11__v_eps = 1e-30
PV11__v_scale = 1e-50
PV12__H_global_L = 0.45
PV12__H_global_R = 0.45
PV12__R_constriction_base = 0.0
PV12__R_constriction_final = 0.0
PV12__gamma_mirror = 0.1
PV12__l = 0.000015
PV12__mu_plasma = 0.001
PV12__one_mm3 = 1e-09
PV12__q_C_init = 0.0
PV12__r = 5e-06
PV12__t0 = 500.0
PV12__tau_H_down = 0.001
PV12__tau_H_mean = 0.001
PV12__tau_link = 0.001
PV12__tau_sig = 1.0
PV12__u_ext = 133.0
PV12__v_eps = 1e-30
PV12__v_scale = 1e-50
PV13__H_global_L = 0.45
PV13__H_global_R = 0.45
PV13__R_constriction_base = 0.0
PV13__R_constriction_final = 0.0
PV13__gamma_mirror = 0.1
PV13__l = 0.000015
PV13__mu_plasma = 0.001
PV13__one_mm3 = 1e-09
PV13__q_C_init = 0.0
PV13__r = 5e-06
PV13__t0 = 500.0
PV13__tau_H_down = 0.001
PV13__tau_H_mean = 0.001
PV13__tau_link = 0.001
PV13__tau_sig = 1.0
PV13__u_ext = 133.0
PV13__v_eps = 1e-30
PV13__v_scale = 1e-50
PV14__H_global_L = 0.45
PV14__H_global_R = 0.45
PV14__R_constriction_base = 0.0
PV14__R_constriction_final = 0.0
PV14__gamma_mirror = 0.1
PV14__l = 0.000015
PV14__mu_plasma = 0.001
PV14__one_mm3 = 1e-09
PV14__q_C_init = 0.0
PV14__r = 5e-06
PV14__t0 = 500.0
PV14__tau_H_down = 0.001
PV14__tau_H_mean = 0.001
PV14__tau_link = 0.001
PV14__tau_sig = 1.0
PV14__u_ext = 133.0
PV14__v_eps = 1e-30
PV14__v_scale = 1e-50
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
PV5__R_constriction_final = 0.0
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
PV7__H_global_L = 0.45
PV7__H_global_R = 0.45
PV7__R_constriction_base = 0.0
PV7__R_constriction_final = 0
PV7__gamma_mirror = 0.1
PV7__l = 0.000015
PV7__mu_plasma = 0.001
PV7__one_mm3 = 1e-09
PV7__q_C_init = 0.0
PV7__r = 5e-06
PV7__t0 = 500.0
PV7__tau_H_down = 0.001
PV7__tau_H_mean = 0.001
PV7__tau_link = 0.001
PV7__tau_sig = 1.0
PV7__u_ext = 133.0
PV7__v_eps = 1e-30
PV7__v_scale = 1e-50
PV8__H_global_L = 0.45
PV8__H_global_R = 0.45
PV8__R_constriction_base = 0.0
PV8__R_constriction_final = 0.0
PV8__gamma_mirror = 0.1
PV8__l = 0.000015
PV8__mu_plasma = 0.001
PV8__one_mm3 = 1e-09
PV8__q_C_init = 0.0
PV8__r = 5e-06
PV8__t0 = 500.0
PV8__tau_H_down = 0.001
PV8__tau_H_mean = 0.001
PV8__tau_link = 0.001
PV8__tau_sig = 1.0
PV8__u_ext = 133.0
PV8__v_eps = 1e-30
PV8__v_scale = 1e-50
PV9__H_global_L = 0.45
PV9__H_global_R = 0.45
PV9__R_constriction_base = 0.0
PV9__R_constriction_final = 0.0
PV9__gamma_mirror = 0.1
PV9__l = 0.000015
PV9__mu_plasma = 0.001
PV9__one_mm3 = 1e-09
PV9__q_C_init = 0.0
PV9__r = 5e-06
PV9__t0 = 500.0
PV9__tau_H_down = 0.001
PV9__tau_H_mean = 0.001
PV9__tau_link = 0.001
PV9__tau_sig = 1.0
PV9__u_ext = 133.0
PV9__v_eps = 1e-30
PV9__v_scale = 1e-50
V10__H_L_out_RHS = 0.45
V10__H_global_L = 0.45
V10__H_global_R = 0.45
V10__gamma_mirror = 0.1
V10__l = 0.00015
V10__mu_plasma = 0.001
V10__one_mm3 = 1e-09
V10__q_C_init = 0.0
V10__r = 4.5e-06
V10__tau_H_down = 0.001
V10__tau_H_mean = 0.001
V10__tau_link = 0.001
V10__u_ext = 133.0
V10__u_out = 6566.1085
V10__v_eps = 1e-30
V10__v_scale = 1e-50
V11__H_L_out_RHS = 0.45
V11__H_global_L = 0.45
V11__H_global_R = 0.45
V11__gamma_mirror = 0.1
V11__l = 0.00015
V11__mu_plasma = 0.001
V11__one_mm3 = 1e-09
V11__q_C_init = 0.0
V11__r = 4.5e-06
V11__tau_H_down = 0.001
V11__tau_H_mean = 0.001
V11__tau_link = 0.001
V11__u_ext = 133.0
V11__u_out = 6566.1085
V11__v_eps = 1e-30
V11__v_scale = 1e-50
V12__H_L_out_RHS = 0.45
V12__H_global_L = 0.45
V12__H_global_R = 0.45
V12__gamma_mirror = 0.1
V12__l = 0.00015
V12__mu_plasma = 0.001
V12__one_mm3 = 1e-09
V12__q_C_init = 0.0
V12__r = 4.5e-06
V12__tau_H_down = 0.001
V12__tau_H_mean = 0.001
V12__tau_link = 0.001
V12__u_ext = 133.0
V12__u_out = 6566.1085
V12__v_eps = 1e-30
V12__v_scale = 1e-50
V13__H_L_out_RHS = 0.45
V13__H_global_L = 0.45
V13__H_global_R = 0.45
V13__gamma_mirror = 0.1
V13__l = 0.00015
V13__mu_plasma = 0.001
V13__one_mm3 = 1e-09
V13__q_C_init = 0.0
V13__r = 4.5e-06
V13__tau_H_down = 0.001
V13__tau_H_mean = 0.001
V13__tau_link = 0.001
V13__u_ext = 133.0
V13__u_out = 6566.1085
V13__v_eps = 1e-30
V13__v_scale = 1e-50
V14__H_L_out_RHS = 0.45
V14__H_global_L = 0.45
V14__H_global_R = 0.45
V14__gamma_mirror = 0.1
V14__l = 0.00015
V14__mu_plasma = 0.001
V14__one_mm3 = 1e-09
V14__q_C_init = 0.0
V14__r = 4.5e-06
V14__tau_H_down = 0.001
V14__tau_H_mean = 0.001
V14__tau_link = 0.001
V14__u_ext = 133.0
V14__u_out = 6566.1085
V14__v_eps = 1e-30
V14__v_scale = 1e-50
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
V3__v_eps = 1e-30
V3__v_scale = 1e-50
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
V4__v_eps = 1e-30
V4__v_scale = 1e-50
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
V5__v_eps = 1e-30
V5__v_scale = 1e-50
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
V6__v_eps = 1e-30
V6__v_scale = 1e-50
V7__H_L_out_RHS = 0.45
V7__H_global_L = 0.45
V7__H_global_R = 0.45
V7__gamma_mirror = 0.1
V7__l = 0.00015
V7__mu_plasma = 0.001
V7__one_mm3 = 1e-09
V7__q_C_init = 0.0
V7__r = 4.5e-06
V7__tau_H_down = 0.001
V7__tau_H_mean = 0.001
V7__tau_link = 0.001
V7__u_ext = 133.0
V7__u_out = 6566.1085
V7__v_eps = 1e-30
V7__v_scale = 1e-50
V8__H_L_out_RHS = 0.45
V8__H_global_L = 0.45
V8__H_global_R = 0.45
V8__gamma_mirror = 0.1
V8__l = 0.00015
V8__mu_plasma = 0.001
V8__one_mm3 = 1e-09
V8__q_C_init = 0.0
V8__r = 4.5e-06
V8__tau_H_down = 0.001
V8__tau_H_mean = 0.001
V8__tau_link = 0.001
V8__u_ext = 133.0
V8__u_out = 6566.1085
V8__v_eps = 1e-30
V8__v_scale = 1e-50
V9__H_L_out_RHS = 0.45
V9__H_global_L = 0.45
V9__H_global_R = 0.45
V9__gamma_mirror = 0.1
V9__l = 0.00015
V9__mu_plasma = 0.001
V9__one_mm3 = 1e-09
V9__q_C_init = 0.0
V9__r = 4.5e-06
V9__tau_H_down = 0.001
V9__tau_H_mean = 0.001
V9__tau_link = 0.001
V9__u_ext = 133.0
V9__u_out = 6566.1085
V9__v_eps = 1e-30
V9__v_scale = 1e-50
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
VV_junc4__C_conn2 = 8.51e-22
VV_junc4__H_global_L = 0.45
VV_junc4__H_global_R = 0.45
VV_junc4__H_to2 = 0.0
VV_junc4__R_VV_junc = 1000000000000000.0
VV_junc4__div_0 = 1e-25
VV_junc4__div_0y = 1e-08
VV_junc4__k = 1000.0
VV_junc4__l = 0.000001
VV_junc4__mu_plasma = 0.001
VV_junc4__one_mm3 = 1e-09
VV_junc4__q_C_init = 0.0
VV_junc4__r = 5e-06
VV_junc4__r_bc2 = 0.0
VV_junc4__u_ext = 133.0
VV_junc4__v_scale = 1e-50
VV_junc4__v_threshold = 1e-18
VV_junc4__vbc2 = 0.0
VV_junc5__C_conn2 = 8.51e-22
VV_junc5__H_global_L = 0.45
VV_junc5__H_global_R = 0.45
VV_junc5__H_to2 = 0.0
VV_junc5__R_VV_junc = 1000000000000000.0
VV_junc5__div_0 = 1e-25
VV_junc5__div_0y = 1e-08
VV_junc5__k = 1000.0
VV_junc5__l = 0.000001
VV_junc5__mu_plasma = 0.001
VV_junc5__one_mm3 = 1e-09
VV_junc5__q_C_init = 0.0
VV_junc5__r = 5e-06
VV_junc5__r_bc2 = 0.0
VV_junc5__u_ext = 133.0
VV_junc5__v_scale = 1e-50
VV_junc5__v_threshold = 1e-18
VV_junc5__vbc2 = 0.0
VV_junc6__C_conn2 = 8.51e-22
VV_junc6__H_global_L = 0.45
VV_junc6__H_global_R = 0.45
VV_junc6__H_to2 = 0.0
VV_junc6__R_VV_junc = 1000000000000000.0
VV_junc6__div_0 = 1e-25
VV_junc6__div_0y = 1e-08
VV_junc6__k = 1000.0
VV_junc6__l = 0.000001
VV_junc6__mu_plasma = 0.001
VV_junc6__one_mm3 = 1e-09
VV_junc6__q_C_init = 0.0
VV_junc6__r = 5e-06
VV_junc6__r_bc2 = 0.0
VV_junc6__u_ext = 133.0
VV_junc6__v_scale = 1e-50
VV_junc6__v_threshold = 1e-18
VV_junc6__vbc2 = 0.0
VV_junc7__C_conn2 = 8.51e-22
VV_junc7__H_global_L = 0.45
VV_junc7__H_global_R = 0.45
VV_junc7__H_to2 = 0.0
VV_junc7__R_VV_junc = 1000000000000000.0
VV_junc7__div_0 = 1e-25
VV_junc7__div_0y = 1e-08
VV_junc7__k = 1000.0
VV_junc7__l = 0.000001
VV_junc7__mu_plasma = 0.001
VV_junc7__one_mm3 = 1e-09
VV_junc7__q_C_init = 0.0
VV_junc7__r = 5e-06
VV_junc7__r_bc2 = 0.0
VV_junc7__u_ext = 133.0
VV_junc7__v_scale = 1e-50
VV_junc7__v_threshold = 1e-18
VV_junc7__vbc2 = 0.0
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
    'VV_junc4__RBC_volume',
    'VV_junc4__q_C',
    'VV_junc4__q_C_d',
    'PV7__H_link_R',
    'PV7__H_link_L',
    'PV7__H_down',
    'PV7__RBC_volume',
    'PV7__q_C',
    'PV8__H_link_R',
    'PV8__H_link_L',
    'PV8__H_down',
    'PV8__RBC_volume',
    'PV8__q_C',
    'V7__H_link_R',
    'V7__H_link_L',
    'V7__H_down',
    'V7__RBC_volume',
    'V7__q_C',
    'V8__H_link_R',
    'V8__H_link_L',
    'V8__H_down',
    'V8__RBC_volume',
    'V8__q_C',
    'VV_junc5__RBC_volume',
    'VV_junc5__q_C',
    'VV_junc5__q_C_d',
    'PV9__H_link_R',
    'PV9__H_link_L',
    'PV9__H_down',
    'PV9__RBC_volume',
    'PV9__q_C',
    'PV10__H_link_R',
    'PV10__H_link_L',
    'PV10__H_down',
    'PV10__RBC_volume',
    'PV10__q_C',
    'V9__H_link_R',
    'V9__H_link_L',
    'V9__H_down',
    'V9__RBC_volume',
    'V9__q_C',
    'V10__H_link_R',
    'V10__H_link_L',
    'V10__H_down',
    'V10__RBC_volume',
    'V10__q_C',
    'VV_junc6__RBC_volume',
    'VV_junc6__q_C',
    'VV_junc6__q_C_d',
    'PV11__H_link_R',
    'PV11__H_link_L',
    'PV11__H_down',
    'PV11__RBC_volume',
    'PV11__q_C',
    'PV12__H_link_R',
    'PV12__H_link_L',
    'PV12__H_down',
    'PV12__RBC_volume',
    'PV12__q_C',
    'V11__H_link_R',
    'V11__H_link_L',
    'V11__H_down',
    'V11__RBC_volume',
    'V11__q_C',
    'V12__H_link_R',
    'V12__H_link_L',
    'V12__H_down',
    'V12__RBC_volume',
    'V12__q_C',
    'VV_junc7__RBC_volume',
    'VV_junc7__q_C',
    'VV_junc7__q_C_d',
    'PV13__H_link_R',
    'PV13__H_link_L',
    'PV13__H_down',
    'PV13__RBC_volume',
    'PV13__q_C',
    'PV14__H_link_R',
    'PV14__H_link_L',
    'PV14__H_down',
    'PV14__RBC_volume',
    'PV14__q_C',
    'V13__H_link_R',
    'V13__H_link_L',
    'V13__H_down',
    'V13__RBC_volume',
    'V13__q_C',
    'V14__H_link_R',
    'V14__H_link_L',
    'V14__H_down',
    'V14__RBC_volume',
    'V14__q_C',
]

# Initial conditions
y0 = np.array([
    0.1655458718842374,
    0.45,
    0.44999999858297884,
    1.5269637997063594e-14,
    3.3283866024657928e-18,
    5.2994374144537023e-17,
    2.765863321514603e-18,
    2.7600734819372476e-18,
    0.4499625595101894,
    0.4623008448303724,
    0.4494864237760941,
    7.635329850908598e-16,
    1.6564211274778232e-19,
    0.449962562316234,
    0.4623006273866477,
    0.4494864429326235,
    7.6353298276877e-16,
    1.6564211274773738e-19,
    0.16554587643938068,
    0.4498422585141897,
    0.45000374012631394,
    1.0692474374035332e-14,
    2.7605271772467856e-18,
    0.16554587624870748,
    0.4498422674831086,
    0.45000373987055603,
    1.0692474374982412e-14,
    2.7605271772472794e-18,
    4.5069972137350334e-17,
    2.750960390410265e-18,
    2.7480654706443405e-18,
    0.450041972367913,
    0.45974995151487547,
    0.4499117574977348,
    6.415462882678065e-16,
    1.6492401487405905e-19,
    0.4500419660110813,
    0.4597504982492192,
    0.4499117112614112,
    6.415462912221819e-16,
    1.6492401487401618e-19,
    0.17255771499321698,
    0.45007619953579836,
    0.449995158956189,
    7.069573752083085e-15,
    2.1988816693618914e-18,
    0.17255771508767379,
    0.4500761786896283,
    0.44999515956272296,
    7.069573751278946e-15,
    2.1988816693603206e-18,
    4.507024191564715e-17,
    2.7509603904070884e-18,
    2.748065470645705e-18,
    0.4500419542796737,
    0.45975288479902937,
    0.44991159678539455,
    6.415463283142517e-16,
    1.6492401487283536e-19,
    0.4500419751676428,
    0.4597511042504137,
    0.4499117323952958,
    6.415462589720601e-16,
    1.649240148740567e-19,
    0.1725577148339267,
    0.45007613608215713,
    0.4499951607651326,
    7.069573752034877e-15,
    2.1988816693442803e-18,
    0.17255771482624957,
    0.4500762019951752,
    0.44999515867827183,
    7.0695737521385975e-15,
    2.1988816693767996e-18,
    3.7624774957169585e-17,
    2.742316061298808e-18,
    2.740868601413843e-18,
    0.4500563288016068,
    0.46093877628313495,
    0.44995224556915664,
    5.302151360836605e-16,
    1.644937926886737e-19,
    0.4500563286984458,
    0.4609388470488498,
    0.4499522425785595,
    5.302151364175481e-16,
    1.6449379268866857e-19,
    0.45,
    0.4501142930268583,
    0.4499943711663996,
    4.294904786321696e-15,
    1.6448761862969992e-18,
    0.45,
    0.4501142923566057,
    0.4499943711767144,
    4.294904786321554e-15,
    1.6448761862968939e-18,
    3.762474847643078e-17,
    2.7423160612942003e-18,
    2.7408686014083145e-18,
    0.45005637446798413,
    0.460905204471643,
    0.4499536397175509,
    5.30215107047996e-16,
    1.6449379269023642e-19,
    0.4500563181906356,
    0.46094180565307025,
    0.4499520910183896,
    5.30215137099694e-16,
    1.644937926897552e-19,
    0.45,
    0.45011459319936165,
    0.44999436660118763,
    4.294904786416624e-15,
    1.6448761863031368e-18,
    0.45,
    0.4501142474206818,
    0.4499943722270337,
    4.294904786300105e-15,
    1.6448761862935514e-18,
    3.762480749018515e-17,
    2.742316061287857e-18,
    2.7408686014058154e-18,
    0.450056330262945,
    0.4609371172527214,
    0.44995231208017594,
    5.302151349411736e-16,
    1.6449379268787082e-19,
    0.4500563306855946,
    0.46093688942422983,
    0.4499523241138349,
    5.302151350873395e-16,
    1.6449379268786765e-19,
    0.45,
    0.45011430559509585,
    0.44999437102034096,
    4.2949047863261954e-15,
    1.6448761862928211e-18,
    0.45,
    0.4501143085037299,
    0.4499943709780539,
    4.294904786325504e-15,
    1.6448761862927749e-18,
    3.7624806671831104e-17,
    2.7423160613078012e-18,
    2.7408686014203365e-18,
    0.4500563293399063,
    0.460937846461119,
    0.4499522832211856,
    5.302151362302142e-16,
    1.6449379268872346e-19,
    0.45005632709530746,
    0.4609400730715621,
    0.44995219344139603,
    5.302151376993219e-16,
    1.6449379268870018e-19,
    0.45,
    0.4501142995594934,
    0.4499943711125117,
    4.2949047863206135e-15,
    1.6448761863006248e-18,
    0.45,
    0.4501142817374055,
    0.44999437133693976,
    4.294904786316709e-15,
    1.6448761863001566e-18,
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
    VV_junc4__RBC_volume = y[74]
    VV_junc4__q_C = y[75]
    VV_junc4__q_C_d = y[76]
    PV7__H_link_R = y[77]
    PV7__H_link_L = y[78]
    PV7__H_down = y[79]
    PV7__RBC_volume = y[80]
    PV7__q_C = y[81]
    PV8__H_link_R = y[82]
    PV8__H_link_L = y[83]
    PV8__H_down = y[84]
    PV8__RBC_volume = y[85]
    PV8__q_C = y[86]
    V7__H_link_R = y[87]
    V7__H_link_L = y[88]
    V7__H_down = y[89]
    V7__RBC_volume = y[90]
    V7__q_C = y[91]
    V8__H_link_R = y[92]
    V8__H_link_L = y[93]
    V8__H_down = y[94]
    V8__RBC_volume = y[95]
    V8__q_C = y[96]
    VV_junc5__RBC_volume = y[97]
    VV_junc5__q_C = y[98]
    VV_junc5__q_C_d = y[99]
    PV9__H_link_R = y[100]
    PV9__H_link_L = y[101]
    PV9__H_down = y[102]
    PV9__RBC_volume = y[103]
    PV9__q_C = y[104]
    PV10__H_link_R = y[105]
    PV10__H_link_L = y[106]
    PV10__H_down = y[107]
    PV10__RBC_volume = y[108]
    PV10__q_C = y[109]
    V9__H_link_R = y[110]
    V9__H_link_L = y[111]
    V9__H_down = y[112]
    V9__RBC_volume = y[113]
    V9__q_C = y[114]
    V10__H_link_R = y[115]
    V10__H_link_L = y[116]
    V10__H_down = y[117]
    V10__RBC_volume = y[118]
    V10__q_C = y[119]
    VV_junc6__RBC_volume = y[120]
    VV_junc6__q_C = y[121]
    VV_junc6__q_C_d = y[122]
    PV11__H_link_R = y[123]
    PV11__H_link_L = y[124]
    PV11__H_down = y[125]
    PV11__RBC_volume = y[126]
    PV11__q_C = y[127]
    PV12__H_link_R = y[128]
    PV12__H_link_L = y[129]
    PV12__H_down = y[130]
    PV12__RBC_volume = y[131]
    PV12__q_C = y[132]
    V11__H_link_R = y[133]
    V11__H_link_L = y[134]
    V11__H_down = y[135]
    V11__RBC_volume = y[136]
    V11__q_C = y[137]
    V12__H_link_R = y[138]
    V12__H_link_L = y[139]
    V12__H_down = y[140]
    V12__RBC_volume = y[141]
    V12__q_C = y[142]
    VV_junc7__RBC_volume = y[143]
    VV_junc7__q_C = y[144]
    VV_junc7__q_C_d = y[145]
    PV13__H_link_R = y[146]
    PV13__H_link_L = y[147]
    PV13__H_down = y[148]
    PV13__RBC_volume = y[149]
    PV13__q_C = y[150]
    PV14__H_link_R = y[151]
    PV14__H_link_L = y[152]
    PV14__H_down = y[153]
    PV14__RBC_volume = y[154]
    PV14__q_C = y[155]
    V13__H_link_R = y[156]
    V13__H_link_L = y[157]
    V13__H_down = y[158]
    V13__RBC_volume = y[159]
    V13__q_C = y[160]
    V14__H_link_R = y[161]
    V14__H_link_L = y[162]
    V14__H_down = y[163]
    V14__RBC_volume = y[164]
    V14__q_C = y[165]

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
    VV_junc4__vj2 = VV_junc4__vbc2
    VV_junc4__D1 = 2*V3__r
    VV_junc4__D2 = 2*VV_junc4__r_bc2
    VV_junc4__D3 = 2*PV7__r
    VV_junc4__D4 = 2*PV8__r
    VV_junc4__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc4__vj2/VV_junc4__v_scale)
    VV_junc4__w_out2 = 1-VV_junc4__w_in2
    VV_junc4__Qin2 = VV_junc4__w_in2*VV_junc4__vj2
    VV_junc4__Qout2 = VV_junc4__w_out2*-VV_junc4__vj2
    VV_junc4__q_us = np.pi*np.square(VV_junc4__r)*VV_junc4__l
    VV_junc4__q = VV_junc4__q_us+VV_junc4__q_C+VV_junc4__q_C_d
    VV_junc4__bc2_is_in = (1 if VV_junc4__Qin2 > VV_junc4__v_threshold else 0)
    VV_junc4__bc2_is_out = (1 if VV_junc4__Qout2 > VV_junc4__v_threshold else 0)
    VV_junc4__C_max12 = (V3__C if V3__C > VV_junc4__C_conn2 else (VV_junc4__C_conn2 if V3__C <= VV_junc4__C_conn2 else 0.0))
    PV7__R_constriction = PV7__R_constriction_base+(PV7__R_constriction_final-PV7__R_constriction_base)/(1+np.exp(-(environment__time-PV7__t0)/PV7__tau_sig))
    PV7__H_L_in = PV7__H_link_L
    PV7__H_R_in = PV7__H_link_R
    PV7__q_us = np.pi*np.square(PV7__r)*PV7__l
    PV7__q = PV7__q_us+PV7__q_C
    PV7__C = np.pi*np.square(8.5e-9)*PV7__l/133.322
    PV7__Z = (0.8+np.exp(-0.075*2*PV7__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV7__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV7__r*1e6, 12))
    PV7__mu_45 = 6*np.exp(-0.085*2*PV7__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV7__r*1e6, 0.645))
    PV7__u = PV7__q_C/PV7__C+PV7__u_ext
    PV8__R_constriction = PV8__R_constriction_base+(PV8__R_constriction_final-PV8__R_constriction_base)/(1+np.exp(-(environment__time-PV8__t0)/PV8__tau_sig))
    PV8__H_L_in = PV8__H_link_L
    PV8__H_R_in = PV8__H_link_R
    PV8__q_us = np.pi*np.square(PV8__r)*PV8__l
    PV8__q = PV8__q_us+PV8__q_C
    PV8__C = np.pi*np.square(8.5e-9)*PV8__l/133.322
    PV8__Z = (0.8+np.exp(-0.075*2*PV8__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV8__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV8__r*1e6, 12))
    PV8__mu_45 = 6*np.exp(-0.085*2*PV8__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV8__r*1e6, 0.645))
    PV8__u = PV8__q_C/PV8__C+PV8__u_ext
    V7__H_L_in = V7__H_link_L
    V7__H_R_in = V7__H_link_R
    V7__q_us = np.pi*np.square(V7__r)*V7__l
    V7__q = V7__q_us+V7__q_C
    V7__C = np.pi*np.square(8.5e-9)*V7__l/133.322
    V7__Z = (0.8+np.exp(-0.075*2*V7__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V7__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V7__r*1e6, 12))
    V7__mu_45 = 6*np.exp(-0.085*2*V7__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V7__r*1e6, 0.645))
    V7__u = V7__q_C/V7__C+V7__u_ext
    V8__H_L_in = V8__H_link_L
    V8__H_R_in = V8__H_link_R
    V8__q_us = np.pi*np.square(V8__r)*V8__l
    V8__q = V8__q_us+V8__q_C
    V8__C = np.pi*np.square(8.5e-9)*V8__l/133.322
    V8__Z = (0.8+np.exp(-0.075*2*V8__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V8__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V8__r*1e6, 12))
    V8__mu_45 = 6*np.exp(-0.085*2*V8__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V8__r*1e6, 0.645))
    V8__u = V8__q_C/V8__C+V8__u_ext
    VV_junc5__vj2 = VV_junc5__vbc2
    VV_junc5__D1 = 2*V4__r
    VV_junc5__D2 = 2*VV_junc5__r_bc2
    VV_junc5__D3 = 2*PV9__r
    VV_junc5__D4 = 2*PV10__r
    VV_junc5__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc5__vj2/VV_junc5__v_scale)
    VV_junc5__w_out2 = 1-VV_junc5__w_in2
    VV_junc5__Qin2 = VV_junc5__w_in2*VV_junc5__vj2
    VV_junc5__Qout2 = VV_junc5__w_out2*-VV_junc5__vj2
    VV_junc5__q_us = np.pi*np.square(VV_junc5__r)*VV_junc5__l
    VV_junc5__q = VV_junc5__q_us+VV_junc5__q_C+VV_junc5__q_C_d
    VV_junc5__bc2_is_in = (1 if VV_junc5__Qin2 > VV_junc5__v_threshold else 0)
    VV_junc5__bc2_is_out = (1 if VV_junc5__Qout2 > VV_junc5__v_threshold else 0)
    VV_junc5__C_max12 = (V4__C if V4__C > VV_junc5__C_conn2 else (VV_junc5__C_conn2 if V4__C <= VV_junc5__C_conn2 else 0.0))
    PV9__R_constriction = PV9__R_constriction_base+(PV9__R_constriction_final-PV9__R_constriction_base)/(1+np.exp(-(environment__time-PV9__t0)/PV9__tau_sig))
    PV9__H_L_in = PV9__H_link_L
    PV9__H_R_in = PV9__H_link_R
    PV9__q_us = np.pi*np.square(PV9__r)*PV9__l
    PV9__q = PV9__q_us+PV9__q_C
    PV9__C = np.pi*np.square(8.5e-9)*PV9__l/133.322
    PV9__Z = (0.8+np.exp(-0.075*2*PV9__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV9__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV9__r*1e6, 12))
    PV9__mu_45 = 6*np.exp(-0.085*2*PV9__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV9__r*1e6, 0.645))
    PV9__u = PV9__q_C/PV9__C+PV9__u_ext
    PV10__R_constriction = PV10__R_constriction_base+(PV10__R_constriction_final-PV10__R_constriction_base)/(1+np.exp(-(environment__time-PV10__t0)/PV10__tau_sig))
    PV10__H_L_in = PV10__H_link_L
    PV10__H_R_in = PV10__H_link_R
    PV10__q_us = np.pi*np.square(PV10__r)*PV10__l
    PV10__q = PV10__q_us+PV10__q_C
    PV10__C = np.pi*np.square(8.5e-9)*PV10__l/133.322
    PV10__Z = (0.8+np.exp(-0.075*2*PV10__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV10__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV10__r*1e6, 12))
    PV10__mu_45 = 6*np.exp(-0.085*2*PV10__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV10__r*1e6, 0.645))
    PV10__u = PV10__q_C/PV10__C+PV10__u_ext
    V9__H_L_in = V9__H_link_L
    V9__H_R_in = V9__H_link_R
    V9__q_us = np.pi*np.square(V9__r)*V9__l
    V9__q = V9__q_us+V9__q_C
    V9__C = np.pi*np.square(8.5e-9)*V9__l/133.322
    V9__Z = (0.8+np.exp(-0.075*2*V9__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V9__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V9__r*1e6, 12))
    V9__mu_45 = 6*np.exp(-0.085*2*V9__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V9__r*1e6, 0.645))
    V9__u = V9__q_C/V9__C+V9__u_ext
    V10__H_L_in = V10__H_link_L
    V10__H_R_in = V10__H_link_R
    V10__q_us = np.pi*np.square(V10__r)*V10__l
    V10__q = V10__q_us+V10__q_C
    V10__C = np.pi*np.square(8.5e-9)*V10__l/133.322
    V10__Z = (0.8+np.exp(-0.075*2*V10__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V10__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V10__r*1e6, 12))
    V10__mu_45 = 6*np.exp(-0.085*2*V10__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V10__r*1e6, 0.645))
    V10__u = V10__q_C/V10__C+V10__u_ext
    VV_junc6__vj2 = VV_junc6__vbc2
    VV_junc6__D1 = 2*V5__r
    VV_junc6__D2 = 2*VV_junc6__r_bc2
    VV_junc6__D3 = 2*PV11__r
    VV_junc6__D4 = 2*PV12__r
    VV_junc6__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc6__vj2/VV_junc6__v_scale)
    VV_junc6__w_out2 = 1-VV_junc6__w_in2
    VV_junc6__Qin2 = VV_junc6__w_in2*VV_junc6__vj2
    VV_junc6__Qout2 = VV_junc6__w_out2*-VV_junc6__vj2
    VV_junc6__q_us = np.pi*np.square(VV_junc6__r)*VV_junc6__l
    VV_junc6__q = VV_junc6__q_us+VV_junc6__q_C+VV_junc6__q_C_d
    VV_junc6__bc2_is_in = (1 if VV_junc6__Qin2 > VV_junc6__v_threshold else 0)
    VV_junc6__bc2_is_out = (1 if VV_junc6__Qout2 > VV_junc6__v_threshold else 0)
    VV_junc6__C_max12 = (V5__C if V5__C > VV_junc6__C_conn2 else (VV_junc6__C_conn2 if V5__C <= VV_junc6__C_conn2 else 0.0))
    PV11__R_constriction = PV11__R_constriction_base+(PV11__R_constriction_final-PV11__R_constriction_base)/(1+np.exp(-(environment__time-PV11__t0)/PV11__tau_sig))
    PV11__H_L_in = PV11__H_link_L
    PV11__H_R_in = PV11__H_link_R
    PV11__q_us = np.pi*np.square(PV11__r)*PV11__l
    PV11__q = PV11__q_us+PV11__q_C
    PV11__C = np.pi*np.square(8.5e-9)*PV11__l/133.322
    PV11__Z = (0.8+np.exp(-0.075*2*PV11__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV11__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV11__r*1e6, 12))
    PV11__mu_45 = 6*np.exp(-0.085*2*PV11__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV11__r*1e6, 0.645))
    PV11__u = PV11__q_C/PV11__C+PV11__u_ext
    PV12__R_constriction = PV12__R_constriction_base+(PV12__R_constriction_final-PV12__R_constriction_base)/(1+np.exp(-(environment__time-PV12__t0)/PV12__tau_sig))
    PV12__H_L_in = PV12__H_link_L
    PV12__H_R_in = PV12__H_link_R
    PV12__q_us = np.pi*np.square(PV12__r)*PV12__l
    PV12__q = PV12__q_us+PV12__q_C
    PV12__C = np.pi*np.square(8.5e-9)*PV12__l/133.322
    PV12__Z = (0.8+np.exp(-0.075*2*PV12__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV12__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV12__r*1e6, 12))
    PV12__mu_45 = 6*np.exp(-0.085*2*PV12__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV12__r*1e6, 0.645))
    PV12__u = PV12__q_C/PV12__C+PV12__u_ext
    V11__H_L_in = V11__H_link_L
    V11__H_R_in = V11__H_link_R
    V11__q_us = np.pi*np.square(V11__r)*V11__l
    V11__q = V11__q_us+V11__q_C
    V11__C = np.pi*np.square(8.5e-9)*V11__l/133.322
    V11__Z = (0.8+np.exp(-0.075*2*V11__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V11__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V11__r*1e6, 12))
    V11__mu_45 = 6*np.exp(-0.085*2*V11__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V11__r*1e6, 0.645))
    V11__u = V11__q_C/V11__C+V11__u_ext
    V12__H_L_in = V12__H_link_L
    V12__H_R_in = V12__H_link_R
    V12__q_us = np.pi*np.square(V12__r)*V12__l
    V12__q = V12__q_us+V12__q_C
    V12__C = np.pi*np.square(8.5e-9)*V12__l/133.322
    V12__Z = (0.8+np.exp(-0.075*2*V12__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V12__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V12__r*1e6, 12))
    V12__mu_45 = 6*np.exp(-0.085*2*V12__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V12__r*1e6, 0.645))
    V12__u = V12__q_C/V12__C+V12__u_ext
    VV_junc7__vj2 = VV_junc7__vbc2
    VV_junc7__D1 = 2*V6__r
    VV_junc7__D2 = 2*VV_junc7__r_bc2
    VV_junc7__D3 = 2*PV13__r
    VV_junc7__D4 = 2*PV14__r
    VV_junc7__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc7__vj2/VV_junc7__v_scale)
    VV_junc7__w_out2 = 1-VV_junc7__w_in2
    VV_junc7__Qin2 = VV_junc7__w_in2*VV_junc7__vj2
    VV_junc7__Qout2 = VV_junc7__w_out2*-VV_junc7__vj2
    VV_junc7__q_us = np.pi*np.square(VV_junc7__r)*VV_junc7__l
    VV_junc7__q = VV_junc7__q_us+VV_junc7__q_C+VV_junc7__q_C_d
    VV_junc7__bc2_is_in = (1 if VV_junc7__Qin2 > VV_junc7__v_threshold else 0)
    VV_junc7__bc2_is_out = (1 if VV_junc7__Qout2 > VV_junc7__v_threshold else 0)
    VV_junc7__C_max12 = (V6__C if V6__C > VV_junc7__C_conn2 else (VV_junc7__C_conn2 if V6__C <= VV_junc7__C_conn2 else 0.0))
    PV13__R_constriction = PV13__R_constriction_base+(PV13__R_constriction_final-PV13__R_constriction_base)/(1+np.exp(-(environment__time-PV13__t0)/PV13__tau_sig))
    PV13__H_L_in = PV13__H_link_L
    PV13__H_R_in = PV13__H_link_R
    PV13__q_us = np.pi*np.square(PV13__r)*PV13__l
    PV13__q = PV13__q_us+PV13__q_C
    PV13__C = np.pi*np.square(8.5e-9)*PV13__l/133.322
    PV13__Z = (0.8+np.exp(-0.075*2*PV13__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV13__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV13__r*1e6, 12))
    PV13__mu_45 = 6*np.exp(-0.085*2*PV13__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV13__r*1e6, 0.645))
    PV13__u = PV13__q_C/PV13__C+PV13__u_ext
    PV14__R_constriction = PV14__R_constriction_base+(PV14__R_constriction_final-PV14__R_constriction_base)/(1+np.exp(-(environment__time-PV14__t0)/PV14__tau_sig))
    PV14__H_L_in = PV14__H_link_L
    PV14__H_R_in = PV14__H_link_R
    PV14__q_us = np.pi*np.square(PV14__r)*PV14__l
    PV14__q = PV14__q_us+PV14__q_C
    PV14__C = np.pi*np.square(8.5e-9)*PV14__l/133.322
    PV14__Z = (0.8+np.exp(-0.075*2*PV14__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV14__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV14__r*1e6, 12))
    PV14__mu_45 = 6*np.exp(-0.085*2*PV14__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV14__r*1e6, 0.645))
    PV14__u = PV14__q_C/PV14__C+PV14__u_ext
    V13__H_L_in = V13__H_link_L
    V13__H_R_in = V13__H_link_R
    V13__q_us = np.pi*np.square(V13__r)*V13__l
    V13__q = V13__q_us+V13__q_C
    V13__C = np.pi*np.square(8.5e-9)*V13__l/133.322
    V13__Z = (0.8+np.exp(-0.075*2*V13__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V13__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V13__r*1e6, 12))
    V13__mu_45 = 6*np.exp(-0.085*2*V13__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V13__r*1e6, 0.645))
    V13__u = V13__q_C/V13__C+V13__u_ext
    V14__H_L_in = V14__H_link_L
    V14__H_R_in = V14__H_link_R
    V14__q_us = np.pi*np.square(V14__r)*V14__l
    V14__q = V14__q_us+V14__q_C
    V14__C = np.pi*np.square(8.5e-9)*V14__l/133.322
    V14__Z = (0.8+np.exp(-0.075*2*V14__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V14__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V14__r*1e6, 12))
    V14__mu_45 = 6*np.exp(-0.085*2*V14__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V14__r*1e6, 0.645))
    V14__u = V14__q_C/V14__C+V14__u_ext
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
    VV_junc4__RBC_volume_init = VV_junc4__H_global_L*VV_junc4__q_us
    VV_junc4__H_mean = VV_junc4__RBC_volume/(VV_junc4__q_us+VV_junc4__div_0)
    VV_junc4__C_max123 = (VV_junc4__C_max12 if VV_junc4__C_max12 > PV7__C else (PV7__C if VV_junc4__C_max12 <= PV7__C else 0.0))
    VV_junc4__C = (VV_junc4__C_max123 if VV_junc4__C_max123 > PV8__C else (PV8__C if VV_junc4__C_max123 <= PV8__C else 0.0))
    PV7__RBC_volume_init = PV7__H_global_L*PV7__q_us
    PV7__H_mean = PV7__RBC_volume/PV7__q
    PV7__hem_dep_u_rel = 1+(PV7__mu_45-1)*(safe_power(1-PV7__H_mean, PV7__Z)-1)/(safe_power(1-PV7__H_global_L, PV7__Z)-1)*np.square(2*PV7__r*1e6/(2*PV7__r*1e6-1.1))
    PV7__u_mmHg = PV7__u/133.322
    PV8__RBC_volume_init = PV8__H_global_L*PV8__q_us
    PV8__H_mean = PV8__RBC_volume/PV8__q
    PV8__hem_dep_u_rel = 1+(PV8__mu_45-1)*(safe_power(1-PV8__H_mean, PV8__Z)-1)/(safe_power(1-PV8__H_global_L, PV8__Z)-1)*np.square(2*PV8__r*1e6/(2*PV8__r*1e6-1.1))
    PV8__u_mmHg = PV8__u/133.322
    V7__RBC_volume_init = V7__H_global_L*V7__q_us
    V7__H_mean = V7__RBC_volume/V7__q
    V7__hem_dep_u_rel = 1+(V7__mu_45-1)*(safe_power(1-V7__H_mean, V7__Z)-1)/(safe_power(1-V7__H_global_L, V7__Z)-1)*np.square(2*V7__r*1e6/(2*V7__r*1e6-1.1))
    V7__u_mmHg = V7__u/133.322
    V8__RBC_volume_init = V8__H_global_L*V8__q_us
    V8__H_mean = V8__RBC_volume/V8__q
    V8__hem_dep_u_rel = 1+(V8__mu_45-1)*(safe_power(1-V8__H_mean, V8__Z)-1)/(safe_power(1-V8__H_global_L, V8__Z)-1)*np.square(2*V8__r*1e6/(2*V8__r*1e6-1.1))
    V8__u_mmHg = V8__u/133.322
    VV_junc5__RBC_volume_init = VV_junc5__H_global_L*VV_junc5__q_us
    VV_junc5__H_mean = VV_junc5__RBC_volume/(VV_junc5__q_us+VV_junc5__div_0)
    VV_junc5__C_max123 = (VV_junc5__C_max12 if VV_junc5__C_max12 > PV9__C else (PV9__C if VV_junc5__C_max12 <= PV9__C else 0.0))
    VV_junc5__C = (VV_junc5__C_max123 if VV_junc5__C_max123 > PV10__C else (PV10__C if VV_junc5__C_max123 <= PV10__C else 0.0))
    PV9__RBC_volume_init = PV9__H_global_L*PV9__q_us
    PV9__H_mean = PV9__RBC_volume/PV9__q
    PV9__hem_dep_u_rel = 1+(PV9__mu_45-1)*(safe_power(1-PV9__H_mean, PV9__Z)-1)/(safe_power(1-PV9__H_global_L, PV9__Z)-1)*np.square(2*PV9__r*1e6/(2*PV9__r*1e6-1.1))
    PV9__u_mmHg = PV9__u/133.322
    PV10__RBC_volume_init = PV10__H_global_L*PV10__q_us
    PV10__H_mean = PV10__RBC_volume/PV10__q
    PV10__hem_dep_u_rel = 1+(PV10__mu_45-1)*(safe_power(1-PV10__H_mean, PV10__Z)-1)/(safe_power(1-PV10__H_global_L, PV10__Z)-1)*np.square(2*PV10__r*1e6/(2*PV10__r*1e6-1.1))
    PV10__u_mmHg = PV10__u/133.322
    V9__RBC_volume_init = V9__H_global_L*V9__q_us
    V9__H_mean = V9__RBC_volume/V9__q
    V9__hem_dep_u_rel = 1+(V9__mu_45-1)*(safe_power(1-V9__H_mean, V9__Z)-1)/(safe_power(1-V9__H_global_L, V9__Z)-1)*np.square(2*V9__r*1e6/(2*V9__r*1e6-1.1))
    V9__u_mmHg = V9__u/133.322
    V10__RBC_volume_init = V10__H_global_L*V10__q_us
    V10__H_mean = V10__RBC_volume/V10__q
    V10__hem_dep_u_rel = 1+(V10__mu_45-1)*(safe_power(1-V10__H_mean, V10__Z)-1)/(safe_power(1-V10__H_global_L, V10__Z)-1)*np.square(2*V10__r*1e6/(2*V10__r*1e6-1.1))
    V10__u_mmHg = V10__u/133.322
    VV_junc6__RBC_volume_init = VV_junc6__H_global_L*VV_junc6__q_us
    VV_junc6__H_mean = VV_junc6__RBC_volume/(VV_junc6__q_us+VV_junc6__div_0)
    VV_junc6__C_max123 = (VV_junc6__C_max12 if VV_junc6__C_max12 > PV11__C else (PV11__C if VV_junc6__C_max12 <= PV11__C else 0.0))
    VV_junc6__C = (VV_junc6__C_max123 if VV_junc6__C_max123 > PV12__C else (PV12__C if VV_junc6__C_max123 <= PV12__C else 0.0))
    PV11__RBC_volume_init = PV11__H_global_L*PV11__q_us
    PV11__H_mean = PV11__RBC_volume/PV11__q
    PV11__hem_dep_u_rel = 1+(PV11__mu_45-1)*(safe_power(1-PV11__H_mean, PV11__Z)-1)/(safe_power(1-PV11__H_global_L, PV11__Z)-1)*np.square(2*PV11__r*1e6/(2*PV11__r*1e6-1.1))
    PV11__u_mmHg = PV11__u/133.322
    PV12__RBC_volume_init = PV12__H_global_L*PV12__q_us
    PV12__H_mean = PV12__RBC_volume/PV12__q
    PV12__hem_dep_u_rel = 1+(PV12__mu_45-1)*(safe_power(1-PV12__H_mean, PV12__Z)-1)/(safe_power(1-PV12__H_global_L, PV12__Z)-1)*np.square(2*PV12__r*1e6/(2*PV12__r*1e6-1.1))
    PV12__u_mmHg = PV12__u/133.322
    V11__RBC_volume_init = V11__H_global_L*V11__q_us
    V11__H_mean = V11__RBC_volume/V11__q
    V11__hem_dep_u_rel = 1+(V11__mu_45-1)*(safe_power(1-V11__H_mean, V11__Z)-1)/(safe_power(1-V11__H_global_L, V11__Z)-1)*np.square(2*V11__r*1e6/(2*V11__r*1e6-1.1))
    V11__u_mmHg = V11__u/133.322
    V12__RBC_volume_init = V12__H_global_L*V12__q_us
    V12__H_mean = V12__RBC_volume/V12__q
    V12__hem_dep_u_rel = 1+(V12__mu_45-1)*(safe_power(1-V12__H_mean, V12__Z)-1)/(safe_power(1-V12__H_global_L, V12__Z)-1)*np.square(2*V12__r*1e6/(2*V12__r*1e6-1.1))
    V12__u_mmHg = V12__u/133.322
    VV_junc7__RBC_volume_init = VV_junc7__H_global_L*VV_junc7__q_us
    VV_junc7__H_mean = VV_junc7__RBC_volume/(VV_junc7__q_us+VV_junc7__div_0)
    VV_junc7__C_max123 = (VV_junc7__C_max12 if VV_junc7__C_max12 > PV13__C else (PV13__C if VV_junc7__C_max12 <= PV13__C else 0.0))
    VV_junc7__C = (VV_junc7__C_max123 if VV_junc7__C_max123 > PV14__C else (PV14__C if VV_junc7__C_max123 <= PV14__C else 0.0))
    PV13__RBC_volume_init = PV13__H_global_L*PV13__q_us
    PV13__H_mean = PV13__RBC_volume/PV13__q
    PV13__hem_dep_u_rel = 1+(PV13__mu_45-1)*(safe_power(1-PV13__H_mean, PV13__Z)-1)/(safe_power(1-PV13__H_global_L, PV13__Z)-1)*np.square(2*PV13__r*1e6/(2*PV13__r*1e6-1.1))
    PV13__u_mmHg = PV13__u/133.322
    PV14__RBC_volume_init = PV14__H_global_L*PV14__q_us
    PV14__H_mean = PV14__RBC_volume/PV14__q
    PV14__hem_dep_u_rel = 1+(PV14__mu_45-1)*(safe_power(1-PV14__H_mean, PV14__Z)-1)/(safe_power(1-PV14__H_global_L, PV14__Z)-1)*np.square(2*PV14__r*1e6/(2*PV14__r*1e6-1.1))
    PV14__u_mmHg = PV14__u/133.322
    V13__RBC_volume_init = V13__H_global_L*V13__q_us
    V13__H_mean = V13__RBC_volume/V13__q
    V13__hem_dep_u_rel = 1+(V13__mu_45-1)*(safe_power(1-V13__H_mean, V13__Z)-1)/(safe_power(1-V13__H_global_L, V13__Z)-1)*np.square(2*V13__r*1e6/(2*V13__r*1e6-1.1))
    V13__u_mmHg = V13__u/133.322
    V14__RBC_volume_init = V14__H_global_L*V14__q_us
    V14__H_mean = V14__RBC_volume/V14__q
    V14__hem_dep_u_rel = 1+(V14__mu_45-1)*(safe_power(1-V14__H_mean, V14__Z)-1)/(safe_power(1-V14__H_global_L, V14__Z)-1)*np.square(2*V14__r*1e6/(2*V14__r*1e6-1.1))
    V14__u_mmHg = V14__u/133.322
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
    V4__mu = V4__hem_dep_u_rel*V4__mu_plasma
    V4__R = 8*V4__mu*V4__l/(np.pi*safe_power(V4__r, 4))
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
    V6__mu = V6__hem_dep_u_rel*V6__mu_plasma
    V6__R = 8*V6__mu*V6__l/(np.pi*safe_power(V6__r, 4))
    VV_junc4__u = VV_junc4__q_C/(VV_junc4__C/2)+VV_junc4__u_ext
    VV_junc4__u_mmHg = VV_junc4__u/133.322
    VV_junc4__u_d = VV_junc4__q_C_d/(VV_junc4__C/2)+VV_junc4__u_ext
    VV_junc4__u_d_mmHg = VV_junc4__u_d/133.322
    PV7__mu = PV7__hem_dep_u_rel*PV7__mu_plasma
    PV7__R = 8*PV7__mu*PV7__l/(np.pi*safe_power(PV7__r, 4))+PV7__R_constriction
    PV7__v = (VV_junc4__u_d-PV7__u)/(PV7__R/2)
    PV7__v_d = (PV7__u-V7__u)/(PV7__R/2)
    PV8__mu = PV8__hem_dep_u_rel*PV8__mu_plasma
    PV8__R = 8*PV8__mu*PV8__l/(np.pi*safe_power(PV8__r, 4))+PV8__R_constriction
    PV8__v = (VV_junc4__u_d-PV8__u)/(PV8__R/2)
    PV8__v_d = (PV8__u-V8__u)/(PV8__R/2)
    V7__mu = V7__hem_dep_u_rel*V7__mu_plasma
    V7__R = 8*V7__mu*V7__l/(np.pi*safe_power(V7__r, 4))
    V7__v = (V7__u-V7__u_out)/V7__R
    V8__mu = V8__hem_dep_u_rel*V8__mu_plasma
    V8__R = 8*V8__mu*V8__l/(np.pi*safe_power(V8__r, 4))
    V8__v = (V8__u-V8__u_out)/V8__R
    VV_junc5__u = VV_junc5__q_C/(VV_junc5__C/2)+VV_junc5__u_ext
    VV_junc5__u_mmHg = VV_junc5__u/133.322
    VV_junc5__u_d = VV_junc5__q_C_d/(VV_junc5__C/2)+VV_junc5__u_ext
    VV_junc5__u_d_mmHg = VV_junc5__u_d/133.322
    PV9__mu = PV9__hem_dep_u_rel*PV9__mu_plasma
    PV9__R = 8*PV9__mu*PV9__l/(np.pi*safe_power(PV9__r, 4))+PV9__R_constriction
    PV9__v = (VV_junc5__u_d-PV9__u)/(PV9__R/2)
    PV9__v_d = (PV9__u-V9__u)/(PV9__R/2)
    PV10__mu = PV10__hem_dep_u_rel*PV10__mu_plasma
    PV10__R = 8*PV10__mu*PV10__l/(np.pi*safe_power(PV10__r, 4))+PV10__R_constriction
    PV10__v = (VV_junc5__u_d-PV10__u)/(PV10__R/2)
    PV10__v_d = (PV10__u-V10__u)/(PV10__R/2)
    V9__mu = V9__hem_dep_u_rel*V9__mu_plasma
    V9__R = 8*V9__mu*V9__l/(np.pi*safe_power(V9__r, 4))
    V9__v = (V9__u-V9__u_out)/V9__R
    V10__mu = V10__hem_dep_u_rel*V10__mu_plasma
    V10__R = 8*V10__mu*V10__l/(np.pi*safe_power(V10__r, 4))
    V10__v = (V10__u-V10__u_out)/V10__R
    VV_junc6__u = VV_junc6__q_C/(VV_junc6__C/2)+VV_junc6__u_ext
    VV_junc6__u_mmHg = VV_junc6__u/133.322
    VV_junc6__u_d = VV_junc6__q_C_d/(VV_junc6__C/2)+VV_junc6__u_ext
    VV_junc6__u_d_mmHg = VV_junc6__u_d/133.322
    PV11__mu = PV11__hem_dep_u_rel*PV11__mu_plasma
    PV11__R = 8*PV11__mu*PV11__l/(np.pi*safe_power(PV11__r, 4))+PV11__R_constriction
    PV11__v = (VV_junc6__u_d-PV11__u)/(PV11__R/2)
    PV11__v_d = (PV11__u-V11__u)/(PV11__R/2)
    PV12__mu = PV12__hem_dep_u_rel*PV12__mu_plasma
    PV12__R = 8*PV12__mu*PV12__l/(np.pi*safe_power(PV12__r, 4))+PV12__R_constriction
    PV12__v = (VV_junc6__u_d-PV12__u)/(PV12__R/2)
    PV12__v_d = (PV12__u-V12__u)/(PV12__R/2)
    V11__mu = V11__hem_dep_u_rel*V11__mu_plasma
    V11__R = 8*V11__mu*V11__l/(np.pi*safe_power(V11__r, 4))
    V11__v = (V11__u-V11__u_out)/V11__R
    V12__mu = V12__hem_dep_u_rel*V12__mu_plasma
    V12__R = 8*V12__mu*V12__l/(np.pi*safe_power(V12__r, 4))
    V12__v = (V12__u-V12__u_out)/V12__R
    VV_junc7__u = VV_junc7__q_C/(VV_junc7__C/2)+VV_junc7__u_ext
    VV_junc7__u_mmHg = VV_junc7__u/133.322
    VV_junc7__u_d = VV_junc7__q_C_d/(VV_junc7__C/2)+VV_junc7__u_ext
    VV_junc7__u_d_mmHg = VV_junc7__u_d/133.322
    PV13__mu = PV13__hem_dep_u_rel*PV13__mu_plasma
    PV13__R = 8*PV13__mu*PV13__l/(np.pi*safe_power(PV13__r, 4))+PV13__R_constriction
    PV13__v = (VV_junc7__u_d-PV13__u)/(PV13__R/2)
    PV13__v_d = (PV13__u-V13__u)/(PV13__R/2)
    PV14__mu = PV14__hem_dep_u_rel*PV14__mu_plasma
    PV14__R = 8*PV14__mu*PV14__l/(np.pi*safe_power(PV14__r, 4))+PV14__R_constriction
    PV14__v = (VV_junc7__u_d-PV14__u)/(PV14__R/2)
    PV14__v_d = (PV14__u-V14__u)/(PV14__R/2)
    V13__mu = V13__hem_dep_u_rel*V13__mu_plasma
    V13__R = 8*V13__mu*V13__l/(np.pi*safe_power(V13__r, 4))
    V13__v = (V13__u-V13__u_out)/V13__R
    V14__mu = V14__hem_dep_u_rel*V14__mu_plasma
    V14__R = 8*V14__mu*V14__l/(np.pi*safe_power(V14__r, 4))
    V14__v = (V14__u-V14__u_out)/V14__R
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
    V3__v = (V3__u-VV_junc4__u)/V3__R
    V4__v = (V4__u-VV_junc5__u)/V4__R
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
    V5__v = (V5__u-VV_junc6__u)/V5__R
    V6__v = (V6__u-VV_junc7__u)/V6__R
    VV_junc4__vj1 = V3__v
    VV_junc4__vj3 = -PV7__v
    VV_junc4__vj4 = -PV8__v
    VV_junc4__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc4__vj1/VV_junc4__v_scale)
    VV_junc4__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc4__vj3/VV_junc4__v_scale)
    VV_junc4__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc4__vj4/VV_junc4__v_scale)
    VV_junc4__w_out1 = 1-VV_junc4__w_in1
    VV_junc4__w_out3 = 1-VV_junc4__w_in3
    VV_junc4__w_out4 = 1-VV_junc4__w_in4
    VV_junc4__Qin1 = VV_junc4__w_in1*VV_junc4__vj1
    VV_junc4__Qin3 = VV_junc4__w_in3*VV_junc4__vj3
    VV_junc4__Qin4 = VV_junc4__w_in4*VV_junc4__vj4
    VV_junc4__Qout1 = VV_junc4__w_out1*-VV_junc4__vj1
    VV_junc4__Qout3 = VV_junc4__w_out3*-VV_junc4__vj3
    VV_junc4__Qout4 = VV_junc4__w_out4*-VV_junc4__vj4
    VV_junc4__Qin_tot = VV_junc4__Qin1+VV_junc4__Qin2+VV_junc4__Qin3+VV_junc4__Qin4
    VV_junc4__Qout_tot = VV_junc4__Qout1+VV_junc4__Qout2+VV_junc4__Qout3+VV_junc4__Qout4
    VV_junc4__v = (VV_junc4__u-VV_junc4__u_d)/VV_junc4__R_VV_junc
    VV_junc4__bc1_is_in = (1 if VV_junc4__Qin1 > VV_junc4__v_threshold else 0)
    VV_junc4__bc3_is_in = (1 if VV_junc4__Qin3 > VV_junc4__v_threshold else 0)
    VV_junc4__bc4_is_in = (1 if VV_junc4__Qin4 > VV_junc4__v_threshold else 0)
    VV_junc4__bc1_is_out = (1 if VV_junc4__Qout1 > VV_junc4__v_threshold else 0)
    VV_junc4__bc3_is_out = (1 if VV_junc4__Qout3 > VV_junc4__v_threshold else 0)
    VV_junc4__bc4_is_out = (1 if VV_junc4__Qout4 > VV_junc4__v_threshold else 0)
    PV7__w_v = 0.5+1/np.pi*np.arctan(PV7__v/PV7__v_scale)
    PV7__w_v_d = 0.5+1/np.pi*np.arctan(PV7__v_d/PV7__v_scale)
    PV7__H_up = PV7__w_v_d*PV7__H_L_in+(1-PV7__w_v_d)*PV7__H_R_in
    PV7__s_v_d = np.abs(PV7__v_d)/(np.abs(PV7__v_d)+PV7__v_eps)
    PV7__H_L_out = (1-PV7__w_v_d)*PV7__H_down+PV7__w_v_d*PV7__H_L_in
    PV7__H_R_out = PV7__w_v_d*PV7__H_down+(1-PV7__w_v_d)*PV7__H_R_in
    PV7__v_pos = PV7__w_v*PV7__v
    PV7__v_neg = (1-PV7__w_v)*-PV7__v
    PV7__v_d_pos = PV7__w_v_d*PV7__v_d
    PV7__v_d_neg = (1-PV7__w_v_d)*-PV7__v_d
    PV7__H_volume_L = PV7__w_v*PV7__H_L_in+(1-PV7__w_v)*PV7__H_L_out
    PV7__H_volume_R = PV7__w_v_d*PV7__H_R_out+(1-PV7__w_v_d)*PV7__H_R_in
    PV7__v_mm3_s = PV7__v/PV7__one_mm3
    PV7__v_d_mm3_s = PV7__v_d/PV7__one_mm3
    PV8__w_v = 0.5+1/np.pi*np.arctan(PV8__v/PV8__v_scale)
    PV8__w_v_d = 0.5+1/np.pi*np.arctan(PV8__v_d/PV8__v_scale)
    PV8__H_up = PV8__w_v_d*PV8__H_L_in+(1-PV8__w_v_d)*PV8__H_R_in
    PV8__s_v_d = np.abs(PV8__v_d)/(np.abs(PV8__v_d)+PV8__v_eps)
    PV8__H_L_out = (1-PV8__w_v_d)*PV8__H_down+PV8__w_v_d*PV8__H_L_in
    PV8__H_R_out = PV8__w_v_d*PV8__H_down+(1-PV8__w_v_d)*PV8__H_R_in
    PV8__v_pos = PV8__w_v*PV8__v
    PV8__v_neg = (1-PV8__w_v)*-PV8__v
    PV8__v_d_pos = PV8__w_v_d*PV8__v_d
    PV8__v_d_neg = (1-PV8__w_v_d)*-PV8__v_d
    PV8__H_volume_L = PV8__w_v*PV8__H_L_in+(1-PV8__w_v)*PV8__H_L_out
    PV8__H_volume_R = PV8__w_v_d*PV8__H_R_out+(1-PV8__w_v_d)*PV8__H_R_in
    PV8__v_mm3_s = PV8__v/PV8__one_mm3
    PV8__v_d_mm3_s = PV8__v_d/PV8__one_mm3
    V7__w_v = 0.5+1/np.pi*np.arctan(V7__v/V7__v_scale)
    V7__H_up = V7__w_v*V7__H_L_in+(1-V7__w_v)*V7__H_R_in
    V7__s_v = np.abs(V7__v)/(np.abs(V7__v)+V7__v_eps)
    V7__H_L_out = (1-V7__w_v)*V7__H_down+V7__w_v*V7__H_L_in
    V7__H_R_out = V7__w_v*V7__H_down+(1-V7__w_v)*V7__H_R_in
    V7__v_pos = V7__w_v*V7__v
    V7__v_neg = (1-V7__w_v)*-V7__v
    V7__H_volume_L = V7__w_v*V7__H_L_in+(1-V7__w_v)*V7__H_L_out
    V7__H_volume_R = V7__w_v*V7__H_R_out+(1-V7__w_v)*V7__H_R_in
    V7__v_mm3_s = V7__v/V7__one_mm3
    V8__w_v = 0.5+1/np.pi*np.arctan(V8__v/V8__v_scale)
    V8__H_up = V8__w_v*V8__H_L_in+(1-V8__w_v)*V8__H_R_in
    V8__s_v = np.abs(V8__v)/(np.abs(V8__v)+V8__v_eps)
    V8__H_L_out = (1-V8__w_v)*V8__H_down+V8__w_v*V8__H_L_in
    V8__H_R_out = V8__w_v*V8__H_down+(1-V8__w_v)*V8__H_R_in
    V8__v_pos = V8__w_v*V8__v
    V8__v_neg = (1-V8__w_v)*-V8__v
    V8__H_volume_L = V8__w_v*V8__H_L_in+(1-V8__w_v)*V8__H_L_out
    V8__H_volume_R = V8__w_v*V8__H_R_out+(1-V8__w_v)*V8__H_R_in
    V8__v_mm3_s = V8__v/V8__one_mm3
    VV_junc5__vj1 = V4__v
    VV_junc5__vj3 = -PV9__v
    VV_junc5__vj4 = -PV10__v
    VV_junc5__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc5__vj1/VV_junc5__v_scale)
    VV_junc5__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc5__vj3/VV_junc5__v_scale)
    VV_junc5__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc5__vj4/VV_junc5__v_scale)
    VV_junc5__w_out1 = 1-VV_junc5__w_in1
    VV_junc5__w_out3 = 1-VV_junc5__w_in3
    VV_junc5__w_out4 = 1-VV_junc5__w_in4
    VV_junc5__Qin1 = VV_junc5__w_in1*VV_junc5__vj1
    VV_junc5__Qin3 = VV_junc5__w_in3*VV_junc5__vj3
    VV_junc5__Qin4 = VV_junc5__w_in4*VV_junc5__vj4
    VV_junc5__Qout1 = VV_junc5__w_out1*-VV_junc5__vj1
    VV_junc5__Qout3 = VV_junc5__w_out3*-VV_junc5__vj3
    VV_junc5__Qout4 = VV_junc5__w_out4*-VV_junc5__vj4
    VV_junc5__Qin_tot = VV_junc5__Qin1+VV_junc5__Qin2+VV_junc5__Qin3+VV_junc5__Qin4
    VV_junc5__Qout_tot = VV_junc5__Qout1+VV_junc5__Qout2+VV_junc5__Qout3+VV_junc5__Qout4
    VV_junc5__v = (VV_junc5__u-VV_junc5__u_d)/VV_junc5__R_VV_junc
    VV_junc5__bc1_is_in = (1 if VV_junc5__Qin1 > VV_junc5__v_threshold else 0)
    VV_junc5__bc3_is_in = (1 if VV_junc5__Qin3 > VV_junc5__v_threshold else 0)
    VV_junc5__bc4_is_in = (1 if VV_junc5__Qin4 > VV_junc5__v_threshold else 0)
    VV_junc5__bc1_is_out = (1 if VV_junc5__Qout1 > VV_junc5__v_threshold else 0)
    VV_junc5__bc3_is_out = (1 if VV_junc5__Qout3 > VV_junc5__v_threshold else 0)
    VV_junc5__bc4_is_out = (1 if VV_junc5__Qout4 > VV_junc5__v_threshold else 0)
    PV9__w_v = 0.5+1/np.pi*np.arctan(PV9__v/PV9__v_scale)
    PV9__w_v_d = 0.5+1/np.pi*np.arctan(PV9__v_d/PV9__v_scale)
    PV9__H_up = PV9__w_v_d*PV9__H_L_in+(1-PV9__w_v_d)*PV9__H_R_in
    PV9__s_v_d = np.abs(PV9__v_d)/(np.abs(PV9__v_d)+PV9__v_eps)
    PV9__H_L_out = (1-PV9__w_v_d)*PV9__H_down+PV9__w_v_d*PV9__H_L_in
    PV9__H_R_out = PV9__w_v_d*PV9__H_down+(1-PV9__w_v_d)*PV9__H_R_in
    PV9__v_pos = PV9__w_v*PV9__v
    PV9__v_neg = (1-PV9__w_v)*-PV9__v
    PV9__v_d_pos = PV9__w_v_d*PV9__v_d
    PV9__v_d_neg = (1-PV9__w_v_d)*-PV9__v_d
    PV9__H_volume_L = PV9__w_v*PV9__H_L_in+(1-PV9__w_v)*PV9__H_L_out
    PV9__H_volume_R = PV9__w_v_d*PV9__H_R_out+(1-PV9__w_v_d)*PV9__H_R_in
    PV9__v_mm3_s = PV9__v/PV9__one_mm3
    PV9__v_d_mm3_s = PV9__v_d/PV9__one_mm3
    PV10__w_v = 0.5+1/np.pi*np.arctan(PV10__v/PV10__v_scale)
    PV10__w_v_d = 0.5+1/np.pi*np.arctan(PV10__v_d/PV10__v_scale)
    PV10__H_up = PV10__w_v_d*PV10__H_L_in+(1-PV10__w_v_d)*PV10__H_R_in
    PV10__s_v_d = np.abs(PV10__v_d)/(np.abs(PV10__v_d)+PV10__v_eps)
    PV10__H_L_out = (1-PV10__w_v_d)*PV10__H_down+PV10__w_v_d*PV10__H_L_in
    PV10__H_R_out = PV10__w_v_d*PV10__H_down+(1-PV10__w_v_d)*PV10__H_R_in
    PV10__v_pos = PV10__w_v*PV10__v
    PV10__v_neg = (1-PV10__w_v)*-PV10__v
    PV10__v_d_pos = PV10__w_v_d*PV10__v_d
    PV10__v_d_neg = (1-PV10__w_v_d)*-PV10__v_d
    PV10__H_volume_L = PV10__w_v*PV10__H_L_in+(1-PV10__w_v)*PV10__H_L_out
    PV10__H_volume_R = PV10__w_v_d*PV10__H_R_out+(1-PV10__w_v_d)*PV10__H_R_in
    PV10__v_mm3_s = PV10__v/PV10__one_mm3
    PV10__v_d_mm3_s = PV10__v_d/PV10__one_mm3
    V9__w_v = 0.5+1/np.pi*np.arctan(V9__v/V9__v_scale)
    V9__H_up = V9__w_v*V9__H_L_in+(1-V9__w_v)*V9__H_R_in
    V9__s_v = np.abs(V9__v)/(np.abs(V9__v)+V9__v_eps)
    V9__H_L_out = (1-V9__w_v)*V9__H_down+V9__w_v*V9__H_L_in
    V9__H_R_out = V9__w_v*V9__H_down+(1-V9__w_v)*V9__H_R_in
    V9__v_pos = V9__w_v*V9__v
    V9__v_neg = (1-V9__w_v)*-V9__v
    V9__H_volume_L = V9__w_v*V9__H_L_in+(1-V9__w_v)*V9__H_L_out
    V9__H_volume_R = V9__w_v*V9__H_R_out+(1-V9__w_v)*V9__H_R_in
    V9__v_mm3_s = V9__v/V9__one_mm3
    V10__w_v = 0.5+1/np.pi*np.arctan(V10__v/V10__v_scale)
    V10__H_up = V10__w_v*V10__H_L_in+(1-V10__w_v)*V10__H_R_in
    V10__s_v = np.abs(V10__v)/(np.abs(V10__v)+V10__v_eps)
    V10__H_L_out = (1-V10__w_v)*V10__H_down+V10__w_v*V10__H_L_in
    V10__H_R_out = V10__w_v*V10__H_down+(1-V10__w_v)*V10__H_R_in
    V10__v_pos = V10__w_v*V10__v
    V10__v_neg = (1-V10__w_v)*-V10__v
    V10__H_volume_L = V10__w_v*V10__H_L_in+(1-V10__w_v)*V10__H_L_out
    V10__H_volume_R = V10__w_v*V10__H_R_out+(1-V10__w_v)*V10__H_R_in
    V10__v_mm3_s = V10__v/V10__one_mm3
    VV_junc6__vj1 = V5__v
    VV_junc6__vj3 = -PV11__v
    VV_junc6__vj4 = -PV12__v
    VV_junc6__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc6__vj1/VV_junc6__v_scale)
    VV_junc6__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc6__vj3/VV_junc6__v_scale)
    VV_junc6__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc6__vj4/VV_junc6__v_scale)
    VV_junc6__w_out1 = 1-VV_junc6__w_in1
    VV_junc6__w_out3 = 1-VV_junc6__w_in3
    VV_junc6__w_out4 = 1-VV_junc6__w_in4
    VV_junc6__Qin1 = VV_junc6__w_in1*VV_junc6__vj1
    VV_junc6__Qin3 = VV_junc6__w_in3*VV_junc6__vj3
    VV_junc6__Qin4 = VV_junc6__w_in4*VV_junc6__vj4
    VV_junc6__Qout1 = VV_junc6__w_out1*-VV_junc6__vj1
    VV_junc6__Qout3 = VV_junc6__w_out3*-VV_junc6__vj3
    VV_junc6__Qout4 = VV_junc6__w_out4*-VV_junc6__vj4
    VV_junc6__Qin_tot = VV_junc6__Qin1+VV_junc6__Qin2+VV_junc6__Qin3+VV_junc6__Qin4
    VV_junc6__Qout_tot = VV_junc6__Qout1+VV_junc6__Qout2+VV_junc6__Qout3+VV_junc6__Qout4
    VV_junc6__v = (VV_junc6__u-VV_junc6__u_d)/VV_junc6__R_VV_junc
    VV_junc6__bc1_is_in = (1 if VV_junc6__Qin1 > VV_junc6__v_threshold else 0)
    VV_junc6__bc3_is_in = (1 if VV_junc6__Qin3 > VV_junc6__v_threshold else 0)
    VV_junc6__bc4_is_in = (1 if VV_junc6__Qin4 > VV_junc6__v_threshold else 0)
    VV_junc6__bc1_is_out = (1 if VV_junc6__Qout1 > VV_junc6__v_threshold else 0)
    VV_junc6__bc3_is_out = (1 if VV_junc6__Qout3 > VV_junc6__v_threshold else 0)
    VV_junc6__bc4_is_out = (1 if VV_junc6__Qout4 > VV_junc6__v_threshold else 0)
    PV11__w_v = 0.5+1/np.pi*np.arctan(PV11__v/PV11__v_scale)
    PV11__w_v_d = 0.5+1/np.pi*np.arctan(PV11__v_d/PV11__v_scale)
    PV11__H_up = PV11__w_v_d*PV11__H_L_in+(1-PV11__w_v_d)*PV11__H_R_in
    PV11__s_v_d = np.abs(PV11__v_d)/(np.abs(PV11__v_d)+PV11__v_eps)
    PV11__H_L_out = (1-PV11__w_v_d)*PV11__H_down+PV11__w_v_d*PV11__H_L_in
    PV11__H_R_out = PV11__w_v_d*PV11__H_down+(1-PV11__w_v_d)*PV11__H_R_in
    PV11__v_pos = PV11__w_v*PV11__v
    PV11__v_neg = (1-PV11__w_v)*-PV11__v
    PV11__v_d_pos = PV11__w_v_d*PV11__v_d
    PV11__v_d_neg = (1-PV11__w_v_d)*-PV11__v_d
    PV11__H_volume_L = PV11__w_v*PV11__H_L_in+(1-PV11__w_v)*PV11__H_L_out
    PV11__H_volume_R = PV11__w_v_d*PV11__H_R_out+(1-PV11__w_v_d)*PV11__H_R_in
    PV11__v_mm3_s = PV11__v/PV11__one_mm3
    PV11__v_d_mm3_s = PV11__v_d/PV11__one_mm3
    PV12__w_v = 0.5+1/np.pi*np.arctan(PV12__v/PV12__v_scale)
    PV12__w_v_d = 0.5+1/np.pi*np.arctan(PV12__v_d/PV12__v_scale)
    PV12__H_up = PV12__w_v_d*PV12__H_L_in+(1-PV12__w_v_d)*PV12__H_R_in
    PV12__s_v_d = np.abs(PV12__v_d)/(np.abs(PV12__v_d)+PV12__v_eps)
    PV12__H_L_out = (1-PV12__w_v_d)*PV12__H_down+PV12__w_v_d*PV12__H_L_in
    PV12__H_R_out = PV12__w_v_d*PV12__H_down+(1-PV12__w_v_d)*PV12__H_R_in
    PV12__v_pos = PV12__w_v*PV12__v
    PV12__v_neg = (1-PV12__w_v)*-PV12__v
    PV12__v_d_pos = PV12__w_v_d*PV12__v_d
    PV12__v_d_neg = (1-PV12__w_v_d)*-PV12__v_d
    PV12__H_volume_L = PV12__w_v*PV12__H_L_in+(1-PV12__w_v)*PV12__H_L_out
    PV12__H_volume_R = PV12__w_v_d*PV12__H_R_out+(1-PV12__w_v_d)*PV12__H_R_in
    PV12__v_mm3_s = PV12__v/PV12__one_mm3
    PV12__v_d_mm3_s = PV12__v_d/PV12__one_mm3
    V11__w_v = 0.5+1/np.pi*np.arctan(V11__v/V11__v_scale)
    V11__H_up = V11__w_v*V11__H_L_in+(1-V11__w_v)*V11__H_R_in
    V11__s_v = np.abs(V11__v)/(np.abs(V11__v)+V11__v_eps)
    V11__H_L_out = (1-V11__w_v)*V11__H_down+V11__w_v*V11__H_L_in
    V11__H_R_out = V11__w_v*V11__H_down+(1-V11__w_v)*V11__H_R_in
    V11__v_pos = V11__w_v*V11__v
    V11__v_neg = (1-V11__w_v)*-V11__v
    V11__H_volume_L = V11__w_v*V11__H_L_in+(1-V11__w_v)*V11__H_L_out
    V11__H_volume_R = V11__w_v*V11__H_R_out+(1-V11__w_v)*V11__H_R_in
    V11__v_mm3_s = V11__v/V11__one_mm3
    V12__w_v = 0.5+1/np.pi*np.arctan(V12__v/V12__v_scale)
    V12__H_up = V12__w_v*V12__H_L_in+(1-V12__w_v)*V12__H_R_in
    V12__s_v = np.abs(V12__v)/(np.abs(V12__v)+V12__v_eps)
    V12__H_L_out = (1-V12__w_v)*V12__H_down+V12__w_v*V12__H_L_in
    V12__H_R_out = V12__w_v*V12__H_down+(1-V12__w_v)*V12__H_R_in
    V12__v_pos = V12__w_v*V12__v
    V12__v_neg = (1-V12__w_v)*-V12__v
    V12__H_volume_L = V12__w_v*V12__H_L_in+(1-V12__w_v)*V12__H_L_out
    V12__H_volume_R = V12__w_v*V12__H_R_out+(1-V12__w_v)*V12__H_R_in
    V12__v_mm3_s = V12__v/V12__one_mm3
    VV_junc7__vj1 = V6__v
    VV_junc7__vj3 = -PV13__v
    VV_junc7__vj4 = -PV14__v
    VV_junc7__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc7__vj1/VV_junc7__v_scale)
    VV_junc7__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc7__vj3/VV_junc7__v_scale)
    VV_junc7__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc7__vj4/VV_junc7__v_scale)
    VV_junc7__w_out1 = 1-VV_junc7__w_in1
    VV_junc7__w_out3 = 1-VV_junc7__w_in3
    VV_junc7__w_out4 = 1-VV_junc7__w_in4
    VV_junc7__Qin1 = VV_junc7__w_in1*VV_junc7__vj1
    VV_junc7__Qin3 = VV_junc7__w_in3*VV_junc7__vj3
    VV_junc7__Qin4 = VV_junc7__w_in4*VV_junc7__vj4
    VV_junc7__Qout1 = VV_junc7__w_out1*-VV_junc7__vj1
    VV_junc7__Qout3 = VV_junc7__w_out3*-VV_junc7__vj3
    VV_junc7__Qout4 = VV_junc7__w_out4*-VV_junc7__vj4
    VV_junc7__Qin_tot = VV_junc7__Qin1+VV_junc7__Qin2+VV_junc7__Qin3+VV_junc7__Qin4
    VV_junc7__Qout_tot = VV_junc7__Qout1+VV_junc7__Qout2+VV_junc7__Qout3+VV_junc7__Qout4
    VV_junc7__v = (VV_junc7__u-VV_junc7__u_d)/VV_junc7__R_VV_junc
    VV_junc7__bc1_is_in = (1 if VV_junc7__Qin1 > VV_junc7__v_threshold else 0)
    VV_junc7__bc3_is_in = (1 if VV_junc7__Qin3 > VV_junc7__v_threshold else 0)
    VV_junc7__bc4_is_in = (1 if VV_junc7__Qin4 > VV_junc7__v_threshold else 0)
    VV_junc7__bc1_is_out = (1 if VV_junc7__Qout1 > VV_junc7__v_threshold else 0)
    VV_junc7__bc3_is_out = (1 if VV_junc7__Qout3 > VV_junc7__v_threshold else 0)
    VV_junc7__bc4_is_out = (1 if VV_junc7__Qout4 > VV_junc7__v_threshold else 0)
    PV13__w_v = 0.5+1/np.pi*np.arctan(PV13__v/PV13__v_scale)
    PV13__w_v_d = 0.5+1/np.pi*np.arctan(PV13__v_d/PV13__v_scale)
    PV13__H_up = PV13__w_v_d*PV13__H_L_in+(1-PV13__w_v_d)*PV13__H_R_in
    PV13__s_v_d = np.abs(PV13__v_d)/(np.abs(PV13__v_d)+PV13__v_eps)
    PV13__H_L_out = (1-PV13__w_v_d)*PV13__H_down+PV13__w_v_d*PV13__H_L_in
    PV13__H_R_out = PV13__w_v_d*PV13__H_down+(1-PV13__w_v_d)*PV13__H_R_in
    PV13__v_pos = PV13__w_v*PV13__v
    PV13__v_neg = (1-PV13__w_v)*-PV13__v
    PV13__v_d_pos = PV13__w_v_d*PV13__v_d
    PV13__v_d_neg = (1-PV13__w_v_d)*-PV13__v_d
    PV13__H_volume_L = PV13__w_v*PV13__H_L_in+(1-PV13__w_v)*PV13__H_L_out
    PV13__H_volume_R = PV13__w_v_d*PV13__H_R_out+(1-PV13__w_v_d)*PV13__H_R_in
    PV13__v_mm3_s = PV13__v/PV13__one_mm3
    PV13__v_d_mm3_s = PV13__v_d/PV13__one_mm3
    PV14__w_v = 0.5+1/np.pi*np.arctan(PV14__v/PV14__v_scale)
    PV14__w_v_d = 0.5+1/np.pi*np.arctan(PV14__v_d/PV14__v_scale)
    PV14__H_up = PV14__w_v_d*PV14__H_L_in+(1-PV14__w_v_d)*PV14__H_R_in
    PV14__s_v_d = np.abs(PV14__v_d)/(np.abs(PV14__v_d)+PV14__v_eps)
    PV14__H_L_out = (1-PV14__w_v_d)*PV14__H_down+PV14__w_v_d*PV14__H_L_in
    PV14__H_R_out = PV14__w_v_d*PV14__H_down+(1-PV14__w_v_d)*PV14__H_R_in
    PV14__v_pos = PV14__w_v*PV14__v
    PV14__v_neg = (1-PV14__w_v)*-PV14__v
    PV14__v_d_pos = PV14__w_v_d*PV14__v_d
    PV14__v_d_neg = (1-PV14__w_v_d)*-PV14__v_d
    PV14__H_volume_L = PV14__w_v*PV14__H_L_in+(1-PV14__w_v)*PV14__H_L_out
    PV14__H_volume_R = PV14__w_v_d*PV14__H_R_out+(1-PV14__w_v_d)*PV14__H_R_in
    PV14__v_mm3_s = PV14__v/PV14__one_mm3
    PV14__v_d_mm3_s = PV14__v_d/PV14__one_mm3
    V13__w_v = 0.5+1/np.pi*np.arctan(V13__v/V13__v_scale)
    V13__H_up = V13__w_v*V13__H_L_in+(1-V13__w_v)*V13__H_R_in
    V13__s_v = np.abs(V13__v)/(np.abs(V13__v)+V13__v_eps)
    V13__H_L_out = (1-V13__w_v)*V13__H_down+V13__w_v*V13__H_L_in
    V13__H_R_out = V13__w_v*V13__H_down+(1-V13__w_v)*V13__H_R_in
    V13__v_pos = V13__w_v*V13__v
    V13__v_neg = (1-V13__w_v)*-V13__v
    V13__H_volume_L = V13__w_v*V13__H_L_in+(1-V13__w_v)*V13__H_L_out
    V13__H_volume_R = V13__w_v*V13__H_R_out+(1-V13__w_v)*V13__H_R_in
    V13__v_mm3_s = V13__v/V13__one_mm3
    V14__w_v = 0.5+1/np.pi*np.arctan(V14__v/V14__v_scale)
    V14__H_up = V14__w_v*V14__H_L_in+(1-V14__w_v)*V14__H_R_in
    V14__s_v = np.abs(V14__v)/(np.abs(V14__v)+V14__v_eps)
    V14__H_L_out = (1-V14__w_v)*V14__H_down+V14__w_v*V14__H_L_in
    V14__H_R_out = V14__w_v*V14__H_down+(1-V14__w_v)*V14__H_R_in
    V14__v_pos = V14__w_v*V14__v
    V14__v_neg = (1-V14__w_v)*-V14__v
    V14__H_volume_L = V14__w_v*V14__H_L_in+(1-V14__w_v)*V14__H_L_out
    V14__H_volume_R = V14__w_v*V14__H_R_out+(1-V14__w_v)*V14__H_R_in
    V14__v_mm3_s = V14__v/V14__one_mm3
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
    VV_junc4__n_in = VV_junc4__bc1_is_in+VV_junc4__bc2_is_in+VV_junc4__bc3_is_in+VV_junc4__bc4_is_in
    VV_junc4__n_out = VV_junc4__bc1_is_out+VV_junc4__bc2_is_out+VV_junc4__bc3_is_out+VV_junc4__bc4_is_out
    VV_junc4__RBC_in = VV_junc4__Qin1*V3__H_R_out+VV_junc4__Qin2*VV_junc4__H_to2+VV_junc4__Qin3*PV7__H_L_out+VV_junc4__Qin4*PV8__H_L_out
    VV_junc4__v_mm3_s = VV_junc4__v/VV_junc4__one_mm3
    VV_junc4__junction_type = (1 if VV_junc4__n_in == 1 else (-1 if VV_junc4__n_in >= 2 else 0))
    VV_junc4__is_split = (1 if VV_junc4__junction_type == 1 else 0)
    VV_junc4__is_merge = (1 if VV_junc4__junction_type == -1 else 0)
    VV_junc4__feed1 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin1 >= VV_junc4__Qin2) and (VV_junc4__Qin1 >= VV_junc4__Qin3) and (VV_junc4__Qin1 >= VV_junc4__Qin4) else 0)
    VV_junc4__feed2 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin2 > VV_junc4__Qin1) and (VV_junc4__Qin2 >= VV_junc4__Qin3) and (VV_junc4__Qin2 >= VV_junc4__Qin4) else 0)
    VV_junc4__feed3 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin3 > VV_junc4__Qin1) and (VV_junc4__Qin3 > VV_junc4__Qin2) and (VV_junc4__Qin3 >= VV_junc4__Qin4) else 0)
    VV_junc4__feed4 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin4 > VV_junc4__Qin1) and (VV_junc4__Qin4 > VV_junc4__Qin2) and (VV_junc4__Qin4 > VV_junc4__Qin3) else 0)
    VV_junc4__alpha1 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc1_is_out == 1) and (VV_junc4__Qout1 >= VV_junc4__Qout2) and (VV_junc4__Qout1 >= VV_junc4__Qout3) and (VV_junc4__Qout1 >= VV_junc4__Qout4) else 0)
    VV_junc4__alpha2 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc2_is_out == 1) and (VV_junc4__Qout2 > VV_junc4__Qout1) and (VV_junc4__Qout2 >= VV_junc4__Qout3) and (VV_junc4__Qout2 >= VV_junc4__Qout4) else 0)
    VV_junc4__alpha3 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc3_is_out == 1) and (VV_junc4__Qout3 > VV_junc4__Qout1) and (VV_junc4__Qout3 > VV_junc4__Qout2) and (VV_junc4__Qout3 >= VV_junc4__Qout4) else 0)
    VV_junc4__alpha4 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc4_is_out == 1) and (VV_junc4__Qout4 > VV_junc4__Qout1) and (VV_junc4__Qout4 > VV_junc4__Qout2) and (VV_junc4__Qout4 > VV_junc4__Qout3) else 0)
    VV_junc4__Qout1_rem = (0 if VV_junc4__alpha1 == 1 else VV_junc4__Qout1)
    VV_junc4__Qout2_rem = (0 if VV_junc4__alpha2 == 1 else VV_junc4__Qout2)
    VV_junc4__Qout3_rem = (0 if VV_junc4__alpha3 == 1 else VV_junc4__Qout3)
    VV_junc4__Qout4_rem = (0 if VV_junc4__alpha4 == 1 else VV_junc4__Qout4)
    VV_junc4__beta1 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc1_is_out == 1) and (VV_junc4__alpha1 == 0) and (VV_junc4__Qout1_rem >= VV_junc4__Qout2_rem) and (VV_junc4__Qout1_rem >= VV_junc4__Qout3_rem) and (VV_junc4__Qout1_rem >= VV_junc4__Qout4_rem) else 0)
    VV_junc4__beta2 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc2_is_out == 1) and (VV_junc4__alpha2 == 0) and (VV_junc4__Qout2_rem > VV_junc4__Qout1_rem) and (VV_junc4__Qout2_rem >= VV_junc4__Qout3_rem) and (VV_junc4__Qout2_rem >= VV_junc4__Qout4_rem) else 0)
    VV_junc4__beta3 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc3_is_out == 1) and (VV_junc4__alpha3 == 0) and (VV_junc4__Qout3_rem > VV_junc4__Qout1_rem) and (VV_junc4__Qout3_rem > VV_junc4__Qout2_rem) and (VV_junc4__Qout3_rem >= VV_junc4__Qout4_rem) else 0)
    VV_junc4__beta4 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc4_is_out == 1) and (VV_junc4__alpha4 == 0) and (VV_junc4__Qout4_rem > VV_junc4__Qout1_rem) and (VV_junc4__Qout4_rem > VV_junc4__Qout2_rem) and (VV_junc4__Qout4_rem > VV_junc4__Qout3_rem) else 0)
    VV_junc4__D_F = (VV_junc4__D1 if VV_junc4__feed1 == 1 else (VV_junc4__D2 if VV_junc4__feed2 == 1 else (VV_junc4__D3 if VV_junc4__feed3 == 1 else (VV_junc4__D4 if VV_junc4__feed4 == 1 else VV_junc4__D1))))
    VV_junc4__D_alpha = (VV_junc4__D1 if VV_junc4__alpha1 == 1 else (VV_junc4__D2 if VV_junc4__alpha2 == 1 else (VV_junc4__D3 if VV_junc4__alpha3 == 1 else (VV_junc4__D4 if VV_junc4__alpha4 == 1 else VV_junc4__D3))))
    VV_junc4__D_beta = (VV_junc4__D1 if VV_junc4__beta1 == 1 else (VV_junc4__D2 if VV_junc4__beta2 == 1 else (VV_junc4__D3 if VV_junc4__beta3 == 1 else (VV_junc4__D4 if VV_junc4__beta4 == 1 else VV_junc4__D4))))
    VV_junc4__v_alpha = (VV_junc4__Qout1 if VV_junc4__alpha1 == 1 else (VV_junc4__Qout2 if VV_junc4__alpha2 == 1 else (VV_junc4__Qout3 if VV_junc4__alpha3 == 1 else (VV_junc4__Qout4 if VV_junc4__alpha4 == 1 else 0))))
    VV_junc4__v_beta = (VV_junc4__Qout1 if VV_junc4__beta1 == 1 else (VV_junc4__Qout2 if VV_junc4__beta2 == 1 else (VV_junc4__Qout3 if VV_junc4__beta3 == 1 else (VV_junc4__Qout4 if VV_junc4__beta4 == 1 else 0))))
    PV7__H_down_target = PV7__s_v_d*(PV7__H_mean+PV7__gamma_mirror*(PV7__H_mean-PV7__H_up))+(1-PV7__s_v_d)*PV7__H_mean
    PV8__H_down_target = PV8__s_v_d*(PV8__H_mean+PV8__gamma_mirror*(PV8__H_mean-PV8__H_up))+(1-PV8__s_v_d)*PV8__H_mean
    V7__H_down_target = V7__s_v*(V7__H_mean+V7__gamma_mirror*(V7__H_mean-V7__H_up))+(1-V7__s_v)*V7__H_mean
    V8__H_down_target = V8__s_v*(V8__H_mean+V8__gamma_mirror*(V8__H_mean-V8__H_up))+(1-V8__s_v)*V8__H_mean
    VV_junc5__n_in = VV_junc5__bc1_is_in+VV_junc5__bc2_is_in+VV_junc5__bc3_is_in+VV_junc5__bc4_is_in
    VV_junc5__n_out = VV_junc5__bc1_is_out+VV_junc5__bc2_is_out+VV_junc5__bc3_is_out+VV_junc5__bc4_is_out
    VV_junc5__RBC_in = VV_junc5__Qin1*V4__H_R_out+VV_junc5__Qin2*VV_junc5__H_to2+VV_junc5__Qin3*PV9__H_L_out+VV_junc5__Qin4*PV10__H_L_out
    VV_junc5__v_mm3_s = VV_junc5__v/VV_junc5__one_mm3
    VV_junc5__junction_type = (1 if VV_junc5__n_in == 1 else (-1 if VV_junc5__n_in >= 2 else 0))
    VV_junc5__is_split = (1 if VV_junc5__junction_type == 1 else 0)
    VV_junc5__is_merge = (1 if VV_junc5__junction_type == -1 else 0)
    VV_junc5__feed1 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin1 >= VV_junc5__Qin2) and (VV_junc5__Qin1 >= VV_junc5__Qin3) and (VV_junc5__Qin1 >= VV_junc5__Qin4) else 0)
    VV_junc5__feed2 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin2 > VV_junc5__Qin1) and (VV_junc5__Qin2 >= VV_junc5__Qin3) and (VV_junc5__Qin2 >= VV_junc5__Qin4) else 0)
    VV_junc5__feed3 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin3 > VV_junc5__Qin1) and (VV_junc5__Qin3 > VV_junc5__Qin2) and (VV_junc5__Qin3 >= VV_junc5__Qin4) else 0)
    VV_junc5__feed4 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin4 > VV_junc5__Qin1) and (VV_junc5__Qin4 > VV_junc5__Qin2) and (VV_junc5__Qin4 > VV_junc5__Qin3) else 0)
    VV_junc5__alpha1 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc1_is_out == 1) and (VV_junc5__Qout1 >= VV_junc5__Qout2) and (VV_junc5__Qout1 >= VV_junc5__Qout3) and (VV_junc5__Qout1 >= VV_junc5__Qout4) else 0)
    VV_junc5__alpha2 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc2_is_out == 1) and (VV_junc5__Qout2 > VV_junc5__Qout1) and (VV_junc5__Qout2 >= VV_junc5__Qout3) and (VV_junc5__Qout2 >= VV_junc5__Qout4) else 0)
    VV_junc5__alpha3 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc3_is_out == 1) and (VV_junc5__Qout3 > VV_junc5__Qout1) and (VV_junc5__Qout3 > VV_junc5__Qout2) and (VV_junc5__Qout3 >= VV_junc5__Qout4) else 0)
    VV_junc5__alpha4 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc4_is_out == 1) and (VV_junc5__Qout4 > VV_junc5__Qout1) and (VV_junc5__Qout4 > VV_junc5__Qout2) and (VV_junc5__Qout4 > VV_junc5__Qout3) else 0)
    VV_junc5__Qout1_rem = (0 if VV_junc5__alpha1 == 1 else VV_junc5__Qout1)
    VV_junc5__Qout2_rem = (0 if VV_junc5__alpha2 == 1 else VV_junc5__Qout2)
    VV_junc5__Qout3_rem = (0 if VV_junc5__alpha3 == 1 else VV_junc5__Qout3)
    VV_junc5__Qout4_rem = (0 if VV_junc5__alpha4 == 1 else VV_junc5__Qout4)
    VV_junc5__beta1 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc1_is_out == 1) and (VV_junc5__alpha1 == 0) and (VV_junc5__Qout1_rem >= VV_junc5__Qout2_rem) and (VV_junc5__Qout1_rem >= VV_junc5__Qout3_rem) and (VV_junc5__Qout1_rem >= VV_junc5__Qout4_rem) else 0)
    VV_junc5__beta2 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc2_is_out == 1) and (VV_junc5__alpha2 == 0) and (VV_junc5__Qout2_rem > VV_junc5__Qout1_rem) and (VV_junc5__Qout2_rem >= VV_junc5__Qout3_rem) and (VV_junc5__Qout2_rem >= VV_junc5__Qout4_rem) else 0)
    VV_junc5__beta3 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc3_is_out == 1) and (VV_junc5__alpha3 == 0) and (VV_junc5__Qout3_rem > VV_junc5__Qout1_rem) and (VV_junc5__Qout3_rem > VV_junc5__Qout2_rem) and (VV_junc5__Qout3_rem >= VV_junc5__Qout4_rem) else 0)
    VV_junc5__beta4 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc4_is_out == 1) and (VV_junc5__alpha4 == 0) and (VV_junc5__Qout4_rem > VV_junc5__Qout1_rem) and (VV_junc5__Qout4_rem > VV_junc5__Qout2_rem) and (VV_junc5__Qout4_rem > VV_junc5__Qout3_rem) else 0)
    VV_junc5__D_F = (VV_junc5__D1 if VV_junc5__feed1 == 1 else (VV_junc5__D2 if VV_junc5__feed2 == 1 else (VV_junc5__D3 if VV_junc5__feed3 == 1 else (VV_junc5__D4 if VV_junc5__feed4 == 1 else VV_junc5__D1))))
    VV_junc5__D_alpha = (VV_junc5__D1 if VV_junc5__alpha1 == 1 else (VV_junc5__D2 if VV_junc5__alpha2 == 1 else (VV_junc5__D3 if VV_junc5__alpha3 == 1 else (VV_junc5__D4 if VV_junc5__alpha4 == 1 else VV_junc5__D3))))
    VV_junc5__D_beta = (VV_junc5__D1 if VV_junc5__beta1 == 1 else (VV_junc5__D2 if VV_junc5__beta2 == 1 else (VV_junc5__D3 if VV_junc5__beta3 == 1 else (VV_junc5__D4 if VV_junc5__beta4 == 1 else VV_junc5__D4))))
    VV_junc5__v_alpha = (VV_junc5__Qout1 if VV_junc5__alpha1 == 1 else (VV_junc5__Qout2 if VV_junc5__alpha2 == 1 else (VV_junc5__Qout3 if VV_junc5__alpha3 == 1 else (VV_junc5__Qout4 if VV_junc5__alpha4 == 1 else 0))))
    VV_junc5__v_beta = (VV_junc5__Qout1 if VV_junc5__beta1 == 1 else (VV_junc5__Qout2 if VV_junc5__beta2 == 1 else (VV_junc5__Qout3 if VV_junc5__beta3 == 1 else (VV_junc5__Qout4 if VV_junc5__beta4 == 1 else 0))))
    PV9__H_down_target = PV9__s_v_d*(PV9__H_mean+PV9__gamma_mirror*(PV9__H_mean-PV9__H_up))+(1-PV9__s_v_d)*PV9__H_mean
    PV10__H_down_target = PV10__s_v_d*(PV10__H_mean+PV10__gamma_mirror*(PV10__H_mean-PV10__H_up))+(1-PV10__s_v_d)*PV10__H_mean
    V9__H_down_target = V9__s_v*(V9__H_mean+V9__gamma_mirror*(V9__H_mean-V9__H_up))+(1-V9__s_v)*V9__H_mean
    V10__H_down_target = V10__s_v*(V10__H_mean+V10__gamma_mirror*(V10__H_mean-V10__H_up))+(1-V10__s_v)*V10__H_mean
    VV_junc6__n_in = VV_junc6__bc1_is_in+VV_junc6__bc2_is_in+VV_junc6__bc3_is_in+VV_junc6__bc4_is_in
    VV_junc6__n_out = VV_junc6__bc1_is_out+VV_junc6__bc2_is_out+VV_junc6__bc3_is_out+VV_junc6__bc4_is_out
    VV_junc6__RBC_in = VV_junc6__Qin1*V5__H_R_out+VV_junc6__Qin2*VV_junc6__H_to2+VV_junc6__Qin3*PV11__H_L_out+VV_junc6__Qin4*PV12__H_L_out
    VV_junc6__v_mm3_s = VV_junc6__v/VV_junc6__one_mm3
    VV_junc6__junction_type = (1 if VV_junc6__n_in == 1 else (-1 if VV_junc6__n_in >= 2 else 0))
    VV_junc6__is_split = (1 if VV_junc6__junction_type == 1 else 0)
    VV_junc6__is_merge = (1 if VV_junc6__junction_type == -1 else 0)
    VV_junc6__feed1 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin1 >= VV_junc6__Qin2) and (VV_junc6__Qin1 >= VV_junc6__Qin3) and (VV_junc6__Qin1 >= VV_junc6__Qin4) else 0)
    VV_junc6__feed2 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin2 > VV_junc6__Qin1) and (VV_junc6__Qin2 >= VV_junc6__Qin3) and (VV_junc6__Qin2 >= VV_junc6__Qin4) else 0)
    VV_junc6__feed3 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin3 > VV_junc6__Qin1) and (VV_junc6__Qin3 > VV_junc6__Qin2) and (VV_junc6__Qin3 >= VV_junc6__Qin4) else 0)
    VV_junc6__feed4 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin4 > VV_junc6__Qin1) and (VV_junc6__Qin4 > VV_junc6__Qin2) and (VV_junc6__Qin4 > VV_junc6__Qin3) else 0)
    VV_junc6__alpha1 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc1_is_out == 1) and (VV_junc6__Qout1 >= VV_junc6__Qout2) and (VV_junc6__Qout1 >= VV_junc6__Qout3) and (VV_junc6__Qout1 >= VV_junc6__Qout4) else 0)
    VV_junc6__alpha2 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc2_is_out == 1) and (VV_junc6__Qout2 > VV_junc6__Qout1) and (VV_junc6__Qout2 >= VV_junc6__Qout3) and (VV_junc6__Qout2 >= VV_junc6__Qout4) else 0)
    VV_junc6__alpha3 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc3_is_out == 1) and (VV_junc6__Qout3 > VV_junc6__Qout1) and (VV_junc6__Qout3 > VV_junc6__Qout2) and (VV_junc6__Qout3 >= VV_junc6__Qout4) else 0)
    VV_junc6__alpha4 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc4_is_out == 1) and (VV_junc6__Qout4 > VV_junc6__Qout1) and (VV_junc6__Qout4 > VV_junc6__Qout2) and (VV_junc6__Qout4 > VV_junc6__Qout3) else 0)
    VV_junc6__Qout1_rem = (0 if VV_junc6__alpha1 == 1 else VV_junc6__Qout1)
    VV_junc6__Qout2_rem = (0 if VV_junc6__alpha2 == 1 else VV_junc6__Qout2)
    VV_junc6__Qout3_rem = (0 if VV_junc6__alpha3 == 1 else VV_junc6__Qout3)
    VV_junc6__Qout4_rem = (0 if VV_junc6__alpha4 == 1 else VV_junc6__Qout4)
    VV_junc6__beta1 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc1_is_out == 1) and (VV_junc6__alpha1 == 0) and (VV_junc6__Qout1_rem >= VV_junc6__Qout2_rem) and (VV_junc6__Qout1_rem >= VV_junc6__Qout3_rem) and (VV_junc6__Qout1_rem >= VV_junc6__Qout4_rem) else 0)
    VV_junc6__beta2 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc2_is_out == 1) and (VV_junc6__alpha2 == 0) and (VV_junc6__Qout2_rem > VV_junc6__Qout1_rem) and (VV_junc6__Qout2_rem >= VV_junc6__Qout3_rem) and (VV_junc6__Qout2_rem >= VV_junc6__Qout4_rem) else 0)
    VV_junc6__beta3 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc3_is_out == 1) and (VV_junc6__alpha3 == 0) and (VV_junc6__Qout3_rem > VV_junc6__Qout1_rem) and (VV_junc6__Qout3_rem > VV_junc6__Qout2_rem) and (VV_junc6__Qout3_rem >= VV_junc6__Qout4_rem) else 0)
    VV_junc6__beta4 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc4_is_out == 1) and (VV_junc6__alpha4 == 0) and (VV_junc6__Qout4_rem > VV_junc6__Qout1_rem) and (VV_junc6__Qout4_rem > VV_junc6__Qout2_rem) and (VV_junc6__Qout4_rem > VV_junc6__Qout3_rem) else 0)
    VV_junc6__D_F = (VV_junc6__D1 if VV_junc6__feed1 == 1 else (VV_junc6__D2 if VV_junc6__feed2 == 1 else (VV_junc6__D3 if VV_junc6__feed3 == 1 else (VV_junc6__D4 if VV_junc6__feed4 == 1 else VV_junc6__D1))))
    VV_junc6__D_alpha = (VV_junc6__D1 if VV_junc6__alpha1 == 1 else (VV_junc6__D2 if VV_junc6__alpha2 == 1 else (VV_junc6__D3 if VV_junc6__alpha3 == 1 else (VV_junc6__D4 if VV_junc6__alpha4 == 1 else VV_junc6__D3))))
    VV_junc6__D_beta = (VV_junc6__D1 if VV_junc6__beta1 == 1 else (VV_junc6__D2 if VV_junc6__beta2 == 1 else (VV_junc6__D3 if VV_junc6__beta3 == 1 else (VV_junc6__D4 if VV_junc6__beta4 == 1 else VV_junc6__D4))))
    VV_junc6__v_alpha = (VV_junc6__Qout1 if VV_junc6__alpha1 == 1 else (VV_junc6__Qout2 if VV_junc6__alpha2 == 1 else (VV_junc6__Qout3 if VV_junc6__alpha3 == 1 else (VV_junc6__Qout4 if VV_junc6__alpha4 == 1 else 0))))
    VV_junc6__v_beta = (VV_junc6__Qout1 if VV_junc6__beta1 == 1 else (VV_junc6__Qout2 if VV_junc6__beta2 == 1 else (VV_junc6__Qout3 if VV_junc6__beta3 == 1 else (VV_junc6__Qout4 if VV_junc6__beta4 == 1 else 0))))
    PV11__H_down_target = PV11__s_v_d*(PV11__H_mean+PV11__gamma_mirror*(PV11__H_mean-PV11__H_up))+(1-PV11__s_v_d)*PV11__H_mean
    PV12__H_down_target = PV12__s_v_d*(PV12__H_mean+PV12__gamma_mirror*(PV12__H_mean-PV12__H_up))+(1-PV12__s_v_d)*PV12__H_mean
    V11__H_down_target = V11__s_v*(V11__H_mean+V11__gamma_mirror*(V11__H_mean-V11__H_up))+(1-V11__s_v)*V11__H_mean
    V12__H_down_target = V12__s_v*(V12__H_mean+V12__gamma_mirror*(V12__H_mean-V12__H_up))+(1-V12__s_v)*V12__H_mean
    VV_junc7__n_in = VV_junc7__bc1_is_in+VV_junc7__bc2_is_in+VV_junc7__bc3_is_in+VV_junc7__bc4_is_in
    VV_junc7__n_out = VV_junc7__bc1_is_out+VV_junc7__bc2_is_out+VV_junc7__bc3_is_out+VV_junc7__bc4_is_out
    VV_junc7__RBC_in = VV_junc7__Qin1*V6__H_R_out+VV_junc7__Qin2*VV_junc7__H_to2+VV_junc7__Qin3*PV13__H_L_out+VV_junc7__Qin4*PV14__H_L_out
    VV_junc7__v_mm3_s = VV_junc7__v/VV_junc7__one_mm3
    VV_junc7__junction_type = (1 if VV_junc7__n_in == 1 else (-1 if VV_junc7__n_in >= 2 else 0))
    VV_junc7__is_split = (1 if VV_junc7__junction_type == 1 else 0)
    VV_junc7__is_merge = (1 if VV_junc7__junction_type == -1 else 0)
    VV_junc7__feed1 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin1 >= VV_junc7__Qin2) and (VV_junc7__Qin1 >= VV_junc7__Qin3) and (VV_junc7__Qin1 >= VV_junc7__Qin4) else 0)
    VV_junc7__feed2 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin2 > VV_junc7__Qin1) and (VV_junc7__Qin2 >= VV_junc7__Qin3) and (VV_junc7__Qin2 >= VV_junc7__Qin4) else 0)
    VV_junc7__feed3 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin3 > VV_junc7__Qin1) and (VV_junc7__Qin3 > VV_junc7__Qin2) and (VV_junc7__Qin3 >= VV_junc7__Qin4) else 0)
    VV_junc7__feed4 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin4 > VV_junc7__Qin1) and (VV_junc7__Qin4 > VV_junc7__Qin2) and (VV_junc7__Qin4 > VV_junc7__Qin3) else 0)
    VV_junc7__alpha1 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc1_is_out == 1) and (VV_junc7__Qout1 >= VV_junc7__Qout2) and (VV_junc7__Qout1 >= VV_junc7__Qout3) and (VV_junc7__Qout1 >= VV_junc7__Qout4) else 0)
    VV_junc7__alpha2 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc2_is_out == 1) and (VV_junc7__Qout2 > VV_junc7__Qout1) and (VV_junc7__Qout2 >= VV_junc7__Qout3) and (VV_junc7__Qout2 >= VV_junc7__Qout4) else 0)
    VV_junc7__alpha3 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc3_is_out == 1) and (VV_junc7__Qout3 > VV_junc7__Qout1) and (VV_junc7__Qout3 > VV_junc7__Qout2) and (VV_junc7__Qout3 >= VV_junc7__Qout4) else 0)
    VV_junc7__alpha4 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc4_is_out == 1) and (VV_junc7__Qout4 > VV_junc7__Qout1) and (VV_junc7__Qout4 > VV_junc7__Qout2) and (VV_junc7__Qout4 > VV_junc7__Qout3) else 0)
    VV_junc7__Qout1_rem = (0 if VV_junc7__alpha1 == 1 else VV_junc7__Qout1)
    VV_junc7__Qout2_rem = (0 if VV_junc7__alpha2 == 1 else VV_junc7__Qout2)
    VV_junc7__Qout3_rem = (0 if VV_junc7__alpha3 == 1 else VV_junc7__Qout3)
    VV_junc7__Qout4_rem = (0 if VV_junc7__alpha4 == 1 else VV_junc7__Qout4)
    VV_junc7__beta1 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc1_is_out == 1) and (VV_junc7__alpha1 == 0) and (VV_junc7__Qout1_rem >= VV_junc7__Qout2_rem) and (VV_junc7__Qout1_rem >= VV_junc7__Qout3_rem) and (VV_junc7__Qout1_rem >= VV_junc7__Qout4_rem) else 0)
    VV_junc7__beta2 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc2_is_out == 1) and (VV_junc7__alpha2 == 0) and (VV_junc7__Qout2_rem > VV_junc7__Qout1_rem) and (VV_junc7__Qout2_rem >= VV_junc7__Qout3_rem) and (VV_junc7__Qout2_rem >= VV_junc7__Qout4_rem) else 0)
    VV_junc7__beta3 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc3_is_out == 1) and (VV_junc7__alpha3 == 0) and (VV_junc7__Qout3_rem > VV_junc7__Qout1_rem) and (VV_junc7__Qout3_rem > VV_junc7__Qout2_rem) and (VV_junc7__Qout3_rem >= VV_junc7__Qout4_rem) else 0)
    VV_junc7__beta4 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc4_is_out == 1) and (VV_junc7__alpha4 == 0) and (VV_junc7__Qout4_rem > VV_junc7__Qout1_rem) and (VV_junc7__Qout4_rem > VV_junc7__Qout2_rem) and (VV_junc7__Qout4_rem > VV_junc7__Qout3_rem) else 0)
    VV_junc7__D_F = (VV_junc7__D1 if VV_junc7__feed1 == 1 else (VV_junc7__D2 if VV_junc7__feed2 == 1 else (VV_junc7__D3 if VV_junc7__feed3 == 1 else (VV_junc7__D4 if VV_junc7__feed4 == 1 else VV_junc7__D1))))
    VV_junc7__D_alpha = (VV_junc7__D1 if VV_junc7__alpha1 == 1 else (VV_junc7__D2 if VV_junc7__alpha2 == 1 else (VV_junc7__D3 if VV_junc7__alpha3 == 1 else (VV_junc7__D4 if VV_junc7__alpha4 == 1 else VV_junc7__D3))))
    VV_junc7__D_beta = (VV_junc7__D1 if VV_junc7__beta1 == 1 else (VV_junc7__D2 if VV_junc7__beta2 == 1 else (VV_junc7__D3 if VV_junc7__beta3 == 1 else (VV_junc7__D4 if VV_junc7__beta4 == 1 else VV_junc7__D4))))
    VV_junc7__v_alpha = (VV_junc7__Qout1 if VV_junc7__alpha1 == 1 else (VV_junc7__Qout2 if VV_junc7__alpha2 == 1 else (VV_junc7__Qout3 if VV_junc7__alpha3 == 1 else (VV_junc7__Qout4 if VV_junc7__alpha4 == 1 else 0))))
    VV_junc7__v_beta = (VV_junc7__Qout1 if VV_junc7__beta1 == 1 else (VV_junc7__Qout2 if VV_junc7__beta2 == 1 else (VV_junc7__Qout3 if VV_junc7__beta3 == 1 else (VV_junc7__Qout4 if VV_junc7__beta4 == 1 else 0))))
    PV13__H_down_target = PV13__s_v_d*(PV13__H_mean+PV13__gamma_mirror*(PV13__H_mean-PV13__H_up))+(1-PV13__s_v_d)*PV13__H_mean
    PV14__H_down_target = PV14__s_v_d*(PV14__H_mean+PV14__gamma_mirror*(PV14__H_mean-PV14__H_up))+(1-PV14__s_v_d)*PV14__H_mean
    V13__H_down_target = V13__s_v*(V13__H_mean+V13__gamma_mirror*(V13__H_mean-V13__H_up))+(1-V13__s_v)*V13__H_mean
    V14__H_down_target = V14__s_v*(V14__H_mean+V14__gamma_mirror*(V14__H_mean-V14__H_up))+(1-V14__s_v)*V14__H_mean
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
    V3__H_down_target = V3__s_v*(V3__H_mean+V3__gamma_mirror*(V3__H_mean-V3__H_up))+(1-V3__s_v)*V3__H_mean
    V4__H_down_target = V4__s_v*(V4__H_mean+V4__gamma_mirror*(V4__H_mean-V4__H_up))+(1-V4__s_v)*V4__H_mean
    VV_junc3__FQB_alpha = (VV_junc3__v_alpha+VV_junc3__div_0)/(VV_junc3__v_alpha+VV_junc3__v_beta+2*VV_junc3__div_0)
    VV_junc3__B = 1+6.98*(1-VV_junc3__H_mean)/(VV_junc3__D_F*1e6)
    VV_junc3__A = -6.96*np.log(VV_junc3__D_alpha*1e6/(VV_junc3__D_beta*1e6))/(VV_junc3__D_F*1e6)
    VV_junc3__X_0 = 0.4/(VV_junc3__D_F*1e6)
    VV_junc3__y_raw = (VV_junc3__FQB_alpha-VV_junc3__X_0)/(1-2*VV_junc3__X_0+VV_junc3__div_0)
    VV_junc3__y = min(max(VV_junc3__y_raw, VV_junc3__div_0y), 1-VV_junc3__div_0y)
    V5__H_down_target = V5__s_v*(V5__H_mean+V5__gamma_mirror*(V5__H_mean-V5__H_up))+(1-V5__s_v)*V5__H_mean
    V6__H_down_target = V6__s_v*(V6__H_mean+V6__gamma_mirror*(V6__H_mean-V6__H_up))+(1-V6__s_v)*V6__H_mean
    VV_junc4__FQB_alpha = (VV_junc4__v_alpha+VV_junc4__div_0)/(VV_junc4__v_alpha+VV_junc4__v_beta+2*VV_junc4__div_0)
    VV_junc4__B = 1+6.98*(1-VV_junc4__H_mean)/(VV_junc4__D_F*1e6)
    VV_junc4__A = -6.96*np.log(VV_junc4__D_alpha*1e6/(VV_junc4__D_beta*1e6))/(VV_junc4__D_F*1e6)
    VV_junc4__X_0 = 0.4/(VV_junc4__D_F*1e6)
    VV_junc4__y_raw = (VV_junc4__FQB_alpha-VV_junc4__X_0)/(1-2*VV_junc4__X_0+VV_junc4__div_0)
    VV_junc4__y = min(max(VV_junc4__y_raw, VV_junc4__div_0y), 1-VV_junc4__div_0y)
    VV_junc5__FQB_alpha = (VV_junc5__v_alpha+VV_junc5__div_0)/(VV_junc5__v_alpha+VV_junc5__v_beta+2*VV_junc5__div_0)
    VV_junc5__B = 1+6.98*(1-VV_junc5__H_mean)/(VV_junc5__D_F*1e6)
    VV_junc5__A = -6.96*np.log(VV_junc5__D_alpha*1e6/(VV_junc5__D_beta*1e6))/(VV_junc5__D_F*1e6)
    VV_junc5__X_0 = 0.4/(VV_junc5__D_F*1e6)
    VV_junc5__y_raw = (VV_junc5__FQB_alpha-VV_junc5__X_0)/(1-2*VV_junc5__X_0+VV_junc5__div_0)
    VV_junc5__y = min(max(VV_junc5__y_raw, VV_junc5__div_0y), 1-VV_junc5__div_0y)
    VV_junc6__FQB_alpha = (VV_junc6__v_alpha+VV_junc6__div_0)/(VV_junc6__v_alpha+VV_junc6__v_beta+2*VV_junc6__div_0)
    VV_junc6__B = 1+6.98*(1-VV_junc6__H_mean)/(VV_junc6__D_F*1e6)
    VV_junc6__A = -6.96*np.log(VV_junc6__D_alpha*1e6/(VV_junc6__D_beta*1e6))/(VV_junc6__D_F*1e6)
    VV_junc6__X_0 = 0.4/(VV_junc6__D_F*1e6)
    VV_junc6__y_raw = (VV_junc6__FQB_alpha-VV_junc6__X_0)/(1-2*VV_junc6__X_0+VV_junc6__div_0)
    VV_junc6__y = min(max(VV_junc6__y_raw, VV_junc6__div_0y), 1-VV_junc6__div_0y)
    VV_junc7__FQB_alpha = (VV_junc7__v_alpha+VV_junc7__div_0)/(VV_junc7__v_alpha+VV_junc7__v_beta+2*VV_junc7__div_0)
    VV_junc7__B = 1+6.98*(1-VV_junc7__H_mean)/(VV_junc7__D_F*1e6)
    VV_junc7__A = -6.96*np.log(VV_junc7__D_alpha*1e6/(VV_junc7__D_beta*1e6))/(VV_junc7__D_F*1e6)
    VV_junc7__X_0 = 0.4/(VV_junc7__D_F*1e6)
    VV_junc7__y_raw = (VV_junc7__FQB_alpha-VV_junc7__X_0)/(1-2*VV_junc7__X_0+VV_junc7__div_0)
    VV_junc7__y = min(max(VV_junc7__y_raw, VV_junc7__div_0y), 1-VV_junc7__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc2__ph = np.log(VV_junc2__y/(1-VV_junc2__y))
    VV_junc3__ph = np.log(VV_junc3__y/(1-VV_junc3__y))
    VV_junc4__ph = np.log(VV_junc4__y/(1-VV_junc4__y))
    VV_junc5__ph = np.log(VV_junc5__y/(1-VV_junc5__y))
    VV_junc6__ph = np.log(VV_junc6__y/(1-VV_junc6__y))
    VV_junc7__ph = np.log(VV_junc7__y/(1-VV_junc7__y))
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
    VV_junc4__FQE_alpha = 1/(1+np.exp(-(VV_junc4__A+VV_junc4__B*VV_junc4__ph)))
    VV_junc4__H_VV_out_alpha = VV_junc4__H_mean*VV_junc4__FQE_alpha/(VV_junc4__FQB_alpha+VV_junc4__div_0)
    VV_junc4__H_VV_out_beta = VV_junc4__H_mean*(1-VV_junc4__FQE_alpha)/(1-VV_junc4__FQB_alpha+VV_junc4__div_0)
    VV_junc4__H_split1 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha1 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta1 == 1 else V3__H_R_out))
    VV_junc4__H_split2 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha2 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta2 == 1 else VV_junc4__H_to2))
    VV_junc4__H_split3 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha3 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta3 == 1 else PV7__H_L_out))
    VV_junc4__H_split4 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha4 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta4 == 1 else PV8__H_L_out))
    VV_junc4__H_daughter1 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split1 if VV_junc4__is_split == 1 else V3__H_R_out))
    VV_junc4__H_daughter2 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split2 if VV_junc4__is_split == 1 else VV_junc4__H_to2))
    VV_junc4__H_daughter3 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split3 if VV_junc4__is_split == 1 else PV7__H_L_out))
    VV_junc4__H_daughter4 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split4 if VV_junc4__is_split == 1 else PV8__H_L_out))
    VV_junc4__H_from1_target = (VV_junc4__H_daughter1 if VV_junc4__bc1_is_out == 1 else V3__H_R_out)
    VV_junc4__H_from2_target = (VV_junc4__H_daughter2 if VV_junc4__bc2_is_out == 1 else VV_junc4__H_to2)
    VV_junc4__H_from3_target = (VV_junc4__H_daughter3 if VV_junc4__bc3_is_out == 1 else PV7__H_L_out)
    VV_junc4__H_from4_target = (VV_junc4__H_daughter4 if VV_junc4__bc4_is_out == 1 else PV8__H_L_out)
    VV_junc5__FQE_alpha = 1/(1+np.exp(-(VV_junc5__A+VV_junc5__B*VV_junc5__ph)))
    VV_junc5__H_VV_out_alpha = VV_junc5__H_mean*VV_junc5__FQE_alpha/(VV_junc5__FQB_alpha+VV_junc5__div_0)
    VV_junc5__H_VV_out_beta = VV_junc5__H_mean*(1-VV_junc5__FQE_alpha)/(1-VV_junc5__FQB_alpha+VV_junc5__div_0)
    VV_junc5__H_split1 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha1 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta1 == 1 else V4__H_R_out))
    VV_junc5__H_split2 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha2 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta2 == 1 else VV_junc5__H_to2))
    VV_junc5__H_split3 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha3 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta3 == 1 else PV9__H_L_out))
    VV_junc5__H_split4 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha4 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta4 == 1 else PV10__H_L_out))
    VV_junc5__H_daughter1 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split1 if VV_junc5__is_split == 1 else V4__H_R_out))
    VV_junc5__H_daughter2 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split2 if VV_junc5__is_split == 1 else VV_junc5__H_to2))
    VV_junc5__H_daughter3 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split3 if VV_junc5__is_split == 1 else PV9__H_L_out))
    VV_junc5__H_daughter4 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split4 if VV_junc5__is_split == 1 else PV10__H_L_out))
    VV_junc5__H_from1_target = (VV_junc5__H_daughter1 if VV_junc5__bc1_is_out == 1 else V4__H_R_out)
    VV_junc5__H_from2_target = (VV_junc5__H_daughter2 if VV_junc5__bc2_is_out == 1 else VV_junc5__H_to2)
    VV_junc5__H_from3_target = (VV_junc5__H_daughter3 if VV_junc5__bc3_is_out == 1 else PV9__H_L_out)
    VV_junc5__H_from4_target = (VV_junc5__H_daughter4 if VV_junc5__bc4_is_out == 1 else PV10__H_L_out)
    VV_junc6__FQE_alpha = 1/(1+np.exp(-(VV_junc6__A+VV_junc6__B*VV_junc6__ph)))
    VV_junc6__H_VV_out_alpha = VV_junc6__H_mean*VV_junc6__FQE_alpha/(VV_junc6__FQB_alpha+VV_junc6__div_0)
    VV_junc6__H_VV_out_beta = VV_junc6__H_mean*(1-VV_junc6__FQE_alpha)/(1-VV_junc6__FQB_alpha+VV_junc6__div_0)
    VV_junc6__H_split1 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha1 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta1 == 1 else V5__H_R_out))
    VV_junc6__H_split2 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha2 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta2 == 1 else VV_junc6__H_to2))
    VV_junc6__H_split3 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha3 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta3 == 1 else PV11__H_L_out))
    VV_junc6__H_split4 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha4 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta4 == 1 else PV12__H_L_out))
    VV_junc6__H_daughter1 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split1 if VV_junc6__is_split == 1 else V5__H_R_out))
    VV_junc6__H_daughter2 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split2 if VV_junc6__is_split == 1 else VV_junc6__H_to2))
    VV_junc6__H_daughter3 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split3 if VV_junc6__is_split == 1 else PV11__H_L_out))
    VV_junc6__H_daughter4 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split4 if VV_junc6__is_split == 1 else PV12__H_L_out))
    VV_junc6__H_from1_target = (VV_junc6__H_daughter1 if VV_junc6__bc1_is_out == 1 else V5__H_R_out)
    VV_junc6__H_from2_target = (VV_junc6__H_daughter2 if VV_junc6__bc2_is_out == 1 else VV_junc6__H_to2)
    VV_junc6__H_from3_target = (VV_junc6__H_daughter3 if VV_junc6__bc3_is_out == 1 else PV11__H_L_out)
    VV_junc6__H_from4_target = (VV_junc6__H_daughter4 if VV_junc6__bc4_is_out == 1 else PV12__H_L_out)
    VV_junc7__FQE_alpha = 1/(1+np.exp(-(VV_junc7__A+VV_junc7__B*VV_junc7__ph)))
    VV_junc7__H_VV_out_alpha = VV_junc7__H_mean*VV_junc7__FQE_alpha/(VV_junc7__FQB_alpha+VV_junc7__div_0)
    VV_junc7__H_VV_out_beta = VV_junc7__H_mean*(1-VV_junc7__FQE_alpha)/(1-VV_junc7__FQB_alpha+VV_junc7__div_0)
    VV_junc7__H_split1 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha1 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta1 == 1 else V6__H_R_out))
    VV_junc7__H_split2 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha2 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta2 == 1 else VV_junc7__H_to2))
    VV_junc7__H_split3 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha3 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta3 == 1 else PV13__H_L_out))
    VV_junc7__H_split4 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha4 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta4 == 1 else PV14__H_L_out))
    VV_junc7__H_daughter1 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split1 if VV_junc7__is_split == 1 else V6__H_R_out))
    VV_junc7__H_daughter2 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split2 if VV_junc7__is_split == 1 else VV_junc7__H_to2))
    VV_junc7__H_daughter3 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split3 if VV_junc7__is_split == 1 else PV13__H_L_out))
    VV_junc7__H_daughter4 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split4 if VV_junc7__is_split == 1 else PV14__H_L_out))
    VV_junc7__H_from1_target = (VV_junc7__H_daughter1 if VV_junc7__bc1_is_out == 1 else V6__H_R_out)
    VV_junc7__H_from2_target = (VV_junc7__H_daughter2 if VV_junc7__bc2_is_out == 1 else VV_junc7__H_to2)
    VV_junc7__H_from3_target = (VV_junc7__H_daughter3 if VV_junc7__bc3_is_out == 1 else PV13__H_L_out)
    VV_junc7__H_from4_target = (VV_junc7__H_daughter4 if VV_junc7__bc4_is_out == 1 else PV14__H_L_out)
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
    VV_junc4__H_from1 = VV_junc4__w_out1*VV_junc4__H_from1_target
    VV_junc4__H_from2 = VV_junc4__w_out2*VV_junc4__H_from2_target
    VV_junc4__H_from3 = VV_junc4__w_out3*VV_junc4__H_from3_target
    VV_junc4__H_from4 = VV_junc4__w_out4*VV_junc4__H_from4_target
    VV_junc4__RBC_out = VV_junc4__Qout1*VV_junc4__H_from1+VV_junc4__Qout2*VV_junc4__H_from2+VV_junc4__Qout3*VV_junc4__H_from3+VV_junc4__Qout4*VV_junc4__H_from4
    VV_junc5__H_from1 = VV_junc5__w_out1*VV_junc5__H_from1_target
    VV_junc5__H_from2 = VV_junc5__w_out2*VV_junc5__H_from2_target
    VV_junc5__H_from3 = VV_junc5__w_out3*VV_junc5__H_from3_target
    VV_junc5__H_from4 = VV_junc5__w_out4*VV_junc5__H_from4_target
    VV_junc5__RBC_out = VV_junc5__Qout1*VV_junc5__H_from1+VV_junc5__Qout2*VV_junc5__H_from2+VV_junc5__Qout3*VV_junc5__H_from3+VV_junc5__Qout4*VV_junc5__H_from4
    VV_junc6__H_from1 = VV_junc6__w_out1*VV_junc6__H_from1_target
    VV_junc6__H_from2 = VV_junc6__w_out2*VV_junc6__H_from2_target
    VV_junc6__H_from3 = VV_junc6__w_out3*VV_junc6__H_from3_target
    VV_junc6__H_from4 = VV_junc6__w_out4*VV_junc6__H_from4_target
    VV_junc6__RBC_out = VV_junc6__Qout1*VV_junc6__H_from1+VV_junc6__Qout2*VV_junc6__H_from2+VV_junc6__Qout3*VV_junc6__H_from3+VV_junc6__Qout4*VV_junc6__H_from4
    VV_junc7__H_from1 = VV_junc7__w_out1*VV_junc7__H_from1_target
    VV_junc7__H_from2 = VV_junc7__w_out2*VV_junc7__H_from2_target
    VV_junc7__H_from3 = VV_junc7__w_out3*VV_junc7__H_from3_target
    VV_junc7__H_from4 = VV_junc7__w_out4*VV_junc7__H_from4_target
    VV_junc7__RBC_out = VV_junc7__Qout1*VV_junc7__H_from1+VV_junc7__Qout2*VV_junc7__H_from2+VV_junc7__Qout3*VV_junc7__H_from3+VV_junc7__Qout4*VV_junc7__H_from4

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
    dydt[41] = (VV_junc4__H_from1-V3__H_link_R)/V3__tau_link
    dydt[42] = (PV3__H_R_out-V3__H_link_L)/V3__tau_link
    dydt[43] = (V3__H_down_target-V3__H_down)/V3__tau_H_down
    dydt[44] = PV3__v_d*V3__H_volume_L-V3__v*V3__H_volume_R
    dydt[45] = PV3__v_d-V3__v
    dydt[46] = (VV_junc5__H_from1-V4__H_link_R)/V4__tau_link
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
    dydt[64] = (VV_junc6__H_from1-V5__H_link_R)/V5__tau_link
    dydt[65] = (PV5__H_R_out-V5__H_link_L)/V5__tau_link
    dydt[66] = (V5__H_down_target-V5__H_down)/V5__tau_H_down
    dydt[67] = PV5__v_d*V5__H_volume_L-V5__v*V5__H_volume_R
    dydt[68] = PV5__v_d-V5__v
    dydt[69] = (VV_junc7__H_from1-V6__H_link_R)/V6__tau_link
    dydt[70] = (PV6__H_R_out-V6__H_link_L)/V6__tau_link
    dydt[71] = (V6__H_down_target-V6__H_down)/V6__tau_H_down
    dydt[72] = PV6__v_d*V6__H_volume_L-V6__v*V6__H_volume_R
    dydt[73] = PV6__v_d-V6__v
    dydt[74] = VV_junc4__RBC_in-VV_junc4__RBC_out
    dydt[75] = V3__v+VV_junc4__vbc2-VV_junc4__v
    dydt[76] = VV_junc4__v-PV7__v-PV8__v
    dydt[77] = (V7__H_L_out-PV7__H_link_R)/PV7__tau_link
    dydt[78] = (VV_junc4__H_from3-PV7__H_link_L)/PV7__tau_link
    dydt[79] = (PV7__H_down_target-PV7__H_down)/PV7__tau_H_down
    dydt[80] = PV7__v*PV7__H_volume_L-PV7__v_d*PV7__H_volume_R
    dydt[81] = PV7__v-PV7__v_d
    dydt[82] = (V8__H_L_out-PV8__H_link_R)/PV8__tau_link
    dydt[83] = (VV_junc4__H_from4-PV8__H_link_L)/PV8__tau_link
    dydt[84] = (PV8__H_down_target-PV8__H_down)/PV8__tau_H_down
    dydt[85] = PV8__v*PV8__H_volume_L-PV8__v_d*PV8__H_volume_R
    dydt[86] = PV8__v-PV8__v_d
    dydt[87] = (V7__H_L_out_RHS-V7__H_link_R)/V7__tau_link
    dydt[88] = (PV7__H_R_out-V7__H_link_L)/V7__tau_link
    dydt[89] = (V7__H_down_target-V7__H_down)/V7__tau_H_down
    dydt[90] = PV7__v_d*V7__H_volume_L-V7__v*V7__H_volume_R
    dydt[91] = PV7__v_d-V7__v
    dydt[92] = (V8__H_L_out_RHS-V8__H_link_R)/V8__tau_link
    dydt[93] = (PV8__H_R_out-V8__H_link_L)/V8__tau_link
    dydt[94] = (V8__H_down_target-V8__H_down)/V8__tau_H_down
    dydt[95] = PV8__v_d*V8__H_volume_L-V8__v*V8__H_volume_R
    dydt[96] = PV8__v_d-V8__v
    dydt[97] = VV_junc5__RBC_in-VV_junc5__RBC_out
    dydt[98] = V4__v+VV_junc5__vbc2-VV_junc5__v
    dydt[99] = VV_junc5__v-PV9__v-PV10__v
    dydt[100] = (V9__H_L_out-PV9__H_link_R)/PV9__tau_link
    dydt[101] = (VV_junc5__H_from3-PV9__H_link_L)/PV9__tau_link
    dydt[102] = (PV9__H_down_target-PV9__H_down)/PV9__tau_H_down
    dydt[103] = PV9__v*PV9__H_volume_L-PV9__v_d*PV9__H_volume_R
    dydt[104] = PV9__v-PV9__v_d
    dydt[105] = (V10__H_L_out-PV10__H_link_R)/PV10__tau_link
    dydt[106] = (VV_junc5__H_from4-PV10__H_link_L)/PV10__tau_link
    dydt[107] = (PV10__H_down_target-PV10__H_down)/PV10__tau_H_down
    dydt[108] = PV10__v*PV10__H_volume_L-PV10__v_d*PV10__H_volume_R
    dydt[109] = PV10__v-PV10__v_d
    dydt[110] = (V9__H_L_out_RHS-V9__H_link_R)/V9__tau_link
    dydt[111] = (PV9__H_R_out-V9__H_link_L)/V9__tau_link
    dydt[112] = (V9__H_down_target-V9__H_down)/V9__tau_H_down
    dydt[113] = PV9__v_d*V9__H_volume_L-V9__v*V9__H_volume_R
    dydt[114] = PV9__v_d-V9__v
    dydt[115] = (V10__H_L_out_RHS-V10__H_link_R)/V10__tau_link
    dydt[116] = (PV10__H_R_out-V10__H_link_L)/V10__tau_link
    dydt[117] = (V10__H_down_target-V10__H_down)/V10__tau_H_down
    dydt[118] = PV10__v_d*V10__H_volume_L-V10__v*V10__H_volume_R
    dydt[119] = PV10__v_d-V10__v
    dydt[120] = VV_junc6__RBC_in-VV_junc6__RBC_out
    dydt[121] = V5__v+VV_junc6__vbc2-VV_junc6__v
    dydt[122] = VV_junc6__v-PV11__v-PV12__v
    dydt[123] = (V11__H_L_out-PV11__H_link_R)/PV11__tau_link
    dydt[124] = (VV_junc6__H_from3-PV11__H_link_L)/PV11__tau_link
    dydt[125] = (PV11__H_down_target-PV11__H_down)/PV11__tau_H_down
    dydt[126] = PV11__v*PV11__H_volume_L-PV11__v_d*PV11__H_volume_R
    dydt[127] = PV11__v-PV11__v_d
    dydt[128] = (V12__H_L_out-PV12__H_link_R)/PV12__tau_link
    dydt[129] = (VV_junc6__H_from4-PV12__H_link_L)/PV12__tau_link
    dydt[130] = (PV12__H_down_target-PV12__H_down)/PV12__tau_H_down
    dydt[131] = PV12__v*PV12__H_volume_L-PV12__v_d*PV12__H_volume_R
    dydt[132] = PV12__v-PV12__v_d
    dydt[133] = (V11__H_L_out_RHS-V11__H_link_R)/V11__tau_link
    dydt[134] = (PV11__H_R_out-V11__H_link_L)/V11__tau_link
    dydt[135] = (V11__H_down_target-V11__H_down)/V11__tau_H_down
    dydt[136] = PV11__v_d*V11__H_volume_L-V11__v*V11__H_volume_R
    dydt[137] = PV11__v_d-V11__v
    dydt[138] = (V12__H_L_out_RHS-V12__H_link_R)/V12__tau_link
    dydt[139] = (PV12__H_R_out-V12__H_link_L)/V12__tau_link
    dydt[140] = (V12__H_down_target-V12__H_down)/V12__tau_H_down
    dydt[141] = PV12__v_d*V12__H_volume_L-V12__v*V12__H_volume_R
    dydt[142] = PV12__v_d-V12__v
    dydt[143] = VV_junc7__RBC_in-VV_junc7__RBC_out
    dydt[144] = V6__v+VV_junc7__vbc2-VV_junc7__v
    dydt[145] = VV_junc7__v-PV13__v-PV14__v
    dydt[146] = (V13__H_L_out-PV13__H_link_R)/PV13__tau_link
    dydt[147] = (VV_junc7__H_from3-PV13__H_link_L)/PV13__tau_link
    dydt[148] = (PV13__H_down_target-PV13__H_down)/PV13__tau_H_down
    dydt[149] = PV13__v*PV13__H_volume_L-PV13__v_d*PV13__H_volume_R
    dydt[150] = PV13__v-PV13__v_d
    dydt[151] = (V14__H_L_out-PV14__H_link_R)/PV14__tau_link
    dydt[152] = (VV_junc7__H_from4-PV14__H_link_L)/PV14__tau_link
    dydt[153] = (PV14__H_down_target-PV14__H_down)/PV14__tau_H_down
    dydt[154] = PV14__v*PV14__H_volume_L-PV14__v_d*PV14__H_volume_R
    dydt[155] = PV14__v-PV14__v_d
    dydt[156] = (V13__H_L_out_RHS-V13__H_link_R)/V13__tau_link
    dydt[157] = (PV13__H_R_out-V13__H_link_L)/V13__tau_link
    dydt[158] = (V13__H_down_target-V13__H_down)/V13__tau_H_down
    dydt[159] = PV13__v_d*V13__H_volume_L-V13__v*V13__H_volume_R
    dydt[160] = PV13__v_d-V13__v
    dydt[161] = (V14__H_L_out_RHS-V14__H_link_R)/V14__tau_link
    dydt[162] = (PV14__H_R_out-V14__H_link_L)/V14__tau_link
    dydt[163] = (V14__H_down_target-V14__H_down)/V14__tau_H_down
    dydt[164] = PV14__v_d*V14__H_volume_L-V14__v*V14__H_volume_R
    dydt[165] = PV14__v_d-V14__v

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
    VV_junc4__RBC_volume = y[74]
    VV_junc4__q_C = y[75]
    VV_junc4__q_C_d = y[76]
    PV7__H_link_R = y[77]
    PV7__H_link_L = y[78]
    PV7__H_down = y[79]
    PV7__RBC_volume = y[80]
    PV7__q_C = y[81]
    PV8__H_link_R = y[82]
    PV8__H_link_L = y[83]
    PV8__H_down = y[84]
    PV8__RBC_volume = y[85]
    PV8__q_C = y[86]
    V7__H_link_R = y[87]
    V7__H_link_L = y[88]
    V7__H_down = y[89]
    V7__RBC_volume = y[90]
    V7__q_C = y[91]
    V8__H_link_R = y[92]
    V8__H_link_L = y[93]
    V8__H_down = y[94]
    V8__RBC_volume = y[95]
    V8__q_C = y[96]
    VV_junc5__RBC_volume = y[97]
    VV_junc5__q_C = y[98]
    VV_junc5__q_C_d = y[99]
    PV9__H_link_R = y[100]
    PV9__H_link_L = y[101]
    PV9__H_down = y[102]
    PV9__RBC_volume = y[103]
    PV9__q_C = y[104]
    PV10__H_link_R = y[105]
    PV10__H_link_L = y[106]
    PV10__H_down = y[107]
    PV10__RBC_volume = y[108]
    PV10__q_C = y[109]
    V9__H_link_R = y[110]
    V9__H_link_L = y[111]
    V9__H_down = y[112]
    V9__RBC_volume = y[113]
    V9__q_C = y[114]
    V10__H_link_R = y[115]
    V10__H_link_L = y[116]
    V10__H_down = y[117]
    V10__RBC_volume = y[118]
    V10__q_C = y[119]
    VV_junc6__RBC_volume = y[120]
    VV_junc6__q_C = y[121]
    VV_junc6__q_C_d = y[122]
    PV11__H_link_R = y[123]
    PV11__H_link_L = y[124]
    PV11__H_down = y[125]
    PV11__RBC_volume = y[126]
    PV11__q_C = y[127]
    PV12__H_link_R = y[128]
    PV12__H_link_L = y[129]
    PV12__H_down = y[130]
    PV12__RBC_volume = y[131]
    PV12__q_C = y[132]
    V11__H_link_R = y[133]
    V11__H_link_L = y[134]
    V11__H_down = y[135]
    V11__RBC_volume = y[136]
    V11__q_C = y[137]
    V12__H_link_R = y[138]
    V12__H_link_L = y[139]
    V12__H_down = y[140]
    V12__RBC_volume = y[141]
    V12__q_C = y[142]
    VV_junc7__RBC_volume = y[143]
    VV_junc7__q_C = y[144]
    VV_junc7__q_C_d = y[145]
    PV13__H_link_R = y[146]
    PV13__H_link_L = y[147]
    PV13__H_down = y[148]
    PV13__RBC_volume = y[149]
    PV13__q_C = y[150]
    PV14__H_link_R = y[151]
    PV14__H_link_L = y[152]
    PV14__H_down = y[153]
    PV14__RBC_volume = y[154]
    PV14__q_C = y[155]
    V13__H_link_R = y[156]
    V13__H_link_L = y[157]
    V13__H_down = y[158]
    V13__RBC_volume = y[159]
    V13__q_C = y[160]
    V14__H_link_R = y[161]
    V14__H_link_L = y[162]
    V14__H_down = y[163]
    V14__RBC_volume = y[164]
    V14__q_C = y[165]

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
    VV_junc4__vj2 = VV_junc4__vbc2
    VV_junc4__D1 = 2*V3__r
    VV_junc4__D2 = 2*VV_junc4__r_bc2
    VV_junc4__D3 = 2*PV7__r
    VV_junc4__D4 = 2*PV8__r
    VV_junc4__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc4__vj2/VV_junc4__v_scale)
    VV_junc4__w_out2 = 1-VV_junc4__w_in2
    VV_junc4__Qin2 = VV_junc4__w_in2*VV_junc4__vj2
    VV_junc4__Qout2 = VV_junc4__w_out2*-VV_junc4__vj2
    VV_junc4__q_us = np.pi*np.square(VV_junc4__r)*VV_junc4__l
    VV_junc4__q = VV_junc4__q_us+VV_junc4__q_C+VV_junc4__q_C_d
    VV_junc4__bc2_is_in = (1 if VV_junc4__Qin2 > VV_junc4__v_threshold else 0)
    VV_junc4__bc2_is_out = (1 if VV_junc4__Qout2 > VV_junc4__v_threshold else 0)
    VV_junc4__C_max12 = (V3__C if V3__C > VV_junc4__C_conn2 else (VV_junc4__C_conn2 if V3__C <= VV_junc4__C_conn2 else 0.0))
    PV7__R_constriction = PV7__R_constriction_base+(PV7__R_constriction_final-PV7__R_constriction_base)/(1+np.exp(-(environment__time-PV7__t0)/PV7__tau_sig))
    PV7__H_L_in = PV7__H_link_L
    PV7__H_R_in = PV7__H_link_R
    PV7__q_us = np.pi*np.square(PV7__r)*PV7__l
    PV7__q = PV7__q_us+PV7__q_C
    PV7__C = np.pi*np.square(8.5e-9)*PV7__l/133.322
    PV7__Z = (0.8+np.exp(-0.075*2*PV7__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV7__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV7__r*1e6, 12))
    PV7__mu_45 = 6*np.exp(-0.085*2*PV7__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV7__r*1e6, 0.645))
    PV7__u = PV7__q_C/PV7__C+PV7__u_ext
    PV8__R_constriction = PV8__R_constriction_base+(PV8__R_constriction_final-PV8__R_constriction_base)/(1+np.exp(-(environment__time-PV8__t0)/PV8__tau_sig))
    PV8__H_L_in = PV8__H_link_L
    PV8__H_R_in = PV8__H_link_R
    PV8__q_us = np.pi*np.square(PV8__r)*PV8__l
    PV8__q = PV8__q_us+PV8__q_C
    PV8__C = np.pi*np.square(8.5e-9)*PV8__l/133.322
    PV8__Z = (0.8+np.exp(-0.075*2*PV8__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV8__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV8__r*1e6, 12))
    PV8__mu_45 = 6*np.exp(-0.085*2*PV8__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV8__r*1e6, 0.645))
    PV8__u = PV8__q_C/PV8__C+PV8__u_ext
    V7__H_L_in = V7__H_link_L
    V7__H_R_in = V7__H_link_R
    V7__q_us = np.pi*np.square(V7__r)*V7__l
    V7__q = V7__q_us+V7__q_C
    V7__C = np.pi*np.square(8.5e-9)*V7__l/133.322
    V7__Z = (0.8+np.exp(-0.075*2*V7__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V7__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V7__r*1e6, 12))
    V7__mu_45 = 6*np.exp(-0.085*2*V7__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V7__r*1e6, 0.645))
    V7__u = V7__q_C/V7__C+V7__u_ext
    V8__H_L_in = V8__H_link_L
    V8__H_R_in = V8__H_link_R
    V8__q_us = np.pi*np.square(V8__r)*V8__l
    V8__q = V8__q_us+V8__q_C
    V8__C = np.pi*np.square(8.5e-9)*V8__l/133.322
    V8__Z = (0.8+np.exp(-0.075*2*V8__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V8__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V8__r*1e6, 12))
    V8__mu_45 = 6*np.exp(-0.085*2*V8__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V8__r*1e6, 0.645))
    V8__u = V8__q_C/V8__C+V8__u_ext
    VV_junc5__vj2 = VV_junc5__vbc2
    VV_junc5__D1 = 2*V4__r
    VV_junc5__D2 = 2*VV_junc5__r_bc2
    VV_junc5__D3 = 2*PV9__r
    VV_junc5__D4 = 2*PV10__r
    VV_junc5__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc5__vj2/VV_junc5__v_scale)
    VV_junc5__w_out2 = 1-VV_junc5__w_in2
    VV_junc5__Qin2 = VV_junc5__w_in2*VV_junc5__vj2
    VV_junc5__Qout2 = VV_junc5__w_out2*-VV_junc5__vj2
    VV_junc5__q_us = np.pi*np.square(VV_junc5__r)*VV_junc5__l
    VV_junc5__q = VV_junc5__q_us+VV_junc5__q_C+VV_junc5__q_C_d
    VV_junc5__bc2_is_in = (1 if VV_junc5__Qin2 > VV_junc5__v_threshold else 0)
    VV_junc5__bc2_is_out = (1 if VV_junc5__Qout2 > VV_junc5__v_threshold else 0)
    VV_junc5__C_max12 = (V4__C if V4__C > VV_junc5__C_conn2 else (VV_junc5__C_conn2 if V4__C <= VV_junc5__C_conn2 else 0.0))
    PV9__R_constriction = PV9__R_constriction_base+(PV9__R_constriction_final-PV9__R_constriction_base)/(1+np.exp(-(environment__time-PV9__t0)/PV9__tau_sig))
    PV9__H_L_in = PV9__H_link_L
    PV9__H_R_in = PV9__H_link_R
    PV9__q_us = np.pi*np.square(PV9__r)*PV9__l
    PV9__q = PV9__q_us+PV9__q_C
    PV9__C = np.pi*np.square(8.5e-9)*PV9__l/133.322
    PV9__Z = (0.8+np.exp(-0.075*2*PV9__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV9__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV9__r*1e6, 12))
    PV9__mu_45 = 6*np.exp(-0.085*2*PV9__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV9__r*1e6, 0.645))
    PV9__u = PV9__q_C/PV9__C+PV9__u_ext
    PV10__R_constriction = PV10__R_constriction_base+(PV10__R_constriction_final-PV10__R_constriction_base)/(1+np.exp(-(environment__time-PV10__t0)/PV10__tau_sig))
    PV10__H_L_in = PV10__H_link_L
    PV10__H_R_in = PV10__H_link_R
    PV10__q_us = np.pi*np.square(PV10__r)*PV10__l
    PV10__q = PV10__q_us+PV10__q_C
    PV10__C = np.pi*np.square(8.5e-9)*PV10__l/133.322
    PV10__Z = (0.8+np.exp(-0.075*2*PV10__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV10__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV10__r*1e6, 12))
    PV10__mu_45 = 6*np.exp(-0.085*2*PV10__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV10__r*1e6, 0.645))
    PV10__u = PV10__q_C/PV10__C+PV10__u_ext
    V9__H_L_in = V9__H_link_L
    V9__H_R_in = V9__H_link_R
    V9__q_us = np.pi*np.square(V9__r)*V9__l
    V9__q = V9__q_us+V9__q_C
    V9__C = np.pi*np.square(8.5e-9)*V9__l/133.322
    V9__Z = (0.8+np.exp(-0.075*2*V9__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V9__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V9__r*1e6, 12))
    V9__mu_45 = 6*np.exp(-0.085*2*V9__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V9__r*1e6, 0.645))
    V9__u = V9__q_C/V9__C+V9__u_ext
    V10__H_L_in = V10__H_link_L
    V10__H_R_in = V10__H_link_R
    V10__q_us = np.pi*np.square(V10__r)*V10__l
    V10__q = V10__q_us+V10__q_C
    V10__C = np.pi*np.square(8.5e-9)*V10__l/133.322
    V10__Z = (0.8+np.exp(-0.075*2*V10__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V10__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V10__r*1e6, 12))
    V10__mu_45 = 6*np.exp(-0.085*2*V10__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V10__r*1e6, 0.645))
    V10__u = V10__q_C/V10__C+V10__u_ext
    VV_junc6__vj2 = VV_junc6__vbc2
    VV_junc6__D1 = 2*V5__r
    VV_junc6__D2 = 2*VV_junc6__r_bc2
    VV_junc6__D3 = 2*PV11__r
    VV_junc6__D4 = 2*PV12__r
    VV_junc6__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc6__vj2/VV_junc6__v_scale)
    VV_junc6__w_out2 = 1-VV_junc6__w_in2
    VV_junc6__Qin2 = VV_junc6__w_in2*VV_junc6__vj2
    VV_junc6__Qout2 = VV_junc6__w_out2*-VV_junc6__vj2
    VV_junc6__q_us = np.pi*np.square(VV_junc6__r)*VV_junc6__l
    VV_junc6__q = VV_junc6__q_us+VV_junc6__q_C+VV_junc6__q_C_d
    VV_junc6__bc2_is_in = (1 if VV_junc6__Qin2 > VV_junc6__v_threshold else 0)
    VV_junc6__bc2_is_out = (1 if VV_junc6__Qout2 > VV_junc6__v_threshold else 0)
    VV_junc6__C_max12 = (V5__C if V5__C > VV_junc6__C_conn2 else (VV_junc6__C_conn2 if V5__C <= VV_junc6__C_conn2 else 0.0))
    PV11__R_constriction = PV11__R_constriction_base+(PV11__R_constriction_final-PV11__R_constriction_base)/(1+np.exp(-(environment__time-PV11__t0)/PV11__tau_sig))
    PV11__H_L_in = PV11__H_link_L
    PV11__H_R_in = PV11__H_link_R
    PV11__q_us = np.pi*np.square(PV11__r)*PV11__l
    PV11__q = PV11__q_us+PV11__q_C
    PV11__C = np.pi*np.square(8.5e-9)*PV11__l/133.322
    PV11__Z = (0.8+np.exp(-0.075*2*PV11__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV11__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV11__r*1e6, 12))
    PV11__mu_45 = 6*np.exp(-0.085*2*PV11__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV11__r*1e6, 0.645))
    PV11__u = PV11__q_C/PV11__C+PV11__u_ext
    PV12__R_constriction = PV12__R_constriction_base+(PV12__R_constriction_final-PV12__R_constriction_base)/(1+np.exp(-(environment__time-PV12__t0)/PV12__tau_sig))
    PV12__H_L_in = PV12__H_link_L
    PV12__H_R_in = PV12__H_link_R
    PV12__q_us = np.pi*np.square(PV12__r)*PV12__l
    PV12__q = PV12__q_us+PV12__q_C
    PV12__C = np.pi*np.square(8.5e-9)*PV12__l/133.322
    PV12__Z = (0.8+np.exp(-0.075*2*PV12__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV12__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV12__r*1e6, 12))
    PV12__mu_45 = 6*np.exp(-0.085*2*PV12__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV12__r*1e6, 0.645))
    PV12__u = PV12__q_C/PV12__C+PV12__u_ext
    V11__H_L_in = V11__H_link_L
    V11__H_R_in = V11__H_link_R
    V11__q_us = np.pi*np.square(V11__r)*V11__l
    V11__q = V11__q_us+V11__q_C
    V11__C = np.pi*np.square(8.5e-9)*V11__l/133.322
    V11__Z = (0.8+np.exp(-0.075*2*V11__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V11__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V11__r*1e6, 12))
    V11__mu_45 = 6*np.exp(-0.085*2*V11__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V11__r*1e6, 0.645))
    V11__u = V11__q_C/V11__C+V11__u_ext
    V12__H_L_in = V12__H_link_L
    V12__H_R_in = V12__H_link_R
    V12__q_us = np.pi*np.square(V12__r)*V12__l
    V12__q = V12__q_us+V12__q_C
    V12__C = np.pi*np.square(8.5e-9)*V12__l/133.322
    V12__Z = (0.8+np.exp(-0.075*2*V12__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V12__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V12__r*1e6, 12))
    V12__mu_45 = 6*np.exp(-0.085*2*V12__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V12__r*1e6, 0.645))
    V12__u = V12__q_C/V12__C+V12__u_ext
    VV_junc7__vj2 = VV_junc7__vbc2
    VV_junc7__D1 = 2*V6__r
    VV_junc7__D2 = 2*VV_junc7__r_bc2
    VV_junc7__D3 = 2*PV13__r
    VV_junc7__D4 = 2*PV14__r
    VV_junc7__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc7__vj2/VV_junc7__v_scale)
    VV_junc7__w_out2 = 1-VV_junc7__w_in2
    VV_junc7__Qin2 = VV_junc7__w_in2*VV_junc7__vj2
    VV_junc7__Qout2 = VV_junc7__w_out2*-VV_junc7__vj2
    VV_junc7__q_us = np.pi*np.square(VV_junc7__r)*VV_junc7__l
    VV_junc7__q = VV_junc7__q_us+VV_junc7__q_C+VV_junc7__q_C_d
    VV_junc7__bc2_is_in = (1 if VV_junc7__Qin2 > VV_junc7__v_threshold else 0)
    VV_junc7__bc2_is_out = (1 if VV_junc7__Qout2 > VV_junc7__v_threshold else 0)
    VV_junc7__C_max12 = (V6__C if V6__C > VV_junc7__C_conn2 else (VV_junc7__C_conn2 if V6__C <= VV_junc7__C_conn2 else 0.0))
    PV13__R_constriction = PV13__R_constriction_base+(PV13__R_constriction_final-PV13__R_constriction_base)/(1+np.exp(-(environment__time-PV13__t0)/PV13__tau_sig))
    PV13__H_L_in = PV13__H_link_L
    PV13__H_R_in = PV13__H_link_R
    PV13__q_us = np.pi*np.square(PV13__r)*PV13__l
    PV13__q = PV13__q_us+PV13__q_C
    PV13__C = np.pi*np.square(8.5e-9)*PV13__l/133.322
    PV13__Z = (0.8+np.exp(-0.075*2*PV13__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV13__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV13__r*1e6, 12))
    PV13__mu_45 = 6*np.exp(-0.085*2*PV13__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV13__r*1e6, 0.645))
    PV13__u = PV13__q_C/PV13__C+PV13__u_ext
    PV14__R_constriction = PV14__R_constriction_base+(PV14__R_constriction_final-PV14__R_constriction_base)/(1+np.exp(-(environment__time-PV14__t0)/PV14__tau_sig))
    PV14__H_L_in = PV14__H_link_L
    PV14__H_R_in = PV14__H_link_R
    PV14__q_us = np.pi*np.square(PV14__r)*PV14__l
    PV14__q = PV14__q_us+PV14__q_C
    PV14__C = np.pi*np.square(8.5e-9)*PV14__l/133.322
    PV14__Z = (0.8+np.exp(-0.075*2*PV14__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV14__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV14__r*1e6, 12))
    PV14__mu_45 = 6*np.exp(-0.085*2*PV14__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV14__r*1e6, 0.645))
    PV14__u = PV14__q_C/PV14__C+PV14__u_ext
    V13__H_L_in = V13__H_link_L
    V13__H_R_in = V13__H_link_R
    V13__q_us = np.pi*np.square(V13__r)*V13__l
    V13__q = V13__q_us+V13__q_C
    V13__C = np.pi*np.square(8.5e-9)*V13__l/133.322
    V13__Z = (0.8+np.exp(-0.075*2*V13__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V13__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V13__r*1e6, 12))
    V13__mu_45 = 6*np.exp(-0.085*2*V13__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V13__r*1e6, 0.645))
    V13__u = V13__q_C/V13__C+V13__u_ext
    V14__H_L_in = V14__H_link_L
    V14__H_R_in = V14__H_link_R
    V14__q_us = np.pi*np.square(V14__r)*V14__l
    V14__q = V14__q_us+V14__q_C
    V14__C = np.pi*np.square(8.5e-9)*V14__l/133.322
    V14__Z = (0.8+np.exp(-0.075*2*V14__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V14__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V14__r*1e6, 12))
    V14__mu_45 = 6*np.exp(-0.085*2*V14__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V14__r*1e6, 0.645))
    V14__u = V14__q_C/V14__C+V14__u_ext
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
    VV_junc4__RBC_volume_init = VV_junc4__H_global_L*VV_junc4__q_us
    VV_junc4__H_mean = VV_junc4__RBC_volume/(VV_junc4__q_us+VV_junc4__div_0)
    VV_junc4__C_max123 = (VV_junc4__C_max12 if VV_junc4__C_max12 > PV7__C else (PV7__C if VV_junc4__C_max12 <= PV7__C else 0.0))
    VV_junc4__C = (VV_junc4__C_max123 if VV_junc4__C_max123 > PV8__C else (PV8__C if VV_junc4__C_max123 <= PV8__C else 0.0))
    PV7__RBC_volume_init = PV7__H_global_L*PV7__q_us
    PV7__H_mean = PV7__RBC_volume/PV7__q
    PV7__hem_dep_u_rel = 1+(PV7__mu_45-1)*(safe_power(1-PV7__H_mean, PV7__Z)-1)/(safe_power(1-PV7__H_global_L, PV7__Z)-1)*np.square(2*PV7__r*1e6/(2*PV7__r*1e6-1.1))
    PV7__u_mmHg = PV7__u/133.322
    PV8__RBC_volume_init = PV8__H_global_L*PV8__q_us
    PV8__H_mean = PV8__RBC_volume/PV8__q
    PV8__hem_dep_u_rel = 1+(PV8__mu_45-1)*(safe_power(1-PV8__H_mean, PV8__Z)-1)/(safe_power(1-PV8__H_global_L, PV8__Z)-1)*np.square(2*PV8__r*1e6/(2*PV8__r*1e6-1.1))
    PV8__u_mmHg = PV8__u/133.322
    V7__RBC_volume_init = V7__H_global_L*V7__q_us
    V7__H_mean = V7__RBC_volume/V7__q
    V7__hem_dep_u_rel = 1+(V7__mu_45-1)*(safe_power(1-V7__H_mean, V7__Z)-1)/(safe_power(1-V7__H_global_L, V7__Z)-1)*np.square(2*V7__r*1e6/(2*V7__r*1e6-1.1))
    V7__u_mmHg = V7__u/133.322
    V8__RBC_volume_init = V8__H_global_L*V8__q_us
    V8__H_mean = V8__RBC_volume/V8__q
    V8__hem_dep_u_rel = 1+(V8__mu_45-1)*(safe_power(1-V8__H_mean, V8__Z)-1)/(safe_power(1-V8__H_global_L, V8__Z)-1)*np.square(2*V8__r*1e6/(2*V8__r*1e6-1.1))
    V8__u_mmHg = V8__u/133.322
    VV_junc5__RBC_volume_init = VV_junc5__H_global_L*VV_junc5__q_us
    VV_junc5__H_mean = VV_junc5__RBC_volume/(VV_junc5__q_us+VV_junc5__div_0)
    VV_junc5__C_max123 = (VV_junc5__C_max12 if VV_junc5__C_max12 > PV9__C else (PV9__C if VV_junc5__C_max12 <= PV9__C else 0.0))
    VV_junc5__C = (VV_junc5__C_max123 if VV_junc5__C_max123 > PV10__C else (PV10__C if VV_junc5__C_max123 <= PV10__C else 0.0))
    PV9__RBC_volume_init = PV9__H_global_L*PV9__q_us
    PV9__H_mean = PV9__RBC_volume/PV9__q
    PV9__hem_dep_u_rel = 1+(PV9__mu_45-1)*(safe_power(1-PV9__H_mean, PV9__Z)-1)/(safe_power(1-PV9__H_global_L, PV9__Z)-1)*np.square(2*PV9__r*1e6/(2*PV9__r*1e6-1.1))
    PV9__u_mmHg = PV9__u/133.322
    PV10__RBC_volume_init = PV10__H_global_L*PV10__q_us
    PV10__H_mean = PV10__RBC_volume/PV10__q
    PV10__hem_dep_u_rel = 1+(PV10__mu_45-1)*(safe_power(1-PV10__H_mean, PV10__Z)-1)/(safe_power(1-PV10__H_global_L, PV10__Z)-1)*np.square(2*PV10__r*1e6/(2*PV10__r*1e6-1.1))
    PV10__u_mmHg = PV10__u/133.322
    V9__RBC_volume_init = V9__H_global_L*V9__q_us
    V9__H_mean = V9__RBC_volume/V9__q
    V9__hem_dep_u_rel = 1+(V9__mu_45-1)*(safe_power(1-V9__H_mean, V9__Z)-1)/(safe_power(1-V9__H_global_L, V9__Z)-1)*np.square(2*V9__r*1e6/(2*V9__r*1e6-1.1))
    V9__u_mmHg = V9__u/133.322
    V10__RBC_volume_init = V10__H_global_L*V10__q_us
    V10__H_mean = V10__RBC_volume/V10__q
    V10__hem_dep_u_rel = 1+(V10__mu_45-1)*(safe_power(1-V10__H_mean, V10__Z)-1)/(safe_power(1-V10__H_global_L, V10__Z)-1)*np.square(2*V10__r*1e6/(2*V10__r*1e6-1.1))
    V10__u_mmHg = V10__u/133.322
    VV_junc6__RBC_volume_init = VV_junc6__H_global_L*VV_junc6__q_us
    VV_junc6__H_mean = VV_junc6__RBC_volume/(VV_junc6__q_us+VV_junc6__div_0)
    VV_junc6__C_max123 = (VV_junc6__C_max12 if VV_junc6__C_max12 > PV11__C else (PV11__C if VV_junc6__C_max12 <= PV11__C else 0.0))
    VV_junc6__C = (VV_junc6__C_max123 if VV_junc6__C_max123 > PV12__C else (PV12__C if VV_junc6__C_max123 <= PV12__C else 0.0))
    PV11__RBC_volume_init = PV11__H_global_L*PV11__q_us
    PV11__H_mean = PV11__RBC_volume/PV11__q
    PV11__hem_dep_u_rel = 1+(PV11__mu_45-1)*(safe_power(1-PV11__H_mean, PV11__Z)-1)/(safe_power(1-PV11__H_global_L, PV11__Z)-1)*np.square(2*PV11__r*1e6/(2*PV11__r*1e6-1.1))
    PV11__u_mmHg = PV11__u/133.322
    PV12__RBC_volume_init = PV12__H_global_L*PV12__q_us
    PV12__H_mean = PV12__RBC_volume/PV12__q
    PV12__hem_dep_u_rel = 1+(PV12__mu_45-1)*(safe_power(1-PV12__H_mean, PV12__Z)-1)/(safe_power(1-PV12__H_global_L, PV12__Z)-1)*np.square(2*PV12__r*1e6/(2*PV12__r*1e6-1.1))
    PV12__u_mmHg = PV12__u/133.322
    V11__RBC_volume_init = V11__H_global_L*V11__q_us
    V11__H_mean = V11__RBC_volume/V11__q
    V11__hem_dep_u_rel = 1+(V11__mu_45-1)*(safe_power(1-V11__H_mean, V11__Z)-1)/(safe_power(1-V11__H_global_L, V11__Z)-1)*np.square(2*V11__r*1e6/(2*V11__r*1e6-1.1))
    V11__u_mmHg = V11__u/133.322
    V12__RBC_volume_init = V12__H_global_L*V12__q_us
    V12__H_mean = V12__RBC_volume/V12__q
    V12__hem_dep_u_rel = 1+(V12__mu_45-1)*(safe_power(1-V12__H_mean, V12__Z)-1)/(safe_power(1-V12__H_global_L, V12__Z)-1)*np.square(2*V12__r*1e6/(2*V12__r*1e6-1.1))
    V12__u_mmHg = V12__u/133.322
    VV_junc7__RBC_volume_init = VV_junc7__H_global_L*VV_junc7__q_us
    VV_junc7__H_mean = VV_junc7__RBC_volume/(VV_junc7__q_us+VV_junc7__div_0)
    VV_junc7__C_max123 = (VV_junc7__C_max12 if VV_junc7__C_max12 > PV13__C else (PV13__C if VV_junc7__C_max12 <= PV13__C else 0.0))
    VV_junc7__C = (VV_junc7__C_max123 if VV_junc7__C_max123 > PV14__C else (PV14__C if VV_junc7__C_max123 <= PV14__C else 0.0))
    PV13__RBC_volume_init = PV13__H_global_L*PV13__q_us
    PV13__H_mean = PV13__RBC_volume/PV13__q
    PV13__hem_dep_u_rel = 1+(PV13__mu_45-1)*(safe_power(1-PV13__H_mean, PV13__Z)-1)/(safe_power(1-PV13__H_global_L, PV13__Z)-1)*np.square(2*PV13__r*1e6/(2*PV13__r*1e6-1.1))
    PV13__u_mmHg = PV13__u/133.322
    PV14__RBC_volume_init = PV14__H_global_L*PV14__q_us
    PV14__H_mean = PV14__RBC_volume/PV14__q
    PV14__hem_dep_u_rel = 1+(PV14__mu_45-1)*(safe_power(1-PV14__H_mean, PV14__Z)-1)/(safe_power(1-PV14__H_global_L, PV14__Z)-1)*np.square(2*PV14__r*1e6/(2*PV14__r*1e6-1.1))
    PV14__u_mmHg = PV14__u/133.322
    V13__RBC_volume_init = V13__H_global_L*V13__q_us
    V13__H_mean = V13__RBC_volume/V13__q
    V13__hem_dep_u_rel = 1+(V13__mu_45-1)*(safe_power(1-V13__H_mean, V13__Z)-1)/(safe_power(1-V13__H_global_L, V13__Z)-1)*np.square(2*V13__r*1e6/(2*V13__r*1e6-1.1))
    V13__u_mmHg = V13__u/133.322
    V14__RBC_volume_init = V14__H_global_L*V14__q_us
    V14__H_mean = V14__RBC_volume/V14__q
    V14__hem_dep_u_rel = 1+(V14__mu_45-1)*(safe_power(1-V14__H_mean, V14__Z)-1)/(safe_power(1-V14__H_global_L, V14__Z)-1)*np.square(2*V14__r*1e6/(2*V14__r*1e6-1.1))
    V14__u_mmHg = V14__u/133.322
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
    V4__mu = V4__hem_dep_u_rel*V4__mu_plasma
    V4__R = 8*V4__mu*V4__l/(np.pi*safe_power(V4__r, 4))
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
    V6__mu = V6__hem_dep_u_rel*V6__mu_plasma
    V6__R = 8*V6__mu*V6__l/(np.pi*safe_power(V6__r, 4))
    VV_junc4__u = VV_junc4__q_C/(VV_junc4__C/2)+VV_junc4__u_ext
    VV_junc4__u_mmHg = VV_junc4__u/133.322
    VV_junc4__u_d = VV_junc4__q_C_d/(VV_junc4__C/2)+VV_junc4__u_ext
    VV_junc4__u_d_mmHg = VV_junc4__u_d/133.322
    PV7__mu = PV7__hem_dep_u_rel*PV7__mu_plasma
    PV7__R = 8*PV7__mu*PV7__l/(np.pi*safe_power(PV7__r, 4))+PV7__R_constriction
    PV7__v = (VV_junc4__u_d-PV7__u)/(PV7__R/2)
    PV7__v_d = (PV7__u-V7__u)/(PV7__R/2)
    PV8__mu = PV8__hem_dep_u_rel*PV8__mu_plasma
    PV8__R = 8*PV8__mu*PV8__l/(np.pi*safe_power(PV8__r, 4))+PV8__R_constriction
    PV8__v = (VV_junc4__u_d-PV8__u)/(PV8__R/2)
    PV8__v_d = (PV8__u-V8__u)/(PV8__R/2)
    V7__mu = V7__hem_dep_u_rel*V7__mu_plasma
    V7__R = 8*V7__mu*V7__l/(np.pi*safe_power(V7__r, 4))
    V7__v = (V7__u-V7__u_out)/V7__R
    V8__mu = V8__hem_dep_u_rel*V8__mu_plasma
    V8__R = 8*V8__mu*V8__l/(np.pi*safe_power(V8__r, 4))
    V8__v = (V8__u-V8__u_out)/V8__R
    VV_junc5__u = VV_junc5__q_C/(VV_junc5__C/2)+VV_junc5__u_ext
    VV_junc5__u_mmHg = VV_junc5__u/133.322
    VV_junc5__u_d = VV_junc5__q_C_d/(VV_junc5__C/2)+VV_junc5__u_ext
    VV_junc5__u_d_mmHg = VV_junc5__u_d/133.322
    PV9__mu = PV9__hem_dep_u_rel*PV9__mu_plasma
    PV9__R = 8*PV9__mu*PV9__l/(np.pi*safe_power(PV9__r, 4))+PV9__R_constriction
    PV9__v = (VV_junc5__u_d-PV9__u)/(PV9__R/2)
    PV9__v_d = (PV9__u-V9__u)/(PV9__R/2)
    PV10__mu = PV10__hem_dep_u_rel*PV10__mu_plasma
    PV10__R = 8*PV10__mu*PV10__l/(np.pi*safe_power(PV10__r, 4))+PV10__R_constriction
    PV10__v = (VV_junc5__u_d-PV10__u)/(PV10__R/2)
    PV10__v_d = (PV10__u-V10__u)/(PV10__R/2)
    V9__mu = V9__hem_dep_u_rel*V9__mu_plasma
    V9__R = 8*V9__mu*V9__l/(np.pi*safe_power(V9__r, 4))
    V9__v = (V9__u-V9__u_out)/V9__R
    V10__mu = V10__hem_dep_u_rel*V10__mu_plasma
    V10__R = 8*V10__mu*V10__l/(np.pi*safe_power(V10__r, 4))
    V10__v = (V10__u-V10__u_out)/V10__R
    VV_junc6__u = VV_junc6__q_C/(VV_junc6__C/2)+VV_junc6__u_ext
    VV_junc6__u_mmHg = VV_junc6__u/133.322
    VV_junc6__u_d = VV_junc6__q_C_d/(VV_junc6__C/2)+VV_junc6__u_ext
    VV_junc6__u_d_mmHg = VV_junc6__u_d/133.322
    PV11__mu = PV11__hem_dep_u_rel*PV11__mu_plasma
    PV11__R = 8*PV11__mu*PV11__l/(np.pi*safe_power(PV11__r, 4))+PV11__R_constriction
    PV11__v = (VV_junc6__u_d-PV11__u)/(PV11__R/2)
    PV11__v_d = (PV11__u-V11__u)/(PV11__R/2)
    PV12__mu = PV12__hem_dep_u_rel*PV12__mu_plasma
    PV12__R = 8*PV12__mu*PV12__l/(np.pi*safe_power(PV12__r, 4))+PV12__R_constriction
    PV12__v = (VV_junc6__u_d-PV12__u)/(PV12__R/2)
    PV12__v_d = (PV12__u-V12__u)/(PV12__R/2)
    V11__mu = V11__hem_dep_u_rel*V11__mu_plasma
    V11__R = 8*V11__mu*V11__l/(np.pi*safe_power(V11__r, 4))
    V11__v = (V11__u-V11__u_out)/V11__R
    V12__mu = V12__hem_dep_u_rel*V12__mu_plasma
    V12__R = 8*V12__mu*V12__l/(np.pi*safe_power(V12__r, 4))
    V12__v = (V12__u-V12__u_out)/V12__R
    VV_junc7__u = VV_junc7__q_C/(VV_junc7__C/2)+VV_junc7__u_ext
    VV_junc7__u_mmHg = VV_junc7__u/133.322
    VV_junc7__u_d = VV_junc7__q_C_d/(VV_junc7__C/2)+VV_junc7__u_ext
    VV_junc7__u_d_mmHg = VV_junc7__u_d/133.322
    PV13__mu = PV13__hem_dep_u_rel*PV13__mu_plasma
    PV13__R = 8*PV13__mu*PV13__l/(np.pi*safe_power(PV13__r, 4))+PV13__R_constriction
    PV13__v = (VV_junc7__u_d-PV13__u)/(PV13__R/2)
    PV13__v_d = (PV13__u-V13__u)/(PV13__R/2)
    PV14__mu = PV14__hem_dep_u_rel*PV14__mu_plasma
    PV14__R = 8*PV14__mu*PV14__l/(np.pi*safe_power(PV14__r, 4))+PV14__R_constriction
    PV14__v = (VV_junc7__u_d-PV14__u)/(PV14__R/2)
    PV14__v_d = (PV14__u-V14__u)/(PV14__R/2)
    V13__mu = V13__hem_dep_u_rel*V13__mu_plasma
    V13__R = 8*V13__mu*V13__l/(np.pi*safe_power(V13__r, 4))
    V13__v = (V13__u-V13__u_out)/V13__R
    V14__mu = V14__hem_dep_u_rel*V14__mu_plasma
    V14__R = 8*V14__mu*V14__l/(np.pi*safe_power(V14__r, 4))
    V14__v = (V14__u-V14__u_out)/V14__R
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
    V3__v = (V3__u-VV_junc4__u)/V3__R
    V4__v = (V4__u-VV_junc5__u)/V4__R
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
    V5__v = (V5__u-VV_junc6__u)/V5__R
    V6__v = (V6__u-VV_junc7__u)/V6__R
    VV_junc4__vj1 = V3__v
    VV_junc4__vj3 = -PV7__v
    VV_junc4__vj4 = -PV8__v
    VV_junc4__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc4__vj1/VV_junc4__v_scale)
    VV_junc4__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc4__vj3/VV_junc4__v_scale)
    VV_junc4__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc4__vj4/VV_junc4__v_scale)
    VV_junc4__w_out1 = 1-VV_junc4__w_in1
    VV_junc4__w_out3 = 1-VV_junc4__w_in3
    VV_junc4__w_out4 = 1-VV_junc4__w_in4
    VV_junc4__Qin1 = VV_junc4__w_in1*VV_junc4__vj1
    VV_junc4__Qin3 = VV_junc4__w_in3*VV_junc4__vj3
    VV_junc4__Qin4 = VV_junc4__w_in4*VV_junc4__vj4
    VV_junc4__Qout1 = VV_junc4__w_out1*-VV_junc4__vj1
    VV_junc4__Qout3 = VV_junc4__w_out3*-VV_junc4__vj3
    VV_junc4__Qout4 = VV_junc4__w_out4*-VV_junc4__vj4
    VV_junc4__Qin_tot = VV_junc4__Qin1+VV_junc4__Qin2+VV_junc4__Qin3+VV_junc4__Qin4
    VV_junc4__Qout_tot = VV_junc4__Qout1+VV_junc4__Qout2+VV_junc4__Qout3+VV_junc4__Qout4
    VV_junc4__v = (VV_junc4__u-VV_junc4__u_d)/VV_junc4__R_VV_junc
    VV_junc4__bc1_is_in = (1 if VV_junc4__Qin1 > VV_junc4__v_threshold else 0)
    VV_junc4__bc3_is_in = (1 if VV_junc4__Qin3 > VV_junc4__v_threshold else 0)
    VV_junc4__bc4_is_in = (1 if VV_junc4__Qin4 > VV_junc4__v_threshold else 0)
    VV_junc4__bc1_is_out = (1 if VV_junc4__Qout1 > VV_junc4__v_threshold else 0)
    VV_junc4__bc3_is_out = (1 if VV_junc4__Qout3 > VV_junc4__v_threshold else 0)
    VV_junc4__bc4_is_out = (1 if VV_junc4__Qout4 > VV_junc4__v_threshold else 0)
    PV7__w_v = 0.5+1/np.pi*np.arctan(PV7__v/PV7__v_scale)
    PV7__w_v_d = 0.5+1/np.pi*np.arctan(PV7__v_d/PV7__v_scale)
    PV7__H_up = PV7__w_v_d*PV7__H_L_in+(1-PV7__w_v_d)*PV7__H_R_in
    PV7__s_v_d = np.abs(PV7__v_d)/(np.abs(PV7__v_d)+PV7__v_eps)
    PV7__H_L_out = (1-PV7__w_v_d)*PV7__H_down+PV7__w_v_d*PV7__H_L_in
    PV7__H_R_out = PV7__w_v_d*PV7__H_down+(1-PV7__w_v_d)*PV7__H_R_in
    PV7__v_pos = PV7__w_v*PV7__v
    PV7__v_neg = (1-PV7__w_v)*-PV7__v
    PV7__v_d_pos = PV7__w_v_d*PV7__v_d
    PV7__v_d_neg = (1-PV7__w_v_d)*-PV7__v_d
    PV7__H_volume_L = PV7__w_v*PV7__H_L_in+(1-PV7__w_v)*PV7__H_L_out
    PV7__H_volume_R = PV7__w_v_d*PV7__H_R_out+(1-PV7__w_v_d)*PV7__H_R_in
    PV7__v_mm3_s = PV7__v/PV7__one_mm3
    PV7__v_d_mm3_s = PV7__v_d/PV7__one_mm3
    PV8__w_v = 0.5+1/np.pi*np.arctan(PV8__v/PV8__v_scale)
    PV8__w_v_d = 0.5+1/np.pi*np.arctan(PV8__v_d/PV8__v_scale)
    PV8__H_up = PV8__w_v_d*PV8__H_L_in+(1-PV8__w_v_d)*PV8__H_R_in
    PV8__s_v_d = np.abs(PV8__v_d)/(np.abs(PV8__v_d)+PV8__v_eps)
    PV8__H_L_out = (1-PV8__w_v_d)*PV8__H_down+PV8__w_v_d*PV8__H_L_in
    PV8__H_R_out = PV8__w_v_d*PV8__H_down+(1-PV8__w_v_d)*PV8__H_R_in
    PV8__v_pos = PV8__w_v*PV8__v
    PV8__v_neg = (1-PV8__w_v)*-PV8__v
    PV8__v_d_pos = PV8__w_v_d*PV8__v_d
    PV8__v_d_neg = (1-PV8__w_v_d)*-PV8__v_d
    PV8__H_volume_L = PV8__w_v*PV8__H_L_in+(1-PV8__w_v)*PV8__H_L_out
    PV8__H_volume_R = PV8__w_v_d*PV8__H_R_out+(1-PV8__w_v_d)*PV8__H_R_in
    PV8__v_mm3_s = PV8__v/PV8__one_mm3
    PV8__v_d_mm3_s = PV8__v_d/PV8__one_mm3
    V7__w_v = 0.5+1/np.pi*np.arctan(V7__v/V7__v_scale)
    V7__H_up = V7__w_v*V7__H_L_in+(1-V7__w_v)*V7__H_R_in
    V7__s_v = np.abs(V7__v)/(np.abs(V7__v)+V7__v_eps)
    V7__H_L_out = (1-V7__w_v)*V7__H_down+V7__w_v*V7__H_L_in
    V7__H_R_out = V7__w_v*V7__H_down+(1-V7__w_v)*V7__H_R_in
    V7__v_pos = V7__w_v*V7__v
    V7__v_neg = (1-V7__w_v)*-V7__v
    V7__H_volume_L = V7__w_v*V7__H_L_in+(1-V7__w_v)*V7__H_L_out
    V7__H_volume_R = V7__w_v*V7__H_R_out+(1-V7__w_v)*V7__H_R_in
    V7__v_mm3_s = V7__v/V7__one_mm3
    V8__w_v = 0.5+1/np.pi*np.arctan(V8__v/V8__v_scale)
    V8__H_up = V8__w_v*V8__H_L_in+(1-V8__w_v)*V8__H_R_in
    V8__s_v = np.abs(V8__v)/(np.abs(V8__v)+V8__v_eps)
    V8__H_L_out = (1-V8__w_v)*V8__H_down+V8__w_v*V8__H_L_in
    V8__H_R_out = V8__w_v*V8__H_down+(1-V8__w_v)*V8__H_R_in
    V8__v_pos = V8__w_v*V8__v
    V8__v_neg = (1-V8__w_v)*-V8__v
    V8__H_volume_L = V8__w_v*V8__H_L_in+(1-V8__w_v)*V8__H_L_out
    V8__H_volume_R = V8__w_v*V8__H_R_out+(1-V8__w_v)*V8__H_R_in
    V8__v_mm3_s = V8__v/V8__one_mm3
    VV_junc5__vj1 = V4__v
    VV_junc5__vj3 = -PV9__v
    VV_junc5__vj4 = -PV10__v
    VV_junc5__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc5__vj1/VV_junc5__v_scale)
    VV_junc5__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc5__vj3/VV_junc5__v_scale)
    VV_junc5__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc5__vj4/VV_junc5__v_scale)
    VV_junc5__w_out1 = 1-VV_junc5__w_in1
    VV_junc5__w_out3 = 1-VV_junc5__w_in3
    VV_junc5__w_out4 = 1-VV_junc5__w_in4
    VV_junc5__Qin1 = VV_junc5__w_in1*VV_junc5__vj1
    VV_junc5__Qin3 = VV_junc5__w_in3*VV_junc5__vj3
    VV_junc5__Qin4 = VV_junc5__w_in4*VV_junc5__vj4
    VV_junc5__Qout1 = VV_junc5__w_out1*-VV_junc5__vj1
    VV_junc5__Qout3 = VV_junc5__w_out3*-VV_junc5__vj3
    VV_junc5__Qout4 = VV_junc5__w_out4*-VV_junc5__vj4
    VV_junc5__Qin_tot = VV_junc5__Qin1+VV_junc5__Qin2+VV_junc5__Qin3+VV_junc5__Qin4
    VV_junc5__Qout_tot = VV_junc5__Qout1+VV_junc5__Qout2+VV_junc5__Qout3+VV_junc5__Qout4
    VV_junc5__v = (VV_junc5__u-VV_junc5__u_d)/VV_junc5__R_VV_junc
    VV_junc5__bc1_is_in = (1 if VV_junc5__Qin1 > VV_junc5__v_threshold else 0)
    VV_junc5__bc3_is_in = (1 if VV_junc5__Qin3 > VV_junc5__v_threshold else 0)
    VV_junc5__bc4_is_in = (1 if VV_junc5__Qin4 > VV_junc5__v_threshold else 0)
    VV_junc5__bc1_is_out = (1 if VV_junc5__Qout1 > VV_junc5__v_threshold else 0)
    VV_junc5__bc3_is_out = (1 if VV_junc5__Qout3 > VV_junc5__v_threshold else 0)
    VV_junc5__bc4_is_out = (1 if VV_junc5__Qout4 > VV_junc5__v_threshold else 0)
    PV9__w_v = 0.5+1/np.pi*np.arctan(PV9__v/PV9__v_scale)
    PV9__w_v_d = 0.5+1/np.pi*np.arctan(PV9__v_d/PV9__v_scale)
    PV9__H_up = PV9__w_v_d*PV9__H_L_in+(1-PV9__w_v_d)*PV9__H_R_in
    PV9__s_v_d = np.abs(PV9__v_d)/(np.abs(PV9__v_d)+PV9__v_eps)
    PV9__H_L_out = (1-PV9__w_v_d)*PV9__H_down+PV9__w_v_d*PV9__H_L_in
    PV9__H_R_out = PV9__w_v_d*PV9__H_down+(1-PV9__w_v_d)*PV9__H_R_in
    PV9__v_pos = PV9__w_v*PV9__v
    PV9__v_neg = (1-PV9__w_v)*-PV9__v
    PV9__v_d_pos = PV9__w_v_d*PV9__v_d
    PV9__v_d_neg = (1-PV9__w_v_d)*-PV9__v_d
    PV9__H_volume_L = PV9__w_v*PV9__H_L_in+(1-PV9__w_v)*PV9__H_L_out
    PV9__H_volume_R = PV9__w_v_d*PV9__H_R_out+(1-PV9__w_v_d)*PV9__H_R_in
    PV9__v_mm3_s = PV9__v/PV9__one_mm3
    PV9__v_d_mm3_s = PV9__v_d/PV9__one_mm3
    PV10__w_v = 0.5+1/np.pi*np.arctan(PV10__v/PV10__v_scale)
    PV10__w_v_d = 0.5+1/np.pi*np.arctan(PV10__v_d/PV10__v_scale)
    PV10__H_up = PV10__w_v_d*PV10__H_L_in+(1-PV10__w_v_d)*PV10__H_R_in
    PV10__s_v_d = np.abs(PV10__v_d)/(np.abs(PV10__v_d)+PV10__v_eps)
    PV10__H_L_out = (1-PV10__w_v_d)*PV10__H_down+PV10__w_v_d*PV10__H_L_in
    PV10__H_R_out = PV10__w_v_d*PV10__H_down+(1-PV10__w_v_d)*PV10__H_R_in
    PV10__v_pos = PV10__w_v*PV10__v
    PV10__v_neg = (1-PV10__w_v)*-PV10__v
    PV10__v_d_pos = PV10__w_v_d*PV10__v_d
    PV10__v_d_neg = (1-PV10__w_v_d)*-PV10__v_d
    PV10__H_volume_L = PV10__w_v*PV10__H_L_in+(1-PV10__w_v)*PV10__H_L_out
    PV10__H_volume_R = PV10__w_v_d*PV10__H_R_out+(1-PV10__w_v_d)*PV10__H_R_in
    PV10__v_mm3_s = PV10__v/PV10__one_mm3
    PV10__v_d_mm3_s = PV10__v_d/PV10__one_mm3
    V9__w_v = 0.5+1/np.pi*np.arctan(V9__v/V9__v_scale)
    V9__H_up = V9__w_v*V9__H_L_in+(1-V9__w_v)*V9__H_R_in
    V9__s_v = np.abs(V9__v)/(np.abs(V9__v)+V9__v_eps)
    V9__H_L_out = (1-V9__w_v)*V9__H_down+V9__w_v*V9__H_L_in
    V9__H_R_out = V9__w_v*V9__H_down+(1-V9__w_v)*V9__H_R_in
    V9__v_pos = V9__w_v*V9__v
    V9__v_neg = (1-V9__w_v)*-V9__v
    V9__H_volume_L = V9__w_v*V9__H_L_in+(1-V9__w_v)*V9__H_L_out
    V9__H_volume_R = V9__w_v*V9__H_R_out+(1-V9__w_v)*V9__H_R_in
    V9__v_mm3_s = V9__v/V9__one_mm3
    V10__w_v = 0.5+1/np.pi*np.arctan(V10__v/V10__v_scale)
    V10__H_up = V10__w_v*V10__H_L_in+(1-V10__w_v)*V10__H_R_in
    V10__s_v = np.abs(V10__v)/(np.abs(V10__v)+V10__v_eps)
    V10__H_L_out = (1-V10__w_v)*V10__H_down+V10__w_v*V10__H_L_in
    V10__H_R_out = V10__w_v*V10__H_down+(1-V10__w_v)*V10__H_R_in
    V10__v_pos = V10__w_v*V10__v
    V10__v_neg = (1-V10__w_v)*-V10__v
    V10__H_volume_L = V10__w_v*V10__H_L_in+(1-V10__w_v)*V10__H_L_out
    V10__H_volume_R = V10__w_v*V10__H_R_out+(1-V10__w_v)*V10__H_R_in
    V10__v_mm3_s = V10__v/V10__one_mm3
    VV_junc6__vj1 = V5__v
    VV_junc6__vj3 = -PV11__v
    VV_junc6__vj4 = -PV12__v
    VV_junc6__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc6__vj1/VV_junc6__v_scale)
    VV_junc6__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc6__vj3/VV_junc6__v_scale)
    VV_junc6__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc6__vj4/VV_junc6__v_scale)
    VV_junc6__w_out1 = 1-VV_junc6__w_in1
    VV_junc6__w_out3 = 1-VV_junc6__w_in3
    VV_junc6__w_out4 = 1-VV_junc6__w_in4
    VV_junc6__Qin1 = VV_junc6__w_in1*VV_junc6__vj1
    VV_junc6__Qin3 = VV_junc6__w_in3*VV_junc6__vj3
    VV_junc6__Qin4 = VV_junc6__w_in4*VV_junc6__vj4
    VV_junc6__Qout1 = VV_junc6__w_out1*-VV_junc6__vj1
    VV_junc6__Qout3 = VV_junc6__w_out3*-VV_junc6__vj3
    VV_junc6__Qout4 = VV_junc6__w_out4*-VV_junc6__vj4
    VV_junc6__Qin_tot = VV_junc6__Qin1+VV_junc6__Qin2+VV_junc6__Qin3+VV_junc6__Qin4
    VV_junc6__Qout_tot = VV_junc6__Qout1+VV_junc6__Qout2+VV_junc6__Qout3+VV_junc6__Qout4
    VV_junc6__v = (VV_junc6__u-VV_junc6__u_d)/VV_junc6__R_VV_junc
    VV_junc6__bc1_is_in = (1 if VV_junc6__Qin1 > VV_junc6__v_threshold else 0)
    VV_junc6__bc3_is_in = (1 if VV_junc6__Qin3 > VV_junc6__v_threshold else 0)
    VV_junc6__bc4_is_in = (1 if VV_junc6__Qin4 > VV_junc6__v_threshold else 0)
    VV_junc6__bc1_is_out = (1 if VV_junc6__Qout1 > VV_junc6__v_threshold else 0)
    VV_junc6__bc3_is_out = (1 if VV_junc6__Qout3 > VV_junc6__v_threshold else 0)
    VV_junc6__bc4_is_out = (1 if VV_junc6__Qout4 > VV_junc6__v_threshold else 0)
    PV11__w_v = 0.5+1/np.pi*np.arctan(PV11__v/PV11__v_scale)
    PV11__w_v_d = 0.5+1/np.pi*np.arctan(PV11__v_d/PV11__v_scale)
    PV11__H_up = PV11__w_v_d*PV11__H_L_in+(1-PV11__w_v_d)*PV11__H_R_in
    PV11__s_v_d = np.abs(PV11__v_d)/(np.abs(PV11__v_d)+PV11__v_eps)
    PV11__H_L_out = (1-PV11__w_v_d)*PV11__H_down+PV11__w_v_d*PV11__H_L_in
    PV11__H_R_out = PV11__w_v_d*PV11__H_down+(1-PV11__w_v_d)*PV11__H_R_in
    PV11__v_pos = PV11__w_v*PV11__v
    PV11__v_neg = (1-PV11__w_v)*-PV11__v
    PV11__v_d_pos = PV11__w_v_d*PV11__v_d
    PV11__v_d_neg = (1-PV11__w_v_d)*-PV11__v_d
    PV11__H_volume_L = PV11__w_v*PV11__H_L_in+(1-PV11__w_v)*PV11__H_L_out
    PV11__H_volume_R = PV11__w_v_d*PV11__H_R_out+(1-PV11__w_v_d)*PV11__H_R_in
    PV11__v_mm3_s = PV11__v/PV11__one_mm3
    PV11__v_d_mm3_s = PV11__v_d/PV11__one_mm3
    PV12__w_v = 0.5+1/np.pi*np.arctan(PV12__v/PV12__v_scale)
    PV12__w_v_d = 0.5+1/np.pi*np.arctan(PV12__v_d/PV12__v_scale)
    PV12__H_up = PV12__w_v_d*PV12__H_L_in+(1-PV12__w_v_d)*PV12__H_R_in
    PV12__s_v_d = np.abs(PV12__v_d)/(np.abs(PV12__v_d)+PV12__v_eps)
    PV12__H_L_out = (1-PV12__w_v_d)*PV12__H_down+PV12__w_v_d*PV12__H_L_in
    PV12__H_R_out = PV12__w_v_d*PV12__H_down+(1-PV12__w_v_d)*PV12__H_R_in
    PV12__v_pos = PV12__w_v*PV12__v
    PV12__v_neg = (1-PV12__w_v)*-PV12__v
    PV12__v_d_pos = PV12__w_v_d*PV12__v_d
    PV12__v_d_neg = (1-PV12__w_v_d)*-PV12__v_d
    PV12__H_volume_L = PV12__w_v*PV12__H_L_in+(1-PV12__w_v)*PV12__H_L_out
    PV12__H_volume_R = PV12__w_v_d*PV12__H_R_out+(1-PV12__w_v_d)*PV12__H_R_in
    PV12__v_mm3_s = PV12__v/PV12__one_mm3
    PV12__v_d_mm3_s = PV12__v_d/PV12__one_mm3
    V11__w_v = 0.5+1/np.pi*np.arctan(V11__v/V11__v_scale)
    V11__H_up = V11__w_v*V11__H_L_in+(1-V11__w_v)*V11__H_R_in
    V11__s_v = np.abs(V11__v)/(np.abs(V11__v)+V11__v_eps)
    V11__H_L_out = (1-V11__w_v)*V11__H_down+V11__w_v*V11__H_L_in
    V11__H_R_out = V11__w_v*V11__H_down+(1-V11__w_v)*V11__H_R_in
    V11__v_pos = V11__w_v*V11__v
    V11__v_neg = (1-V11__w_v)*-V11__v
    V11__H_volume_L = V11__w_v*V11__H_L_in+(1-V11__w_v)*V11__H_L_out
    V11__H_volume_R = V11__w_v*V11__H_R_out+(1-V11__w_v)*V11__H_R_in
    V11__v_mm3_s = V11__v/V11__one_mm3
    V12__w_v = 0.5+1/np.pi*np.arctan(V12__v/V12__v_scale)
    V12__H_up = V12__w_v*V12__H_L_in+(1-V12__w_v)*V12__H_R_in
    V12__s_v = np.abs(V12__v)/(np.abs(V12__v)+V12__v_eps)
    V12__H_L_out = (1-V12__w_v)*V12__H_down+V12__w_v*V12__H_L_in
    V12__H_R_out = V12__w_v*V12__H_down+(1-V12__w_v)*V12__H_R_in
    V12__v_pos = V12__w_v*V12__v
    V12__v_neg = (1-V12__w_v)*-V12__v
    V12__H_volume_L = V12__w_v*V12__H_L_in+(1-V12__w_v)*V12__H_L_out
    V12__H_volume_R = V12__w_v*V12__H_R_out+(1-V12__w_v)*V12__H_R_in
    V12__v_mm3_s = V12__v/V12__one_mm3
    VV_junc7__vj1 = V6__v
    VV_junc7__vj3 = -PV13__v
    VV_junc7__vj4 = -PV14__v
    VV_junc7__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc7__vj1/VV_junc7__v_scale)
    VV_junc7__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc7__vj3/VV_junc7__v_scale)
    VV_junc7__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc7__vj4/VV_junc7__v_scale)
    VV_junc7__w_out1 = 1-VV_junc7__w_in1
    VV_junc7__w_out3 = 1-VV_junc7__w_in3
    VV_junc7__w_out4 = 1-VV_junc7__w_in4
    VV_junc7__Qin1 = VV_junc7__w_in1*VV_junc7__vj1
    VV_junc7__Qin3 = VV_junc7__w_in3*VV_junc7__vj3
    VV_junc7__Qin4 = VV_junc7__w_in4*VV_junc7__vj4
    VV_junc7__Qout1 = VV_junc7__w_out1*-VV_junc7__vj1
    VV_junc7__Qout3 = VV_junc7__w_out3*-VV_junc7__vj3
    VV_junc7__Qout4 = VV_junc7__w_out4*-VV_junc7__vj4
    VV_junc7__Qin_tot = VV_junc7__Qin1+VV_junc7__Qin2+VV_junc7__Qin3+VV_junc7__Qin4
    VV_junc7__Qout_tot = VV_junc7__Qout1+VV_junc7__Qout2+VV_junc7__Qout3+VV_junc7__Qout4
    VV_junc7__v = (VV_junc7__u-VV_junc7__u_d)/VV_junc7__R_VV_junc
    VV_junc7__bc1_is_in = (1 if VV_junc7__Qin1 > VV_junc7__v_threshold else 0)
    VV_junc7__bc3_is_in = (1 if VV_junc7__Qin3 > VV_junc7__v_threshold else 0)
    VV_junc7__bc4_is_in = (1 if VV_junc7__Qin4 > VV_junc7__v_threshold else 0)
    VV_junc7__bc1_is_out = (1 if VV_junc7__Qout1 > VV_junc7__v_threshold else 0)
    VV_junc7__bc3_is_out = (1 if VV_junc7__Qout3 > VV_junc7__v_threshold else 0)
    VV_junc7__bc4_is_out = (1 if VV_junc7__Qout4 > VV_junc7__v_threshold else 0)
    PV13__w_v = 0.5+1/np.pi*np.arctan(PV13__v/PV13__v_scale)
    PV13__w_v_d = 0.5+1/np.pi*np.arctan(PV13__v_d/PV13__v_scale)
    PV13__H_up = PV13__w_v_d*PV13__H_L_in+(1-PV13__w_v_d)*PV13__H_R_in
    PV13__s_v_d = np.abs(PV13__v_d)/(np.abs(PV13__v_d)+PV13__v_eps)
    PV13__H_L_out = (1-PV13__w_v_d)*PV13__H_down+PV13__w_v_d*PV13__H_L_in
    PV13__H_R_out = PV13__w_v_d*PV13__H_down+(1-PV13__w_v_d)*PV13__H_R_in
    PV13__v_pos = PV13__w_v*PV13__v
    PV13__v_neg = (1-PV13__w_v)*-PV13__v
    PV13__v_d_pos = PV13__w_v_d*PV13__v_d
    PV13__v_d_neg = (1-PV13__w_v_d)*-PV13__v_d
    PV13__H_volume_L = PV13__w_v*PV13__H_L_in+(1-PV13__w_v)*PV13__H_L_out
    PV13__H_volume_R = PV13__w_v_d*PV13__H_R_out+(1-PV13__w_v_d)*PV13__H_R_in
    PV13__v_mm3_s = PV13__v/PV13__one_mm3
    PV13__v_d_mm3_s = PV13__v_d/PV13__one_mm3
    PV14__w_v = 0.5+1/np.pi*np.arctan(PV14__v/PV14__v_scale)
    PV14__w_v_d = 0.5+1/np.pi*np.arctan(PV14__v_d/PV14__v_scale)
    PV14__H_up = PV14__w_v_d*PV14__H_L_in+(1-PV14__w_v_d)*PV14__H_R_in
    PV14__s_v_d = np.abs(PV14__v_d)/(np.abs(PV14__v_d)+PV14__v_eps)
    PV14__H_L_out = (1-PV14__w_v_d)*PV14__H_down+PV14__w_v_d*PV14__H_L_in
    PV14__H_R_out = PV14__w_v_d*PV14__H_down+(1-PV14__w_v_d)*PV14__H_R_in
    PV14__v_pos = PV14__w_v*PV14__v
    PV14__v_neg = (1-PV14__w_v)*-PV14__v
    PV14__v_d_pos = PV14__w_v_d*PV14__v_d
    PV14__v_d_neg = (1-PV14__w_v_d)*-PV14__v_d
    PV14__H_volume_L = PV14__w_v*PV14__H_L_in+(1-PV14__w_v)*PV14__H_L_out
    PV14__H_volume_R = PV14__w_v_d*PV14__H_R_out+(1-PV14__w_v_d)*PV14__H_R_in
    PV14__v_mm3_s = PV14__v/PV14__one_mm3
    PV14__v_d_mm3_s = PV14__v_d/PV14__one_mm3
    V13__w_v = 0.5+1/np.pi*np.arctan(V13__v/V13__v_scale)
    V13__H_up = V13__w_v*V13__H_L_in+(1-V13__w_v)*V13__H_R_in
    V13__s_v = np.abs(V13__v)/(np.abs(V13__v)+V13__v_eps)
    V13__H_L_out = (1-V13__w_v)*V13__H_down+V13__w_v*V13__H_L_in
    V13__H_R_out = V13__w_v*V13__H_down+(1-V13__w_v)*V13__H_R_in
    V13__v_pos = V13__w_v*V13__v
    V13__v_neg = (1-V13__w_v)*-V13__v
    V13__H_volume_L = V13__w_v*V13__H_L_in+(1-V13__w_v)*V13__H_L_out
    V13__H_volume_R = V13__w_v*V13__H_R_out+(1-V13__w_v)*V13__H_R_in
    V13__v_mm3_s = V13__v/V13__one_mm3
    V14__w_v = 0.5+1/np.pi*np.arctan(V14__v/V14__v_scale)
    V14__H_up = V14__w_v*V14__H_L_in+(1-V14__w_v)*V14__H_R_in
    V14__s_v = np.abs(V14__v)/(np.abs(V14__v)+V14__v_eps)
    V14__H_L_out = (1-V14__w_v)*V14__H_down+V14__w_v*V14__H_L_in
    V14__H_R_out = V14__w_v*V14__H_down+(1-V14__w_v)*V14__H_R_in
    V14__v_pos = V14__w_v*V14__v
    V14__v_neg = (1-V14__w_v)*-V14__v
    V14__H_volume_L = V14__w_v*V14__H_L_in+(1-V14__w_v)*V14__H_L_out
    V14__H_volume_R = V14__w_v*V14__H_R_out+(1-V14__w_v)*V14__H_R_in
    V14__v_mm3_s = V14__v/V14__one_mm3
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
    VV_junc4__n_in = VV_junc4__bc1_is_in+VV_junc4__bc2_is_in+VV_junc4__bc3_is_in+VV_junc4__bc4_is_in
    VV_junc4__n_out = VV_junc4__bc1_is_out+VV_junc4__bc2_is_out+VV_junc4__bc3_is_out+VV_junc4__bc4_is_out
    VV_junc4__RBC_in = VV_junc4__Qin1*V3__H_R_out+VV_junc4__Qin2*VV_junc4__H_to2+VV_junc4__Qin3*PV7__H_L_out+VV_junc4__Qin4*PV8__H_L_out
    VV_junc4__v_mm3_s = VV_junc4__v/VV_junc4__one_mm3
    VV_junc4__junction_type = (1 if VV_junc4__n_in == 1 else (-1 if VV_junc4__n_in >= 2 else 0))
    VV_junc4__is_split = (1 if VV_junc4__junction_type == 1 else 0)
    VV_junc4__is_merge = (1 if VV_junc4__junction_type == -1 else 0)
    VV_junc4__feed1 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin1 >= VV_junc4__Qin2) and (VV_junc4__Qin1 >= VV_junc4__Qin3) and (VV_junc4__Qin1 >= VV_junc4__Qin4) else 0)
    VV_junc4__feed2 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin2 > VV_junc4__Qin1) and (VV_junc4__Qin2 >= VV_junc4__Qin3) and (VV_junc4__Qin2 >= VV_junc4__Qin4) else 0)
    VV_junc4__feed3 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin3 > VV_junc4__Qin1) and (VV_junc4__Qin3 > VV_junc4__Qin2) and (VV_junc4__Qin3 >= VV_junc4__Qin4) else 0)
    VV_junc4__feed4 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__Qin4 > VV_junc4__Qin1) and (VV_junc4__Qin4 > VV_junc4__Qin2) and (VV_junc4__Qin4 > VV_junc4__Qin3) else 0)
    VV_junc4__alpha1 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc1_is_out == 1) and (VV_junc4__Qout1 >= VV_junc4__Qout2) and (VV_junc4__Qout1 >= VV_junc4__Qout3) and (VV_junc4__Qout1 >= VV_junc4__Qout4) else 0)
    VV_junc4__alpha2 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc2_is_out == 1) and (VV_junc4__Qout2 > VV_junc4__Qout1) and (VV_junc4__Qout2 >= VV_junc4__Qout3) and (VV_junc4__Qout2 >= VV_junc4__Qout4) else 0)
    VV_junc4__alpha3 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc3_is_out == 1) and (VV_junc4__Qout3 > VV_junc4__Qout1) and (VV_junc4__Qout3 > VV_junc4__Qout2) and (VV_junc4__Qout3 >= VV_junc4__Qout4) else 0)
    VV_junc4__alpha4 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc4_is_out == 1) and (VV_junc4__Qout4 > VV_junc4__Qout1) and (VV_junc4__Qout4 > VV_junc4__Qout2) and (VV_junc4__Qout4 > VV_junc4__Qout3) else 0)
    VV_junc4__Qout1_rem = (0 if VV_junc4__alpha1 == 1 else VV_junc4__Qout1)
    VV_junc4__Qout2_rem = (0 if VV_junc4__alpha2 == 1 else VV_junc4__Qout2)
    VV_junc4__Qout3_rem = (0 if VV_junc4__alpha3 == 1 else VV_junc4__Qout3)
    VV_junc4__Qout4_rem = (0 if VV_junc4__alpha4 == 1 else VV_junc4__Qout4)
    VV_junc4__beta1 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc1_is_out == 1) and (VV_junc4__alpha1 == 0) and (VV_junc4__Qout1_rem >= VV_junc4__Qout2_rem) and (VV_junc4__Qout1_rem >= VV_junc4__Qout3_rem) and (VV_junc4__Qout1_rem >= VV_junc4__Qout4_rem) else 0)
    VV_junc4__beta2 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc2_is_out == 1) and (VV_junc4__alpha2 == 0) and (VV_junc4__Qout2_rem > VV_junc4__Qout1_rem) and (VV_junc4__Qout2_rem >= VV_junc4__Qout3_rem) and (VV_junc4__Qout2_rem >= VV_junc4__Qout4_rem) else 0)
    VV_junc4__beta3 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc3_is_out == 1) and (VV_junc4__alpha3 == 0) and (VV_junc4__Qout3_rem > VV_junc4__Qout1_rem) and (VV_junc4__Qout3_rem > VV_junc4__Qout2_rem) and (VV_junc4__Qout3_rem >= VV_junc4__Qout4_rem) else 0)
    VV_junc4__beta4 = (1 if (VV_junc4__is_split == 1) and (VV_junc4__bc4_is_out == 1) and (VV_junc4__alpha4 == 0) and (VV_junc4__Qout4_rem > VV_junc4__Qout1_rem) and (VV_junc4__Qout4_rem > VV_junc4__Qout2_rem) and (VV_junc4__Qout4_rem > VV_junc4__Qout3_rem) else 0)
    VV_junc4__D_F = (VV_junc4__D1 if VV_junc4__feed1 == 1 else (VV_junc4__D2 if VV_junc4__feed2 == 1 else (VV_junc4__D3 if VV_junc4__feed3 == 1 else (VV_junc4__D4 if VV_junc4__feed4 == 1 else VV_junc4__D1))))
    VV_junc4__D_alpha = (VV_junc4__D1 if VV_junc4__alpha1 == 1 else (VV_junc4__D2 if VV_junc4__alpha2 == 1 else (VV_junc4__D3 if VV_junc4__alpha3 == 1 else (VV_junc4__D4 if VV_junc4__alpha4 == 1 else VV_junc4__D3))))
    VV_junc4__D_beta = (VV_junc4__D1 if VV_junc4__beta1 == 1 else (VV_junc4__D2 if VV_junc4__beta2 == 1 else (VV_junc4__D3 if VV_junc4__beta3 == 1 else (VV_junc4__D4 if VV_junc4__beta4 == 1 else VV_junc4__D4))))
    VV_junc4__v_alpha = (VV_junc4__Qout1 if VV_junc4__alpha1 == 1 else (VV_junc4__Qout2 if VV_junc4__alpha2 == 1 else (VV_junc4__Qout3 if VV_junc4__alpha3 == 1 else (VV_junc4__Qout4 if VV_junc4__alpha4 == 1 else 0))))
    VV_junc4__v_beta = (VV_junc4__Qout1 if VV_junc4__beta1 == 1 else (VV_junc4__Qout2 if VV_junc4__beta2 == 1 else (VV_junc4__Qout3 if VV_junc4__beta3 == 1 else (VV_junc4__Qout4 if VV_junc4__beta4 == 1 else 0))))
    PV7__H_down_target = PV7__s_v_d*(PV7__H_mean+PV7__gamma_mirror*(PV7__H_mean-PV7__H_up))+(1-PV7__s_v_d)*PV7__H_mean
    PV8__H_down_target = PV8__s_v_d*(PV8__H_mean+PV8__gamma_mirror*(PV8__H_mean-PV8__H_up))+(1-PV8__s_v_d)*PV8__H_mean
    V7__H_down_target = V7__s_v*(V7__H_mean+V7__gamma_mirror*(V7__H_mean-V7__H_up))+(1-V7__s_v)*V7__H_mean
    V8__H_down_target = V8__s_v*(V8__H_mean+V8__gamma_mirror*(V8__H_mean-V8__H_up))+(1-V8__s_v)*V8__H_mean
    VV_junc5__n_in = VV_junc5__bc1_is_in+VV_junc5__bc2_is_in+VV_junc5__bc3_is_in+VV_junc5__bc4_is_in
    VV_junc5__n_out = VV_junc5__bc1_is_out+VV_junc5__bc2_is_out+VV_junc5__bc3_is_out+VV_junc5__bc4_is_out
    VV_junc5__RBC_in = VV_junc5__Qin1*V4__H_R_out+VV_junc5__Qin2*VV_junc5__H_to2+VV_junc5__Qin3*PV9__H_L_out+VV_junc5__Qin4*PV10__H_L_out
    VV_junc5__v_mm3_s = VV_junc5__v/VV_junc5__one_mm3
    VV_junc5__junction_type = (1 if VV_junc5__n_in == 1 else (-1 if VV_junc5__n_in >= 2 else 0))
    VV_junc5__is_split = (1 if VV_junc5__junction_type == 1 else 0)
    VV_junc5__is_merge = (1 if VV_junc5__junction_type == -1 else 0)
    VV_junc5__feed1 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin1 >= VV_junc5__Qin2) and (VV_junc5__Qin1 >= VV_junc5__Qin3) and (VV_junc5__Qin1 >= VV_junc5__Qin4) else 0)
    VV_junc5__feed2 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin2 > VV_junc5__Qin1) and (VV_junc5__Qin2 >= VV_junc5__Qin3) and (VV_junc5__Qin2 >= VV_junc5__Qin4) else 0)
    VV_junc5__feed3 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin3 > VV_junc5__Qin1) and (VV_junc5__Qin3 > VV_junc5__Qin2) and (VV_junc5__Qin3 >= VV_junc5__Qin4) else 0)
    VV_junc5__feed4 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__Qin4 > VV_junc5__Qin1) and (VV_junc5__Qin4 > VV_junc5__Qin2) and (VV_junc5__Qin4 > VV_junc5__Qin3) else 0)
    VV_junc5__alpha1 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc1_is_out == 1) and (VV_junc5__Qout1 >= VV_junc5__Qout2) and (VV_junc5__Qout1 >= VV_junc5__Qout3) and (VV_junc5__Qout1 >= VV_junc5__Qout4) else 0)
    VV_junc5__alpha2 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc2_is_out == 1) and (VV_junc5__Qout2 > VV_junc5__Qout1) and (VV_junc5__Qout2 >= VV_junc5__Qout3) and (VV_junc5__Qout2 >= VV_junc5__Qout4) else 0)
    VV_junc5__alpha3 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc3_is_out == 1) and (VV_junc5__Qout3 > VV_junc5__Qout1) and (VV_junc5__Qout3 > VV_junc5__Qout2) and (VV_junc5__Qout3 >= VV_junc5__Qout4) else 0)
    VV_junc5__alpha4 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc4_is_out == 1) and (VV_junc5__Qout4 > VV_junc5__Qout1) and (VV_junc5__Qout4 > VV_junc5__Qout2) and (VV_junc5__Qout4 > VV_junc5__Qout3) else 0)
    VV_junc5__Qout1_rem = (0 if VV_junc5__alpha1 == 1 else VV_junc5__Qout1)
    VV_junc5__Qout2_rem = (0 if VV_junc5__alpha2 == 1 else VV_junc5__Qout2)
    VV_junc5__Qout3_rem = (0 if VV_junc5__alpha3 == 1 else VV_junc5__Qout3)
    VV_junc5__Qout4_rem = (0 if VV_junc5__alpha4 == 1 else VV_junc5__Qout4)
    VV_junc5__beta1 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc1_is_out == 1) and (VV_junc5__alpha1 == 0) and (VV_junc5__Qout1_rem >= VV_junc5__Qout2_rem) and (VV_junc5__Qout1_rem >= VV_junc5__Qout3_rem) and (VV_junc5__Qout1_rem >= VV_junc5__Qout4_rem) else 0)
    VV_junc5__beta2 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc2_is_out == 1) and (VV_junc5__alpha2 == 0) and (VV_junc5__Qout2_rem > VV_junc5__Qout1_rem) and (VV_junc5__Qout2_rem >= VV_junc5__Qout3_rem) and (VV_junc5__Qout2_rem >= VV_junc5__Qout4_rem) else 0)
    VV_junc5__beta3 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc3_is_out == 1) and (VV_junc5__alpha3 == 0) and (VV_junc5__Qout3_rem > VV_junc5__Qout1_rem) and (VV_junc5__Qout3_rem > VV_junc5__Qout2_rem) and (VV_junc5__Qout3_rem >= VV_junc5__Qout4_rem) else 0)
    VV_junc5__beta4 = (1 if (VV_junc5__is_split == 1) and (VV_junc5__bc4_is_out == 1) and (VV_junc5__alpha4 == 0) and (VV_junc5__Qout4_rem > VV_junc5__Qout1_rem) and (VV_junc5__Qout4_rem > VV_junc5__Qout2_rem) and (VV_junc5__Qout4_rem > VV_junc5__Qout3_rem) else 0)
    VV_junc5__D_F = (VV_junc5__D1 if VV_junc5__feed1 == 1 else (VV_junc5__D2 if VV_junc5__feed2 == 1 else (VV_junc5__D3 if VV_junc5__feed3 == 1 else (VV_junc5__D4 if VV_junc5__feed4 == 1 else VV_junc5__D1))))
    VV_junc5__D_alpha = (VV_junc5__D1 if VV_junc5__alpha1 == 1 else (VV_junc5__D2 if VV_junc5__alpha2 == 1 else (VV_junc5__D3 if VV_junc5__alpha3 == 1 else (VV_junc5__D4 if VV_junc5__alpha4 == 1 else VV_junc5__D3))))
    VV_junc5__D_beta = (VV_junc5__D1 if VV_junc5__beta1 == 1 else (VV_junc5__D2 if VV_junc5__beta2 == 1 else (VV_junc5__D3 if VV_junc5__beta3 == 1 else (VV_junc5__D4 if VV_junc5__beta4 == 1 else VV_junc5__D4))))
    VV_junc5__v_alpha = (VV_junc5__Qout1 if VV_junc5__alpha1 == 1 else (VV_junc5__Qout2 if VV_junc5__alpha2 == 1 else (VV_junc5__Qout3 if VV_junc5__alpha3 == 1 else (VV_junc5__Qout4 if VV_junc5__alpha4 == 1 else 0))))
    VV_junc5__v_beta = (VV_junc5__Qout1 if VV_junc5__beta1 == 1 else (VV_junc5__Qout2 if VV_junc5__beta2 == 1 else (VV_junc5__Qout3 if VV_junc5__beta3 == 1 else (VV_junc5__Qout4 if VV_junc5__beta4 == 1 else 0))))
    PV9__H_down_target = PV9__s_v_d*(PV9__H_mean+PV9__gamma_mirror*(PV9__H_mean-PV9__H_up))+(1-PV9__s_v_d)*PV9__H_mean
    PV10__H_down_target = PV10__s_v_d*(PV10__H_mean+PV10__gamma_mirror*(PV10__H_mean-PV10__H_up))+(1-PV10__s_v_d)*PV10__H_mean
    V9__H_down_target = V9__s_v*(V9__H_mean+V9__gamma_mirror*(V9__H_mean-V9__H_up))+(1-V9__s_v)*V9__H_mean
    V10__H_down_target = V10__s_v*(V10__H_mean+V10__gamma_mirror*(V10__H_mean-V10__H_up))+(1-V10__s_v)*V10__H_mean
    VV_junc6__n_in = VV_junc6__bc1_is_in+VV_junc6__bc2_is_in+VV_junc6__bc3_is_in+VV_junc6__bc4_is_in
    VV_junc6__n_out = VV_junc6__bc1_is_out+VV_junc6__bc2_is_out+VV_junc6__bc3_is_out+VV_junc6__bc4_is_out
    VV_junc6__RBC_in = VV_junc6__Qin1*V5__H_R_out+VV_junc6__Qin2*VV_junc6__H_to2+VV_junc6__Qin3*PV11__H_L_out+VV_junc6__Qin4*PV12__H_L_out
    VV_junc6__v_mm3_s = VV_junc6__v/VV_junc6__one_mm3
    VV_junc6__junction_type = (1 if VV_junc6__n_in == 1 else (-1 if VV_junc6__n_in >= 2 else 0))
    VV_junc6__is_split = (1 if VV_junc6__junction_type == 1 else 0)
    VV_junc6__is_merge = (1 if VV_junc6__junction_type == -1 else 0)
    VV_junc6__feed1 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin1 >= VV_junc6__Qin2) and (VV_junc6__Qin1 >= VV_junc6__Qin3) and (VV_junc6__Qin1 >= VV_junc6__Qin4) else 0)
    VV_junc6__feed2 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin2 > VV_junc6__Qin1) and (VV_junc6__Qin2 >= VV_junc6__Qin3) and (VV_junc6__Qin2 >= VV_junc6__Qin4) else 0)
    VV_junc6__feed3 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin3 > VV_junc6__Qin1) and (VV_junc6__Qin3 > VV_junc6__Qin2) and (VV_junc6__Qin3 >= VV_junc6__Qin4) else 0)
    VV_junc6__feed4 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__Qin4 > VV_junc6__Qin1) and (VV_junc6__Qin4 > VV_junc6__Qin2) and (VV_junc6__Qin4 > VV_junc6__Qin3) else 0)
    VV_junc6__alpha1 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc1_is_out == 1) and (VV_junc6__Qout1 >= VV_junc6__Qout2) and (VV_junc6__Qout1 >= VV_junc6__Qout3) and (VV_junc6__Qout1 >= VV_junc6__Qout4) else 0)
    VV_junc6__alpha2 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc2_is_out == 1) and (VV_junc6__Qout2 > VV_junc6__Qout1) and (VV_junc6__Qout2 >= VV_junc6__Qout3) and (VV_junc6__Qout2 >= VV_junc6__Qout4) else 0)
    VV_junc6__alpha3 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc3_is_out == 1) and (VV_junc6__Qout3 > VV_junc6__Qout1) and (VV_junc6__Qout3 > VV_junc6__Qout2) and (VV_junc6__Qout3 >= VV_junc6__Qout4) else 0)
    VV_junc6__alpha4 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc4_is_out == 1) and (VV_junc6__Qout4 > VV_junc6__Qout1) and (VV_junc6__Qout4 > VV_junc6__Qout2) and (VV_junc6__Qout4 > VV_junc6__Qout3) else 0)
    VV_junc6__Qout1_rem = (0 if VV_junc6__alpha1 == 1 else VV_junc6__Qout1)
    VV_junc6__Qout2_rem = (0 if VV_junc6__alpha2 == 1 else VV_junc6__Qout2)
    VV_junc6__Qout3_rem = (0 if VV_junc6__alpha3 == 1 else VV_junc6__Qout3)
    VV_junc6__Qout4_rem = (0 if VV_junc6__alpha4 == 1 else VV_junc6__Qout4)
    VV_junc6__beta1 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc1_is_out == 1) and (VV_junc6__alpha1 == 0) and (VV_junc6__Qout1_rem >= VV_junc6__Qout2_rem) and (VV_junc6__Qout1_rem >= VV_junc6__Qout3_rem) and (VV_junc6__Qout1_rem >= VV_junc6__Qout4_rem) else 0)
    VV_junc6__beta2 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc2_is_out == 1) and (VV_junc6__alpha2 == 0) and (VV_junc6__Qout2_rem > VV_junc6__Qout1_rem) and (VV_junc6__Qout2_rem >= VV_junc6__Qout3_rem) and (VV_junc6__Qout2_rem >= VV_junc6__Qout4_rem) else 0)
    VV_junc6__beta3 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc3_is_out == 1) and (VV_junc6__alpha3 == 0) and (VV_junc6__Qout3_rem > VV_junc6__Qout1_rem) and (VV_junc6__Qout3_rem > VV_junc6__Qout2_rem) and (VV_junc6__Qout3_rem >= VV_junc6__Qout4_rem) else 0)
    VV_junc6__beta4 = (1 if (VV_junc6__is_split == 1) and (VV_junc6__bc4_is_out == 1) and (VV_junc6__alpha4 == 0) and (VV_junc6__Qout4_rem > VV_junc6__Qout1_rem) and (VV_junc6__Qout4_rem > VV_junc6__Qout2_rem) and (VV_junc6__Qout4_rem > VV_junc6__Qout3_rem) else 0)
    VV_junc6__D_F = (VV_junc6__D1 if VV_junc6__feed1 == 1 else (VV_junc6__D2 if VV_junc6__feed2 == 1 else (VV_junc6__D3 if VV_junc6__feed3 == 1 else (VV_junc6__D4 if VV_junc6__feed4 == 1 else VV_junc6__D1))))
    VV_junc6__D_alpha = (VV_junc6__D1 if VV_junc6__alpha1 == 1 else (VV_junc6__D2 if VV_junc6__alpha2 == 1 else (VV_junc6__D3 if VV_junc6__alpha3 == 1 else (VV_junc6__D4 if VV_junc6__alpha4 == 1 else VV_junc6__D3))))
    VV_junc6__D_beta = (VV_junc6__D1 if VV_junc6__beta1 == 1 else (VV_junc6__D2 if VV_junc6__beta2 == 1 else (VV_junc6__D3 if VV_junc6__beta3 == 1 else (VV_junc6__D4 if VV_junc6__beta4 == 1 else VV_junc6__D4))))
    VV_junc6__v_alpha = (VV_junc6__Qout1 if VV_junc6__alpha1 == 1 else (VV_junc6__Qout2 if VV_junc6__alpha2 == 1 else (VV_junc6__Qout3 if VV_junc6__alpha3 == 1 else (VV_junc6__Qout4 if VV_junc6__alpha4 == 1 else 0))))
    VV_junc6__v_beta = (VV_junc6__Qout1 if VV_junc6__beta1 == 1 else (VV_junc6__Qout2 if VV_junc6__beta2 == 1 else (VV_junc6__Qout3 if VV_junc6__beta3 == 1 else (VV_junc6__Qout4 if VV_junc6__beta4 == 1 else 0))))
    PV11__H_down_target = PV11__s_v_d*(PV11__H_mean+PV11__gamma_mirror*(PV11__H_mean-PV11__H_up))+(1-PV11__s_v_d)*PV11__H_mean
    PV12__H_down_target = PV12__s_v_d*(PV12__H_mean+PV12__gamma_mirror*(PV12__H_mean-PV12__H_up))+(1-PV12__s_v_d)*PV12__H_mean
    V11__H_down_target = V11__s_v*(V11__H_mean+V11__gamma_mirror*(V11__H_mean-V11__H_up))+(1-V11__s_v)*V11__H_mean
    V12__H_down_target = V12__s_v*(V12__H_mean+V12__gamma_mirror*(V12__H_mean-V12__H_up))+(1-V12__s_v)*V12__H_mean
    VV_junc7__n_in = VV_junc7__bc1_is_in+VV_junc7__bc2_is_in+VV_junc7__bc3_is_in+VV_junc7__bc4_is_in
    VV_junc7__n_out = VV_junc7__bc1_is_out+VV_junc7__bc2_is_out+VV_junc7__bc3_is_out+VV_junc7__bc4_is_out
    VV_junc7__RBC_in = VV_junc7__Qin1*V6__H_R_out+VV_junc7__Qin2*VV_junc7__H_to2+VV_junc7__Qin3*PV13__H_L_out+VV_junc7__Qin4*PV14__H_L_out
    VV_junc7__v_mm3_s = VV_junc7__v/VV_junc7__one_mm3
    VV_junc7__junction_type = (1 if VV_junc7__n_in == 1 else (-1 if VV_junc7__n_in >= 2 else 0))
    VV_junc7__is_split = (1 if VV_junc7__junction_type == 1 else 0)
    VV_junc7__is_merge = (1 if VV_junc7__junction_type == -1 else 0)
    VV_junc7__feed1 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin1 >= VV_junc7__Qin2) and (VV_junc7__Qin1 >= VV_junc7__Qin3) and (VV_junc7__Qin1 >= VV_junc7__Qin4) else 0)
    VV_junc7__feed2 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin2 > VV_junc7__Qin1) and (VV_junc7__Qin2 >= VV_junc7__Qin3) and (VV_junc7__Qin2 >= VV_junc7__Qin4) else 0)
    VV_junc7__feed3 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin3 > VV_junc7__Qin1) and (VV_junc7__Qin3 > VV_junc7__Qin2) and (VV_junc7__Qin3 >= VV_junc7__Qin4) else 0)
    VV_junc7__feed4 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__Qin4 > VV_junc7__Qin1) and (VV_junc7__Qin4 > VV_junc7__Qin2) and (VV_junc7__Qin4 > VV_junc7__Qin3) else 0)
    VV_junc7__alpha1 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc1_is_out == 1) and (VV_junc7__Qout1 >= VV_junc7__Qout2) and (VV_junc7__Qout1 >= VV_junc7__Qout3) and (VV_junc7__Qout1 >= VV_junc7__Qout4) else 0)
    VV_junc7__alpha2 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc2_is_out == 1) and (VV_junc7__Qout2 > VV_junc7__Qout1) and (VV_junc7__Qout2 >= VV_junc7__Qout3) and (VV_junc7__Qout2 >= VV_junc7__Qout4) else 0)
    VV_junc7__alpha3 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc3_is_out == 1) and (VV_junc7__Qout3 > VV_junc7__Qout1) and (VV_junc7__Qout3 > VV_junc7__Qout2) and (VV_junc7__Qout3 >= VV_junc7__Qout4) else 0)
    VV_junc7__alpha4 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc4_is_out == 1) and (VV_junc7__Qout4 > VV_junc7__Qout1) and (VV_junc7__Qout4 > VV_junc7__Qout2) and (VV_junc7__Qout4 > VV_junc7__Qout3) else 0)
    VV_junc7__Qout1_rem = (0 if VV_junc7__alpha1 == 1 else VV_junc7__Qout1)
    VV_junc7__Qout2_rem = (0 if VV_junc7__alpha2 == 1 else VV_junc7__Qout2)
    VV_junc7__Qout3_rem = (0 if VV_junc7__alpha3 == 1 else VV_junc7__Qout3)
    VV_junc7__Qout4_rem = (0 if VV_junc7__alpha4 == 1 else VV_junc7__Qout4)
    VV_junc7__beta1 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc1_is_out == 1) and (VV_junc7__alpha1 == 0) and (VV_junc7__Qout1_rem >= VV_junc7__Qout2_rem) and (VV_junc7__Qout1_rem >= VV_junc7__Qout3_rem) and (VV_junc7__Qout1_rem >= VV_junc7__Qout4_rem) else 0)
    VV_junc7__beta2 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc2_is_out == 1) and (VV_junc7__alpha2 == 0) and (VV_junc7__Qout2_rem > VV_junc7__Qout1_rem) and (VV_junc7__Qout2_rem >= VV_junc7__Qout3_rem) and (VV_junc7__Qout2_rem >= VV_junc7__Qout4_rem) else 0)
    VV_junc7__beta3 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc3_is_out == 1) and (VV_junc7__alpha3 == 0) and (VV_junc7__Qout3_rem > VV_junc7__Qout1_rem) and (VV_junc7__Qout3_rem > VV_junc7__Qout2_rem) and (VV_junc7__Qout3_rem >= VV_junc7__Qout4_rem) else 0)
    VV_junc7__beta4 = (1 if (VV_junc7__is_split == 1) and (VV_junc7__bc4_is_out == 1) and (VV_junc7__alpha4 == 0) and (VV_junc7__Qout4_rem > VV_junc7__Qout1_rem) and (VV_junc7__Qout4_rem > VV_junc7__Qout2_rem) and (VV_junc7__Qout4_rem > VV_junc7__Qout3_rem) else 0)
    VV_junc7__D_F = (VV_junc7__D1 if VV_junc7__feed1 == 1 else (VV_junc7__D2 if VV_junc7__feed2 == 1 else (VV_junc7__D3 if VV_junc7__feed3 == 1 else (VV_junc7__D4 if VV_junc7__feed4 == 1 else VV_junc7__D1))))
    VV_junc7__D_alpha = (VV_junc7__D1 if VV_junc7__alpha1 == 1 else (VV_junc7__D2 if VV_junc7__alpha2 == 1 else (VV_junc7__D3 if VV_junc7__alpha3 == 1 else (VV_junc7__D4 if VV_junc7__alpha4 == 1 else VV_junc7__D3))))
    VV_junc7__D_beta = (VV_junc7__D1 if VV_junc7__beta1 == 1 else (VV_junc7__D2 if VV_junc7__beta2 == 1 else (VV_junc7__D3 if VV_junc7__beta3 == 1 else (VV_junc7__D4 if VV_junc7__beta4 == 1 else VV_junc7__D4))))
    VV_junc7__v_alpha = (VV_junc7__Qout1 if VV_junc7__alpha1 == 1 else (VV_junc7__Qout2 if VV_junc7__alpha2 == 1 else (VV_junc7__Qout3 if VV_junc7__alpha3 == 1 else (VV_junc7__Qout4 if VV_junc7__alpha4 == 1 else 0))))
    VV_junc7__v_beta = (VV_junc7__Qout1 if VV_junc7__beta1 == 1 else (VV_junc7__Qout2 if VV_junc7__beta2 == 1 else (VV_junc7__Qout3 if VV_junc7__beta3 == 1 else (VV_junc7__Qout4 if VV_junc7__beta4 == 1 else 0))))
    PV13__H_down_target = PV13__s_v_d*(PV13__H_mean+PV13__gamma_mirror*(PV13__H_mean-PV13__H_up))+(1-PV13__s_v_d)*PV13__H_mean
    PV14__H_down_target = PV14__s_v_d*(PV14__H_mean+PV14__gamma_mirror*(PV14__H_mean-PV14__H_up))+(1-PV14__s_v_d)*PV14__H_mean
    V13__H_down_target = V13__s_v*(V13__H_mean+V13__gamma_mirror*(V13__H_mean-V13__H_up))+(1-V13__s_v)*V13__H_mean
    V14__H_down_target = V14__s_v*(V14__H_mean+V14__gamma_mirror*(V14__H_mean-V14__H_up))+(1-V14__s_v)*V14__H_mean
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
    V3__H_down_target = V3__s_v*(V3__H_mean+V3__gamma_mirror*(V3__H_mean-V3__H_up))+(1-V3__s_v)*V3__H_mean
    V4__H_down_target = V4__s_v*(V4__H_mean+V4__gamma_mirror*(V4__H_mean-V4__H_up))+(1-V4__s_v)*V4__H_mean
    VV_junc3__FQB_alpha = (VV_junc3__v_alpha+VV_junc3__div_0)/(VV_junc3__v_alpha+VV_junc3__v_beta+2*VV_junc3__div_0)
    VV_junc3__B = 1+6.98*(1-VV_junc3__H_mean)/(VV_junc3__D_F*1e6)
    VV_junc3__A = -6.96*np.log(VV_junc3__D_alpha*1e6/(VV_junc3__D_beta*1e6))/(VV_junc3__D_F*1e6)
    VV_junc3__X_0 = 0.4/(VV_junc3__D_F*1e6)
    VV_junc3__y_raw = (VV_junc3__FQB_alpha-VV_junc3__X_0)/(1-2*VV_junc3__X_0+VV_junc3__div_0)
    VV_junc3__y = min(max(VV_junc3__y_raw, VV_junc3__div_0y), 1-VV_junc3__div_0y)
    V5__H_down_target = V5__s_v*(V5__H_mean+V5__gamma_mirror*(V5__H_mean-V5__H_up))+(1-V5__s_v)*V5__H_mean
    V6__H_down_target = V6__s_v*(V6__H_mean+V6__gamma_mirror*(V6__H_mean-V6__H_up))+(1-V6__s_v)*V6__H_mean
    VV_junc4__FQB_alpha = (VV_junc4__v_alpha+VV_junc4__div_0)/(VV_junc4__v_alpha+VV_junc4__v_beta+2*VV_junc4__div_0)
    VV_junc4__B = 1+6.98*(1-VV_junc4__H_mean)/(VV_junc4__D_F*1e6)
    VV_junc4__A = -6.96*np.log(VV_junc4__D_alpha*1e6/(VV_junc4__D_beta*1e6))/(VV_junc4__D_F*1e6)
    VV_junc4__X_0 = 0.4/(VV_junc4__D_F*1e6)
    VV_junc4__y_raw = (VV_junc4__FQB_alpha-VV_junc4__X_0)/(1-2*VV_junc4__X_0+VV_junc4__div_0)
    VV_junc4__y = min(max(VV_junc4__y_raw, VV_junc4__div_0y), 1-VV_junc4__div_0y)
    VV_junc5__FQB_alpha = (VV_junc5__v_alpha+VV_junc5__div_0)/(VV_junc5__v_alpha+VV_junc5__v_beta+2*VV_junc5__div_0)
    VV_junc5__B = 1+6.98*(1-VV_junc5__H_mean)/(VV_junc5__D_F*1e6)
    VV_junc5__A = -6.96*np.log(VV_junc5__D_alpha*1e6/(VV_junc5__D_beta*1e6))/(VV_junc5__D_F*1e6)
    VV_junc5__X_0 = 0.4/(VV_junc5__D_F*1e6)
    VV_junc5__y_raw = (VV_junc5__FQB_alpha-VV_junc5__X_0)/(1-2*VV_junc5__X_0+VV_junc5__div_0)
    VV_junc5__y = min(max(VV_junc5__y_raw, VV_junc5__div_0y), 1-VV_junc5__div_0y)
    VV_junc6__FQB_alpha = (VV_junc6__v_alpha+VV_junc6__div_0)/(VV_junc6__v_alpha+VV_junc6__v_beta+2*VV_junc6__div_0)
    VV_junc6__B = 1+6.98*(1-VV_junc6__H_mean)/(VV_junc6__D_F*1e6)
    VV_junc6__A = -6.96*np.log(VV_junc6__D_alpha*1e6/(VV_junc6__D_beta*1e6))/(VV_junc6__D_F*1e6)
    VV_junc6__X_0 = 0.4/(VV_junc6__D_F*1e6)
    VV_junc6__y_raw = (VV_junc6__FQB_alpha-VV_junc6__X_0)/(1-2*VV_junc6__X_0+VV_junc6__div_0)
    VV_junc6__y = min(max(VV_junc6__y_raw, VV_junc6__div_0y), 1-VV_junc6__div_0y)
    VV_junc7__FQB_alpha = (VV_junc7__v_alpha+VV_junc7__div_0)/(VV_junc7__v_alpha+VV_junc7__v_beta+2*VV_junc7__div_0)
    VV_junc7__B = 1+6.98*(1-VV_junc7__H_mean)/(VV_junc7__D_F*1e6)
    VV_junc7__A = -6.96*np.log(VV_junc7__D_alpha*1e6/(VV_junc7__D_beta*1e6))/(VV_junc7__D_F*1e6)
    VV_junc7__X_0 = 0.4/(VV_junc7__D_F*1e6)
    VV_junc7__y_raw = (VV_junc7__FQB_alpha-VV_junc7__X_0)/(1-2*VV_junc7__X_0+VV_junc7__div_0)
    VV_junc7__y = min(max(VV_junc7__y_raw, VV_junc7__div_0y), 1-VV_junc7__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc2__ph = np.log(VV_junc2__y/(1-VV_junc2__y))
    VV_junc3__ph = np.log(VV_junc3__y/(1-VV_junc3__y))
    VV_junc4__ph = np.log(VV_junc4__y/(1-VV_junc4__y))
    VV_junc5__ph = np.log(VV_junc5__y/(1-VV_junc5__y))
    VV_junc6__ph = np.log(VV_junc6__y/(1-VV_junc6__y))
    VV_junc7__ph = np.log(VV_junc7__y/(1-VV_junc7__y))
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
    VV_junc4__FQE_alpha = 1/(1+np.exp(-(VV_junc4__A+VV_junc4__B*VV_junc4__ph)))
    VV_junc4__H_VV_out_alpha = VV_junc4__H_mean*VV_junc4__FQE_alpha/(VV_junc4__FQB_alpha+VV_junc4__div_0)
    VV_junc4__H_VV_out_beta = VV_junc4__H_mean*(1-VV_junc4__FQE_alpha)/(1-VV_junc4__FQB_alpha+VV_junc4__div_0)
    VV_junc4__H_split1 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha1 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta1 == 1 else V3__H_R_out))
    VV_junc4__H_split2 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha2 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta2 == 1 else VV_junc4__H_to2))
    VV_junc4__H_split3 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha3 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta3 == 1 else PV7__H_L_out))
    VV_junc4__H_split4 = (VV_junc4__H_VV_out_alpha if VV_junc4__alpha4 == 1 else (VV_junc4__H_VV_out_beta if VV_junc4__beta4 == 1 else PV8__H_L_out))
    VV_junc4__H_daughter1 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split1 if VV_junc4__is_split == 1 else V3__H_R_out))
    VV_junc4__H_daughter2 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split2 if VV_junc4__is_split == 1 else VV_junc4__H_to2))
    VV_junc4__H_daughter3 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split3 if VV_junc4__is_split == 1 else PV7__H_L_out))
    VV_junc4__H_daughter4 = (VV_junc4__H_mean if VV_junc4__is_merge == 1 else (VV_junc4__H_split4 if VV_junc4__is_split == 1 else PV8__H_L_out))
    VV_junc4__H_from1_target = (VV_junc4__H_daughter1 if VV_junc4__bc1_is_out == 1 else V3__H_R_out)
    VV_junc4__H_from2_target = (VV_junc4__H_daughter2 if VV_junc4__bc2_is_out == 1 else VV_junc4__H_to2)
    VV_junc4__H_from3_target = (VV_junc4__H_daughter3 if VV_junc4__bc3_is_out == 1 else PV7__H_L_out)
    VV_junc4__H_from4_target = (VV_junc4__H_daughter4 if VV_junc4__bc4_is_out == 1 else PV8__H_L_out)
    VV_junc5__FQE_alpha = 1/(1+np.exp(-(VV_junc5__A+VV_junc5__B*VV_junc5__ph)))
    VV_junc5__H_VV_out_alpha = VV_junc5__H_mean*VV_junc5__FQE_alpha/(VV_junc5__FQB_alpha+VV_junc5__div_0)
    VV_junc5__H_VV_out_beta = VV_junc5__H_mean*(1-VV_junc5__FQE_alpha)/(1-VV_junc5__FQB_alpha+VV_junc5__div_0)
    VV_junc5__H_split1 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha1 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta1 == 1 else V4__H_R_out))
    VV_junc5__H_split2 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha2 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta2 == 1 else VV_junc5__H_to2))
    VV_junc5__H_split3 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha3 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta3 == 1 else PV9__H_L_out))
    VV_junc5__H_split4 = (VV_junc5__H_VV_out_alpha if VV_junc5__alpha4 == 1 else (VV_junc5__H_VV_out_beta if VV_junc5__beta4 == 1 else PV10__H_L_out))
    VV_junc5__H_daughter1 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split1 if VV_junc5__is_split == 1 else V4__H_R_out))
    VV_junc5__H_daughter2 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split2 if VV_junc5__is_split == 1 else VV_junc5__H_to2))
    VV_junc5__H_daughter3 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split3 if VV_junc5__is_split == 1 else PV9__H_L_out))
    VV_junc5__H_daughter4 = (VV_junc5__H_mean if VV_junc5__is_merge == 1 else (VV_junc5__H_split4 if VV_junc5__is_split == 1 else PV10__H_L_out))
    VV_junc5__H_from1_target = (VV_junc5__H_daughter1 if VV_junc5__bc1_is_out == 1 else V4__H_R_out)
    VV_junc5__H_from2_target = (VV_junc5__H_daughter2 if VV_junc5__bc2_is_out == 1 else VV_junc5__H_to2)
    VV_junc5__H_from3_target = (VV_junc5__H_daughter3 if VV_junc5__bc3_is_out == 1 else PV9__H_L_out)
    VV_junc5__H_from4_target = (VV_junc5__H_daughter4 if VV_junc5__bc4_is_out == 1 else PV10__H_L_out)
    VV_junc6__FQE_alpha = 1/(1+np.exp(-(VV_junc6__A+VV_junc6__B*VV_junc6__ph)))
    VV_junc6__H_VV_out_alpha = VV_junc6__H_mean*VV_junc6__FQE_alpha/(VV_junc6__FQB_alpha+VV_junc6__div_0)
    VV_junc6__H_VV_out_beta = VV_junc6__H_mean*(1-VV_junc6__FQE_alpha)/(1-VV_junc6__FQB_alpha+VV_junc6__div_0)
    VV_junc6__H_split1 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha1 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta1 == 1 else V5__H_R_out))
    VV_junc6__H_split2 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha2 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta2 == 1 else VV_junc6__H_to2))
    VV_junc6__H_split3 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha3 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta3 == 1 else PV11__H_L_out))
    VV_junc6__H_split4 = (VV_junc6__H_VV_out_alpha if VV_junc6__alpha4 == 1 else (VV_junc6__H_VV_out_beta if VV_junc6__beta4 == 1 else PV12__H_L_out))
    VV_junc6__H_daughter1 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split1 if VV_junc6__is_split == 1 else V5__H_R_out))
    VV_junc6__H_daughter2 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split2 if VV_junc6__is_split == 1 else VV_junc6__H_to2))
    VV_junc6__H_daughter3 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split3 if VV_junc6__is_split == 1 else PV11__H_L_out))
    VV_junc6__H_daughter4 = (VV_junc6__H_mean if VV_junc6__is_merge == 1 else (VV_junc6__H_split4 if VV_junc6__is_split == 1 else PV12__H_L_out))
    VV_junc6__H_from1_target = (VV_junc6__H_daughter1 if VV_junc6__bc1_is_out == 1 else V5__H_R_out)
    VV_junc6__H_from2_target = (VV_junc6__H_daughter2 if VV_junc6__bc2_is_out == 1 else VV_junc6__H_to2)
    VV_junc6__H_from3_target = (VV_junc6__H_daughter3 if VV_junc6__bc3_is_out == 1 else PV11__H_L_out)
    VV_junc6__H_from4_target = (VV_junc6__H_daughter4 if VV_junc6__bc4_is_out == 1 else PV12__H_L_out)
    VV_junc7__FQE_alpha = 1/(1+np.exp(-(VV_junc7__A+VV_junc7__B*VV_junc7__ph)))
    VV_junc7__H_VV_out_alpha = VV_junc7__H_mean*VV_junc7__FQE_alpha/(VV_junc7__FQB_alpha+VV_junc7__div_0)
    VV_junc7__H_VV_out_beta = VV_junc7__H_mean*(1-VV_junc7__FQE_alpha)/(1-VV_junc7__FQB_alpha+VV_junc7__div_0)
    VV_junc7__H_split1 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha1 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta1 == 1 else V6__H_R_out))
    VV_junc7__H_split2 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha2 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta2 == 1 else VV_junc7__H_to2))
    VV_junc7__H_split3 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha3 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta3 == 1 else PV13__H_L_out))
    VV_junc7__H_split4 = (VV_junc7__H_VV_out_alpha if VV_junc7__alpha4 == 1 else (VV_junc7__H_VV_out_beta if VV_junc7__beta4 == 1 else PV14__H_L_out))
    VV_junc7__H_daughter1 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split1 if VV_junc7__is_split == 1 else V6__H_R_out))
    VV_junc7__H_daughter2 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split2 if VV_junc7__is_split == 1 else VV_junc7__H_to2))
    VV_junc7__H_daughter3 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split3 if VV_junc7__is_split == 1 else PV13__H_L_out))
    VV_junc7__H_daughter4 = (VV_junc7__H_mean if VV_junc7__is_merge == 1 else (VV_junc7__H_split4 if VV_junc7__is_split == 1 else PV14__H_L_out))
    VV_junc7__H_from1_target = (VV_junc7__H_daughter1 if VV_junc7__bc1_is_out == 1 else V6__H_R_out)
    VV_junc7__H_from2_target = (VV_junc7__H_daughter2 if VV_junc7__bc2_is_out == 1 else VV_junc7__H_to2)
    VV_junc7__H_from3_target = (VV_junc7__H_daughter3 if VV_junc7__bc3_is_out == 1 else PV13__H_L_out)
    VV_junc7__H_from4_target = (VV_junc7__H_daughter4 if VV_junc7__bc4_is_out == 1 else PV14__H_L_out)
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
    VV_junc4__H_from1 = VV_junc4__w_out1*VV_junc4__H_from1_target
    VV_junc4__H_from2 = VV_junc4__w_out2*VV_junc4__H_from2_target
    VV_junc4__H_from3 = VV_junc4__w_out3*VV_junc4__H_from3_target
    VV_junc4__H_from4 = VV_junc4__w_out4*VV_junc4__H_from4_target
    VV_junc4__RBC_out = VV_junc4__Qout1*VV_junc4__H_from1+VV_junc4__Qout2*VV_junc4__H_from2+VV_junc4__Qout3*VV_junc4__H_from3+VV_junc4__Qout4*VV_junc4__H_from4
    VV_junc5__H_from1 = VV_junc5__w_out1*VV_junc5__H_from1_target
    VV_junc5__H_from2 = VV_junc5__w_out2*VV_junc5__H_from2_target
    VV_junc5__H_from3 = VV_junc5__w_out3*VV_junc5__H_from3_target
    VV_junc5__H_from4 = VV_junc5__w_out4*VV_junc5__H_from4_target
    VV_junc5__RBC_out = VV_junc5__Qout1*VV_junc5__H_from1+VV_junc5__Qout2*VV_junc5__H_from2+VV_junc5__Qout3*VV_junc5__H_from3+VV_junc5__Qout4*VV_junc5__H_from4
    VV_junc6__H_from1 = VV_junc6__w_out1*VV_junc6__H_from1_target
    VV_junc6__H_from2 = VV_junc6__w_out2*VV_junc6__H_from2_target
    VV_junc6__H_from3 = VV_junc6__w_out3*VV_junc6__H_from3_target
    VV_junc6__H_from4 = VV_junc6__w_out4*VV_junc6__H_from4_target
    VV_junc6__RBC_out = VV_junc6__Qout1*VV_junc6__H_from1+VV_junc6__Qout2*VV_junc6__H_from2+VV_junc6__Qout3*VV_junc6__H_from3+VV_junc6__Qout4*VV_junc6__H_from4
    VV_junc7__H_from1 = VV_junc7__w_out1*VV_junc7__H_from1_target
    VV_junc7__H_from2 = VV_junc7__w_out2*VV_junc7__H_from2_target
    VV_junc7__H_from3 = VV_junc7__w_out3*VV_junc7__H_from3_target
    VV_junc7__H_from4 = VV_junc7__w_out4*VV_junc7__H_from4_target
    VV_junc7__RBC_out = VV_junc7__Qout1*VV_junc7__H_from1+VV_junc7__Qout2*VV_junc7__H_from2+VV_junc7__Qout3*VV_junc7__H_from3+VV_junc7__Qout4*VV_junc7__H_from4

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
        "VV_junc4__vj2": VV_junc4__vj2,
        "VV_junc4__D1": VV_junc4__D1,
        "VV_junc4__D2": VV_junc4__D2,
        "VV_junc4__D3": VV_junc4__D3,
        "VV_junc4__D4": VV_junc4__D4,
        "VV_junc4__w_in2": VV_junc4__w_in2,
        "VV_junc4__w_out2": VV_junc4__w_out2,
        "VV_junc4__Qin2": VV_junc4__Qin2,
        "VV_junc4__Qout2": VV_junc4__Qout2,
        "VV_junc4__q_us": VV_junc4__q_us,
        "VV_junc4__q": VV_junc4__q,
        "VV_junc4__bc2_is_in": VV_junc4__bc2_is_in,
        "VV_junc4__bc2_is_out": VV_junc4__bc2_is_out,
        "VV_junc4__C_max12": VV_junc4__C_max12,
        "PV7__R_constriction": PV7__R_constriction,
        "PV7__H_L_in": PV7__H_L_in,
        "PV7__H_R_in": PV7__H_R_in,
        "PV7__q_us": PV7__q_us,
        "PV7__q": PV7__q,
        "PV7__C": PV7__C,
        "PV7__Z": PV7__Z,
        "PV7__mu_45": PV7__mu_45,
        "PV7__u": PV7__u,
        "PV8__R_constriction": PV8__R_constriction,
        "PV8__H_L_in": PV8__H_L_in,
        "PV8__H_R_in": PV8__H_R_in,
        "PV8__q_us": PV8__q_us,
        "PV8__q": PV8__q,
        "PV8__C": PV8__C,
        "PV8__Z": PV8__Z,
        "PV8__mu_45": PV8__mu_45,
        "PV8__u": PV8__u,
        "V7__H_L_in": V7__H_L_in,
        "V7__H_R_in": V7__H_R_in,
        "V7__q_us": V7__q_us,
        "V7__q": V7__q,
        "V7__C": V7__C,
        "V7__Z": V7__Z,
        "V7__mu_45": V7__mu_45,
        "V7__u": V7__u,
        "V8__H_L_in": V8__H_L_in,
        "V8__H_R_in": V8__H_R_in,
        "V8__q_us": V8__q_us,
        "V8__q": V8__q,
        "V8__C": V8__C,
        "V8__Z": V8__Z,
        "V8__mu_45": V8__mu_45,
        "V8__u": V8__u,
        "VV_junc5__vj2": VV_junc5__vj2,
        "VV_junc5__D1": VV_junc5__D1,
        "VV_junc5__D2": VV_junc5__D2,
        "VV_junc5__D3": VV_junc5__D3,
        "VV_junc5__D4": VV_junc5__D4,
        "VV_junc5__w_in2": VV_junc5__w_in2,
        "VV_junc5__w_out2": VV_junc5__w_out2,
        "VV_junc5__Qin2": VV_junc5__Qin2,
        "VV_junc5__Qout2": VV_junc5__Qout2,
        "VV_junc5__q_us": VV_junc5__q_us,
        "VV_junc5__q": VV_junc5__q,
        "VV_junc5__bc2_is_in": VV_junc5__bc2_is_in,
        "VV_junc5__bc2_is_out": VV_junc5__bc2_is_out,
        "VV_junc5__C_max12": VV_junc5__C_max12,
        "PV9__R_constriction": PV9__R_constriction,
        "PV9__H_L_in": PV9__H_L_in,
        "PV9__H_R_in": PV9__H_R_in,
        "PV9__q_us": PV9__q_us,
        "PV9__q": PV9__q,
        "PV9__C": PV9__C,
        "PV9__Z": PV9__Z,
        "PV9__mu_45": PV9__mu_45,
        "PV9__u": PV9__u,
        "PV10__R_constriction": PV10__R_constriction,
        "PV10__H_L_in": PV10__H_L_in,
        "PV10__H_R_in": PV10__H_R_in,
        "PV10__q_us": PV10__q_us,
        "PV10__q": PV10__q,
        "PV10__C": PV10__C,
        "PV10__Z": PV10__Z,
        "PV10__mu_45": PV10__mu_45,
        "PV10__u": PV10__u,
        "V9__H_L_in": V9__H_L_in,
        "V9__H_R_in": V9__H_R_in,
        "V9__q_us": V9__q_us,
        "V9__q": V9__q,
        "V9__C": V9__C,
        "V9__Z": V9__Z,
        "V9__mu_45": V9__mu_45,
        "V9__u": V9__u,
        "V10__H_L_in": V10__H_L_in,
        "V10__H_R_in": V10__H_R_in,
        "V10__q_us": V10__q_us,
        "V10__q": V10__q,
        "V10__C": V10__C,
        "V10__Z": V10__Z,
        "V10__mu_45": V10__mu_45,
        "V10__u": V10__u,
        "VV_junc6__vj2": VV_junc6__vj2,
        "VV_junc6__D1": VV_junc6__D1,
        "VV_junc6__D2": VV_junc6__D2,
        "VV_junc6__D3": VV_junc6__D3,
        "VV_junc6__D4": VV_junc6__D4,
        "VV_junc6__w_in2": VV_junc6__w_in2,
        "VV_junc6__w_out2": VV_junc6__w_out2,
        "VV_junc6__Qin2": VV_junc6__Qin2,
        "VV_junc6__Qout2": VV_junc6__Qout2,
        "VV_junc6__q_us": VV_junc6__q_us,
        "VV_junc6__q": VV_junc6__q,
        "VV_junc6__bc2_is_in": VV_junc6__bc2_is_in,
        "VV_junc6__bc2_is_out": VV_junc6__bc2_is_out,
        "VV_junc6__C_max12": VV_junc6__C_max12,
        "PV11__R_constriction": PV11__R_constriction,
        "PV11__H_L_in": PV11__H_L_in,
        "PV11__H_R_in": PV11__H_R_in,
        "PV11__q_us": PV11__q_us,
        "PV11__q": PV11__q,
        "PV11__C": PV11__C,
        "PV11__Z": PV11__Z,
        "PV11__mu_45": PV11__mu_45,
        "PV11__u": PV11__u,
        "PV12__R_constriction": PV12__R_constriction,
        "PV12__H_L_in": PV12__H_L_in,
        "PV12__H_R_in": PV12__H_R_in,
        "PV12__q_us": PV12__q_us,
        "PV12__q": PV12__q,
        "PV12__C": PV12__C,
        "PV12__Z": PV12__Z,
        "PV12__mu_45": PV12__mu_45,
        "PV12__u": PV12__u,
        "V11__H_L_in": V11__H_L_in,
        "V11__H_R_in": V11__H_R_in,
        "V11__q_us": V11__q_us,
        "V11__q": V11__q,
        "V11__C": V11__C,
        "V11__Z": V11__Z,
        "V11__mu_45": V11__mu_45,
        "V11__u": V11__u,
        "V12__H_L_in": V12__H_L_in,
        "V12__H_R_in": V12__H_R_in,
        "V12__q_us": V12__q_us,
        "V12__q": V12__q,
        "V12__C": V12__C,
        "V12__Z": V12__Z,
        "V12__mu_45": V12__mu_45,
        "V12__u": V12__u,
        "VV_junc7__vj2": VV_junc7__vj2,
        "VV_junc7__D1": VV_junc7__D1,
        "VV_junc7__D2": VV_junc7__D2,
        "VV_junc7__D3": VV_junc7__D3,
        "VV_junc7__D4": VV_junc7__D4,
        "VV_junc7__w_in2": VV_junc7__w_in2,
        "VV_junc7__w_out2": VV_junc7__w_out2,
        "VV_junc7__Qin2": VV_junc7__Qin2,
        "VV_junc7__Qout2": VV_junc7__Qout2,
        "VV_junc7__q_us": VV_junc7__q_us,
        "VV_junc7__q": VV_junc7__q,
        "VV_junc7__bc2_is_in": VV_junc7__bc2_is_in,
        "VV_junc7__bc2_is_out": VV_junc7__bc2_is_out,
        "VV_junc7__C_max12": VV_junc7__C_max12,
        "PV13__R_constriction": PV13__R_constriction,
        "PV13__H_L_in": PV13__H_L_in,
        "PV13__H_R_in": PV13__H_R_in,
        "PV13__q_us": PV13__q_us,
        "PV13__q": PV13__q,
        "PV13__C": PV13__C,
        "PV13__Z": PV13__Z,
        "PV13__mu_45": PV13__mu_45,
        "PV13__u": PV13__u,
        "PV14__R_constriction": PV14__R_constriction,
        "PV14__H_L_in": PV14__H_L_in,
        "PV14__H_R_in": PV14__H_R_in,
        "PV14__q_us": PV14__q_us,
        "PV14__q": PV14__q,
        "PV14__C": PV14__C,
        "PV14__Z": PV14__Z,
        "PV14__mu_45": PV14__mu_45,
        "PV14__u": PV14__u,
        "V13__H_L_in": V13__H_L_in,
        "V13__H_R_in": V13__H_R_in,
        "V13__q_us": V13__q_us,
        "V13__q": V13__q,
        "V13__C": V13__C,
        "V13__Z": V13__Z,
        "V13__mu_45": V13__mu_45,
        "V13__u": V13__u,
        "V14__H_L_in": V14__H_L_in,
        "V14__H_R_in": V14__H_R_in,
        "V14__q_us": V14__q_us,
        "V14__q": V14__q,
        "V14__C": V14__C,
        "V14__Z": V14__Z,
        "V14__mu_45": V14__mu_45,
        "V14__u": V14__u,
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
        "VV_junc4__RBC_volume_init": VV_junc4__RBC_volume_init,
        "VV_junc4__H_mean": VV_junc4__H_mean,
        "VV_junc4__C_max123": VV_junc4__C_max123,
        "VV_junc4__C": VV_junc4__C,
        "PV7__RBC_volume_init": PV7__RBC_volume_init,
        "PV7__H_mean": PV7__H_mean,
        "PV7__hem_dep_u_rel": PV7__hem_dep_u_rel,
        "PV7__u_mmHg": PV7__u_mmHg,
        "PV8__RBC_volume_init": PV8__RBC_volume_init,
        "PV8__H_mean": PV8__H_mean,
        "PV8__hem_dep_u_rel": PV8__hem_dep_u_rel,
        "PV8__u_mmHg": PV8__u_mmHg,
        "V7__RBC_volume_init": V7__RBC_volume_init,
        "V7__H_mean": V7__H_mean,
        "V7__hem_dep_u_rel": V7__hem_dep_u_rel,
        "V7__u_mmHg": V7__u_mmHg,
        "V8__RBC_volume_init": V8__RBC_volume_init,
        "V8__H_mean": V8__H_mean,
        "V8__hem_dep_u_rel": V8__hem_dep_u_rel,
        "V8__u_mmHg": V8__u_mmHg,
        "VV_junc5__RBC_volume_init": VV_junc5__RBC_volume_init,
        "VV_junc5__H_mean": VV_junc5__H_mean,
        "VV_junc5__C_max123": VV_junc5__C_max123,
        "VV_junc5__C": VV_junc5__C,
        "PV9__RBC_volume_init": PV9__RBC_volume_init,
        "PV9__H_mean": PV9__H_mean,
        "PV9__hem_dep_u_rel": PV9__hem_dep_u_rel,
        "PV9__u_mmHg": PV9__u_mmHg,
        "PV10__RBC_volume_init": PV10__RBC_volume_init,
        "PV10__H_mean": PV10__H_mean,
        "PV10__hem_dep_u_rel": PV10__hem_dep_u_rel,
        "PV10__u_mmHg": PV10__u_mmHg,
        "V9__RBC_volume_init": V9__RBC_volume_init,
        "V9__H_mean": V9__H_mean,
        "V9__hem_dep_u_rel": V9__hem_dep_u_rel,
        "V9__u_mmHg": V9__u_mmHg,
        "V10__RBC_volume_init": V10__RBC_volume_init,
        "V10__H_mean": V10__H_mean,
        "V10__hem_dep_u_rel": V10__hem_dep_u_rel,
        "V10__u_mmHg": V10__u_mmHg,
        "VV_junc6__RBC_volume_init": VV_junc6__RBC_volume_init,
        "VV_junc6__H_mean": VV_junc6__H_mean,
        "VV_junc6__C_max123": VV_junc6__C_max123,
        "VV_junc6__C": VV_junc6__C,
        "PV11__RBC_volume_init": PV11__RBC_volume_init,
        "PV11__H_mean": PV11__H_mean,
        "PV11__hem_dep_u_rel": PV11__hem_dep_u_rel,
        "PV11__u_mmHg": PV11__u_mmHg,
        "PV12__RBC_volume_init": PV12__RBC_volume_init,
        "PV12__H_mean": PV12__H_mean,
        "PV12__hem_dep_u_rel": PV12__hem_dep_u_rel,
        "PV12__u_mmHg": PV12__u_mmHg,
        "V11__RBC_volume_init": V11__RBC_volume_init,
        "V11__H_mean": V11__H_mean,
        "V11__hem_dep_u_rel": V11__hem_dep_u_rel,
        "V11__u_mmHg": V11__u_mmHg,
        "V12__RBC_volume_init": V12__RBC_volume_init,
        "V12__H_mean": V12__H_mean,
        "V12__hem_dep_u_rel": V12__hem_dep_u_rel,
        "V12__u_mmHg": V12__u_mmHg,
        "VV_junc7__RBC_volume_init": VV_junc7__RBC_volume_init,
        "VV_junc7__H_mean": VV_junc7__H_mean,
        "VV_junc7__C_max123": VV_junc7__C_max123,
        "VV_junc7__C": VV_junc7__C,
        "PV13__RBC_volume_init": PV13__RBC_volume_init,
        "PV13__H_mean": PV13__H_mean,
        "PV13__hem_dep_u_rel": PV13__hem_dep_u_rel,
        "PV13__u_mmHg": PV13__u_mmHg,
        "PV14__RBC_volume_init": PV14__RBC_volume_init,
        "PV14__H_mean": PV14__H_mean,
        "PV14__hem_dep_u_rel": PV14__hem_dep_u_rel,
        "PV14__u_mmHg": PV14__u_mmHg,
        "V13__RBC_volume_init": V13__RBC_volume_init,
        "V13__H_mean": V13__H_mean,
        "V13__hem_dep_u_rel": V13__hem_dep_u_rel,
        "V13__u_mmHg": V13__u_mmHg,
        "V14__RBC_volume_init": V14__RBC_volume_init,
        "V14__H_mean": V14__H_mean,
        "V14__hem_dep_u_rel": V14__hem_dep_u_rel,
        "V14__u_mmHg": V14__u_mmHg,
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
        "V4__mu": V4__mu,
        "V4__R": V4__R,
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
        "V6__mu": V6__mu,
        "V6__R": V6__R,
        "VV_junc4__u": VV_junc4__u,
        "VV_junc4__u_mmHg": VV_junc4__u_mmHg,
        "VV_junc4__u_d": VV_junc4__u_d,
        "VV_junc4__u_d_mmHg": VV_junc4__u_d_mmHg,
        "PV7__mu": PV7__mu,
        "PV7__R": PV7__R,
        "PV7__v": PV7__v,
        "PV7__v_d": PV7__v_d,
        "PV8__mu": PV8__mu,
        "PV8__R": PV8__R,
        "PV8__v": PV8__v,
        "PV8__v_d": PV8__v_d,
        "V7__mu": V7__mu,
        "V7__R": V7__R,
        "V7__v": V7__v,
        "V8__mu": V8__mu,
        "V8__R": V8__R,
        "V8__v": V8__v,
        "VV_junc5__u": VV_junc5__u,
        "VV_junc5__u_mmHg": VV_junc5__u_mmHg,
        "VV_junc5__u_d": VV_junc5__u_d,
        "VV_junc5__u_d_mmHg": VV_junc5__u_d_mmHg,
        "PV9__mu": PV9__mu,
        "PV9__R": PV9__R,
        "PV9__v": PV9__v,
        "PV9__v_d": PV9__v_d,
        "PV10__mu": PV10__mu,
        "PV10__R": PV10__R,
        "PV10__v": PV10__v,
        "PV10__v_d": PV10__v_d,
        "V9__mu": V9__mu,
        "V9__R": V9__R,
        "V9__v": V9__v,
        "V10__mu": V10__mu,
        "V10__R": V10__R,
        "V10__v": V10__v,
        "VV_junc6__u": VV_junc6__u,
        "VV_junc6__u_mmHg": VV_junc6__u_mmHg,
        "VV_junc6__u_d": VV_junc6__u_d,
        "VV_junc6__u_d_mmHg": VV_junc6__u_d_mmHg,
        "PV11__mu": PV11__mu,
        "PV11__R": PV11__R,
        "PV11__v": PV11__v,
        "PV11__v_d": PV11__v_d,
        "PV12__mu": PV12__mu,
        "PV12__R": PV12__R,
        "PV12__v": PV12__v,
        "PV12__v_d": PV12__v_d,
        "V11__mu": V11__mu,
        "V11__R": V11__R,
        "V11__v": V11__v,
        "V12__mu": V12__mu,
        "V12__R": V12__R,
        "V12__v": V12__v,
        "VV_junc7__u": VV_junc7__u,
        "VV_junc7__u_mmHg": VV_junc7__u_mmHg,
        "VV_junc7__u_d": VV_junc7__u_d,
        "VV_junc7__u_d_mmHg": VV_junc7__u_d_mmHg,
        "PV13__mu": PV13__mu,
        "PV13__R": PV13__R,
        "PV13__v": PV13__v,
        "PV13__v_d": PV13__v_d,
        "PV14__mu": PV14__mu,
        "PV14__R": PV14__R,
        "PV14__v": PV14__v,
        "PV14__v_d": PV14__v_d,
        "V13__mu": V13__mu,
        "V13__R": V13__R,
        "V13__v": V13__v,
        "V14__mu": V14__mu,
        "V14__R": V14__R,
        "V14__v": V14__v,
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
        "V3__v": V3__v,
        "V4__v": V4__v,
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
        "V5__v": V5__v,
        "V6__v": V6__v,
        "VV_junc4__vj1": VV_junc4__vj1,
        "VV_junc4__vj3": VV_junc4__vj3,
        "VV_junc4__vj4": VV_junc4__vj4,
        "VV_junc4__w_in1": VV_junc4__w_in1,
        "VV_junc4__w_in3": VV_junc4__w_in3,
        "VV_junc4__w_in4": VV_junc4__w_in4,
        "VV_junc4__w_out1": VV_junc4__w_out1,
        "VV_junc4__w_out3": VV_junc4__w_out3,
        "VV_junc4__w_out4": VV_junc4__w_out4,
        "VV_junc4__Qin1": VV_junc4__Qin1,
        "VV_junc4__Qin3": VV_junc4__Qin3,
        "VV_junc4__Qin4": VV_junc4__Qin4,
        "VV_junc4__Qout1": VV_junc4__Qout1,
        "VV_junc4__Qout3": VV_junc4__Qout3,
        "VV_junc4__Qout4": VV_junc4__Qout4,
        "VV_junc4__Qin_tot": VV_junc4__Qin_tot,
        "VV_junc4__Qout_tot": VV_junc4__Qout_tot,
        "VV_junc4__v": VV_junc4__v,
        "VV_junc4__bc1_is_in": VV_junc4__bc1_is_in,
        "VV_junc4__bc3_is_in": VV_junc4__bc3_is_in,
        "VV_junc4__bc4_is_in": VV_junc4__bc4_is_in,
        "VV_junc4__bc1_is_out": VV_junc4__bc1_is_out,
        "VV_junc4__bc3_is_out": VV_junc4__bc3_is_out,
        "VV_junc4__bc4_is_out": VV_junc4__bc4_is_out,
        "PV7__w_v": PV7__w_v,
        "PV7__w_v_d": PV7__w_v_d,
        "PV7__H_up": PV7__H_up,
        "PV7__s_v_d": PV7__s_v_d,
        "PV7__H_L_out": PV7__H_L_out,
        "PV7__H_R_out": PV7__H_R_out,
        "PV7__v_pos": PV7__v_pos,
        "PV7__v_neg": PV7__v_neg,
        "PV7__v_d_pos": PV7__v_d_pos,
        "PV7__v_d_neg": PV7__v_d_neg,
        "PV7__H_volume_L": PV7__H_volume_L,
        "PV7__H_volume_R": PV7__H_volume_R,
        "PV7__v_mm3_s": PV7__v_mm3_s,
        "PV7__v_d_mm3_s": PV7__v_d_mm3_s,
        "PV8__w_v": PV8__w_v,
        "PV8__w_v_d": PV8__w_v_d,
        "PV8__H_up": PV8__H_up,
        "PV8__s_v_d": PV8__s_v_d,
        "PV8__H_L_out": PV8__H_L_out,
        "PV8__H_R_out": PV8__H_R_out,
        "PV8__v_pos": PV8__v_pos,
        "PV8__v_neg": PV8__v_neg,
        "PV8__v_d_pos": PV8__v_d_pos,
        "PV8__v_d_neg": PV8__v_d_neg,
        "PV8__H_volume_L": PV8__H_volume_L,
        "PV8__H_volume_R": PV8__H_volume_R,
        "PV8__v_mm3_s": PV8__v_mm3_s,
        "PV8__v_d_mm3_s": PV8__v_d_mm3_s,
        "V7__w_v": V7__w_v,
        "V7__H_up": V7__H_up,
        "V7__s_v": V7__s_v,
        "V7__H_L_out": V7__H_L_out,
        "V7__H_R_out": V7__H_R_out,
        "V7__v_pos": V7__v_pos,
        "V7__v_neg": V7__v_neg,
        "V7__H_volume_L": V7__H_volume_L,
        "V7__H_volume_R": V7__H_volume_R,
        "V7__v_mm3_s": V7__v_mm3_s,
        "V8__w_v": V8__w_v,
        "V8__H_up": V8__H_up,
        "V8__s_v": V8__s_v,
        "V8__H_L_out": V8__H_L_out,
        "V8__H_R_out": V8__H_R_out,
        "V8__v_pos": V8__v_pos,
        "V8__v_neg": V8__v_neg,
        "V8__H_volume_L": V8__H_volume_L,
        "V8__H_volume_R": V8__H_volume_R,
        "V8__v_mm3_s": V8__v_mm3_s,
        "VV_junc5__vj1": VV_junc5__vj1,
        "VV_junc5__vj3": VV_junc5__vj3,
        "VV_junc5__vj4": VV_junc5__vj4,
        "VV_junc5__w_in1": VV_junc5__w_in1,
        "VV_junc5__w_in3": VV_junc5__w_in3,
        "VV_junc5__w_in4": VV_junc5__w_in4,
        "VV_junc5__w_out1": VV_junc5__w_out1,
        "VV_junc5__w_out3": VV_junc5__w_out3,
        "VV_junc5__w_out4": VV_junc5__w_out4,
        "VV_junc5__Qin1": VV_junc5__Qin1,
        "VV_junc5__Qin3": VV_junc5__Qin3,
        "VV_junc5__Qin4": VV_junc5__Qin4,
        "VV_junc5__Qout1": VV_junc5__Qout1,
        "VV_junc5__Qout3": VV_junc5__Qout3,
        "VV_junc5__Qout4": VV_junc5__Qout4,
        "VV_junc5__Qin_tot": VV_junc5__Qin_tot,
        "VV_junc5__Qout_tot": VV_junc5__Qout_tot,
        "VV_junc5__v": VV_junc5__v,
        "VV_junc5__bc1_is_in": VV_junc5__bc1_is_in,
        "VV_junc5__bc3_is_in": VV_junc5__bc3_is_in,
        "VV_junc5__bc4_is_in": VV_junc5__bc4_is_in,
        "VV_junc5__bc1_is_out": VV_junc5__bc1_is_out,
        "VV_junc5__bc3_is_out": VV_junc5__bc3_is_out,
        "VV_junc5__bc4_is_out": VV_junc5__bc4_is_out,
        "PV9__w_v": PV9__w_v,
        "PV9__w_v_d": PV9__w_v_d,
        "PV9__H_up": PV9__H_up,
        "PV9__s_v_d": PV9__s_v_d,
        "PV9__H_L_out": PV9__H_L_out,
        "PV9__H_R_out": PV9__H_R_out,
        "PV9__v_pos": PV9__v_pos,
        "PV9__v_neg": PV9__v_neg,
        "PV9__v_d_pos": PV9__v_d_pos,
        "PV9__v_d_neg": PV9__v_d_neg,
        "PV9__H_volume_L": PV9__H_volume_L,
        "PV9__H_volume_R": PV9__H_volume_R,
        "PV9__v_mm3_s": PV9__v_mm3_s,
        "PV9__v_d_mm3_s": PV9__v_d_mm3_s,
        "PV10__w_v": PV10__w_v,
        "PV10__w_v_d": PV10__w_v_d,
        "PV10__H_up": PV10__H_up,
        "PV10__s_v_d": PV10__s_v_d,
        "PV10__H_L_out": PV10__H_L_out,
        "PV10__H_R_out": PV10__H_R_out,
        "PV10__v_pos": PV10__v_pos,
        "PV10__v_neg": PV10__v_neg,
        "PV10__v_d_pos": PV10__v_d_pos,
        "PV10__v_d_neg": PV10__v_d_neg,
        "PV10__H_volume_L": PV10__H_volume_L,
        "PV10__H_volume_R": PV10__H_volume_R,
        "PV10__v_mm3_s": PV10__v_mm3_s,
        "PV10__v_d_mm3_s": PV10__v_d_mm3_s,
        "V9__w_v": V9__w_v,
        "V9__H_up": V9__H_up,
        "V9__s_v": V9__s_v,
        "V9__H_L_out": V9__H_L_out,
        "V9__H_R_out": V9__H_R_out,
        "V9__v_pos": V9__v_pos,
        "V9__v_neg": V9__v_neg,
        "V9__H_volume_L": V9__H_volume_L,
        "V9__H_volume_R": V9__H_volume_R,
        "V9__v_mm3_s": V9__v_mm3_s,
        "V10__w_v": V10__w_v,
        "V10__H_up": V10__H_up,
        "V10__s_v": V10__s_v,
        "V10__H_L_out": V10__H_L_out,
        "V10__H_R_out": V10__H_R_out,
        "V10__v_pos": V10__v_pos,
        "V10__v_neg": V10__v_neg,
        "V10__H_volume_L": V10__H_volume_L,
        "V10__H_volume_R": V10__H_volume_R,
        "V10__v_mm3_s": V10__v_mm3_s,
        "VV_junc6__vj1": VV_junc6__vj1,
        "VV_junc6__vj3": VV_junc6__vj3,
        "VV_junc6__vj4": VV_junc6__vj4,
        "VV_junc6__w_in1": VV_junc6__w_in1,
        "VV_junc6__w_in3": VV_junc6__w_in3,
        "VV_junc6__w_in4": VV_junc6__w_in4,
        "VV_junc6__w_out1": VV_junc6__w_out1,
        "VV_junc6__w_out3": VV_junc6__w_out3,
        "VV_junc6__w_out4": VV_junc6__w_out4,
        "VV_junc6__Qin1": VV_junc6__Qin1,
        "VV_junc6__Qin3": VV_junc6__Qin3,
        "VV_junc6__Qin4": VV_junc6__Qin4,
        "VV_junc6__Qout1": VV_junc6__Qout1,
        "VV_junc6__Qout3": VV_junc6__Qout3,
        "VV_junc6__Qout4": VV_junc6__Qout4,
        "VV_junc6__Qin_tot": VV_junc6__Qin_tot,
        "VV_junc6__Qout_tot": VV_junc6__Qout_tot,
        "VV_junc6__v": VV_junc6__v,
        "VV_junc6__bc1_is_in": VV_junc6__bc1_is_in,
        "VV_junc6__bc3_is_in": VV_junc6__bc3_is_in,
        "VV_junc6__bc4_is_in": VV_junc6__bc4_is_in,
        "VV_junc6__bc1_is_out": VV_junc6__bc1_is_out,
        "VV_junc6__bc3_is_out": VV_junc6__bc3_is_out,
        "VV_junc6__bc4_is_out": VV_junc6__bc4_is_out,
        "PV11__w_v": PV11__w_v,
        "PV11__w_v_d": PV11__w_v_d,
        "PV11__H_up": PV11__H_up,
        "PV11__s_v_d": PV11__s_v_d,
        "PV11__H_L_out": PV11__H_L_out,
        "PV11__H_R_out": PV11__H_R_out,
        "PV11__v_pos": PV11__v_pos,
        "PV11__v_neg": PV11__v_neg,
        "PV11__v_d_pos": PV11__v_d_pos,
        "PV11__v_d_neg": PV11__v_d_neg,
        "PV11__H_volume_L": PV11__H_volume_L,
        "PV11__H_volume_R": PV11__H_volume_R,
        "PV11__v_mm3_s": PV11__v_mm3_s,
        "PV11__v_d_mm3_s": PV11__v_d_mm3_s,
        "PV12__w_v": PV12__w_v,
        "PV12__w_v_d": PV12__w_v_d,
        "PV12__H_up": PV12__H_up,
        "PV12__s_v_d": PV12__s_v_d,
        "PV12__H_L_out": PV12__H_L_out,
        "PV12__H_R_out": PV12__H_R_out,
        "PV12__v_pos": PV12__v_pos,
        "PV12__v_neg": PV12__v_neg,
        "PV12__v_d_pos": PV12__v_d_pos,
        "PV12__v_d_neg": PV12__v_d_neg,
        "PV12__H_volume_L": PV12__H_volume_L,
        "PV12__H_volume_R": PV12__H_volume_R,
        "PV12__v_mm3_s": PV12__v_mm3_s,
        "PV12__v_d_mm3_s": PV12__v_d_mm3_s,
        "V11__w_v": V11__w_v,
        "V11__H_up": V11__H_up,
        "V11__s_v": V11__s_v,
        "V11__H_L_out": V11__H_L_out,
        "V11__H_R_out": V11__H_R_out,
        "V11__v_pos": V11__v_pos,
        "V11__v_neg": V11__v_neg,
        "V11__H_volume_L": V11__H_volume_L,
        "V11__H_volume_R": V11__H_volume_R,
        "V11__v_mm3_s": V11__v_mm3_s,
        "V12__w_v": V12__w_v,
        "V12__H_up": V12__H_up,
        "V12__s_v": V12__s_v,
        "V12__H_L_out": V12__H_L_out,
        "V12__H_R_out": V12__H_R_out,
        "V12__v_pos": V12__v_pos,
        "V12__v_neg": V12__v_neg,
        "V12__H_volume_L": V12__H_volume_L,
        "V12__H_volume_R": V12__H_volume_R,
        "V12__v_mm3_s": V12__v_mm3_s,
        "VV_junc7__vj1": VV_junc7__vj1,
        "VV_junc7__vj3": VV_junc7__vj3,
        "VV_junc7__vj4": VV_junc7__vj4,
        "VV_junc7__w_in1": VV_junc7__w_in1,
        "VV_junc7__w_in3": VV_junc7__w_in3,
        "VV_junc7__w_in4": VV_junc7__w_in4,
        "VV_junc7__w_out1": VV_junc7__w_out1,
        "VV_junc7__w_out3": VV_junc7__w_out3,
        "VV_junc7__w_out4": VV_junc7__w_out4,
        "VV_junc7__Qin1": VV_junc7__Qin1,
        "VV_junc7__Qin3": VV_junc7__Qin3,
        "VV_junc7__Qin4": VV_junc7__Qin4,
        "VV_junc7__Qout1": VV_junc7__Qout1,
        "VV_junc7__Qout3": VV_junc7__Qout3,
        "VV_junc7__Qout4": VV_junc7__Qout4,
        "VV_junc7__Qin_tot": VV_junc7__Qin_tot,
        "VV_junc7__Qout_tot": VV_junc7__Qout_tot,
        "VV_junc7__v": VV_junc7__v,
        "VV_junc7__bc1_is_in": VV_junc7__bc1_is_in,
        "VV_junc7__bc3_is_in": VV_junc7__bc3_is_in,
        "VV_junc7__bc4_is_in": VV_junc7__bc4_is_in,
        "VV_junc7__bc1_is_out": VV_junc7__bc1_is_out,
        "VV_junc7__bc3_is_out": VV_junc7__bc3_is_out,
        "VV_junc7__bc4_is_out": VV_junc7__bc4_is_out,
        "PV13__w_v": PV13__w_v,
        "PV13__w_v_d": PV13__w_v_d,
        "PV13__H_up": PV13__H_up,
        "PV13__s_v_d": PV13__s_v_d,
        "PV13__H_L_out": PV13__H_L_out,
        "PV13__H_R_out": PV13__H_R_out,
        "PV13__v_pos": PV13__v_pos,
        "PV13__v_neg": PV13__v_neg,
        "PV13__v_d_pos": PV13__v_d_pos,
        "PV13__v_d_neg": PV13__v_d_neg,
        "PV13__H_volume_L": PV13__H_volume_L,
        "PV13__H_volume_R": PV13__H_volume_R,
        "PV13__v_mm3_s": PV13__v_mm3_s,
        "PV13__v_d_mm3_s": PV13__v_d_mm3_s,
        "PV14__w_v": PV14__w_v,
        "PV14__w_v_d": PV14__w_v_d,
        "PV14__H_up": PV14__H_up,
        "PV14__s_v_d": PV14__s_v_d,
        "PV14__H_L_out": PV14__H_L_out,
        "PV14__H_R_out": PV14__H_R_out,
        "PV14__v_pos": PV14__v_pos,
        "PV14__v_neg": PV14__v_neg,
        "PV14__v_d_pos": PV14__v_d_pos,
        "PV14__v_d_neg": PV14__v_d_neg,
        "PV14__H_volume_L": PV14__H_volume_L,
        "PV14__H_volume_R": PV14__H_volume_R,
        "PV14__v_mm3_s": PV14__v_mm3_s,
        "PV14__v_d_mm3_s": PV14__v_d_mm3_s,
        "V13__w_v": V13__w_v,
        "V13__H_up": V13__H_up,
        "V13__s_v": V13__s_v,
        "V13__H_L_out": V13__H_L_out,
        "V13__H_R_out": V13__H_R_out,
        "V13__v_pos": V13__v_pos,
        "V13__v_neg": V13__v_neg,
        "V13__H_volume_L": V13__H_volume_L,
        "V13__H_volume_R": V13__H_volume_R,
        "V13__v_mm3_s": V13__v_mm3_s,
        "V14__w_v": V14__w_v,
        "V14__H_up": V14__H_up,
        "V14__s_v": V14__s_v,
        "V14__H_L_out": V14__H_L_out,
        "V14__H_R_out": V14__H_R_out,
        "V14__v_pos": V14__v_pos,
        "V14__v_neg": V14__v_neg,
        "V14__H_volume_L": V14__H_volume_L,
        "V14__H_volume_R": V14__H_volume_R,
        "V14__v_mm3_s": V14__v_mm3_s,
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
        "VV_junc4__n_in": VV_junc4__n_in,
        "VV_junc4__n_out": VV_junc4__n_out,
        "VV_junc4__RBC_in": VV_junc4__RBC_in,
        "VV_junc4__v_mm3_s": VV_junc4__v_mm3_s,
        "VV_junc4__junction_type": VV_junc4__junction_type,
        "VV_junc4__is_split": VV_junc4__is_split,
        "VV_junc4__is_merge": VV_junc4__is_merge,
        "VV_junc4__feed1": VV_junc4__feed1,
        "VV_junc4__feed2": VV_junc4__feed2,
        "VV_junc4__feed3": VV_junc4__feed3,
        "VV_junc4__feed4": VV_junc4__feed4,
        "VV_junc4__alpha1": VV_junc4__alpha1,
        "VV_junc4__alpha2": VV_junc4__alpha2,
        "VV_junc4__alpha3": VV_junc4__alpha3,
        "VV_junc4__alpha4": VV_junc4__alpha4,
        "VV_junc4__Qout1_rem": VV_junc4__Qout1_rem,
        "VV_junc4__Qout2_rem": VV_junc4__Qout2_rem,
        "VV_junc4__Qout3_rem": VV_junc4__Qout3_rem,
        "VV_junc4__Qout4_rem": VV_junc4__Qout4_rem,
        "VV_junc4__beta1": VV_junc4__beta1,
        "VV_junc4__beta2": VV_junc4__beta2,
        "VV_junc4__beta3": VV_junc4__beta3,
        "VV_junc4__beta4": VV_junc4__beta4,
        "VV_junc4__D_F": VV_junc4__D_F,
        "VV_junc4__D_alpha": VV_junc4__D_alpha,
        "VV_junc4__D_beta": VV_junc4__D_beta,
        "VV_junc4__v_alpha": VV_junc4__v_alpha,
        "VV_junc4__v_beta": VV_junc4__v_beta,
        "PV7__H_down_target": PV7__H_down_target,
        "PV8__H_down_target": PV8__H_down_target,
        "V7__H_down_target": V7__H_down_target,
        "V8__H_down_target": V8__H_down_target,
        "VV_junc5__n_in": VV_junc5__n_in,
        "VV_junc5__n_out": VV_junc5__n_out,
        "VV_junc5__RBC_in": VV_junc5__RBC_in,
        "VV_junc5__v_mm3_s": VV_junc5__v_mm3_s,
        "VV_junc5__junction_type": VV_junc5__junction_type,
        "VV_junc5__is_split": VV_junc5__is_split,
        "VV_junc5__is_merge": VV_junc5__is_merge,
        "VV_junc5__feed1": VV_junc5__feed1,
        "VV_junc5__feed2": VV_junc5__feed2,
        "VV_junc5__feed3": VV_junc5__feed3,
        "VV_junc5__feed4": VV_junc5__feed4,
        "VV_junc5__alpha1": VV_junc5__alpha1,
        "VV_junc5__alpha2": VV_junc5__alpha2,
        "VV_junc5__alpha3": VV_junc5__alpha3,
        "VV_junc5__alpha4": VV_junc5__alpha4,
        "VV_junc5__Qout1_rem": VV_junc5__Qout1_rem,
        "VV_junc5__Qout2_rem": VV_junc5__Qout2_rem,
        "VV_junc5__Qout3_rem": VV_junc5__Qout3_rem,
        "VV_junc5__Qout4_rem": VV_junc5__Qout4_rem,
        "VV_junc5__beta1": VV_junc5__beta1,
        "VV_junc5__beta2": VV_junc5__beta2,
        "VV_junc5__beta3": VV_junc5__beta3,
        "VV_junc5__beta4": VV_junc5__beta4,
        "VV_junc5__D_F": VV_junc5__D_F,
        "VV_junc5__D_alpha": VV_junc5__D_alpha,
        "VV_junc5__D_beta": VV_junc5__D_beta,
        "VV_junc5__v_alpha": VV_junc5__v_alpha,
        "VV_junc5__v_beta": VV_junc5__v_beta,
        "PV9__H_down_target": PV9__H_down_target,
        "PV10__H_down_target": PV10__H_down_target,
        "V9__H_down_target": V9__H_down_target,
        "V10__H_down_target": V10__H_down_target,
        "VV_junc6__n_in": VV_junc6__n_in,
        "VV_junc6__n_out": VV_junc6__n_out,
        "VV_junc6__RBC_in": VV_junc6__RBC_in,
        "VV_junc6__v_mm3_s": VV_junc6__v_mm3_s,
        "VV_junc6__junction_type": VV_junc6__junction_type,
        "VV_junc6__is_split": VV_junc6__is_split,
        "VV_junc6__is_merge": VV_junc6__is_merge,
        "VV_junc6__feed1": VV_junc6__feed1,
        "VV_junc6__feed2": VV_junc6__feed2,
        "VV_junc6__feed3": VV_junc6__feed3,
        "VV_junc6__feed4": VV_junc6__feed4,
        "VV_junc6__alpha1": VV_junc6__alpha1,
        "VV_junc6__alpha2": VV_junc6__alpha2,
        "VV_junc6__alpha3": VV_junc6__alpha3,
        "VV_junc6__alpha4": VV_junc6__alpha4,
        "VV_junc6__Qout1_rem": VV_junc6__Qout1_rem,
        "VV_junc6__Qout2_rem": VV_junc6__Qout2_rem,
        "VV_junc6__Qout3_rem": VV_junc6__Qout3_rem,
        "VV_junc6__Qout4_rem": VV_junc6__Qout4_rem,
        "VV_junc6__beta1": VV_junc6__beta1,
        "VV_junc6__beta2": VV_junc6__beta2,
        "VV_junc6__beta3": VV_junc6__beta3,
        "VV_junc6__beta4": VV_junc6__beta4,
        "VV_junc6__D_F": VV_junc6__D_F,
        "VV_junc6__D_alpha": VV_junc6__D_alpha,
        "VV_junc6__D_beta": VV_junc6__D_beta,
        "VV_junc6__v_alpha": VV_junc6__v_alpha,
        "VV_junc6__v_beta": VV_junc6__v_beta,
        "PV11__H_down_target": PV11__H_down_target,
        "PV12__H_down_target": PV12__H_down_target,
        "V11__H_down_target": V11__H_down_target,
        "V12__H_down_target": V12__H_down_target,
        "VV_junc7__n_in": VV_junc7__n_in,
        "VV_junc7__n_out": VV_junc7__n_out,
        "VV_junc7__RBC_in": VV_junc7__RBC_in,
        "VV_junc7__v_mm3_s": VV_junc7__v_mm3_s,
        "VV_junc7__junction_type": VV_junc7__junction_type,
        "VV_junc7__is_split": VV_junc7__is_split,
        "VV_junc7__is_merge": VV_junc7__is_merge,
        "VV_junc7__feed1": VV_junc7__feed1,
        "VV_junc7__feed2": VV_junc7__feed2,
        "VV_junc7__feed3": VV_junc7__feed3,
        "VV_junc7__feed4": VV_junc7__feed4,
        "VV_junc7__alpha1": VV_junc7__alpha1,
        "VV_junc7__alpha2": VV_junc7__alpha2,
        "VV_junc7__alpha3": VV_junc7__alpha3,
        "VV_junc7__alpha4": VV_junc7__alpha4,
        "VV_junc7__Qout1_rem": VV_junc7__Qout1_rem,
        "VV_junc7__Qout2_rem": VV_junc7__Qout2_rem,
        "VV_junc7__Qout3_rem": VV_junc7__Qout3_rem,
        "VV_junc7__Qout4_rem": VV_junc7__Qout4_rem,
        "VV_junc7__beta1": VV_junc7__beta1,
        "VV_junc7__beta2": VV_junc7__beta2,
        "VV_junc7__beta3": VV_junc7__beta3,
        "VV_junc7__beta4": VV_junc7__beta4,
        "VV_junc7__D_F": VV_junc7__D_F,
        "VV_junc7__D_alpha": VV_junc7__D_alpha,
        "VV_junc7__D_beta": VV_junc7__D_beta,
        "VV_junc7__v_alpha": VV_junc7__v_alpha,
        "VV_junc7__v_beta": VV_junc7__v_beta,
        "PV13__H_down_target": PV13__H_down_target,
        "PV14__H_down_target": PV14__H_down_target,
        "V13__H_down_target": V13__H_down_target,
        "V14__H_down_target": V14__H_down_target,
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
        "V3__H_down_target": V3__H_down_target,
        "V4__H_down_target": V4__H_down_target,
        "VV_junc3__FQB_alpha": VV_junc3__FQB_alpha,
        "VV_junc3__B": VV_junc3__B,
        "VV_junc3__A": VV_junc3__A,
        "VV_junc3__X_0": VV_junc3__X_0,
        "VV_junc3__y_raw": VV_junc3__y_raw,
        "VV_junc3__y": VV_junc3__y,
        "V5__H_down_target": V5__H_down_target,
        "V6__H_down_target": V6__H_down_target,
        "VV_junc4__FQB_alpha": VV_junc4__FQB_alpha,
        "VV_junc4__B": VV_junc4__B,
        "VV_junc4__A": VV_junc4__A,
        "VV_junc4__X_0": VV_junc4__X_0,
        "VV_junc4__y_raw": VV_junc4__y_raw,
        "VV_junc4__y": VV_junc4__y,
        "VV_junc5__FQB_alpha": VV_junc5__FQB_alpha,
        "VV_junc5__B": VV_junc5__B,
        "VV_junc5__A": VV_junc5__A,
        "VV_junc5__X_0": VV_junc5__X_0,
        "VV_junc5__y_raw": VV_junc5__y_raw,
        "VV_junc5__y": VV_junc5__y,
        "VV_junc6__FQB_alpha": VV_junc6__FQB_alpha,
        "VV_junc6__B": VV_junc6__B,
        "VV_junc6__A": VV_junc6__A,
        "VV_junc6__X_0": VV_junc6__X_0,
        "VV_junc6__y_raw": VV_junc6__y_raw,
        "VV_junc6__y": VV_junc6__y,
        "VV_junc7__FQB_alpha": VV_junc7__FQB_alpha,
        "VV_junc7__B": VV_junc7__B,
        "VV_junc7__A": VV_junc7__A,
        "VV_junc7__X_0": VV_junc7__X_0,
        "VV_junc7__y_raw": VV_junc7__y_raw,
        "VV_junc7__y": VV_junc7__y,
        "VV_junc1__ph": VV_junc1__ph,
        "VV_junc2__ph": VV_junc2__ph,
        "VV_junc3__ph": VV_junc3__ph,
        "VV_junc4__ph": VV_junc4__ph,
        "VV_junc5__ph": VV_junc5__ph,
        "VV_junc6__ph": VV_junc6__ph,
        "VV_junc7__ph": VV_junc7__ph,
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
        "VV_junc4__FQE_alpha": VV_junc4__FQE_alpha,
        "VV_junc4__H_VV_out_alpha": VV_junc4__H_VV_out_alpha,
        "VV_junc4__H_VV_out_beta": VV_junc4__H_VV_out_beta,
        "VV_junc4__H_split1": VV_junc4__H_split1,
        "VV_junc4__H_split2": VV_junc4__H_split2,
        "VV_junc4__H_split3": VV_junc4__H_split3,
        "VV_junc4__H_split4": VV_junc4__H_split4,
        "VV_junc4__H_daughter1": VV_junc4__H_daughter1,
        "VV_junc4__H_daughter2": VV_junc4__H_daughter2,
        "VV_junc4__H_daughter3": VV_junc4__H_daughter3,
        "VV_junc4__H_daughter4": VV_junc4__H_daughter4,
        "VV_junc4__H_from1_target": VV_junc4__H_from1_target,
        "VV_junc4__H_from2_target": VV_junc4__H_from2_target,
        "VV_junc4__H_from3_target": VV_junc4__H_from3_target,
        "VV_junc4__H_from4_target": VV_junc4__H_from4_target,
        "VV_junc5__FQE_alpha": VV_junc5__FQE_alpha,
        "VV_junc5__H_VV_out_alpha": VV_junc5__H_VV_out_alpha,
        "VV_junc5__H_VV_out_beta": VV_junc5__H_VV_out_beta,
        "VV_junc5__H_split1": VV_junc5__H_split1,
        "VV_junc5__H_split2": VV_junc5__H_split2,
        "VV_junc5__H_split3": VV_junc5__H_split3,
        "VV_junc5__H_split4": VV_junc5__H_split4,
        "VV_junc5__H_daughter1": VV_junc5__H_daughter1,
        "VV_junc5__H_daughter2": VV_junc5__H_daughter2,
        "VV_junc5__H_daughter3": VV_junc5__H_daughter3,
        "VV_junc5__H_daughter4": VV_junc5__H_daughter4,
        "VV_junc5__H_from1_target": VV_junc5__H_from1_target,
        "VV_junc5__H_from2_target": VV_junc5__H_from2_target,
        "VV_junc5__H_from3_target": VV_junc5__H_from3_target,
        "VV_junc5__H_from4_target": VV_junc5__H_from4_target,
        "VV_junc6__FQE_alpha": VV_junc6__FQE_alpha,
        "VV_junc6__H_VV_out_alpha": VV_junc6__H_VV_out_alpha,
        "VV_junc6__H_VV_out_beta": VV_junc6__H_VV_out_beta,
        "VV_junc6__H_split1": VV_junc6__H_split1,
        "VV_junc6__H_split2": VV_junc6__H_split2,
        "VV_junc6__H_split3": VV_junc6__H_split3,
        "VV_junc6__H_split4": VV_junc6__H_split4,
        "VV_junc6__H_daughter1": VV_junc6__H_daughter1,
        "VV_junc6__H_daughter2": VV_junc6__H_daughter2,
        "VV_junc6__H_daughter3": VV_junc6__H_daughter3,
        "VV_junc6__H_daughter4": VV_junc6__H_daughter4,
        "VV_junc6__H_from1_target": VV_junc6__H_from1_target,
        "VV_junc6__H_from2_target": VV_junc6__H_from2_target,
        "VV_junc6__H_from3_target": VV_junc6__H_from3_target,
        "VV_junc6__H_from4_target": VV_junc6__H_from4_target,
        "VV_junc7__FQE_alpha": VV_junc7__FQE_alpha,
        "VV_junc7__H_VV_out_alpha": VV_junc7__H_VV_out_alpha,
        "VV_junc7__H_VV_out_beta": VV_junc7__H_VV_out_beta,
        "VV_junc7__H_split1": VV_junc7__H_split1,
        "VV_junc7__H_split2": VV_junc7__H_split2,
        "VV_junc7__H_split3": VV_junc7__H_split3,
        "VV_junc7__H_split4": VV_junc7__H_split4,
        "VV_junc7__H_daughter1": VV_junc7__H_daughter1,
        "VV_junc7__H_daughter2": VV_junc7__H_daughter2,
        "VV_junc7__H_daughter3": VV_junc7__H_daughter3,
        "VV_junc7__H_daughter4": VV_junc7__H_daughter4,
        "VV_junc7__H_from1_target": VV_junc7__H_from1_target,
        "VV_junc7__H_from2_target": VV_junc7__H_from2_target,
        "VV_junc7__H_from3_target": VV_junc7__H_from3_target,
        "VV_junc7__H_from4_target": VV_junc7__H_from4_target,
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
        "VV_junc4__H_from1": VV_junc4__H_from1,
        "VV_junc4__H_from2": VV_junc4__H_from2,
        "VV_junc4__H_from3": VV_junc4__H_from3,
        "VV_junc4__H_from4": VV_junc4__H_from4,
        "VV_junc4__RBC_out": VV_junc4__RBC_out,
        "VV_junc5__H_from1": VV_junc5__H_from1,
        "VV_junc5__H_from2": VV_junc5__H_from2,
        "VV_junc5__H_from3": VV_junc5__H_from3,
        "VV_junc5__H_from4": VV_junc5__H_from4,
        "VV_junc5__RBC_out": VV_junc5__RBC_out,
        "VV_junc6__H_from1": VV_junc6__H_from1,
        "VV_junc6__H_from2": VV_junc6__H_from2,
        "VV_junc6__H_from3": VV_junc6__H_from3,
        "VV_junc6__H_from4": VV_junc6__H_from4,
        "VV_junc6__RBC_out": VV_junc6__RBC_out,
        "VV_junc7__H_from1": VV_junc7__H_from1,
        "VV_junc7__H_from2": VV_junc7__H_from2,
        "VV_junc7__H_from3": VV_junc7__H_from3,
        "VV_junc7__H_from4": VV_junc7__H_from4,
        "VV_junc7__RBC_out": VV_junc7__RBC_out,
    }