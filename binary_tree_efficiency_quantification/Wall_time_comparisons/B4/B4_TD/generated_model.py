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
PV15__H_global_L = 0.45
PV15__H_global_R = 0.45
PV15__R_constriction_base = 0.0
PV15__R_constriction_final = 0.0
PV15__gamma_mirror = 0.1
PV15__l = 0.000015
PV15__mu_plasma = 0.001
PV15__one_mm3 = 1e-09
PV15__q_C_init = 0.0
PV15__r = 4.5e-06
PV15__t0 = 500.0
PV15__tau_H_down = 0.001
PV15__tau_H_mean = 0.001
PV15__tau_link = 0.001
PV15__tau_sig = 1.0
PV15__u_ext = 133.0
PV15__v_eps = 1e-30
PV15__v_scale = 1e-50
PV16__H_global_L = 0.45
PV16__H_global_R = 0.45
PV16__R_constriction_base = 0.0
PV16__R_constriction_final = 0.0
PV16__gamma_mirror = 0.1
PV16__l = 0.000015
PV16__mu_plasma = 0.001
PV16__one_mm3 = 1e-09
PV16__q_C_init = 0.0
PV16__r = 4.5e-06
PV16__t0 = 500.0
PV16__tau_H_down = 0.001
PV16__tau_H_mean = 0.001
PV16__tau_link = 0.001
PV16__tau_sig = 1.0
PV16__u_ext = 133.0
PV16__v_eps = 1e-30
PV16__v_scale = 1e-50
PV17__H_global_L = 0.45
PV17__H_global_R = 0.45
PV17__R_constriction_base = 0.0
PV17__R_constriction_final = 0.0
PV17__gamma_mirror = 0.1
PV17__l = 0.000015
PV17__mu_plasma = 0.001
PV17__one_mm3 = 1e-09
PV17__q_C_init = 0.0
PV17__r = 4.5e-06
PV17__t0 = 500.0
PV17__tau_H_down = 0.001
PV17__tau_H_mean = 0.001
PV17__tau_link = 0.001
PV17__tau_sig = 1.0
PV17__u_ext = 133.0
PV17__v_eps = 1e-30
PV17__v_scale = 1e-50
PV18__H_global_L = 0.45
PV18__H_global_R = 0.45
PV18__R_constriction_base = 0.0
PV18__R_constriction_final = 0.0
PV18__gamma_mirror = 0.1
PV18__l = 0.000015
PV18__mu_plasma = 0.001
PV18__one_mm3 = 1e-09
PV18__q_C_init = 0.0
PV18__r = 4.5e-06
PV18__t0 = 500.0
PV18__tau_H_down = 0.001
PV18__tau_H_mean = 0.001
PV18__tau_link = 0.001
PV18__tau_sig = 1.0
PV18__u_ext = 133.0
PV18__v_eps = 1e-30
PV18__v_scale = 1e-50
PV19__H_global_L = 0.45
PV19__H_global_R = 0.45
PV19__R_constriction_base = 0.0
PV19__R_constriction_final = 0.0
PV19__gamma_mirror = 0.1
PV19__l = 0.000015
PV19__mu_plasma = 0.001
PV19__one_mm3 = 1e-09
PV19__q_C_init = 0.0
PV19__r = 4.5e-06
PV19__t0 = 500.0
PV19__tau_H_down = 0.001
PV19__tau_H_mean = 0.001
PV19__tau_link = 0.001
PV19__tau_sig = 1.0
PV19__u_ext = 133.0
PV19__v_eps = 1e-30
PV19__v_scale = 1e-50
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
PV20__H_global_L = 0.45
PV20__H_global_R = 0.45
PV20__R_constriction_base = 0.0
PV20__R_constriction_final = 0.0
PV20__gamma_mirror = 0.1
PV20__l = 0.000015
PV20__mu_plasma = 0.001
PV20__one_mm3 = 1e-09
PV20__q_C_init = 0.0
PV20__r = 4.5e-06
PV20__t0 = 500.0
PV20__tau_H_down = 0.001
PV20__tau_H_mean = 0.001
PV20__tau_link = 0.001
PV20__tau_sig = 1.0
PV20__u_ext = 133.0
PV20__v_eps = 1e-30
PV20__v_scale = 1e-50
PV21__H_global_L = 0.45
PV21__H_global_R = 0.45
PV21__R_constriction_base = 0.0
PV21__R_constriction_final = 0.0
PV21__gamma_mirror = 0.1
PV21__l = 0.000015
PV21__mu_plasma = 0.001
PV21__one_mm3 = 1e-09
PV21__q_C_init = 0.0
PV21__r = 4.5e-06
PV21__t0 = 500.0
PV21__tau_H_down = 0.001
PV21__tau_H_mean = 0.001
PV21__tau_link = 0.001
PV21__tau_sig = 1.0
PV21__u_ext = 133.0
PV21__v_eps = 1e-30
PV21__v_scale = 1e-50
PV22__H_global_L = 0.45
PV22__H_global_R = 0.45
PV22__R_constriction_base = 0.0
PV22__R_constriction_final = 0.0
PV22__gamma_mirror = 0.1
PV22__l = 0.000015
PV22__mu_plasma = 0.001
PV22__one_mm3 = 1e-09
PV22__q_C_init = 0.0
PV22__r = 4.5e-06
PV22__t0 = 500.0
PV22__tau_H_down = 0.001
PV22__tau_H_mean = 0.001
PV22__tau_link = 0.001
PV22__tau_sig = 1.0
PV22__u_ext = 133.0
PV22__v_eps = 1e-30
PV22__v_scale = 1e-50
PV23__H_global_L = 0.45
PV23__H_global_R = 0.45
PV23__R_constriction_base = 0.0
PV23__R_constriction_final = 0.0
PV23__gamma_mirror = 0.1
PV23__l = 0.000015
PV23__mu_plasma = 0.001
PV23__one_mm3 = 1e-09
PV23__q_C_init = 0.0
PV23__r = 4.5e-06
PV23__t0 = 500.0
PV23__tau_H_down = 0.001
PV23__tau_H_mean = 0.001
PV23__tau_link = 0.001
PV23__tau_sig = 1.0
PV23__u_ext = 133.0
PV23__v_eps = 1e-30
PV23__v_scale = 1e-50
PV24__H_global_L = 0.45
PV24__H_global_R = 0.45
PV24__R_constriction_base = 0.0
PV24__R_constriction_final = 0.0
PV24__gamma_mirror = 0.1
PV24__l = 0.000015
PV24__mu_plasma = 0.001
PV24__one_mm3 = 1e-09
PV24__q_C_init = 0.0
PV24__r = 4.5e-06
PV24__t0 = 500.0
PV24__tau_H_down = 0.001
PV24__tau_H_mean = 0.001
PV24__tau_link = 0.001
PV24__tau_sig = 1.0
PV24__u_ext = 133.0
PV24__v_eps = 1e-30
PV24__v_scale = 1e-50
PV25__H_global_L = 0.45
PV25__H_global_R = 0.45
PV25__R_constriction_base = 0.0
PV25__R_constriction_final = 0.0
PV25__gamma_mirror = 0.1
PV25__l = 0.000015
PV25__mu_plasma = 0.001
PV25__one_mm3 = 1e-09
PV25__q_C_init = 0.0
PV25__r = 4.5e-06
PV25__t0 = 500.0
PV25__tau_H_down = 0.001
PV25__tau_H_mean = 0.001
PV25__tau_link = 0.001
PV25__tau_sig = 1.0
PV25__u_ext = 133.0
PV25__v_eps = 1e-30
PV25__v_scale = 1e-50
PV26__H_global_L = 0.45
PV26__H_global_R = 0.45
PV26__R_constriction_base = 0.0
PV26__R_constriction_final = 0.0
PV26__gamma_mirror = 0.1
PV26__l = 0.000015
PV26__mu_plasma = 0.001
PV26__one_mm3 = 1e-09
PV26__q_C_init = 0.0
PV26__r = 4.5e-06
PV26__t0 = 500.0
PV26__tau_H_down = 0.001
PV26__tau_H_mean = 0.001
PV26__tau_link = 0.001
PV26__tau_sig = 1.0
PV26__u_ext = 133.0
PV26__v_eps = 1e-30
PV26__v_scale = 1e-50
PV27__H_global_L = 0.45
PV27__H_global_R = 0.45
PV27__R_constriction_base = 0.0
PV27__R_constriction_final = 0.0
PV27__gamma_mirror = 0.1
PV27__l = 0.000015
PV27__mu_plasma = 0.001
PV27__one_mm3 = 1e-09
PV27__q_C_init = 0.0
PV27__r = 4.5e-06
PV27__t0 = 500.0
PV27__tau_H_down = 0.001
PV27__tau_H_mean = 0.001
PV27__tau_link = 0.001
PV27__tau_sig = 1.0
PV27__u_ext = 133.0
PV27__v_eps = 1e-30
PV27__v_scale = 1e-50
PV28__H_global_L = 0.45
PV28__H_global_R = 0.45
PV28__R_constriction_base = 0.0
PV28__R_constriction_final = 0.0
PV28__gamma_mirror = 0.1
PV28__l = 0.000015
PV28__mu_plasma = 0.001
PV28__one_mm3 = 1e-09
PV28__q_C_init = 0.0
PV28__r = 4.5e-06
PV28__t0 = 500.0
PV28__tau_H_down = 0.001
PV28__tau_H_mean = 0.001
PV28__tau_link = 0.001
PV28__tau_sig = 1.0
PV28__u_ext = 133.0
PV28__v_eps = 1e-30
PV28__v_scale = 1e-50
PV29__H_global_L = 0.45
PV29__H_global_R = 0.45
PV29__R_constriction_base = 0.0
PV29__R_constriction_final = 0.0
PV29__gamma_mirror = 0.1
PV29__l = 0.000015
PV29__mu_plasma = 0.001
PV29__one_mm3 = 1e-09
PV29__q_C_init = 0.0
PV29__r = 4.5e-06
PV29__t0 = 500.0
PV29__tau_H_down = 0.001
PV29__tau_H_mean = 0.001
PV29__tau_link = 0.001
PV29__tau_sig = 1.0
PV29__u_ext = 133.0
PV29__v_eps = 1e-30
PV29__v_scale = 1e-50
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
PV30__H_global_L = 0.45
PV30__H_global_R = 0.45
PV30__R_constriction_base = 0.0
PV30__R_constriction_final = 0.0
PV30__gamma_mirror = 0.1
PV30__l = 0.000015
PV30__mu_plasma = 0.001
PV30__one_mm3 = 1e-09
PV30__q_C_init = 0.0
PV30__r = 4.5e-06
PV30__t0 = 500.0
PV30__tau_H_down = 0.001
PV30__tau_H_mean = 0.001
PV30__tau_link = 0.001
PV30__tau_sig = 1.0
PV30__u_ext = 133.0
PV30__v_eps = 1e-30
PV30__v_scale = 1e-50
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
PV7__R_constriction_final = 0.0
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
V10__v_eps = 1e-30
V10__v_scale = 1e-50
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
V11__v_eps = 1e-30
V11__v_scale = 1e-50
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
V12__v_eps = 1e-30
V12__v_scale = 1e-50
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
V13__v_eps = 1e-30
V13__v_scale = 1e-50
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
V14__v_eps = 1e-30
V14__v_scale = 1e-50
V15__H_L_out_RHS = 0.45
V15__H_global_L = 0.45
V15__H_global_R = 0.45
V15__gamma_mirror = 0.1
V15__l = 0.00001
V15__mu_plasma = 0.001
V15__one_mm3 = 1e-09
V15__q_C_init = 0.0
V15__r = 4e-06
V15__tau_H_down = 0.001
V15__tau_H_mean = 0.001
V15__tau_link = 0.001
V15__u_ext = 133.0
V15__u_out = 6532.778
V15__v_eps = 1e-30
V15__v_scale = 1e-50
V16__H_L_out_RHS = 0.45
V16__H_global_L = 0.45
V16__H_global_R = 0.45
V16__gamma_mirror = 0.1
V16__l = 0.00001
V16__mu_plasma = 0.001
V16__one_mm3 = 1e-09
V16__q_C_init = 0.0
V16__r = 4e-06
V16__tau_H_down = 0.001
V16__tau_H_mean = 0.001
V16__tau_link = 0.001
V16__u_ext = 133.0
V16__u_out = 6532.778
V16__v_eps = 1e-30
V16__v_scale = 1e-50
V17__H_L_out_RHS = 0.45
V17__H_global_L = 0.45
V17__H_global_R = 0.45
V17__gamma_mirror = 0.1
V17__l = 0.00001
V17__mu_plasma = 0.001
V17__one_mm3 = 1e-09
V17__q_C_init = 0.0
V17__r = 4e-06
V17__tau_H_down = 0.001
V17__tau_H_mean = 0.001
V17__tau_link = 0.001
V17__u_ext = 133.0
V17__u_out = 6532.778
V17__v_eps = 1e-30
V17__v_scale = 1e-50
V18__H_L_out_RHS = 0.45
V18__H_global_L = 0.45
V18__H_global_R = 0.45
V18__gamma_mirror = 0.1
V18__l = 0.00001
V18__mu_plasma = 0.001
V18__one_mm3 = 1e-09
V18__q_C_init = 0.0
V18__r = 4e-06
V18__tau_H_down = 0.001
V18__tau_H_mean = 0.001
V18__tau_link = 0.001
V18__u_ext = 133.0
V18__u_out = 6532.778
V18__v_eps = 1e-30
V18__v_scale = 1e-50
V19__H_L_out_RHS = 0.45
V19__H_global_L = 0.45
V19__H_global_R = 0.45
V19__gamma_mirror = 0.1
V19__l = 0.00001
V19__mu_plasma = 0.001
V19__one_mm3 = 1e-09
V19__q_C_init = 0.0
V19__r = 4e-06
V19__tau_H_down = 0.001
V19__tau_H_mean = 0.001
V19__tau_link = 0.001
V19__u_ext = 133.0
V19__u_out = 6532.778
V19__v_eps = 1e-30
V19__v_scale = 1e-50
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
V20__H_L_out_RHS = 0.45
V20__H_global_L = 0.45
V20__H_global_R = 0.45
V20__gamma_mirror = 0.1
V20__l = 0.00001
V20__mu_plasma = 0.001
V20__one_mm3 = 1e-09
V20__q_C_init = 0.0
V20__r = 4e-06
V20__tau_H_down = 0.001
V20__tau_H_mean = 0.001
V20__tau_link = 0.001
V20__u_ext = 133.0
V20__u_out = 6532.778
V20__v_eps = 1e-30
V20__v_scale = 1e-50
V21__H_L_out_RHS = 0.45
V21__H_global_L = 0.45
V21__H_global_R = 0.45
V21__gamma_mirror = 0.1
V21__l = 0.00001
V21__mu_plasma = 0.001
V21__one_mm3 = 1e-09
V21__q_C_init = 0.0
V21__r = 4e-06
V21__tau_H_down = 0.001
V21__tau_H_mean = 0.001
V21__tau_link = 0.001
V21__u_ext = 133.0
V21__u_out = 6532.778
V21__v_eps = 1e-30
V21__v_scale = 1e-50
V22__H_L_out_RHS = 0.45
V22__H_global_L = 0.45
V22__H_global_R = 0.45
V22__gamma_mirror = 0.1
V22__l = 0.00001
V22__mu_plasma = 0.001
V22__one_mm3 = 1e-09
V22__q_C_init = 0.0
V22__r = 4e-06
V22__tau_H_down = 0.001
V22__tau_H_mean = 0.001
V22__tau_link = 0.001
V22__u_ext = 133.0
V22__u_out = 6532.778
V22__v_eps = 1e-30
V22__v_scale = 1e-50
V23__H_L_out_RHS = 0.45
V23__H_global_L = 0.45
V23__H_global_R = 0.45
V23__gamma_mirror = 0.1
V23__l = 0.00001
V23__mu_plasma = 0.001
V23__one_mm3 = 1e-09
V23__q_C_init = 0.0
V23__r = 4e-06
V23__tau_H_down = 0.001
V23__tau_H_mean = 0.001
V23__tau_link = 0.001
V23__u_ext = 133.0
V23__u_out = 6532.778
V23__v_eps = 1e-30
V23__v_scale = 1e-50
V24__H_L_out_RHS = 0.45
V24__H_global_L = 0.45
V24__H_global_R = 0.45
V24__gamma_mirror = 0.1
V24__l = 0.00001
V24__mu_plasma = 0.001
V24__one_mm3 = 1e-09
V24__q_C_init = 0.0
V24__r = 4e-06
V24__tau_H_down = 0.001
V24__tau_H_mean = 0.001
V24__tau_link = 0.001
V24__u_ext = 133.0
V24__u_out = 6532.778
V24__v_eps = 1e-30
V24__v_scale = 1e-50
V25__H_L_out_RHS = 0.45
V25__H_global_L = 0.45
V25__H_global_R = 0.45
V25__gamma_mirror = 0.1
V25__l = 0.00001
V25__mu_plasma = 0.001
V25__one_mm3 = 1e-09
V25__q_C_init = 0.0
V25__r = 4e-06
V25__tau_H_down = 0.001
V25__tau_H_mean = 0.001
V25__tau_link = 0.001
V25__u_ext = 133.0
V25__u_out = 6532.778
V25__v_eps = 1e-30
V25__v_scale = 1e-50
V26__H_L_out_RHS = 0.45
V26__H_global_L = 0.45
V26__H_global_R = 0.45
V26__gamma_mirror = 0.1
V26__l = 0.00001
V26__mu_plasma = 0.001
V26__one_mm3 = 1e-09
V26__q_C_init = 0.0
V26__r = 4e-06
V26__tau_H_down = 0.001
V26__tau_H_mean = 0.001
V26__tau_link = 0.001
V26__u_ext = 133.0
V26__u_out = 6532.778
V26__v_eps = 1e-30
V26__v_scale = 1e-50
V27__H_L_out_RHS = 0.45
V27__H_global_L = 0.45
V27__H_global_R = 0.45
V27__gamma_mirror = 0.1
V27__l = 0.00001
V27__mu_plasma = 0.001
V27__one_mm3 = 1e-09
V27__q_C_init = 0.0
V27__r = 4e-06
V27__tau_H_down = 0.001
V27__tau_H_mean = 0.001
V27__tau_link = 0.001
V27__u_ext = 133.0
V27__u_out = 6532.778
V27__v_eps = 1e-30
V27__v_scale = 1e-50
V28__H_L_out_RHS = 0.45
V28__H_global_L = 0.45
V28__H_global_R = 0.45
V28__gamma_mirror = 0.1
V28__l = 0.00001
V28__mu_plasma = 0.001
V28__one_mm3 = 1e-09
V28__q_C_init = 0.0
V28__r = 4e-06
V28__tau_H_down = 0.001
V28__tau_H_mean = 0.001
V28__tau_link = 0.001
V28__u_ext = 133.0
V28__u_out = 6532.778
V28__v_eps = 1e-30
V28__v_scale = 1e-50
V29__H_L_out_RHS = 0.45
V29__H_global_L = 0.45
V29__H_global_R = 0.45
V29__gamma_mirror = 0.1
V29__l = 0.00001
V29__mu_plasma = 0.001
V29__one_mm3 = 1e-09
V29__q_C_init = 0.0
V29__r = 4e-06
V29__tau_H_down = 0.001
V29__tau_H_mean = 0.001
V29__tau_link = 0.001
V29__u_ext = 133.0
V29__u_out = 6532.778
V29__v_eps = 1e-30
V29__v_scale = 1e-50
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
V30__H_L_out_RHS = 0.45
V30__H_global_L = 0.45
V30__H_global_R = 0.45
V30__gamma_mirror = 0.1
V30__l = 0.00001
V30__mu_plasma = 0.001
V30__one_mm3 = 1e-09
V30__q_C_init = 0.0
V30__r = 4e-06
V30__tau_H_down = 0.001
V30__tau_H_mean = 0.001
V30__tau_link = 0.001
V30__u_ext = 133.0
V30__u_out = 6532.778
V30__v_eps = 1e-30
V30__v_scale = 1e-50
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
V7__v_eps = 1e-30
V7__v_scale = 1e-50
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
V8__v_eps = 1e-30
V8__v_scale = 1e-50
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
V9__v_eps = 1e-30
V9__v_scale = 1e-50
VV_junc10__C_conn2 = 8.51e-22
VV_junc10__H_global_L = 0.45
VV_junc10__H_global_R = 0.45
VV_junc10__H_to2 = 0.0
VV_junc10__R_VV_junc = 1000000000000000.0
VV_junc10__div_0 = 1e-25
VV_junc10__div_0y = 1e-08
VV_junc10__k = 1000.0
VV_junc10__l = 0.000001
VV_junc10__mu_plasma = 0.001
VV_junc10__one_mm3 = 1e-09
VV_junc10__q_C_init = 0.0
VV_junc10__r = 4.5e-06
VV_junc10__r_bc2 = 0.0
VV_junc10__u_ext = 133.0
VV_junc10__v_scale = 1e-50
VV_junc10__v_threshold = 1e-18
VV_junc10__vbc2 = 0.0
VV_junc11__C_conn2 = 8.51e-22
VV_junc11__H_global_L = 0.45
VV_junc11__H_global_R = 0.45
VV_junc11__H_to2 = 0.0
VV_junc11__R_VV_junc = 1000000000000000.0
VV_junc11__div_0 = 1e-25
VV_junc11__div_0y = 1e-08
VV_junc11__k = 1000.0
VV_junc11__l = 0.000001
VV_junc11__mu_plasma = 0.001
VV_junc11__one_mm3 = 1e-09
VV_junc11__q_C_init = 0.0
VV_junc11__r = 4.5e-06
VV_junc11__r_bc2 = 0.0
VV_junc11__u_ext = 133.0
VV_junc11__v_scale = 1e-50
VV_junc11__v_threshold = 1e-18
VV_junc11__vbc2 = 0.0
VV_junc12__C_conn2 = 8.51e-22
VV_junc12__H_global_L = 0.45
VV_junc12__H_global_R = 0.45
VV_junc12__H_to2 = 0.0
VV_junc12__R_VV_junc = 1000000000000000.0
VV_junc12__div_0 = 1e-25
VV_junc12__div_0y = 1e-08
VV_junc12__k = 1000.0
VV_junc12__l = 0.000001
VV_junc12__mu_plasma = 0.001
VV_junc12__one_mm3 = 1e-09
VV_junc12__q_C_init = 0.0
VV_junc12__r = 4.5e-06
VV_junc12__r_bc2 = 0.0
VV_junc12__u_ext = 133.0
VV_junc12__v_scale = 1e-50
VV_junc12__v_threshold = 1e-18
VV_junc12__vbc2 = 0.0
VV_junc13__C_conn2 = 8.51e-22
VV_junc13__H_global_L = 0.45
VV_junc13__H_global_R = 0.45
VV_junc13__H_to2 = 0.0
VV_junc13__R_VV_junc = 1000000000000000.0
VV_junc13__div_0 = 1e-25
VV_junc13__div_0y = 1e-08
VV_junc13__k = 1000.0
VV_junc13__l = 0.000001
VV_junc13__mu_plasma = 0.001
VV_junc13__one_mm3 = 1e-09
VV_junc13__q_C_init = 0.0
VV_junc13__r = 4.5e-06
VV_junc13__r_bc2 = 0.0
VV_junc13__u_ext = 133.0
VV_junc13__v_scale = 1e-50
VV_junc13__v_threshold = 1e-18
VV_junc13__vbc2 = 0.0
VV_junc14__C_conn2 = 8.51e-22
VV_junc14__H_global_L = 0.45
VV_junc14__H_global_R = 0.45
VV_junc14__H_to2 = 0.0
VV_junc14__R_VV_junc = 1000000000000000.0
VV_junc14__div_0 = 1e-25
VV_junc14__div_0y = 1e-08
VV_junc14__k = 1000.0
VV_junc14__l = 0.000001
VV_junc14__mu_plasma = 0.001
VV_junc14__one_mm3 = 1e-09
VV_junc14__q_C_init = 0.0
VV_junc14__r = 4.5e-06
VV_junc14__r_bc2 = 0.0
VV_junc14__u_ext = 133.0
VV_junc14__v_scale = 1e-50
VV_junc14__v_threshold = 1e-18
VV_junc14__vbc2 = 0.0
VV_junc15__C_conn2 = 8.51e-22
VV_junc15__H_global_L = 0.45
VV_junc15__H_global_R = 0.45
VV_junc15__H_to2 = 0.0
VV_junc15__R_VV_junc = 1000000000000000.0
VV_junc15__div_0 = 1e-25
VV_junc15__div_0y = 1e-08
VV_junc15__k = 1000.0
VV_junc15__l = 0.000001
VV_junc15__mu_plasma = 0.001
VV_junc15__one_mm3 = 1e-09
VV_junc15__q_C_init = 0.0
VV_junc15__r = 4.5e-06
VV_junc15__r_bc2 = 0.0
VV_junc15__u_ext = 133.0
VV_junc15__v_scale = 1e-50
VV_junc15__v_threshold = 1e-18
VV_junc15__vbc2 = 0.0
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
VV_junc8__C_conn2 = 8.51e-22
VV_junc8__H_global_L = 0.45
VV_junc8__H_global_R = 0.45
VV_junc8__H_to2 = 0.0
VV_junc8__R_VV_junc = 1000000000000000.0
VV_junc8__div_0 = 1e-25
VV_junc8__div_0y = 1e-08
VV_junc8__k = 1000.0
VV_junc8__l = 0.000001
VV_junc8__mu_plasma = 0.001
VV_junc8__one_mm3 = 1e-09
VV_junc8__q_C_init = 0.0
VV_junc8__r = 4.5e-06
VV_junc8__r_bc2 = 0.0
VV_junc8__u_ext = 133.0
VV_junc8__v_scale = 1e-50
VV_junc8__v_threshold = 1e-18
VV_junc8__vbc2 = 0.0
VV_junc9__C_conn2 = 8.51e-22
VV_junc9__H_global_L = 0.45
VV_junc9__H_global_R = 0.45
VV_junc9__H_to2 = 0.0
VV_junc9__R_VV_junc = 1000000000000000.0
VV_junc9__div_0 = 1e-25
VV_junc9__div_0y = 1e-08
VV_junc9__k = 1000.0
VV_junc9__l = 0.000001
VV_junc9__mu_plasma = 0.001
VV_junc9__one_mm3 = 1e-09
VV_junc9__q_C_init = 0.0
VV_junc9__r = 4.5e-06
VV_junc9__r_bc2 = 0.0
VV_junc9__u_ext = 133.0
VV_junc9__v_scale = 1e-50
VV_junc9__v_threshold = 1e-18
VV_junc9__vbc2 = 0.0
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
    'VV_junc8__RBC_volume',
    'VV_junc8__q_C',
    'VV_junc8__q_C_d',
    'PV15__H_link_R',
    'PV15__H_link_L',
    'PV15__H_down',
    'PV15__RBC_volume',
    'PV15__q_C',
    'PV16__H_link_R',
    'PV16__H_link_L',
    'PV16__H_down',
    'PV16__RBC_volume',
    'PV16__q_C',
    'V15__H_link_R',
    'V15__H_link_L',
    'V15__H_down',
    'V15__RBC_volume',
    'V15__q_C',
    'V16__H_link_R',
    'V16__H_link_L',
    'V16__H_down',
    'V16__RBC_volume',
    'V16__q_C',
    'VV_junc9__RBC_volume',
    'VV_junc9__q_C',
    'VV_junc9__q_C_d',
    'PV17__H_link_R',
    'PV17__H_link_L',
    'PV17__H_down',
    'PV17__RBC_volume',
    'PV17__q_C',
    'PV18__H_link_R',
    'PV18__H_link_L',
    'PV18__H_down',
    'PV18__RBC_volume',
    'PV18__q_C',
    'V17__H_link_R',
    'V17__H_link_L',
    'V17__H_down',
    'V17__RBC_volume',
    'V17__q_C',
    'V18__H_link_R',
    'V18__H_link_L',
    'V18__H_down',
    'V18__RBC_volume',
    'V18__q_C',
    'VV_junc10__RBC_volume',
    'VV_junc10__q_C',
    'VV_junc10__q_C_d',
    'PV19__H_link_R',
    'PV19__H_link_L',
    'PV19__H_down',
    'PV19__RBC_volume',
    'PV19__q_C',
    'PV20__H_link_R',
    'PV20__H_link_L',
    'PV20__H_down',
    'PV20__RBC_volume',
    'PV20__q_C',
    'V19__H_link_R',
    'V19__H_link_L',
    'V19__H_down',
    'V19__RBC_volume',
    'V19__q_C',
    'V20__H_link_R',
    'V20__H_link_L',
    'V20__H_down',
    'V20__RBC_volume',
    'V20__q_C',
    'VV_junc11__RBC_volume',
    'VV_junc11__q_C',
    'VV_junc11__q_C_d',
    'PV21__H_link_R',
    'PV21__H_link_L',
    'PV21__H_down',
    'PV21__RBC_volume',
    'PV21__q_C',
    'PV22__H_link_R',
    'PV22__H_link_L',
    'PV22__H_down',
    'PV22__RBC_volume',
    'PV22__q_C',
    'V21__H_link_R',
    'V21__H_link_L',
    'V21__H_down',
    'V21__RBC_volume',
    'V21__q_C',
    'V22__H_link_R',
    'V22__H_link_L',
    'V22__H_down',
    'V22__RBC_volume',
    'V22__q_C',
    'VV_junc12__RBC_volume',
    'VV_junc12__q_C',
    'VV_junc12__q_C_d',
    'PV23__H_link_R',
    'PV23__H_link_L',
    'PV23__H_down',
    'PV23__RBC_volume',
    'PV23__q_C',
    'PV24__H_link_R',
    'PV24__H_link_L',
    'PV24__H_down',
    'PV24__RBC_volume',
    'PV24__q_C',
    'V23__H_link_R',
    'V23__H_link_L',
    'V23__H_down',
    'V23__RBC_volume',
    'V23__q_C',
    'V24__H_link_R',
    'V24__H_link_L',
    'V24__H_down',
    'V24__RBC_volume',
    'V24__q_C',
    'VV_junc13__RBC_volume',
    'VV_junc13__q_C',
    'VV_junc13__q_C_d',
    'PV25__H_link_R',
    'PV25__H_link_L',
    'PV25__H_down',
    'PV25__RBC_volume',
    'PV25__q_C',
    'PV26__H_link_R',
    'PV26__H_link_L',
    'PV26__H_down',
    'PV26__RBC_volume',
    'PV26__q_C',
    'V25__H_link_R',
    'V25__H_link_L',
    'V25__H_down',
    'V25__RBC_volume',
    'V25__q_C',
    'V26__H_link_R',
    'V26__H_link_L',
    'V26__H_down',
    'V26__RBC_volume',
    'V26__q_C',
    'VV_junc14__RBC_volume',
    'VV_junc14__q_C',
    'VV_junc14__q_C_d',
    'PV27__H_link_R',
    'PV27__H_link_L',
    'PV27__H_down',
    'PV27__RBC_volume',
    'PV27__q_C',
    'PV28__H_link_R',
    'PV28__H_link_L',
    'PV28__H_down',
    'PV28__RBC_volume',
    'PV28__q_C',
    'V27__H_link_R',
    'V27__H_link_L',
    'V27__H_down',
    'V27__RBC_volume',
    'V27__q_C',
    'V28__H_link_R',
    'V28__H_link_L',
    'V28__H_down',
    'V28__RBC_volume',
    'V28__q_C',
    'VV_junc15__RBC_volume',
    'VV_junc15__q_C',
    'VV_junc15__q_C_d',
    'PV29__H_link_R',
    'PV29__H_link_L',
    'PV29__H_down',
    'PV29__RBC_volume',
    'PV29__q_C',
    'PV30__H_link_R',
    'PV30__H_link_L',
    'PV30__H_down',
    'PV30__RBC_volume',
    'PV30__q_C',
    'V29__H_link_R',
    'V29__H_link_L',
    'V29__H_down',
    'V29__RBC_volume',
    'V29__q_C',
    'V30__H_link_R',
    'V30__H_link_L',
    'V30__H_down',
    'V30__RBC_volume',
    'V30__q_C',
]

# Initial conditions
y0 = np.array([
    0.1655457647776386,
    0.45,
    0.44999999796711987,
    1.5269636830903878e-14,
    3.325870448338449e-18,
    5.2901001055264705e-17,
    2.7616709511665752e-18,
    2.7541436824103965e-18,
    0.4499634960003781,
    0.46192376185344425,
    0.44950208171288486,
    7.635461752398577e-16,
    1.6528307541479e-19,
    0.4499634905737863,
    0.4619242626263206,
    0.44950204068440186,
    7.635461815927457e-16,
    1.6528307541458152e-19,
    0.16554538069262895,
    0.4498464843820186,
    0.4500036450913047,
    1.0692471546992408e-14,
    2.754490790923632e-18,
    0.1655453805587889,
    0.449846466239972,
    0.45000364563794965,
    1.0692471547324324e-14,
    2.754490790918686e-18,
    4.501523160718711e-17,
    2.7422959008008252e-18,
    2.7385322664321122e-18,
    0.4500413386965926,
    0.4595599477418926,
    0.4499130115767971,
    6.415452363839733e-16,
    1.6434948869529687e-19,
    0.45004133999691287,
    0.4595597990684754,
    0.449913022007954,
    6.415452360303248e-16,
    1.643494886952948e-19,
    0.1728840422146208,
    0.4500749809350375,
    0.4499952162398607,
    7.069570308014228e-15,
    2.191189752664704e-18,
    0.17288404209699978,
    0.4500749851292954,
    0.4499952161225151,
    7.0695703086277285e-15,
    2.1911897526624583e-18,
    4.5015201280852384e-17,
    2.7422959008090774e-18,
    2.7385322664422642e-18,
    0.45004134087256653,
    0.4595596419838114,
    0.449913029714462,
    6.415452301860364e-16,
    1.643494886873376e-19,
    0.4500413379106554,
    0.45955982194307476,
    0.449913009134201,
    6.415452352678077e-16,
    1.6434948868758413e-19,
    0.17288404217266165,
    0.4500749885331944,
    0.44999521598625464,
    7.069570306112786e-15,
    2.191189752679202e-18,
    0.17288404213796835,
    0.4500749783524287,
    0.4499952163332208,
    7.069570308701218e-15,
    2.1911897526689756e-18,
    3.760316984225824e-17,
    2.731057560910528e-18,
    2.729175743732162e-18,
    0.45006478144046447,
    0.46021400903551113,
    0.45001211337595537,
    5.302118809191947e-16,
    1.6379016444726086e-19,
    0.45006480020419587,
    0.4602121513363472,
    0.45001227191674487,
    5.302118779691705e-16,
    1.6379016444731317e-19,
    0.17440839444403422,
    0.4501417913935532,
    0.4499921371594105,
    4.294903277043359e-15,
    1.6378213770825793e-18,
    0.1744083944522123,
    0.4501418585188839,
    0.44999213528278026,
    4.2949032770726995e-15,
    1.6378213770837828e-18,
    3.7603204544107674e-17,
    2.73105756084122e-18,
    2.7291757436450814e-18,
    0.4500648028979424,
    0.4602128446834922,
    0.4500122468159069,
    5.302118617935937e-16,
    1.6379016443791466e-19,
    0.45006477911146187,
    0.4602138162215531,
    0.45001211545865366,
    5.302118670698469e-16,
    1.637901644377183e-19,
    0.17440839429726687,
    0.4501418591808089,
    0.4499921350307213,
    4.294903277507554e-15,
    1.6378213770374906e-18,
    0.17440839430052774,
    0.4501417879906864,
    0.44999213739621696,
    4.294903277125747e-15,
    1.6378213770345023e-18,
    3.7603204055633625e-17,
    2.731057560997745e-18,
    2.7291757438408587e-18,
    0.4500648164470462,
    0.46018675465589864,
    0.45001321717322595,
    5.30211836582495e-16,
    1.637901644501512e-19,
    0.4500648040664037,
    0.4601998470348539,
    0.45001270701339174,
    5.302118507334687e-16,
    1.6379016444998648e-19,
    0.17440839448101522,
    0.45014202499480915,
    0.44999213353824513,
    4.294903273681258e-15,
    1.6378213771677586e-18,
    0.17440839446326165,
    0.4501419261114839,
    0.44999213484297856,
    4.29490327546812e-15,
    1.6378213771648048e-18,
    3.7603195757861033e-17,
    2.731057560796488e-18,
    2.7291757435865335e-18,
    0.45006478825772384,
    0.46021384160078854,
    0.4500121517618676,
    5.302118668129685e-16,
    1.6379016442829348e-19,
    0.45006479159072627,
    0.46021290772181433,
    0.4500121981862958,
    5.302118654859538e-16,
    1.637901644284138e-19,
    0.17440839443253636,
    0.4501418133438403,
    0.4499921364875955,
    4.2949032772938796e-15,
    1.6378213769982798e-18,
    0.17440839443160014,
    0.45014182725673685,
    0.4499921361533855,
    4.294903277284176e-15,
    1.6378213769996049e-18,
    3.079964655314858e-17,
    2.7245202333370253e-18,
    2.723579324739458e-18,
    0.45006327455300144,
    0.46285415809855257,
    0.4499372773410599,
    4.294882273503415e-16,
    1.6345572435130145e-19,
    0.45006327811419505,
    0.46285327024154477,
    0.4499373053090473,
    4.29488226910111e-16,
    1.6345572435130547e-19,
    0.45,
    0.45012796188698984,
    0.449993728343443,
    2.2624380322751027e-16,
    1.0896609364320287e-19,
    0.45,
    0.4501279741298731,
    0.4499937279739048,
    2.2624380321085933e-16,
    1.08966093643209e-19,
    3.0799650404060914e-17,
    2.7245202333364206e-18,
    2.7235793247383065e-18,
    0.45006327504933286,
    0.46285368304473185,
    0.4499372963629793,
    4.2948822702725344e-16,
    1.6345572435122894e-19,
    0.45006328177627497,
    0.4628470324580802,
    0.4499375571224463,
    4.294882235972755e-16,
    1.6345572435126755e-19,
    0.45,
    0.45012796566100355,
    0.4499937282662242,
    2.262438031891385e-16,
    1.0896609364317935e-19,
    0.45,
    0.45012801700431265,
    0.44999372760738465,
    2.262438032143333e-16,
    1.0896609364323063e-19,
    3.0799644453691635e-17,
    2.7245202332330948e-18,
    2.7235793246275567e-18,
    0.4500632690800887,
    0.4628475795207647,
    0.44993748468881567,
    4.294882250781315e-16,
    1.6345572433249188e-19,
    0.4500632687026557,
    0.46284797121600707,
    0.4499374695218006,
    4.294882254322511e-16,
    1.6345572433248605e-19,
    0.45,
    0.45012797857959624,
    0.4499937289278767,
    2.2624380327995704e-16,
    1.089660936387036e-19,
    0.45,
    0.4501279756312486,
    0.44999372890541517,
    2.262438031950737e-16,
    1.0896609363869615e-19,
    3.079964245681227e-17,
    2.724520233210651e-18,
    2.7235793246021382e-18,
    0.45006326459519846,
    0.4628543237231626,
    0.44993721178475016,
    4.294882284172175e-16,
    1.6345572432718423e-19,
    0.45006326825842824,
    0.4628480952425546,
    0.44993746316921307,
    4.2948822549168184e-16,
    1.6345572432721724e-19,
    0.45,
    0.4501279309359734,
    0.4499937292753653,
    2.2624380313427445e-16,
    1.089660936375984e-19,
    0.45,
    0.4501279737512424,
    0.449993728949924,
    2.2624380319521455e-16,
    1.0896609363764324e-19,
    3.079952786673215e-17,
    2.7245202334973805e-18,
    2.7235793249120493e-18,
    0.4500632030711476,
    0.462833251565287,
    0.449938297434662,
    4.2948821376793414e-16,
    1.6345572438199803e-19,
    0.45006336189204754,
    0.4627112119894882,
    0.44994300352769184,
    4.294881490522699e-16,
    1.6345572438270814e-19,
    0.45,
    0.45012793363577397,
    0.44999373542388316,
    2.262438030997255e-16,
    1.0896609365108777e-19,
    0.45,
    0.45012894732720954,
    0.44999371960140616,
    2.2624380331538183e-16,
    1.0896609365204176e-19,
    3.079966995874873e-17,
    2.7245202335785616e-18,
    2.7235793250098726e-18,
    0.45006330504814723,
    0.4628468160395157,
    0.4499375047151839,
    4.2948822342840915e-16,
    1.6345572439737203e-19,
    0.45006328703764653,
    0.462859258141861,
    0.44993702938908775,
    4.2948823060535335e-16,
    1.6345572439729336e-19,
    0.45,
    0.4501280631209765,
    0.4499937252949429,
    2.262438032505646e-16,
    1.089660936544039e-19,
    0.45,
    0.4501279556931096,
    0.44999372708855917,
    2.2624380322556434e-16,
    1.089660936542981e-19,
    3.0799647933588804e-17,
    2.724520233121751e-18,
    2.723579324506867e-18,
    0.4500632856119152,
    0.4628471319330997,
    0.44993756913791516,
    4.294882232344643e-16,
    1.6345572431106926e-19,
    0.4500632867664229,
    0.4628460375145098,
    0.44993761265265925,
    4.2948822253155604e-16,
    1.6345572431107568e-19,
    0.45,
    0.4501280271958931,
    0.4499937272649098,
    2.2624380327338815e-16,
    1.08966093633866e-19,
    0.45,
    0.4501280358905748,
    0.44999372711193186,
    2.2624380322184427e-16,
    1.089660936338753e-19,
    3.079964194242968e-17,
    2.724520233144003e-18,
    2.723579324532595e-18,
    0.4500632867597379,
    0.4628460286147621,
    0.44993761237004576,
    4.2948822285665533e-16,
    1.634557243162621e-19,
    0.45006328564400105,
    0.46284710181902206,
    0.44993756990535283,
    4.2948822316459907e-16,
    1.6345572431625554e-19,
    0.45,
    0.4501280357966516,
    0.44999372722373376,
    2.262438033772993e-16,
    1.089660936349204e-19,
    0.45,
    0.4501280273692307,
    0.4499937272240356,
    2.262438032204168e-16,
    1.089660936349123e-19,
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
    VV_junc8__RBC_volume = y[166]
    VV_junc8__q_C = y[167]
    VV_junc8__q_C_d = y[168]
    PV15__H_link_R = y[169]
    PV15__H_link_L = y[170]
    PV15__H_down = y[171]
    PV15__RBC_volume = y[172]
    PV15__q_C = y[173]
    PV16__H_link_R = y[174]
    PV16__H_link_L = y[175]
    PV16__H_down = y[176]
    PV16__RBC_volume = y[177]
    PV16__q_C = y[178]
    V15__H_link_R = y[179]
    V15__H_link_L = y[180]
    V15__H_down = y[181]
    V15__RBC_volume = y[182]
    V15__q_C = y[183]
    V16__H_link_R = y[184]
    V16__H_link_L = y[185]
    V16__H_down = y[186]
    V16__RBC_volume = y[187]
    V16__q_C = y[188]
    VV_junc9__RBC_volume = y[189]
    VV_junc9__q_C = y[190]
    VV_junc9__q_C_d = y[191]
    PV17__H_link_R = y[192]
    PV17__H_link_L = y[193]
    PV17__H_down = y[194]
    PV17__RBC_volume = y[195]
    PV17__q_C = y[196]
    PV18__H_link_R = y[197]
    PV18__H_link_L = y[198]
    PV18__H_down = y[199]
    PV18__RBC_volume = y[200]
    PV18__q_C = y[201]
    V17__H_link_R = y[202]
    V17__H_link_L = y[203]
    V17__H_down = y[204]
    V17__RBC_volume = y[205]
    V17__q_C = y[206]
    V18__H_link_R = y[207]
    V18__H_link_L = y[208]
    V18__H_down = y[209]
    V18__RBC_volume = y[210]
    V18__q_C = y[211]
    VV_junc10__RBC_volume = y[212]
    VV_junc10__q_C = y[213]
    VV_junc10__q_C_d = y[214]
    PV19__H_link_R = y[215]
    PV19__H_link_L = y[216]
    PV19__H_down = y[217]
    PV19__RBC_volume = y[218]
    PV19__q_C = y[219]
    PV20__H_link_R = y[220]
    PV20__H_link_L = y[221]
    PV20__H_down = y[222]
    PV20__RBC_volume = y[223]
    PV20__q_C = y[224]
    V19__H_link_R = y[225]
    V19__H_link_L = y[226]
    V19__H_down = y[227]
    V19__RBC_volume = y[228]
    V19__q_C = y[229]
    V20__H_link_R = y[230]
    V20__H_link_L = y[231]
    V20__H_down = y[232]
    V20__RBC_volume = y[233]
    V20__q_C = y[234]
    VV_junc11__RBC_volume = y[235]
    VV_junc11__q_C = y[236]
    VV_junc11__q_C_d = y[237]
    PV21__H_link_R = y[238]
    PV21__H_link_L = y[239]
    PV21__H_down = y[240]
    PV21__RBC_volume = y[241]
    PV21__q_C = y[242]
    PV22__H_link_R = y[243]
    PV22__H_link_L = y[244]
    PV22__H_down = y[245]
    PV22__RBC_volume = y[246]
    PV22__q_C = y[247]
    V21__H_link_R = y[248]
    V21__H_link_L = y[249]
    V21__H_down = y[250]
    V21__RBC_volume = y[251]
    V21__q_C = y[252]
    V22__H_link_R = y[253]
    V22__H_link_L = y[254]
    V22__H_down = y[255]
    V22__RBC_volume = y[256]
    V22__q_C = y[257]
    VV_junc12__RBC_volume = y[258]
    VV_junc12__q_C = y[259]
    VV_junc12__q_C_d = y[260]
    PV23__H_link_R = y[261]
    PV23__H_link_L = y[262]
    PV23__H_down = y[263]
    PV23__RBC_volume = y[264]
    PV23__q_C = y[265]
    PV24__H_link_R = y[266]
    PV24__H_link_L = y[267]
    PV24__H_down = y[268]
    PV24__RBC_volume = y[269]
    PV24__q_C = y[270]
    V23__H_link_R = y[271]
    V23__H_link_L = y[272]
    V23__H_down = y[273]
    V23__RBC_volume = y[274]
    V23__q_C = y[275]
    V24__H_link_R = y[276]
    V24__H_link_L = y[277]
    V24__H_down = y[278]
    V24__RBC_volume = y[279]
    V24__q_C = y[280]
    VV_junc13__RBC_volume = y[281]
    VV_junc13__q_C = y[282]
    VV_junc13__q_C_d = y[283]
    PV25__H_link_R = y[284]
    PV25__H_link_L = y[285]
    PV25__H_down = y[286]
    PV25__RBC_volume = y[287]
    PV25__q_C = y[288]
    PV26__H_link_R = y[289]
    PV26__H_link_L = y[290]
    PV26__H_down = y[291]
    PV26__RBC_volume = y[292]
    PV26__q_C = y[293]
    V25__H_link_R = y[294]
    V25__H_link_L = y[295]
    V25__H_down = y[296]
    V25__RBC_volume = y[297]
    V25__q_C = y[298]
    V26__H_link_R = y[299]
    V26__H_link_L = y[300]
    V26__H_down = y[301]
    V26__RBC_volume = y[302]
    V26__q_C = y[303]
    VV_junc14__RBC_volume = y[304]
    VV_junc14__q_C = y[305]
    VV_junc14__q_C_d = y[306]
    PV27__H_link_R = y[307]
    PV27__H_link_L = y[308]
    PV27__H_down = y[309]
    PV27__RBC_volume = y[310]
    PV27__q_C = y[311]
    PV28__H_link_R = y[312]
    PV28__H_link_L = y[313]
    PV28__H_down = y[314]
    PV28__RBC_volume = y[315]
    PV28__q_C = y[316]
    V27__H_link_R = y[317]
    V27__H_link_L = y[318]
    V27__H_down = y[319]
    V27__RBC_volume = y[320]
    V27__q_C = y[321]
    V28__H_link_R = y[322]
    V28__H_link_L = y[323]
    V28__H_down = y[324]
    V28__RBC_volume = y[325]
    V28__q_C = y[326]
    VV_junc15__RBC_volume = y[327]
    VV_junc15__q_C = y[328]
    VV_junc15__q_C_d = y[329]
    PV29__H_link_R = y[330]
    PV29__H_link_L = y[331]
    PV29__H_down = y[332]
    PV29__RBC_volume = y[333]
    PV29__q_C = y[334]
    PV30__H_link_R = y[335]
    PV30__H_link_L = y[336]
    PV30__H_down = y[337]
    PV30__RBC_volume = y[338]
    PV30__q_C = y[339]
    V29__H_link_R = y[340]
    V29__H_link_L = y[341]
    V29__H_down = y[342]
    V29__RBC_volume = y[343]
    V29__q_C = y[344]
    V30__H_link_R = y[345]
    V30__H_link_L = y[346]
    V30__H_down = y[347]
    V30__RBC_volume = y[348]
    V30__q_C = y[349]

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
    VV_junc8__vj2 = VV_junc8__vbc2
    VV_junc8__D1 = 2*V7__r
    VV_junc8__D2 = 2*VV_junc8__r_bc2
    VV_junc8__D3 = 2*PV15__r
    VV_junc8__D4 = 2*PV16__r
    VV_junc8__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc8__vj2/VV_junc8__v_scale)
    VV_junc8__w_out2 = 1-VV_junc8__w_in2
    VV_junc8__Qin2 = VV_junc8__w_in2*VV_junc8__vj2
    VV_junc8__Qout2 = VV_junc8__w_out2*-VV_junc8__vj2
    VV_junc8__q_us = np.pi*np.square(VV_junc8__r)*VV_junc8__l
    VV_junc8__q = VV_junc8__q_us+VV_junc8__q_C+VV_junc8__q_C_d
    VV_junc8__bc2_is_in = (1 if VV_junc8__Qin2 > VV_junc8__v_threshold else 0)
    VV_junc8__bc2_is_out = (1 if VV_junc8__Qout2 > VV_junc8__v_threshold else 0)
    VV_junc8__C_max12 = (V7__C if V7__C > VV_junc8__C_conn2 else (VV_junc8__C_conn2 if V7__C <= VV_junc8__C_conn2 else 0.0))
    PV15__R_constriction = PV15__R_constriction_base+(PV15__R_constriction_final-PV15__R_constriction_base)/(1+np.exp(-(environment__time-PV15__t0)/PV15__tau_sig))
    PV15__H_L_in = PV15__H_link_L
    PV15__H_R_in = PV15__H_link_R
    PV15__q_us = np.pi*np.square(PV15__r)*PV15__l
    PV15__q = PV15__q_us+PV15__q_C
    PV15__C = np.pi*np.square(8.5e-9)*PV15__l/133.322
    PV15__Z = (0.8+np.exp(-0.075*2*PV15__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV15__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV15__r*1e6, 12))
    PV15__mu_45 = 6*np.exp(-0.085*2*PV15__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV15__r*1e6, 0.645))
    PV15__u = PV15__q_C/PV15__C+PV15__u_ext
    PV16__R_constriction = PV16__R_constriction_base+(PV16__R_constriction_final-PV16__R_constriction_base)/(1+np.exp(-(environment__time-PV16__t0)/PV16__tau_sig))
    PV16__H_L_in = PV16__H_link_L
    PV16__H_R_in = PV16__H_link_R
    PV16__q_us = np.pi*np.square(PV16__r)*PV16__l
    PV16__q = PV16__q_us+PV16__q_C
    PV16__C = np.pi*np.square(8.5e-9)*PV16__l/133.322
    PV16__Z = (0.8+np.exp(-0.075*2*PV16__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV16__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV16__r*1e6, 12))
    PV16__mu_45 = 6*np.exp(-0.085*2*PV16__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV16__r*1e6, 0.645))
    PV16__u = PV16__q_C/PV16__C+PV16__u_ext
    V15__H_L_in = V15__H_link_L
    V15__H_R_in = V15__H_link_R
    V15__q_us = np.pi*np.square(V15__r)*V15__l
    V15__q = V15__q_us+V15__q_C
    V15__C = np.pi*np.square(8.5e-9)*V15__l/133.322
    V15__Z = (0.8+np.exp(-0.075*2*V15__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V15__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V15__r*1e6, 12))
    V15__mu_45 = 6*np.exp(-0.085*2*V15__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V15__r*1e6, 0.645))
    V15__u = V15__q_C/V15__C+V15__u_ext
    V16__H_L_in = V16__H_link_L
    V16__H_R_in = V16__H_link_R
    V16__q_us = np.pi*np.square(V16__r)*V16__l
    V16__q = V16__q_us+V16__q_C
    V16__C = np.pi*np.square(8.5e-9)*V16__l/133.322
    V16__Z = (0.8+np.exp(-0.075*2*V16__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V16__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V16__r*1e6, 12))
    V16__mu_45 = 6*np.exp(-0.085*2*V16__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V16__r*1e6, 0.645))
    V16__u = V16__q_C/V16__C+V16__u_ext
    VV_junc9__vj2 = VV_junc9__vbc2
    VV_junc9__D1 = 2*V8__r
    VV_junc9__D2 = 2*VV_junc9__r_bc2
    VV_junc9__D3 = 2*PV17__r
    VV_junc9__D4 = 2*PV18__r
    VV_junc9__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc9__vj2/VV_junc9__v_scale)
    VV_junc9__w_out2 = 1-VV_junc9__w_in2
    VV_junc9__Qin2 = VV_junc9__w_in2*VV_junc9__vj2
    VV_junc9__Qout2 = VV_junc9__w_out2*-VV_junc9__vj2
    VV_junc9__q_us = np.pi*np.square(VV_junc9__r)*VV_junc9__l
    VV_junc9__q = VV_junc9__q_us+VV_junc9__q_C+VV_junc9__q_C_d
    VV_junc9__bc2_is_in = (1 if VV_junc9__Qin2 > VV_junc9__v_threshold else 0)
    VV_junc9__bc2_is_out = (1 if VV_junc9__Qout2 > VV_junc9__v_threshold else 0)
    VV_junc9__C_max12 = (V8__C if V8__C > VV_junc9__C_conn2 else (VV_junc9__C_conn2 if V8__C <= VV_junc9__C_conn2 else 0.0))
    PV17__R_constriction = PV17__R_constriction_base+(PV17__R_constriction_final-PV17__R_constriction_base)/(1+np.exp(-(environment__time-PV17__t0)/PV17__tau_sig))
    PV17__H_L_in = PV17__H_link_L
    PV17__H_R_in = PV17__H_link_R
    PV17__q_us = np.pi*np.square(PV17__r)*PV17__l
    PV17__q = PV17__q_us+PV17__q_C
    PV17__C = np.pi*np.square(8.5e-9)*PV17__l/133.322
    PV17__Z = (0.8+np.exp(-0.075*2*PV17__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV17__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV17__r*1e6, 12))
    PV17__mu_45 = 6*np.exp(-0.085*2*PV17__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV17__r*1e6, 0.645))
    PV17__u = PV17__q_C/PV17__C+PV17__u_ext
    PV18__R_constriction = PV18__R_constriction_base+(PV18__R_constriction_final-PV18__R_constriction_base)/(1+np.exp(-(environment__time-PV18__t0)/PV18__tau_sig))
    PV18__H_L_in = PV18__H_link_L
    PV18__H_R_in = PV18__H_link_R
    PV18__q_us = np.pi*np.square(PV18__r)*PV18__l
    PV18__q = PV18__q_us+PV18__q_C
    PV18__C = np.pi*np.square(8.5e-9)*PV18__l/133.322
    PV18__Z = (0.8+np.exp(-0.075*2*PV18__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV18__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV18__r*1e6, 12))
    PV18__mu_45 = 6*np.exp(-0.085*2*PV18__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV18__r*1e6, 0.645))
    PV18__u = PV18__q_C/PV18__C+PV18__u_ext
    V17__H_L_in = V17__H_link_L
    V17__H_R_in = V17__H_link_R
    V17__q_us = np.pi*np.square(V17__r)*V17__l
    V17__q = V17__q_us+V17__q_C
    V17__C = np.pi*np.square(8.5e-9)*V17__l/133.322
    V17__Z = (0.8+np.exp(-0.075*2*V17__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V17__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V17__r*1e6, 12))
    V17__mu_45 = 6*np.exp(-0.085*2*V17__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V17__r*1e6, 0.645))
    V17__u = V17__q_C/V17__C+V17__u_ext
    V18__H_L_in = V18__H_link_L
    V18__H_R_in = V18__H_link_R
    V18__q_us = np.pi*np.square(V18__r)*V18__l
    V18__q = V18__q_us+V18__q_C
    V18__C = np.pi*np.square(8.5e-9)*V18__l/133.322
    V18__Z = (0.8+np.exp(-0.075*2*V18__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V18__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V18__r*1e6, 12))
    V18__mu_45 = 6*np.exp(-0.085*2*V18__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V18__r*1e6, 0.645))
    V18__u = V18__q_C/V18__C+V18__u_ext
    VV_junc10__vj2 = VV_junc10__vbc2
    VV_junc10__D1 = 2*V9__r
    VV_junc10__D2 = 2*VV_junc10__r_bc2
    VV_junc10__D3 = 2*PV19__r
    VV_junc10__D4 = 2*PV20__r
    VV_junc10__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc10__vj2/VV_junc10__v_scale)
    VV_junc10__w_out2 = 1-VV_junc10__w_in2
    VV_junc10__Qin2 = VV_junc10__w_in2*VV_junc10__vj2
    VV_junc10__Qout2 = VV_junc10__w_out2*-VV_junc10__vj2
    VV_junc10__q_us = np.pi*np.square(VV_junc10__r)*VV_junc10__l
    VV_junc10__q = VV_junc10__q_us+VV_junc10__q_C+VV_junc10__q_C_d
    VV_junc10__bc2_is_in = (1 if VV_junc10__Qin2 > VV_junc10__v_threshold else 0)
    VV_junc10__bc2_is_out = (1 if VV_junc10__Qout2 > VV_junc10__v_threshold else 0)
    VV_junc10__C_max12 = (V9__C if V9__C > VV_junc10__C_conn2 else (VV_junc10__C_conn2 if V9__C <= VV_junc10__C_conn2 else 0.0))
    PV19__R_constriction = PV19__R_constriction_base+(PV19__R_constriction_final-PV19__R_constriction_base)/(1+np.exp(-(environment__time-PV19__t0)/PV19__tau_sig))
    PV19__H_L_in = PV19__H_link_L
    PV19__H_R_in = PV19__H_link_R
    PV19__q_us = np.pi*np.square(PV19__r)*PV19__l
    PV19__q = PV19__q_us+PV19__q_C
    PV19__C = np.pi*np.square(8.5e-9)*PV19__l/133.322
    PV19__Z = (0.8+np.exp(-0.075*2*PV19__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV19__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV19__r*1e6, 12))
    PV19__mu_45 = 6*np.exp(-0.085*2*PV19__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV19__r*1e6, 0.645))
    PV19__u = PV19__q_C/PV19__C+PV19__u_ext
    PV20__R_constriction = PV20__R_constriction_base+(PV20__R_constriction_final-PV20__R_constriction_base)/(1+np.exp(-(environment__time-PV20__t0)/PV20__tau_sig))
    PV20__H_L_in = PV20__H_link_L
    PV20__H_R_in = PV20__H_link_R
    PV20__q_us = np.pi*np.square(PV20__r)*PV20__l
    PV20__q = PV20__q_us+PV20__q_C
    PV20__C = np.pi*np.square(8.5e-9)*PV20__l/133.322
    PV20__Z = (0.8+np.exp(-0.075*2*PV20__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV20__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV20__r*1e6, 12))
    PV20__mu_45 = 6*np.exp(-0.085*2*PV20__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV20__r*1e6, 0.645))
    PV20__u = PV20__q_C/PV20__C+PV20__u_ext
    V19__H_L_in = V19__H_link_L
    V19__H_R_in = V19__H_link_R
    V19__q_us = np.pi*np.square(V19__r)*V19__l
    V19__q = V19__q_us+V19__q_C
    V19__C = np.pi*np.square(8.5e-9)*V19__l/133.322
    V19__Z = (0.8+np.exp(-0.075*2*V19__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V19__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V19__r*1e6, 12))
    V19__mu_45 = 6*np.exp(-0.085*2*V19__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V19__r*1e6, 0.645))
    V19__u = V19__q_C/V19__C+V19__u_ext
    V20__H_L_in = V20__H_link_L
    V20__H_R_in = V20__H_link_R
    V20__q_us = np.pi*np.square(V20__r)*V20__l
    V20__q = V20__q_us+V20__q_C
    V20__C = np.pi*np.square(8.5e-9)*V20__l/133.322
    V20__Z = (0.8+np.exp(-0.075*2*V20__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V20__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V20__r*1e6, 12))
    V20__mu_45 = 6*np.exp(-0.085*2*V20__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V20__r*1e6, 0.645))
    V20__u = V20__q_C/V20__C+V20__u_ext
    VV_junc11__vj2 = VV_junc11__vbc2
    VV_junc11__D1 = 2*V10__r
    VV_junc11__D2 = 2*VV_junc11__r_bc2
    VV_junc11__D3 = 2*PV21__r
    VV_junc11__D4 = 2*PV22__r
    VV_junc11__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc11__vj2/VV_junc11__v_scale)
    VV_junc11__w_out2 = 1-VV_junc11__w_in2
    VV_junc11__Qin2 = VV_junc11__w_in2*VV_junc11__vj2
    VV_junc11__Qout2 = VV_junc11__w_out2*-VV_junc11__vj2
    VV_junc11__q_us = np.pi*np.square(VV_junc11__r)*VV_junc11__l
    VV_junc11__q = VV_junc11__q_us+VV_junc11__q_C+VV_junc11__q_C_d
    VV_junc11__bc2_is_in = (1 if VV_junc11__Qin2 > VV_junc11__v_threshold else 0)
    VV_junc11__bc2_is_out = (1 if VV_junc11__Qout2 > VV_junc11__v_threshold else 0)
    VV_junc11__C_max12 = (V10__C if V10__C > VV_junc11__C_conn2 else (VV_junc11__C_conn2 if V10__C <= VV_junc11__C_conn2 else 0.0))
    PV21__R_constriction = PV21__R_constriction_base+(PV21__R_constriction_final-PV21__R_constriction_base)/(1+np.exp(-(environment__time-PV21__t0)/PV21__tau_sig))
    PV21__H_L_in = PV21__H_link_L
    PV21__H_R_in = PV21__H_link_R
    PV21__q_us = np.pi*np.square(PV21__r)*PV21__l
    PV21__q = PV21__q_us+PV21__q_C
    PV21__C = np.pi*np.square(8.5e-9)*PV21__l/133.322
    PV21__Z = (0.8+np.exp(-0.075*2*PV21__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV21__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV21__r*1e6, 12))
    PV21__mu_45 = 6*np.exp(-0.085*2*PV21__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV21__r*1e6, 0.645))
    PV21__u = PV21__q_C/PV21__C+PV21__u_ext
    PV22__R_constriction = PV22__R_constriction_base+(PV22__R_constriction_final-PV22__R_constriction_base)/(1+np.exp(-(environment__time-PV22__t0)/PV22__tau_sig))
    PV22__H_L_in = PV22__H_link_L
    PV22__H_R_in = PV22__H_link_R
    PV22__q_us = np.pi*np.square(PV22__r)*PV22__l
    PV22__q = PV22__q_us+PV22__q_C
    PV22__C = np.pi*np.square(8.5e-9)*PV22__l/133.322
    PV22__Z = (0.8+np.exp(-0.075*2*PV22__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV22__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV22__r*1e6, 12))
    PV22__mu_45 = 6*np.exp(-0.085*2*PV22__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV22__r*1e6, 0.645))
    PV22__u = PV22__q_C/PV22__C+PV22__u_ext
    V21__H_L_in = V21__H_link_L
    V21__H_R_in = V21__H_link_R
    V21__q_us = np.pi*np.square(V21__r)*V21__l
    V21__q = V21__q_us+V21__q_C
    V21__C = np.pi*np.square(8.5e-9)*V21__l/133.322
    V21__Z = (0.8+np.exp(-0.075*2*V21__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V21__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V21__r*1e6, 12))
    V21__mu_45 = 6*np.exp(-0.085*2*V21__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V21__r*1e6, 0.645))
    V21__u = V21__q_C/V21__C+V21__u_ext
    V22__H_L_in = V22__H_link_L
    V22__H_R_in = V22__H_link_R
    V22__q_us = np.pi*np.square(V22__r)*V22__l
    V22__q = V22__q_us+V22__q_C
    V22__C = np.pi*np.square(8.5e-9)*V22__l/133.322
    V22__Z = (0.8+np.exp(-0.075*2*V22__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V22__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V22__r*1e6, 12))
    V22__mu_45 = 6*np.exp(-0.085*2*V22__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V22__r*1e6, 0.645))
    V22__u = V22__q_C/V22__C+V22__u_ext
    VV_junc12__vj2 = VV_junc12__vbc2
    VV_junc12__D1 = 2*V11__r
    VV_junc12__D2 = 2*VV_junc12__r_bc2
    VV_junc12__D3 = 2*PV23__r
    VV_junc12__D4 = 2*PV24__r
    VV_junc12__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc12__vj2/VV_junc12__v_scale)
    VV_junc12__w_out2 = 1-VV_junc12__w_in2
    VV_junc12__Qin2 = VV_junc12__w_in2*VV_junc12__vj2
    VV_junc12__Qout2 = VV_junc12__w_out2*-VV_junc12__vj2
    VV_junc12__q_us = np.pi*np.square(VV_junc12__r)*VV_junc12__l
    VV_junc12__q = VV_junc12__q_us+VV_junc12__q_C+VV_junc12__q_C_d
    VV_junc12__bc2_is_in = (1 if VV_junc12__Qin2 > VV_junc12__v_threshold else 0)
    VV_junc12__bc2_is_out = (1 if VV_junc12__Qout2 > VV_junc12__v_threshold else 0)
    VV_junc12__C_max12 = (V11__C if V11__C > VV_junc12__C_conn2 else (VV_junc12__C_conn2 if V11__C <= VV_junc12__C_conn2 else 0.0))
    PV23__R_constriction = PV23__R_constriction_base+(PV23__R_constriction_final-PV23__R_constriction_base)/(1+np.exp(-(environment__time-PV23__t0)/PV23__tau_sig))
    PV23__H_L_in = PV23__H_link_L
    PV23__H_R_in = PV23__H_link_R
    PV23__q_us = np.pi*np.square(PV23__r)*PV23__l
    PV23__q = PV23__q_us+PV23__q_C
    PV23__C = np.pi*np.square(8.5e-9)*PV23__l/133.322
    PV23__Z = (0.8+np.exp(-0.075*2*PV23__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV23__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV23__r*1e6, 12))
    PV23__mu_45 = 6*np.exp(-0.085*2*PV23__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV23__r*1e6, 0.645))
    PV23__u = PV23__q_C/PV23__C+PV23__u_ext
    PV24__R_constriction = PV24__R_constriction_base+(PV24__R_constriction_final-PV24__R_constriction_base)/(1+np.exp(-(environment__time-PV24__t0)/PV24__tau_sig))
    PV24__H_L_in = PV24__H_link_L
    PV24__H_R_in = PV24__H_link_R
    PV24__q_us = np.pi*np.square(PV24__r)*PV24__l
    PV24__q = PV24__q_us+PV24__q_C
    PV24__C = np.pi*np.square(8.5e-9)*PV24__l/133.322
    PV24__Z = (0.8+np.exp(-0.075*2*PV24__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV24__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV24__r*1e6, 12))
    PV24__mu_45 = 6*np.exp(-0.085*2*PV24__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV24__r*1e6, 0.645))
    PV24__u = PV24__q_C/PV24__C+PV24__u_ext
    V23__H_L_in = V23__H_link_L
    V23__H_R_in = V23__H_link_R
    V23__q_us = np.pi*np.square(V23__r)*V23__l
    V23__q = V23__q_us+V23__q_C
    V23__C = np.pi*np.square(8.5e-9)*V23__l/133.322
    V23__Z = (0.8+np.exp(-0.075*2*V23__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V23__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V23__r*1e6, 12))
    V23__mu_45 = 6*np.exp(-0.085*2*V23__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V23__r*1e6, 0.645))
    V23__u = V23__q_C/V23__C+V23__u_ext
    V24__H_L_in = V24__H_link_L
    V24__H_R_in = V24__H_link_R
    V24__q_us = np.pi*np.square(V24__r)*V24__l
    V24__q = V24__q_us+V24__q_C
    V24__C = np.pi*np.square(8.5e-9)*V24__l/133.322
    V24__Z = (0.8+np.exp(-0.075*2*V24__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V24__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V24__r*1e6, 12))
    V24__mu_45 = 6*np.exp(-0.085*2*V24__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V24__r*1e6, 0.645))
    V24__u = V24__q_C/V24__C+V24__u_ext
    VV_junc13__vj2 = VV_junc13__vbc2
    VV_junc13__D1 = 2*V12__r
    VV_junc13__D2 = 2*VV_junc13__r_bc2
    VV_junc13__D3 = 2*PV25__r
    VV_junc13__D4 = 2*PV26__r
    VV_junc13__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc13__vj2/VV_junc13__v_scale)
    VV_junc13__w_out2 = 1-VV_junc13__w_in2
    VV_junc13__Qin2 = VV_junc13__w_in2*VV_junc13__vj2
    VV_junc13__Qout2 = VV_junc13__w_out2*-VV_junc13__vj2
    VV_junc13__q_us = np.pi*np.square(VV_junc13__r)*VV_junc13__l
    VV_junc13__q = VV_junc13__q_us+VV_junc13__q_C+VV_junc13__q_C_d
    VV_junc13__bc2_is_in = (1 if VV_junc13__Qin2 > VV_junc13__v_threshold else 0)
    VV_junc13__bc2_is_out = (1 if VV_junc13__Qout2 > VV_junc13__v_threshold else 0)
    VV_junc13__C_max12 = (V12__C if V12__C > VV_junc13__C_conn2 else (VV_junc13__C_conn2 if V12__C <= VV_junc13__C_conn2 else 0.0))
    PV25__R_constriction = PV25__R_constriction_base+(PV25__R_constriction_final-PV25__R_constriction_base)/(1+np.exp(-(environment__time-PV25__t0)/PV25__tau_sig))
    PV25__H_L_in = PV25__H_link_L
    PV25__H_R_in = PV25__H_link_R
    PV25__q_us = np.pi*np.square(PV25__r)*PV25__l
    PV25__q = PV25__q_us+PV25__q_C
    PV25__C = np.pi*np.square(8.5e-9)*PV25__l/133.322
    PV25__Z = (0.8+np.exp(-0.075*2*PV25__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV25__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV25__r*1e6, 12))
    PV25__mu_45 = 6*np.exp(-0.085*2*PV25__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV25__r*1e6, 0.645))
    PV25__u = PV25__q_C/PV25__C+PV25__u_ext
    PV26__R_constriction = PV26__R_constriction_base+(PV26__R_constriction_final-PV26__R_constriction_base)/(1+np.exp(-(environment__time-PV26__t0)/PV26__tau_sig))
    PV26__H_L_in = PV26__H_link_L
    PV26__H_R_in = PV26__H_link_R
    PV26__q_us = np.pi*np.square(PV26__r)*PV26__l
    PV26__q = PV26__q_us+PV26__q_C
    PV26__C = np.pi*np.square(8.5e-9)*PV26__l/133.322
    PV26__Z = (0.8+np.exp(-0.075*2*PV26__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV26__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV26__r*1e6, 12))
    PV26__mu_45 = 6*np.exp(-0.085*2*PV26__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV26__r*1e6, 0.645))
    PV26__u = PV26__q_C/PV26__C+PV26__u_ext
    V25__H_L_in = V25__H_link_L
    V25__H_R_in = V25__H_link_R
    V25__q_us = np.pi*np.square(V25__r)*V25__l
    V25__q = V25__q_us+V25__q_C
    V25__C = np.pi*np.square(8.5e-9)*V25__l/133.322
    V25__Z = (0.8+np.exp(-0.075*2*V25__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V25__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V25__r*1e6, 12))
    V25__mu_45 = 6*np.exp(-0.085*2*V25__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V25__r*1e6, 0.645))
    V25__u = V25__q_C/V25__C+V25__u_ext
    V26__H_L_in = V26__H_link_L
    V26__H_R_in = V26__H_link_R
    V26__q_us = np.pi*np.square(V26__r)*V26__l
    V26__q = V26__q_us+V26__q_C
    V26__C = np.pi*np.square(8.5e-9)*V26__l/133.322
    V26__Z = (0.8+np.exp(-0.075*2*V26__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V26__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V26__r*1e6, 12))
    V26__mu_45 = 6*np.exp(-0.085*2*V26__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V26__r*1e6, 0.645))
    V26__u = V26__q_C/V26__C+V26__u_ext
    VV_junc14__vj2 = VV_junc14__vbc2
    VV_junc14__D1 = 2*V13__r
    VV_junc14__D2 = 2*VV_junc14__r_bc2
    VV_junc14__D3 = 2*PV27__r
    VV_junc14__D4 = 2*PV28__r
    VV_junc14__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc14__vj2/VV_junc14__v_scale)
    VV_junc14__w_out2 = 1-VV_junc14__w_in2
    VV_junc14__Qin2 = VV_junc14__w_in2*VV_junc14__vj2
    VV_junc14__Qout2 = VV_junc14__w_out2*-VV_junc14__vj2
    VV_junc14__q_us = np.pi*np.square(VV_junc14__r)*VV_junc14__l
    VV_junc14__q = VV_junc14__q_us+VV_junc14__q_C+VV_junc14__q_C_d
    VV_junc14__bc2_is_in = (1 if VV_junc14__Qin2 > VV_junc14__v_threshold else 0)
    VV_junc14__bc2_is_out = (1 if VV_junc14__Qout2 > VV_junc14__v_threshold else 0)
    VV_junc14__C_max12 = (V13__C if V13__C > VV_junc14__C_conn2 else (VV_junc14__C_conn2 if V13__C <= VV_junc14__C_conn2 else 0.0))
    PV27__R_constriction = PV27__R_constriction_base+(PV27__R_constriction_final-PV27__R_constriction_base)/(1+np.exp(-(environment__time-PV27__t0)/PV27__tau_sig))
    PV27__H_L_in = PV27__H_link_L
    PV27__H_R_in = PV27__H_link_R
    PV27__q_us = np.pi*np.square(PV27__r)*PV27__l
    PV27__q = PV27__q_us+PV27__q_C
    PV27__C = np.pi*np.square(8.5e-9)*PV27__l/133.322
    PV27__Z = (0.8+np.exp(-0.075*2*PV27__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV27__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV27__r*1e6, 12))
    PV27__mu_45 = 6*np.exp(-0.085*2*PV27__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV27__r*1e6, 0.645))
    PV27__u = PV27__q_C/PV27__C+PV27__u_ext
    PV28__R_constriction = PV28__R_constriction_base+(PV28__R_constriction_final-PV28__R_constriction_base)/(1+np.exp(-(environment__time-PV28__t0)/PV28__tau_sig))
    PV28__H_L_in = PV28__H_link_L
    PV28__H_R_in = PV28__H_link_R
    PV28__q_us = np.pi*np.square(PV28__r)*PV28__l
    PV28__q = PV28__q_us+PV28__q_C
    PV28__C = np.pi*np.square(8.5e-9)*PV28__l/133.322
    PV28__Z = (0.8+np.exp(-0.075*2*PV28__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV28__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV28__r*1e6, 12))
    PV28__mu_45 = 6*np.exp(-0.085*2*PV28__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV28__r*1e6, 0.645))
    PV28__u = PV28__q_C/PV28__C+PV28__u_ext
    V27__H_L_in = V27__H_link_L
    V27__H_R_in = V27__H_link_R
    V27__q_us = np.pi*np.square(V27__r)*V27__l
    V27__q = V27__q_us+V27__q_C
    V27__C = np.pi*np.square(8.5e-9)*V27__l/133.322
    V27__Z = (0.8+np.exp(-0.075*2*V27__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V27__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V27__r*1e6, 12))
    V27__mu_45 = 6*np.exp(-0.085*2*V27__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V27__r*1e6, 0.645))
    V27__u = V27__q_C/V27__C+V27__u_ext
    V28__H_L_in = V28__H_link_L
    V28__H_R_in = V28__H_link_R
    V28__q_us = np.pi*np.square(V28__r)*V28__l
    V28__q = V28__q_us+V28__q_C
    V28__C = np.pi*np.square(8.5e-9)*V28__l/133.322
    V28__Z = (0.8+np.exp(-0.075*2*V28__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V28__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V28__r*1e6, 12))
    V28__mu_45 = 6*np.exp(-0.085*2*V28__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V28__r*1e6, 0.645))
    V28__u = V28__q_C/V28__C+V28__u_ext
    VV_junc15__vj2 = VV_junc15__vbc2
    VV_junc15__D1 = 2*V14__r
    VV_junc15__D2 = 2*VV_junc15__r_bc2
    VV_junc15__D3 = 2*PV29__r
    VV_junc15__D4 = 2*PV30__r
    VV_junc15__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc15__vj2/VV_junc15__v_scale)
    VV_junc15__w_out2 = 1-VV_junc15__w_in2
    VV_junc15__Qin2 = VV_junc15__w_in2*VV_junc15__vj2
    VV_junc15__Qout2 = VV_junc15__w_out2*-VV_junc15__vj2
    VV_junc15__q_us = np.pi*np.square(VV_junc15__r)*VV_junc15__l
    VV_junc15__q = VV_junc15__q_us+VV_junc15__q_C+VV_junc15__q_C_d
    VV_junc15__bc2_is_in = (1 if VV_junc15__Qin2 > VV_junc15__v_threshold else 0)
    VV_junc15__bc2_is_out = (1 if VV_junc15__Qout2 > VV_junc15__v_threshold else 0)
    VV_junc15__C_max12 = (V14__C if V14__C > VV_junc15__C_conn2 else (VV_junc15__C_conn2 if V14__C <= VV_junc15__C_conn2 else 0.0))
    PV29__R_constriction = PV29__R_constriction_base+(PV29__R_constriction_final-PV29__R_constriction_base)/(1+np.exp(-(environment__time-PV29__t0)/PV29__tau_sig))
    PV29__H_L_in = PV29__H_link_L
    PV29__H_R_in = PV29__H_link_R
    PV29__q_us = np.pi*np.square(PV29__r)*PV29__l
    PV29__q = PV29__q_us+PV29__q_C
    PV29__C = np.pi*np.square(8.5e-9)*PV29__l/133.322
    PV29__Z = (0.8+np.exp(-0.075*2*PV29__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV29__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV29__r*1e6, 12))
    PV29__mu_45 = 6*np.exp(-0.085*2*PV29__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV29__r*1e6, 0.645))
    PV29__u = PV29__q_C/PV29__C+PV29__u_ext
    PV30__R_constriction = PV30__R_constriction_base+(PV30__R_constriction_final-PV30__R_constriction_base)/(1+np.exp(-(environment__time-PV30__t0)/PV30__tau_sig))
    PV30__H_L_in = PV30__H_link_L
    PV30__H_R_in = PV30__H_link_R
    PV30__q_us = np.pi*np.square(PV30__r)*PV30__l
    PV30__q = PV30__q_us+PV30__q_C
    PV30__C = np.pi*np.square(8.5e-9)*PV30__l/133.322
    PV30__Z = (0.8+np.exp(-0.075*2*PV30__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV30__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV30__r*1e6, 12))
    PV30__mu_45 = 6*np.exp(-0.085*2*PV30__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV30__r*1e6, 0.645))
    PV30__u = PV30__q_C/PV30__C+PV30__u_ext
    V29__H_L_in = V29__H_link_L
    V29__H_R_in = V29__H_link_R
    V29__q_us = np.pi*np.square(V29__r)*V29__l
    V29__q = V29__q_us+V29__q_C
    V29__C = np.pi*np.square(8.5e-9)*V29__l/133.322
    V29__Z = (0.8+np.exp(-0.075*2*V29__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V29__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V29__r*1e6, 12))
    V29__mu_45 = 6*np.exp(-0.085*2*V29__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V29__r*1e6, 0.645))
    V29__u = V29__q_C/V29__C+V29__u_ext
    V30__H_L_in = V30__H_link_L
    V30__H_R_in = V30__H_link_R
    V30__q_us = np.pi*np.square(V30__r)*V30__l
    V30__q = V30__q_us+V30__q_C
    V30__C = np.pi*np.square(8.5e-9)*V30__l/133.322
    V30__Z = (0.8+np.exp(-0.075*2*V30__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V30__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V30__r*1e6, 12))
    V30__mu_45 = 6*np.exp(-0.085*2*V30__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V30__r*1e6, 0.645))
    V30__u = V30__q_C/V30__C+V30__u_ext
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
    VV_junc8__RBC_volume_init = VV_junc8__H_global_L*VV_junc8__q_us
    VV_junc8__H_mean = VV_junc8__RBC_volume/(VV_junc8__q_us+VV_junc8__div_0)
    VV_junc8__C_max123 = (VV_junc8__C_max12 if VV_junc8__C_max12 > PV15__C else (PV15__C if VV_junc8__C_max12 <= PV15__C else 0.0))
    VV_junc8__C = (VV_junc8__C_max123 if VV_junc8__C_max123 > PV16__C else (PV16__C if VV_junc8__C_max123 <= PV16__C else 0.0))
    PV15__RBC_volume_init = PV15__H_global_L*PV15__q_us
    PV15__H_mean = PV15__RBC_volume/PV15__q
    PV15__hem_dep_u_rel = 1+(PV15__mu_45-1)*(safe_power(1-PV15__H_mean, PV15__Z)-1)/(safe_power(1-PV15__H_global_L, PV15__Z)-1)*np.square(2*PV15__r*1e6/(2*PV15__r*1e6-1.1))
    PV15__u_mmHg = PV15__u/133.322
    PV16__RBC_volume_init = PV16__H_global_L*PV16__q_us
    PV16__H_mean = PV16__RBC_volume/PV16__q
    PV16__hem_dep_u_rel = 1+(PV16__mu_45-1)*(safe_power(1-PV16__H_mean, PV16__Z)-1)/(safe_power(1-PV16__H_global_L, PV16__Z)-1)*np.square(2*PV16__r*1e6/(2*PV16__r*1e6-1.1))
    PV16__u_mmHg = PV16__u/133.322
    V15__RBC_volume_init = V15__H_global_L*V15__q_us
    V15__H_mean = V15__RBC_volume/V15__q
    V15__hem_dep_u_rel = 1+(V15__mu_45-1)*(safe_power(1-V15__H_mean, V15__Z)-1)/(safe_power(1-V15__H_global_L, V15__Z)-1)*np.square(2*V15__r*1e6/(2*V15__r*1e6-1.1))
    V15__u_mmHg = V15__u/133.322
    V16__RBC_volume_init = V16__H_global_L*V16__q_us
    V16__H_mean = V16__RBC_volume/V16__q
    V16__hem_dep_u_rel = 1+(V16__mu_45-1)*(safe_power(1-V16__H_mean, V16__Z)-1)/(safe_power(1-V16__H_global_L, V16__Z)-1)*np.square(2*V16__r*1e6/(2*V16__r*1e6-1.1))
    V16__u_mmHg = V16__u/133.322
    VV_junc9__RBC_volume_init = VV_junc9__H_global_L*VV_junc9__q_us
    VV_junc9__H_mean = VV_junc9__RBC_volume/(VV_junc9__q_us+VV_junc9__div_0)
    VV_junc9__C_max123 = (VV_junc9__C_max12 if VV_junc9__C_max12 > PV17__C else (PV17__C if VV_junc9__C_max12 <= PV17__C else 0.0))
    VV_junc9__C = (VV_junc9__C_max123 if VV_junc9__C_max123 > PV18__C else (PV18__C if VV_junc9__C_max123 <= PV18__C else 0.0))
    PV17__RBC_volume_init = PV17__H_global_L*PV17__q_us
    PV17__H_mean = PV17__RBC_volume/PV17__q
    PV17__hem_dep_u_rel = 1+(PV17__mu_45-1)*(safe_power(1-PV17__H_mean, PV17__Z)-1)/(safe_power(1-PV17__H_global_L, PV17__Z)-1)*np.square(2*PV17__r*1e6/(2*PV17__r*1e6-1.1))
    PV17__u_mmHg = PV17__u/133.322
    PV18__RBC_volume_init = PV18__H_global_L*PV18__q_us
    PV18__H_mean = PV18__RBC_volume/PV18__q
    PV18__hem_dep_u_rel = 1+(PV18__mu_45-1)*(safe_power(1-PV18__H_mean, PV18__Z)-1)/(safe_power(1-PV18__H_global_L, PV18__Z)-1)*np.square(2*PV18__r*1e6/(2*PV18__r*1e6-1.1))
    PV18__u_mmHg = PV18__u/133.322
    V17__RBC_volume_init = V17__H_global_L*V17__q_us
    V17__H_mean = V17__RBC_volume/V17__q
    V17__hem_dep_u_rel = 1+(V17__mu_45-1)*(safe_power(1-V17__H_mean, V17__Z)-1)/(safe_power(1-V17__H_global_L, V17__Z)-1)*np.square(2*V17__r*1e6/(2*V17__r*1e6-1.1))
    V17__u_mmHg = V17__u/133.322
    V18__RBC_volume_init = V18__H_global_L*V18__q_us
    V18__H_mean = V18__RBC_volume/V18__q
    V18__hem_dep_u_rel = 1+(V18__mu_45-1)*(safe_power(1-V18__H_mean, V18__Z)-1)/(safe_power(1-V18__H_global_L, V18__Z)-1)*np.square(2*V18__r*1e6/(2*V18__r*1e6-1.1))
    V18__u_mmHg = V18__u/133.322
    VV_junc10__RBC_volume_init = VV_junc10__H_global_L*VV_junc10__q_us
    VV_junc10__H_mean = VV_junc10__RBC_volume/(VV_junc10__q_us+VV_junc10__div_0)
    VV_junc10__C_max123 = (VV_junc10__C_max12 if VV_junc10__C_max12 > PV19__C else (PV19__C if VV_junc10__C_max12 <= PV19__C else 0.0))
    VV_junc10__C = (VV_junc10__C_max123 if VV_junc10__C_max123 > PV20__C else (PV20__C if VV_junc10__C_max123 <= PV20__C else 0.0))
    PV19__RBC_volume_init = PV19__H_global_L*PV19__q_us
    PV19__H_mean = PV19__RBC_volume/PV19__q
    PV19__hem_dep_u_rel = 1+(PV19__mu_45-1)*(safe_power(1-PV19__H_mean, PV19__Z)-1)/(safe_power(1-PV19__H_global_L, PV19__Z)-1)*np.square(2*PV19__r*1e6/(2*PV19__r*1e6-1.1))
    PV19__u_mmHg = PV19__u/133.322
    PV20__RBC_volume_init = PV20__H_global_L*PV20__q_us
    PV20__H_mean = PV20__RBC_volume/PV20__q
    PV20__hem_dep_u_rel = 1+(PV20__mu_45-1)*(safe_power(1-PV20__H_mean, PV20__Z)-1)/(safe_power(1-PV20__H_global_L, PV20__Z)-1)*np.square(2*PV20__r*1e6/(2*PV20__r*1e6-1.1))
    PV20__u_mmHg = PV20__u/133.322
    V19__RBC_volume_init = V19__H_global_L*V19__q_us
    V19__H_mean = V19__RBC_volume/V19__q
    V19__hem_dep_u_rel = 1+(V19__mu_45-1)*(safe_power(1-V19__H_mean, V19__Z)-1)/(safe_power(1-V19__H_global_L, V19__Z)-1)*np.square(2*V19__r*1e6/(2*V19__r*1e6-1.1))
    V19__u_mmHg = V19__u/133.322
    V20__RBC_volume_init = V20__H_global_L*V20__q_us
    V20__H_mean = V20__RBC_volume/V20__q
    V20__hem_dep_u_rel = 1+(V20__mu_45-1)*(safe_power(1-V20__H_mean, V20__Z)-1)/(safe_power(1-V20__H_global_L, V20__Z)-1)*np.square(2*V20__r*1e6/(2*V20__r*1e6-1.1))
    V20__u_mmHg = V20__u/133.322
    VV_junc11__RBC_volume_init = VV_junc11__H_global_L*VV_junc11__q_us
    VV_junc11__H_mean = VV_junc11__RBC_volume/(VV_junc11__q_us+VV_junc11__div_0)
    VV_junc11__C_max123 = (VV_junc11__C_max12 if VV_junc11__C_max12 > PV21__C else (PV21__C if VV_junc11__C_max12 <= PV21__C else 0.0))
    VV_junc11__C = (VV_junc11__C_max123 if VV_junc11__C_max123 > PV22__C else (PV22__C if VV_junc11__C_max123 <= PV22__C else 0.0))
    PV21__RBC_volume_init = PV21__H_global_L*PV21__q_us
    PV21__H_mean = PV21__RBC_volume/PV21__q
    PV21__hem_dep_u_rel = 1+(PV21__mu_45-1)*(safe_power(1-PV21__H_mean, PV21__Z)-1)/(safe_power(1-PV21__H_global_L, PV21__Z)-1)*np.square(2*PV21__r*1e6/(2*PV21__r*1e6-1.1))
    PV21__u_mmHg = PV21__u/133.322
    PV22__RBC_volume_init = PV22__H_global_L*PV22__q_us
    PV22__H_mean = PV22__RBC_volume/PV22__q
    PV22__hem_dep_u_rel = 1+(PV22__mu_45-1)*(safe_power(1-PV22__H_mean, PV22__Z)-1)/(safe_power(1-PV22__H_global_L, PV22__Z)-1)*np.square(2*PV22__r*1e6/(2*PV22__r*1e6-1.1))
    PV22__u_mmHg = PV22__u/133.322
    V21__RBC_volume_init = V21__H_global_L*V21__q_us
    V21__H_mean = V21__RBC_volume/V21__q
    V21__hem_dep_u_rel = 1+(V21__mu_45-1)*(safe_power(1-V21__H_mean, V21__Z)-1)/(safe_power(1-V21__H_global_L, V21__Z)-1)*np.square(2*V21__r*1e6/(2*V21__r*1e6-1.1))
    V21__u_mmHg = V21__u/133.322
    V22__RBC_volume_init = V22__H_global_L*V22__q_us
    V22__H_mean = V22__RBC_volume/V22__q
    V22__hem_dep_u_rel = 1+(V22__mu_45-1)*(safe_power(1-V22__H_mean, V22__Z)-1)/(safe_power(1-V22__H_global_L, V22__Z)-1)*np.square(2*V22__r*1e6/(2*V22__r*1e6-1.1))
    V22__u_mmHg = V22__u/133.322
    VV_junc12__RBC_volume_init = VV_junc12__H_global_L*VV_junc12__q_us
    VV_junc12__H_mean = VV_junc12__RBC_volume/(VV_junc12__q_us+VV_junc12__div_0)
    VV_junc12__C_max123 = (VV_junc12__C_max12 if VV_junc12__C_max12 > PV23__C else (PV23__C if VV_junc12__C_max12 <= PV23__C else 0.0))
    VV_junc12__C = (VV_junc12__C_max123 if VV_junc12__C_max123 > PV24__C else (PV24__C if VV_junc12__C_max123 <= PV24__C else 0.0))
    PV23__RBC_volume_init = PV23__H_global_L*PV23__q_us
    PV23__H_mean = PV23__RBC_volume/PV23__q
    PV23__hem_dep_u_rel = 1+(PV23__mu_45-1)*(safe_power(1-PV23__H_mean, PV23__Z)-1)/(safe_power(1-PV23__H_global_L, PV23__Z)-1)*np.square(2*PV23__r*1e6/(2*PV23__r*1e6-1.1))
    PV23__u_mmHg = PV23__u/133.322
    PV24__RBC_volume_init = PV24__H_global_L*PV24__q_us
    PV24__H_mean = PV24__RBC_volume/PV24__q
    PV24__hem_dep_u_rel = 1+(PV24__mu_45-1)*(safe_power(1-PV24__H_mean, PV24__Z)-1)/(safe_power(1-PV24__H_global_L, PV24__Z)-1)*np.square(2*PV24__r*1e6/(2*PV24__r*1e6-1.1))
    PV24__u_mmHg = PV24__u/133.322
    V23__RBC_volume_init = V23__H_global_L*V23__q_us
    V23__H_mean = V23__RBC_volume/V23__q
    V23__hem_dep_u_rel = 1+(V23__mu_45-1)*(safe_power(1-V23__H_mean, V23__Z)-1)/(safe_power(1-V23__H_global_L, V23__Z)-1)*np.square(2*V23__r*1e6/(2*V23__r*1e6-1.1))
    V23__u_mmHg = V23__u/133.322
    V24__RBC_volume_init = V24__H_global_L*V24__q_us
    V24__H_mean = V24__RBC_volume/V24__q
    V24__hem_dep_u_rel = 1+(V24__mu_45-1)*(safe_power(1-V24__H_mean, V24__Z)-1)/(safe_power(1-V24__H_global_L, V24__Z)-1)*np.square(2*V24__r*1e6/(2*V24__r*1e6-1.1))
    V24__u_mmHg = V24__u/133.322
    VV_junc13__RBC_volume_init = VV_junc13__H_global_L*VV_junc13__q_us
    VV_junc13__H_mean = VV_junc13__RBC_volume/(VV_junc13__q_us+VV_junc13__div_0)
    VV_junc13__C_max123 = (VV_junc13__C_max12 if VV_junc13__C_max12 > PV25__C else (PV25__C if VV_junc13__C_max12 <= PV25__C else 0.0))
    VV_junc13__C = (VV_junc13__C_max123 if VV_junc13__C_max123 > PV26__C else (PV26__C if VV_junc13__C_max123 <= PV26__C else 0.0))
    PV25__RBC_volume_init = PV25__H_global_L*PV25__q_us
    PV25__H_mean = PV25__RBC_volume/PV25__q
    PV25__hem_dep_u_rel = 1+(PV25__mu_45-1)*(safe_power(1-PV25__H_mean, PV25__Z)-1)/(safe_power(1-PV25__H_global_L, PV25__Z)-1)*np.square(2*PV25__r*1e6/(2*PV25__r*1e6-1.1))
    PV25__u_mmHg = PV25__u/133.322
    PV26__RBC_volume_init = PV26__H_global_L*PV26__q_us
    PV26__H_mean = PV26__RBC_volume/PV26__q
    PV26__hem_dep_u_rel = 1+(PV26__mu_45-1)*(safe_power(1-PV26__H_mean, PV26__Z)-1)/(safe_power(1-PV26__H_global_L, PV26__Z)-1)*np.square(2*PV26__r*1e6/(2*PV26__r*1e6-1.1))
    PV26__u_mmHg = PV26__u/133.322
    V25__RBC_volume_init = V25__H_global_L*V25__q_us
    V25__H_mean = V25__RBC_volume/V25__q
    V25__hem_dep_u_rel = 1+(V25__mu_45-1)*(safe_power(1-V25__H_mean, V25__Z)-1)/(safe_power(1-V25__H_global_L, V25__Z)-1)*np.square(2*V25__r*1e6/(2*V25__r*1e6-1.1))
    V25__u_mmHg = V25__u/133.322
    V26__RBC_volume_init = V26__H_global_L*V26__q_us
    V26__H_mean = V26__RBC_volume/V26__q
    V26__hem_dep_u_rel = 1+(V26__mu_45-1)*(safe_power(1-V26__H_mean, V26__Z)-1)/(safe_power(1-V26__H_global_L, V26__Z)-1)*np.square(2*V26__r*1e6/(2*V26__r*1e6-1.1))
    V26__u_mmHg = V26__u/133.322
    VV_junc14__RBC_volume_init = VV_junc14__H_global_L*VV_junc14__q_us
    VV_junc14__H_mean = VV_junc14__RBC_volume/(VV_junc14__q_us+VV_junc14__div_0)
    VV_junc14__C_max123 = (VV_junc14__C_max12 if VV_junc14__C_max12 > PV27__C else (PV27__C if VV_junc14__C_max12 <= PV27__C else 0.0))
    VV_junc14__C = (VV_junc14__C_max123 if VV_junc14__C_max123 > PV28__C else (PV28__C if VV_junc14__C_max123 <= PV28__C else 0.0))
    PV27__RBC_volume_init = PV27__H_global_L*PV27__q_us
    PV27__H_mean = PV27__RBC_volume/PV27__q
    PV27__hem_dep_u_rel = 1+(PV27__mu_45-1)*(safe_power(1-PV27__H_mean, PV27__Z)-1)/(safe_power(1-PV27__H_global_L, PV27__Z)-1)*np.square(2*PV27__r*1e6/(2*PV27__r*1e6-1.1))
    PV27__u_mmHg = PV27__u/133.322
    PV28__RBC_volume_init = PV28__H_global_L*PV28__q_us
    PV28__H_mean = PV28__RBC_volume/PV28__q
    PV28__hem_dep_u_rel = 1+(PV28__mu_45-1)*(safe_power(1-PV28__H_mean, PV28__Z)-1)/(safe_power(1-PV28__H_global_L, PV28__Z)-1)*np.square(2*PV28__r*1e6/(2*PV28__r*1e6-1.1))
    PV28__u_mmHg = PV28__u/133.322
    V27__RBC_volume_init = V27__H_global_L*V27__q_us
    V27__H_mean = V27__RBC_volume/V27__q
    V27__hem_dep_u_rel = 1+(V27__mu_45-1)*(safe_power(1-V27__H_mean, V27__Z)-1)/(safe_power(1-V27__H_global_L, V27__Z)-1)*np.square(2*V27__r*1e6/(2*V27__r*1e6-1.1))
    V27__u_mmHg = V27__u/133.322
    V28__RBC_volume_init = V28__H_global_L*V28__q_us
    V28__H_mean = V28__RBC_volume/V28__q
    V28__hem_dep_u_rel = 1+(V28__mu_45-1)*(safe_power(1-V28__H_mean, V28__Z)-1)/(safe_power(1-V28__H_global_L, V28__Z)-1)*np.square(2*V28__r*1e6/(2*V28__r*1e6-1.1))
    V28__u_mmHg = V28__u/133.322
    VV_junc15__RBC_volume_init = VV_junc15__H_global_L*VV_junc15__q_us
    VV_junc15__H_mean = VV_junc15__RBC_volume/(VV_junc15__q_us+VV_junc15__div_0)
    VV_junc15__C_max123 = (VV_junc15__C_max12 if VV_junc15__C_max12 > PV29__C else (PV29__C if VV_junc15__C_max12 <= PV29__C else 0.0))
    VV_junc15__C = (VV_junc15__C_max123 if VV_junc15__C_max123 > PV30__C else (PV30__C if VV_junc15__C_max123 <= PV30__C else 0.0))
    PV29__RBC_volume_init = PV29__H_global_L*PV29__q_us
    PV29__H_mean = PV29__RBC_volume/PV29__q
    PV29__hem_dep_u_rel = 1+(PV29__mu_45-1)*(safe_power(1-PV29__H_mean, PV29__Z)-1)/(safe_power(1-PV29__H_global_L, PV29__Z)-1)*np.square(2*PV29__r*1e6/(2*PV29__r*1e6-1.1))
    PV29__u_mmHg = PV29__u/133.322
    PV30__RBC_volume_init = PV30__H_global_L*PV30__q_us
    PV30__H_mean = PV30__RBC_volume/PV30__q
    PV30__hem_dep_u_rel = 1+(PV30__mu_45-1)*(safe_power(1-PV30__H_mean, PV30__Z)-1)/(safe_power(1-PV30__H_global_L, PV30__Z)-1)*np.square(2*PV30__r*1e6/(2*PV30__r*1e6-1.1))
    PV30__u_mmHg = PV30__u/133.322
    V29__RBC_volume_init = V29__H_global_L*V29__q_us
    V29__H_mean = V29__RBC_volume/V29__q
    V29__hem_dep_u_rel = 1+(V29__mu_45-1)*(safe_power(1-V29__H_mean, V29__Z)-1)/(safe_power(1-V29__H_global_L, V29__Z)-1)*np.square(2*V29__r*1e6/(2*V29__r*1e6-1.1))
    V29__u_mmHg = V29__u/133.322
    V30__RBC_volume_init = V30__H_global_L*V30__q_us
    V30__H_mean = V30__RBC_volume/V30__q
    V30__hem_dep_u_rel = 1+(V30__mu_45-1)*(safe_power(1-V30__H_mean, V30__Z)-1)/(safe_power(1-V30__H_global_L, V30__Z)-1)*np.square(2*V30__r*1e6/(2*V30__r*1e6-1.1))
    V30__u_mmHg = V30__u/133.322
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
    V8__mu = V8__hem_dep_u_rel*V8__mu_plasma
    V8__R = 8*V8__mu*V8__l/(np.pi*safe_power(V8__r, 4))
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
    V10__mu = V10__hem_dep_u_rel*V10__mu_plasma
    V10__R = 8*V10__mu*V10__l/(np.pi*safe_power(V10__r, 4))
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
    V12__mu = V12__hem_dep_u_rel*V12__mu_plasma
    V12__R = 8*V12__mu*V12__l/(np.pi*safe_power(V12__r, 4))
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
    V14__mu = V14__hem_dep_u_rel*V14__mu_plasma
    V14__R = 8*V14__mu*V14__l/(np.pi*safe_power(V14__r, 4))
    VV_junc8__u = VV_junc8__q_C/(VV_junc8__C/2)+VV_junc8__u_ext
    VV_junc8__u_mmHg = VV_junc8__u/133.322
    VV_junc8__u_d = VV_junc8__q_C_d/(VV_junc8__C/2)+VV_junc8__u_ext
    VV_junc8__u_d_mmHg = VV_junc8__u_d/133.322
    PV15__mu = PV15__hem_dep_u_rel*PV15__mu_plasma
    PV15__R = 8*PV15__mu*PV15__l/(np.pi*safe_power(PV15__r, 4))+PV15__R_constriction
    PV15__v = (VV_junc8__u_d-PV15__u)/(PV15__R/2)
    PV15__v_d = (PV15__u-V15__u)/(PV15__R/2)
    PV16__mu = PV16__hem_dep_u_rel*PV16__mu_plasma
    PV16__R = 8*PV16__mu*PV16__l/(np.pi*safe_power(PV16__r, 4))+PV16__R_constriction
    PV16__v = (VV_junc8__u_d-PV16__u)/(PV16__R/2)
    PV16__v_d = (PV16__u-V16__u)/(PV16__R/2)
    V15__mu = V15__hem_dep_u_rel*V15__mu_plasma
    V15__R = 8*V15__mu*V15__l/(np.pi*safe_power(V15__r, 4))
    V15__v = (V15__u-V15__u_out)/V15__R
    V16__mu = V16__hem_dep_u_rel*V16__mu_plasma
    V16__R = 8*V16__mu*V16__l/(np.pi*safe_power(V16__r, 4))
    V16__v = (V16__u-V16__u_out)/V16__R
    VV_junc9__u = VV_junc9__q_C/(VV_junc9__C/2)+VV_junc9__u_ext
    VV_junc9__u_mmHg = VV_junc9__u/133.322
    VV_junc9__u_d = VV_junc9__q_C_d/(VV_junc9__C/2)+VV_junc9__u_ext
    VV_junc9__u_d_mmHg = VV_junc9__u_d/133.322
    PV17__mu = PV17__hem_dep_u_rel*PV17__mu_plasma
    PV17__R = 8*PV17__mu*PV17__l/(np.pi*safe_power(PV17__r, 4))+PV17__R_constriction
    PV17__v = (VV_junc9__u_d-PV17__u)/(PV17__R/2)
    PV17__v_d = (PV17__u-V17__u)/(PV17__R/2)
    PV18__mu = PV18__hem_dep_u_rel*PV18__mu_plasma
    PV18__R = 8*PV18__mu*PV18__l/(np.pi*safe_power(PV18__r, 4))+PV18__R_constriction
    PV18__v = (VV_junc9__u_d-PV18__u)/(PV18__R/2)
    PV18__v_d = (PV18__u-V18__u)/(PV18__R/2)
    V17__mu = V17__hem_dep_u_rel*V17__mu_plasma
    V17__R = 8*V17__mu*V17__l/(np.pi*safe_power(V17__r, 4))
    V17__v = (V17__u-V17__u_out)/V17__R
    V18__mu = V18__hem_dep_u_rel*V18__mu_plasma
    V18__R = 8*V18__mu*V18__l/(np.pi*safe_power(V18__r, 4))
    V18__v = (V18__u-V18__u_out)/V18__R
    VV_junc10__u = VV_junc10__q_C/(VV_junc10__C/2)+VV_junc10__u_ext
    VV_junc10__u_mmHg = VV_junc10__u/133.322
    VV_junc10__u_d = VV_junc10__q_C_d/(VV_junc10__C/2)+VV_junc10__u_ext
    VV_junc10__u_d_mmHg = VV_junc10__u_d/133.322
    PV19__mu = PV19__hem_dep_u_rel*PV19__mu_plasma
    PV19__R = 8*PV19__mu*PV19__l/(np.pi*safe_power(PV19__r, 4))+PV19__R_constriction
    PV19__v = (VV_junc10__u_d-PV19__u)/(PV19__R/2)
    PV19__v_d = (PV19__u-V19__u)/(PV19__R/2)
    PV20__mu = PV20__hem_dep_u_rel*PV20__mu_plasma
    PV20__R = 8*PV20__mu*PV20__l/(np.pi*safe_power(PV20__r, 4))+PV20__R_constriction
    PV20__v = (VV_junc10__u_d-PV20__u)/(PV20__R/2)
    PV20__v_d = (PV20__u-V20__u)/(PV20__R/2)
    V19__mu = V19__hem_dep_u_rel*V19__mu_plasma
    V19__R = 8*V19__mu*V19__l/(np.pi*safe_power(V19__r, 4))
    V19__v = (V19__u-V19__u_out)/V19__R
    V20__mu = V20__hem_dep_u_rel*V20__mu_plasma
    V20__R = 8*V20__mu*V20__l/(np.pi*safe_power(V20__r, 4))
    V20__v = (V20__u-V20__u_out)/V20__R
    VV_junc11__u = VV_junc11__q_C/(VV_junc11__C/2)+VV_junc11__u_ext
    VV_junc11__u_mmHg = VV_junc11__u/133.322
    VV_junc11__u_d = VV_junc11__q_C_d/(VV_junc11__C/2)+VV_junc11__u_ext
    VV_junc11__u_d_mmHg = VV_junc11__u_d/133.322
    PV21__mu = PV21__hem_dep_u_rel*PV21__mu_plasma
    PV21__R = 8*PV21__mu*PV21__l/(np.pi*safe_power(PV21__r, 4))+PV21__R_constriction
    PV21__v = (VV_junc11__u_d-PV21__u)/(PV21__R/2)
    PV21__v_d = (PV21__u-V21__u)/(PV21__R/2)
    PV22__mu = PV22__hem_dep_u_rel*PV22__mu_plasma
    PV22__R = 8*PV22__mu*PV22__l/(np.pi*safe_power(PV22__r, 4))+PV22__R_constriction
    PV22__v = (VV_junc11__u_d-PV22__u)/(PV22__R/2)
    PV22__v_d = (PV22__u-V22__u)/(PV22__R/2)
    V21__mu = V21__hem_dep_u_rel*V21__mu_plasma
    V21__R = 8*V21__mu*V21__l/(np.pi*safe_power(V21__r, 4))
    V21__v = (V21__u-V21__u_out)/V21__R
    V22__mu = V22__hem_dep_u_rel*V22__mu_plasma
    V22__R = 8*V22__mu*V22__l/(np.pi*safe_power(V22__r, 4))
    V22__v = (V22__u-V22__u_out)/V22__R
    VV_junc12__u = VV_junc12__q_C/(VV_junc12__C/2)+VV_junc12__u_ext
    VV_junc12__u_mmHg = VV_junc12__u/133.322
    VV_junc12__u_d = VV_junc12__q_C_d/(VV_junc12__C/2)+VV_junc12__u_ext
    VV_junc12__u_d_mmHg = VV_junc12__u_d/133.322
    PV23__mu = PV23__hem_dep_u_rel*PV23__mu_plasma
    PV23__R = 8*PV23__mu*PV23__l/(np.pi*safe_power(PV23__r, 4))+PV23__R_constriction
    PV23__v = (VV_junc12__u_d-PV23__u)/(PV23__R/2)
    PV23__v_d = (PV23__u-V23__u)/(PV23__R/2)
    PV24__mu = PV24__hem_dep_u_rel*PV24__mu_plasma
    PV24__R = 8*PV24__mu*PV24__l/(np.pi*safe_power(PV24__r, 4))+PV24__R_constriction
    PV24__v = (VV_junc12__u_d-PV24__u)/(PV24__R/2)
    PV24__v_d = (PV24__u-V24__u)/(PV24__R/2)
    V23__mu = V23__hem_dep_u_rel*V23__mu_plasma
    V23__R = 8*V23__mu*V23__l/(np.pi*safe_power(V23__r, 4))
    V23__v = (V23__u-V23__u_out)/V23__R
    V24__mu = V24__hem_dep_u_rel*V24__mu_plasma
    V24__R = 8*V24__mu*V24__l/(np.pi*safe_power(V24__r, 4))
    V24__v = (V24__u-V24__u_out)/V24__R
    VV_junc13__u = VV_junc13__q_C/(VV_junc13__C/2)+VV_junc13__u_ext
    VV_junc13__u_mmHg = VV_junc13__u/133.322
    VV_junc13__u_d = VV_junc13__q_C_d/(VV_junc13__C/2)+VV_junc13__u_ext
    VV_junc13__u_d_mmHg = VV_junc13__u_d/133.322
    PV25__mu = PV25__hem_dep_u_rel*PV25__mu_plasma
    PV25__R = 8*PV25__mu*PV25__l/(np.pi*safe_power(PV25__r, 4))+PV25__R_constriction
    PV25__v = (VV_junc13__u_d-PV25__u)/(PV25__R/2)
    PV25__v_d = (PV25__u-V25__u)/(PV25__R/2)
    PV26__mu = PV26__hem_dep_u_rel*PV26__mu_plasma
    PV26__R = 8*PV26__mu*PV26__l/(np.pi*safe_power(PV26__r, 4))+PV26__R_constriction
    PV26__v = (VV_junc13__u_d-PV26__u)/(PV26__R/2)
    PV26__v_d = (PV26__u-V26__u)/(PV26__R/2)
    V25__mu = V25__hem_dep_u_rel*V25__mu_plasma
    V25__R = 8*V25__mu*V25__l/(np.pi*safe_power(V25__r, 4))
    V25__v = (V25__u-V25__u_out)/V25__R
    V26__mu = V26__hem_dep_u_rel*V26__mu_plasma
    V26__R = 8*V26__mu*V26__l/(np.pi*safe_power(V26__r, 4))
    V26__v = (V26__u-V26__u_out)/V26__R
    VV_junc14__u = VV_junc14__q_C/(VV_junc14__C/2)+VV_junc14__u_ext
    VV_junc14__u_mmHg = VV_junc14__u/133.322
    VV_junc14__u_d = VV_junc14__q_C_d/(VV_junc14__C/2)+VV_junc14__u_ext
    VV_junc14__u_d_mmHg = VV_junc14__u_d/133.322
    PV27__mu = PV27__hem_dep_u_rel*PV27__mu_plasma
    PV27__R = 8*PV27__mu*PV27__l/(np.pi*safe_power(PV27__r, 4))+PV27__R_constriction
    PV27__v = (VV_junc14__u_d-PV27__u)/(PV27__R/2)
    PV27__v_d = (PV27__u-V27__u)/(PV27__R/2)
    PV28__mu = PV28__hem_dep_u_rel*PV28__mu_plasma
    PV28__R = 8*PV28__mu*PV28__l/(np.pi*safe_power(PV28__r, 4))+PV28__R_constriction
    PV28__v = (VV_junc14__u_d-PV28__u)/(PV28__R/2)
    PV28__v_d = (PV28__u-V28__u)/(PV28__R/2)
    V27__mu = V27__hem_dep_u_rel*V27__mu_plasma
    V27__R = 8*V27__mu*V27__l/(np.pi*safe_power(V27__r, 4))
    V27__v = (V27__u-V27__u_out)/V27__R
    V28__mu = V28__hem_dep_u_rel*V28__mu_plasma
    V28__R = 8*V28__mu*V28__l/(np.pi*safe_power(V28__r, 4))
    V28__v = (V28__u-V28__u_out)/V28__R
    VV_junc15__u = VV_junc15__q_C/(VV_junc15__C/2)+VV_junc15__u_ext
    VV_junc15__u_mmHg = VV_junc15__u/133.322
    VV_junc15__u_d = VV_junc15__q_C_d/(VV_junc15__C/2)+VV_junc15__u_ext
    VV_junc15__u_d_mmHg = VV_junc15__u_d/133.322
    PV29__mu = PV29__hem_dep_u_rel*PV29__mu_plasma
    PV29__R = 8*PV29__mu*PV29__l/(np.pi*safe_power(PV29__r, 4))+PV29__R_constriction
    PV29__v = (VV_junc15__u_d-PV29__u)/(PV29__R/2)
    PV29__v_d = (PV29__u-V29__u)/(PV29__R/2)
    PV30__mu = PV30__hem_dep_u_rel*PV30__mu_plasma
    PV30__R = 8*PV30__mu*PV30__l/(np.pi*safe_power(PV30__r, 4))+PV30__R_constriction
    PV30__v = (VV_junc15__u_d-PV30__u)/(PV30__R/2)
    PV30__v_d = (PV30__u-V30__u)/(PV30__R/2)
    V29__mu = V29__hem_dep_u_rel*V29__mu_plasma
    V29__R = 8*V29__mu*V29__l/(np.pi*safe_power(V29__r, 4))
    V29__v = (V29__u-V29__u_out)/V29__R
    V30__mu = V30__hem_dep_u_rel*V30__mu_plasma
    V30__R = 8*V30__mu*V30__l/(np.pi*safe_power(V30__r, 4))
    V30__v = (V30__u-V30__u_out)/V30__R
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
    V7__v = (V7__u-VV_junc8__u)/V7__R
    V8__v = (V8__u-VV_junc9__u)/V8__R
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
    V9__v = (V9__u-VV_junc10__u)/V9__R
    V10__v = (V10__u-VV_junc11__u)/V10__R
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
    V11__v = (V11__u-VV_junc12__u)/V11__R
    V12__v = (V12__u-VV_junc13__u)/V12__R
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
    V13__v = (V13__u-VV_junc14__u)/V13__R
    V14__v = (V14__u-VV_junc15__u)/V14__R
    VV_junc8__vj1 = V7__v
    VV_junc8__vj3 = -PV15__v
    VV_junc8__vj4 = -PV16__v
    VV_junc8__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc8__vj1/VV_junc8__v_scale)
    VV_junc8__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc8__vj3/VV_junc8__v_scale)
    VV_junc8__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc8__vj4/VV_junc8__v_scale)
    VV_junc8__w_out1 = 1-VV_junc8__w_in1
    VV_junc8__w_out3 = 1-VV_junc8__w_in3
    VV_junc8__w_out4 = 1-VV_junc8__w_in4
    VV_junc8__Qin1 = VV_junc8__w_in1*VV_junc8__vj1
    VV_junc8__Qin3 = VV_junc8__w_in3*VV_junc8__vj3
    VV_junc8__Qin4 = VV_junc8__w_in4*VV_junc8__vj4
    VV_junc8__Qout1 = VV_junc8__w_out1*-VV_junc8__vj1
    VV_junc8__Qout3 = VV_junc8__w_out3*-VV_junc8__vj3
    VV_junc8__Qout4 = VV_junc8__w_out4*-VV_junc8__vj4
    VV_junc8__Qin_tot = VV_junc8__Qin1+VV_junc8__Qin2+VV_junc8__Qin3+VV_junc8__Qin4
    VV_junc8__Qout_tot = VV_junc8__Qout1+VV_junc8__Qout2+VV_junc8__Qout3+VV_junc8__Qout4
    VV_junc8__v = (VV_junc8__u-VV_junc8__u_d)/VV_junc8__R_VV_junc
    VV_junc8__bc1_is_in = (1 if VV_junc8__Qin1 > VV_junc8__v_threshold else 0)
    VV_junc8__bc3_is_in = (1 if VV_junc8__Qin3 > VV_junc8__v_threshold else 0)
    VV_junc8__bc4_is_in = (1 if VV_junc8__Qin4 > VV_junc8__v_threshold else 0)
    VV_junc8__bc1_is_out = (1 if VV_junc8__Qout1 > VV_junc8__v_threshold else 0)
    VV_junc8__bc3_is_out = (1 if VV_junc8__Qout3 > VV_junc8__v_threshold else 0)
    VV_junc8__bc4_is_out = (1 if VV_junc8__Qout4 > VV_junc8__v_threshold else 0)
    PV15__w_v = 0.5+1/np.pi*np.arctan(PV15__v/PV15__v_scale)
    PV15__w_v_d = 0.5+1/np.pi*np.arctan(PV15__v_d/PV15__v_scale)
    PV15__H_up = PV15__w_v_d*PV15__H_L_in+(1-PV15__w_v_d)*PV15__H_R_in
    PV15__s_v_d = np.abs(PV15__v_d)/(np.abs(PV15__v_d)+PV15__v_eps)
    PV15__H_L_out = (1-PV15__w_v_d)*PV15__H_down+PV15__w_v_d*PV15__H_L_in
    PV15__H_R_out = PV15__w_v_d*PV15__H_down+(1-PV15__w_v_d)*PV15__H_R_in
    PV15__v_pos = PV15__w_v*PV15__v
    PV15__v_neg = (1-PV15__w_v)*-PV15__v
    PV15__v_d_pos = PV15__w_v_d*PV15__v_d
    PV15__v_d_neg = (1-PV15__w_v_d)*-PV15__v_d
    PV15__H_volume_L = PV15__w_v*PV15__H_L_in+(1-PV15__w_v)*PV15__H_L_out
    PV15__H_volume_R = PV15__w_v_d*PV15__H_R_out+(1-PV15__w_v_d)*PV15__H_R_in
    PV15__v_mm3_s = PV15__v/PV15__one_mm3
    PV15__v_d_mm3_s = PV15__v_d/PV15__one_mm3
    PV16__w_v = 0.5+1/np.pi*np.arctan(PV16__v/PV16__v_scale)
    PV16__w_v_d = 0.5+1/np.pi*np.arctan(PV16__v_d/PV16__v_scale)
    PV16__H_up = PV16__w_v_d*PV16__H_L_in+(1-PV16__w_v_d)*PV16__H_R_in
    PV16__s_v_d = np.abs(PV16__v_d)/(np.abs(PV16__v_d)+PV16__v_eps)
    PV16__H_L_out = (1-PV16__w_v_d)*PV16__H_down+PV16__w_v_d*PV16__H_L_in
    PV16__H_R_out = PV16__w_v_d*PV16__H_down+(1-PV16__w_v_d)*PV16__H_R_in
    PV16__v_pos = PV16__w_v*PV16__v
    PV16__v_neg = (1-PV16__w_v)*-PV16__v
    PV16__v_d_pos = PV16__w_v_d*PV16__v_d
    PV16__v_d_neg = (1-PV16__w_v_d)*-PV16__v_d
    PV16__H_volume_L = PV16__w_v*PV16__H_L_in+(1-PV16__w_v)*PV16__H_L_out
    PV16__H_volume_R = PV16__w_v_d*PV16__H_R_out+(1-PV16__w_v_d)*PV16__H_R_in
    PV16__v_mm3_s = PV16__v/PV16__one_mm3
    PV16__v_d_mm3_s = PV16__v_d/PV16__one_mm3
    V15__w_v = 0.5+1/np.pi*np.arctan(V15__v/V15__v_scale)
    V15__H_up = V15__w_v*V15__H_L_in+(1-V15__w_v)*V15__H_R_in
    V15__s_v = np.abs(V15__v)/(np.abs(V15__v)+V15__v_eps)
    V15__H_L_out = (1-V15__w_v)*V15__H_down+V15__w_v*V15__H_L_in
    V15__H_R_out = V15__w_v*V15__H_down+(1-V15__w_v)*V15__H_R_in
    V15__v_pos = V15__w_v*V15__v
    V15__v_neg = (1-V15__w_v)*-V15__v
    V15__H_volume_L = V15__w_v*V15__H_L_in+(1-V15__w_v)*V15__H_L_out
    V15__H_volume_R = V15__w_v*V15__H_R_out+(1-V15__w_v)*V15__H_R_in
    V15__v_mm3_s = V15__v/V15__one_mm3
    V16__w_v = 0.5+1/np.pi*np.arctan(V16__v/V16__v_scale)
    V16__H_up = V16__w_v*V16__H_L_in+(1-V16__w_v)*V16__H_R_in
    V16__s_v = np.abs(V16__v)/(np.abs(V16__v)+V16__v_eps)
    V16__H_L_out = (1-V16__w_v)*V16__H_down+V16__w_v*V16__H_L_in
    V16__H_R_out = V16__w_v*V16__H_down+(1-V16__w_v)*V16__H_R_in
    V16__v_pos = V16__w_v*V16__v
    V16__v_neg = (1-V16__w_v)*-V16__v
    V16__H_volume_L = V16__w_v*V16__H_L_in+(1-V16__w_v)*V16__H_L_out
    V16__H_volume_R = V16__w_v*V16__H_R_out+(1-V16__w_v)*V16__H_R_in
    V16__v_mm3_s = V16__v/V16__one_mm3
    VV_junc9__vj1 = V8__v
    VV_junc9__vj3 = -PV17__v
    VV_junc9__vj4 = -PV18__v
    VV_junc9__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc9__vj1/VV_junc9__v_scale)
    VV_junc9__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc9__vj3/VV_junc9__v_scale)
    VV_junc9__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc9__vj4/VV_junc9__v_scale)
    VV_junc9__w_out1 = 1-VV_junc9__w_in1
    VV_junc9__w_out3 = 1-VV_junc9__w_in3
    VV_junc9__w_out4 = 1-VV_junc9__w_in4
    VV_junc9__Qin1 = VV_junc9__w_in1*VV_junc9__vj1
    VV_junc9__Qin3 = VV_junc9__w_in3*VV_junc9__vj3
    VV_junc9__Qin4 = VV_junc9__w_in4*VV_junc9__vj4
    VV_junc9__Qout1 = VV_junc9__w_out1*-VV_junc9__vj1
    VV_junc9__Qout3 = VV_junc9__w_out3*-VV_junc9__vj3
    VV_junc9__Qout4 = VV_junc9__w_out4*-VV_junc9__vj4
    VV_junc9__Qin_tot = VV_junc9__Qin1+VV_junc9__Qin2+VV_junc9__Qin3+VV_junc9__Qin4
    VV_junc9__Qout_tot = VV_junc9__Qout1+VV_junc9__Qout2+VV_junc9__Qout3+VV_junc9__Qout4
    VV_junc9__v = (VV_junc9__u-VV_junc9__u_d)/VV_junc9__R_VV_junc
    VV_junc9__bc1_is_in = (1 if VV_junc9__Qin1 > VV_junc9__v_threshold else 0)
    VV_junc9__bc3_is_in = (1 if VV_junc9__Qin3 > VV_junc9__v_threshold else 0)
    VV_junc9__bc4_is_in = (1 if VV_junc9__Qin4 > VV_junc9__v_threshold else 0)
    VV_junc9__bc1_is_out = (1 if VV_junc9__Qout1 > VV_junc9__v_threshold else 0)
    VV_junc9__bc3_is_out = (1 if VV_junc9__Qout3 > VV_junc9__v_threshold else 0)
    VV_junc9__bc4_is_out = (1 if VV_junc9__Qout4 > VV_junc9__v_threshold else 0)
    PV17__w_v = 0.5+1/np.pi*np.arctan(PV17__v/PV17__v_scale)
    PV17__w_v_d = 0.5+1/np.pi*np.arctan(PV17__v_d/PV17__v_scale)
    PV17__H_up = PV17__w_v_d*PV17__H_L_in+(1-PV17__w_v_d)*PV17__H_R_in
    PV17__s_v_d = np.abs(PV17__v_d)/(np.abs(PV17__v_d)+PV17__v_eps)
    PV17__H_L_out = (1-PV17__w_v_d)*PV17__H_down+PV17__w_v_d*PV17__H_L_in
    PV17__H_R_out = PV17__w_v_d*PV17__H_down+(1-PV17__w_v_d)*PV17__H_R_in
    PV17__v_pos = PV17__w_v*PV17__v
    PV17__v_neg = (1-PV17__w_v)*-PV17__v
    PV17__v_d_pos = PV17__w_v_d*PV17__v_d
    PV17__v_d_neg = (1-PV17__w_v_d)*-PV17__v_d
    PV17__H_volume_L = PV17__w_v*PV17__H_L_in+(1-PV17__w_v)*PV17__H_L_out
    PV17__H_volume_R = PV17__w_v_d*PV17__H_R_out+(1-PV17__w_v_d)*PV17__H_R_in
    PV17__v_mm3_s = PV17__v/PV17__one_mm3
    PV17__v_d_mm3_s = PV17__v_d/PV17__one_mm3
    PV18__w_v = 0.5+1/np.pi*np.arctan(PV18__v/PV18__v_scale)
    PV18__w_v_d = 0.5+1/np.pi*np.arctan(PV18__v_d/PV18__v_scale)
    PV18__H_up = PV18__w_v_d*PV18__H_L_in+(1-PV18__w_v_d)*PV18__H_R_in
    PV18__s_v_d = np.abs(PV18__v_d)/(np.abs(PV18__v_d)+PV18__v_eps)
    PV18__H_L_out = (1-PV18__w_v_d)*PV18__H_down+PV18__w_v_d*PV18__H_L_in
    PV18__H_R_out = PV18__w_v_d*PV18__H_down+(1-PV18__w_v_d)*PV18__H_R_in
    PV18__v_pos = PV18__w_v*PV18__v
    PV18__v_neg = (1-PV18__w_v)*-PV18__v
    PV18__v_d_pos = PV18__w_v_d*PV18__v_d
    PV18__v_d_neg = (1-PV18__w_v_d)*-PV18__v_d
    PV18__H_volume_L = PV18__w_v*PV18__H_L_in+(1-PV18__w_v)*PV18__H_L_out
    PV18__H_volume_R = PV18__w_v_d*PV18__H_R_out+(1-PV18__w_v_d)*PV18__H_R_in
    PV18__v_mm3_s = PV18__v/PV18__one_mm3
    PV18__v_d_mm3_s = PV18__v_d/PV18__one_mm3
    V17__w_v = 0.5+1/np.pi*np.arctan(V17__v/V17__v_scale)
    V17__H_up = V17__w_v*V17__H_L_in+(1-V17__w_v)*V17__H_R_in
    V17__s_v = np.abs(V17__v)/(np.abs(V17__v)+V17__v_eps)
    V17__H_L_out = (1-V17__w_v)*V17__H_down+V17__w_v*V17__H_L_in
    V17__H_R_out = V17__w_v*V17__H_down+(1-V17__w_v)*V17__H_R_in
    V17__v_pos = V17__w_v*V17__v
    V17__v_neg = (1-V17__w_v)*-V17__v
    V17__H_volume_L = V17__w_v*V17__H_L_in+(1-V17__w_v)*V17__H_L_out
    V17__H_volume_R = V17__w_v*V17__H_R_out+(1-V17__w_v)*V17__H_R_in
    V17__v_mm3_s = V17__v/V17__one_mm3
    V18__w_v = 0.5+1/np.pi*np.arctan(V18__v/V18__v_scale)
    V18__H_up = V18__w_v*V18__H_L_in+(1-V18__w_v)*V18__H_R_in
    V18__s_v = np.abs(V18__v)/(np.abs(V18__v)+V18__v_eps)
    V18__H_L_out = (1-V18__w_v)*V18__H_down+V18__w_v*V18__H_L_in
    V18__H_R_out = V18__w_v*V18__H_down+(1-V18__w_v)*V18__H_R_in
    V18__v_pos = V18__w_v*V18__v
    V18__v_neg = (1-V18__w_v)*-V18__v
    V18__H_volume_L = V18__w_v*V18__H_L_in+(1-V18__w_v)*V18__H_L_out
    V18__H_volume_R = V18__w_v*V18__H_R_out+(1-V18__w_v)*V18__H_R_in
    V18__v_mm3_s = V18__v/V18__one_mm3
    VV_junc10__vj1 = V9__v
    VV_junc10__vj3 = -PV19__v
    VV_junc10__vj4 = -PV20__v
    VV_junc10__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc10__vj1/VV_junc10__v_scale)
    VV_junc10__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc10__vj3/VV_junc10__v_scale)
    VV_junc10__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc10__vj4/VV_junc10__v_scale)
    VV_junc10__w_out1 = 1-VV_junc10__w_in1
    VV_junc10__w_out3 = 1-VV_junc10__w_in3
    VV_junc10__w_out4 = 1-VV_junc10__w_in4
    VV_junc10__Qin1 = VV_junc10__w_in1*VV_junc10__vj1
    VV_junc10__Qin3 = VV_junc10__w_in3*VV_junc10__vj3
    VV_junc10__Qin4 = VV_junc10__w_in4*VV_junc10__vj4
    VV_junc10__Qout1 = VV_junc10__w_out1*-VV_junc10__vj1
    VV_junc10__Qout3 = VV_junc10__w_out3*-VV_junc10__vj3
    VV_junc10__Qout4 = VV_junc10__w_out4*-VV_junc10__vj4
    VV_junc10__Qin_tot = VV_junc10__Qin1+VV_junc10__Qin2+VV_junc10__Qin3+VV_junc10__Qin4
    VV_junc10__Qout_tot = VV_junc10__Qout1+VV_junc10__Qout2+VV_junc10__Qout3+VV_junc10__Qout4
    VV_junc10__v = (VV_junc10__u-VV_junc10__u_d)/VV_junc10__R_VV_junc
    VV_junc10__bc1_is_in = (1 if VV_junc10__Qin1 > VV_junc10__v_threshold else 0)
    VV_junc10__bc3_is_in = (1 if VV_junc10__Qin3 > VV_junc10__v_threshold else 0)
    VV_junc10__bc4_is_in = (1 if VV_junc10__Qin4 > VV_junc10__v_threshold else 0)
    VV_junc10__bc1_is_out = (1 if VV_junc10__Qout1 > VV_junc10__v_threshold else 0)
    VV_junc10__bc3_is_out = (1 if VV_junc10__Qout3 > VV_junc10__v_threshold else 0)
    VV_junc10__bc4_is_out = (1 if VV_junc10__Qout4 > VV_junc10__v_threshold else 0)
    PV19__w_v = 0.5+1/np.pi*np.arctan(PV19__v/PV19__v_scale)
    PV19__w_v_d = 0.5+1/np.pi*np.arctan(PV19__v_d/PV19__v_scale)
    PV19__H_up = PV19__w_v_d*PV19__H_L_in+(1-PV19__w_v_d)*PV19__H_R_in
    PV19__s_v_d = np.abs(PV19__v_d)/(np.abs(PV19__v_d)+PV19__v_eps)
    PV19__H_L_out = (1-PV19__w_v_d)*PV19__H_down+PV19__w_v_d*PV19__H_L_in
    PV19__H_R_out = PV19__w_v_d*PV19__H_down+(1-PV19__w_v_d)*PV19__H_R_in
    PV19__v_pos = PV19__w_v*PV19__v
    PV19__v_neg = (1-PV19__w_v)*-PV19__v
    PV19__v_d_pos = PV19__w_v_d*PV19__v_d
    PV19__v_d_neg = (1-PV19__w_v_d)*-PV19__v_d
    PV19__H_volume_L = PV19__w_v*PV19__H_L_in+(1-PV19__w_v)*PV19__H_L_out
    PV19__H_volume_R = PV19__w_v_d*PV19__H_R_out+(1-PV19__w_v_d)*PV19__H_R_in
    PV19__v_mm3_s = PV19__v/PV19__one_mm3
    PV19__v_d_mm3_s = PV19__v_d/PV19__one_mm3
    PV20__w_v = 0.5+1/np.pi*np.arctan(PV20__v/PV20__v_scale)
    PV20__w_v_d = 0.5+1/np.pi*np.arctan(PV20__v_d/PV20__v_scale)
    PV20__H_up = PV20__w_v_d*PV20__H_L_in+(1-PV20__w_v_d)*PV20__H_R_in
    PV20__s_v_d = np.abs(PV20__v_d)/(np.abs(PV20__v_d)+PV20__v_eps)
    PV20__H_L_out = (1-PV20__w_v_d)*PV20__H_down+PV20__w_v_d*PV20__H_L_in
    PV20__H_R_out = PV20__w_v_d*PV20__H_down+(1-PV20__w_v_d)*PV20__H_R_in
    PV20__v_pos = PV20__w_v*PV20__v
    PV20__v_neg = (1-PV20__w_v)*-PV20__v
    PV20__v_d_pos = PV20__w_v_d*PV20__v_d
    PV20__v_d_neg = (1-PV20__w_v_d)*-PV20__v_d
    PV20__H_volume_L = PV20__w_v*PV20__H_L_in+(1-PV20__w_v)*PV20__H_L_out
    PV20__H_volume_R = PV20__w_v_d*PV20__H_R_out+(1-PV20__w_v_d)*PV20__H_R_in
    PV20__v_mm3_s = PV20__v/PV20__one_mm3
    PV20__v_d_mm3_s = PV20__v_d/PV20__one_mm3
    V19__w_v = 0.5+1/np.pi*np.arctan(V19__v/V19__v_scale)
    V19__H_up = V19__w_v*V19__H_L_in+(1-V19__w_v)*V19__H_R_in
    V19__s_v = np.abs(V19__v)/(np.abs(V19__v)+V19__v_eps)
    V19__H_L_out = (1-V19__w_v)*V19__H_down+V19__w_v*V19__H_L_in
    V19__H_R_out = V19__w_v*V19__H_down+(1-V19__w_v)*V19__H_R_in
    V19__v_pos = V19__w_v*V19__v
    V19__v_neg = (1-V19__w_v)*-V19__v
    V19__H_volume_L = V19__w_v*V19__H_L_in+(1-V19__w_v)*V19__H_L_out
    V19__H_volume_R = V19__w_v*V19__H_R_out+(1-V19__w_v)*V19__H_R_in
    V19__v_mm3_s = V19__v/V19__one_mm3
    V20__w_v = 0.5+1/np.pi*np.arctan(V20__v/V20__v_scale)
    V20__H_up = V20__w_v*V20__H_L_in+(1-V20__w_v)*V20__H_R_in
    V20__s_v = np.abs(V20__v)/(np.abs(V20__v)+V20__v_eps)
    V20__H_L_out = (1-V20__w_v)*V20__H_down+V20__w_v*V20__H_L_in
    V20__H_R_out = V20__w_v*V20__H_down+(1-V20__w_v)*V20__H_R_in
    V20__v_pos = V20__w_v*V20__v
    V20__v_neg = (1-V20__w_v)*-V20__v
    V20__H_volume_L = V20__w_v*V20__H_L_in+(1-V20__w_v)*V20__H_L_out
    V20__H_volume_R = V20__w_v*V20__H_R_out+(1-V20__w_v)*V20__H_R_in
    V20__v_mm3_s = V20__v/V20__one_mm3
    VV_junc11__vj1 = V10__v
    VV_junc11__vj3 = -PV21__v
    VV_junc11__vj4 = -PV22__v
    VV_junc11__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc11__vj1/VV_junc11__v_scale)
    VV_junc11__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc11__vj3/VV_junc11__v_scale)
    VV_junc11__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc11__vj4/VV_junc11__v_scale)
    VV_junc11__w_out1 = 1-VV_junc11__w_in1
    VV_junc11__w_out3 = 1-VV_junc11__w_in3
    VV_junc11__w_out4 = 1-VV_junc11__w_in4
    VV_junc11__Qin1 = VV_junc11__w_in1*VV_junc11__vj1
    VV_junc11__Qin3 = VV_junc11__w_in3*VV_junc11__vj3
    VV_junc11__Qin4 = VV_junc11__w_in4*VV_junc11__vj4
    VV_junc11__Qout1 = VV_junc11__w_out1*-VV_junc11__vj1
    VV_junc11__Qout3 = VV_junc11__w_out3*-VV_junc11__vj3
    VV_junc11__Qout4 = VV_junc11__w_out4*-VV_junc11__vj4
    VV_junc11__Qin_tot = VV_junc11__Qin1+VV_junc11__Qin2+VV_junc11__Qin3+VV_junc11__Qin4
    VV_junc11__Qout_tot = VV_junc11__Qout1+VV_junc11__Qout2+VV_junc11__Qout3+VV_junc11__Qout4
    VV_junc11__v = (VV_junc11__u-VV_junc11__u_d)/VV_junc11__R_VV_junc
    VV_junc11__bc1_is_in = (1 if VV_junc11__Qin1 > VV_junc11__v_threshold else 0)
    VV_junc11__bc3_is_in = (1 if VV_junc11__Qin3 > VV_junc11__v_threshold else 0)
    VV_junc11__bc4_is_in = (1 if VV_junc11__Qin4 > VV_junc11__v_threshold else 0)
    VV_junc11__bc1_is_out = (1 if VV_junc11__Qout1 > VV_junc11__v_threshold else 0)
    VV_junc11__bc3_is_out = (1 if VV_junc11__Qout3 > VV_junc11__v_threshold else 0)
    VV_junc11__bc4_is_out = (1 if VV_junc11__Qout4 > VV_junc11__v_threshold else 0)
    PV21__w_v = 0.5+1/np.pi*np.arctan(PV21__v/PV21__v_scale)
    PV21__w_v_d = 0.5+1/np.pi*np.arctan(PV21__v_d/PV21__v_scale)
    PV21__H_up = PV21__w_v_d*PV21__H_L_in+(1-PV21__w_v_d)*PV21__H_R_in
    PV21__s_v_d = np.abs(PV21__v_d)/(np.abs(PV21__v_d)+PV21__v_eps)
    PV21__H_L_out = (1-PV21__w_v_d)*PV21__H_down+PV21__w_v_d*PV21__H_L_in
    PV21__H_R_out = PV21__w_v_d*PV21__H_down+(1-PV21__w_v_d)*PV21__H_R_in
    PV21__v_pos = PV21__w_v*PV21__v
    PV21__v_neg = (1-PV21__w_v)*-PV21__v
    PV21__v_d_pos = PV21__w_v_d*PV21__v_d
    PV21__v_d_neg = (1-PV21__w_v_d)*-PV21__v_d
    PV21__H_volume_L = PV21__w_v*PV21__H_L_in+(1-PV21__w_v)*PV21__H_L_out
    PV21__H_volume_R = PV21__w_v_d*PV21__H_R_out+(1-PV21__w_v_d)*PV21__H_R_in
    PV21__v_mm3_s = PV21__v/PV21__one_mm3
    PV21__v_d_mm3_s = PV21__v_d/PV21__one_mm3
    PV22__w_v = 0.5+1/np.pi*np.arctan(PV22__v/PV22__v_scale)
    PV22__w_v_d = 0.5+1/np.pi*np.arctan(PV22__v_d/PV22__v_scale)
    PV22__H_up = PV22__w_v_d*PV22__H_L_in+(1-PV22__w_v_d)*PV22__H_R_in
    PV22__s_v_d = np.abs(PV22__v_d)/(np.abs(PV22__v_d)+PV22__v_eps)
    PV22__H_L_out = (1-PV22__w_v_d)*PV22__H_down+PV22__w_v_d*PV22__H_L_in
    PV22__H_R_out = PV22__w_v_d*PV22__H_down+(1-PV22__w_v_d)*PV22__H_R_in
    PV22__v_pos = PV22__w_v*PV22__v
    PV22__v_neg = (1-PV22__w_v)*-PV22__v
    PV22__v_d_pos = PV22__w_v_d*PV22__v_d
    PV22__v_d_neg = (1-PV22__w_v_d)*-PV22__v_d
    PV22__H_volume_L = PV22__w_v*PV22__H_L_in+(1-PV22__w_v)*PV22__H_L_out
    PV22__H_volume_R = PV22__w_v_d*PV22__H_R_out+(1-PV22__w_v_d)*PV22__H_R_in
    PV22__v_mm3_s = PV22__v/PV22__one_mm3
    PV22__v_d_mm3_s = PV22__v_d/PV22__one_mm3
    V21__w_v = 0.5+1/np.pi*np.arctan(V21__v/V21__v_scale)
    V21__H_up = V21__w_v*V21__H_L_in+(1-V21__w_v)*V21__H_R_in
    V21__s_v = np.abs(V21__v)/(np.abs(V21__v)+V21__v_eps)
    V21__H_L_out = (1-V21__w_v)*V21__H_down+V21__w_v*V21__H_L_in
    V21__H_R_out = V21__w_v*V21__H_down+(1-V21__w_v)*V21__H_R_in
    V21__v_pos = V21__w_v*V21__v
    V21__v_neg = (1-V21__w_v)*-V21__v
    V21__H_volume_L = V21__w_v*V21__H_L_in+(1-V21__w_v)*V21__H_L_out
    V21__H_volume_R = V21__w_v*V21__H_R_out+(1-V21__w_v)*V21__H_R_in
    V21__v_mm3_s = V21__v/V21__one_mm3
    V22__w_v = 0.5+1/np.pi*np.arctan(V22__v/V22__v_scale)
    V22__H_up = V22__w_v*V22__H_L_in+(1-V22__w_v)*V22__H_R_in
    V22__s_v = np.abs(V22__v)/(np.abs(V22__v)+V22__v_eps)
    V22__H_L_out = (1-V22__w_v)*V22__H_down+V22__w_v*V22__H_L_in
    V22__H_R_out = V22__w_v*V22__H_down+(1-V22__w_v)*V22__H_R_in
    V22__v_pos = V22__w_v*V22__v
    V22__v_neg = (1-V22__w_v)*-V22__v
    V22__H_volume_L = V22__w_v*V22__H_L_in+(1-V22__w_v)*V22__H_L_out
    V22__H_volume_R = V22__w_v*V22__H_R_out+(1-V22__w_v)*V22__H_R_in
    V22__v_mm3_s = V22__v/V22__one_mm3
    VV_junc12__vj1 = V11__v
    VV_junc12__vj3 = -PV23__v
    VV_junc12__vj4 = -PV24__v
    VV_junc12__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc12__vj1/VV_junc12__v_scale)
    VV_junc12__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc12__vj3/VV_junc12__v_scale)
    VV_junc12__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc12__vj4/VV_junc12__v_scale)
    VV_junc12__w_out1 = 1-VV_junc12__w_in1
    VV_junc12__w_out3 = 1-VV_junc12__w_in3
    VV_junc12__w_out4 = 1-VV_junc12__w_in4
    VV_junc12__Qin1 = VV_junc12__w_in1*VV_junc12__vj1
    VV_junc12__Qin3 = VV_junc12__w_in3*VV_junc12__vj3
    VV_junc12__Qin4 = VV_junc12__w_in4*VV_junc12__vj4
    VV_junc12__Qout1 = VV_junc12__w_out1*-VV_junc12__vj1
    VV_junc12__Qout3 = VV_junc12__w_out3*-VV_junc12__vj3
    VV_junc12__Qout4 = VV_junc12__w_out4*-VV_junc12__vj4
    VV_junc12__Qin_tot = VV_junc12__Qin1+VV_junc12__Qin2+VV_junc12__Qin3+VV_junc12__Qin4
    VV_junc12__Qout_tot = VV_junc12__Qout1+VV_junc12__Qout2+VV_junc12__Qout3+VV_junc12__Qout4
    VV_junc12__v = (VV_junc12__u-VV_junc12__u_d)/VV_junc12__R_VV_junc
    VV_junc12__bc1_is_in = (1 if VV_junc12__Qin1 > VV_junc12__v_threshold else 0)
    VV_junc12__bc3_is_in = (1 if VV_junc12__Qin3 > VV_junc12__v_threshold else 0)
    VV_junc12__bc4_is_in = (1 if VV_junc12__Qin4 > VV_junc12__v_threshold else 0)
    VV_junc12__bc1_is_out = (1 if VV_junc12__Qout1 > VV_junc12__v_threshold else 0)
    VV_junc12__bc3_is_out = (1 if VV_junc12__Qout3 > VV_junc12__v_threshold else 0)
    VV_junc12__bc4_is_out = (1 if VV_junc12__Qout4 > VV_junc12__v_threshold else 0)
    PV23__w_v = 0.5+1/np.pi*np.arctan(PV23__v/PV23__v_scale)
    PV23__w_v_d = 0.5+1/np.pi*np.arctan(PV23__v_d/PV23__v_scale)
    PV23__H_up = PV23__w_v_d*PV23__H_L_in+(1-PV23__w_v_d)*PV23__H_R_in
    PV23__s_v_d = np.abs(PV23__v_d)/(np.abs(PV23__v_d)+PV23__v_eps)
    PV23__H_L_out = (1-PV23__w_v_d)*PV23__H_down+PV23__w_v_d*PV23__H_L_in
    PV23__H_R_out = PV23__w_v_d*PV23__H_down+(1-PV23__w_v_d)*PV23__H_R_in
    PV23__v_pos = PV23__w_v*PV23__v
    PV23__v_neg = (1-PV23__w_v)*-PV23__v
    PV23__v_d_pos = PV23__w_v_d*PV23__v_d
    PV23__v_d_neg = (1-PV23__w_v_d)*-PV23__v_d
    PV23__H_volume_L = PV23__w_v*PV23__H_L_in+(1-PV23__w_v)*PV23__H_L_out
    PV23__H_volume_R = PV23__w_v_d*PV23__H_R_out+(1-PV23__w_v_d)*PV23__H_R_in
    PV23__v_mm3_s = PV23__v/PV23__one_mm3
    PV23__v_d_mm3_s = PV23__v_d/PV23__one_mm3
    PV24__w_v = 0.5+1/np.pi*np.arctan(PV24__v/PV24__v_scale)
    PV24__w_v_d = 0.5+1/np.pi*np.arctan(PV24__v_d/PV24__v_scale)
    PV24__H_up = PV24__w_v_d*PV24__H_L_in+(1-PV24__w_v_d)*PV24__H_R_in
    PV24__s_v_d = np.abs(PV24__v_d)/(np.abs(PV24__v_d)+PV24__v_eps)
    PV24__H_L_out = (1-PV24__w_v_d)*PV24__H_down+PV24__w_v_d*PV24__H_L_in
    PV24__H_R_out = PV24__w_v_d*PV24__H_down+(1-PV24__w_v_d)*PV24__H_R_in
    PV24__v_pos = PV24__w_v*PV24__v
    PV24__v_neg = (1-PV24__w_v)*-PV24__v
    PV24__v_d_pos = PV24__w_v_d*PV24__v_d
    PV24__v_d_neg = (1-PV24__w_v_d)*-PV24__v_d
    PV24__H_volume_L = PV24__w_v*PV24__H_L_in+(1-PV24__w_v)*PV24__H_L_out
    PV24__H_volume_R = PV24__w_v_d*PV24__H_R_out+(1-PV24__w_v_d)*PV24__H_R_in
    PV24__v_mm3_s = PV24__v/PV24__one_mm3
    PV24__v_d_mm3_s = PV24__v_d/PV24__one_mm3
    V23__w_v = 0.5+1/np.pi*np.arctan(V23__v/V23__v_scale)
    V23__H_up = V23__w_v*V23__H_L_in+(1-V23__w_v)*V23__H_R_in
    V23__s_v = np.abs(V23__v)/(np.abs(V23__v)+V23__v_eps)
    V23__H_L_out = (1-V23__w_v)*V23__H_down+V23__w_v*V23__H_L_in
    V23__H_R_out = V23__w_v*V23__H_down+(1-V23__w_v)*V23__H_R_in
    V23__v_pos = V23__w_v*V23__v
    V23__v_neg = (1-V23__w_v)*-V23__v
    V23__H_volume_L = V23__w_v*V23__H_L_in+(1-V23__w_v)*V23__H_L_out
    V23__H_volume_R = V23__w_v*V23__H_R_out+(1-V23__w_v)*V23__H_R_in
    V23__v_mm3_s = V23__v/V23__one_mm3
    V24__w_v = 0.5+1/np.pi*np.arctan(V24__v/V24__v_scale)
    V24__H_up = V24__w_v*V24__H_L_in+(1-V24__w_v)*V24__H_R_in
    V24__s_v = np.abs(V24__v)/(np.abs(V24__v)+V24__v_eps)
    V24__H_L_out = (1-V24__w_v)*V24__H_down+V24__w_v*V24__H_L_in
    V24__H_R_out = V24__w_v*V24__H_down+(1-V24__w_v)*V24__H_R_in
    V24__v_pos = V24__w_v*V24__v
    V24__v_neg = (1-V24__w_v)*-V24__v
    V24__H_volume_L = V24__w_v*V24__H_L_in+(1-V24__w_v)*V24__H_L_out
    V24__H_volume_R = V24__w_v*V24__H_R_out+(1-V24__w_v)*V24__H_R_in
    V24__v_mm3_s = V24__v/V24__one_mm3
    VV_junc13__vj1 = V12__v
    VV_junc13__vj3 = -PV25__v
    VV_junc13__vj4 = -PV26__v
    VV_junc13__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc13__vj1/VV_junc13__v_scale)
    VV_junc13__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc13__vj3/VV_junc13__v_scale)
    VV_junc13__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc13__vj4/VV_junc13__v_scale)
    VV_junc13__w_out1 = 1-VV_junc13__w_in1
    VV_junc13__w_out3 = 1-VV_junc13__w_in3
    VV_junc13__w_out4 = 1-VV_junc13__w_in4
    VV_junc13__Qin1 = VV_junc13__w_in1*VV_junc13__vj1
    VV_junc13__Qin3 = VV_junc13__w_in3*VV_junc13__vj3
    VV_junc13__Qin4 = VV_junc13__w_in4*VV_junc13__vj4
    VV_junc13__Qout1 = VV_junc13__w_out1*-VV_junc13__vj1
    VV_junc13__Qout3 = VV_junc13__w_out3*-VV_junc13__vj3
    VV_junc13__Qout4 = VV_junc13__w_out4*-VV_junc13__vj4
    VV_junc13__Qin_tot = VV_junc13__Qin1+VV_junc13__Qin2+VV_junc13__Qin3+VV_junc13__Qin4
    VV_junc13__Qout_tot = VV_junc13__Qout1+VV_junc13__Qout2+VV_junc13__Qout3+VV_junc13__Qout4
    VV_junc13__v = (VV_junc13__u-VV_junc13__u_d)/VV_junc13__R_VV_junc
    VV_junc13__bc1_is_in = (1 if VV_junc13__Qin1 > VV_junc13__v_threshold else 0)
    VV_junc13__bc3_is_in = (1 if VV_junc13__Qin3 > VV_junc13__v_threshold else 0)
    VV_junc13__bc4_is_in = (1 if VV_junc13__Qin4 > VV_junc13__v_threshold else 0)
    VV_junc13__bc1_is_out = (1 if VV_junc13__Qout1 > VV_junc13__v_threshold else 0)
    VV_junc13__bc3_is_out = (1 if VV_junc13__Qout3 > VV_junc13__v_threshold else 0)
    VV_junc13__bc4_is_out = (1 if VV_junc13__Qout4 > VV_junc13__v_threshold else 0)
    PV25__w_v = 0.5+1/np.pi*np.arctan(PV25__v/PV25__v_scale)
    PV25__w_v_d = 0.5+1/np.pi*np.arctan(PV25__v_d/PV25__v_scale)
    PV25__H_up = PV25__w_v_d*PV25__H_L_in+(1-PV25__w_v_d)*PV25__H_R_in
    PV25__s_v_d = np.abs(PV25__v_d)/(np.abs(PV25__v_d)+PV25__v_eps)
    PV25__H_L_out = (1-PV25__w_v_d)*PV25__H_down+PV25__w_v_d*PV25__H_L_in
    PV25__H_R_out = PV25__w_v_d*PV25__H_down+(1-PV25__w_v_d)*PV25__H_R_in
    PV25__v_pos = PV25__w_v*PV25__v
    PV25__v_neg = (1-PV25__w_v)*-PV25__v
    PV25__v_d_pos = PV25__w_v_d*PV25__v_d
    PV25__v_d_neg = (1-PV25__w_v_d)*-PV25__v_d
    PV25__H_volume_L = PV25__w_v*PV25__H_L_in+(1-PV25__w_v)*PV25__H_L_out
    PV25__H_volume_R = PV25__w_v_d*PV25__H_R_out+(1-PV25__w_v_d)*PV25__H_R_in
    PV25__v_mm3_s = PV25__v/PV25__one_mm3
    PV25__v_d_mm3_s = PV25__v_d/PV25__one_mm3
    PV26__w_v = 0.5+1/np.pi*np.arctan(PV26__v/PV26__v_scale)
    PV26__w_v_d = 0.5+1/np.pi*np.arctan(PV26__v_d/PV26__v_scale)
    PV26__H_up = PV26__w_v_d*PV26__H_L_in+(1-PV26__w_v_d)*PV26__H_R_in
    PV26__s_v_d = np.abs(PV26__v_d)/(np.abs(PV26__v_d)+PV26__v_eps)
    PV26__H_L_out = (1-PV26__w_v_d)*PV26__H_down+PV26__w_v_d*PV26__H_L_in
    PV26__H_R_out = PV26__w_v_d*PV26__H_down+(1-PV26__w_v_d)*PV26__H_R_in
    PV26__v_pos = PV26__w_v*PV26__v
    PV26__v_neg = (1-PV26__w_v)*-PV26__v
    PV26__v_d_pos = PV26__w_v_d*PV26__v_d
    PV26__v_d_neg = (1-PV26__w_v_d)*-PV26__v_d
    PV26__H_volume_L = PV26__w_v*PV26__H_L_in+(1-PV26__w_v)*PV26__H_L_out
    PV26__H_volume_R = PV26__w_v_d*PV26__H_R_out+(1-PV26__w_v_d)*PV26__H_R_in
    PV26__v_mm3_s = PV26__v/PV26__one_mm3
    PV26__v_d_mm3_s = PV26__v_d/PV26__one_mm3
    V25__w_v = 0.5+1/np.pi*np.arctan(V25__v/V25__v_scale)
    V25__H_up = V25__w_v*V25__H_L_in+(1-V25__w_v)*V25__H_R_in
    V25__s_v = np.abs(V25__v)/(np.abs(V25__v)+V25__v_eps)
    V25__H_L_out = (1-V25__w_v)*V25__H_down+V25__w_v*V25__H_L_in
    V25__H_R_out = V25__w_v*V25__H_down+(1-V25__w_v)*V25__H_R_in
    V25__v_pos = V25__w_v*V25__v
    V25__v_neg = (1-V25__w_v)*-V25__v
    V25__H_volume_L = V25__w_v*V25__H_L_in+(1-V25__w_v)*V25__H_L_out
    V25__H_volume_R = V25__w_v*V25__H_R_out+(1-V25__w_v)*V25__H_R_in
    V25__v_mm3_s = V25__v/V25__one_mm3
    V26__w_v = 0.5+1/np.pi*np.arctan(V26__v/V26__v_scale)
    V26__H_up = V26__w_v*V26__H_L_in+(1-V26__w_v)*V26__H_R_in
    V26__s_v = np.abs(V26__v)/(np.abs(V26__v)+V26__v_eps)
    V26__H_L_out = (1-V26__w_v)*V26__H_down+V26__w_v*V26__H_L_in
    V26__H_R_out = V26__w_v*V26__H_down+(1-V26__w_v)*V26__H_R_in
    V26__v_pos = V26__w_v*V26__v
    V26__v_neg = (1-V26__w_v)*-V26__v
    V26__H_volume_L = V26__w_v*V26__H_L_in+(1-V26__w_v)*V26__H_L_out
    V26__H_volume_R = V26__w_v*V26__H_R_out+(1-V26__w_v)*V26__H_R_in
    V26__v_mm3_s = V26__v/V26__one_mm3
    VV_junc14__vj1 = V13__v
    VV_junc14__vj3 = -PV27__v
    VV_junc14__vj4 = -PV28__v
    VV_junc14__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc14__vj1/VV_junc14__v_scale)
    VV_junc14__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc14__vj3/VV_junc14__v_scale)
    VV_junc14__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc14__vj4/VV_junc14__v_scale)
    VV_junc14__w_out1 = 1-VV_junc14__w_in1
    VV_junc14__w_out3 = 1-VV_junc14__w_in3
    VV_junc14__w_out4 = 1-VV_junc14__w_in4
    VV_junc14__Qin1 = VV_junc14__w_in1*VV_junc14__vj1
    VV_junc14__Qin3 = VV_junc14__w_in3*VV_junc14__vj3
    VV_junc14__Qin4 = VV_junc14__w_in4*VV_junc14__vj4
    VV_junc14__Qout1 = VV_junc14__w_out1*-VV_junc14__vj1
    VV_junc14__Qout3 = VV_junc14__w_out3*-VV_junc14__vj3
    VV_junc14__Qout4 = VV_junc14__w_out4*-VV_junc14__vj4
    VV_junc14__Qin_tot = VV_junc14__Qin1+VV_junc14__Qin2+VV_junc14__Qin3+VV_junc14__Qin4
    VV_junc14__Qout_tot = VV_junc14__Qout1+VV_junc14__Qout2+VV_junc14__Qout3+VV_junc14__Qout4
    VV_junc14__v = (VV_junc14__u-VV_junc14__u_d)/VV_junc14__R_VV_junc
    VV_junc14__bc1_is_in = (1 if VV_junc14__Qin1 > VV_junc14__v_threshold else 0)
    VV_junc14__bc3_is_in = (1 if VV_junc14__Qin3 > VV_junc14__v_threshold else 0)
    VV_junc14__bc4_is_in = (1 if VV_junc14__Qin4 > VV_junc14__v_threshold else 0)
    VV_junc14__bc1_is_out = (1 if VV_junc14__Qout1 > VV_junc14__v_threshold else 0)
    VV_junc14__bc3_is_out = (1 if VV_junc14__Qout3 > VV_junc14__v_threshold else 0)
    VV_junc14__bc4_is_out = (1 if VV_junc14__Qout4 > VV_junc14__v_threshold else 0)
    PV27__w_v = 0.5+1/np.pi*np.arctan(PV27__v/PV27__v_scale)
    PV27__w_v_d = 0.5+1/np.pi*np.arctan(PV27__v_d/PV27__v_scale)
    PV27__H_up = PV27__w_v_d*PV27__H_L_in+(1-PV27__w_v_d)*PV27__H_R_in
    PV27__s_v_d = np.abs(PV27__v_d)/(np.abs(PV27__v_d)+PV27__v_eps)
    PV27__H_L_out = (1-PV27__w_v_d)*PV27__H_down+PV27__w_v_d*PV27__H_L_in
    PV27__H_R_out = PV27__w_v_d*PV27__H_down+(1-PV27__w_v_d)*PV27__H_R_in
    PV27__v_pos = PV27__w_v*PV27__v
    PV27__v_neg = (1-PV27__w_v)*-PV27__v
    PV27__v_d_pos = PV27__w_v_d*PV27__v_d
    PV27__v_d_neg = (1-PV27__w_v_d)*-PV27__v_d
    PV27__H_volume_L = PV27__w_v*PV27__H_L_in+(1-PV27__w_v)*PV27__H_L_out
    PV27__H_volume_R = PV27__w_v_d*PV27__H_R_out+(1-PV27__w_v_d)*PV27__H_R_in
    PV27__v_mm3_s = PV27__v/PV27__one_mm3
    PV27__v_d_mm3_s = PV27__v_d/PV27__one_mm3
    PV28__w_v = 0.5+1/np.pi*np.arctan(PV28__v/PV28__v_scale)
    PV28__w_v_d = 0.5+1/np.pi*np.arctan(PV28__v_d/PV28__v_scale)
    PV28__H_up = PV28__w_v_d*PV28__H_L_in+(1-PV28__w_v_d)*PV28__H_R_in
    PV28__s_v_d = np.abs(PV28__v_d)/(np.abs(PV28__v_d)+PV28__v_eps)
    PV28__H_L_out = (1-PV28__w_v_d)*PV28__H_down+PV28__w_v_d*PV28__H_L_in
    PV28__H_R_out = PV28__w_v_d*PV28__H_down+(1-PV28__w_v_d)*PV28__H_R_in
    PV28__v_pos = PV28__w_v*PV28__v
    PV28__v_neg = (1-PV28__w_v)*-PV28__v
    PV28__v_d_pos = PV28__w_v_d*PV28__v_d
    PV28__v_d_neg = (1-PV28__w_v_d)*-PV28__v_d
    PV28__H_volume_L = PV28__w_v*PV28__H_L_in+(1-PV28__w_v)*PV28__H_L_out
    PV28__H_volume_R = PV28__w_v_d*PV28__H_R_out+(1-PV28__w_v_d)*PV28__H_R_in
    PV28__v_mm3_s = PV28__v/PV28__one_mm3
    PV28__v_d_mm3_s = PV28__v_d/PV28__one_mm3
    V27__w_v = 0.5+1/np.pi*np.arctan(V27__v/V27__v_scale)
    V27__H_up = V27__w_v*V27__H_L_in+(1-V27__w_v)*V27__H_R_in
    V27__s_v = np.abs(V27__v)/(np.abs(V27__v)+V27__v_eps)
    V27__H_L_out = (1-V27__w_v)*V27__H_down+V27__w_v*V27__H_L_in
    V27__H_R_out = V27__w_v*V27__H_down+(1-V27__w_v)*V27__H_R_in
    V27__v_pos = V27__w_v*V27__v
    V27__v_neg = (1-V27__w_v)*-V27__v
    V27__H_volume_L = V27__w_v*V27__H_L_in+(1-V27__w_v)*V27__H_L_out
    V27__H_volume_R = V27__w_v*V27__H_R_out+(1-V27__w_v)*V27__H_R_in
    V27__v_mm3_s = V27__v/V27__one_mm3
    V28__w_v = 0.5+1/np.pi*np.arctan(V28__v/V28__v_scale)
    V28__H_up = V28__w_v*V28__H_L_in+(1-V28__w_v)*V28__H_R_in
    V28__s_v = np.abs(V28__v)/(np.abs(V28__v)+V28__v_eps)
    V28__H_L_out = (1-V28__w_v)*V28__H_down+V28__w_v*V28__H_L_in
    V28__H_R_out = V28__w_v*V28__H_down+(1-V28__w_v)*V28__H_R_in
    V28__v_pos = V28__w_v*V28__v
    V28__v_neg = (1-V28__w_v)*-V28__v
    V28__H_volume_L = V28__w_v*V28__H_L_in+(1-V28__w_v)*V28__H_L_out
    V28__H_volume_R = V28__w_v*V28__H_R_out+(1-V28__w_v)*V28__H_R_in
    V28__v_mm3_s = V28__v/V28__one_mm3
    VV_junc15__vj1 = V14__v
    VV_junc15__vj3 = -PV29__v
    VV_junc15__vj4 = -PV30__v
    VV_junc15__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc15__vj1/VV_junc15__v_scale)
    VV_junc15__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc15__vj3/VV_junc15__v_scale)
    VV_junc15__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc15__vj4/VV_junc15__v_scale)
    VV_junc15__w_out1 = 1-VV_junc15__w_in1
    VV_junc15__w_out3 = 1-VV_junc15__w_in3
    VV_junc15__w_out4 = 1-VV_junc15__w_in4
    VV_junc15__Qin1 = VV_junc15__w_in1*VV_junc15__vj1
    VV_junc15__Qin3 = VV_junc15__w_in3*VV_junc15__vj3
    VV_junc15__Qin4 = VV_junc15__w_in4*VV_junc15__vj4
    VV_junc15__Qout1 = VV_junc15__w_out1*-VV_junc15__vj1
    VV_junc15__Qout3 = VV_junc15__w_out3*-VV_junc15__vj3
    VV_junc15__Qout4 = VV_junc15__w_out4*-VV_junc15__vj4
    VV_junc15__Qin_tot = VV_junc15__Qin1+VV_junc15__Qin2+VV_junc15__Qin3+VV_junc15__Qin4
    VV_junc15__Qout_tot = VV_junc15__Qout1+VV_junc15__Qout2+VV_junc15__Qout3+VV_junc15__Qout4
    VV_junc15__v = (VV_junc15__u-VV_junc15__u_d)/VV_junc15__R_VV_junc
    VV_junc15__bc1_is_in = (1 if VV_junc15__Qin1 > VV_junc15__v_threshold else 0)
    VV_junc15__bc3_is_in = (1 if VV_junc15__Qin3 > VV_junc15__v_threshold else 0)
    VV_junc15__bc4_is_in = (1 if VV_junc15__Qin4 > VV_junc15__v_threshold else 0)
    VV_junc15__bc1_is_out = (1 if VV_junc15__Qout1 > VV_junc15__v_threshold else 0)
    VV_junc15__bc3_is_out = (1 if VV_junc15__Qout3 > VV_junc15__v_threshold else 0)
    VV_junc15__bc4_is_out = (1 if VV_junc15__Qout4 > VV_junc15__v_threshold else 0)
    PV29__w_v = 0.5+1/np.pi*np.arctan(PV29__v/PV29__v_scale)
    PV29__w_v_d = 0.5+1/np.pi*np.arctan(PV29__v_d/PV29__v_scale)
    PV29__H_up = PV29__w_v_d*PV29__H_L_in+(1-PV29__w_v_d)*PV29__H_R_in
    PV29__s_v_d = np.abs(PV29__v_d)/(np.abs(PV29__v_d)+PV29__v_eps)
    PV29__H_L_out = (1-PV29__w_v_d)*PV29__H_down+PV29__w_v_d*PV29__H_L_in
    PV29__H_R_out = PV29__w_v_d*PV29__H_down+(1-PV29__w_v_d)*PV29__H_R_in
    PV29__v_pos = PV29__w_v*PV29__v
    PV29__v_neg = (1-PV29__w_v)*-PV29__v
    PV29__v_d_pos = PV29__w_v_d*PV29__v_d
    PV29__v_d_neg = (1-PV29__w_v_d)*-PV29__v_d
    PV29__H_volume_L = PV29__w_v*PV29__H_L_in+(1-PV29__w_v)*PV29__H_L_out
    PV29__H_volume_R = PV29__w_v_d*PV29__H_R_out+(1-PV29__w_v_d)*PV29__H_R_in
    PV29__v_mm3_s = PV29__v/PV29__one_mm3
    PV29__v_d_mm3_s = PV29__v_d/PV29__one_mm3
    PV30__w_v = 0.5+1/np.pi*np.arctan(PV30__v/PV30__v_scale)
    PV30__w_v_d = 0.5+1/np.pi*np.arctan(PV30__v_d/PV30__v_scale)
    PV30__H_up = PV30__w_v_d*PV30__H_L_in+(1-PV30__w_v_d)*PV30__H_R_in
    PV30__s_v_d = np.abs(PV30__v_d)/(np.abs(PV30__v_d)+PV30__v_eps)
    PV30__H_L_out = (1-PV30__w_v_d)*PV30__H_down+PV30__w_v_d*PV30__H_L_in
    PV30__H_R_out = PV30__w_v_d*PV30__H_down+(1-PV30__w_v_d)*PV30__H_R_in
    PV30__v_pos = PV30__w_v*PV30__v
    PV30__v_neg = (1-PV30__w_v)*-PV30__v
    PV30__v_d_pos = PV30__w_v_d*PV30__v_d
    PV30__v_d_neg = (1-PV30__w_v_d)*-PV30__v_d
    PV30__H_volume_L = PV30__w_v*PV30__H_L_in+(1-PV30__w_v)*PV30__H_L_out
    PV30__H_volume_R = PV30__w_v_d*PV30__H_R_out+(1-PV30__w_v_d)*PV30__H_R_in
    PV30__v_mm3_s = PV30__v/PV30__one_mm3
    PV30__v_d_mm3_s = PV30__v_d/PV30__one_mm3
    V29__w_v = 0.5+1/np.pi*np.arctan(V29__v/V29__v_scale)
    V29__H_up = V29__w_v*V29__H_L_in+(1-V29__w_v)*V29__H_R_in
    V29__s_v = np.abs(V29__v)/(np.abs(V29__v)+V29__v_eps)
    V29__H_L_out = (1-V29__w_v)*V29__H_down+V29__w_v*V29__H_L_in
    V29__H_R_out = V29__w_v*V29__H_down+(1-V29__w_v)*V29__H_R_in
    V29__v_pos = V29__w_v*V29__v
    V29__v_neg = (1-V29__w_v)*-V29__v
    V29__H_volume_L = V29__w_v*V29__H_L_in+(1-V29__w_v)*V29__H_L_out
    V29__H_volume_R = V29__w_v*V29__H_R_out+(1-V29__w_v)*V29__H_R_in
    V29__v_mm3_s = V29__v/V29__one_mm3
    V30__w_v = 0.5+1/np.pi*np.arctan(V30__v/V30__v_scale)
    V30__H_up = V30__w_v*V30__H_L_in+(1-V30__w_v)*V30__H_R_in
    V30__s_v = np.abs(V30__v)/(np.abs(V30__v)+V30__v_eps)
    V30__H_L_out = (1-V30__w_v)*V30__H_down+V30__w_v*V30__H_L_in
    V30__H_R_out = V30__w_v*V30__H_down+(1-V30__w_v)*V30__H_R_in
    V30__v_pos = V30__w_v*V30__v
    V30__v_neg = (1-V30__w_v)*-V30__v
    V30__H_volume_L = V30__w_v*V30__H_L_in+(1-V30__w_v)*V30__H_L_out
    V30__H_volume_R = V30__w_v*V30__H_R_out+(1-V30__w_v)*V30__H_R_in
    V30__v_mm3_s = V30__v/V30__one_mm3
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
    VV_junc8__n_in = VV_junc8__bc1_is_in+VV_junc8__bc2_is_in+VV_junc8__bc3_is_in+VV_junc8__bc4_is_in
    VV_junc8__n_out = VV_junc8__bc1_is_out+VV_junc8__bc2_is_out+VV_junc8__bc3_is_out+VV_junc8__bc4_is_out
    VV_junc8__RBC_in = VV_junc8__Qin1*V7__H_R_out+VV_junc8__Qin2*VV_junc8__H_to2+VV_junc8__Qin3*PV15__H_L_out+VV_junc8__Qin4*PV16__H_L_out
    VV_junc8__v_mm3_s = VV_junc8__v/VV_junc8__one_mm3
    VV_junc8__junction_type = (1 if VV_junc8__n_in == 1 else (-1 if VV_junc8__n_in >= 2 else 0))
    VV_junc8__is_split = (1 if VV_junc8__junction_type == 1 else 0)
    VV_junc8__is_merge = (1 if VV_junc8__junction_type == -1 else 0)
    VV_junc8__feed1 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin1 >= VV_junc8__Qin2) and (VV_junc8__Qin1 >= VV_junc8__Qin3) and (VV_junc8__Qin1 >= VV_junc8__Qin4) else 0)
    VV_junc8__feed2 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin2 > VV_junc8__Qin1) and (VV_junc8__Qin2 >= VV_junc8__Qin3) and (VV_junc8__Qin2 >= VV_junc8__Qin4) else 0)
    VV_junc8__feed3 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin3 > VV_junc8__Qin1) and (VV_junc8__Qin3 > VV_junc8__Qin2) and (VV_junc8__Qin3 >= VV_junc8__Qin4) else 0)
    VV_junc8__feed4 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin4 > VV_junc8__Qin1) and (VV_junc8__Qin4 > VV_junc8__Qin2) and (VV_junc8__Qin4 > VV_junc8__Qin3) else 0)
    VV_junc8__alpha1 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc1_is_out == 1) and (VV_junc8__Qout1 >= VV_junc8__Qout2) and (VV_junc8__Qout1 >= VV_junc8__Qout3) and (VV_junc8__Qout1 >= VV_junc8__Qout4) else 0)
    VV_junc8__alpha2 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc2_is_out == 1) and (VV_junc8__Qout2 > VV_junc8__Qout1) and (VV_junc8__Qout2 >= VV_junc8__Qout3) and (VV_junc8__Qout2 >= VV_junc8__Qout4) else 0)
    VV_junc8__alpha3 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc3_is_out == 1) and (VV_junc8__Qout3 > VV_junc8__Qout1) and (VV_junc8__Qout3 > VV_junc8__Qout2) and (VV_junc8__Qout3 >= VV_junc8__Qout4) else 0)
    VV_junc8__alpha4 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc4_is_out == 1) and (VV_junc8__Qout4 > VV_junc8__Qout1) and (VV_junc8__Qout4 > VV_junc8__Qout2) and (VV_junc8__Qout4 > VV_junc8__Qout3) else 0)
    VV_junc8__Qout1_rem = (0 if VV_junc8__alpha1 == 1 else VV_junc8__Qout1)
    VV_junc8__Qout2_rem = (0 if VV_junc8__alpha2 == 1 else VV_junc8__Qout2)
    VV_junc8__Qout3_rem = (0 if VV_junc8__alpha3 == 1 else VV_junc8__Qout3)
    VV_junc8__Qout4_rem = (0 if VV_junc8__alpha4 == 1 else VV_junc8__Qout4)
    VV_junc8__beta1 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc1_is_out == 1) and (VV_junc8__alpha1 == 0) and (VV_junc8__Qout1_rem >= VV_junc8__Qout2_rem) and (VV_junc8__Qout1_rem >= VV_junc8__Qout3_rem) and (VV_junc8__Qout1_rem >= VV_junc8__Qout4_rem) else 0)
    VV_junc8__beta2 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc2_is_out == 1) and (VV_junc8__alpha2 == 0) and (VV_junc8__Qout2_rem > VV_junc8__Qout1_rem) and (VV_junc8__Qout2_rem >= VV_junc8__Qout3_rem) and (VV_junc8__Qout2_rem >= VV_junc8__Qout4_rem) else 0)
    VV_junc8__beta3 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc3_is_out == 1) and (VV_junc8__alpha3 == 0) and (VV_junc8__Qout3_rem > VV_junc8__Qout1_rem) and (VV_junc8__Qout3_rem > VV_junc8__Qout2_rem) and (VV_junc8__Qout3_rem >= VV_junc8__Qout4_rem) else 0)
    VV_junc8__beta4 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc4_is_out == 1) and (VV_junc8__alpha4 == 0) and (VV_junc8__Qout4_rem > VV_junc8__Qout1_rem) and (VV_junc8__Qout4_rem > VV_junc8__Qout2_rem) and (VV_junc8__Qout4_rem > VV_junc8__Qout3_rem) else 0)
    VV_junc8__D_F = (VV_junc8__D1 if VV_junc8__feed1 == 1 else (VV_junc8__D2 if VV_junc8__feed2 == 1 else (VV_junc8__D3 if VV_junc8__feed3 == 1 else (VV_junc8__D4 if VV_junc8__feed4 == 1 else VV_junc8__D1))))
    VV_junc8__D_alpha = (VV_junc8__D1 if VV_junc8__alpha1 == 1 else (VV_junc8__D2 if VV_junc8__alpha2 == 1 else (VV_junc8__D3 if VV_junc8__alpha3 == 1 else (VV_junc8__D4 if VV_junc8__alpha4 == 1 else VV_junc8__D3))))
    VV_junc8__D_beta = (VV_junc8__D1 if VV_junc8__beta1 == 1 else (VV_junc8__D2 if VV_junc8__beta2 == 1 else (VV_junc8__D3 if VV_junc8__beta3 == 1 else (VV_junc8__D4 if VV_junc8__beta4 == 1 else VV_junc8__D4))))
    VV_junc8__v_alpha = (VV_junc8__Qout1 if VV_junc8__alpha1 == 1 else (VV_junc8__Qout2 if VV_junc8__alpha2 == 1 else (VV_junc8__Qout3 if VV_junc8__alpha3 == 1 else (VV_junc8__Qout4 if VV_junc8__alpha4 == 1 else 0))))
    VV_junc8__v_beta = (VV_junc8__Qout1 if VV_junc8__beta1 == 1 else (VV_junc8__Qout2 if VV_junc8__beta2 == 1 else (VV_junc8__Qout3 if VV_junc8__beta3 == 1 else (VV_junc8__Qout4 if VV_junc8__beta4 == 1 else 0))))
    PV15__H_down_target = PV15__s_v_d*(PV15__H_mean+PV15__gamma_mirror*(PV15__H_mean-PV15__H_up))+(1-PV15__s_v_d)*PV15__H_mean
    PV16__H_down_target = PV16__s_v_d*(PV16__H_mean+PV16__gamma_mirror*(PV16__H_mean-PV16__H_up))+(1-PV16__s_v_d)*PV16__H_mean
    V15__H_down_target = V15__s_v*(V15__H_mean+V15__gamma_mirror*(V15__H_mean-V15__H_up))+(1-V15__s_v)*V15__H_mean
    V16__H_down_target = V16__s_v*(V16__H_mean+V16__gamma_mirror*(V16__H_mean-V16__H_up))+(1-V16__s_v)*V16__H_mean
    VV_junc9__n_in = VV_junc9__bc1_is_in+VV_junc9__bc2_is_in+VV_junc9__bc3_is_in+VV_junc9__bc4_is_in
    VV_junc9__n_out = VV_junc9__bc1_is_out+VV_junc9__bc2_is_out+VV_junc9__bc3_is_out+VV_junc9__bc4_is_out
    VV_junc9__RBC_in = VV_junc9__Qin1*V8__H_R_out+VV_junc9__Qin2*VV_junc9__H_to2+VV_junc9__Qin3*PV17__H_L_out+VV_junc9__Qin4*PV18__H_L_out
    VV_junc9__v_mm3_s = VV_junc9__v/VV_junc9__one_mm3
    VV_junc9__junction_type = (1 if VV_junc9__n_in == 1 else (-1 if VV_junc9__n_in >= 2 else 0))
    VV_junc9__is_split = (1 if VV_junc9__junction_type == 1 else 0)
    VV_junc9__is_merge = (1 if VV_junc9__junction_type == -1 else 0)
    VV_junc9__feed1 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin1 >= VV_junc9__Qin2) and (VV_junc9__Qin1 >= VV_junc9__Qin3) and (VV_junc9__Qin1 >= VV_junc9__Qin4) else 0)
    VV_junc9__feed2 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin2 > VV_junc9__Qin1) and (VV_junc9__Qin2 >= VV_junc9__Qin3) and (VV_junc9__Qin2 >= VV_junc9__Qin4) else 0)
    VV_junc9__feed3 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin3 > VV_junc9__Qin1) and (VV_junc9__Qin3 > VV_junc9__Qin2) and (VV_junc9__Qin3 >= VV_junc9__Qin4) else 0)
    VV_junc9__feed4 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin4 > VV_junc9__Qin1) and (VV_junc9__Qin4 > VV_junc9__Qin2) and (VV_junc9__Qin4 > VV_junc9__Qin3) else 0)
    VV_junc9__alpha1 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc1_is_out == 1) and (VV_junc9__Qout1 >= VV_junc9__Qout2) and (VV_junc9__Qout1 >= VV_junc9__Qout3) and (VV_junc9__Qout1 >= VV_junc9__Qout4) else 0)
    VV_junc9__alpha2 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc2_is_out == 1) and (VV_junc9__Qout2 > VV_junc9__Qout1) and (VV_junc9__Qout2 >= VV_junc9__Qout3) and (VV_junc9__Qout2 >= VV_junc9__Qout4) else 0)
    VV_junc9__alpha3 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc3_is_out == 1) and (VV_junc9__Qout3 > VV_junc9__Qout1) and (VV_junc9__Qout3 > VV_junc9__Qout2) and (VV_junc9__Qout3 >= VV_junc9__Qout4) else 0)
    VV_junc9__alpha4 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc4_is_out == 1) and (VV_junc9__Qout4 > VV_junc9__Qout1) and (VV_junc9__Qout4 > VV_junc9__Qout2) and (VV_junc9__Qout4 > VV_junc9__Qout3) else 0)
    VV_junc9__Qout1_rem = (0 if VV_junc9__alpha1 == 1 else VV_junc9__Qout1)
    VV_junc9__Qout2_rem = (0 if VV_junc9__alpha2 == 1 else VV_junc9__Qout2)
    VV_junc9__Qout3_rem = (0 if VV_junc9__alpha3 == 1 else VV_junc9__Qout3)
    VV_junc9__Qout4_rem = (0 if VV_junc9__alpha4 == 1 else VV_junc9__Qout4)
    VV_junc9__beta1 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc1_is_out == 1) and (VV_junc9__alpha1 == 0) and (VV_junc9__Qout1_rem >= VV_junc9__Qout2_rem) and (VV_junc9__Qout1_rem >= VV_junc9__Qout3_rem) and (VV_junc9__Qout1_rem >= VV_junc9__Qout4_rem) else 0)
    VV_junc9__beta2 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc2_is_out == 1) and (VV_junc9__alpha2 == 0) and (VV_junc9__Qout2_rem > VV_junc9__Qout1_rem) and (VV_junc9__Qout2_rem >= VV_junc9__Qout3_rem) and (VV_junc9__Qout2_rem >= VV_junc9__Qout4_rem) else 0)
    VV_junc9__beta3 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc3_is_out == 1) and (VV_junc9__alpha3 == 0) and (VV_junc9__Qout3_rem > VV_junc9__Qout1_rem) and (VV_junc9__Qout3_rem > VV_junc9__Qout2_rem) and (VV_junc9__Qout3_rem >= VV_junc9__Qout4_rem) else 0)
    VV_junc9__beta4 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc4_is_out == 1) and (VV_junc9__alpha4 == 0) and (VV_junc9__Qout4_rem > VV_junc9__Qout1_rem) and (VV_junc9__Qout4_rem > VV_junc9__Qout2_rem) and (VV_junc9__Qout4_rem > VV_junc9__Qout3_rem) else 0)
    VV_junc9__D_F = (VV_junc9__D1 if VV_junc9__feed1 == 1 else (VV_junc9__D2 if VV_junc9__feed2 == 1 else (VV_junc9__D3 if VV_junc9__feed3 == 1 else (VV_junc9__D4 if VV_junc9__feed4 == 1 else VV_junc9__D1))))
    VV_junc9__D_alpha = (VV_junc9__D1 if VV_junc9__alpha1 == 1 else (VV_junc9__D2 if VV_junc9__alpha2 == 1 else (VV_junc9__D3 if VV_junc9__alpha3 == 1 else (VV_junc9__D4 if VV_junc9__alpha4 == 1 else VV_junc9__D3))))
    VV_junc9__D_beta = (VV_junc9__D1 if VV_junc9__beta1 == 1 else (VV_junc9__D2 if VV_junc9__beta2 == 1 else (VV_junc9__D3 if VV_junc9__beta3 == 1 else (VV_junc9__D4 if VV_junc9__beta4 == 1 else VV_junc9__D4))))
    VV_junc9__v_alpha = (VV_junc9__Qout1 if VV_junc9__alpha1 == 1 else (VV_junc9__Qout2 if VV_junc9__alpha2 == 1 else (VV_junc9__Qout3 if VV_junc9__alpha3 == 1 else (VV_junc9__Qout4 if VV_junc9__alpha4 == 1 else 0))))
    VV_junc9__v_beta = (VV_junc9__Qout1 if VV_junc9__beta1 == 1 else (VV_junc9__Qout2 if VV_junc9__beta2 == 1 else (VV_junc9__Qout3 if VV_junc9__beta3 == 1 else (VV_junc9__Qout4 if VV_junc9__beta4 == 1 else 0))))
    PV17__H_down_target = PV17__s_v_d*(PV17__H_mean+PV17__gamma_mirror*(PV17__H_mean-PV17__H_up))+(1-PV17__s_v_d)*PV17__H_mean
    PV18__H_down_target = PV18__s_v_d*(PV18__H_mean+PV18__gamma_mirror*(PV18__H_mean-PV18__H_up))+(1-PV18__s_v_d)*PV18__H_mean
    V17__H_down_target = V17__s_v*(V17__H_mean+V17__gamma_mirror*(V17__H_mean-V17__H_up))+(1-V17__s_v)*V17__H_mean
    V18__H_down_target = V18__s_v*(V18__H_mean+V18__gamma_mirror*(V18__H_mean-V18__H_up))+(1-V18__s_v)*V18__H_mean
    VV_junc10__n_in = VV_junc10__bc1_is_in+VV_junc10__bc2_is_in+VV_junc10__bc3_is_in+VV_junc10__bc4_is_in
    VV_junc10__n_out = VV_junc10__bc1_is_out+VV_junc10__bc2_is_out+VV_junc10__bc3_is_out+VV_junc10__bc4_is_out
    VV_junc10__RBC_in = VV_junc10__Qin1*V9__H_R_out+VV_junc10__Qin2*VV_junc10__H_to2+VV_junc10__Qin3*PV19__H_L_out+VV_junc10__Qin4*PV20__H_L_out
    VV_junc10__v_mm3_s = VV_junc10__v/VV_junc10__one_mm3
    VV_junc10__junction_type = (1 if VV_junc10__n_in == 1 else (-1 if VV_junc10__n_in >= 2 else 0))
    VV_junc10__is_split = (1 if VV_junc10__junction_type == 1 else 0)
    VV_junc10__is_merge = (1 if VV_junc10__junction_type == -1 else 0)
    VV_junc10__feed1 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin1 >= VV_junc10__Qin2) and (VV_junc10__Qin1 >= VV_junc10__Qin3) and (VV_junc10__Qin1 >= VV_junc10__Qin4) else 0)
    VV_junc10__feed2 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin2 > VV_junc10__Qin1) and (VV_junc10__Qin2 >= VV_junc10__Qin3) and (VV_junc10__Qin2 >= VV_junc10__Qin4) else 0)
    VV_junc10__feed3 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin3 > VV_junc10__Qin1) and (VV_junc10__Qin3 > VV_junc10__Qin2) and (VV_junc10__Qin3 >= VV_junc10__Qin4) else 0)
    VV_junc10__feed4 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin4 > VV_junc10__Qin1) and (VV_junc10__Qin4 > VV_junc10__Qin2) and (VV_junc10__Qin4 > VV_junc10__Qin3) else 0)
    VV_junc10__alpha1 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc1_is_out == 1) and (VV_junc10__Qout1 >= VV_junc10__Qout2) and (VV_junc10__Qout1 >= VV_junc10__Qout3) and (VV_junc10__Qout1 >= VV_junc10__Qout4) else 0)
    VV_junc10__alpha2 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc2_is_out == 1) and (VV_junc10__Qout2 > VV_junc10__Qout1) and (VV_junc10__Qout2 >= VV_junc10__Qout3) and (VV_junc10__Qout2 >= VV_junc10__Qout4) else 0)
    VV_junc10__alpha3 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc3_is_out == 1) and (VV_junc10__Qout3 > VV_junc10__Qout1) and (VV_junc10__Qout3 > VV_junc10__Qout2) and (VV_junc10__Qout3 >= VV_junc10__Qout4) else 0)
    VV_junc10__alpha4 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc4_is_out == 1) and (VV_junc10__Qout4 > VV_junc10__Qout1) and (VV_junc10__Qout4 > VV_junc10__Qout2) and (VV_junc10__Qout4 > VV_junc10__Qout3) else 0)
    VV_junc10__Qout1_rem = (0 if VV_junc10__alpha1 == 1 else VV_junc10__Qout1)
    VV_junc10__Qout2_rem = (0 if VV_junc10__alpha2 == 1 else VV_junc10__Qout2)
    VV_junc10__Qout3_rem = (0 if VV_junc10__alpha3 == 1 else VV_junc10__Qout3)
    VV_junc10__Qout4_rem = (0 if VV_junc10__alpha4 == 1 else VV_junc10__Qout4)
    VV_junc10__beta1 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc1_is_out == 1) and (VV_junc10__alpha1 == 0) and (VV_junc10__Qout1_rem >= VV_junc10__Qout2_rem) and (VV_junc10__Qout1_rem >= VV_junc10__Qout3_rem) and (VV_junc10__Qout1_rem >= VV_junc10__Qout4_rem) else 0)
    VV_junc10__beta2 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc2_is_out == 1) and (VV_junc10__alpha2 == 0) and (VV_junc10__Qout2_rem > VV_junc10__Qout1_rem) and (VV_junc10__Qout2_rem >= VV_junc10__Qout3_rem) and (VV_junc10__Qout2_rem >= VV_junc10__Qout4_rem) else 0)
    VV_junc10__beta3 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc3_is_out == 1) and (VV_junc10__alpha3 == 0) and (VV_junc10__Qout3_rem > VV_junc10__Qout1_rem) and (VV_junc10__Qout3_rem > VV_junc10__Qout2_rem) and (VV_junc10__Qout3_rem >= VV_junc10__Qout4_rem) else 0)
    VV_junc10__beta4 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc4_is_out == 1) and (VV_junc10__alpha4 == 0) and (VV_junc10__Qout4_rem > VV_junc10__Qout1_rem) and (VV_junc10__Qout4_rem > VV_junc10__Qout2_rem) and (VV_junc10__Qout4_rem > VV_junc10__Qout3_rem) else 0)
    VV_junc10__D_F = (VV_junc10__D1 if VV_junc10__feed1 == 1 else (VV_junc10__D2 if VV_junc10__feed2 == 1 else (VV_junc10__D3 if VV_junc10__feed3 == 1 else (VV_junc10__D4 if VV_junc10__feed4 == 1 else VV_junc10__D1))))
    VV_junc10__D_alpha = (VV_junc10__D1 if VV_junc10__alpha1 == 1 else (VV_junc10__D2 if VV_junc10__alpha2 == 1 else (VV_junc10__D3 if VV_junc10__alpha3 == 1 else (VV_junc10__D4 if VV_junc10__alpha4 == 1 else VV_junc10__D3))))
    VV_junc10__D_beta = (VV_junc10__D1 if VV_junc10__beta1 == 1 else (VV_junc10__D2 if VV_junc10__beta2 == 1 else (VV_junc10__D3 if VV_junc10__beta3 == 1 else (VV_junc10__D4 if VV_junc10__beta4 == 1 else VV_junc10__D4))))
    VV_junc10__v_alpha = (VV_junc10__Qout1 if VV_junc10__alpha1 == 1 else (VV_junc10__Qout2 if VV_junc10__alpha2 == 1 else (VV_junc10__Qout3 if VV_junc10__alpha3 == 1 else (VV_junc10__Qout4 if VV_junc10__alpha4 == 1 else 0))))
    VV_junc10__v_beta = (VV_junc10__Qout1 if VV_junc10__beta1 == 1 else (VV_junc10__Qout2 if VV_junc10__beta2 == 1 else (VV_junc10__Qout3 if VV_junc10__beta3 == 1 else (VV_junc10__Qout4 if VV_junc10__beta4 == 1 else 0))))
    PV19__H_down_target = PV19__s_v_d*(PV19__H_mean+PV19__gamma_mirror*(PV19__H_mean-PV19__H_up))+(1-PV19__s_v_d)*PV19__H_mean
    PV20__H_down_target = PV20__s_v_d*(PV20__H_mean+PV20__gamma_mirror*(PV20__H_mean-PV20__H_up))+(1-PV20__s_v_d)*PV20__H_mean
    V19__H_down_target = V19__s_v*(V19__H_mean+V19__gamma_mirror*(V19__H_mean-V19__H_up))+(1-V19__s_v)*V19__H_mean
    V20__H_down_target = V20__s_v*(V20__H_mean+V20__gamma_mirror*(V20__H_mean-V20__H_up))+(1-V20__s_v)*V20__H_mean
    VV_junc11__n_in = VV_junc11__bc1_is_in+VV_junc11__bc2_is_in+VV_junc11__bc3_is_in+VV_junc11__bc4_is_in
    VV_junc11__n_out = VV_junc11__bc1_is_out+VV_junc11__bc2_is_out+VV_junc11__bc3_is_out+VV_junc11__bc4_is_out
    VV_junc11__RBC_in = VV_junc11__Qin1*V10__H_R_out+VV_junc11__Qin2*VV_junc11__H_to2+VV_junc11__Qin3*PV21__H_L_out+VV_junc11__Qin4*PV22__H_L_out
    VV_junc11__v_mm3_s = VV_junc11__v/VV_junc11__one_mm3
    VV_junc11__junction_type = (1 if VV_junc11__n_in == 1 else (-1 if VV_junc11__n_in >= 2 else 0))
    VV_junc11__is_split = (1 if VV_junc11__junction_type == 1 else 0)
    VV_junc11__is_merge = (1 if VV_junc11__junction_type == -1 else 0)
    VV_junc11__feed1 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin1 >= VV_junc11__Qin2) and (VV_junc11__Qin1 >= VV_junc11__Qin3) and (VV_junc11__Qin1 >= VV_junc11__Qin4) else 0)
    VV_junc11__feed2 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin2 > VV_junc11__Qin1) and (VV_junc11__Qin2 >= VV_junc11__Qin3) and (VV_junc11__Qin2 >= VV_junc11__Qin4) else 0)
    VV_junc11__feed3 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin3 > VV_junc11__Qin1) and (VV_junc11__Qin3 > VV_junc11__Qin2) and (VV_junc11__Qin3 >= VV_junc11__Qin4) else 0)
    VV_junc11__feed4 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin4 > VV_junc11__Qin1) and (VV_junc11__Qin4 > VV_junc11__Qin2) and (VV_junc11__Qin4 > VV_junc11__Qin3) else 0)
    VV_junc11__alpha1 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc1_is_out == 1) and (VV_junc11__Qout1 >= VV_junc11__Qout2) and (VV_junc11__Qout1 >= VV_junc11__Qout3) and (VV_junc11__Qout1 >= VV_junc11__Qout4) else 0)
    VV_junc11__alpha2 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc2_is_out == 1) and (VV_junc11__Qout2 > VV_junc11__Qout1) and (VV_junc11__Qout2 >= VV_junc11__Qout3) and (VV_junc11__Qout2 >= VV_junc11__Qout4) else 0)
    VV_junc11__alpha3 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc3_is_out == 1) and (VV_junc11__Qout3 > VV_junc11__Qout1) and (VV_junc11__Qout3 > VV_junc11__Qout2) and (VV_junc11__Qout3 >= VV_junc11__Qout4) else 0)
    VV_junc11__alpha4 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc4_is_out == 1) and (VV_junc11__Qout4 > VV_junc11__Qout1) and (VV_junc11__Qout4 > VV_junc11__Qout2) and (VV_junc11__Qout4 > VV_junc11__Qout3) else 0)
    VV_junc11__Qout1_rem = (0 if VV_junc11__alpha1 == 1 else VV_junc11__Qout1)
    VV_junc11__Qout2_rem = (0 if VV_junc11__alpha2 == 1 else VV_junc11__Qout2)
    VV_junc11__Qout3_rem = (0 if VV_junc11__alpha3 == 1 else VV_junc11__Qout3)
    VV_junc11__Qout4_rem = (0 if VV_junc11__alpha4 == 1 else VV_junc11__Qout4)
    VV_junc11__beta1 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc1_is_out == 1) and (VV_junc11__alpha1 == 0) and (VV_junc11__Qout1_rem >= VV_junc11__Qout2_rem) and (VV_junc11__Qout1_rem >= VV_junc11__Qout3_rem) and (VV_junc11__Qout1_rem >= VV_junc11__Qout4_rem) else 0)
    VV_junc11__beta2 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc2_is_out == 1) and (VV_junc11__alpha2 == 0) and (VV_junc11__Qout2_rem > VV_junc11__Qout1_rem) and (VV_junc11__Qout2_rem >= VV_junc11__Qout3_rem) and (VV_junc11__Qout2_rem >= VV_junc11__Qout4_rem) else 0)
    VV_junc11__beta3 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc3_is_out == 1) and (VV_junc11__alpha3 == 0) and (VV_junc11__Qout3_rem > VV_junc11__Qout1_rem) and (VV_junc11__Qout3_rem > VV_junc11__Qout2_rem) and (VV_junc11__Qout3_rem >= VV_junc11__Qout4_rem) else 0)
    VV_junc11__beta4 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc4_is_out == 1) and (VV_junc11__alpha4 == 0) and (VV_junc11__Qout4_rem > VV_junc11__Qout1_rem) and (VV_junc11__Qout4_rem > VV_junc11__Qout2_rem) and (VV_junc11__Qout4_rem > VV_junc11__Qout3_rem) else 0)
    VV_junc11__D_F = (VV_junc11__D1 if VV_junc11__feed1 == 1 else (VV_junc11__D2 if VV_junc11__feed2 == 1 else (VV_junc11__D3 if VV_junc11__feed3 == 1 else (VV_junc11__D4 if VV_junc11__feed4 == 1 else VV_junc11__D1))))
    VV_junc11__D_alpha = (VV_junc11__D1 if VV_junc11__alpha1 == 1 else (VV_junc11__D2 if VV_junc11__alpha2 == 1 else (VV_junc11__D3 if VV_junc11__alpha3 == 1 else (VV_junc11__D4 if VV_junc11__alpha4 == 1 else VV_junc11__D3))))
    VV_junc11__D_beta = (VV_junc11__D1 if VV_junc11__beta1 == 1 else (VV_junc11__D2 if VV_junc11__beta2 == 1 else (VV_junc11__D3 if VV_junc11__beta3 == 1 else (VV_junc11__D4 if VV_junc11__beta4 == 1 else VV_junc11__D4))))
    VV_junc11__v_alpha = (VV_junc11__Qout1 if VV_junc11__alpha1 == 1 else (VV_junc11__Qout2 if VV_junc11__alpha2 == 1 else (VV_junc11__Qout3 if VV_junc11__alpha3 == 1 else (VV_junc11__Qout4 if VV_junc11__alpha4 == 1 else 0))))
    VV_junc11__v_beta = (VV_junc11__Qout1 if VV_junc11__beta1 == 1 else (VV_junc11__Qout2 if VV_junc11__beta2 == 1 else (VV_junc11__Qout3 if VV_junc11__beta3 == 1 else (VV_junc11__Qout4 if VV_junc11__beta4 == 1 else 0))))
    PV21__H_down_target = PV21__s_v_d*(PV21__H_mean+PV21__gamma_mirror*(PV21__H_mean-PV21__H_up))+(1-PV21__s_v_d)*PV21__H_mean
    PV22__H_down_target = PV22__s_v_d*(PV22__H_mean+PV22__gamma_mirror*(PV22__H_mean-PV22__H_up))+(1-PV22__s_v_d)*PV22__H_mean
    V21__H_down_target = V21__s_v*(V21__H_mean+V21__gamma_mirror*(V21__H_mean-V21__H_up))+(1-V21__s_v)*V21__H_mean
    V22__H_down_target = V22__s_v*(V22__H_mean+V22__gamma_mirror*(V22__H_mean-V22__H_up))+(1-V22__s_v)*V22__H_mean
    VV_junc12__n_in = VV_junc12__bc1_is_in+VV_junc12__bc2_is_in+VV_junc12__bc3_is_in+VV_junc12__bc4_is_in
    VV_junc12__n_out = VV_junc12__bc1_is_out+VV_junc12__bc2_is_out+VV_junc12__bc3_is_out+VV_junc12__bc4_is_out
    VV_junc12__RBC_in = VV_junc12__Qin1*V11__H_R_out+VV_junc12__Qin2*VV_junc12__H_to2+VV_junc12__Qin3*PV23__H_L_out+VV_junc12__Qin4*PV24__H_L_out
    VV_junc12__v_mm3_s = VV_junc12__v/VV_junc12__one_mm3
    VV_junc12__junction_type = (1 if VV_junc12__n_in == 1 else (-1 if VV_junc12__n_in >= 2 else 0))
    VV_junc12__is_split = (1 if VV_junc12__junction_type == 1 else 0)
    VV_junc12__is_merge = (1 if VV_junc12__junction_type == -1 else 0)
    VV_junc12__feed1 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin1 >= VV_junc12__Qin2) and (VV_junc12__Qin1 >= VV_junc12__Qin3) and (VV_junc12__Qin1 >= VV_junc12__Qin4) else 0)
    VV_junc12__feed2 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin2 > VV_junc12__Qin1) and (VV_junc12__Qin2 >= VV_junc12__Qin3) and (VV_junc12__Qin2 >= VV_junc12__Qin4) else 0)
    VV_junc12__feed3 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin3 > VV_junc12__Qin1) and (VV_junc12__Qin3 > VV_junc12__Qin2) and (VV_junc12__Qin3 >= VV_junc12__Qin4) else 0)
    VV_junc12__feed4 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin4 > VV_junc12__Qin1) and (VV_junc12__Qin4 > VV_junc12__Qin2) and (VV_junc12__Qin4 > VV_junc12__Qin3) else 0)
    VV_junc12__alpha1 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc1_is_out == 1) and (VV_junc12__Qout1 >= VV_junc12__Qout2) and (VV_junc12__Qout1 >= VV_junc12__Qout3) and (VV_junc12__Qout1 >= VV_junc12__Qout4) else 0)
    VV_junc12__alpha2 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc2_is_out == 1) and (VV_junc12__Qout2 > VV_junc12__Qout1) and (VV_junc12__Qout2 >= VV_junc12__Qout3) and (VV_junc12__Qout2 >= VV_junc12__Qout4) else 0)
    VV_junc12__alpha3 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc3_is_out == 1) and (VV_junc12__Qout3 > VV_junc12__Qout1) and (VV_junc12__Qout3 > VV_junc12__Qout2) and (VV_junc12__Qout3 >= VV_junc12__Qout4) else 0)
    VV_junc12__alpha4 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc4_is_out == 1) and (VV_junc12__Qout4 > VV_junc12__Qout1) and (VV_junc12__Qout4 > VV_junc12__Qout2) and (VV_junc12__Qout4 > VV_junc12__Qout3) else 0)
    VV_junc12__Qout1_rem = (0 if VV_junc12__alpha1 == 1 else VV_junc12__Qout1)
    VV_junc12__Qout2_rem = (0 if VV_junc12__alpha2 == 1 else VV_junc12__Qout2)
    VV_junc12__Qout3_rem = (0 if VV_junc12__alpha3 == 1 else VV_junc12__Qout3)
    VV_junc12__Qout4_rem = (0 if VV_junc12__alpha4 == 1 else VV_junc12__Qout4)
    VV_junc12__beta1 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc1_is_out == 1) and (VV_junc12__alpha1 == 0) and (VV_junc12__Qout1_rem >= VV_junc12__Qout2_rem) and (VV_junc12__Qout1_rem >= VV_junc12__Qout3_rem) and (VV_junc12__Qout1_rem >= VV_junc12__Qout4_rem) else 0)
    VV_junc12__beta2 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc2_is_out == 1) and (VV_junc12__alpha2 == 0) and (VV_junc12__Qout2_rem > VV_junc12__Qout1_rem) and (VV_junc12__Qout2_rem >= VV_junc12__Qout3_rem) and (VV_junc12__Qout2_rem >= VV_junc12__Qout4_rem) else 0)
    VV_junc12__beta3 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc3_is_out == 1) and (VV_junc12__alpha3 == 0) and (VV_junc12__Qout3_rem > VV_junc12__Qout1_rem) and (VV_junc12__Qout3_rem > VV_junc12__Qout2_rem) and (VV_junc12__Qout3_rem >= VV_junc12__Qout4_rem) else 0)
    VV_junc12__beta4 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc4_is_out == 1) and (VV_junc12__alpha4 == 0) and (VV_junc12__Qout4_rem > VV_junc12__Qout1_rem) and (VV_junc12__Qout4_rem > VV_junc12__Qout2_rem) and (VV_junc12__Qout4_rem > VV_junc12__Qout3_rem) else 0)
    VV_junc12__D_F = (VV_junc12__D1 if VV_junc12__feed1 == 1 else (VV_junc12__D2 if VV_junc12__feed2 == 1 else (VV_junc12__D3 if VV_junc12__feed3 == 1 else (VV_junc12__D4 if VV_junc12__feed4 == 1 else VV_junc12__D1))))
    VV_junc12__D_alpha = (VV_junc12__D1 if VV_junc12__alpha1 == 1 else (VV_junc12__D2 if VV_junc12__alpha2 == 1 else (VV_junc12__D3 if VV_junc12__alpha3 == 1 else (VV_junc12__D4 if VV_junc12__alpha4 == 1 else VV_junc12__D3))))
    VV_junc12__D_beta = (VV_junc12__D1 if VV_junc12__beta1 == 1 else (VV_junc12__D2 if VV_junc12__beta2 == 1 else (VV_junc12__D3 if VV_junc12__beta3 == 1 else (VV_junc12__D4 if VV_junc12__beta4 == 1 else VV_junc12__D4))))
    VV_junc12__v_alpha = (VV_junc12__Qout1 if VV_junc12__alpha1 == 1 else (VV_junc12__Qout2 if VV_junc12__alpha2 == 1 else (VV_junc12__Qout3 if VV_junc12__alpha3 == 1 else (VV_junc12__Qout4 if VV_junc12__alpha4 == 1 else 0))))
    VV_junc12__v_beta = (VV_junc12__Qout1 if VV_junc12__beta1 == 1 else (VV_junc12__Qout2 if VV_junc12__beta2 == 1 else (VV_junc12__Qout3 if VV_junc12__beta3 == 1 else (VV_junc12__Qout4 if VV_junc12__beta4 == 1 else 0))))
    PV23__H_down_target = PV23__s_v_d*(PV23__H_mean+PV23__gamma_mirror*(PV23__H_mean-PV23__H_up))+(1-PV23__s_v_d)*PV23__H_mean
    PV24__H_down_target = PV24__s_v_d*(PV24__H_mean+PV24__gamma_mirror*(PV24__H_mean-PV24__H_up))+(1-PV24__s_v_d)*PV24__H_mean
    V23__H_down_target = V23__s_v*(V23__H_mean+V23__gamma_mirror*(V23__H_mean-V23__H_up))+(1-V23__s_v)*V23__H_mean
    V24__H_down_target = V24__s_v*(V24__H_mean+V24__gamma_mirror*(V24__H_mean-V24__H_up))+(1-V24__s_v)*V24__H_mean
    VV_junc13__n_in = VV_junc13__bc1_is_in+VV_junc13__bc2_is_in+VV_junc13__bc3_is_in+VV_junc13__bc4_is_in
    VV_junc13__n_out = VV_junc13__bc1_is_out+VV_junc13__bc2_is_out+VV_junc13__bc3_is_out+VV_junc13__bc4_is_out
    VV_junc13__RBC_in = VV_junc13__Qin1*V12__H_R_out+VV_junc13__Qin2*VV_junc13__H_to2+VV_junc13__Qin3*PV25__H_L_out+VV_junc13__Qin4*PV26__H_L_out
    VV_junc13__v_mm3_s = VV_junc13__v/VV_junc13__one_mm3
    VV_junc13__junction_type = (1 if VV_junc13__n_in == 1 else (-1 if VV_junc13__n_in >= 2 else 0))
    VV_junc13__is_split = (1 if VV_junc13__junction_type == 1 else 0)
    VV_junc13__is_merge = (1 if VV_junc13__junction_type == -1 else 0)
    VV_junc13__feed1 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin1 >= VV_junc13__Qin2) and (VV_junc13__Qin1 >= VV_junc13__Qin3) and (VV_junc13__Qin1 >= VV_junc13__Qin4) else 0)
    VV_junc13__feed2 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin2 > VV_junc13__Qin1) and (VV_junc13__Qin2 >= VV_junc13__Qin3) and (VV_junc13__Qin2 >= VV_junc13__Qin4) else 0)
    VV_junc13__feed3 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin3 > VV_junc13__Qin1) and (VV_junc13__Qin3 > VV_junc13__Qin2) and (VV_junc13__Qin3 >= VV_junc13__Qin4) else 0)
    VV_junc13__feed4 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin4 > VV_junc13__Qin1) and (VV_junc13__Qin4 > VV_junc13__Qin2) and (VV_junc13__Qin4 > VV_junc13__Qin3) else 0)
    VV_junc13__alpha1 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc1_is_out == 1) and (VV_junc13__Qout1 >= VV_junc13__Qout2) and (VV_junc13__Qout1 >= VV_junc13__Qout3) and (VV_junc13__Qout1 >= VV_junc13__Qout4) else 0)
    VV_junc13__alpha2 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc2_is_out == 1) and (VV_junc13__Qout2 > VV_junc13__Qout1) and (VV_junc13__Qout2 >= VV_junc13__Qout3) and (VV_junc13__Qout2 >= VV_junc13__Qout4) else 0)
    VV_junc13__alpha3 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc3_is_out == 1) and (VV_junc13__Qout3 > VV_junc13__Qout1) and (VV_junc13__Qout3 > VV_junc13__Qout2) and (VV_junc13__Qout3 >= VV_junc13__Qout4) else 0)
    VV_junc13__alpha4 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc4_is_out == 1) and (VV_junc13__Qout4 > VV_junc13__Qout1) and (VV_junc13__Qout4 > VV_junc13__Qout2) and (VV_junc13__Qout4 > VV_junc13__Qout3) else 0)
    VV_junc13__Qout1_rem = (0 if VV_junc13__alpha1 == 1 else VV_junc13__Qout1)
    VV_junc13__Qout2_rem = (0 if VV_junc13__alpha2 == 1 else VV_junc13__Qout2)
    VV_junc13__Qout3_rem = (0 if VV_junc13__alpha3 == 1 else VV_junc13__Qout3)
    VV_junc13__Qout4_rem = (0 if VV_junc13__alpha4 == 1 else VV_junc13__Qout4)
    VV_junc13__beta1 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc1_is_out == 1) and (VV_junc13__alpha1 == 0) and (VV_junc13__Qout1_rem >= VV_junc13__Qout2_rem) and (VV_junc13__Qout1_rem >= VV_junc13__Qout3_rem) and (VV_junc13__Qout1_rem >= VV_junc13__Qout4_rem) else 0)
    VV_junc13__beta2 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc2_is_out == 1) and (VV_junc13__alpha2 == 0) and (VV_junc13__Qout2_rem > VV_junc13__Qout1_rem) and (VV_junc13__Qout2_rem >= VV_junc13__Qout3_rem) and (VV_junc13__Qout2_rem >= VV_junc13__Qout4_rem) else 0)
    VV_junc13__beta3 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc3_is_out == 1) and (VV_junc13__alpha3 == 0) and (VV_junc13__Qout3_rem > VV_junc13__Qout1_rem) and (VV_junc13__Qout3_rem > VV_junc13__Qout2_rem) and (VV_junc13__Qout3_rem >= VV_junc13__Qout4_rem) else 0)
    VV_junc13__beta4 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc4_is_out == 1) and (VV_junc13__alpha4 == 0) and (VV_junc13__Qout4_rem > VV_junc13__Qout1_rem) and (VV_junc13__Qout4_rem > VV_junc13__Qout2_rem) and (VV_junc13__Qout4_rem > VV_junc13__Qout3_rem) else 0)
    VV_junc13__D_F = (VV_junc13__D1 if VV_junc13__feed1 == 1 else (VV_junc13__D2 if VV_junc13__feed2 == 1 else (VV_junc13__D3 if VV_junc13__feed3 == 1 else (VV_junc13__D4 if VV_junc13__feed4 == 1 else VV_junc13__D1))))
    VV_junc13__D_alpha = (VV_junc13__D1 if VV_junc13__alpha1 == 1 else (VV_junc13__D2 if VV_junc13__alpha2 == 1 else (VV_junc13__D3 if VV_junc13__alpha3 == 1 else (VV_junc13__D4 if VV_junc13__alpha4 == 1 else VV_junc13__D3))))
    VV_junc13__D_beta = (VV_junc13__D1 if VV_junc13__beta1 == 1 else (VV_junc13__D2 if VV_junc13__beta2 == 1 else (VV_junc13__D3 if VV_junc13__beta3 == 1 else (VV_junc13__D4 if VV_junc13__beta4 == 1 else VV_junc13__D4))))
    VV_junc13__v_alpha = (VV_junc13__Qout1 if VV_junc13__alpha1 == 1 else (VV_junc13__Qout2 if VV_junc13__alpha2 == 1 else (VV_junc13__Qout3 if VV_junc13__alpha3 == 1 else (VV_junc13__Qout4 if VV_junc13__alpha4 == 1 else 0))))
    VV_junc13__v_beta = (VV_junc13__Qout1 if VV_junc13__beta1 == 1 else (VV_junc13__Qout2 if VV_junc13__beta2 == 1 else (VV_junc13__Qout3 if VV_junc13__beta3 == 1 else (VV_junc13__Qout4 if VV_junc13__beta4 == 1 else 0))))
    PV25__H_down_target = PV25__s_v_d*(PV25__H_mean+PV25__gamma_mirror*(PV25__H_mean-PV25__H_up))+(1-PV25__s_v_d)*PV25__H_mean
    PV26__H_down_target = PV26__s_v_d*(PV26__H_mean+PV26__gamma_mirror*(PV26__H_mean-PV26__H_up))+(1-PV26__s_v_d)*PV26__H_mean
    V25__H_down_target = V25__s_v*(V25__H_mean+V25__gamma_mirror*(V25__H_mean-V25__H_up))+(1-V25__s_v)*V25__H_mean
    V26__H_down_target = V26__s_v*(V26__H_mean+V26__gamma_mirror*(V26__H_mean-V26__H_up))+(1-V26__s_v)*V26__H_mean
    VV_junc14__n_in = VV_junc14__bc1_is_in+VV_junc14__bc2_is_in+VV_junc14__bc3_is_in+VV_junc14__bc4_is_in
    VV_junc14__n_out = VV_junc14__bc1_is_out+VV_junc14__bc2_is_out+VV_junc14__bc3_is_out+VV_junc14__bc4_is_out
    VV_junc14__RBC_in = VV_junc14__Qin1*V13__H_R_out+VV_junc14__Qin2*VV_junc14__H_to2+VV_junc14__Qin3*PV27__H_L_out+VV_junc14__Qin4*PV28__H_L_out
    VV_junc14__v_mm3_s = VV_junc14__v/VV_junc14__one_mm3
    VV_junc14__junction_type = (1 if VV_junc14__n_in == 1 else (-1 if VV_junc14__n_in >= 2 else 0))
    VV_junc14__is_split = (1 if VV_junc14__junction_type == 1 else 0)
    VV_junc14__is_merge = (1 if VV_junc14__junction_type == -1 else 0)
    VV_junc14__feed1 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin1 >= VV_junc14__Qin2) and (VV_junc14__Qin1 >= VV_junc14__Qin3) and (VV_junc14__Qin1 >= VV_junc14__Qin4) else 0)
    VV_junc14__feed2 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin2 > VV_junc14__Qin1) and (VV_junc14__Qin2 >= VV_junc14__Qin3) and (VV_junc14__Qin2 >= VV_junc14__Qin4) else 0)
    VV_junc14__feed3 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin3 > VV_junc14__Qin1) and (VV_junc14__Qin3 > VV_junc14__Qin2) and (VV_junc14__Qin3 >= VV_junc14__Qin4) else 0)
    VV_junc14__feed4 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin4 > VV_junc14__Qin1) and (VV_junc14__Qin4 > VV_junc14__Qin2) and (VV_junc14__Qin4 > VV_junc14__Qin3) else 0)
    VV_junc14__alpha1 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc1_is_out == 1) and (VV_junc14__Qout1 >= VV_junc14__Qout2) and (VV_junc14__Qout1 >= VV_junc14__Qout3) and (VV_junc14__Qout1 >= VV_junc14__Qout4) else 0)
    VV_junc14__alpha2 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc2_is_out == 1) and (VV_junc14__Qout2 > VV_junc14__Qout1) and (VV_junc14__Qout2 >= VV_junc14__Qout3) and (VV_junc14__Qout2 >= VV_junc14__Qout4) else 0)
    VV_junc14__alpha3 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc3_is_out == 1) and (VV_junc14__Qout3 > VV_junc14__Qout1) and (VV_junc14__Qout3 > VV_junc14__Qout2) and (VV_junc14__Qout3 >= VV_junc14__Qout4) else 0)
    VV_junc14__alpha4 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc4_is_out == 1) and (VV_junc14__Qout4 > VV_junc14__Qout1) and (VV_junc14__Qout4 > VV_junc14__Qout2) and (VV_junc14__Qout4 > VV_junc14__Qout3) else 0)
    VV_junc14__Qout1_rem = (0 if VV_junc14__alpha1 == 1 else VV_junc14__Qout1)
    VV_junc14__Qout2_rem = (0 if VV_junc14__alpha2 == 1 else VV_junc14__Qout2)
    VV_junc14__Qout3_rem = (0 if VV_junc14__alpha3 == 1 else VV_junc14__Qout3)
    VV_junc14__Qout4_rem = (0 if VV_junc14__alpha4 == 1 else VV_junc14__Qout4)
    VV_junc14__beta1 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc1_is_out == 1) and (VV_junc14__alpha1 == 0) and (VV_junc14__Qout1_rem >= VV_junc14__Qout2_rem) and (VV_junc14__Qout1_rem >= VV_junc14__Qout3_rem) and (VV_junc14__Qout1_rem >= VV_junc14__Qout4_rem) else 0)
    VV_junc14__beta2 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc2_is_out == 1) and (VV_junc14__alpha2 == 0) and (VV_junc14__Qout2_rem > VV_junc14__Qout1_rem) and (VV_junc14__Qout2_rem >= VV_junc14__Qout3_rem) and (VV_junc14__Qout2_rem >= VV_junc14__Qout4_rem) else 0)
    VV_junc14__beta3 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc3_is_out == 1) and (VV_junc14__alpha3 == 0) and (VV_junc14__Qout3_rem > VV_junc14__Qout1_rem) and (VV_junc14__Qout3_rem > VV_junc14__Qout2_rem) and (VV_junc14__Qout3_rem >= VV_junc14__Qout4_rem) else 0)
    VV_junc14__beta4 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc4_is_out == 1) and (VV_junc14__alpha4 == 0) and (VV_junc14__Qout4_rem > VV_junc14__Qout1_rem) and (VV_junc14__Qout4_rem > VV_junc14__Qout2_rem) and (VV_junc14__Qout4_rem > VV_junc14__Qout3_rem) else 0)
    VV_junc14__D_F = (VV_junc14__D1 if VV_junc14__feed1 == 1 else (VV_junc14__D2 if VV_junc14__feed2 == 1 else (VV_junc14__D3 if VV_junc14__feed3 == 1 else (VV_junc14__D4 if VV_junc14__feed4 == 1 else VV_junc14__D1))))
    VV_junc14__D_alpha = (VV_junc14__D1 if VV_junc14__alpha1 == 1 else (VV_junc14__D2 if VV_junc14__alpha2 == 1 else (VV_junc14__D3 if VV_junc14__alpha3 == 1 else (VV_junc14__D4 if VV_junc14__alpha4 == 1 else VV_junc14__D3))))
    VV_junc14__D_beta = (VV_junc14__D1 if VV_junc14__beta1 == 1 else (VV_junc14__D2 if VV_junc14__beta2 == 1 else (VV_junc14__D3 if VV_junc14__beta3 == 1 else (VV_junc14__D4 if VV_junc14__beta4 == 1 else VV_junc14__D4))))
    VV_junc14__v_alpha = (VV_junc14__Qout1 if VV_junc14__alpha1 == 1 else (VV_junc14__Qout2 if VV_junc14__alpha2 == 1 else (VV_junc14__Qout3 if VV_junc14__alpha3 == 1 else (VV_junc14__Qout4 if VV_junc14__alpha4 == 1 else 0))))
    VV_junc14__v_beta = (VV_junc14__Qout1 if VV_junc14__beta1 == 1 else (VV_junc14__Qout2 if VV_junc14__beta2 == 1 else (VV_junc14__Qout3 if VV_junc14__beta3 == 1 else (VV_junc14__Qout4 if VV_junc14__beta4 == 1 else 0))))
    PV27__H_down_target = PV27__s_v_d*(PV27__H_mean+PV27__gamma_mirror*(PV27__H_mean-PV27__H_up))+(1-PV27__s_v_d)*PV27__H_mean
    PV28__H_down_target = PV28__s_v_d*(PV28__H_mean+PV28__gamma_mirror*(PV28__H_mean-PV28__H_up))+(1-PV28__s_v_d)*PV28__H_mean
    V27__H_down_target = V27__s_v*(V27__H_mean+V27__gamma_mirror*(V27__H_mean-V27__H_up))+(1-V27__s_v)*V27__H_mean
    V28__H_down_target = V28__s_v*(V28__H_mean+V28__gamma_mirror*(V28__H_mean-V28__H_up))+(1-V28__s_v)*V28__H_mean
    VV_junc15__n_in = VV_junc15__bc1_is_in+VV_junc15__bc2_is_in+VV_junc15__bc3_is_in+VV_junc15__bc4_is_in
    VV_junc15__n_out = VV_junc15__bc1_is_out+VV_junc15__bc2_is_out+VV_junc15__bc3_is_out+VV_junc15__bc4_is_out
    VV_junc15__RBC_in = VV_junc15__Qin1*V14__H_R_out+VV_junc15__Qin2*VV_junc15__H_to2+VV_junc15__Qin3*PV29__H_L_out+VV_junc15__Qin4*PV30__H_L_out
    VV_junc15__v_mm3_s = VV_junc15__v/VV_junc15__one_mm3
    VV_junc15__junction_type = (1 if VV_junc15__n_in == 1 else (-1 if VV_junc15__n_in >= 2 else 0))
    VV_junc15__is_split = (1 if VV_junc15__junction_type == 1 else 0)
    VV_junc15__is_merge = (1 if VV_junc15__junction_type == -1 else 0)
    VV_junc15__feed1 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin1 >= VV_junc15__Qin2) and (VV_junc15__Qin1 >= VV_junc15__Qin3) and (VV_junc15__Qin1 >= VV_junc15__Qin4) else 0)
    VV_junc15__feed2 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin2 > VV_junc15__Qin1) and (VV_junc15__Qin2 >= VV_junc15__Qin3) and (VV_junc15__Qin2 >= VV_junc15__Qin4) else 0)
    VV_junc15__feed3 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin3 > VV_junc15__Qin1) and (VV_junc15__Qin3 > VV_junc15__Qin2) and (VV_junc15__Qin3 >= VV_junc15__Qin4) else 0)
    VV_junc15__feed4 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin4 > VV_junc15__Qin1) and (VV_junc15__Qin4 > VV_junc15__Qin2) and (VV_junc15__Qin4 > VV_junc15__Qin3) else 0)
    VV_junc15__alpha1 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc1_is_out == 1) and (VV_junc15__Qout1 >= VV_junc15__Qout2) and (VV_junc15__Qout1 >= VV_junc15__Qout3) and (VV_junc15__Qout1 >= VV_junc15__Qout4) else 0)
    VV_junc15__alpha2 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc2_is_out == 1) and (VV_junc15__Qout2 > VV_junc15__Qout1) and (VV_junc15__Qout2 >= VV_junc15__Qout3) and (VV_junc15__Qout2 >= VV_junc15__Qout4) else 0)
    VV_junc15__alpha3 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc3_is_out == 1) and (VV_junc15__Qout3 > VV_junc15__Qout1) and (VV_junc15__Qout3 > VV_junc15__Qout2) and (VV_junc15__Qout3 >= VV_junc15__Qout4) else 0)
    VV_junc15__alpha4 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc4_is_out == 1) and (VV_junc15__Qout4 > VV_junc15__Qout1) and (VV_junc15__Qout4 > VV_junc15__Qout2) and (VV_junc15__Qout4 > VV_junc15__Qout3) else 0)
    VV_junc15__Qout1_rem = (0 if VV_junc15__alpha1 == 1 else VV_junc15__Qout1)
    VV_junc15__Qout2_rem = (0 if VV_junc15__alpha2 == 1 else VV_junc15__Qout2)
    VV_junc15__Qout3_rem = (0 if VV_junc15__alpha3 == 1 else VV_junc15__Qout3)
    VV_junc15__Qout4_rem = (0 if VV_junc15__alpha4 == 1 else VV_junc15__Qout4)
    VV_junc15__beta1 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc1_is_out == 1) and (VV_junc15__alpha1 == 0) and (VV_junc15__Qout1_rem >= VV_junc15__Qout2_rem) and (VV_junc15__Qout1_rem >= VV_junc15__Qout3_rem) and (VV_junc15__Qout1_rem >= VV_junc15__Qout4_rem) else 0)
    VV_junc15__beta2 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc2_is_out == 1) and (VV_junc15__alpha2 == 0) and (VV_junc15__Qout2_rem > VV_junc15__Qout1_rem) and (VV_junc15__Qout2_rem >= VV_junc15__Qout3_rem) and (VV_junc15__Qout2_rem >= VV_junc15__Qout4_rem) else 0)
    VV_junc15__beta3 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc3_is_out == 1) and (VV_junc15__alpha3 == 0) and (VV_junc15__Qout3_rem > VV_junc15__Qout1_rem) and (VV_junc15__Qout3_rem > VV_junc15__Qout2_rem) and (VV_junc15__Qout3_rem >= VV_junc15__Qout4_rem) else 0)
    VV_junc15__beta4 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc4_is_out == 1) and (VV_junc15__alpha4 == 0) and (VV_junc15__Qout4_rem > VV_junc15__Qout1_rem) and (VV_junc15__Qout4_rem > VV_junc15__Qout2_rem) and (VV_junc15__Qout4_rem > VV_junc15__Qout3_rem) else 0)
    VV_junc15__D_F = (VV_junc15__D1 if VV_junc15__feed1 == 1 else (VV_junc15__D2 if VV_junc15__feed2 == 1 else (VV_junc15__D3 if VV_junc15__feed3 == 1 else (VV_junc15__D4 if VV_junc15__feed4 == 1 else VV_junc15__D1))))
    VV_junc15__D_alpha = (VV_junc15__D1 if VV_junc15__alpha1 == 1 else (VV_junc15__D2 if VV_junc15__alpha2 == 1 else (VV_junc15__D3 if VV_junc15__alpha3 == 1 else (VV_junc15__D4 if VV_junc15__alpha4 == 1 else VV_junc15__D3))))
    VV_junc15__D_beta = (VV_junc15__D1 if VV_junc15__beta1 == 1 else (VV_junc15__D2 if VV_junc15__beta2 == 1 else (VV_junc15__D3 if VV_junc15__beta3 == 1 else (VV_junc15__D4 if VV_junc15__beta4 == 1 else VV_junc15__D4))))
    VV_junc15__v_alpha = (VV_junc15__Qout1 if VV_junc15__alpha1 == 1 else (VV_junc15__Qout2 if VV_junc15__alpha2 == 1 else (VV_junc15__Qout3 if VV_junc15__alpha3 == 1 else (VV_junc15__Qout4 if VV_junc15__alpha4 == 1 else 0))))
    VV_junc15__v_beta = (VV_junc15__Qout1 if VV_junc15__beta1 == 1 else (VV_junc15__Qout2 if VV_junc15__beta2 == 1 else (VV_junc15__Qout3 if VV_junc15__beta3 == 1 else (VV_junc15__Qout4 if VV_junc15__beta4 == 1 else 0))))
    PV29__H_down_target = PV29__s_v_d*(PV29__H_mean+PV29__gamma_mirror*(PV29__H_mean-PV29__H_up))+(1-PV29__s_v_d)*PV29__H_mean
    PV30__H_down_target = PV30__s_v_d*(PV30__H_mean+PV30__gamma_mirror*(PV30__H_mean-PV30__H_up))+(1-PV30__s_v_d)*PV30__H_mean
    V29__H_down_target = V29__s_v*(V29__H_mean+V29__gamma_mirror*(V29__H_mean-V29__H_up))+(1-V29__s_v)*V29__H_mean
    V30__H_down_target = V30__s_v*(V30__H_mean+V30__gamma_mirror*(V30__H_mean-V30__H_up))+(1-V30__s_v)*V30__H_mean
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
    V7__H_down_target = V7__s_v*(V7__H_mean+V7__gamma_mirror*(V7__H_mean-V7__H_up))+(1-V7__s_v)*V7__H_mean
    V8__H_down_target = V8__s_v*(V8__H_mean+V8__gamma_mirror*(V8__H_mean-V8__H_up))+(1-V8__s_v)*V8__H_mean
    VV_junc5__FQB_alpha = (VV_junc5__v_alpha+VV_junc5__div_0)/(VV_junc5__v_alpha+VV_junc5__v_beta+2*VV_junc5__div_0)
    VV_junc5__B = 1+6.98*(1-VV_junc5__H_mean)/(VV_junc5__D_F*1e6)
    VV_junc5__A = -6.96*np.log(VV_junc5__D_alpha*1e6/(VV_junc5__D_beta*1e6))/(VV_junc5__D_F*1e6)
    VV_junc5__X_0 = 0.4/(VV_junc5__D_F*1e6)
    VV_junc5__y_raw = (VV_junc5__FQB_alpha-VV_junc5__X_0)/(1-2*VV_junc5__X_0+VV_junc5__div_0)
    VV_junc5__y = min(max(VV_junc5__y_raw, VV_junc5__div_0y), 1-VV_junc5__div_0y)
    V9__H_down_target = V9__s_v*(V9__H_mean+V9__gamma_mirror*(V9__H_mean-V9__H_up))+(1-V9__s_v)*V9__H_mean
    V10__H_down_target = V10__s_v*(V10__H_mean+V10__gamma_mirror*(V10__H_mean-V10__H_up))+(1-V10__s_v)*V10__H_mean
    VV_junc6__FQB_alpha = (VV_junc6__v_alpha+VV_junc6__div_0)/(VV_junc6__v_alpha+VV_junc6__v_beta+2*VV_junc6__div_0)
    VV_junc6__B = 1+6.98*(1-VV_junc6__H_mean)/(VV_junc6__D_F*1e6)
    VV_junc6__A = -6.96*np.log(VV_junc6__D_alpha*1e6/(VV_junc6__D_beta*1e6))/(VV_junc6__D_F*1e6)
    VV_junc6__X_0 = 0.4/(VV_junc6__D_F*1e6)
    VV_junc6__y_raw = (VV_junc6__FQB_alpha-VV_junc6__X_0)/(1-2*VV_junc6__X_0+VV_junc6__div_0)
    VV_junc6__y = min(max(VV_junc6__y_raw, VV_junc6__div_0y), 1-VV_junc6__div_0y)
    V11__H_down_target = V11__s_v*(V11__H_mean+V11__gamma_mirror*(V11__H_mean-V11__H_up))+(1-V11__s_v)*V11__H_mean
    V12__H_down_target = V12__s_v*(V12__H_mean+V12__gamma_mirror*(V12__H_mean-V12__H_up))+(1-V12__s_v)*V12__H_mean
    VV_junc7__FQB_alpha = (VV_junc7__v_alpha+VV_junc7__div_0)/(VV_junc7__v_alpha+VV_junc7__v_beta+2*VV_junc7__div_0)
    VV_junc7__B = 1+6.98*(1-VV_junc7__H_mean)/(VV_junc7__D_F*1e6)
    VV_junc7__A = -6.96*np.log(VV_junc7__D_alpha*1e6/(VV_junc7__D_beta*1e6))/(VV_junc7__D_F*1e6)
    VV_junc7__X_0 = 0.4/(VV_junc7__D_F*1e6)
    VV_junc7__y_raw = (VV_junc7__FQB_alpha-VV_junc7__X_0)/(1-2*VV_junc7__X_0+VV_junc7__div_0)
    VV_junc7__y = min(max(VV_junc7__y_raw, VV_junc7__div_0y), 1-VV_junc7__div_0y)
    V13__H_down_target = V13__s_v*(V13__H_mean+V13__gamma_mirror*(V13__H_mean-V13__H_up))+(1-V13__s_v)*V13__H_mean
    V14__H_down_target = V14__s_v*(V14__H_mean+V14__gamma_mirror*(V14__H_mean-V14__H_up))+(1-V14__s_v)*V14__H_mean
    VV_junc8__FQB_alpha = (VV_junc8__v_alpha+VV_junc8__div_0)/(VV_junc8__v_alpha+VV_junc8__v_beta+2*VV_junc8__div_0)
    VV_junc8__B = 1+6.98*(1-VV_junc8__H_mean)/(VV_junc8__D_F*1e6)
    VV_junc8__A = -6.96*np.log(VV_junc8__D_alpha*1e6/(VV_junc8__D_beta*1e6))/(VV_junc8__D_F*1e6)
    VV_junc8__X_0 = 0.4/(VV_junc8__D_F*1e6)
    VV_junc8__y_raw = (VV_junc8__FQB_alpha-VV_junc8__X_0)/(1-2*VV_junc8__X_0+VV_junc8__div_0)
    VV_junc8__y = min(max(VV_junc8__y_raw, VV_junc8__div_0y), 1-VV_junc8__div_0y)
    VV_junc9__FQB_alpha = (VV_junc9__v_alpha+VV_junc9__div_0)/(VV_junc9__v_alpha+VV_junc9__v_beta+2*VV_junc9__div_0)
    VV_junc9__B = 1+6.98*(1-VV_junc9__H_mean)/(VV_junc9__D_F*1e6)
    VV_junc9__A = -6.96*np.log(VV_junc9__D_alpha*1e6/(VV_junc9__D_beta*1e6))/(VV_junc9__D_F*1e6)
    VV_junc9__X_0 = 0.4/(VV_junc9__D_F*1e6)
    VV_junc9__y_raw = (VV_junc9__FQB_alpha-VV_junc9__X_0)/(1-2*VV_junc9__X_0+VV_junc9__div_0)
    VV_junc9__y = min(max(VV_junc9__y_raw, VV_junc9__div_0y), 1-VV_junc9__div_0y)
    VV_junc10__FQB_alpha = (VV_junc10__v_alpha+VV_junc10__div_0)/(VV_junc10__v_alpha+VV_junc10__v_beta+2*VV_junc10__div_0)
    VV_junc10__B = 1+6.98*(1-VV_junc10__H_mean)/(VV_junc10__D_F*1e6)
    VV_junc10__A = -6.96*np.log(VV_junc10__D_alpha*1e6/(VV_junc10__D_beta*1e6))/(VV_junc10__D_F*1e6)
    VV_junc10__X_0 = 0.4/(VV_junc10__D_F*1e6)
    VV_junc10__y_raw = (VV_junc10__FQB_alpha-VV_junc10__X_0)/(1-2*VV_junc10__X_0+VV_junc10__div_0)
    VV_junc10__y = min(max(VV_junc10__y_raw, VV_junc10__div_0y), 1-VV_junc10__div_0y)
    VV_junc11__FQB_alpha = (VV_junc11__v_alpha+VV_junc11__div_0)/(VV_junc11__v_alpha+VV_junc11__v_beta+2*VV_junc11__div_0)
    VV_junc11__B = 1+6.98*(1-VV_junc11__H_mean)/(VV_junc11__D_F*1e6)
    VV_junc11__A = -6.96*np.log(VV_junc11__D_alpha*1e6/(VV_junc11__D_beta*1e6))/(VV_junc11__D_F*1e6)
    VV_junc11__X_0 = 0.4/(VV_junc11__D_F*1e6)
    VV_junc11__y_raw = (VV_junc11__FQB_alpha-VV_junc11__X_0)/(1-2*VV_junc11__X_0+VV_junc11__div_0)
    VV_junc11__y = min(max(VV_junc11__y_raw, VV_junc11__div_0y), 1-VV_junc11__div_0y)
    VV_junc12__FQB_alpha = (VV_junc12__v_alpha+VV_junc12__div_0)/(VV_junc12__v_alpha+VV_junc12__v_beta+2*VV_junc12__div_0)
    VV_junc12__B = 1+6.98*(1-VV_junc12__H_mean)/(VV_junc12__D_F*1e6)
    VV_junc12__A = -6.96*np.log(VV_junc12__D_alpha*1e6/(VV_junc12__D_beta*1e6))/(VV_junc12__D_F*1e6)
    VV_junc12__X_0 = 0.4/(VV_junc12__D_F*1e6)
    VV_junc12__y_raw = (VV_junc12__FQB_alpha-VV_junc12__X_0)/(1-2*VV_junc12__X_0+VV_junc12__div_0)
    VV_junc12__y = min(max(VV_junc12__y_raw, VV_junc12__div_0y), 1-VV_junc12__div_0y)
    VV_junc13__FQB_alpha = (VV_junc13__v_alpha+VV_junc13__div_0)/(VV_junc13__v_alpha+VV_junc13__v_beta+2*VV_junc13__div_0)
    VV_junc13__B = 1+6.98*(1-VV_junc13__H_mean)/(VV_junc13__D_F*1e6)
    VV_junc13__A = -6.96*np.log(VV_junc13__D_alpha*1e6/(VV_junc13__D_beta*1e6))/(VV_junc13__D_F*1e6)
    VV_junc13__X_0 = 0.4/(VV_junc13__D_F*1e6)
    VV_junc13__y_raw = (VV_junc13__FQB_alpha-VV_junc13__X_0)/(1-2*VV_junc13__X_0+VV_junc13__div_0)
    VV_junc13__y = min(max(VV_junc13__y_raw, VV_junc13__div_0y), 1-VV_junc13__div_0y)
    VV_junc14__FQB_alpha = (VV_junc14__v_alpha+VV_junc14__div_0)/(VV_junc14__v_alpha+VV_junc14__v_beta+2*VV_junc14__div_0)
    VV_junc14__B = 1+6.98*(1-VV_junc14__H_mean)/(VV_junc14__D_F*1e6)
    VV_junc14__A = -6.96*np.log(VV_junc14__D_alpha*1e6/(VV_junc14__D_beta*1e6))/(VV_junc14__D_F*1e6)
    VV_junc14__X_0 = 0.4/(VV_junc14__D_F*1e6)
    VV_junc14__y_raw = (VV_junc14__FQB_alpha-VV_junc14__X_0)/(1-2*VV_junc14__X_0+VV_junc14__div_0)
    VV_junc14__y = min(max(VV_junc14__y_raw, VV_junc14__div_0y), 1-VV_junc14__div_0y)
    VV_junc15__FQB_alpha = (VV_junc15__v_alpha+VV_junc15__div_0)/(VV_junc15__v_alpha+VV_junc15__v_beta+2*VV_junc15__div_0)
    VV_junc15__B = 1+6.98*(1-VV_junc15__H_mean)/(VV_junc15__D_F*1e6)
    VV_junc15__A = -6.96*np.log(VV_junc15__D_alpha*1e6/(VV_junc15__D_beta*1e6))/(VV_junc15__D_F*1e6)
    VV_junc15__X_0 = 0.4/(VV_junc15__D_F*1e6)
    VV_junc15__y_raw = (VV_junc15__FQB_alpha-VV_junc15__X_0)/(1-2*VV_junc15__X_0+VV_junc15__div_0)
    VV_junc15__y = min(max(VV_junc15__y_raw, VV_junc15__div_0y), 1-VV_junc15__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc2__ph = np.log(VV_junc2__y/(1-VV_junc2__y))
    VV_junc3__ph = np.log(VV_junc3__y/(1-VV_junc3__y))
    VV_junc4__ph = np.log(VV_junc4__y/(1-VV_junc4__y))
    VV_junc5__ph = np.log(VV_junc5__y/(1-VV_junc5__y))
    VV_junc6__ph = np.log(VV_junc6__y/(1-VV_junc6__y))
    VV_junc7__ph = np.log(VV_junc7__y/(1-VV_junc7__y))
    VV_junc8__ph = np.log(VV_junc8__y/(1-VV_junc8__y))
    VV_junc9__ph = np.log(VV_junc9__y/(1-VV_junc9__y))
    VV_junc10__ph = np.log(VV_junc10__y/(1-VV_junc10__y))
    VV_junc11__ph = np.log(VV_junc11__y/(1-VV_junc11__y))
    VV_junc12__ph = np.log(VV_junc12__y/(1-VV_junc12__y))
    VV_junc13__ph = np.log(VV_junc13__y/(1-VV_junc13__y))
    VV_junc14__ph = np.log(VV_junc14__y/(1-VV_junc14__y))
    VV_junc15__ph = np.log(VV_junc15__y/(1-VV_junc15__y))
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
    VV_junc8__FQE_alpha = 1/(1+np.exp(-(VV_junc8__A+VV_junc8__B*VV_junc8__ph)))
    VV_junc8__H_VV_out_alpha = VV_junc8__H_mean*VV_junc8__FQE_alpha/(VV_junc8__FQB_alpha+VV_junc8__div_0)
    VV_junc8__H_VV_out_beta = VV_junc8__H_mean*(1-VV_junc8__FQE_alpha)/(1-VV_junc8__FQB_alpha+VV_junc8__div_0)
    VV_junc8__H_split1 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha1 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta1 == 1 else V7__H_R_out))
    VV_junc8__H_split2 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha2 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta2 == 1 else VV_junc8__H_to2))
    VV_junc8__H_split3 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha3 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta3 == 1 else PV15__H_L_out))
    VV_junc8__H_split4 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha4 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta4 == 1 else PV16__H_L_out))
    VV_junc8__H_daughter1 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split1 if VV_junc8__is_split == 1 else V7__H_R_out))
    VV_junc8__H_daughter2 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split2 if VV_junc8__is_split == 1 else VV_junc8__H_to2))
    VV_junc8__H_daughter3 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split3 if VV_junc8__is_split == 1 else PV15__H_L_out))
    VV_junc8__H_daughter4 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split4 if VV_junc8__is_split == 1 else PV16__H_L_out))
    VV_junc8__H_from1_target = (VV_junc8__H_daughter1 if VV_junc8__bc1_is_out == 1 else V7__H_R_out)
    VV_junc8__H_from2_target = (VV_junc8__H_daughter2 if VV_junc8__bc2_is_out == 1 else VV_junc8__H_to2)
    VV_junc8__H_from3_target = (VV_junc8__H_daughter3 if VV_junc8__bc3_is_out == 1 else PV15__H_L_out)
    VV_junc8__H_from4_target = (VV_junc8__H_daughter4 if VV_junc8__bc4_is_out == 1 else PV16__H_L_out)
    VV_junc9__FQE_alpha = 1/(1+np.exp(-(VV_junc9__A+VV_junc9__B*VV_junc9__ph)))
    VV_junc9__H_VV_out_alpha = VV_junc9__H_mean*VV_junc9__FQE_alpha/(VV_junc9__FQB_alpha+VV_junc9__div_0)
    VV_junc9__H_VV_out_beta = VV_junc9__H_mean*(1-VV_junc9__FQE_alpha)/(1-VV_junc9__FQB_alpha+VV_junc9__div_0)
    VV_junc9__H_split1 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha1 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta1 == 1 else V8__H_R_out))
    VV_junc9__H_split2 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha2 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta2 == 1 else VV_junc9__H_to2))
    VV_junc9__H_split3 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha3 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta3 == 1 else PV17__H_L_out))
    VV_junc9__H_split4 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha4 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta4 == 1 else PV18__H_L_out))
    VV_junc9__H_daughter1 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split1 if VV_junc9__is_split == 1 else V8__H_R_out))
    VV_junc9__H_daughter2 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split2 if VV_junc9__is_split == 1 else VV_junc9__H_to2))
    VV_junc9__H_daughter3 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split3 if VV_junc9__is_split == 1 else PV17__H_L_out))
    VV_junc9__H_daughter4 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split4 if VV_junc9__is_split == 1 else PV18__H_L_out))
    VV_junc9__H_from1_target = (VV_junc9__H_daughter1 if VV_junc9__bc1_is_out == 1 else V8__H_R_out)
    VV_junc9__H_from2_target = (VV_junc9__H_daughter2 if VV_junc9__bc2_is_out == 1 else VV_junc9__H_to2)
    VV_junc9__H_from3_target = (VV_junc9__H_daughter3 if VV_junc9__bc3_is_out == 1 else PV17__H_L_out)
    VV_junc9__H_from4_target = (VV_junc9__H_daughter4 if VV_junc9__bc4_is_out == 1 else PV18__H_L_out)
    VV_junc10__FQE_alpha = 1/(1+np.exp(-(VV_junc10__A+VV_junc10__B*VV_junc10__ph)))
    VV_junc10__H_VV_out_alpha = VV_junc10__H_mean*VV_junc10__FQE_alpha/(VV_junc10__FQB_alpha+VV_junc10__div_0)
    VV_junc10__H_VV_out_beta = VV_junc10__H_mean*(1-VV_junc10__FQE_alpha)/(1-VV_junc10__FQB_alpha+VV_junc10__div_0)
    VV_junc10__H_split1 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha1 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta1 == 1 else V9__H_R_out))
    VV_junc10__H_split2 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha2 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta2 == 1 else VV_junc10__H_to2))
    VV_junc10__H_split3 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha3 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta3 == 1 else PV19__H_L_out))
    VV_junc10__H_split4 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha4 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta4 == 1 else PV20__H_L_out))
    VV_junc10__H_daughter1 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split1 if VV_junc10__is_split == 1 else V9__H_R_out))
    VV_junc10__H_daughter2 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split2 if VV_junc10__is_split == 1 else VV_junc10__H_to2))
    VV_junc10__H_daughter3 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split3 if VV_junc10__is_split == 1 else PV19__H_L_out))
    VV_junc10__H_daughter4 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split4 if VV_junc10__is_split == 1 else PV20__H_L_out))
    VV_junc10__H_from1_target = (VV_junc10__H_daughter1 if VV_junc10__bc1_is_out == 1 else V9__H_R_out)
    VV_junc10__H_from2_target = (VV_junc10__H_daughter2 if VV_junc10__bc2_is_out == 1 else VV_junc10__H_to2)
    VV_junc10__H_from3_target = (VV_junc10__H_daughter3 if VV_junc10__bc3_is_out == 1 else PV19__H_L_out)
    VV_junc10__H_from4_target = (VV_junc10__H_daughter4 if VV_junc10__bc4_is_out == 1 else PV20__H_L_out)
    VV_junc11__FQE_alpha = 1/(1+np.exp(-(VV_junc11__A+VV_junc11__B*VV_junc11__ph)))
    VV_junc11__H_VV_out_alpha = VV_junc11__H_mean*VV_junc11__FQE_alpha/(VV_junc11__FQB_alpha+VV_junc11__div_0)
    VV_junc11__H_VV_out_beta = VV_junc11__H_mean*(1-VV_junc11__FQE_alpha)/(1-VV_junc11__FQB_alpha+VV_junc11__div_0)
    VV_junc11__H_split1 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha1 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta1 == 1 else V10__H_R_out))
    VV_junc11__H_split2 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha2 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta2 == 1 else VV_junc11__H_to2))
    VV_junc11__H_split3 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha3 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta3 == 1 else PV21__H_L_out))
    VV_junc11__H_split4 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha4 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta4 == 1 else PV22__H_L_out))
    VV_junc11__H_daughter1 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split1 if VV_junc11__is_split == 1 else V10__H_R_out))
    VV_junc11__H_daughter2 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split2 if VV_junc11__is_split == 1 else VV_junc11__H_to2))
    VV_junc11__H_daughter3 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split3 if VV_junc11__is_split == 1 else PV21__H_L_out))
    VV_junc11__H_daughter4 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split4 if VV_junc11__is_split == 1 else PV22__H_L_out))
    VV_junc11__H_from1_target = (VV_junc11__H_daughter1 if VV_junc11__bc1_is_out == 1 else V10__H_R_out)
    VV_junc11__H_from2_target = (VV_junc11__H_daughter2 if VV_junc11__bc2_is_out == 1 else VV_junc11__H_to2)
    VV_junc11__H_from3_target = (VV_junc11__H_daughter3 if VV_junc11__bc3_is_out == 1 else PV21__H_L_out)
    VV_junc11__H_from4_target = (VV_junc11__H_daughter4 if VV_junc11__bc4_is_out == 1 else PV22__H_L_out)
    VV_junc12__FQE_alpha = 1/(1+np.exp(-(VV_junc12__A+VV_junc12__B*VV_junc12__ph)))
    VV_junc12__H_VV_out_alpha = VV_junc12__H_mean*VV_junc12__FQE_alpha/(VV_junc12__FQB_alpha+VV_junc12__div_0)
    VV_junc12__H_VV_out_beta = VV_junc12__H_mean*(1-VV_junc12__FQE_alpha)/(1-VV_junc12__FQB_alpha+VV_junc12__div_0)
    VV_junc12__H_split1 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha1 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta1 == 1 else V11__H_R_out))
    VV_junc12__H_split2 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha2 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta2 == 1 else VV_junc12__H_to2))
    VV_junc12__H_split3 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha3 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta3 == 1 else PV23__H_L_out))
    VV_junc12__H_split4 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha4 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta4 == 1 else PV24__H_L_out))
    VV_junc12__H_daughter1 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split1 if VV_junc12__is_split == 1 else V11__H_R_out))
    VV_junc12__H_daughter2 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split2 if VV_junc12__is_split == 1 else VV_junc12__H_to2))
    VV_junc12__H_daughter3 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split3 if VV_junc12__is_split == 1 else PV23__H_L_out))
    VV_junc12__H_daughter4 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split4 if VV_junc12__is_split == 1 else PV24__H_L_out))
    VV_junc12__H_from1_target = (VV_junc12__H_daughter1 if VV_junc12__bc1_is_out == 1 else V11__H_R_out)
    VV_junc12__H_from2_target = (VV_junc12__H_daughter2 if VV_junc12__bc2_is_out == 1 else VV_junc12__H_to2)
    VV_junc12__H_from3_target = (VV_junc12__H_daughter3 if VV_junc12__bc3_is_out == 1 else PV23__H_L_out)
    VV_junc12__H_from4_target = (VV_junc12__H_daughter4 if VV_junc12__bc4_is_out == 1 else PV24__H_L_out)
    VV_junc13__FQE_alpha = 1/(1+np.exp(-(VV_junc13__A+VV_junc13__B*VV_junc13__ph)))
    VV_junc13__H_VV_out_alpha = VV_junc13__H_mean*VV_junc13__FQE_alpha/(VV_junc13__FQB_alpha+VV_junc13__div_0)
    VV_junc13__H_VV_out_beta = VV_junc13__H_mean*(1-VV_junc13__FQE_alpha)/(1-VV_junc13__FQB_alpha+VV_junc13__div_0)
    VV_junc13__H_split1 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha1 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta1 == 1 else V12__H_R_out))
    VV_junc13__H_split2 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha2 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta2 == 1 else VV_junc13__H_to2))
    VV_junc13__H_split3 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha3 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta3 == 1 else PV25__H_L_out))
    VV_junc13__H_split4 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha4 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta4 == 1 else PV26__H_L_out))
    VV_junc13__H_daughter1 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split1 if VV_junc13__is_split == 1 else V12__H_R_out))
    VV_junc13__H_daughter2 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split2 if VV_junc13__is_split == 1 else VV_junc13__H_to2))
    VV_junc13__H_daughter3 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split3 if VV_junc13__is_split == 1 else PV25__H_L_out))
    VV_junc13__H_daughter4 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split4 if VV_junc13__is_split == 1 else PV26__H_L_out))
    VV_junc13__H_from1_target = (VV_junc13__H_daughter1 if VV_junc13__bc1_is_out == 1 else V12__H_R_out)
    VV_junc13__H_from2_target = (VV_junc13__H_daughter2 if VV_junc13__bc2_is_out == 1 else VV_junc13__H_to2)
    VV_junc13__H_from3_target = (VV_junc13__H_daughter3 if VV_junc13__bc3_is_out == 1 else PV25__H_L_out)
    VV_junc13__H_from4_target = (VV_junc13__H_daughter4 if VV_junc13__bc4_is_out == 1 else PV26__H_L_out)
    VV_junc14__FQE_alpha = 1/(1+np.exp(-(VV_junc14__A+VV_junc14__B*VV_junc14__ph)))
    VV_junc14__H_VV_out_alpha = VV_junc14__H_mean*VV_junc14__FQE_alpha/(VV_junc14__FQB_alpha+VV_junc14__div_0)
    VV_junc14__H_VV_out_beta = VV_junc14__H_mean*(1-VV_junc14__FQE_alpha)/(1-VV_junc14__FQB_alpha+VV_junc14__div_0)
    VV_junc14__H_split1 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha1 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta1 == 1 else V13__H_R_out))
    VV_junc14__H_split2 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha2 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta2 == 1 else VV_junc14__H_to2))
    VV_junc14__H_split3 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha3 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta3 == 1 else PV27__H_L_out))
    VV_junc14__H_split4 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha4 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta4 == 1 else PV28__H_L_out))
    VV_junc14__H_daughter1 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split1 if VV_junc14__is_split == 1 else V13__H_R_out))
    VV_junc14__H_daughter2 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split2 if VV_junc14__is_split == 1 else VV_junc14__H_to2))
    VV_junc14__H_daughter3 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split3 if VV_junc14__is_split == 1 else PV27__H_L_out))
    VV_junc14__H_daughter4 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split4 if VV_junc14__is_split == 1 else PV28__H_L_out))
    VV_junc14__H_from1_target = (VV_junc14__H_daughter1 if VV_junc14__bc1_is_out == 1 else V13__H_R_out)
    VV_junc14__H_from2_target = (VV_junc14__H_daughter2 if VV_junc14__bc2_is_out == 1 else VV_junc14__H_to2)
    VV_junc14__H_from3_target = (VV_junc14__H_daughter3 if VV_junc14__bc3_is_out == 1 else PV27__H_L_out)
    VV_junc14__H_from4_target = (VV_junc14__H_daughter4 if VV_junc14__bc4_is_out == 1 else PV28__H_L_out)
    VV_junc15__FQE_alpha = 1/(1+np.exp(-(VV_junc15__A+VV_junc15__B*VV_junc15__ph)))
    VV_junc15__H_VV_out_alpha = VV_junc15__H_mean*VV_junc15__FQE_alpha/(VV_junc15__FQB_alpha+VV_junc15__div_0)
    VV_junc15__H_VV_out_beta = VV_junc15__H_mean*(1-VV_junc15__FQE_alpha)/(1-VV_junc15__FQB_alpha+VV_junc15__div_0)
    VV_junc15__H_split1 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha1 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta1 == 1 else V14__H_R_out))
    VV_junc15__H_split2 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha2 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta2 == 1 else VV_junc15__H_to2))
    VV_junc15__H_split3 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha3 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta3 == 1 else PV29__H_L_out))
    VV_junc15__H_split4 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha4 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta4 == 1 else PV30__H_L_out))
    VV_junc15__H_daughter1 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split1 if VV_junc15__is_split == 1 else V14__H_R_out))
    VV_junc15__H_daughter2 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split2 if VV_junc15__is_split == 1 else VV_junc15__H_to2))
    VV_junc15__H_daughter3 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split3 if VV_junc15__is_split == 1 else PV29__H_L_out))
    VV_junc15__H_daughter4 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split4 if VV_junc15__is_split == 1 else PV30__H_L_out))
    VV_junc15__H_from1_target = (VV_junc15__H_daughter1 if VV_junc15__bc1_is_out == 1 else V14__H_R_out)
    VV_junc15__H_from2_target = (VV_junc15__H_daughter2 if VV_junc15__bc2_is_out == 1 else VV_junc15__H_to2)
    VV_junc15__H_from3_target = (VV_junc15__H_daughter3 if VV_junc15__bc3_is_out == 1 else PV29__H_L_out)
    VV_junc15__H_from4_target = (VV_junc15__H_daughter4 if VV_junc15__bc4_is_out == 1 else PV30__H_L_out)
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
    VV_junc8__H_from1 = VV_junc8__w_out1*VV_junc8__H_from1_target
    VV_junc8__H_from2 = VV_junc8__w_out2*VV_junc8__H_from2_target
    VV_junc8__H_from3 = VV_junc8__w_out3*VV_junc8__H_from3_target
    VV_junc8__H_from4 = VV_junc8__w_out4*VV_junc8__H_from4_target
    VV_junc8__RBC_out = VV_junc8__Qout1*VV_junc8__H_from1+VV_junc8__Qout2*VV_junc8__H_from2+VV_junc8__Qout3*VV_junc8__H_from3+VV_junc8__Qout4*VV_junc8__H_from4
    VV_junc9__H_from1 = VV_junc9__w_out1*VV_junc9__H_from1_target
    VV_junc9__H_from2 = VV_junc9__w_out2*VV_junc9__H_from2_target
    VV_junc9__H_from3 = VV_junc9__w_out3*VV_junc9__H_from3_target
    VV_junc9__H_from4 = VV_junc9__w_out4*VV_junc9__H_from4_target
    VV_junc9__RBC_out = VV_junc9__Qout1*VV_junc9__H_from1+VV_junc9__Qout2*VV_junc9__H_from2+VV_junc9__Qout3*VV_junc9__H_from3+VV_junc9__Qout4*VV_junc9__H_from4
    VV_junc10__H_from1 = VV_junc10__w_out1*VV_junc10__H_from1_target
    VV_junc10__H_from2 = VV_junc10__w_out2*VV_junc10__H_from2_target
    VV_junc10__H_from3 = VV_junc10__w_out3*VV_junc10__H_from3_target
    VV_junc10__H_from4 = VV_junc10__w_out4*VV_junc10__H_from4_target
    VV_junc10__RBC_out = VV_junc10__Qout1*VV_junc10__H_from1+VV_junc10__Qout2*VV_junc10__H_from2+VV_junc10__Qout3*VV_junc10__H_from3+VV_junc10__Qout4*VV_junc10__H_from4
    VV_junc11__H_from1 = VV_junc11__w_out1*VV_junc11__H_from1_target
    VV_junc11__H_from2 = VV_junc11__w_out2*VV_junc11__H_from2_target
    VV_junc11__H_from3 = VV_junc11__w_out3*VV_junc11__H_from3_target
    VV_junc11__H_from4 = VV_junc11__w_out4*VV_junc11__H_from4_target
    VV_junc11__RBC_out = VV_junc11__Qout1*VV_junc11__H_from1+VV_junc11__Qout2*VV_junc11__H_from2+VV_junc11__Qout3*VV_junc11__H_from3+VV_junc11__Qout4*VV_junc11__H_from4
    VV_junc12__H_from1 = VV_junc12__w_out1*VV_junc12__H_from1_target
    VV_junc12__H_from2 = VV_junc12__w_out2*VV_junc12__H_from2_target
    VV_junc12__H_from3 = VV_junc12__w_out3*VV_junc12__H_from3_target
    VV_junc12__H_from4 = VV_junc12__w_out4*VV_junc12__H_from4_target
    VV_junc12__RBC_out = VV_junc12__Qout1*VV_junc12__H_from1+VV_junc12__Qout2*VV_junc12__H_from2+VV_junc12__Qout3*VV_junc12__H_from3+VV_junc12__Qout4*VV_junc12__H_from4
    VV_junc13__H_from1 = VV_junc13__w_out1*VV_junc13__H_from1_target
    VV_junc13__H_from2 = VV_junc13__w_out2*VV_junc13__H_from2_target
    VV_junc13__H_from3 = VV_junc13__w_out3*VV_junc13__H_from3_target
    VV_junc13__H_from4 = VV_junc13__w_out4*VV_junc13__H_from4_target
    VV_junc13__RBC_out = VV_junc13__Qout1*VV_junc13__H_from1+VV_junc13__Qout2*VV_junc13__H_from2+VV_junc13__Qout3*VV_junc13__H_from3+VV_junc13__Qout4*VV_junc13__H_from4
    VV_junc14__H_from1 = VV_junc14__w_out1*VV_junc14__H_from1_target
    VV_junc14__H_from2 = VV_junc14__w_out2*VV_junc14__H_from2_target
    VV_junc14__H_from3 = VV_junc14__w_out3*VV_junc14__H_from3_target
    VV_junc14__H_from4 = VV_junc14__w_out4*VV_junc14__H_from4_target
    VV_junc14__RBC_out = VV_junc14__Qout1*VV_junc14__H_from1+VV_junc14__Qout2*VV_junc14__H_from2+VV_junc14__Qout3*VV_junc14__H_from3+VV_junc14__Qout4*VV_junc14__H_from4
    VV_junc15__H_from1 = VV_junc15__w_out1*VV_junc15__H_from1_target
    VV_junc15__H_from2 = VV_junc15__w_out2*VV_junc15__H_from2_target
    VV_junc15__H_from3 = VV_junc15__w_out3*VV_junc15__H_from3_target
    VV_junc15__H_from4 = VV_junc15__w_out4*VV_junc15__H_from4_target
    VV_junc15__RBC_out = VV_junc15__Qout1*VV_junc15__H_from1+VV_junc15__Qout2*VV_junc15__H_from2+VV_junc15__Qout3*VV_junc15__H_from3+VV_junc15__Qout4*VV_junc15__H_from4

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
    dydt[87] = (VV_junc8__H_from1-V7__H_link_R)/V7__tau_link
    dydt[88] = (PV7__H_R_out-V7__H_link_L)/V7__tau_link
    dydt[89] = (V7__H_down_target-V7__H_down)/V7__tau_H_down
    dydt[90] = PV7__v_d*V7__H_volume_L-V7__v*V7__H_volume_R
    dydt[91] = PV7__v_d-V7__v
    dydt[92] = (VV_junc9__H_from1-V8__H_link_R)/V8__tau_link
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
    dydt[110] = (VV_junc10__H_from1-V9__H_link_R)/V9__tau_link
    dydt[111] = (PV9__H_R_out-V9__H_link_L)/V9__tau_link
    dydt[112] = (V9__H_down_target-V9__H_down)/V9__tau_H_down
    dydt[113] = PV9__v_d*V9__H_volume_L-V9__v*V9__H_volume_R
    dydt[114] = PV9__v_d-V9__v
    dydt[115] = (VV_junc11__H_from1-V10__H_link_R)/V10__tau_link
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
    dydt[133] = (VV_junc12__H_from1-V11__H_link_R)/V11__tau_link
    dydt[134] = (PV11__H_R_out-V11__H_link_L)/V11__tau_link
    dydt[135] = (V11__H_down_target-V11__H_down)/V11__tau_H_down
    dydt[136] = PV11__v_d*V11__H_volume_L-V11__v*V11__H_volume_R
    dydt[137] = PV11__v_d-V11__v
    dydt[138] = (VV_junc13__H_from1-V12__H_link_R)/V12__tau_link
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
    dydt[156] = (VV_junc14__H_from1-V13__H_link_R)/V13__tau_link
    dydt[157] = (PV13__H_R_out-V13__H_link_L)/V13__tau_link
    dydt[158] = (V13__H_down_target-V13__H_down)/V13__tau_H_down
    dydt[159] = PV13__v_d*V13__H_volume_L-V13__v*V13__H_volume_R
    dydt[160] = PV13__v_d-V13__v
    dydt[161] = (VV_junc15__H_from1-V14__H_link_R)/V14__tau_link
    dydt[162] = (PV14__H_R_out-V14__H_link_L)/V14__tau_link
    dydt[163] = (V14__H_down_target-V14__H_down)/V14__tau_H_down
    dydt[164] = PV14__v_d*V14__H_volume_L-V14__v*V14__H_volume_R
    dydt[165] = PV14__v_d-V14__v
    dydt[166] = VV_junc8__RBC_in-VV_junc8__RBC_out
    dydt[167] = V7__v+VV_junc8__vbc2-VV_junc8__v
    dydt[168] = VV_junc8__v-PV15__v-PV16__v
    dydt[169] = (V15__H_L_out-PV15__H_link_R)/PV15__tau_link
    dydt[170] = (VV_junc8__H_from3-PV15__H_link_L)/PV15__tau_link
    dydt[171] = (PV15__H_down_target-PV15__H_down)/PV15__tau_H_down
    dydt[172] = PV15__v*PV15__H_volume_L-PV15__v_d*PV15__H_volume_R
    dydt[173] = PV15__v-PV15__v_d
    dydt[174] = (V16__H_L_out-PV16__H_link_R)/PV16__tau_link
    dydt[175] = (VV_junc8__H_from4-PV16__H_link_L)/PV16__tau_link
    dydt[176] = (PV16__H_down_target-PV16__H_down)/PV16__tau_H_down
    dydt[177] = PV16__v*PV16__H_volume_L-PV16__v_d*PV16__H_volume_R
    dydt[178] = PV16__v-PV16__v_d
    dydt[179] = (V15__H_L_out_RHS-V15__H_link_R)/V15__tau_link
    dydt[180] = (PV15__H_R_out-V15__H_link_L)/V15__tau_link
    dydt[181] = (V15__H_down_target-V15__H_down)/V15__tau_H_down
    dydt[182] = PV15__v_d*V15__H_volume_L-V15__v*V15__H_volume_R
    dydt[183] = PV15__v_d-V15__v
    dydt[184] = (V16__H_L_out_RHS-V16__H_link_R)/V16__tau_link
    dydt[185] = (PV16__H_R_out-V16__H_link_L)/V16__tau_link
    dydt[186] = (V16__H_down_target-V16__H_down)/V16__tau_H_down
    dydt[187] = PV16__v_d*V16__H_volume_L-V16__v*V16__H_volume_R
    dydt[188] = PV16__v_d-V16__v
    dydt[189] = VV_junc9__RBC_in-VV_junc9__RBC_out
    dydt[190] = V8__v+VV_junc9__vbc2-VV_junc9__v
    dydt[191] = VV_junc9__v-PV17__v-PV18__v
    dydt[192] = (V17__H_L_out-PV17__H_link_R)/PV17__tau_link
    dydt[193] = (VV_junc9__H_from3-PV17__H_link_L)/PV17__tau_link
    dydt[194] = (PV17__H_down_target-PV17__H_down)/PV17__tau_H_down
    dydt[195] = PV17__v*PV17__H_volume_L-PV17__v_d*PV17__H_volume_R
    dydt[196] = PV17__v-PV17__v_d
    dydt[197] = (V18__H_L_out-PV18__H_link_R)/PV18__tau_link
    dydt[198] = (VV_junc9__H_from4-PV18__H_link_L)/PV18__tau_link
    dydt[199] = (PV18__H_down_target-PV18__H_down)/PV18__tau_H_down
    dydt[200] = PV18__v*PV18__H_volume_L-PV18__v_d*PV18__H_volume_R
    dydt[201] = PV18__v-PV18__v_d
    dydt[202] = (V17__H_L_out_RHS-V17__H_link_R)/V17__tau_link
    dydt[203] = (PV17__H_R_out-V17__H_link_L)/V17__tau_link
    dydt[204] = (V17__H_down_target-V17__H_down)/V17__tau_H_down
    dydt[205] = PV17__v_d*V17__H_volume_L-V17__v*V17__H_volume_R
    dydt[206] = PV17__v_d-V17__v
    dydt[207] = (V18__H_L_out_RHS-V18__H_link_R)/V18__tau_link
    dydt[208] = (PV18__H_R_out-V18__H_link_L)/V18__tau_link
    dydt[209] = (V18__H_down_target-V18__H_down)/V18__tau_H_down
    dydt[210] = PV18__v_d*V18__H_volume_L-V18__v*V18__H_volume_R
    dydt[211] = PV18__v_d-V18__v
    dydt[212] = VV_junc10__RBC_in-VV_junc10__RBC_out
    dydt[213] = V9__v+VV_junc10__vbc2-VV_junc10__v
    dydt[214] = VV_junc10__v-PV19__v-PV20__v
    dydt[215] = (V19__H_L_out-PV19__H_link_R)/PV19__tau_link
    dydt[216] = (VV_junc10__H_from3-PV19__H_link_L)/PV19__tau_link
    dydt[217] = (PV19__H_down_target-PV19__H_down)/PV19__tau_H_down
    dydt[218] = PV19__v*PV19__H_volume_L-PV19__v_d*PV19__H_volume_R
    dydt[219] = PV19__v-PV19__v_d
    dydt[220] = (V20__H_L_out-PV20__H_link_R)/PV20__tau_link
    dydt[221] = (VV_junc10__H_from4-PV20__H_link_L)/PV20__tau_link
    dydt[222] = (PV20__H_down_target-PV20__H_down)/PV20__tau_H_down
    dydt[223] = PV20__v*PV20__H_volume_L-PV20__v_d*PV20__H_volume_R
    dydt[224] = PV20__v-PV20__v_d
    dydt[225] = (V19__H_L_out_RHS-V19__H_link_R)/V19__tau_link
    dydt[226] = (PV19__H_R_out-V19__H_link_L)/V19__tau_link
    dydt[227] = (V19__H_down_target-V19__H_down)/V19__tau_H_down
    dydt[228] = PV19__v_d*V19__H_volume_L-V19__v*V19__H_volume_R
    dydt[229] = PV19__v_d-V19__v
    dydt[230] = (V20__H_L_out_RHS-V20__H_link_R)/V20__tau_link
    dydt[231] = (PV20__H_R_out-V20__H_link_L)/V20__tau_link
    dydt[232] = (V20__H_down_target-V20__H_down)/V20__tau_H_down
    dydt[233] = PV20__v_d*V20__H_volume_L-V20__v*V20__H_volume_R
    dydt[234] = PV20__v_d-V20__v
    dydt[235] = VV_junc11__RBC_in-VV_junc11__RBC_out
    dydt[236] = V10__v+VV_junc11__vbc2-VV_junc11__v
    dydt[237] = VV_junc11__v-PV21__v-PV22__v
    dydt[238] = (V21__H_L_out-PV21__H_link_R)/PV21__tau_link
    dydt[239] = (VV_junc11__H_from3-PV21__H_link_L)/PV21__tau_link
    dydt[240] = (PV21__H_down_target-PV21__H_down)/PV21__tau_H_down
    dydt[241] = PV21__v*PV21__H_volume_L-PV21__v_d*PV21__H_volume_R
    dydt[242] = PV21__v-PV21__v_d
    dydt[243] = (V22__H_L_out-PV22__H_link_R)/PV22__tau_link
    dydt[244] = (VV_junc11__H_from4-PV22__H_link_L)/PV22__tau_link
    dydt[245] = (PV22__H_down_target-PV22__H_down)/PV22__tau_H_down
    dydt[246] = PV22__v*PV22__H_volume_L-PV22__v_d*PV22__H_volume_R
    dydt[247] = PV22__v-PV22__v_d
    dydt[248] = (V21__H_L_out_RHS-V21__H_link_R)/V21__tau_link
    dydt[249] = (PV21__H_R_out-V21__H_link_L)/V21__tau_link
    dydt[250] = (V21__H_down_target-V21__H_down)/V21__tau_H_down
    dydt[251] = PV21__v_d*V21__H_volume_L-V21__v*V21__H_volume_R
    dydt[252] = PV21__v_d-V21__v
    dydt[253] = (V22__H_L_out_RHS-V22__H_link_R)/V22__tau_link
    dydt[254] = (PV22__H_R_out-V22__H_link_L)/V22__tau_link
    dydt[255] = (V22__H_down_target-V22__H_down)/V22__tau_H_down
    dydt[256] = PV22__v_d*V22__H_volume_L-V22__v*V22__H_volume_R
    dydt[257] = PV22__v_d-V22__v
    dydt[258] = VV_junc12__RBC_in-VV_junc12__RBC_out
    dydt[259] = V11__v+VV_junc12__vbc2-VV_junc12__v
    dydt[260] = VV_junc12__v-PV23__v-PV24__v
    dydt[261] = (V23__H_L_out-PV23__H_link_R)/PV23__tau_link
    dydt[262] = (VV_junc12__H_from3-PV23__H_link_L)/PV23__tau_link
    dydt[263] = (PV23__H_down_target-PV23__H_down)/PV23__tau_H_down
    dydt[264] = PV23__v*PV23__H_volume_L-PV23__v_d*PV23__H_volume_R
    dydt[265] = PV23__v-PV23__v_d
    dydt[266] = (V24__H_L_out-PV24__H_link_R)/PV24__tau_link
    dydt[267] = (VV_junc12__H_from4-PV24__H_link_L)/PV24__tau_link
    dydt[268] = (PV24__H_down_target-PV24__H_down)/PV24__tau_H_down
    dydt[269] = PV24__v*PV24__H_volume_L-PV24__v_d*PV24__H_volume_R
    dydt[270] = PV24__v-PV24__v_d
    dydt[271] = (V23__H_L_out_RHS-V23__H_link_R)/V23__tau_link
    dydt[272] = (PV23__H_R_out-V23__H_link_L)/V23__tau_link
    dydt[273] = (V23__H_down_target-V23__H_down)/V23__tau_H_down
    dydt[274] = PV23__v_d*V23__H_volume_L-V23__v*V23__H_volume_R
    dydt[275] = PV23__v_d-V23__v
    dydt[276] = (V24__H_L_out_RHS-V24__H_link_R)/V24__tau_link
    dydt[277] = (PV24__H_R_out-V24__H_link_L)/V24__tau_link
    dydt[278] = (V24__H_down_target-V24__H_down)/V24__tau_H_down
    dydt[279] = PV24__v_d*V24__H_volume_L-V24__v*V24__H_volume_R
    dydt[280] = PV24__v_d-V24__v
    dydt[281] = VV_junc13__RBC_in-VV_junc13__RBC_out
    dydt[282] = V12__v+VV_junc13__vbc2-VV_junc13__v
    dydt[283] = VV_junc13__v-PV25__v-PV26__v
    dydt[284] = (V25__H_L_out-PV25__H_link_R)/PV25__tau_link
    dydt[285] = (VV_junc13__H_from3-PV25__H_link_L)/PV25__tau_link
    dydt[286] = (PV25__H_down_target-PV25__H_down)/PV25__tau_H_down
    dydt[287] = PV25__v*PV25__H_volume_L-PV25__v_d*PV25__H_volume_R
    dydt[288] = PV25__v-PV25__v_d
    dydt[289] = (V26__H_L_out-PV26__H_link_R)/PV26__tau_link
    dydt[290] = (VV_junc13__H_from4-PV26__H_link_L)/PV26__tau_link
    dydt[291] = (PV26__H_down_target-PV26__H_down)/PV26__tau_H_down
    dydt[292] = PV26__v*PV26__H_volume_L-PV26__v_d*PV26__H_volume_R
    dydt[293] = PV26__v-PV26__v_d
    dydt[294] = (V25__H_L_out_RHS-V25__H_link_R)/V25__tau_link
    dydt[295] = (PV25__H_R_out-V25__H_link_L)/V25__tau_link
    dydt[296] = (V25__H_down_target-V25__H_down)/V25__tau_H_down
    dydt[297] = PV25__v_d*V25__H_volume_L-V25__v*V25__H_volume_R
    dydt[298] = PV25__v_d-V25__v
    dydt[299] = (V26__H_L_out_RHS-V26__H_link_R)/V26__tau_link
    dydt[300] = (PV26__H_R_out-V26__H_link_L)/V26__tau_link
    dydt[301] = (V26__H_down_target-V26__H_down)/V26__tau_H_down
    dydt[302] = PV26__v_d*V26__H_volume_L-V26__v*V26__H_volume_R
    dydt[303] = PV26__v_d-V26__v
    dydt[304] = VV_junc14__RBC_in-VV_junc14__RBC_out
    dydt[305] = V13__v+VV_junc14__vbc2-VV_junc14__v
    dydt[306] = VV_junc14__v-PV27__v-PV28__v
    dydt[307] = (V27__H_L_out-PV27__H_link_R)/PV27__tau_link
    dydt[308] = (VV_junc14__H_from3-PV27__H_link_L)/PV27__tau_link
    dydt[309] = (PV27__H_down_target-PV27__H_down)/PV27__tau_H_down
    dydt[310] = PV27__v*PV27__H_volume_L-PV27__v_d*PV27__H_volume_R
    dydt[311] = PV27__v-PV27__v_d
    dydt[312] = (V28__H_L_out-PV28__H_link_R)/PV28__tau_link
    dydt[313] = (VV_junc14__H_from4-PV28__H_link_L)/PV28__tau_link
    dydt[314] = (PV28__H_down_target-PV28__H_down)/PV28__tau_H_down
    dydt[315] = PV28__v*PV28__H_volume_L-PV28__v_d*PV28__H_volume_R
    dydt[316] = PV28__v-PV28__v_d
    dydt[317] = (V27__H_L_out_RHS-V27__H_link_R)/V27__tau_link
    dydt[318] = (PV27__H_R_out-V27__H_link_L)/V27__tau_link
    dydt[319] = (V27__H_down_target-V27__H_down)/V27__tau_H_down
    dydt[320] = PV27__v_d*V27__H_volume_L-V27__v*V27__H_volume_R
    dydt[321] = PV27__v_d-V27__v
    dydt[322] = (V28__H_L_out_RHS-V28__H_link_R)/V28__tau_link
    dydt[323] = (PV28__H_R_out-V28__H_link_L)/V28__tau_link
    dydt[324] = (V28__H_down_target-V28__H_down)/V28__tau_H_down
    dydt[325] = PV28__v_d*V28__H_volume_L-V28__v*V28__H_volume_R
    dydt[326] = PV28__v_d-V28__v
    dydt[327] = VV_junc15__RBC_in-VV_junc15__RBC_out
    dydt[328] = V14__v+VV_junc15__vbc2-VV_junc15__v
    dydt[329] = VV_junc15__v-PV29__v-PV30__v
    dydt[330] = (V29__H_L_out-PV29__H_link_R)/PV29__tau_link
    dydt[331] = (VV_junc15__H_from3-PV29__H_link_L)/PV29__tau_link
    dydt[332] = (PV29__H_down_target-PV29__H_down)/PV29__tau_H_down
    dydt[333] = PV29__v*PV29__H_volume_L-PV29__v_d*PV29__H_volume_R
    dydt[334] = PV29__v-PV29__v_d
    dydt[335] = (V30__H_L_out-PV30__H_link_R)/PV30__tau_link
    dydt[336] = (VV_junc15__H_from4-PV30__H_link_L)/PV30__tau_link
    dydt[337] = (PV30__H_down_target-PV30__H_down)/PV30__tau_H_down
    dydt[338] = PV30__v*PV30__H_volume_L-PV30__v_d*PV30__H_volume_R
    dydt[339] = PV30__v-PV30__v_d
    dydt[340] = (V29__H_L_out_RHS-V29__H_link_R)/V29__tau_link
    dydt[341] = (PV29__H_R_out-V29__H_link_L)/V29__tau_link
    dydt[342] = (V29__H_down_target-V29__H_down)/V29__tau_H_down
    dydt[343] = PV29__v_d*V29__H_volume_L-V29__v*V29__H_volume_R
    dydt[344] = PV29__v_d-V29__v
    dydt[345] = (V30__H_L_out_RHS-V30__H_link_R)/V30__tau_link
    dydt[346] = (PV30__H_R_out-V30__H_link_L)/V30__tau_link
    dydt[347] = (V30__H_down_target-V30__H_down)/V30__tau_H_down
    dydt[348] = PV30__v_d*V30__H_volume_L-V30__v*V30__H_volume_R
    dydt[349] = PV30__v_d-V30__v

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
    VV_junc8__RBC_volume = y[166]
    VV_junc8__q_C = y[167]
    VV_junc8__q_C_d = y[168]
    PV15__H_link_R = y[169]
    PV15__H_link_L = y[170]
    PV15__H_down = y[171]
    PV15__RBC_volume = y[172]
    PV15__q_C = y[173]
    PV16__H_link_R = y[174]
    PV16__H_link_L = y[175]
    PV16__H_down = y[176]
    PV16__RBC_volume = y[177]
    PV16__q_C = y[178]
    V15__H_link_R = y[179]
    V15__H_link_L = y[180]
    V15__H_down = y[181]
    V15__RBC_volume = y[182]
    V15__q_C = y[183]
    V16__H_link_R = y[184]
    V16__H_link_L = y[185]
    V16__H_down = y[186]
    V16__RBC_volume = y[187]
    V16__q_C = y[188]
    VV_junc9__RBC_volume = y[189]
    VV_junc9__q_C = y[190]
    VV_junc9__q_C_d = y[191]
    PV17__H_link_R = y[192]
    PV17__H_link_L = y[193]
    PV17__H_down = y[194]
    PV17__RBC_volume = y[195]
    PV17__q_C = y[196]
    PV18__H_link_R = y[197]
    PV18__H_link_L = y[198]
    PV18__H_down = y[199]
    PV18__RBC_volume = y[200]
    PV18__q_C = y[201]
    V17__H_link_R = y[202]
    V17__H_link_L = y[203]
    V17__H_down = y[204]
    V17__RBC_volume = y[205]
    V17__q_C = y[206]
    V18__H_link_R = y[207]
    V18__H_link_L = y[208]
    V18__H_down = y[209]
    V18__RBC_volume = y[210]
    V18__q_C = y[211]
    VV_junc10__RBC_volume = y[212]
    VV_junc10__q_C = y[213]
    VV_junc10__q_C_d = y[214]
    PV19__H_link_R = y[215]
    PV19__H_link_L = y[216]
    PV19__H_down = y[217]
    PV19__RBC_volume = y[218]
    PV19__q_C = y[219]
    PV20__H_link_R = y[220]
    PV20__H_link_L = y[221]
    PV20__H_down = y[222]
    PV20__RBC_volume = y[223]
    PV20__q_C = y[224]
    V19__H_link_R = y[225]
    V19__H_link_L = y[226]
    V19__H_down = y[227]
    V19__RBC_volume = y[228]
    V19__q_C = y[229]
    V20__H_link_R = y[230]
    V20__H_link_L = y[231]
    V20__H_down = y[232]
    V20__RBC_volume = y[233]
    V20__q_C = y[234]
    VV_junc11__RBC_volume = y[235]
    VV_junc11__q_C = y[236]
    VV_junc11__q_C_d = y[237]
    PV21__H_link_R = y[238]
    PV21__H_link_L = y[239]
    PV21__H_down = y[240]
    PV21__RBC_volume = y[241]
    PV21__q_C = y[242]
    PV22__H_link_R = y[243]
    PV22__H_link_L = y[244]
    PV22__H_down = y[245]
    PV22__RBC_volume = y[246]
    PV22__q_C = y[247]
    V21__H_link_R = y[248]
    V21__H_link_L = y[249]
    V21__H_down = y[250]
    V21__RBC_volume = y[251]
    V21__q_C = y[252]
    V22__H_link_R = y[253]
    V22__H_link_L = y[254]
    V22__H_down = y[255]
    V22__RBC_volume = y[256]
    V22__q_C = y[257]
    VV_junc12__RBC_volume = y[258]
    VV_junc12__q_C = y[259]
    VV_junc12__q_C_d = y[260]
    PV23__H_link_R = y[261]
    PV23__H_link_L = y[262]
    PV23__H_down = y[263]
    PV23__RBC_volume = y[264]
    PV23__q_C = y[265]
    PV24__H_link_R = y[266]
    PV24__H_link_L = y[267]
    PV24__H_down = y[268]
    PV24__RBC_volume = y[269]
    PV24__q_C = y[270]
    V23__H_link_R = y[271]
    V23__H_link_L = y[272]
    V23__H_down = y[273]
    V23__RBC_volume = y[274]
    V23__q_C = y[275]
    V24__H_link_R = y[276]
    V24__H_link_L = y[277]
    V24__H_down = y[278]
    V24__RBC_volume = y[279]
    V24__q_C = y[280]
    VV_junc13__RBC_volume = y[281]
    VV_junc13__q_C = y[282]
    VV_junc13__q_C_d = y[283]
    PV25__H_link_R = y[284]
    PV25__H_link_L = y[285]
    PV25__H_down = y[286]
    PV25__RBC_volume = y[287]
    PV25__q_C = y[288]
    PV26__H_link_R = y[289]
    PV26__H_link_L = y[290]
    PV26__H_down = y[291]
    PV26__RBC_volume = y[292]
    PV26__q_C = y[293]
    V25__H_link_R = y[294]
    V25__H_link_L = y[295]
    V25__H_down = y[296]
    V25__RBC_volume = y[297]
    V25__q_C = y[298]
    V26__H_link_R = y[299]
    V26__H_link_L = y[300]
    V26__H_down = y[301]
    V26__RBC_volume = y[302]
    V26__q_C = y[303]
    VV_junc14__RBC_volume = y[304]
    VV_junc14__q_C = y[305]
    VV_junc14__q_C_d = y[306]
    PV27__H_link_R = y[307]
    PV27__H_link_L = y[308]
    PV27__H_down = y[309]
    PV27__RBC_volume = y[310]
    PV27__q_C = y[311]
    PV28__H_link_R = y[312]
    PV28__H_link_L = y[313]
    PV28__H_down = y[314]
    PV28__RBC_volume = y[315]
    PV28__q_C = y[316]
    V27__H_link_R = y[317]
    V27__H_link_L = y[318]
    V27__H_down = y[319]
    V27__RBC_volume = y[320]
    V27__q_C = y[321]
    V28__H_link_R = y[322]
    V28__H_link_L = y[323]
    V28__H_down = y[324]
    V28__RBC_volume = y[325]
    V28__q_C = y[326]
    VV_junc15__RBC_volume = y[327]
    VV_junc15__q_C = y[328]
    VV_junc15__q_C_d = y[329]
    PV29__H_link_R = y[330]
    PV29__H_link_L = y[331]
    PV29__H_down = y[332]
    PV29__RBC_volume = y[333]
    PV29__q_C = y[334]
    PV30__H_link_R = y[335]
    PV30__H_link_L = y[336]
    PV30__H_down = y[337]
    PV30__RBC_volume = y[338]
    PV30__q_C = y[339]
    V29__H_link_R = y[340]
    V29__H_link_L = y[341]
    V29__H_down = y[342]
    V29__RBC_volume = y[343]
    V29__q_C = y[344]
    V30__H_link_R = y[345]
    V30__H_link_L = y[346]
    V30__H_down = y[347]
    V30__RBC_volume = y[348]
    V30__q_C = y[349]

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
    VV_junc8__vj2 = VV_junc8__vbc2
    VV_junc8__D1 = 2*V7__r
    VV_junc8__D2 = 2*VV_junc8__r_bc2
    VV_junc8__D3 = 2*PV15__r
    VV_junc8__D4 = 2*PV16__r
    VV_junc8__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc8__vj2/VV_junc8__v_scale)
    VV_junc8__w_out2 = 1-VV_junc8__w_in2
    VV_junc8__Qin2 = VV_junc8__w_in2*VV_junc8__vj2
    VV_junc8__Qout2 = VV_junc8__w_out2*-VV_junc8__vj2
    VV_junc8__q_us = np.pi*np.square(VV_junc8__r)*VV_junc8__l
    VV_junc8__q = VV_junc8__q_us+VV_junc8__q_C+VV_junc8__q_C_d
    VV_junc8__bc2_is_in = (1 if VV_junc8__Qin2 > VV_junc8__v_threshold else 0)
    VV_junc8__bc2_is_out = (1 if VV_junc8__Qout2 > VV_junc8__v_threshold else 0)
    VV_junc8__C_max12 = (V7__C if V7__C > VV_junc8__C_conn2 else (VV_junc8__C_conn2 if V7__C <= VV_junc8__C_conn2 else 0.0))
    PV15__R_constriction = PV15__R_constriction_base+(PV15__R_constriction_final-PV15__R_constriction_base)/(1+np.exp(-(environment__time-PV15__t0)/PV15__tau_sig))
    PV15__H_L_in = PV15__H_link_L
    PV15__H_R_in = PV15__H_link_R
    PV15__q_us = np.pi*np.square(PV15__r)*PV15__l
    PV15__q = PV15__q_us+PV15__q_C
    PV15__C = np.pi*np.square(8.5e-9)*PV15__l/133.322
    PV15__Z = (0.8+np.exp(-0.075*2*PV15__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV15__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV15__r*1e6, 12))
    PV15__mu_45 = 6*np.exp(-0.085*2*PV15__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV15__r*1e6, 0.645))
    PV15__u = PV15__q_C/PV15__C+PV15__u_ext
    PV16__R_constriction = PV16__R_constriction_base+(PV16__R_constriction_final-PV16__R_constriction_base)/(1+np.exp(-(environment__time-PV16__t0)/PV16__tau_sig))
    PV16__H_L_in = PV16__H_link_L
    PV16__H_R_in = PV16__H_link_R
    PV16__q_us = np.pi*np.square(PV16__r)*PV16__l
    PV16__q = PV16__q_us+PV16__q_C
    PV16__C = np.pi*np.square(8.5e-9)*PV16__l/133.322
    PV16__Z = (0.8+np.exp(-0.075*2*PV16__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV16__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV16__r*1e6, 12))
    PV16__mu_45 = 6*np.exp(-0.085*2*PV16__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV16__r*1e6, 0.645))
    PV16__u = PV16__q_C/PV16__C+PV16__u_ext
    V15__H_L_in = V15__H_link_L
    V15__H_R_in = V15__H_link_R
    V15__q_us = np.pi*np.square(V15__r)*V15__l
    V15__q = V15__q_us+V15__q_C
    V15__C = np.pi*np.square(8.5e-9)*V15__l/133.322
    V15__Z = (0.8+np.exp(-0.075*2*V15__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V15__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V15__r*1e6, 12))
    V15__mu_45 = 6*np.exp(-0.085*2*V15__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V15__r*1e6, 0.645))
    V15__u = V15__q_C/V15__C+V15__u_ext
    V16__H_L_in = V16__H_link_L
    V16__H_R_in = V16__H_link_R
    V16__q_us = np.pi*np.square(V16__r)*V16__l
    V16__q = V16__q_us+V16__q_C
    V16__C = np.pi*np.square(8.5e-9)*V16__l/133.322
    V16__Z = (0.8+np.exp(-0.075*2*V16__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V16__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V16__r*1e6, 12))
    V16__mu_45 = 6*np.exp(-0.085*2*V16__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V16__r*1e6, 0.645))
    V16__u = V16__q_C/V16__C+V16__u_ext
    VV_junc9__vj2 = VV_junc9__vbc2
    VV_junc9__D1 = 2*V8__r
    VV_junc9__D2 = 2*VV_junc9__r_bc2
    VV_junc9__D3 = 2*PV17__r
    VV_junc9__D4 = 2*PV18__r
    VV_junc9__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc9__vj2/VV_junc9__v_scale)
    VV_junc9__w_out2 = 1-VV_junc9__w_in2
    VV_junc9__Qin2 = VV_junc9__w_in2*VV_junc9__vj2
    VV_junc9__Qout2 = VV_junc9__w_out2*-VV_junc9__vj2
    VV_junc9__q_us = np.pi*np.square(VV_junc9__r)*VV_junc9__l
    VV_junc9__q = VV_junc9__q_us+VV_junc9__q_C+VV_junc9__q_C_d
    VV_junc9__bc2_is_in = (1 if VV_junc9__Qin2 > VV_junc9__v_threshold else 0)
    VV_junc9__bc2_is_out = (1 if VV_junc9__Qout2 > VV_junc9__v_threshold else 0)
    VV_junc9__C_max12 = (V8__C if V8__C > VV_junc9__C_conn2 else (VV_junc9__C_conn2 if V8__C <= VV_junc9__C_conn2 else 0.0))
    PV17__R_constriction = PV17__R_constriction_base+(PV17__R_constriction_final-PV17__R_constriction_base)/(1+np.exp(-(environment__time-PV17__t0)/PV17__tau_sig))
    PV17__H_L_in = PV17__H_link_L
    PV17__H_R_in = PV17__H_link_R
    PV17__q_us = np.pi*np.square(PV17__r)*PV17__l
    PV17__q = PV17__q_us+PV17__q_C
    PV17__C = np.pi*np.square(8.5e-9)*PV17__l/133.322
    PV17__Z = (0.8+np.exp(-0.075*2*PV17__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV17__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV17__r*1e6, 12))
    PV17__mu_45 = 6*np.exp(-0.085*2*PV17__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV17__r*1e6, 0.645))
    PV17__u = PV17__q_C/PV17__C+PV17__u_ext
    PV18__R_constriction = PV18__R_constriction_base+(PV18__R_constriction_final-PV18__R_constriction_base)/(1+np.exp(-(environment__time-PV18__t0)/PV18__tau_sig))
    PV18__H_L_in = PV18__H_link_L
    PV18__H_R_in = PV18__H_link_R
    PV18__q_us = np.pi*np.square(PV18__r)*PV18__l
    PV18__q = PV18__q_us+PV18__q_C
    PV18__C = np.pi*np.square(8.5e-9)*PV18__l/133.322
    PV18__Z = (0.8+np.exp(-0.075*2*PV18__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV18__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV18__r*1e6, 12))
    PV18__mu_45 = 6*np.exp(-0.085*2*PV18__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV18__r*1e6, 0.645))
    PV18__u = PV18__q_C/PV18__C+PV18__u_ext
    V17__H_L_in = V17__H_link_L
    V17__H_R_in = V17__H_link_R
    V17__q_us = np.pi*np.square(V17__r)*V17__l
    V17__q = V17__q_us+V17__q_C
    V17__C = np.pi*np.square(8.5e-9)*V17__l/133.322
    V17__Z = (0.8+np.exp(-0.075*2*V17__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V17__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V17__r*1e6, 12))
    V17__mu_45 = 6*np.exp(-0.085*2*V17__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V17__r*1e6, 0.645))
    V17__u = V17__q_C/V17__C+V17__u_ext
    V18__H_L_in = V18__H_link_L
    V18__H_R_in = V18__H_link_R
    V18__q_us = np.pi*np.square(V18__r)*V18__l
    V18__q = V18__q_us+V18__q_C
    V18__C = np.pi*np.square(8.5e-9)*V18__l/133.322
    V18__Z = (0.8+np.exp(-0.075*2*V18__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V18__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V18__r*1e6, 12))
    V18__mu_45 = 6*np.exp(-0.085*2*V18__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V18__r*1e6, 0.645))
    V18__u = V18__q_C/V18__C+V18__u_ext
    VV_junc10__vj2 = VV_junc10__vbc2
    VV_junc10__D1 = 2*V9__r
    VV_junc10__D2 = 2*VV_junc10__r_bc2
    VV_junc10__D3 = 2*PV19__r
    VV_junc10__D4 = 2*PV20__r
    VV_junc10__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc10__vj2/VV_junc10__v_scale)
    VV_junc10__w_out2 = 1-VV_junc10__w_in2
    VV_junc10__Qin2 = VV_junc10__w_in2*VV_junc10__vj2
    VV_junc10__Qout2 = VV_junc10__w_out2*-VV_junc10__vj2
    VV_junc10__q_us = np.pi*np.square(VV_junc10__r)*VV_junc10__l
    VV_junc10__q = VV_junc10__q_us+VV_junc10__q_C+VV_junc10__q_C_d
    VV_junc10__bc2_is_in = (1 if VV_junc10__Qin2 > VV_junc10__v_threshold else 0)
    VV_junc10__bc2_is_out = (1 if VV_junc10__Qout2 > VV_junc10__v_threshold else 0)
    VV_junc10__C_max12 = (V9__C if V9__C > VV_junc10__C_conn2 else (VV_junc10__C_conn2 if V9__C <= VV_junc10__C_conn2 else 0.0))
    PV19__R_constriction = PV19__R_constriction_base+(PV19__R_constriction_final-PV19__R_constriction_base)/(1+np.exp(-(environment__time-PV19__t0)/PV19__tau_sig))
    PV19__H_L_in = PV19__H_link_L
    PV19__H_R_in = PV19__H_link_R
    PV19__q_us = np.pi*np.square(PV19__r)*PV19__l
    PV19__q = PV19__q_us+PV19__q_C
    PV19__C = np.pi*np.square(8.5e-9)*PV19__l/133.322
    PV19__Z = (0.8+np.exp(-0.075*2*PV19__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV19__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV19__r*1e6, 12))
    PV19__mu_45 = 6*np.exp(-0.085*2*PV19__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV19__r*1e6, 0.645))
    PV19__u = PV19__q_C/PV19__C+PV19__u_ext
    PV20__R_constriction = PV20__R_constriction_base+(PV20__R_constriction_final-PV20__R_constriction_base)/(1+np.exp(-(environment__time-PV20__t0)/PV20__tau_sig))
    PV20__H_L_in = PV20__H_link_L
    PV20__H_R_in = PV20__H_link_R
    PV20__q_us = np.pi*np.square(PV20__r)*PV20__l
    PV20__q = PV20__q_us+PV20__q_C
    PV20__C = np.pi*np.square(8.5e-9)*PV20__l/133.322
    PV20__Z = (0.8+np.exp(-0.075*2*PV20__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV20__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV20__r*1e6, 12))
    PV20__mu_45 = 6*np.exp(-0.085*2*PV20__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV20__r*1e6, 0.645))
    PV20__u = PV20__q_C/PV20__C+PV20__u_ext
    V19__H_L_in = V19__H_link_L
    V19__H_R_in = V19__H_link_R
    V19__q_us = np.pi*np.square(V19__r)*V19__l
    V19__q = V19__q_us+V19__q_C
    V19__C = np.pi*np.square(8.5e-9)*V19__l/133.322
    V19__Z = (0.8+np.exp(-0.075*2*V19__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V19__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V19__r*1e6, 12))
    V19__mu_45 = 6*np.exp(-0.085*2*V19__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V19__r*1e6, 0.645))
    V19__u = V19__q_C/V19__C+V19__u_ext
    V20__H_L_in = V20__H_link_L
    V20__H_R_in = V20__H_link_R
    V20__q_us = np.pi*np.square(V20__r)*V20__l
    V20__q = V20__q_us+V20__q_C
    V20__C = np.pi*np.square(8.5e-9)*V20__l/133.322
    V20__Z = (0.8+np.exp(-0.075*2*V20__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V20__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V20__r*1e6, 12))
    V20__mu_45 = 6*np.exp(-0.085*2*V20__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V20__r*1e6, 0.645))
    V20__u = V20__q_C/V20__C+V20__u_ext
    VV_junc11__vj2 = VV_junc11__vbc2
    VV_junc11__D1 = 2*V10__r
    VV_junc11__D2 = 2*VV_junc11__r_bc2
    VV_junc11__D3 = 2*PV21__r
    VV_junc11__D4 = 2*PV22__r
    VV_junc11__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc11__vj2/VV_junc11__v_scale)
    VV_junc11__w_out2 = 1-VV_junc11__w_in2
    VV_junc11__Qin2 = VV_junc11__w_in2*VV_junc11__vj2
    VV_junc11__Qout2 = VV_junc11__w_out2*-VV_junc11__vj2
    VV_junc11__q_us = np.pi*np.square(VV_junc11__r)*VV_junc11__l
    VV_junc11__q = VV_junc11__q_us+VV_junc11__q_C+VV_junc11__q_C_d
    VV_junc11__bc2_is_in = (1 if VV_junc11__Qin2 > VV_junc11__v_threshold else 0)
    VV_junc11__bc2_is_out = (1 if VV_junc11__Qout2 > VV_junc11__v_threshold else 0)
    VV_junc11__C_max12 = (V10__C if V10__C > VV_junc11__C_conn2 else (VV_junc11__C_conn2 if V10__C <= VV_junc11__C_conn2 else 0.0))
    PV21__R_constriction = PV21__R_constriction_base+(PV21__R_constriction_final-PV21__R_constriction_base)/(1+np.exp(-(environment__time-PV21__t0)/PV21__tau_sig))
    PV21__H_L_in = PV21__H_link_L
    PV21__H_R_in = PV21__H_link_R
    PV21__q_us = np.pi*np.square(PV21__r)*PV21__l
    PV21__q = PV21__q_us+PV21__q_C
    PV21__C = np.pi*np.square(8.5e-9)*PV21__l/133.322
    PV21__Z = (0.8+np.exp(-0.075*2*PV21__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV21__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV21__r*1e6, 12))
    PV21__mu_45 = 6*np.exp(-0.085*2*PV21__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV21__r*1e6, 0.645))
    PV21__u = PV21__q_C/PV21__C+PV21__u_ext
    PV22__R_constriction = PV22__R_constriction_base+(PV22__R_constriction_final-PV22__R_constriction_base)/(1+np.exp(-(environment__time-PV22__t0)/PV22__tau_sig))
    PV22__H_L_in = PV22__H_link_L
    PV22__H_R_in = PV22__H_link_R
    PV22__q_us = np.pi*np.square(PV22__r)*PV22__l
    PV22__q = PV22__q_us+PV22__q_C
    PV22__C = np.pi*np.square(8.5e-9)*PV22__l/133.322
    PV22__Z = (0.8+np.exp(-0.075*2*PV22__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV22__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV22__r*1e6, 12))
    PV22__mu_45 = 6*np.exp(-0.085*2*PV22__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV22__r*1e6, 0.645))
    PV22__u = PV22__q_C/PV22__C+PV22__u_ext
    V21__H_L_in = V21__H_link_L
    V21__H_R_in = V21__H_link_R
    V21__q_us = np.pi*np.square(V21__r)*V21__l
    V21__q = V21__q_us+V21__q_C
    V21__C = np.pi*np.square(8.5e-9)*V21__l/133.322
    V21__Z = (0.8+np.exp(-0.075*2*V21__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V21__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V21__r*1e6, 12))
    V21__mu_45 = 6*np.exp(-0.085*2*V21__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V21__r*1e6, 0.645))
    V21__u = V21__q_C/V21__C+V21__u_ext
    V22__H_L_in = V22__H_link_L
    V22__H_R_in = V22__H_link_R
    V22__q_us = np.pi*np.square(V22__r)*V22__l
    V22__q = V22__q_us+V22__q_C
    V22__C = np.pi*np.square(8.5e-9)*V22__l/133.322
    V22__Z = (0.8+np.exp(-0.075*2*V22__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V22__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V22__r*1e6, 12))
    V22__mu_45 = 6*np.exp(-0.085*2*V22__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V22__r*1e6, 0.645))
    V22__u = V22__q_C/V22__C+V22__u_ext
    VV_junc12__vj2 = VV_junc12__vbc2
    VV_junc12__D1 = 2*V11__r
    VV_junc12__D2 = 2*VV_junc12__r_bc2
    VV_junc12__D3 = 2*PV23__r
    VV_junc12__D4 = 2*PV24__r
    VV_junc12__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc12__vj2/VV_junc12__v_scale)
    VV_junc12__w_out2 = 1-VV_junc12__w_in2
    VV_junc12__Qin2 = VV_junc12__w_in2*VV_junc12__vj2
    VV_junc12__Qout2 = VV_junc12__w_out2*-VV_junc12__vj2
    VV_junc12__q_us = np.pi*np.square(VV_junc12__r)*VV_junc12__l
    VV_junc12__q = VV_junc12__q_us+VV_junc12__q_C+VV_junc12__q_C_d
    VV_junc12__bc2_is_in = (1 if VV_junc12__Qin2 > VV_junc12__v_threshold else 0)
    VV_junc12__bc2_is_out = (1 if VV_junc12__Qout2 > VV_junc12__v_threshold else 0)
    VV_junc12__C_max12 = (V11__C if V11__C > VV_junc12__C_conn2 else (VV_junc12__C_conn2 if V11__C <= VV_junc12__C_conn2 else 0.0))
    PV23__R_constriction = PV23__R_constriction_base+(PV23__R_constriction_final-PV23__R_constriction_base)/(1+np.exp(-(environment__time-PV23__t0)/PV23__tau_sig))
    PV23__H_L_in = PV23__H_link_L
    PV23__H_R_in = PV23__H_link_R
    PV23__q_us = np.pi*np.square(PV23__r)*PV23__l
    PV23__q = PV23__q_us+PV23__q_C
    PV23__C = np.pi*np.square(8.5e-9)*PV23__l/133.322
    PV23__Z = (0.8+np.exp(-0.075*2*PV23__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV23__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV23__r*1e6, 12))
    PV23__mu_45 = 6*np.exp(-0.085*2*PV23__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV23__r*1e6, 0.645))
    PV23__u = PV23__q_C/PV23__C+PV23__u_ext
    PV24__R_constriction = PV24__R_constriction_base+(PV24__R_constriction_final-PV24__R_constriction_base)/(1+np.exp(-(environment__time-PV24__t0)/PV24__tau_sig))
    PV24__H_L_in = PV24__H_link_L
    PV24__H_R_in = PV24__H_link_R
    PV24__q_us = np.pi*np.square(PV24__r)*PV24__l
    PV24__q = PV24__q_us+PV24__q_C
    PV24__C = np.pi*np.square(8.5e-9)*PV24__l/133.322
    PV24__Z = (0.8+np.exp(-0.075*2*PV24__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV24__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV24__r*1e6, 12))
    PV24__mu_45 = 6*np.exp(-0.085*2*PV24__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV24__r*1e6, 0.645))
    PV24__u = PV24__q_C/PV24__C+PV24__u_ext
    V23__H_L_in = V23__H_link_L
    V23__H_R_in = V23__H_link_R
    V23__q_us = np.pi*np.square(V23__r)*V23__l
    V23__q = V23__q_us+V23__q_C
    V23__C = np.pi*np.square(8.5e-9)*V23__l/133.322
    V23__Z = (0.8+np.exp(-0.075*2*V23__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V23__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V23__r*1e6, 12))
    V23__mu_45 = 6*np.exp(-0.085*2*V23__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V23__r*1e6, 0.645))
    V23__u = V23__q_C/V23__C+V23__u_ext
    V24__H_L_in = V24__H_link_L
    V24__H_R_in = V24__H_link_R
    V24__q_us = np.pi*np.square(V24__r)*V24__l
    V24__q = V24__q_us+V24__q_C
    V24__C = np.pi*np.square(8.5e-9)*V24__l/133.322
    V24__Z = (0.8+np.exp(-0.075*2*V24__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V24__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V24__r*1e6, 12))
    V24__mu_45 = 6*np.exp(-0.085*2*V24__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V24__r*1e6, 0.645))
    V24__u = V24__q_C/V24__C+V24__u_ext
    VV_junc13__vj2 = VV_junc13__vbc2
    VV_junc13__D1 = 2*V12__r
    VV_junc13__D2 = 2*VV_junc13__r_bc2
    VV_junc13__D3 = 2*PV25__r
    VV_junc13__D4 = 2*PV26__r
    VV_junc13__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc13__vj2/VV_junc13__v_scale)
    VV_junc13__w_out2 = 1-VV_junc13__w_in2
    VV_junc13__Qin2 = VV_junc13__w_in2*VV_junc13__vj2
    VV_junc13__Qout2 = VV_junc13__w_out2*-VV_junc13__vj2
    VV_junc13__q_us = np.pi*np.square(VV_junc13__r)*VV_junc13__l
    VV_junc13__q = VV_junc13__q_us+VV_junc13__q_C+VV_junc13__q_C_d
    VV_junc13__bc2_is_in = (1 if VV_junc13__Qin2 > VV_junc13__v_threshold else 0)
    VV_junc13__bc2_is_out = (1 if VV_junc13__Qout2 > VV_junc13__v_threshold else 0)
    VV_junc13__C_max12 = (V12__C if V12__C > VV_junc13__C_conn2 else (VV_junc13__C_conn2 if V12__C <= VV_junc13__C_conn2 else 0.0))
    PV25__R_constriction = PV25__R_constriction_base+(PV25__R_constriction_final-PV25__R_constriction_base)/(1+np.exp(-(environment__time-PV25__t0)/PV25__tau_sig))
    PV25__H_L_in = PV25__H_link_L
    PV25__H_R_in = PV25__H_link_R
    PV25__q_us = np.pi*np.square(PV25__r)*PV25__l
    PV25__q = PV25__q_us+PV25__q_C
    PV25__C = np.pi*np.square(8.5e-9)*PV25__l/133.322
    PV25__Z = (0.8+np.exp(-0.075*2*PV25__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV25__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV25__r*1e6, 12))
    PV25__mu_45 = 6*np.exp(-0.085*2*PV25__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV25__r*1e6, 0.645))
    PV25__u = PV25__q_C/PV25__C+PV25__u_ext
    PV26__R_constriction = PV26__R_constriction_base+(PV26__R_constriction_final-PV26__R_constriction_base)/(1+np.exp(-(environment__time-PV26__t0)/PV26__tau_sig))
    PV26__H_L_in = PV26__H_link_L
    PV26__H_R_in = PV26__H_link_R
    PV26__q_us = np.pi*np.square(PV26__r)*PV26__l
    PV26__q = PV26__q_us+PV26__q_C
    PV26__C = np.pi*np.square(8.5e-9)*PV26__l/133.322
    PV26__Z = (0.8+np.exp(-0.075*2*PV26__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV26__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV26__r*1e6, 12))
    PV26__mu_45 = 6*np.exp(-0.085*2*PV26__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV26__r*1e6, 0.645))
    PV26__u = PV26__q_C/PV26__C+PV26__u_ext
    V25__H_L_in = V25__H_link_L
    V25__H_R_in = V25__H_link_R
    V25__q_us = np.pi*np.square(V25__r)*V25__l
    V25__q = V25__q_us+V25__q_C
    V25__C = np.pi*np.square(8.5e-9)*V25__l/133.322
    V25__Z = (0.8+np.exp(-0.075*2*V25__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V25__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V25__r*1e6, 12))
    V25__mu_45 = 6*np.exp(-0.085*2*V25__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V25__r*1e6, 0.645))
    V25__u = V25__q_C/V25__C+V25__u_ext
    V26__H_L_in = V26__H_link_L
    V26__H_R_in = V26__H_link_R
    V26__q_us = np.pi*np.square(V26__r)*V26__l
    V26__q = V26__q_us+V26__q_C
    V26__C = np.pi*np.square(8.5e-9)*V26__l/133.322
    V26__Z = (0.8+np.exp(-0.075*2*V26__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V26__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V26__r*1e6, 12))
    V26__mu_45 = 6*np.exp(-0.085*2*V26__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V26__r*1e6, 0.645))
    V26__u = V26__q_C/V26__C+V26__u_ext
    VV_junc14__vj2 = VV_junc14__vbc2
    VV_junc14__D1 = 2*V13__r
    VV_junc14__D2 = 2*VV_junc14__r_bc2
    VV_junc14__D3 = 2*PV27__r
    VV_junc14__D4 = 2*PV28__r
    VV_junc14__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc14__vj2/VV_junc14__v_scale)
    VV_junc14__w_out2 = 1-VV_junc14__w_in2
    VV_junc14__Qin2 = VV_junc14__w_in2*VV_junc14__vj2
    VV_junc14__Qout2 = VV_junc14__w_out2*-VV_junc14__vj2
    VV_junc14__q_us = np.pi*np.square(VV_junc14__r)*VV_junc14__l
    VV_junc14__q = VV_junc14__q_us+VV_junc14__q_C+VV_junc14__q_C_d
    VV_junc14__bc2_is_in = (1 if VV_junc14__Qin2 > VV_junc14__v_threshold else 0)
    VV_junc14__bc2_is_out = (1 if VV_junc14__Qout2 > VV_junc14__v_threshold else 0)
    VV_junc14__C_max12 = (V13__C if V13__C > VV_junc14__C_conn2 else (VV_junc14__C_conn2 if V13__C <= VV_junc14__C_conn2 else 0.0))
    PV27__R_constriction = PV27__R_constriction_base+(PV27__R_constriction_final-PV27__R_constriction_base)/(1+np.exp(-(environment__time-PV27__t0)/PV27__tau_sig))
    PV27__H_L_in = PV27__H_link_L
    PV27__H_R_in = PV27__H_link_R
    PV27__q_us = np.pi*np.square(PV27__r)*PV27__l
    PV27__q = PV27__q_us+PV27__q_C
    PV27__C = np.pi*np.square(8.5e-9)*PV27__l/133.322
    PV27__Z = (0.8+np.exp(-0.075*2*PV27__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV27__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV27__r*1e6, 12))
    PV27__mu_45 = 6*np.exp(-0.085*2*PV27__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV27__r*1e6, 0.645))
    PV27__u = PV27__q_C/PV27__C+PV27__u_ext
    PV28__R_constriction = PV28__R_constriction_base+(PV28__R_constriction_final-PV28__R_constriction_base)/(1+np.exp(-(environment__time-PV28__t0)/PV28__tau_sig))
    PV28__H_L_in = PV28__H_link_L
    PV28__H_R_in = PV28__H_link_R
    PV28__q_us = np.pi*np.square(PV28__r)*PV28__l
    PV28__q = PV28__q_us+PV28__q_C
    PV28__C = np.pi*np.square(8.5e-9)*PV28__l/133.322
    PV28__Z = (0.8+np.exp(-0.075*2*PV28__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV28__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV28__r*1e6, 12))
    PV28__mu_45 = 6*np.exp(-0.085*2*PV28__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV28__r*1e6, 0.645))
    PV28__u = PV28__q_C/PV28__C+PV28__u_ext
    V27__H_L_in = V27__H_link_L
    V27__H_R_in = V27__H_link_R
    V27__q_us = np.pi*np.square(V27__r)*V27__l
    V27__q = V27__q_us+V27__q_C
    V27__C = np.pi*np.square(8.5e-9)*V27__l/133.322
    V27__Z = (0.8+np.exp(-0.075*2*V27__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V27__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V27__r*1e6, 12))
    V27__mu_45 = 6*np.exp(-0.085*2*V27__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V27__r*1e6, 0.645))
    V27__u = V27__q_C/V27__C+V27__u_ext
    V28__H_L_in = V28__H_link_L
    V28__H_R_in = V28__H_link_R
    V28__q_us = np.pi*np.square(V28__r)*V28__l
    V28__q = V28__q_us+V28__q_C
    V28__C = np.pi*np.square(8.5e-9)*V28__l/133.322
    V28__Z = (0.8+np.exp(-0.075*2*V28__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V28__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V28__r*1e6, 12))
    V28__mu_45 = 6*np.exp(-0.085*2*V28__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V28__r*1e6, 0.645))
    V28__u = V28__q_C/V28__C+V28__u_ext
    VV_junc15__vj2 = VV_junc15__vbc2
    VV_junc15__D1 = 2*V14__r
    VV_junc15__D2 = 2*VV_junc15__r_bc2
    VV_junc15__D3 = 2*PV29__r
    VV_junc15__D4 = 2*PV30__r
    VV_junc15__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc15__vj2/VV_junc15__v_scale)
    VV_junc15__w_out2 = 1-VV_junc15__w_in2
    VV_junc15__Qin2 = VV_junc15__w_in2*VV_junc15__vj2
    VV_junc15__Qout2 = VV_junc15__w_out2*-VV_junc15__vj2
    VV_junc15__q_us = np.pi*np.square(VV_junc15__r)*VV_junc15__l
    VV_junc15__q = VV_junc15__q_us+VV_junc15__q_C+VV_junc15__q_C_d
    VV_junc15__bc2_is_in = (1 if VV_junc15__Qin2 > VV_junc15__v_threshold else 0)
    VV_junc15__bc2_is_out = (1 if VV_junc15__Qout2 > VV_junc15__v_threshold else 0)
    VV_junc15__C_max12 = (V14__C if V14__C > VV_junc15__C_conn2 else (VV_junc15__C_conn2 if V14__C <= VV_junc15__C_conn2 else 0.0))
    PV29__R_constriction = PV29__R_constriction_base+(PV29__R_constriction_final-PV29__R_constriction_base)/(1+np.exp(-(environment__time-PV29__t0)/PV29__tau_sig))
    PV29__H_L_in = PV29__H_link_L
    PV29__H_R_in = PV29__H_link_R
    PV29__q_us = np.pi*np.square(PV29__r)*PV29__l
    PV29__q = PV29__q_us+PV29__q_C
    PV29__C = np.pi*np.square(8.5e-9)*PV29__l/133.322
    PV29__Z = (0.8+np.exp(-0.075*2*PV29__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV29__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV29__r*1e6, 12))
    PV29__mu_45 = 6*np.exp(-0.085*2*PV29__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV29__r*1e6, 0.645))
    PV29__u = PV29__q_C/PV29__C+PV29__u_ext
    PV30__R_constriction = PV30__R_constriction_base+(PV30__R_constriction_final-PV30__R_constriction_base)/(1+np.exp(-(environment__time-PV30__t0)/PV30__tau_sig))
    PV30__H_L_in = PV30__H_link_L
    PV30__H_R_in = PV30__H_link_R
    PV30__q_us = np.pi*np.square(PV30__r)*PV30__l
    PV30__q = PV30__q_us+PV30__q_C
    PV30__C = np.pi*np.square(8.5e-9)*PV30__l/133.322
    PV30__Z = (0.8+np.exp(-0.075*2*PV30__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*PV30__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*PV30__r*1e6, 12))
    PV30__mu_45 = 6*np.exp(-0.085*2*PV30__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*PV30__r*1e6, 0.645))
    PV30__u = PV30__q_C/PV30__C+PV30__u_ext
    V29__H_L_in = V29__H_link_L
    V29__H_R_in = V29__H_link_R
    V29__q_us = np.pi*np.square(V29__r)*V29__l
    V29__q = V29__q_us+V29__q_C
    V29__C = np.pi*np.square(8.5e-9)*V29__l/133.322
    V29__Z = (0.8+np.exp(-0.075*2*V29__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V29__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V29__r*1e6, 12))
    V29__mu_45 = 6*np.exp(-0.085*2*V29__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V29__r*1e6, 0.645))
    V29__u = V29__q_C/V29__C+V29__u_ext
    V30__H_L_in = V30__H_link_L
    V30__H_R_in = V30__H_link_R
    V30__q_us = np.pi*np.square(V30__r)*V30__l
    V30__q = V30__q_us+V30__q_C
    V30__C = np.pi*np.square(8.5e-9)*V30__l/133.322
    V30__Z = (0.8+np.exp(-0.075*2*V30__r*1e6))*(-1+1/(1+safe_power(10.0, -11)*safe_power(2*V30__r*1e6, 12)))+1/(1+safe_power(10.0, -11)*safe_power(2*V30__r*1e6, 12))
    V30__mu_45 = 6*np.exp(-0.085*2*V30__r*1e6)+3.2-2.44*np.exp(-0.06*safe_power(2*V30__r*1e6, 0.645))
    V30__u = V30__q_C/V30__C+V30__u_ext
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
    VV_junc8__RBC_volume_init = VV_junc8__H_global_L*VV_junc8__q_us
    VV_junc8__H_mean = VV_junc8__RBC_volume/(VV_junc8__q_us+VV_junc8__div_0)
    VV_junc8__C_max123 = (VV_junc8__C_max12 if VV_junc8__C_max12 > PV15__C else (PV15__C if VV_junc8__C_max12 <= PV15__C else 0.0))
    VV_junc8__C = (VV_junc8__C_max123 if VV_junc8__C_max123 > PV16__C else (PV16__C if VV_junc8__C_max123 <= PV16__C else 0.0))
    PV15__RBC_volume_init = PV15__H_global_L*PV15__q_us
    PV15__H_mean = PV15__RBC_volume/PV15__q
    PV15__hem_dep_u_rel = 1+(PV15__mu_45-1)*(safe_power(1-PV15__H_mean, PV15__Z)-1)/(safe_power(1-PV15__H_global_L, PV15__Z)-1)*np.square(2*PV15__r*1e6/(2*PV15__r*1e6-1.1))
    PV15__u_mmHg = PV15__u/133.322
    PV16__RBC_volume_init = PV16__H_global_L*PV16__q_us
    PV16__H_mean = PV16__RBC_volume/PV16__q
    PV16__hem_dep_u_rel = 1+(PV16__mu_45-1)*(safe_power(1-PV16__H_mean, PV16__Z)-1)/(safe_power(1-PV16__H_global_L, PV16__Z)-1)*np.square(2*PV16__r*1e6/(2*PV16__r*1e6-1.1))
    PV16__u_mmHg = PV16__u/133.322
    V15__RBC_volume_init = V15__H_global_L*V15__q_us
    V15__H_mean = V15__RBC_volume/V15__q
    V15__hem_dep_u_rel = 1+(V15__mu_45-1)*(safe_power(1-V15__H_mean, V15__Z)-1)/(safe_power(1-V15__H_global_L, V15__Z)-1)*np.square(2*V15__r*1e6/(2*V15__r*1e6-1.1))
    V15__u_mmHg = V15__u/133.322
    V16__RBC_volume_init = V16__H_global_L*V16__q_us
    V16__H_mean = V16__RBC_volume/V16__q
    V16__hem_dep_u_rel = 1+(V16__mu_45-1)*(safe_power(1-V16__H_mean, V16__Z)-1)/(safe_power(1-V16__H_global_L, V16__Z)-1)*np.square(2*V16__r*1e6/(2*V16__r*1e6-1.1))
    V16__u_mmHg = V16__u/133.322
    VV_junc9__RBC_volume_init = VV_junc9__H_global_L*VV_junc9__q_us
    VV_junc9__H_mean = VV_junc9__RBC_volume/(VV_junc9__q_us+VV_junc9__div_0)
    VV_junc9__C_max123 = (VV_junc9__C_max12 if VV_junc9__C_max12 > PV17__C else (PV17__C if VV_junc9__C_max12 <= PV17__C else 0.0))
    VV_junc9__C = (VV_junc9__C_max123 if VV_junc9__C_max123 > PV18__C else (PV18__C if VV_junc9__C_max123 <= PV18__C else 0.0))
    PV17__RBC_volume_init = PV17__H_global_L*PV17__q_us
    PV17__H_mean = PV17__RBC_volume/PV17__q
    PV17__hem_dep_u_rel = 1+(PV17__mu_45-1)*(safe_power(1-PV17__H_mean, PV17__Z)-1)/(safe_power(1-PV17__H_global_L, PV17__Z)-1)*np.square(2*PV17__r*1e6/(2*PV17__r*1e6-1.1))
    PV17__u_mmHg = PV17__u/133.322
    PV18__RBC_volume_init = PV18__H_global_L*PV18__q_us
    PV18__H_mean = PV18__RBC_volume/PV18__q
    PV18__hem_dep_u_rel = 1+(PV18__mu_45-1)*(safe_power(1-PV18__H_mean, PV18__Z)-1)/(safe_power(1-PV18__H_global_L, PV18__Z)-1)*np.square(2*PV18__r*1e6/(2*PV18__r*1e6-1.1))
    PV18__u_mmHg = PV18__u/133.322
    V17__RBC_volume_init = V17__H_global_L*V17__q_us
    V17__H_mean = V17__RBC_volume/V17__q
    V17__hem_dep_u_rel = 1+(V17__mu_45-1)*(safe_power(1-V17__H_mean, V17__Z)-1)/(safe_power(1-V17__H_global_L, V17__Z)-1)*np.square(2*V17__r*1e6/(2*V17__r*1e6-1.1))
    V17__u_mmHg = V17__u/133.322
    V18__RBC_volume_init = V18__H_global_L*V18__q_us
    V18__H_mean = V18__RBC_volume/V18__q
    V18__hem_dep_u_rel = 1+(V18__mu_45-1)*(safe_power(1-V18__H_mean, V18__Z)-1)/(safe_power(1-V18__H_global_L, V18__Z)-1)*np.square(2*V18__r*1e6/(2*V18__r*1e6-1.1))
    V18__u_mmHg = V18__u/133.322
    VV_junc10__RBC_volume_init = VV_junc10__H_global_L*VV_junc10__q_us
    VV_junc10__H_mean = VV_junc10__RBC_volume/(VV_junc10__q_us+VV_junc10__div_0)
    VV_junc10__C_max123 = (VV_junc10__C_max12 if VV_junc10__C_max12 > PV19__C else (PV19__C if VV_junc10__C_max12 <= PV19__C else 0.0))
    VV_junc10__C = (VV_junc10__C_max123 if VV_junc10__C_max123 > PV20__C else (PV20__C if VV_junc10__C_max123 <= PV20__C else 0.0))
    PV19__RBC_volume_init = PV19__H_global_L*PV19__q_us
    PV19__H_mean = PV19__RBC_volume/PV19__q
    PV19__hem_dep_u_rel = 1+(PV19__mu_45-1)*(safe_power(1-PV19__H_mean, PV19__Z)-1)/(safe_power(1-PV19__H_global_L, PV19__Z)-1)*np.square(2*PV19__r*1e6/(2*PV19__r*1e6-1.1))
    PV19__u_mmHg = PV19__u/133.322
    PV20__RBC_volume_init = PV20__H_global_L*PV20__q_us
    PV20__H_mean = PV20__RBC_volume/PV20__q
    PV20__hem_dep_u_rel = 1+(PV20__mu_45-1)*(safe_power(1-PV20__H_mean, PV20__Z)-1)/(safe_power(1-PV20__H_global_L, PV20__Z)-1)*np.square(2*PV20__r*1e6/(2*PV20__r*1e6-1.1))
    PV20__u_mmHg = PV20__u/133.322
    V19__RBC_volume_init = V19__H_global_L*V19__q_us
    V19__H_mean = V19__RBC_volume/V19__q
    V19__hem_dep_u_rel = 1+(V19__mu_45-1)*(safe_power(1-V19__H_mean, V19__Z)-1)/(safe_power(1-V19__H_global_L, V19__Z)-1)*np.square(2*V19__r*1e6/(2*V19__r*1e6-1.1))
    V19__u_mmHg = V19__u/133.322
    V20__RBC_volume_init = V20__H_global_L*V20__q_us
    V20__H_mean = V20__RBC_volume/V20__q
    V20__hem_dep_u_rel = 1+(V20__mu_45-1)*(safe_power(1-V20__H_mean, V20__Z)-1)/(safe_power(1-V20__H_global_L, V20__Z)-1)*np.square(2*V20__r*1e6/(2*V20__r*1e6-1.1))
    V20__u_mmHg = V20__u/133.322
    VV_junc11__RBC_volume_init = VV_junc11__H_global_L*VV_junc11__q_us
    VV_junc11__H_mean = VV_junc11__RBC_volume/(VV_junc11__q_us+VV_junc11__div_0)
    VV_junc11__C_max123 = (VV_junc11__C_max12 if VV_junc11__C_max12 > PV21__C else (PV21__C if VV_junc11__C_max12 <= PV21__C else 0.0))
    VV_junc11__C = (VV_junc11__C_max123 if VV_junc11__C_max123 > PV22__C else (PV22__C if VV_junc11__C_max123 <= PV22__C else 0.0))
    PV21__RBC_volume_init = PV21__H_global_L*PV21__q_us
    PV21__H_mean = PV21__RBC_volume/PV21__q
    PV21__hem_dep_u_rel = 1+(PV21__mu_45-1)*(safe_power(1-PV21__H_mean, PV21__Z)-1)/(safe_power(1-PV21__H_global_L, PV21__Z)-1)*np.square(2*PV21__r*1e6/(2*PV21__r*1e6-1.1))
    PV21__u_mmHg = PV21__u/133.322
    PV22__RBC_volume_init = PV22__H_global_L*PV22__q_us
    PV22__H_mean = PV22__RBC_volume/PV22__q
    PV22__hem_dep_u_rel = 1+(PV22__mu_45-1)*(safe_power(1-PV22__H_mean, PV22__Z)-1)/(safe_power(1-PV22__H_global_L, PV22__Z)-1)*np.square(2*PV22__r*1e6/(2*PV22__r*1e6-1.1))
    PV22__u_mmHg = PV22__u/133.322
    V21__RBC_volume_init = V21__H_global_L*V21__q_us
    V21__H_mean = V21__RBC_volume/V21__q
    V21__hem_dep_u_rel = 1+(V21__mu_45-1)*(safe_power(1-V21__H_mean, V21__Z)-1)/(safe_power(1-V21__H_global_L, V21__Z)-1)*np.square(2*V21__r*1e6/(2*V21__r*1e6-1.1))
    V21__u_mmHg = V21__u/133.322
    V22__RBC_volume_init = V22__H_global_L*V22__q_us
    V22__H_mean = V22__RBC_volume/V22__q
    V22__hem_dep_u_rel = 1+(V22__mu_45-1)*(safe_power(1-V22__H_mean, V22__Z)-1)/(safe_power(1-V22__H_global_L, V22__Z)-1)*np.square(2*V22__r*1e6/(2*V22__r*1e6-1.1))
    V22__u_mmHg = V22__u/133.322
    VV_junc12__RBC_volume_init = VV_junc12__H_global_L*VV_junc12__q_us
    VV_junc12__H_mean = VV_junc12__RBC_volume/(VV_junc12__q_us+VV_junc12__div_0)
    VV_junc12__C_max123 = (VV_junc12__C_max12 if VV_junc12__C_max12 > PV23__C else (PV23__C if VV_junc12__C_max12 <= PV23__C else 0.0))
    VV_junc12__C = (VV_junc12__C_max123 if VV_junc12__C_max123 > PV24__C else (PV24__C if VV_junc12__C_max123 <= PV24__C else 0.0))
    PV23__RBC_volume_init = PV23__H_global_L*PV23__q_us
    PV23__H_mean = PV23__RBC_volume/PV23__q
    PV23__hem_dep_u_rel = 1+(PV23__mu_45-1)*(safe_power(1-PV23__H_mean, PV23__Z)-1)/(safe_power(1-PV23__H_global_L, PV23__Z)-1)*np.square(2*PV23__r*1e6/(2*PV23__r*1e6-1.1))
    PV23__u_mmHg = PV23__u/133.322
    PV24__RBC_volume_init = PV24__H_global_L*PV24__q_us
    PV24__H_mean = PV24__RBC_volume/PV24__q
    PV24__hem_dep_u_rel = 1+(PV24__mu_45-1)*(safe_power(1-PV24__H_mean, PV24__Z)-1)/(safe_power(1-PV24__H_global_L, PV24__Z)-1)*np.square(2*PV24__r*1e6/(2*PV24__r*1e6-1.1))
    PV24__u_mmHg = PV24__u/133.322
    V23__RBC_volume_init = V23__H_global_L*V23__q_us
    V23__H_mean = V23__RBC_volume/V23__q
    V23__hem_dep_u_rel = 1+(V23__mu_45-1)*(safe_power(1-V23__H_mean, V23__Z)-1)/(safe_power(1-V23__H_global_L, V23__Z)-1)*np.square(2*V23__r*1e6/(2*V23__r*1e6-1.1))
    V23__u_mmHg = V23__u/133.322
    V24__RBC_volume_init = V24__H_global_L*V24__q_us
    V24__H_mean = V24__RBC_volume/V24__q
    V24__hem_dep_u_rel = 1+(V24__mu_45-1)*(safe_power(1-V24__H_mean, V24__Z)-1)/(safe_power(1-V24__H_global_L, V24__Z)-1)*np.square(2*V24__r*1e6/(2*V24__r*1e6-1.1))
    V24__u_mmHg = V24__u/133.322
    VV_junc13__RBC_volume_init = VV_junc13__H_global_L*VV_junc13__q_us
    VV_junc13__H_mean = VV_junc13__RBC_volume/(VV_junc13__q_us+VV_junc13__div_0)
    VV_junc13__C_max123 = (VV_junc13__C_max12 if VV_junc13__C_max12 > PV25__C else (PV25__C if VV_junc13__C_max12 <= PV25__C else 0.0))
    VV_junc13__C = (VV_junc13__C_max123 if VV_junc13__C_max123 > PV26__C else (PV26__C if VV_junc13__C_max123 <= PV26__C else 0.0))
    PV25__RBC_volume_init = PV25__H_global_L*PV25__q_us
    PV25__H_mean = PV25__RBC_volume/PV25__q
    PV25__hem_dep_u_rel = 1+(PV25__mu_45-1)*(safe_power(1-PV25__H_mean, PV25__Z)-1)/(safe_power(1-PV25__H_global_L, PV25__Z)-1)*np.square(2*PV25__r*1e6/(2*PV25__r*1e6-1.1))
    PV25__u_mmHg = PV25__u/133.322
    PV26__RBC_volume_init = PV26__H_global_L*PV26__q_us
    PV26__H_mean = PV26__RBC_volume/PV26__q
    PV26__hem_dep_u_rel = 1+(PV26__mu_45-1)*(safe_power(1-PV26__H_mean, PV26__Z)-1)/(safe_power(1-PV26__H_global_L, PV26__Z)-1)*np.square(2*PV26__r*1e6/(2*PV26__r*1e6-1.1))
    PV26__u_mmHg = PV26__u/133.322
    V25__RBC_volume_init = V25__H_global_L*V25__q_us
    V25__H_mean = V25__RBC_volume/V25__q
    V25__hem_dep_u_rel = 1+(V25__mu_45-1)*(safe_power(1-V25__H_mean, V25__Z)-1)/(safe_power(1-V25__H_global_L, V25__Z)-1)*np.square(2*V25__r*1e6/(2*V25__r*1e6-1.1))
    V25__u_mmHg = V25__u/133.322
    V26__RBC_volume_init = V26__H_global_L*V26__q_us
    V26__H_mean = V26__RBC_volume/V26__q
    V26__hem_dep_u_rel = 1+(V26__mu_45-1)*(safe_power(1-V26__H_mean, V26__Z)-1)/(safe_power(1-V26__H_global_L, V26__Z)-1)*np.square(2*V26__r*1e6/(2*V26__r*1e6-1.1))
    V26__u_mmHg = V26__u/133.322
    VV_junc14__RBC_volume_init = VV_junc14__H_global_L*VV_junc14__q_us
    VV_junc14__H_mean = VV_junc14__RBC_volume/(VV_junc14__q_us+VV_junc14__div_0)
    VV_junc14__C_max123 = (VV_junc14__C_max12 if VV_junc14__C_max12 > PV27__C else (PV27__C if VV_junc14__C_max12 <= PV27__C else 0.0))
    VV_junc14__C = (VV_junc14__C_max123 if VV_junc14__C_max123 > PV28__C else (PV28__C if VV_junc14__C_max123 <= PV28__C else 0.0))
    PV27__RBC_volume_init = PV27__H_global_L*PV27__q_us
    PV27__H_mean = PV27__RBC_volume/PV27__q
    PV27__hem_dep_u_rel = 1+(PV27__mu_45-1)*(safe_power(1-PV27__H_mean, PV27__Z)-1)/(safe_power(1-PV27__H_global_L, PV27__Z)-1)*np.square(2*PV27__r*1e6/(2*PV27__r*1e6-1.1))
    PV27__u_mmHg = PV27__u/133.322
    PV28__RBC_volume_init = PV28__H_global_L*PV28__q_us
    PV28__H_mean = PV28__RBC_volume/PV28__q
    PV28__hem_dep_u_rel = 1+(PV28__mu_45-1)*(safe_power(1-PV28__H_mean, PV28__Z)-1)/(safe_power(1-PV28__H_global_L, PV28__Z)-1)*np.square(2*PV28__r*1e6/(2*PV28__r*1e6-1.1))
    PV28__u_mmHg = PV28__u/133.322
    V27__RBC_volume_init = V27__H_global_L*V27__q_us
    V27__H_mean = V27__RBC_volume/V27__q
    V27__hem_dep_u_rel = 1+(V27__mu_45-1)*(safe_power(1-V27__H_mean, V27__Z)-1)/(safe_power(1-V27__H_global_L, V27__Z)-1)*np.square(2*V27__r*1e6/(2*V27__r*1e6-1.1))
    V27__u_mmHg = V27__u/133.322
    V28__RBC_volume_init = V28__H_global_L*V28__q_us
    V28__H_mean = V28__RBC_volume/V28__q
    V28__hem_dep_u_rel = 1+(V28__mu_45-1)*(safe_power(1-V28__H_mean, V28__Z)-1)/(safe_power(1-V28__H_global_L, V28__Z)-1)*np.square(2*V28__r*1e6/(2*V28__r*1e6-1.1))
    V28__u_mmHg = V28__u/133.322
    VV_junc15__RBC_volume_init = VV_junc15__H_global_L*VV_junc15__q_us
    VV_junc15__H_mean = VV_junc15__RBC_volume/(VV_junc15__q_us+VV_junc15__div_0)
    VV_junc15__C_max123 = (VV_junc15__C_max12 if VV_junc15__C_max12 > PV29__C else (PV29__C if VV_junc15__C_max12 <= PV29__C else 0.0))
    VV_junc15__C = (VV_junc15__C_max123 if VV_junc15__C_max123 > PV30__C else (PV30__C if VV_junc15__C_max123 <= PV30__C else 0.0))
    PV29__RBC_volume_init = PV29__H_global_L*PV29__q_us
    PV29__H_mean = PV29__RBC_volume/PV29__q
    PV29__hem_dep_u_rel = 1+(PV29__mu_45-1)*(safe_power(1-PV29__H_mean, PV29__Z)-1)/(safe_power(1-PV29__H_global_L, PV29__Z)-1)*np.square(2*PV29__r*1e6/(2*PV29__r*1e6-1.1))
    PV29__u_mmHg = PV29__u/133.322
    PV30__RBC_volume_init = PV30__H_global_L*PV30__q_us
    PV30__H_mean = PV30__RBC_volume/PV30__q
    PV30__hem_dep_u_rel = 1+(PV30__mu_45-1)*(safe_power(1-PV30__H_mean, PV30__Z)-1)/(safe_power(1-PV30__H_global_L, PV30__Z)-1)*np.square(2*PV30__r*1e6/(2*PV30__r*1e6-1.1))
    PV30__u_mmHg = PV30__u/133.322
    V29__RBC_volume_init = V29__H_global_L*V29__q_us
    V29__H_mean = V29__RBC_volume/V29__q
    V29__hem_dep_u_rel = 1+(V29__mu_45-1)*(safe_power(1-V29__H_mean, V29__Z)-1)/(safe_power(1-V29__H_global_L, V29__Z)-1)*np.square(2*V29__r*1e6/(2*V29__r*1e6-1.1))
    V29__u_mmHg = V29__u/133.322
    V30__RBC_volume_init = V30__H_global_L*V30__q_us
    V30__H_mean = V30__RBC_volume/V30__q
    V30__hem_dep_u_rel = 1+(V30__mu_45-1)*(safe_power(1-V30__H_mean, V30__Z)-1)/(safe_power(1-V30__H_global_L, V30__Z)-1)*np.square(2*V30__r*1e6/(2*V30__r*1e6-1.1))
    V30__u_mmHg = V30__u/133.322
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
    V8__mu = V8__hem_dep_u_rel*V8__mu_plasma
    V8__R = 8*V8__mu*V8__l/(np.pi*safe_power(V8__r, 4))
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
    V10__mu = V10__hem_dep_u_rel*V10__mu_plasma
    V10__R = 8*V10__mu*V10__l/(np.pi*safe_power(V10__r, 4))
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
    V12__mu = V12__hem_dep_u_rel*V12__mu_plasma
    V12__R = 8*V12__mu*V12__l/(np.pi*safe_power(V12__r, 4))
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
    V14__mu = V14__hem_dep_u_rel*V14__mu_plasma
    V14__R = 8*V14__mu*V14__l/(np.pi*safe_power(V14__r, 4))
    VV_junc8__u = VV_junc8__q_C/(VV_junc8__C/2)+VV_junc8__u_ext
    VV_junc8__u_mmHg = VV_junc8__u/133.322
    VV_junc8__u_d = VV_junc8__q_C_d/(VV_junc8__C/2)+VV_junc8__u_ext
    VV_junc8__u_d_mmHg = VV_junc8__u_d/133.322
    PV15__mu = PV15__hem_dep_u_rel*PV15__mu_plasma
    PV15__R = 8*PV15__mu*PV15__l/(np.pi*safe_power(PV15__r, 4))+PV15__R_constriction
    PV15__v = (VV_junc8__u_d-PV15__u)/(PV15__R/2)
    PV15__v_d = (PV15__u-V15__u)/(PV15__R/2)
    PV16__mu = PV16__hem_dep_u_rel*PV16__mu_plasma
    PV16__R = 8*PV16__mu*PV16__l/(np.pi*safe_power(PV16__r, 4))+PV16__R_constriction
    PV16__v = (VV_junc8__u_d-PV16__u)/(PV16__R/2)
    PV16__v_d = (PV16__u-V16__u)/(PV16__R/2)
    V15__mu = V15__hem_dep_u_rel*V15__mu_plasma
    V15__R = 8*V15__mu*V15__l/(np.pi*safe_power(V15__r, 4))
    V15__v = (V15__u-V15__u_out)/V15__R
    V16__mu = V16__hem_dep_u_rel*V16__mu_plasma
    V16__R = 8*V16__mu*V16__l/(np.pi*safe_power(V16__r, 4))
    V16__v = (V16__u-V16__u_out)/V16__R
    VV_junc9__u = VV_junc9__q_C/(VV_junc9__C/2)+VV_junc9__u_ext
    VV_junc9__u_mmHg = VV_junc9__u/133.322
    VV_junc9__u_d = VV_junc9__q_C_d/(VV_junc9__C/2)+VV_junc9__u_ext
    VV_junc9__u_d_mmHg = VV_junc9__u_d/133.322
    PV17__mu = PV17__hem_dep_u_rel*PV17__mu_plasma
    PV17__R = 8*PV17__mu*PV17__l/(np.pi*safe_power(PV17__r, 4))+PV17__R_constriction
    PV17__v = (VV_junc9__u_d-PV17__u)/(PV17__R/2)
    PV17__v_d = (PV17__u-V17__u)/(PV17__R/2)
    PV18__mu = PV18__hem_dep_u_rel*PV18__mu_plasma
    PV18__R = 8*PV18__mu*PV18__l/(np.pi*safe_power(PV18__r, 4))+PV18__R_constriction
    PV18__v = (VV_junc9__u_d-PV18__u)/(PV18__R/2)
    PV18__v_d = (PV18__u-V18__u)/(PV18__R/2)
    V17__mu = V17__hem_dep_u_rel*V17__mu_plasma
    V17__R = 8*V17__mu*V17__l/(np.pi*safe_power(V17__r, 4))
    V17__v = (V17__u-V17__u_out)/V17__R
    V18__mu = V18__hem_dep_u_rel*V18__mu_plasma
    V18__R = 8*V18__mu*V18__l/(np.pi*safe_power(V18__r, 4))
    V18__v = (V18__u-V18__u_out)/V18__R
    VV_junc10__u = VV_junc10__q_C/(VV_junc10__C/2)+VV_junc10__u_ext
    VV_junc10__u_mmHg = VV_junc10__u/133.322
    VV_junc10__u_d = VV_junc10__q_C_d/(VV_junc10__C/2)+VV_junc10__u_ext
    VV_junc10__u_d_mmHg = VV_junc10__u_d/133.322
    PV19__mu = PV19__hem_dep_u_rel*PV19__mu_plasma
    PV19__R = 8*PV19__mu*PV19__l/(np.pi*safe_power(PV19__r, 4))+PV19__R_constriction
    PV19__v = (VV_junc10__u_d-PV19__u)/(PV19__R/2)
    PV19__v_d = (PV19__u-V19__u)/(PV19__R/2)
    PV20__mu = PV20__hem_dep_u_rel*PV20__mu_plasma
    PV20__R = 8*PV20__mu*PV20__l/(np.pi*safe_power(PV20__r, 4))+PV20__R_constriction
    PV20__v = (VV_junc10__u_d-PV20__u)/(PV20__R/2)
    PV20__v_d = (PV20__u-V20__u)/(PV20__R/2)
    V19__mu = V19__hem_dep_u_rel*V19__mu_plasma
    V19__R = 8*V19__mu*V19__l/(np.pi*safe_power(V19__r, 4))
    V19__v = (V19__u-V19__u_out)/V19__R
    V20__mu = V20__hem_dep_u_rel*V20__mu_plasma
    V20__R = 8*V20__mu*V20__l/(np.pi*safe_power(V20__r, 4))
    V20__v = (V20__u-V20__u_out)/V20__R
    VV_junc11__u = VV_junc11__q_C/(VV_junc11__C/2)+VV_junc11__u_ext
    VV_junc11__u_mmHg = VV_junc11__u/133.322
    VV_junc11__u_d = VV_junc11__q_C_d/(VV_junc11__C/2)+VV_junc11__u_ext
    VV_junc11__u_d_mmHg = VV_junc11__u_d/133.322
    PV21__mu = PV21__hem_dep_u_rel*PV21__mu_plasma
    PV21__R = 8*PV21__mu*PV21__l/(np.pi*safe_power(PV21__r, 4))+PV21__R_constriction
    PV21__v = (VV_junc11__u_d-PV21__u)/(PV21__R/2)
    PV21__v_d = (PV21__u-V21__u)/(PV21__R/2)
    PV22__mu = PV22__hem_dep_u_rel*PV22__mu_plasma
    PV22__R = 8*PV22__mu*PV22__l/(np.pi*safe_power(PV22__r, 4))+PV22__R_constriction
    PV22__v = (VV_junc11__u_d-PV22__u)/(PV22__R/2)
    PV22__v_d = (PV22__u-V22__u)/(PV22__R/2)
    V21__mu = V21__hem_dep_u_rel*V21__mu_plasma
    V21__R = 8*V21__mu*V21__l/(np.pi*safe_power(V21__r, 4))
    V21__v = (V21__u-V21__u_out)/V21__R
    V22__mu = V22__hem_dep_u_rel*V22__mu_plasma
    V22__R = 8*V22__mu*V22__l/(np.pi*safe_power(V22__r, 4))
    V22__v = (V22__u-V22__u_out)/V22__R
    VV_junc12__u = VV_junc12__q_C/(VV_junc12__C/2)+VV_junc12__u_ext
    VV_junc12__u_mmHg = VV_junc12__u/133.322
    VV_junc12__u_d = VV_junc12__q_C_d/(VV_junc12__C/2)+VV_junc12__u_ext
    VV_junc12__u_d_mmHg = VV_junc12__u_d/133.322
    PV23__mu = PV23__hem_dep_u_rel*PV23__mu_plasma
    PV23__R = 8*PV23__mu*PV23__l/(np.pi*safe_power(PV23__r, 4))+PV23__R_constriction
    PV23__v = (VV_junc12__u_d-PV23__u)/(PV23__R/2)
    PV23__v_d = (PV23__u-V23__u)/(PV23__R/2)
    PV24__mu = PV24__hem_dep_u_rel*PV24__mu_plasma
    PV24__R = 8*PV24__mu*PV24__l/(np.pi*safe_power(PV24__r, 4))+PV24__R_constriction
    PV24__v = (VV_junc12__u_d-PV24__u)/(PV24__R/2)
    PV24__v_d = (PV24__u-V24__u)/(PV24__R/2)
    V23__mu = V23__hem_dep_u_rel*V23__mu_plasma
    V23__R = 8*V23__mu*V23__l/(np.pi*safe_power(V23__r, 4))
    V23__v = (V23__u-V23__u_out)/V23__R
    V24__mu = V24__hem_dep_u_rel*V24__mu_plasma
    V24__R = 8*V24__mu*V24__l/(np.pi*safe_power(V24__r, 4))
    V24__v = (V24__u-V24__u_out)/V24__R
    VV_junc13__u = VV_junc13__q_C/(VV_junc13__C/2)+VV_junc13__u_ext
    VV_junc13__u_mmHg = VV_junc13__u/133.322
    VV_junc13__u_d = VV_junc13__q_C_d/(VV_junc13__C/2)+VV_junc13__u_ext
    VV_junc13__u_d_mmHg = VV_junc13__u_d/133.322
    PV25__mu = PV25__hem_dep_u_rel*PV25__mu_plasma
    PV25__R = 8*PV25__mu*PV25__l/(np.pi*safe_power(PV25__r, 4))+PV25__R_constriction
    PV25__v = (VV_junc13__u_d-PV25__u)/(PV25__R/2)
    PV25__v_d = (PV25__u-V25__u)/(PV25__R/2)
    PV26__mu = PV26__hem_dep_u_rel*PV26__mu_plasma
    PV26__R = 8*PV26__mu*PV26__l/(np.pi*safe_power(PV26__r, 4))+PV26__R_constriction
    PV26__v = (VV_junc13__u_d-PV26__u)/(PV26__R/2)
    PV26__v_d = (PV26__u-V26__u)/(PV26__R/2)
    V25__mu = V25__hem_dep_u_rel*V25__mu_plasma
    V25__R = 8*V25__mu*V25__l/(np.pi*safe_power(V25__r, 4))
    V25__v = (V25__u-V25__u_out)/V25__R
    V26__mu = V26__hem_dep_u_rel*V26__mu_plasma
    V26__R = 8*V26__mu*V26__l/(np.pi*safe_power(V26__r, 4))
    V26__v = (V26__u-V26__u_out)/V26__R
    VV_junc14__u = VV_junc14__q_C/(VV_junc14__C/2)+VV_junc14__u_ext
    VV_junc14__u_mmHg = VV_junc14__u/133.322
    VV_junc14__u_d = VV_junc14__q_C_d/(VV_junc14__C/2)+VV_junc14__u_ext
    VV_junc14__u_d_mmHg = VV_junc14__u_d/133.322
    PV27__mu = PV27__hem_dep_u_rel*PV27__mu_plasma
    PV27__R = 8*PV27__mu*PV27__l/(np.pi*safe_power(PV27__r, 4))+PV27__R_constriction
    PV27__v = (VV_junc14__u_d-PV27__u)/(PV27__R/2)
    PV27__v_d = (PV27__u-V27__u)/(PV27__R/2)
    PV28__mu = PV28__hem_dep_u_rel*PV28__mu_plasma
    PV28__R = 8*PV28__mu*PV28__l/(np.pi*safe_power(PV28__r, 4))+PV28__R_constriction
    PV28__v = (VV_junc14__u_d-PV28__u)/(PV28__R/2)
    PV28__v_d = (PV28__u-V28__u)/(PV28__R/2)
    V27__mu = V27__hem_dep_u_rel*V27__mu_plasma
    V27__R = 8*V27__mu*V27__l/(np.pi*safe_power(V27__r, 4))
    V27__v = (V27__u-V27__u_out)/V27__R
    V28__mu = V28__hem_dep_u_rel*V28__mu_plasma
    V28__R = 8*V28__mu*V28__l/(np.pi*safe_power(V28__r, 4))
    V28__v = (V28__u-V28__u_out)/V28__R
    VV_junc15__u = VV_junc15__q_C/(VV_junc15__C/2)+VV_junc15__u_ext
    VV_junc15__u_mmHg = VV_junc15__u/133.322
    VV_junc15__u_d = VV_junc15__q_C_d/(VV_junc15__C/2)+VV_junc15__u_ext
    VV_junc15__u_d_mmHg = VV_junc15__u_d/133.322
    PV29__mu = PV29__hem_dep_u_rel*PV29__mu_plasma
    PV29__R = 8*PV29__mu*PV29__l/(np.pi*safe_power(PV29__r, 4))+PV29__R_constriction
    PV29__v = (VV_junc15__u_d-PV29__u)/(PV29__R/2)
    PV29__v_d = (PV29__u-V29__u)/(PV29__R/2)
    PV30__mu = PV30__hem_dep_u_rel*PV30__mu_plasma
    PV30__R = 8*PV30__mu*PV30__l/(np.pi*safe_power(PV30__r, 4))+PV30__R_constriction
    PV30__v = (VV_junc15__u_d-PV30__u)/(PV30__R/2)
    PV30__v_d = (PV30__u-V30__u)/(PV30__R/2)
    V29__mu = V29__hem_dep_u_rel*V29__mu_plasma
    V29__R = 8*V29__mu*V29__l/(np.pi*safe_power(V29__r, 4))
    V29__v = (V29__u-V29__u_out)/V29__R
    V30__mu = V30__hem_dep_u_rel*V30__mu_plasma
    V30__R = 8*V30__mu*V30__l/(np.pi*safe_power(V30__r, 4))
    V30__v = (V30__u-V30__u_out)/V30__R
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
    V7__v = (V7__u-VV_junc8__u)/V7__R
    V8__v = (V8__u-VV_junc9__u)/V8__R
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
    V9__v = (V9__u-VV_junc10__u)/V9__R
    V10__v = (V10__u-VV_junc11__u)/V10__R
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
    V11__v = (V11__u-VV_junc12__u)/V11__R
    V12__v = (V12__u-VV_junc13__u)/V12__R
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
    V13__v = (V13__u-VV_junc14__u)/V13__R
    V14__v = (V14__u-VV_junc15__u)/V14__R
    VV_junc8__vj1 = V7__v
    VV_junc8__vj3 = -PV15__v
    VV_junc8__vj4 = -PV16__v
    VV_junc8__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc8__vj1/VV_junc8__v_scale)
    VV_junc8__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc8__vj3/VV_junc8__v_scale)
    VV_junc8__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc8__vj4/VV_junc8__v_scale)
    VV_junc8__w_out1 = 1-VV_junc8__w_in1
    VV_junc8__w_out3 = 1-VV_junc8__w_in3
    VV_junc8__w_out4 = 1-VV_junc8__w_in4
    VV_junc8__Qin1 = VV_junc8__w_in1*VV_junc8__vj1
    VV_junc8__Qin3 = VV_junc8__w_in3*VV_junc8__vj3
    VV_junc8__Qin4 = VV_junc8__w_in4*VV_junc8__vj4
    VV_junc8__Qout1 = VV_junc8__w_out1*-VV_junc8__vj1
    VV_junc8__Qout3 = VV_junc8__w_out3*-VV_junc8__vj3
    VV_junc8__Qout4 = VV_junc8__w_out4*-VV_junc8__vj4
    VV_junc8__Qin_tot = VV_junc8__Qin1+VV_junc8__Qin2+VV_junc8__Qin3+VV_junc8__Qin4
    VV_junc8__Qout_tot = VV_junc8__Qout1+VV_junc8__Qout2+VV_junc8__Qout3+VV_junc8__Qout4
    VV_junc8__v = (VV_junc8__u-VV_junc8__u_d)/VV_junc8__R_VV_junc
    VV_junc8__bc1_is_in = (1 if VV_junc8__Qin1 > VV_junc8__v_threshold else 0)
    VV_junc8__bc3_is_in = (1 if VV_junc8__Qin3 > VV_junc8__v_threshold else 0)
    VV_junc8__bc4_is_in = (1 if VV_junc8__Qin4 > VV_junc8__v_threshold else 0)
    VV_junc8__bc1_is_out = (1 if VV_junc8__Qout1 > VV_junc8__v_threshold else 0)
    VV_junc8__bc3_is_out = (1 if VV_junc8__Qout3 > VV_junc8__v_threshold else 0)
    VV_junc8__bc4_is_out = (1 if VV_junc8__Qout4 > VV_junc8__v_threshold else 0)
    PV15__w_v = 0.5+1/np.pi*np.arctan(PV15__v/PV15__v_scale)
    PV15__w_v_d = 0.5+1/np.pi*np.arctan(PV15__v_d/PV15__v_scale)
    PV15__H_up = PV15__w_v_d*PV15__H_L_in+(1-PV15__w_v_d)*PV15__H_R_in
    PV15__s_v_d = np.abs(PV15__v_d)/(np.abs(PV15__v_d)+PV15__v_eps)
    PV15__H_L_out = (1-PV15__w_v_d)*PV15__H_down+PV15__w_v_d*PV15__H_L_in
    PV15__H_R_out = PV15__w_v_d*PV15__H_down+(1-PV15__w_v_d)*PV15__H_R_in
    PV15__v_pos = PV15__w_v*PV15__v
    PV15__v_neg = (1-PV15__w_v)*-PV15__v
    PV15__v_d_pos = PV15__w_v_d*PV15__v_d
    PV15__v_d_neg = (1-PV15__w_v_d)*-PV15__v_d
    PV15__H_volume_L = PV15__w_v*PV15__H_L_in+(1-PV15__w_v)*PV15__H_L_out
    PV15__H_volume_R = PV15__w_v_d*PV15__H_R_out+(1-PV15__w_v_d)*PV15__H_R_in
    PV15__v_mm3_s = PV15__v/PV15__one_mm3
    PV15__v_d_mm3_s = PV15__v_d/PV15__one_mm3
    PV16__w_v = 0.5+1/np.pi*np.arctan(PV16__v/PV16__v_scale)
    PV16__w_v_d = 0.5+1/np.pi*np.arctan(PV16__v_d/PV16__v_scale)
    PV16__H_up = PV16__w_v_d*PV16__H_L_in+(1-PV16__w_v_d)*PV16__H_R_in
    PV16__s_v_d = np.abs(PV16__v_d)/(np.abs(PV16__v_d)+PV16__v_eps)
    PV16__H_L_out = (1-PV16__w_v_d)*PV16__H_down+PV16__w_v_d*PV16__H_L_in
    PV16__H_R_out = PV16__w_v_d*PV16__H_down+(1-PV16__w_v_d)*PV16__H_R_in
    PV16__v_pos = PV16__w_v*PV16__v
    PV16__v_neg = (1-PV16__w_v)*-PV16__v
    PV16__v_d_pos = PV16__w_v_d*PV16__v_d
    PV16__v_d_neg = (1-PV16__w_v_d)*-PV16__v_d
    PV16__H_volume_L = PV16__w_v*PV16__H_L_in+(1-PV16__w_v)*PV16__H_L_out
    PV16__H_volume_R = PV16__w_v_d*PV16__H_R_out+(1-PV16__w_v_d)*PV16__H_R_in
    PV16__v_mm3_s = PV16__v/PV16__one_mm3
    PV16__v_d_mm3_s = PV16__v_d/PV16__one_mm3
    V15__w_v = 0.5+1/np.pi*np.arctan(V15__v/V15__v_scale)
    V15__H_up = V15__w_v*V15__H_L_in+(1-V15__w_v)*V15__H_R_in
    V15__s_v = np.abs(V15__v)/(np.abs(V15__v)+V15__v_eps)
    V15__H_L_out = (1-V15__w_v)*V15__H_down+V15__w_v*V15__H_L_in
    V15__H_R_out = V15__w_v*V15__H_down+(1-V15__w_v)*V15__H_R_in
    V15__v_pos = V15__w_v*V15__v
    V15__v_neg = (1-V15__w_v)*-V15__v
    V15__H_volume_L = V15__w_v*V15__H_L_in+(1-V15__w_v)*V15__H_L_out
    V15__H_volume_R = V15__w_v*V15__H_R_out+(1-V15__w_v)*V15__H_R_in
    V15__v_mm3_s = V15__v/V15__one_mm3
    V16__w_v = 0.5+1/np.pi*np.arctan(V16__v/V16__v_scale)
    V16__H_up = V16__w_v*V16__H_L_in+(1-V16__w_v)*V16__H_R_in
    V16__s_v = np.abs(V16__v)/(np.abs(V16__v)+V16__v_eps)
    V16__H_L_out = (1-V16__w_v)*V16__H_down+V16__w_v*V16__H_L_in
    V16__H_R_out = V16__w_v*V16__H_down+(1-V16__w_v)*V16__H_R_in
    V16__v_pos = V16__w_v*V16__v
    V16__v_neg = (1-V16__w_v)*-V16__v
    V16__H_volume_L = V16__w_v*V16__H_L_in+(1-V16__w_v)*V16__H_L_out
    V16__H_volume_R = V16__w_v*V16__H_R_out+(1-V16__w_v)*V16__H_R_in
    V16__v_mm3_s = V16__v/V16__one_mm3
    VV_junc9__vj1 = V8__v
    VV_junc9__vj3 = -PV17__v
    VV_junc9__vj4 = -PV18__v
    VV_junc9__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc9__vj1/VV_junc9__v_scale)
    VV_junc9__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc9__vj3/VV_junc9__v_scale)
    VV_junc9__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc9__vj4/VV_junc9__v_scale)
    VV_junc9__w_out1 = 1-VV_junc9__w_in1
    VV_junc9__w_out3 = 1-VV_junc9__w_in3
    VV_junc9__w_out4 = 1-VV_junc9__w_in4
    VV_junc9__Qin1 = VV_junc9__w_in1*VV_junc9__vj1
    VV_junc9__Qin3 = VV_junc9__w_in3*VV_junc9__vj3
    VV_junc9__Qin4 = VV_junc9__w_in4*VV_junc9__vj4
    VV_junc9__Qout1 = VV_junc9__w_out1*-VV_junc9__vj1
    VV_junc9__Qout3 = VV_junc9__w_out3*-VV_junc9__vj3
    VV_junc9__Qout4 = VV_junc9__w_out4*-VV_junc9__vj4
    VV_junc9__Qin_tot = VV_junc9__Qin1+VV_junc9__Qin2+VV_junc9__Qin3+VV_junc9__Qin4
    VV_junc9__Qout_tot = VV_junc9__Qout1+VV_junc9__Qout2+VV_junc9__Qout3+VV_junc9__Qout4
    VV_junc9__v = (VV_junc9__u-VV_junc9__u_d)/VV_junc9__R_VV_junc
    VV_junc9__bc1_is_in = (1 if VV_junc9__Qin1 > VV_junc9__v_threshold else 0)
    VV_junc9__bc3_is_in = (1 if VV_junc9__Qin3 > VV_junc9__v_threshold else 0)
    VV_junc9__bc4_is_in = (1 if VV_junc9__Qin4 > VV_junc9__v_threshold else 0)
    VV_junc9__bc1_is_out = (1 if VV_junc9__Qout1 > VV_junc9__v_threshold else 0)
    VV_junc9__bc3_is_out = (1 if VV_junc9__Qout3 > VV_junc9__v_threshold else 0)
    VV_junc9__bc4_is_out = (1 if VV_junc9__Qout4 > VV_junc9__v_threshold else 0)
    PV17__w_v = 0.5+1/np.pi*np.arctan(PV17__v/PV17__v_scale)
    PV17__w_v_d = 0.5+1/np.pi*np.arctan(PV17__v_d/PV17__v_scale)
    PV17__H_up = PV17__w_v_d*PV17__H_L_in+(1-PV17__w_v_d)*PV17__H_R_in
    PV17__s_v_d = np.abs(PV17__v_d)/(np.abs(PV17__v_d)+PV17__v_eps)
    PV17__H_L_out = (1-PV17__w_v_d)*PV17__H_down+PV17__w_v_d*PV17__H_L_in
    PV17__H_R_out = PV17__w_v_d*PV17__H_down+(1-PV17__w_v_d)*PV17__H_R_in
    PV17__v_pos = PV17__w_v*PV17__v
    PV17__v_neg = (1-PV17__w_v)*-PV17__v
    PV17__v_d_pos = PV17__w_v_d*PV17__v_d
    PV17__v_d_neg = (1-PV17__w_v_d)*-PV17__v_d
    PV17__H_volume_L = PV17__w_v*PV17__H_L_in+(1-PV17__w_v)*PV17__H_L_out
    PV17__H_volume_R = PV17__w_v_d*PV17__H_R_out+(1-PV17__w_v_d)*PV17__H_R_in
    PV17__v_mm3_s = PV17__v/PV17__one_mm3
    PV17__v_d_mm3_s = PV17__v_d/PV17__one_mm3
    PV18__w_v = 0.5+1/np.pi*np.arctan(PV18__v/PV18__v_scale)
    PV18__w_v_d = 0.5+1/np.pi*np.arctan(PV18__v_d/PV18__v_scale)
    PV18__H_up = PV18__w_v_d*PV18__H_L_in+(1-PV18__w_v_d)*PV18__H_R_in
    PV18__s_v_d = np.abs(PV18__v_d)/(np.abs(PV18__v_d)+PV18__v_eps)
    PV18__H_L_out = (1-PV18__w_v_d)*PV18__H_down+PV18__w_v_d*PV18__H_L_in
    PV18__H_R_out = PV18__w_v_d*PV18__H_down+(1-PV18__w_v_d)*PV18__H_R_in
    PV18__v_pos = PV18__w_v*PV18__v
    PV18__v_neg = (1-PV18__w_v)*-PV18__v
    PV18__v_d_pos = PV18__w_v_d*PV18__v_d
    PV18__v_d_neg = (1-PV18__w_v_d)*-PV18__v_d
    PV18__H_volume_L = PV18__w_v*PV18__H_L_in+(1-PV18__w_v)*PV18__H_L_out
    PV18__H_volume_R = PV18__w_v_d*PV18__H_R_out+(1-PV18__w_v_d)*PV18__H_R_in
    PV18__v_mm3_s = PV18__v/PV18__one_mm3
    PV18__v_d_mm3_s = PV18__v_d/PV18__one_mm3
    V17__w_v = 0.5+1/np.pi*np.arctan(V17__v/V17__v_scale)
    V17__H_up = V17__w_v*V17__H_L_in+(1-V17__w_v)*V17__H_R_in
    V17__s_v = np.abs(V17__v)/(np.abs(V17__v)+V17__v_eps)
    V17__H_L_out = (1-V17__w_v)*V17__H_down+V17__w_v*V17__H_L_in
    V17__H_R_out = V17__w_v*V17__H_down+(1-V17__w_v)*V17__H_R_in
    V17__v_pos = V17__w_v*V17__v
    V17__v_neg = (1-V17__w_v)*-V17__v
    V17__H_volume_L = V17__w_v*V17__H_L_in+(1-V17__w_v)*V17__H_L_out
    V17__H_volume_R = V17__w_v*V17__H_R_out+(1-V17__w_v)*V17__H_R_in
    V17__v_mm3_s = V17__v/V17__one_mm3
    V18__w_v = 0.5+1/np.pi*np.arctan(V18__v/V18__v_scale)
    V18__H_up = V18__w_v*V18__H_L_in+(1-V18__w_v)*V18__H_R_in
    V18__s_v = np.abs(V18__v)/(np.abs(V18__v)+V18__v_eps)
    V18__H_L_out = (1-V18__w_v)*V18__H_down+V18__w_v*V18__H_L_in
    V18__H_R_out = V18__w_v*V18__H_down+(1-V18__w_v)*V18__H_R_in
    V18__v_pos = V18__w_v*V18__v
    V18__v_neg = (1-V18__w_v)*-V18__v
    V18__H_volume_L = V18__w_v*V18__H_L_in+(1-V18__w_v)*V18__H_L_out
    V18__H_volume_R = V18__w_v*V18__H_R_out+(1-V18__w_v)*V18__H_R_in
    V18__v_mm3_s = V18__v/V18__one_mm3
    VV_junc10__vj1 = V9__v
    VV_junc10__vj3 = -PV19__v
    VV_junc10__vj4 = -PV20__v
    VV_junc10__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc10__vj1/VV_junc10__v_scale)
    VV_junc10__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc10__vj3/VV_junc10__v_scale)
    VV_junc10__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc10__vj4/VV_junc10__v_scale)
    VV_junc10__w_out1 = 1-VV_junc10__w_in1
    VV_junc10__w_out3 = 1-VV_junc10__w_in3
    VV_junc10__w_out4 = 1-VV_junc10__w_in4
    VV_junc10__Qin1 = VV_junc10__w_in1*VV_junc10__vj1
    VV_junc10__Qin3 = VV_junc10__w_in3*VV_junc10__vj3
    VV_junc10__Qin4 = VV_junc10__w_in4*VV_junc10__vj4
    VV_junc10__Qout1 = VV_junc10__w_out1*-VV_junc10__vj1
    VV_junc10__Qout3 = VV_junc10__w_out3*-VV_junc10__vj3
    VV_junc10__Qout4 = VV_junc10__w_out4*-VV_junc10__vj4
    VV_junc10__Qin_tot = VV_junc10__Qin1+VV_junc10__Qin2+VV_junc10__Qin3+VV_junc10__Qin4
    VV_junc10__Qout_tot = VV_junc10__Qout1+VV_junc10__Qout2+VV_junc10__Qout3+VV_junc10__Qout4
    VV_junc10__v = (VV_junc10__u-VV_junc10__u_d)/VV_junc10__R_VV_junc
    VV_junc10__bc1_is_in = (1 if VV_junc10__Qin1 > VV_junc10__v_threshold else 0)
    VV_junc10__bc3_is_in = (1 if VV_junc10__Qin3 > VV_junc10__v_threshold else 0)
    VV_junc10__bc4_is_in = (1 if VV_junc10__Qin4 > VV_junc10__v_threshold else 0)
    VV_junc10__bc1_is_out = (1 if VV_junc10__Qout1 > VV_junc10__v_threshold else 0)
    VV_junc10__bc3_is_out = (1 if VV_junc10__Qout3 > VV_junc10__v_threshold else 0)
    VV_junc10__bc4_is_out = (1 if VV_junc10__Qout4 > VV_junc10__v_threshold else 0)
    PV19__w_v = 0.5+1/np.pi*np.arctan(PV19__v/PV19__v_scale)
    PV19__w_v_d = 0.5+1/np.pi*np.arctan(PV19__v_d/PV19__v_scale)
    PV19__H_up = PV19__w_v_d*PV19__H_L_in+(1-PV19__w_v_d)*PV19__H_R_in
    PV19__s_v_d = np.abs(PV19__v_d)/(np.abs(PV19__v_d)+PV19__v_eps)
    PV19__H_L_out = (1-PV19__w_v_d)*PV19__H_down+PV19__w_v_d*PV19__H_L_in
    PV19__H_R_out = PV19__w_v_d*PV19__H_down+(1-PV19__w_v_d)*PV19__H_R_in
    PV19__v_pos = PV19__w_v*PV19__v
    PV19__v_neg = (1-PV19__w_v)*-PV19__v
    PV19__v_d_pos = PV19__w_v_d*PV19__v_d
    PV19__v_d_neg = (1-PV19__w_v_d)*-PV19__v_d
    PV19__H_volume_L = PV19__w_v*PV19__H_L_in+(1-PV19__w_v)*PV19__H_L_out
    PV19__H_volume_R = PV19__w_v_d*PV19__H_R_out+(1-PV19__w_v_d)*PV19__H_R_in
    PV19__v_mm3_s = PV19__v/PV19__one_mm3
    PV19__v_d_mm3_s = PV19__v_d/PV19__one_mm3
    PV20__w_v = 0.5+1/np.pi*np.arctan(PV20__v/PV20__v_scale)
    PV20__w_v_d = 0.5+1/np.pi*np.arctan(PV20__v_d/PV20__v_scale)
    PV20__H_up = PV20__w_v_d*PV20__H_L_in+(1-PV20__w_v_d)*PV20__H_R_in
    PV20__s_v_d = np.abs(PV20__v_d)/(np.abs(PV20__v_d)+PV20__v_eps)
    PV20__H_L_out = (1-PV20__w_v_d)*PV20__H_down+PV20__w_v_d*PV20__H_L_in
    PV20__H_R_out = PV20__w_v_d*PV20__H_down+(1-PV20__w_v_d)*PV20__H_R_in
    PV20__v_pos = PV20__w_v*PV20__v
    PV20__v_neg = (1-PV20__w_v)*-PV20__v
    PV20__v_d_pos = PV20__w_v_d*PV20__v_d
    PV20__v_d_neg = (1-PV20__w_v_d)*-PV20__v_d
    PV20__H_volume_L = PV20__w_v*PV20__H_L_in+(1-PV20__w_v)*PV20__H_L_out
    PV20__H_volume_R = PV20__w_v_d*PV20__H_R_out+(1-PV20__w_v_d)*PV20__H_R_in
    PV20__v_mm3_s = PV20__v/PV20__one_mm3
    PV20__v_d_mm3_s = PV20__v_d/PV20__one_mm3
    V19__w_v = 0.5+1/np.pi*np.arctan(V19__v/V19__v_scale)
    V19__H_up = V19__w_v*V19__H_L_in+(1-V19__w_v)*V19__H_R_in
    V19__s_v = np.abs(V19__v)/(np.abs(V19__v)+V19__v_eps)
    V19__H_L_out = (1-V19__w_v)*V19__H_down+V19__w_v*V19__H_L_in
    V19__H_R_out = V19__w_v*V19__H_down+(1-V19__w_v)*V19__H_R_in
    V19__v_pos = V19__w_v*V19__v
    V19__v_neg = (1-V19__w_v)*-V19__v
    V19__H_volume_L = V19__w_v*V19__H_L_in+(1-V19__w_v)*V19__H_L_out
    V19__H_volume_R = V19__w_v*V19__H_R_out+(1-V19__w_v)*V19__H_R_in
    V19__v_mm3_s = V19__v/V19__one_mm3
    V20__w_v = 0.5+1/np.pi*np.arctan(V20__v/V20__v_scale)
    V20__H_up = V20__w_v*V20__H_L_in+(1-V20__w_v)*V20__H_R_in
    V20__s_v = np.abs(V20__v)/(np.abs(V20__v)+V20__v_eps)
    V20__H_L_out = (1-V20__w_v)*V20__H_down+V20__w_v*V20__H_L_in
    V20__H_R_out = V20__w_v*V20__H_down+(1-V20__w_v)*V20__H_R_in
    V20__v_pos = V20__w_v*V20__v
    V20__v_neg = (1-V20__w_v)*-V20__v
    V20__H_volume_L = V20__w_v*V20__H_L_in+(1-V20__w_v)*V20__H_L_out
    V20__H_volume_R = V20__w_v*V20__H_R_out+(1-V20__w_v)*V20__H_R_in
    V20__v_mm3_s = V20__v/V20__one_mm3
    VV_junc11__vj1 = V10__v
    VV_junc11__vj3 = -PV21__v
    VV_junc11__vj4 = -PV22__v
    VV_junc11__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc11__vj1/VV_junc11__v_scale)
    VV_junc11__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc11__vj3/VV_junc11__v_scale)
    VV_junc11__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc11__vj4/VV_junc11__v_scale)
    VV_junc11__w_out1 = 1-VV_junc11__w_in1
    VV_junc11__w_out3 = 1-VV_junc11__w_in3
    VV_junc11__w_out4 = 1-VV_junc11__w_in4
    VV_junc11__Qin1 = VV_junc11__w_in1*VV_junc11__vj1
    VV_junc11__Qin3 = VV_junc11__w_in3*VV_junc11__vj3
    VV_junc11__Qin4 = VV_junc11__w_in4*VV_junc11__vj4
    VV_junc11__Qout1 = VV_junc11__w_out1*-VV_junc11__vj1
    VV_junc11__Qout3 = VV_junc11__w_out3*-VV_junc11__vj3
    VV_junc11__Qout4 = VV_junc11__w_out4*-VV_junc11__vj4
    VV_junc11__Qin_tot = VV_junc11__Qin1+VV_junc11__Qin2+VV_junc11__Qin3+VV_junc11__Qin4
    VV_junc11__Qout_tot = VV_junc11__Qout1+VV_junc11__Qout2+VV_junc11__Qout3+VV_junc11__Qout4
    VV_junc11__v = (VV_junc11__u-VV_junc11__u_d)/VV_junc11__R_VV_junc
    VV_junc11__bc1_is_in = (1 if VV_junc11__Qin1 > VV_junc11__v_threshold else 0)
    VV_junc11__bc3_is_in = (1 if VV_junc11__Qin3 > VV_junc11__v_threshold else 0)
    VV_junc11__bc4_is_in = (1 if VV_junc11__Qin4 > VV_junc11__v_threshold else 0)
    VV_junc11__bc1_is_out = (1 if VV_junc11__Qout1 > VV_junc11__v_threshold else 0)
    VV_junc11__bc3_is_out = (1 if VV_junc11__Qout3 > VV_junc11__v_threshold else 0)
    VV_junc11__bc4_is_out = (1 if VV_junc11__Qout4 > VV_junc11__v_threshold else 0)
    PV21__w_v = 0.5+1/np.pi*np.arctan(PV21__v/PV21__v_scale)
    PV21__w_v_d = 0.5+1/np.pi*np.arctan(PV21__v_d/PV21__v_scale)
    PV21__H_up = PV21__w_v_d*PV21__H_L_in+(1-PV21__w_v_d)*PV21__H_R_in
    PV21__s_v_d = np.abs(PV21__v_d)/(np.abs(PV21__v_d)+PV21__v_eps)
    PV21__H_L_out = (1-PV21__w_v_d)*PV21__H_down+PV21__w_v_d*PV21__H_L_in
    PV21__H_R_out = PV21__w_v_d*PV21__H_down+(1-PV21__w_v_d)*PV21__H_R_in
    PV21__v_pos = PV21__w_v*PV21__v
    PV21__v_neg = (1-PV21__w_v)*-PV21__v
    PV21__v_d_pos = PV21__w_v_d*PV21__v_d
    PV21__v_d_neg = (1-PV21__w_v_d)*-PV21__v_d
    PV21__H_volume_L = PV21__w_v*PV21__H_L_in+(1-PV21__w_v)*PV21__H_L_out
    PV21__H_volume_R = PV21__w_v_d*PV21__H_R_out+(1-PV21__w_v_d)*PV21__H_R_in
    PV21__v_mm3_s = PV21__v/PV21__one_mm3
    PV21__v_d_mm3_s = PV21__v_d/PV21__one_mm3
    PV22__w_v = 0.5+1/np.pi*np.arctan(PV22__v/PV22__v_scale)
    PV22__w_v_d = 0.5+1/np.pi*np.arctan(PV22__v_d/PV22__v_scale)
    PV22__H_up = PV22__w_v_d*PV22__H_L_in+(1-PV22__w_v_d)*PV22__H_R_in
    PV22__s_v_d = np.abs(PV22__v_d)/(np.abs(PV22__v_d)+PV22__v_eps)
    PV22__H_L_out = (1-PV22__w_v_d)*PV22__H_down+PV22__w_v_d*PV22__H_L_in
    PV22__H_R_out = PV22__w_v_d*PV22__H_down+(1-PV22__w_v_d)*PV22__H_R_in
    PV22__v_pos = PV22__w_v*PV22__v
    PV22__v_neg = (1-PV22__w_v)*-PV22__v
    PV22__v_d_pos = PV22__w_v_d*PV22__v_d
    PV22__v_d_neg = (1-PV22__w_v_d)*-PV22__v_d
    PV22__H_volume_L = PV22__w_v*PV22__H_L_in+(1-PV22__w_v)*PV22__H_L_out
    PV22__H_volume_R = PV22__w_v_d*PV22__H_R_out+(1-PV22__w_v_d)*PV22__H_R_in
    PV22__v_mm3_s = PV22__v/PV22__one_mm3
    PV22__v_d_mm3_s = PV22__v_d/PV22__one_mm3
    V21__w_v = 0.5+1/np.pi*np.arctan(V21__v/V21__v_scale)
    V21__H_up = V21__w_v*V21__H_L_in+(1-V21__w_v)*V21__H_R_in
    V21__s_v = np.abs(V21__v)/(np.abs(V21__v)+V21__v_eps)
    V21__H_L_out = (1-V21__w_v)*V21__H_down+V21__w_v*V21__H_L_in
    V21__H_R_out = V21__w_v*V21__H_down+(1-V21__w_v)*V21__H_R_in
    V21__v_pos = V21__w_v*V21__v
    V21__v_neg = (1-V21__w_v)*-V21__v
    V21__H_volume_L = V21__w_v*V21__H_L_in+(1-V21__w_v)*V21__H_L_out
    V21__H_volume_R = V21__w_v*V21__H_R_out+(1-V21__w_v)*V21__H_R_in
    V21__v_mm3_s = V21__v/V21__one_mm3
    V22__w_v = 0.5+1/np.pi*np.arctan(V22__v/V22__v_scale)
    V22__H_up = V22__w_v*V22__H_L_in+(1-V22__w_v)*V22__H_R_in
    V22__s_v = np.abs(V22__v)/(np.abs(V22__v)+V22__v_eps)
    V22__H_L_out = (1-V22__w_v)*V22__H_down+V22__w_v*V22__H_L_in
    V22__H_R_out = V22__w_v*V22__H_down+(1-V22__w_v)*V22__H_R_in
    V22__v_pos = V22__w_v*V22__v
    V22__v_neg = (1-V22__w_v)*-V22__v
    V22__H_volume_L = V22__w_v*V22__H_L_in+(1-V22__w_v)*V22__H_L_out
    V22__H_volume_R = V22__w_v*V22__H_R_out+(1-V22__w_v)*V22__H_R_in
    V22__v_mm3_s = V22__v/V22__one_mm3
    VV_junc12__vj1 = V11__v
    VV_junc12__vj3 = -PV23__v
    VV_junc12__vj4 = -PV24__v
    VV_junc12__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc12__vj1/VV_junc12__v_scale)
    VV_junc12__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc12__vj3/VV_junc12__v_scale)
    VV_junc12__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc12__vj4/VV_junc12__v_scale)
    VV_junc12__w_out1 = 1-VV_junc12__w_in1
    VV_junc12__w_out3 = 1-VV_junc12__w_in3
    VV_junc12__w_out4 = 1-VV_junc12__w_in4
    VV_junc12__Qin1 = VV_junc12__w_in1*VV_junc12__vj1
    VV_junc12__Qin3 = VV_junc12__w_in3*VV_junc12__vj3
    VV_junc12__Qin4 = VV_junc12__w_in4*VV_junc12__vj4
    VV_junc12__Qout1 = VV_junc12__w_out1*-VV_junc12__vj1
    VV_junc12__Qout3 = VV_junc12__w_out3*-VV_junc12__vj3
    VV_junc12__Qout4 = VV_junc12__w_out4*-VV_junc12__vj4
    VV_junc12__Qin_tot = VV_junc12__Qin1+VV_junc12__Qin2+VV_junc12__Qin3+VV_junc12__Qin4
    VV_junc12__Qout_tot = VV_junc12__Qout1+VV_junc12__Qout2+VV_junc12__Qout3+VV_junc12__Qout4
    VV_junc12__v = (VV_junc12__u-VV_junc12__u_d)/VV_junc12__R_VV_junc
    VV_junc12__bc1_is_in = (1 if VV_junc12__Qin1 > VV_junc12__v_threshold else 0)
    VV_junc12__bc3_is_in = (1 if VV_junc12__Qin3 > VV_junc12__v_threshold else 0)
    VV_junc12__bc4_is_in = (1 if VV_junc12__Qin4 > VV_junc12__v_threshold else 0)
    VV_junc12__bc1_is_out = (1 if VV_junc12__Qout1 > VV_junc12__v_threshold else 0)
    VV_junc12__bc3_is_out = (1 if VV_junc12__Qout3 > VV_junc12__v_threshold else 0)
    VV_junc12__bc4_is_out = (1 if VV_junc12__Qout4 > VV_junc12__v_threshold else 0)
    PV23__w_v = 0.5+1/np.pi*np.arctan(PV23__v/PV23__v_scale)
    PV23__w_v_d = 0.5+1/np.pi*np.arctan(PV23__v_d/PV23__v_scale)
    PV23__H_up = PV23__w_v_d*PV23__H_L_in+(1-PV23__w_v_d)*PV23__H_R_in
    PV23__s_v_d = np.abs(PV23__v_d)/(np.abs(PV23__v_d)+PV23__v_eps)
    PV23__H_L_out = (1-PV23__w_v_d)*PV23__H_down+PV23__w_v_d*PV23__H_L_in
    PV23__H_R_out = PV23__w_v_d*PV23__H_down+(1-PV23__w_v_d)*PV23__H_R_in
    PV23__v_pos = PV23__w_v*PV23__v
    PV23__v_neg = (1-PV23__w_v)*-PV23__v
    PV23__v_d_pos = PV23__w_v_d*PV23__v_d
    PV23__v_d_neg = (1-PV23__w_v_d)*-PV23__v_d
    PV23__H_volume_L = PV23__w_v*PV23__H_L_in+(1-PV23__w_v)*PV23__H_L_out
    PV23__H_volume_R = PV23__w_v_d*PV23__H_R_out+(1-PV23__w_v_d)*PV23__H_R_in
    PV23__v_mm3_s = PV23__v/PV23__one_mm3
    PV23__v_d_mm3_s = PV23__v_d/PV23__one_mm3
    PV24__w_v = 0.5+1/np.pi*np.arctan(PV24__v/PV24__v_scale)
    PV24__w_v_d = 0.5+1/np.pi*np.arctan(PV24__v_d/PV24__v_scale)
    PV24__H_up = PV24__w_v_d*PV24__H_L_in+(1-PV24__w_v_d)*PV24__H_R_in
    PV24__s_v_d = np.abs(PV24__v_d)/(np.abs(PV24__v_d)+PV24__v_eps)
    PV24__H_L_out = (1-PV24__w_v_d)*PV24__H_down+PV24__w_v_d*PV24__H_L_in
    PV24__H_R_out = PV24__w_v_d*PV24__H_down+(1-PV24__w_v_d)*PV24__H_R_in
    PV24__v_pos = PV24__w_v*PV24__v
    PV24__v_neg = (1-PV24__w_v)*-PV24__v
    PV24__v_d_pos = PV24__w_v_d*PV24__v_d
    PV24__v_d_neg = (1-PV24__w_v_d)*-PV24__v_d
    PV24__H_volume_L = PV24__w_v*PV24__H_L_in+(1-PV24__w_v)*PV24__H_L_out
    PV24__H_volume_R = PV24__w_v_d*PV24__H_R_out+(1-PV24__w_v_d)*PV24__H_R_in
    PV24__v_mm3_s = PV24__v/PV24__one_mm3
    PV24__v_d_mm3_s = PV24__v_d/PV24__one_mm3
    V23__w_v = 0.5+1/np.pi*np.arctan(V23__v/V23__v_scale)
    V23__H_up = V23__w_v*V23__H_L_in+(1-V23__w_v)*V23__H_R_in
    V23__s_v = np.abs(V23__v)/(np.abs(V23__v)+V23__v_eps)
    V23__H_L_out = (1-V23__w_v)*V23__H_down+V23__w_v*V23__H_L_in
    V23__H_R_out = V23__w_v*V23__H_down+(1-V23__w_v)*V23__H_R_in
    V23__v_pos = V23__w_v*V23__v
    V23__v_neg = (1-V23__w_v)*-V23__v
    V23__H_volume_L = V23__w_v*V23__H_L_in+(1-V23__w_v)*V23__H_L_out
    V23__H_volume_R = V23__w_v*V23__H_R_out+(1-V23__w_v)*V23__H_R_in
    V23__v_mm3_s = V23__v/V23__one_mm3
    V24__w_v = 0.5+1/np.pi*np.arctan(V24__v/V24__v_scale)
    V24__H_up = V24__w_v*V24__H_L_in+(1-V24__w_v)*V24__H_R_in
    V24__s_v = np.abs(V24__v)/(np.abs(V24__v)+V24__v_eps)
    V24__H_L_out = (1-V24__w_v)*V24__H_down+V24__w_v*V24__H_L_in
    V24__H_R_out = V24__w_v*V24__H_down+(1-V24__w_v)*V24__H_R_in
    V24__v_pos = V24__w_v*V24__v
    V24__v_neg = (1-V24__w_v)*-V24__v
    V24__H_volume_L = V24__w_v*V24__H_L_in+(1-V24__w_v)*V24__H_L_out
    V24__H_volume_R = V24__w_v*V24__H_R_out+(1-V24__w_v)*V24__H_R_in
    V24__v_mm3_s = V24__v/V24__one_mm3
    VV_junc13__vj1 = V12__v
    VV_junc13__vj3 = -PV25__v
    VV_junc13__vj4 = -PV26__v
    VV_junc13__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc13__vj1/VV_junc13__v_scale)
    VV_junc13__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc13__vj3/VV_junc13__v_scale)
    VV_junc13__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc13__vj4/VV_junc13__v_scale)
    VV_junc13__w_out1 = 1-VV_junc13__w_in1
    VV_junc13__w_out3 = 1-VV_junc13__w_in3
    VV_junc13__w_out4 = 1-VV_junc13__w_in4
    VV_junc13__Qin1 = VV_junc13__w_in1*VV_junc13__vj1
    VV_junc13__Qin3 = VV_junc13__w_in3*VV_junc13__vj3
    VV_junc13__Qin4 = VV_junc13__w_in4*VV_junc13__vj4
    VV_junc13__Qout1 = VV_junc13__w_out1*-VV_junc13__vj1
    VV_junc13__Qout3 = VV_junc13__w_out3*-VV_junc13__vj3
    VV_junc13__Qout4 = VV_junc13__w_out4*-VV_junc13__vj4
    VV_junc13__Qin_tot = VV_junc13__Qin1+VV_junc13__Qin2+VV_junc13__Qin3+VV_junc13__Qin4
    VV_junc13__Qout_tot = VV_junc13__Qout1+VV_junc13__Qout2+VV_junc13__Qout3+VV_junc13__Qout4
    VV_junc13__v = (VV_junc13__u-VV_junc13__u_d)/VV_junc13__R_VV_junc
    VV_junc13__bc1_is_in = (1 if VV_junc13__Qin1 > VV_junc13__v_threshold else 0)
    VV_junc13__bc3_is_in = (1 if VV_junc13__Qin3 > VV_junc13__v_threshold else 0)
    VV_junc13__bc4_is_in = (1 if VV_junc13__Qin4 > VV_junc13__v_threshold else 0)
    VV_junc13__bc1_is_out = (1 if VV_junc13__Qout1 > VV_junc13__v_threshold else 0)
    VV_junc13__bc3_is_out = (1 if VV_junc13__Qout3 > VV_junc13__v_threshold else 0)
    VV_junc13__bc4_is_out = (1 if VV_junc13__Qout4 > VV_junc13__v_threshold else 0)
    PV25__w_v = 0.5+1/np.pi*np.arctan(PV25__v/PV25__v_scale)
    PV25__w_v_d = 0.5+1/np.pi*np.arctan(PV25__v_d/PV25__v_scale)
    PV25__H_up = PV25__w_v_d*PV25__H_L_in+(1-PV25__w_v_d)*PV25__H_R_in
    PV25__s_v_d = np.abs(PV25__v_d)/(np.abs(PV25__v_d)+PV25__v_eps)
    PV25__H_L_out = (1-PV25__w_v_d)*PV25__H_down+PV25__w_v_d*PV25__H_L_in
    PV25__H_R_out = PV25__w_v_d*PV25__H_down+(1-PV25__w_v_d)*PV25__H_R_in
    PV25__v_pos = PV25__w_v*PV25__v
    PV25__v_neg = (1-PV25__w_v)*-PV25__v
    PV25__v_d_pos = PV25__w_v_d*PV25__v_d
    PV25__v_d_neg = (1-PV25__w_v_d)*-PV25__v_d
    PV25__H_volume_L = PV25__w_v*PV25__H_L_in+(1-PV25__w_v)*PV25__H_L_out
    PV25__H_volume_R = PV25__w_v_d*PV25__H_R_out+(1-PV25__w_v_d)*PV25__H_R_in
    PV25__v_mm3_s = PV25__v/PV25__one_mm3
    PV25__v_d_mm3_s = PV25__v_d/PV25__one_mm3
    PV26__w_v = 0.5+1/np.pi*np.arctan(PV26__v/PV26__v_scale)
    PV26__w_v_d = 0.5+1/np.pi*np.arctan(PV26__v_d/PV26__v_scale)
    PV26__H_up = PV26__w_v_d*PV26__H_L_in+(1-PV26__w_v_d)*PV26__H_R_in
    PV26__s_v_d = np.abs(PV26__v_d)/(np.abs(PV26__v_d)+PV26__v_eps)
    PV26__H_L_out = (1-PV26__w_v_d)*PV26__H_down+PV26__w_v_d*PV26__H_L_in
    PV26__H_R_out = PV26__w_v_d*PV26__H_down+(1-PV26__w_v_d)*PV26__H_R_in
    PV26__v_pos = PV26__w_v*PV26__v
    PV26__v_neg = (1-PV26__w_v)*-PV26__v
    PV26__v_d_pos = PV26__w_v_d*PV26__v_d
    PV26__v_d_neg = (1-PV26__w_v_d)*-PV26__v_d
    PV26__H_volume_L = PV26__w_v*PV26__H_L_in+(1-PV26__w_v)*PV26__H_L_out
    PV26__H_volume_R = PV26__w_v_d*PV26__H_R_out+(1-PV26__w_v_d)*PV26__H_R_in
    PV26__v_mm3_s = PV26__v/PV26__one_mm3
    PV26__v_d_mm3_s = PV26__v_d/PV26__one_mm3
    V25__w_v = 0.5+1/np.pi*np.arctan(V25__v/V25__v_scale)
    V25__H_up = V25__w_v*V25__H_L_in+(1-V25__w_v)*V25__H_R_in
    V25__s_v = np.abs(V25__v)/(np.abs(V25__v)+V25__v_eps)
    V25__H_L_out = (1-V25__w_v)*V25__H_down+V25__w_v*V25__H_L_in
    V25__H_R_out = V25__w_v*V25__H_down+(1-V25__w_v)*V25__H_R_in
    V25__v_pos = V25__w_v*V25__v
    V25__v_neg = (1-V25__w_v)*-V25__v
    V25__H_volume_L = V25__w_v*V25__H_L_in+(1-V25__w_v)*V25__H_L_out
    V25__H_volume_R = V25__w_v*V25__H_R_out+(1-V25__w_v)*V25__H_R_in
    V25__v_mm3_s = V25__v/V25__one_mm3
    V26__w_v = 0.5+1/np.pi*np.arctan(V26__v/V26__v_scale)
    V26__H_up = V26__w_v*V26__H_L_in+(1-V26__w_v)*V26__H_R_in
    V26__s_v = np.abs(V26__v)/(np.abs(V26__v)+V26__v_eps)
    V26__H_L_out = (1-V26__w_v)*V26__H_down+V26__w_v*V26__H_L_in
    V26__H_R_out = V26__w_v*V26__H_down+(1-V26__w_v)*V26__H_R_in
    V26__v_pos = V26__w_v*V26__v
    V26__v_neg = (1-V26__w_v)*-V26__v
    V26__H_volume_L = V26__w_v*V26__H_L_in+(1-V26__w_v)*V26__H_L_out
    V26__H_volume_R = V26__w_v*V26__H_R_out+(1-V26__w_v)*V26__H_R_in
    V26__v_mm3_s = V26__v/V26__one_mm3
    VV_junc14__vj1 = V13__v
    VV_junc14__vj3 = -PV27__v
    VV_junc14__vj4 = -PV28__v
    VV_junc14__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc14__vj1/VV_junc14__v_scale)
    VV_junc14__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc14__vj3/VV_junc14__v_scale)
    VV_junc14__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc14__vj4/VV_junc14__v_scale)
    VV_junc14__w_out1 = 1-VV_junc14__w_in1
    VV_junc14__w_out3 = 1-VV_junc14__w_in3
    VV_junc14__w_out4 = 1-VV_junc14__w_in4
    VV_junc14__Qin1 = VV_junc14__w_in1*VV_junc14__vj1
    VV_junc14__Qin3 = VV_junc14__w_in3*VV_junc14__vj3
    VV_junc14__Qin4 = VV_junc14__w_in4*VV_junc14__vj4
    VV_junc14__Qout1 = VV_junc14__w_out1*-VV_junc14__vj1
    VV_junc14__Qout3 = VV_junc14__w_out3*-VV_junc14__vj3
    VV_junc14__Qout4 = VV_junc14__w_out4*-VV_junc14__vj4
    VV_junc14__Qin_tot = VV_junc14__Qin1+VV_junc14__Qin2+VV_junc14__Qin3+VV_junc14__Qin4
    VV_junc14__Qout_tot = VV_junc14__Qout1+VV_junc14__Qout2+VV_junc14__Qout3+VV_junc14__Qout4
    VV_junc14__v = (VV_junc14__u-VV_junc14__u_d)/VV_junc14__R_VV_junc
    VV_junc14__bc1_is_in = (1 if VV_junc14__Qin1 > VV_junc14__v_threshold else 0)
    VV_junc14__bc3_is_in = (1 if VV_junc14__Qin3 > VV_junc14__v_threshold else 0)
    VV_junc14__bc4_is_in = (1 if VV_junc14__Qin4 > VV_junc14__v_threshold else 0)
    VV_junc14__bc1_is_out = (1 if VV_junc14__Qout1 > VV_junc14__v_threshold else 0)
    VV_junc14__bc3_is_out = (1 if VV_junc14__Qout3 > VV_junc14__v_threshold else 0)
    VV_junc14__bc4_is_out = (1 if VV_junc14__Qout4 > VV_junc14__v_threshold else 0)
    PV27__w_v = 0.5+1/np.pi*np.arctan(PV27__v/PV27__v_scale)
    PV27__w_v_d = 0.5+1/np.pi*np.arctan(PV27__v_d/PV27__v_scale)
    PV27__H_up = PV27__w_v_d*PV27__H_L_in+(1-PV27__w_v_d)*PV27__H_R_in
    PV27__s_v_d = np.abs(PV27__v_d)/(np.abs(PV27__v_d)+PV27__v_eps)
    PV27__H_L_out = (1-PV27__w_v_d)*PV27__H_down+PV27__w_v_d*PV27__H_L_in
    PV27__H_R_out = PV27__w_v_d*PV27__H_down+(1-PV27__w_v_d)*PV27__H_R_in
    PV27__v_pos = PV27__w_v*PV27__v
    PV27__v_neg = (1-PV27__w_v)*-PV27__v
    PV27__v_d_pos = PV27__w_v_d*PV27__v_d
    PV27__v_d_neg = (1-PV27__w_v_d)*-PV27__v_d
    PV27__H_volume_L = PV27__w_v*PV27__H_L_in+(1-PV27__w_v)*PV27__H_L_out
    PV27__H_volume_R = PV27__w_v_d*PV27__H_R_out+(1-PV27__w_v_d)*PV27__H_R_in
    PV27__v_mm3_s = PV27__v/PV27__one_mm3
    PV27__v_d_mm3_s = PV27__v_d/PV27__one_mm3
    PV28__w_v = 0.5+1/np.pi*np.arctan(PV28__v/PV28__v_scale)
    PV28__w_v_d = 0.5+1/np.pi*np.arctan(PV28__v_d/PV28__v_scale)
    PV28__H_up = PV28__w_v_d*PV28__H_L_in+(1-PV28__w_v_d)*PV28__H_R_in
    PV28__s_v_d = np.abs(PV28__v_d)/(np.abs(PV28__v_d)+PV28__v_eps)
    PV28__H_L_out = (1-PV28__w_v_d)*PV28__H_down+PV28__w_v_d*PV28__H_L_in
    PV28__H_R_out = PV28__w_v_d*PV28__H_down+(1-PV28__w_v_d)*PV28__H_R_in
    PV28__v_pos = PV28__w_v*PV28__v
    PV28__v_neg = (1-PV28__w_v)*-PV28__v
    PV28__v_d_pos = PV28__w_v_d*PV28__v_d
    PV28__v_d_neg = (1-PV28__w_v_d)*-PV28__v_d
    PV28__H_volume_L = PV28__w_v*PV28__H_L_in+(1-PV28__w_v)*PV28__H_L_out
    PV28__H_volume_R = PV28__w_v_d*PV28__H_R_out+(1-PV28__w_v_d)*PV28__H_R_in
    PV28__v_mm3_s = PV28__v/PV28__one_mm3
    PV28__v_d_mm3_s = PV28__v_d/PV28__one_mm3
    V27__w_v = 0.5+1/np.pi*np.arctan(V27__v/V27__v_scale)
    V27__H_up = V27__w_v*V27__H_L_in+(1-V27__w_v)*V27__H_R_in
    V27__s_v = np.abs(V27__v)/(np.abs(V27__v)+V27__v_eps)
    V27__H_L_out = (1-V27__w_v)*V27__H_down+V27__w_v*V27__H_L_in
    V27__H_R_out = V27__w_v*V27__H_down+(1-V27__w_v)*V27__H_R_in
    V27__v_pos = V27__w_v*V27__v
    V27__v_neg = (1-V27__w_v)*-V27__v
    V27__H_volume_L = V27__w_v*V27__H_L_in+(1-V27__w_v)*V27__H_L_out
    V27__H_volume_R = V27__w_v*V27__H_R_out+(1-V27__w_v)*V27__H_R_in
    V27__v_mm3_s = V27__v/V27__one_mm3
    V28__w_v = 0.5+1/np.pi*np.arctan(V28__v/V28__v_scale)
    V28__H_up = V28__w_v*V28__H_L_in+(1-V28__w_v)*V28__H_R_in
    V28__s_v = np.abs(V28__v)/(np.abs(V28__v)+V28__v_eps)
    V28__H_L_out = (1-V28__w_v)*V28__H_down+V28__w_v*V28__H_L_in
    V28__H_R_out = V28__w_v*V28__H_down+(1-V28__w_v)*V28__H_R_in
    V28__v_pos = V28__w_v*V28__v
    V28__v_neg = (1-V28__w_v)*-V28__v
    V28__H_volume_L = V28__w_v*V28__H_L_in+(1-V28__w_v)*V28__H_L_out
    V28__H_volume_R = V28__w_v*V28__H_R_out+(1-V28__w_v)*V28__H_R_in
    V28__v_mm3_s = V28__v/V28__one_mm3
    VV_junc15__vj1 = V14__v
    VV_junc15__vj3 = -PV29__v
    VV_junc15__vj4 = -PV30__v
    VV_junc15__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc15__vj1/VV_junc15__v_scale)
    VV_junc15__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc15__vj3/VV_junc15__v_scale)
    VV_junc15__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc15__vj4/VV_junc15__v_scale)
    VV_junc15__w_out1 = 1-VV_junc15__w_in1
    VV_junc15__w_out3 = 1-VV_junc15__w_in3
    VV_junc15__w_out4 = 1-VV_junc15__w_in4
    VV_junc15__Qin1 = VV_junc15__w_in1*VV_junc15__vj1
    VV_junc15__Qin3 = VV_junc15__w_in3*VV_junc15__vj3
    VV_junc15__Qin4 = VV_junc15__w_in4*VV_junc15__vj4
    VV_junc15__Qout1 = VV_junc15__w_out1*-VV_junc15__vj1
    VV_junc15__Qout3 = VV_junc15__w_out3*-VV_junc15__vj3
    VV_junc15__Qout4 = VV_junc15__w_out4*-VV_junc15__vj4
    VV_junc15__Qin_tot = VV_junc15__Qin1+VV_junc15__Qin2+VV_junc15__Qin3+VV_junc15__Qin4
    VV_junc15__Qout_tot = VV_junc15__Qout1+VV_junc15__Qout2+VV_junc15__Qout3+VV_junc15__Qout4
    VV_junc15__v = (VV_junc15__u-VV_junc15__u_d)/VV_junc15__R_VV_junc
    VV_junc15__bc1_is_in = (1 if VV_junc15__Qin1 > VV_junc15__v_threshold else 0)
    VV_junc15__bc3_is_in = (1 if VV_junc15__Qin3 > VV_junc15__v_threshold else 0)
    VV_junc15__bc4_is_in = (1 if VV_junc15__Qin4 > VV_junc15__v_threshold else 0)
    VV_junc15__bc1_is_out = (1 if VV_junc15__Qout1 > VV_junc15__v_threshold else 0)
    VV_junc15__bc3_is_out = (1 if VV_junc15__Qout3 > VV_junc15__v_threshold else 0)
    VV_junc15__bc4_is_out = (1 if VV_junc15__Qout4 > VV_junc15__v_threshold else 0)
    PV29__w_v = 0.5+1/np.pi*np.arctan(PV29__v/PV29__v_scale)
    PV29__w_v_d = 0.5+1/np.pi*np.arctan(PV29__v_d/PV29__v_scale)
    PV29__H_up = PV29__w_v_d*PV29__H_L_in+(1-PV29__w_v_d)*PV29__H_R_in
    PV29__s_v_d = np.abs(PV29__v_d)/(np.abs(PV29__v_d)+PV29__v_eps)
    PV29__H_L_out = (1-PV29__w_v_d)*PV29__H_down+PV29__w_v_d*PV29__H_L_in
    PV29__H_R_out = PV29__w_v_d*PV29__H_down+(1-PV29__w_v_d)*PV29__H_R_in
    PV29__v_pos = PV29__w_v*PV29__v
    PV29__v_neg = (1-PV29__w_v)*-PV29__v
    PV29__v_d_pos = PV29__w_v_d*PV29__v_d
    PV29__v_d_neg = (1-PV29__w_v_d)*-PV29__v_d
    PV29__H_volume_L = PV29__w_v*PV29__H_L_in+(1-PV29__w_v)*PV29__H_L_out
    PV29__H_volume_R = PV29__w_v_d*PV29__H_R_out+(1-PV29__w_v_d)*PV29__H_R_in
    PV29__v_mm3_s = PV29__v/PV29__one_mm3
    PV29__v_d_mm3_s = PV29__v_d/PV29__one_mm3
    PV30__w_v = 0.5+1/np.pi*np.arctan(PV30__v/PV30__v_scale)
    PV30__w_v_d = 0.5+1/np.pi*np.arctan(PV30__v_d/PV30__v_scale)
    PV30__H_up = PV30__w_v_d*PV30__H_L_in+(1-PV30__w_v_d)*PV30__H_R_in
    PV30__s_v_d = np.abs(PV30__v_d)/(np.abs(PV30__v_d)+PV30__v_eps)
    PV30__H_L_out = (1-PV30__w_v_d)*PV30__H_down+PV30__w_v_d*PV30__H_L_in
    PV30__H_R_out = PV30__w_v_d*PV30__H_down+(1-PV30__w_v_d)*PV30__H_R_in
    PV30__v_pos = PV30__w_v*PV30__v
    PV30__v_neg = (1-PV30__w_v)*-PV30__v
    PV30__v_d_pos = PV30__w_v_d*PV30__v_d
    PV30__v_d_neg = (1-PV30__w_v_d)*-PV30__v_d
    PV30__H_volume_L = PV30__w_v*PV30__H_L_in+(1-PV30__w_v)*PV30__H_L_out
    PV30__H_volume_R = PV30__w_v_d*PV30__H_R_out+(1-PV30__w_v_d)*PV30__H_R_in
    PV30__v_mm3_s = PV30__v/PV30__one_mm3
    PV30__v_d_mm3_s = PV30__v_d/PV30__one_mm3
    V29__w_v = 0.5+1/np.pi*np.arctan(V29__v/V29__v_scale)
    V29__H_up = V29__w_v*V29__H_L_in+(1-V29__w_v)*V29__H_R_in
    V29__s_v = np.abs(V29__v)/(np.abs(V29__v)+V29__v_eps)
    V29__H_L_out = (1-V29__w_v)*V29__H_down+V29__w_v*V29__H_L_in
    V29__H_R_out = V29__w_v*V29__H_down+(1-V29__w_v)*V29__H_R_in
    V29__v_pos = V29__w_v*V29__v
    V29__v_neg = (1-V29__w_v)*-V29__v
    V29__H_volume_L = V29__w_v*V29__H_L_in+(1-V29__w_v)*V29__H_L_out
    V29__H_volume_R = V29__w_v*V29__H_R_out+(1-V29__w_v)*V29__H_R_in
    V29__v_mm3_s = V29__v/V29__one_mm3
    V30__w_v = 0.5+1/np.pi*np.arctan(V30__v/V30__v_scale)
    V30__H_up = V30__w_v*V30__H_L_in+(1-V30__w_v)*V30__H_R_in
    V30__s_v = np.abs(V30__v)/(np.abs(V30__v)+V30__v_eps)
    V30__H_L_out = (1-V30__w_v)*V30__H_down+V30__w_v*V30__H_L_in
    V30__H_R_out = V30__w_v*V30__H_down+(1-V30__w_v)*V30__H_R_in
    V30__v_pos = V30__w_v*V30__v
    V30__v_neg = (1-V30__w_v)*-V30__v
    V30__H_volume_L = V30__w_v*V30__H_L_in+(1-V30__w_v)*V30__H_L_out
    V30__H_volume_R = V30__w_v*V30__H_R_out+(1-V30__w_v)*V30__H_R_in
    V30__v_mm3_s = V30__v/V30__one_mm3
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
    VV_junc8__n_in = VV_junc8__bc1_is_in+VV_junc8__bc2_is_in+VV_junc8__bc3_is_in+VV_junc8__bc4_is_in
    VV_junc8__n_out = VV_junc8__bc1_is_out+VV_junc8__bc2_is_out+VV_junc8__bc3_is_out+VV_junc8__bc4_is_out
    VV_junc8__RBC_in = VV_junc8__Qin1*V7__H_R_out+VV_junc8__Qin2*VV_junc8__H_to2+VV_junc8__Qin3*PV15__H_L_out+VV_junc8__Qin4*PV16__H_L_out
    VV_junc8__v_mm3_s = VV_junc8__v/VV_junc8__one_mm3
    VV_junc8__junction_type = (1 if VV_junc8__n_in == 1 else (-1 if VV_junc8__n_in >= 2 else 0))
    VV_junc8__is_split = (1 if VV_junc8__junction_type == 1 else 0)
    VV_junc8__is_merge = (1 if VV_junc8__junction_type == -1 else 0)
    VV_junc8__feed1 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin1 >= VV_junc8__Qin2) and (VV_junc8__Qin1 >= VV_junc8__Qin3) and (VV_junc8__Qin1 >= VV_junc8__Qin4) else 0)
    VV_junc8__feed2 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin2 > VV_junc8__Qin1) and (VV_junc8__Qin2 >= VV_junc8__Qin3) and (VV_junc8__Qin2 >= VV_junc8__Qin4) else 0)
    VV_junc8__feed3 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin3 > VV_junc8__Qin1) and (VV_junc8__Qin3 > VV_junc8__Qin2) and (VV_junc8__Qin3 >= VV_junc8__Qin4) else 0)
    VV_junc8__feed4 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__Qin4 > VV_junc8__Qin1) and (VV_junc8__Qin4 > VV_junc8__Qin2) and (VV_junc8__Qin4 > VV_junc8__Qin3) else 0)
    VV_junc8__alpha1 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc1_is_out == 1) and (VV_junc8__Qout1 >= VV_junc8__Qout2) and (VV_junc8__Qout1 >= VV_junc8__Qout3) and (VV_junc8__Qout1 >= VV_junc8__Qout4) else 0)
    VV_junc8__alpha2 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc2_is_out == 1) and (VV_junc8__Qout2 > VV_junc8__Qout1) and (VV_junc8__Qout2 >= VV_junc8__Qout3) and (VV_junc8__Qout2 >= VV_junc8__Qout4) else 0)
    VV_junc8__alpha3 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc3_is_out == 1) and (VV_junc8__Qout3 > VV_junc8__Qout1) and (VV_junc8__Qout3 > VV_junc8__Qout2) and (VV_junc8__Qout3 >= VV_junc8__Qout4) else 0)
    VV_junc8__alpha4 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc4_is_out == 1) and (VV_junc8__Qout4 > VV_junc8__Qout1) and (VV_junc8__Qout4 > VV_junc8__Qout2) and (VV_junc8__Qout4 > VV_junc8__Qout3) else 0)
    VV_junc8__Qout1_rem = (0 if VV_junc8__alpha1 == 1 else VV_junc8__Qout1)
    VV_junc8__Qout2_rem = (0 if VV_junc8__alpha2 == 1 else VV_junc8__Qout2)
    VV_junc8__Qout3_rem = (0 if VV_junc8__alpha3 == 1 else VV_junc8__Qout3)
    VV_junc8__Qout4_rem = (0 if VV_junc8__alpha4 == 1 else VV_junc8__Qout4)
    VV_junc8__beta1 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc1_is_out == 1) and (VV_junc8__alpha1 == 0) and (VV_junc8__Qout1_rem >= VV_junc8__Qout2_rem) and (VV_junc8__Qout1_rem >= VV_junc8__Qout3_rem) and (VV_junc8__Qout1_rem >= VV_junc8__Qout4_rem) else 0)
    VV_junc8__beta2 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc2_is_out == 1) and (VV_junc8__alpha2 == 0) and (VV_junc8__Qout2_rem > VV_junc8__Qout1_rem) and (VV_junc8__Qout2_rem >= VV_junc8__Qout3_rem) and (VV_junc8__Qout2_rem >= VV_junc8__Qout4_rem) else 0)
    VV_junc8__beta3 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc3_is_out == 1) and (VV_junc8__alpha3 == 0) and (VV_junc8__Qout3_rem > VV_junc8__Qout1_rem) and (VV_junc8__Qout3_rem > VV_junc8__Qout2_rem) and (VV_junc8__Qout3_rem >= VV_junc8__Qout4_rem) else 0)
    VV_junc8__beta4 = (1 if (VV_junc8__is_split == 1) and (VV_junc8__bc4_is_out == 1) and (VV_junc8__alpha4 == 0) and (VV_junc8__Qout4_rem > VV_junc8__Qout1_rem) and (VV_junc8__Qout4_rem > VV_junc8__Qout2_rem) and (VV_junc8__Qout4_rem > VV_junc8__Qout3_rem) else 0)
    VV_junc8__D_F = (VV_junc8__D1 if VV_junc8__feed1 == 1 else (VV_junc8__D2 if VV_junc8__feed2 == 1 else (VV_junc8__D3 if VV_junc8__feed3 == 1 else (VV_junc8__D4 if VV_junc8__feed4 == 1 else VV_junc8__D1))))
    VV_junc8__D_alpha = (VV_junc8__D1 if VV_junc8__alpha1 == 1 else (VV_junc8__D2 if VV_junc8__alpha2 == 1 else (VV_junc8__D3 if VV_junc8__alpha3 == 1 else (VV_junc8__D4 if VV_junc8__alpha4 == 1 else VV_junc8__D3))))
    VV_junc8__D_beta = (VV_junc8__D1 if VV_junc8__beta1 == 1 else (VV_junc8__D2 if VV_junc8__beta2 == 1 else (VV_junc8__D3 if VV_junc8__beta3 == 1 else (VV_junc8__D4 if VV_junc8__beta4 == 1 else VV_junc8__D4))))
    VV_junc8__v_alpha = (VV_junc8__Qout1 if VV_junc8__alpha1 == 1 else (VV_junc8__Qout2 if VV_junc8__alpha2 == 1 else (VV_junc8__Qout3 if VV_junc8__alpha3 == 1 else (VV_junc8__Qout4 if VV_junc8__alpha4 == 1 else 0))))
    VV_junc8__v_beta = (VV_junc8__Qout1 if VV_junc8__beta1 == 1 else (VV_junc8__Qout2 if VV_junc8__beta2 == 1 else (VV_junc8__Qout3 if VV_junc8__beta3 == 1 else (VV_junc8__Qout4 if VV_junc8__beta4 == 1 else 0))))
    PV15__H_down_target = PV15__s_v_d*(PV15__H_mean+PV15__gamma_mirror*(PV15__H_mean-PV15__H_up))+(1-PV15__s_v_d)*PV15__H_mean
    PV16__H_down_target = PV16__s_v_d*(PV16__H_mean+PV16__gamma_mirror*(PV16__H_mean-PV16__H_up))+(1-PV16__s_v_d)*PV16__H_mean
    V15__H_down_target = V15__s_v*(V15__H_mean+V15__gamma_mirror*(V15__H_mean-V15__H_up))+(1-V15__s_v)*V15__H_mean
    V16__H_down_target = V16__s_v*(V16__H_mean+V16__gamma_mirror*(V16__H_mean-V16__H_up))+(1-V16__s_v)*V16__H_mean
    VV_junc9__n_in = VV_junc9__bc1_is_in+VV_junc9__bc2_is_in+VV_junc9__bc3_is_in+VV_junc9__bc4_is_in
    VV_junc9__n_out = VV_junc9__bc1_is_out+VV_junc9__bc2_is_out+VV_junc9__bc3_is_out+VV_junc9__bc4_is_out
    VV_junc9__RBC_in = VV_junc9__Qin1*V8__H_R_out+VV_junc9__Qin2*VV_junc9__H_to2+VV_junc9__Qin3*PV17__H_L_out+VV_junc9__Qin4*PV18__H_L_out
    VV_junc9__v_mm3_s = VV_junc9__v/VV_junc9__one_mm3
    VV_junc9__junction_type = (1 if VV_junc9__n_in == 1 else (-1 if VV_junc9__n_in >= 2 else 0))
    VV_junc9__is_split = (1 if VV_junc9__junction_type == 1 else 0)
    VV_junc9__is_merge = (1 if VV_junc9__junction_type == -1 else 0)
    VV_junc9__feed1 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin1 >= VV_junc9__Qin2) and (VV_junc9__Qin1 >= VV_junc9__Qin3) and (VV_junc9__Qin1 >= VV_junc9__Qin4) else 0)
    VV_junc9__feed2 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin2 > VV_junc9__Qin1) and (VV_junc9__Qin2 >= VV_junc9__Qin3) and (VV_junc9__Qin2 >= VV_junc9__Qin4) else 0)
    VV_junc9__feed3 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin3 > VV_junc9__Qin1) and (VV_junc9__Qin3 > VV_junc9__Qin2) and (VV_junc9__Qin3 >= VV_junc9__Qin4) else 0)
    VV_junc9__feed4 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__Qin4 > VV_junc9__Qin1) and (VV_junc9__Qin4 > VV_junc9__Qin2) and (VV_junc9__Qin4 > VV_junc9__Qin3) else 0)
    VV_junc9__alpha1 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc1_is_out == 1) and (VV_junc9__Qout1 >= VV_junc9__Qout2) and (VV_junc9__Qout1 >= VV_junc9__Qout3) and (VV_junc9__Qout1 >= VV_junc9__Qout4) else 0)
    VV_junc9__alpha2 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc2_is_out == 1) and (VV_junc9__Qout2 > VV_junc9__Qout1) and (VV_junc9__Qout2 >= VV_junc9__Qout3) and (VV_junc9__Qout2 >= VV_junc9__Qout4) else 0)
    VV_junc9__alpha3 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc3_is_out == 1) and (VV_junc9__Qout3 > VV_junc9__Qout1) and (VV_junc9__Qout3 > VV_junc9__Qout2) and (VV_junc9__Qout3 >= VV_junc9__Qout4) else 0)
    VV_junc9__alpha4 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc4_is_out == 1) and (VV_junc9__Qout4 > VV_junc9__Qout1) and (VV_junc9__Qout4 > VV_junc9__Qout2) and (VV_junc9__Qout4 > VV_junc9__Qout3) else 0)
    VV_junc9__Qout1_rem = (0 if VV_junc9__alpha1 == 1 else VV_junc9__Qout1)
    VV_junc9__Qout2_rem = (0 if VV_junc9__alpha2 == 1 else VV_junc9__Qout2)
    VV_junc9__Qout3_rem = (0 if VV_junc9__alpha3 == 1 else VV_junc9__Qout3)
    VV_junc9__Qout4_rem = (0 if VV_junc9__alpha4 == 1 else VV_junc9__Qout4)
    VV_junc9__beta1 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc1_is_out == 1) and (VV_junc9__alpha1 == 0) and (VV_junc9__Qout1_rem >= VV_junc9__Qout2_rem) and (VV_junc9__Qout1_rem >= VV_junc9__Qout3_rem) and (VV_junc9__Qout1_rem >= VV_junc9__Qout4_rem) else 0)
    VV_junc9__beta2 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc2_is_out == 1) and (VV_junc9__alpha2 == 0) and (VV_junc9__Qout2_rem > VV_junc9__Qout1_rem) and (VV_junc9__Qout2_rem >= VV_junc9__Qout3_rem) and (VV_junc9__Qout2_rem >= VV_junc9__Qout4_rem) else 0)
    VV_junc9__beta3 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc3_is_out == 1) and (VV_junc9__alpha3 == 0) and (VV_junc9__Qout3_rem > VV_junc9__Qout1_rem) and (VV_junc9__Qout3_rem > VV_junc9__Qout2_rem) and (VV_junc9__Qout3_rem >= VV_junc9__Qout4_rem) else 0)
    VV_junc9__beta4 = (1 if (VV_junc9__is_split == 1) and (VV_junc9__bc4_is_out == 1) and (VV_junc9__alpha4 == 0) and (VV_junc9__Qout4_rem > VV_junc9__Qout1_rem) and (VV_junc9__Qout4_rem > VV_junc9__Qout2_rem) and (VV_junc9__Qout4_rem > VV_junc9__Qout3_rem) else 0)
    VV_junc9__D_F = (VV_junc9__D1 if VV_junc9__feed1 == 1 else (VV_junc9__D2 if VV_junc9__feed2 == 1 else (VV_junc9__D3 if VV_junc9__feed3 == 1 else (VV_junc9__D4 if VV_junc9__feed4 == 1 else VV_junc9__D1))))
    VV_junc9__D_alpha = (VV_junc9__D1 if VV_junc9__alpha1 == 1 else (VV_junc9__D2 if VV_junc9__alpha2 == 1 else (VV_junc9__D3 if VV_junc9__alpha3 == 1 else (VV_junc9__D4 if VV_junc9__alpha4 == 1 else VV_junc9__D3))))
    VV_junc9__D_beta = (VV_junc9__D1 if VV_junc9__beta1 == 1 else (VV_junc9__D2 if VV_junc9__beta2 == 1 else (VV_junc9__D3 if VV_junc9__beta3 == 1 else (VV_junc9__D4 if VV_junc9__beta4 == 1 else VV_junc9__D4))))
    VV_junc9__v_alpha = (VV_junc9__Qout1 if VV_junc9__alpha1 == 1 else (VV_junc9__Qout2 if VV_junc9__alpha2 == 1 else (VV_junc9__Qout3 if VV_junc9__alpha3 == 1 else (VV_junc9__Qout4 if VV_junc9__alpha4 == 1 else 0))))
    VV_junc9__v_beta = (VV_junc9__Qout1 if VV_junc9__beta1 == 1 else (VV_junc9__Qout2 if VV_junc9__beta2 == 1 else (VV_junc9__Qout3 if VV_junc9__beta3 == 1 else (VV_junc9__Qout4 if VV_junc9__beta4 == 1 else 0))))
    PV17__H_down_target = PV17__s_v_d*(PV17__H_mean+PV17__gamma_mirror*(PV17__H_mean-PV17__H_up))+(1-PV17__s_v_d)*PV17__H_mean
    PV18__H_down_target = PV18__s_v_d*(PV18__H_mean+PV18__gamma_mirror*(PV18__H_mean-PV18__H_up))+(1-PV18__s_v_d)*PV18__H_mean
    V17__H_down_target = V17__s_v*(V17__H_mean+V17__gamma_mirror*(V17__H_mean-V17__H_up))+(1-V17__s_v)*V17__H_mean
    V18__H_down_target = V18__s_v*(V18__H_mean+V18__gamma_mirror*(V18__H_mean-V18__H_up))+(1-V18__s_v)*V18__H_mean
    VV_junc10__n_in = VV_junc10__bc1_is_in+VV_junc10__bc2_is_in+VV_junc10__bc3_is_in+VV_junc10__bc4_is_in
    VV_junc10__n_out = VV_junc10__bc1_is_out+VV_junc10__bc2_is_out+VV_junc10__bc3_is_out+VV_junc10__bc4_is_out
    VV_junc10__RBC_in = VV_junc10__Qin1*V9__H_R_out+VV_junc10__Qin2*VV_junc10__H_to2+VV_junc10__Qin3*PV19__H_L_out+VV_junc10__Qin4*PV20__H_L_out
    VV_junc10__v_mm3_s = VV_junc10__v/VV_junc10__one_mm3
    VV_junc10__junction_type = (1 if VV_junc10__n_in == 1 else (-1 if VV_junc10__n_in >= 2 else 0))
    VV_junc10__is_split = (1 if VV_junc10__junction_type == 1 else 0)
    VV_junc10__is_merge = (1 if VV_junc10__junction_type == -1 else 0)
    VV_junc10__feed1 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin1 >= VV_junc10__Qin2) and (VV_junc10__Qin1 >= VV_junc10__Qin3) and (VV_junc10__Qin1 >= VV_junc10__Qin4) else 0)
    VV_junc10__feed2 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin2 > VV_junc10__Qin1) and (VV_junc10__Qin2 >= VV_junc10__Qin3) and (VV_junc10__Qin2 >= VV_junc10__Qin4) else 0)
    VV_junc10__feed3 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin3 > VV_junc10__Qin1) and (VV_junc10__Qin3 > VV_junc10__Qin2) and (VV_junc10__Qin3 >= VV_junc10__Qin4) else 0)
    VV_junc10__feed4 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__Qin4 > VV_junc10__Qin1) and (VV_junc10__Qin4 > VV_junc10__Qin2) and (VV_junc10__Qin4 > VV_junc10__Qin3) else 0)
    VV_junc10__alpha1 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc1_is_out == 1) and (VV_junc10__Qout1 >= VV_junc10__Qout2) and (VV_junc10__Qout1 >= VV_junc10__Qout3) and (VV_junc10__Qout1 >= VV_junc10__Qout4) else 0)
    VV_junc10__alpha2 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc2_is_out == 1) and (VV_junc10__Qout2 > VV_junc10__Qout1) and (VV_junc10__Qout2 >= VV_junc10__Qout3) and (VV_junc10__Qout2 >= VV_junc10__Qout4) else 0)
    VV_junc10__alpha3 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc3_is_out == 1) and (VV_junc10__Qout3 > VV_junc10__Qout1) and (VV_junc10__Qout3 > VV_junc10__Qout2) and (VV_junc10__Qout3 >= VV_junc10__Qout4) else 0)
    VV_junc10__alpha4 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc4_is_out == 1) and (VV_junc10__Qout4 > VV_junc10__Qout1) and (VV_junc10__Qout4 > VV_junc10__Qout2) and (VV_junc10__Qout4 > VV_junc10__Qout3) else 0)
    VV_junc10__Qout1_rem = (0 if VV_junc10__alpha1 == 1 else VV_junc10__Qout1)
    VV_junc10__Qout2_rem = (0 if VV_junc10__alpha2 == 1 else VV_junc10__Qout2)
    VV_junc10__Qout3_rem = (0 if VV_junc10__alpha3 == 1 else VV_junc10__Qout3)
    VV_junc10__Qout4_rem = (0 if VV_junc10__alpha4 == 1 else VV_junc10__Qout4)
    VV_junc10__beta1 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc1_is_out == 1) and (VV_junc10__alpha1 == 0) and (VV_junc10__Qout1_rem >= VV_junc10__Qout2_rem) and (VV_junc10__Qout1_rem >= VV_junc10__Qout3_rem) and (VV_junc10__Qout1_rem >= VV_junc10__Qout4_rem) else 0)
    VV_junc10__beta2 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc2_is_out == 1) and (VV_junc10__alpha2 == 0) and (VV_junc10__Qout2_rem > VV_junc10__Qout1_rem) and (VV_junc10__Qout2_rem >= VV_junc10__Qout3_rem) and (VV_junc10__Qout2_rem >= VV_junc10__Qout4_rem) else 0)
    VV_junc10__beta3 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc3_is_out == 1) and (VV_junc10__alpha3 == 0) and (VV_junc10__Qout3_rem > VV_junc10__Qout1_rem) and (VV_junc10__Qout3_rem > VV_junc10__Qout2_rem) and (VV_junc10__Qout3_rem >= VV_junc10__Qout4_rem) else 0)
    VV_junc10__beta4 = (1 if (VV_junc10__is_split == 1) and (VV_junc10__bc4_is_out == 1) and (VV_junc10__alpha4 == 0) and (VV_junc10__Qout4_rem > VV_junc10__Qout1_rem) and (VV_junc10__Qout4_rem > VV_junc10__Qout2_rem) and (VV_junc10__Qout4_rem > VV_junc10__Qout3_rem) else 0)
    VV_junc10__D_F = (VV_junc10__D1 if VV_junc10__feed1 == 1 else (VV_junc10__D2 if VV_junc10__feed2 == 1 else (VV_junc10__D3 if VV_junc10__feed3 == 1 else (VV_junc10__D4 if VV_junc10__feed4 == 1 else VV_junc10__D1))))
    VV_junc10__D_alpha = (VV_junc10__D1 if VV_junc10__alpha1 == 1 else (VV_junc10__D2 if VV_junc10__alpha2 == 1 else (VV_junc10__D3 if VV_junc10__alpha3 == 1 else (VV_junc10__D4 if VV_junc10__alpha4 == 1 else VV_junc10__D3))))
    VV_junc10__D_beta = (VV_junc10__D1 if VV_junc10__beta1 == 1 else (VV_junc10__D2 if VV_junc10__beta2 == 1 else (VV_junc10__D3 if VV_junc10__beta3 == 1 else (VV_junc10__D4 if VV_junc10__beta4 == 1 else VV_junc10__D4))))
    VV_junc10__v_alpha = (VV_junc10__Qout1 if VV_junc10__alpha1 == 1 else (VV_junc10__Qout2 if VV_junc10__alpha2 == 1 else (VV_junc10__Qout3 if VV_junc10__alpha3 == 1 else (VV_junc10__Qout4 if VV_junc10__alpha4 == 1 else 0))))
    VV_junc10__v_beta = (VV_junc10__Qout1 if VV_junc10__beta1 == 1 else (VV_junc10__Qout2 if VV_junc10__beta2 == 1 else (VV_junc10__Qout3 if VV_junc10__beta3 == 1 else (VV_junc10__Qout4 if VV_junc10__beta4 == 1 else 0))))
    PV19__H_down_target = PV19__s_v_d*(PV19__H_mean+PV19__gamma_mirror*(PV19__H_mean-PV19__H_up))+(1-PV19__s_v_d)*PV19__H_mean
    PV20__H_down_target = PV20__s_v_d*(PV20__H_mean+PV20__gamma_mirror*(PV20__H_mean-PV20__H_up))+(1-PV20__s_v_d)*PV20__H_mean
    V19__H_down_target = V19__s_v*(V19__H_mean+V19__gamma_mirror*(V19__H_mean-V19__H_up))+(1-V19__s_v)*V19__H_mean
    V20__H_down_target = V20__s_v*(V20__H_mean+V20__gamma_mirror*(V20__H_mean-V20__H_up))+(1-V20__s_v)*V20__H_mean
    VV_junc11__n_in = VV_junc11__bc1_is_in+VV_junc11__bc2_is_in+VV_junc11__bc3_is_in+VV_junc11__bc4_is_in
    VV_junc11__n_out = VV_junc11__bc1_is_out+VV_junc11__bc2_is_out+VV_junc11__bc3_is_out+VV_junc11__bc4_is_out
    VV_junc11__RBC_in = VV_junc11__Qin1*V10__H_R_out+VV_junc11__Qin2*VV_junc11__H_to2+VV_junc11__Qin3*PV21__H_L_out+VV_junc11__Qin4*PV22__H_L_out
    VV_junc11__v_mm3_s = VV_junc11__v/VV_junc11__one_mm3
    VV_junc11__junction_type = (1 if VV_junc11__n_in == 1 else (-1 if VV_junc11__n_in >= 2 else 0))
    VV_junc11__is_split = (1 if VV_junc11__junction_type == 1 else 0)
    VV_junc11__is_merge = (1 if VV_junc11__junction_type == -1 else 0)
    VV_junc11__feed1 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin1 >= VV_junc11__Qin2) and (VV_junc11__Qin1 >= VV_junc11__Qin3) and (VV_junc11__Qin1 >= VV_junc11__Qin4) else 0)
    VV_junc11__feed2 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin2 > VV_junc11__Qin1) and (VV_junc11__Qin2 >= VV_junc11__Qin3) and (VV_junc11__Qin2 >= VV_junc11__Qin4) else 0)
    VV_junc11__feed3 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin3 > VV_junc11__Qin1) and (VV_junc11__Qin3 > VV_junc11__Qin2) and (VV_junc11__Qin3 >= VV_junc11__Qin4) else 0)
    VV_junc11__feed4 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__Qin4 > VV_junc11__Qin1) and (VV_junc11__Qin4 > VV_junc11__Qin2) and (VV_junc11__Qin4 > VV_junc11__Qin3) else 0)
    VV_junc11__alpha1 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc1_is_out == 1) and (VV_junc11__Qout1 >= VV_junc11__Qout2) and (VV_junc11__Qout1 >= VV_junc11__Qout3) and (VV_junc11__Qout1 >= VV_junc11__Qout4) else 0)
    VV_junc11__alpha2 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc2_is_out == 1) and (VV_junc11__Qout2 > VV_junc11__Qout1) and (VV_junc11__Qout2 >= VV_junc11__Qout3) and (VV_junc11__Qout2 >= VV_junc11__Qout4) else 0)
    VV_junc11__alpha3 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc3_is_out == 1) and (VV_junc11__Qout3 > VV_junc11__Qout1) and (VV_junc11__Qout3 > VV_junc11__Qout2) and (VV_junc11__Qout3 >= VV_junc11__Qout4) else 0)
    VV_junc11__alpha4 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc4_is_out == 1) and (VV_junc11__Qout4 > VV_junc11__Qout1) and (VV_junc11__Qout4 > VV_junc11__Qout2) and (VV_junc11__Qout4 > VV_junc11__Qout3) else 0)
    VV_junc11__Qout1_rem = (0 if VV_junc11__alpha1 == 1 else VV_junc11__Qout1)
    VV_junc11__Qout2_rem = (0 if VV_junc11__alpha2 == 1 else VV_junc11__Qout2)
    VV_junc11__Qout3_rem = (0 if VV_junc11__alpha3 == 1 else VV_junc11__Qout3)
    VV_junc11__Qout4_rem = (0 if VV_junc11__alpha4 == 1 else VV_junc11__Qout4)
    VV_junc11__beta1 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc1_is_out == 1) and (VV_junc11__alpha1 == 0) and (VV_junc11__Qout1_rem >= VV_junc11__Qout2_rem) and (VV_junc11__Qout1_rem >= VV_junc11__Qout3_rem) and (VV_junc11__Qout1_rem >= VV_junc11__Qout4_rem) else 0)
    VV_junc11__beta2 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc2_is_out == 1) and (VV_junc11__alpha2 == 0) and (VV_junc11__Qout2_rem > VV_junc11__Qout1_rem) and (VV_junc11__Qout2_rem >= VV_junc11__Qout3_rem) and (VV_junc11__Qout2_rem >= VV_junc11__Qout4_rem) else 0)
    VV_junc11__beta3 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc3_is_out == 1) and (VV_junc11__alpha3 == 0) and (VV_junc11__Qout3_rem > VV_junc11__Qout1_rem) and (VV_junc11__Qout3_rem > VV_junc11__Qout2_rem) and (VV_junc11__Qout3_rem >= VV_junc11__Qout4_rem) else 0)
    VV_junc11__beta4 = (1 if (VV_junc11__is_split == 1) and (VV_junc11__bc4_is_out == 1) and (VV_junc11__alpha4 == 0) and (VV_junc11__Qout4_rem > VV_junc11__Qout1_rem) and (VV_junc11__Qout4_rem > VV_junc11__Qout2_rem) and (VV_junc11__Qout4_rem > VV_junc11__Qout3_rem) else 0)
    VV_junc11__D_F = (VV_junc11__D1 if VV_junc11__feed1 == 1 else (VV_junc11__D2 if VV_junc11__feed2 == 1 else (VV_junc11__D3 if VV_junc11__feed3 == 1 else (VV_junc11__D4 if VV_junc11__feed4 == 1 else VV_junc11__D1))))
    VV_junc11__D_alpha = (VV_junc11__D1 if VV_junc11__alpha1 == 1 else (VV_junc11__D2 if VV_junc11__alpha2 == 1 else (VV_junc11__D3 if VV_junc11__alpha3 == 1 else (VV_junc11__D4 if VV_junc11__alpha4 == 1 else VV_junc11__D3))))
    VV_junc11__D_beta = (VV_junc11__D1 if VV_junc11__beta1 == 1 else (VV_junc11__D2 if VV_junc11__beta2 == 1 else (VV_junc11__D3 if VV_junc11__beta3 == 1 else (VV_junc11__D4 if VV_junc11__beta4 == 1 else VV_junc11__D4))))
    VV_junc11__v_alpha = (VV_junc11__Qout1 if VV_junc11__alpha1 == 1 else (VV_junc11__Qout2 if VV_junc11__alpha2 == 1 else (VV_junc11__Qout3 if VV_junc11__alpha3 == 1 else (VV_junc11__Qout4 if VV_junc11__alpha4 == 1 else 0))))
    VV_junc11__v_beta = (VV_junc11__Qout1 if VV_junc11__beta1 == 1 else (VV_junc11__Qout2 if VV_junc11__beta2 == 1 else (VV_junc11__Qout3 if VV_junc11__beta3 == 1 else (VV_junc11__Qout4 if VV_junc11__beta4 == 1 else 0))))
    PV21__H_down_target = PV21__s_v_d*(PV21__H_mean+PV21__gamma_mirror*(PV21__H_mean-PV21__H_up))+(1-PV21__s_v_d)*PV21__H_mean
    PV22__H_down_target = PV22__s_v_d*(PV22__H_mean+PV22__gamma_mirror*(PV22__H_mean-PV22__H_up))+(1-PV22__s_v_d)*PV22__H_mean
    V21__H_down_target = V21__s_v*(V21__H_mean+V21__gamma_mirror*(V21__H_mean-V21__H_up))+(1-V21__s_v)*V21__H_mean
    V22__H_down_target = V22__s_v*(V22__H_mean+V22__gamma_mirror*(V22__H_mean-V22__H_up))+(1-V22__s_v)*V22__H_mean
    VV_junc12__n_in = VV_junc12__bc1_is_in+VV_junc12__bc2_is_in+VV_junc12__bc3_is_in+VV_junc12__bc4_is_in
    VV_junc12__n_out = VV_junc12__bc1_is_out+VV_junc12__bc2_is_out+VV_junc12__bc3_is_out+VV_junc12__bc4_is_out
    VV_junc12__RBC_in = VV_junc12__Qin1*V11__H_R_out+VV_junc12__Qin2*VV_junc12__H_to2+VV_junc12__Qin3*PV23__H_L_out+VV_junc12__Qin4*PV24__H_L_out
    VV_junc12__v_mm3_s = VV_junc12__v/VV_junc12__one_mm3
    VV_junc12__junction_type = (1 if VV_junc12__n_in == 1 else (-1 if VV_junc12__n_in >= 2 else 0))
    VV_junc12__is_split = (1 if VV_junc12__junction_type == 1 else 0)
    VV_junc12__is_merge = (1 if VV_junc12__junction_type == -1 else 0)
    VV_junc12__feed1 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin1 >= VV_junc12__Qin2) and (VV_junc12__Qin1 >= VV_junc12__Qin3) and (VV_junc12__Qin1 >= VV_junc12__Qin4) else 0)
    VV_junc12__feed2 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin2 > VV_junc12__Qin1) and (VV_junc12__Qin2 >= VV_junc12__Qin3) and (VV_junc12__Qin2 >= VV_junc12__Qin4) else 0)
    VV_junc12__feed3 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin3 > VV_junc12__Qin1) and (VV_junc12__Qin3 > VV_junc12__Qin2) and (VV_junc12__Qin3 >= VV_junc12__Qin4) else 0)
    VV_junc12__feed4 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__Qin4 > VV_junc12__Qin1) and (VV_junc12__Qin4 > VV_junc12__Qin2) and (VV_junc12__Qin4 > VV_junc12__Qin3) else 0)
    VV_junc12__alpha1 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc1_is_out == 1) and (VV_junc12__Qout1 >= VV_junc12__Qout2) and (VV_junc12__Qout1 >= VV_junc12__Qout3) and (VV_junc12__Qout1 >= VV_junc12__Qout4) else 0)
    VV_junc12__alpha2 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc2_is_out == 1) and (VV_junc12__Qout2 > VV_junc12__Qout1) and (VV_junc12__Qout2 >= VV_junc12__Qout3) and (VV_junc12__Qout2 >= VV_junc12__Qout4) else 0)
    VV_junc12__alpha3 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc3_is_out == 1) and (VV_junc12__Qout3 > VV_junc12__Qout1) and (VV_junc12__Qout3 > VV_junc12__Qout2) and (VV_junc12__Qout3 >= VV_junc12__Qout4) else 0)
    VV_junc12__alpha4 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc4_is_out == 1) and (VV_junc12__Qout4 > VV_junc12__Qout1) and (VV_junc12__Qout4 > VV_junc12__Qout2) and (VV_junc12__Qout4 > VV_junc12__Qout3) else 0)
    VV_junc12__Qout1_rem = (0 if VV_junc12__alpha1 == 1 else VV_junc12__Qout1)
    VV_junc12__Qout2_rem = (0 if VV_junc12__alpha2 == 1 else VV_junc12__Qout2)
    VV_junc12__Qout3_rem = (0 if VV_junc12__alpha3 == 1 else VV_junc12__Qout3)
    VV_junc12__Qout4_rem = (0 if VV_junc12__alpha4 == 1 else VV_junc12__Qout4)
    VV_junc12__beta1 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc1_is_out == 1) and (VV_junc12__alpha1 == 0) and (VV_junc12__Qout1_rem >= VV_junc12__Qout2_rem) and (VV_junc12__Qout1_rem >= VV_junc12__Qout3_rem) and (VV_junc12__Qout1_rem >= VV_junc12__Qout4_rem) else 0)
    VV_junc12__beta2 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc2_is_out == 1) and (VV_junc12__alpha2 == 0) and (VV_junc12__Qout2_rem > VV_junc12__Qout1_rem) and (VV_junc12__Qout2_rem >= VV_junc12__Qout3_rem) and (VV_junc12__Qout2_rem >= VV_junc12__Qout4_rem) else 0)
    VV_junc12__beta3 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc3_is_out == 1) and (VV_junc12__alpha3 == 0) and (VV_junc12__Qout3_rem > VV_junc12__Qout1_rem) and (VV_junc12__Qout3_rem > VV_junc12__Qout2_rem) and (VV_junc12__Qout3_rem >= VV_junc12__Qout4_rem) else 0)
    VV_junc12__beta4 = (1 if (VV_junc12__is_split == 1) and (VV_junc12__bc4_is_out == 1) and (VV_junc12__alpha4 == 0) and (VV_junc12__Qout4_rem > VV_junc12__Qout1_rem) and (VV_junc12__Qout4_rem > VV_junc12__Qout2_rem) and (VV_junc12__Qout4_rem > VV_junc12__Qout3_rem) else 0)
    VV_junc12__D_F = (VV_junc12__D1 if VV_junc12__feed1 == 1 else (VV_junc12__D2 if VV_junc12__feed2 == 1 else (VV_junc12__D3 if VV_junc12__feed3 == 1 else (VV_junc12__D4 if VV_junc12__feed4 == 1 else VV_junc12__D1))))
    VV_junc12__D_alpha = (VV_junc12__D1 if VV_junc12__alpha1 == 1 else (VV_junc12__D2 if VV_junc12__alpha2 == 1 else (VV_junc12__D3 if VV_junc12__alpha3 == 1 else (VV_junc12__D4 if VV_junc12__alpha4 == 1 else VV_junc12__D3))))
    VV_junc12__D_beta = (VV_junc12__D1 if VV_junc12__beta1 == 1 else (VV_junc12__D2 if VV_junc12__beta2 == 1 else (VV_junc12__D3 if VV_junc12__beta3 == 1 else (VV_junc12__D4 if VV_junc12__beta4 == 1 else VV_junc12__D4))))
    VV_junc12__v_alpha = (VV_junc12__Qout1 if VV_junc12__alpha1 == 1 else (VV_junc12__Qout2 if VV_junc12__alpha2 == 1 else (VV_junc12__Qout3 if VV_junc12__alpha3 == 1 else (VV_junc12__Qout4 if VV_junc12__alpha4 == 1 else 0))))
    VV_junc12__v_beta = (VV_junc12__Qout1 if VV_junc12__beta1 == 1 else (VV_junc12__Qout2 if VV_junc12__beta2 == 1 else (VV_junc12__Qout3 if VV_junc12__beta3 == 1 else (VV_junc12__Qout4 if VV_junc12__beta4 == 1 else 0))))
    PV23__H_down_target = PV23__s_v_d*(PV23__H_mean+PV23__gamma_mirror*(PV23__H_mean-PV23__H_up))+(1-PV23__s_v_d)*PV23__H_mean
    PV24__H_down_target = PV24__s_v_d*(PV24__H_mean+PV24__gamma_mirror*(PV24__H_mean-PV24__H_up))+(1-PV24__s_v_d)*PV24__H_mean
    V23__H_down_target = V23__s_v*(V23__H_mean+V23__gamma_mirror*(V23__H_mean-V23__H_up))+(1-V23__s_v)*V23__H_mean
    V24__H_down_target = V24__s_v*(V24__H_mean+V24__gamma_mirror*(V24__H_mean-V24__H_up))+(1-V24__s_v)*V24__H_mean
    VV_junc13__n_in = VV_junc13__bc1_is_in+VV_junc13__bc2_is_in+VV_junc13__bc3_is_in+VV_junc13__bc4_is_in
    VV_junc13__n_out = VV_junc13__bc1_is_out+VV_junc13__bc2_is_out+VV_junc13__bc3_is_out+VV_junc13__bc4_is_out
    VV_junc13__RBC_in = VV_junc13__Qin1*V12__H_R_out+VV_junc13__Qin2*VV_junc13__H_to2+VV_junc13__Qin3*PV25__H_L_out+VV_junc13__Qin4*PV26__H_L_out
    VV_junc13__v_mm3_s = VV_junc13__v/VV_junc13__one_mm3
    VV_junc13__junction_type = (1 if VV_junc13__n_in == 1 else (-1 if VV_junc13__n_in >= 2 else 0))
    VV_junc13__is_split = (1 if VV_junc13__junction_type == 1 else 0)
    VV_junc13__is_merge = (1 if VV_junc13__junction_type == -1 else 0)
    VV_junc13__feed1 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin1 >= VV_junc13__Qin2) and (VV_junc13__Qin1 >= VV_junc13__Qin3) and (VV_junc13__Qin1 >= VV_junc13__Qin4) else 0)
    VV_junc13__feed2 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin2 > VV_junc13__Qin1) and (VV_junc13__Qin2 >= VV_junc13__Qin3) and (VV_junc13__Qin2 >= VV_junc13__Qin4) else 0)
    VV_junc13__feed3 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin3 > VV_junc13__Qin1) and (VV_junc13__Qin3 > VV_junc13__Qin2) and (VV_junc13__Qin3 >= VV_junc13__Qin4) else 0)
    VV_junc13__feed4 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__Qin4 > VV_junc13__Qin1) and (VV_junc13__Qin4 > VV_junc13__Qin2) and (VV_junc13__Qin4 > VV_junc13__Qin3) else 0)
    VV_junc13__alpha1 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc1_is_out == 1) and (VV_junc13__Qout1 >= VV_junc13__Qout2) and (VV_junc13__Qout1 >= VV_junc13__Qout3) and (VV_junc13__Qout1 >= VV_junc13__Qout4) else 0)
    VV_junc13__alpha2 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc2_is_out == 1) and (VV_junc13__Qout2 > VV_junc13__Qout1) and (VV_junc13__Qout2 >= VV_junc13__Qout3) and (VV_junc13__Qout2 >= VV_junc13__Qout4) else 0)
    VV_junc13__alpha3 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc3_is_out == 1) and (VV_junc13__Qout3 > VV_junc13__Qout1) and (VV_junc13__Qout3 > VV_junc13__Qout2) and (VV_junc13__Qout3 >= VV_junc13__Qout4) else 0)
    VV_junc13__alpha4 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc4_is_out == 1) and (VV_junc13__Qout4 > VV_junc13__Qout1) and (VV_junc13__Qout4 > VV_junc13__Qout2) and (VV_junc13__Qout4 > VV_junc13__Qout3) else 0)
    VV_junc13__Qout1_rem = (0 if VV_junc13__alpha1 == 1 else VV_junc13__Qout1)
    VV_junc13__Qout2_rem = (0 if VV_junc13__alpha2 == 1 else VV_junc13__Qout2)
    VV_junc13__Qout3_rem = (0 if VV_junc13__alpha3 == 1 else VV_junc13__Qout3)
    VV_junc13__Qout4_rem = (0 if VV_junc13__alpha4 == 1 else VV_junc13__Qout4)
    VV_junc13__beta1 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc1_is_out == 1) and (VV_junc13__alpha1 == 0) and (VV_junc13__Qout1_rem >= VV_junc13__Qout2_rem) and (VV_junc13__Qout1_rem >= VV_junc13__Qout3_rem) and (VV_junc13__Qout1_rem >= VV_junc13__Qout4_rem) else 0)
    VV_junc13__beta2 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc2_is_out == 1) and (VV_junc13__alpha2 == 0) and (VV_junc13__Qout2_rem > VV_junc13__Qout1_rem) and (VV_junc13__Qout2_rem >= VV_junc13__Qout3_rem) and (VV_junc13__Qout2_rem >= VV_junc13__Qout4_rem) else 0)
    VV_junc13__beta3 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc3_is_out == 1) and (VV_junc13__alpha3 == 0) and (VV_junc13__Qout3_rem > VV_junc13__Qout1_rem) and (VV_junc13__Qout3_rem > VV_junc13__Qout2_rem) and (VV_junc13__Qout3_rem >= VV_junc13__Qout4_rem) else 0)
    VV_junc13__beta4 = (1 if (VV_junc13__is_split == 1) and (VV_junc13__bc4_is_out == 1) and (VV_junc13__alpha4 == 0) and (VV_junc13__Qout4_rem > VV_junc13__Qout1_rem) and (VV_junc13__Qout4_rem > VV_junc13__Qout2_rem) and (VV_junc13__Qout4_rem > VV_junc13__Qout3_rem) else 0)
    VV_junc13__D_F = (VV_junc13__D1 if VV_junc13__feed1 == 1 else (VV_junc13__D2 if VV_junc13__feed2 == 1 else (VV_junc13__D3 if VV_junc13__feed3 == 1 else (VV_junc13__D4 if VV_junc13__feed4 == 1 else VV_junc13__D1))))
    VV_junc13__D_alpha = (VV_junc13__D1 if VV_junc13__alpha1 == 1 else (VV_junc13__D2 if VV_junc13__alpha2 == 1 else (VV_junc13__D3 if VV_junc13__alpha3 == 1 else (VV_junc13__D4 if VV_junc13__alpha4 == 1 else VV_junc13__D3))))
    VV_junc13__D_beta = (VV_junc13__D1 if VV_junc13__beta1 == 1 else (VV_junc13__D2 if VV_junc13__beta2 == 1 else (VV_junc13__D3 if VV_junc13__beta3 == 1 else (VV_junc13__D4 if VV_junc13__beta4 == 1 else VV_junc13__D4))))
    VV_junc13__v_alpha = (VV_junc13__Qout1 if VV_junc13__alpha1 == 1 else (VV_junc13__Qout2 if VV_junc13__alpha2 == 1 else (VV_junc13__Qout3 if VV_junc13__alpha3 == 1 else (VV_junc13__Qout4 if VV_junc13__alpha4 == 1 else 0))))
    VV_junc13__v_beta = (VV_junc13__Qout1 if VV_junc13__beta1 == 1 else (VV_junc13__Qout2 if VV_junc13__beta2 == 1 else (VV_junc13__Qout3 if VV_junc13__beta3 == 1 else (VV_junc13__Qout4 if VV_junc13__beta4 == 1 else 0))))
    PV25__H_down_target = PV25__s_v_d*(PV25__H_mean+PV25__gamma_mirror*(PV25__H_mean-PV25__H_up))+(1-PV25__s_v_d)*PV25__H_mean
    PV26__H_down_target = PV26__s_v_d*(PV26__H_mean+PV26__gamma_mirror*(PV26__H_mean-PV26__H_up))+(1-PV26__s_v_d)*PV26__H_mean
    V25__H_down_target = V25__s_v*(V25__H_mean+V25__gamma_mirror*(V25__H_mean-V25__H_up))+(1-V25__s_v)*V25__H_mean
    V26__H_down_target = V26__s_v*(V26__H_mean+V26__gamma_mirror*(V26__H_mean-V26__H_up))+(1-V26__s_v)*V26__H_mean
    VV_junc14__n_in = VV_junc14__bc1_is_in+VV_junc14__bc2_is_in+VV_junc14__bc3_is_in+VV_junc14__bc4_is_in
    VV_junc14__n_out = VV_junc14__bc1_is_out+VV_junc14__bc2_is_out+VV_junc14__bc3_is_out+VV_junc14__bc4_is_out
    VV_junc14__RBC_in = VV_junc14__Qin1*V13__H_R_out+VV_junc14__Qin2*VV_junc14__H_to2+VV_junc14__Qin3*PV27__H_L_out+VV_junc14__Qin4*PV28__H_L_out
    VV_junc14__v_mm3_s = VV_junc14__v/VV_junc14__one_mm3
    VV_junc14__junction_type = (1 if VV_junc14__n_in == 1 else (-1 if VV_junc14__n_in >= 2 else 0))
    VV_junc14__is_split = (1 if VV_junc14__junction_type == 1 else 0)
    VV_junc14__is_merge = (1 if VV_junc14__junction_type == -1 else 0)
    VV_junc14__feed1 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin1 >= VV_junc14__Qin2) and (VV_junc14__Qin1 >= VV_junc14__Qin3) and (VV_junc14__Qin1 >= VV_junc14__Qin4) else 0)
    VV_junc14__feed2 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin2 > VV_junc14__Qin1) and (VV_junc14__Qin2 >= VV_junc14__Qin3) and (VV_junc14__Qin2 >= VV_junc14__Qin4) else 0)
    VV_junc14__feed3 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin3 > VV_junc14__Qin1) and (VV_junc14__Qin3 > VV_junc14__Qin2) and (VV_junc14__Qin3 >= VV_junc14__Qin4) else 0)
    VV_junc14__feed4 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__Qin4 > VV_junc14__Qin1) and (VV_junc14__Qin4 > VV_junc14__Qin2) and (VV_junc14__Qin4 > VV_junc14__Qin3) else 0)
    VV_junc14__alpha1 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc1_is_out == 1) and (VV_junc14__Qout1 >= VV_junc14__Qout2) and (VV_junc14__Qout1 >= VV_junc14__Qout3) and (VV_junc14__Qout1 >= VV_junc14__Qout4) else 0)
    VV_junc14__alpha2 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc2_is_out == 1) and (VV_junc14__Qout2 > VV_junc14__Qout1) and (VV_junc14__Qout2 >= VV_junc14__Qout3) and (VV_junc14__Qout2 >= VV_junc14__Qout4) else 0)
    VV_junc14__alpha3 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc3_is_out == 1) and (VV_junc14__Qout3 > VV_junc14__Qout1) and (VV_junc14__Qout3 > VV_junc14__Qout2) and (VV_junc14__Qout3 >= VV_junc14__Qout4) else 0)
    VV_junc14__alpha4 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc4_is_out == 1) and (VV_junc14__Qout4 > VV_junc14__Qout1) and (VV_junc14__Qout4 > VV_junc14__Qout2) and (VV_junc14__Qout4 > VV_junc14__Qout3) else 0)
    VV_junc14__Qout1_rem = (0 if VV_junc14__alpha1 == 1 else VV_junc14__Qout1)
    VV_junc14__Qout2_rem = (0 if VV_junc14__alpha2 == 1 else VV_junc14__Qout2)
    VV_junc14__Qout3_rem = (0 if VV_junc14__alpha3 == 1 else VV_junc14__Qout3)
    VV_junc14__Qout4_rem = (0 if VV_junc14__alpha4 == 1 else VV_junc14__Qout4)
    VV_junc14__beta1 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc1_is_out == 1) and (VV_junc14__alpha1 == 0) and (VV_junc14__Qout1_rem >= VV_junc14__Qout2_rem) and (VV_junc14__Qout1_rem >= VV_junc14__Qout3_rem) and (VV_junc14__Qout1_rem >= VV_junc14__Qout4_rem) else 0)
    VV_junc14__beta2 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc2_is_out == 1) and (VV_junc14__alpha2 == 0) and (VV_junc14__Qout2_rem > VV_junc14__Qout1_rem) and (VV_junc14__Qout2_rem >= VV_junc14__Qout3_rem) and (VV_junc14__Qout2_rem >= VV_junc14__Qout4_rem) else 0)
    VV_junc14__beta3 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc3_is_out == 1) and (VV_junc14__alpha3 == 0) and (VV_junc14__Qout3_rem > VV_junc14__Qout1_rem) and (VV_junc14__Qout3_rem > VV_junc14__Qout2_rem) and (VV_junc14__Qout3_rem >= VV_junc14__Qout4_rem) else 0)
    VV_junc14__beta4 = (1 if (VV_junc14__is_split == 1) and (VV_junc14__bc4_is_out == 1) and (VV_junc14__alpha4 == 0) and (VV_junc14__Qout4_rem > VV_junc14__Qout1_rem) and (VV_junc14__Qout4_rem > VV_junc14__Qout2_rem) and (VV_junc14__Qout4_rem > VV_junc14__Qout3_rem) else 0)
    VV_junc14__D_F = (VV_junc14__D1 if VV_junc14__feed1 == 1 else (VV_junc14__D2 if VV_junc14__feed2 == 1 else (VV_junc14__D3 if VV_junc14__feed3 == 1 else (VV_junc14__D4 if VV_junc14__feed4 == 1 else VV_junc14__D1))))
    VV_junc14__D_alpha = (VV_junc14__D1 if VV_junc14__alpha1 == 1 else (VV_junc14__D2 if VV_junc14__alpha2 == 1 else (VV_junc14__D3 if VV_junc14__alpha3 == 1 else (VV_junc14__D4 if VV_junc14__alpha4 == 1 else VV_junc14__D3))))
    VV_junc14__D_beta = (VV_junc14__D1 if VV_junc14__beta1 == 1 else (VV_junc14__D2 if VV_junc14__beta2 == 1 else (VV_junc14__D3 if VV_junc14__beta3 == 1 else (VV_junc14__D4 if VV_junc14__beta4 == 1 else VV_junc14__D4))))
    VV_junc14__v_alpha = (VV_junc14__Qout1 if VV_junc14__alpha1 == 1 else (VV_junc14__Qout2 if VV_junc14__alpha2 == 1 else (VV_junc14__Qout3 if VV_junc14__alpha3 == 1 else (VV_junc14__Qout4 if VV_junc14__alpha4 == 1 else 0))))
    VV_junc14__v_beta = (VV_junc14__Qout1 if VV_junc14__beta1 == 1 else (VV_junc14__Qout2 if VV_junc14__beta2 == 1 else (VV_junc14__Qout3 if VV_junc14__beta3 == 1 else (VV_junc14__Qout4 if VV_junc14__beta4 == 1 else 0))))
    PV27__H_down_target = PV27__s_v_d*(PV27__H_mean+PV27__gamma_mirror*(PV27__H_mean-PV27__H_up))+(1-PV27__s_v_d)*PV27__H_mean
    PV28__H_down_target = PV28__s_v_d*(PV28__H_mean+PV28__gamma_mirror*(PV28__H_mean-PV28__H_up))+(1-PV28__s_v_d)*PV28__H_mean
    V27__H_down_target = V27__s_v*(V27__H_mean+V27__gamma_mirror*(V27__H_mean-V27__H_up))+(1-V27__s_v)*V27__H_mean
    V28__H_down_target = V28__s_v*(V28__H_mean+V28__gamma_mirror*(V28__H_mean-V28__H_up))+(1-V28__s_v)*V28__H_mean
    VV_junc15__n_in = VV_junc15__bc1_is_in+VV_junc15__bc2_is_in+VV_junc15__bc3_is_in+VV_junc15__bc4_is_in
    VV_junc15__n_out = VV_junc15__bc1_is_out+VV_junc15__bc2_is_out+VV_junc15__bc3_is_out+VV_junc15__bc4_is_out
    VV_junc15__RBC_in = VV_junc15__Qin1*V14__H_R_out+VV_junc15__Qin2*VV_junc15__H_to2+VV_junc15__Qin3*PV29__H_L_out+VV_junc15__Qin4*PV30__H_L_out
    VV_junc15__v_mm3_s = VV_junc15__v/VV_junc15__one_mm3
    VV_junc15__junction_type = (1 if VV_junc15__n_in == 1 else (-1 if VV_junc15__n_in >= 2 else 0))
    VV_junc15__is_split = (1 if VV_junc15__junction_type == 1 else 0)
    VV_junc15__is_merge = (1 if VV_junc15__junction_type == -1 else 0)
    VV_junc15__feed1 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin1 >= VV_junc15__Qin2) and (VV_junc15__Qin1 >= VV_junc15__Qin3) and (VV_junc15__Qin1 >= VV_junc15__Qin4) else 0)
    VV_junc15__feed2 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin2 > VV_junc15__Qin1) and (VV_junc15__Qin2 >= VV_junc15__Qin3) and (VV_junc15__Qin2 >= VV_junc15__Qin4) else 0)
    VV_junc15__feed3 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin3 > VV_junc15__Qin1) and (VV_junc15__Qin3 > VV_junc15__Qin2) and (VV_junc15__Qin3 >= VV_junc15__Qin4) else 0)
    VV_junc15__feed4 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__Qin4 > VV_junc15__Qin1) and (VV_junc15__Qin4 > VV_junc15__Qin2) and (VV_junc15__Qin4 > VV_junc15__Qin3) else 0)
    VV_junc15__alpha1 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc1_is_out == 1) and (VV_junc15__Qout1 >= VV_junc15__Qout2) and (VV_junc15__Qout1 >= VV_junc15__Qout3) and (VV_junc15__Qout1 >= VV_junc15__Qout4) else 0)
    VV_junc15__alpha2 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc2_is_out == 1) and (VV_junc15__Qout2 > VV_junc15__Qout1) and (VV_junc15__Qout2 >= VV_junc15__Qout3) and (VV_junc15__Qout2 >= VV_junc15__Qout4) else 0)
    VV_junc15__alpha3 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc3_is_out == 1) and (VV_junc15__Qout3 > VV_junc15__Qout1) and (VV_junc15__Qout3 > VV_junc15__Qout2) and (VV_junc15__Qout3 >= VV_junc15__Qout4) else 0)
    VV_junc15__alpha4 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc4_is_out == 1) and (VV_junc15__Qout4 > VV_junc15__Qout1) and (VV_junc15__Qout4 > VV_junc15__Qout2) and (VV_junc15__Qout4 > VV_junc15__Qout3) else 0)
    VV_junc15__Qout1_rem = (0 if VV_junc15__alpha1 == 1 else VV_junc15__Qout1)
    VV_junc15__Qout2_rem = (0 if VV_junc15__alpha2 == 1 else VV_junc15__Qout2)
    VV_junc15__Qout3_rem = (0 if VV_junc15__alpha3 == 1 else VV_junc15__Qout3)
    VV_junc15__Qout4_rem = (0 if VV_junc15__alpha4 == 1 else VV_junc15__Qout4)
    VV_junc15__beta1 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc1_is_out == 1) and (VV_junc15__alpha1 == 0) and (VV_junc15__Qout1_rem >= VV_junc15__Qout2_rem) and (VV_junc15__Qout1_rem >= VV_junc15__Qout3_rem) and (VV_junc15__Qout1_rem >= VV_junc15__Qout4_rem) else 0)
    VV_junc15__beta2 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc2_is_out == 1) and (VV_junc15__alpha2 == 0) and (VV_junc15__Qout2_rem > VV_junc15__Qout1_rem) and (VV_junc15__Qout2_rem >= VV_junc15__Qout3_rem) and (VV_junc15__Qout2_rem >= VV_junc15__Qout4_rem) else 0)
    VV_junc15__beta3 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc3_is_out == 1) and (VV_junc15__alpha3 == 0) and (VV_junc15__Qout3_rem > VV_junc15__Qout1_rem) and (VV_junc15__Qout3_rem > VV_junc15__Qout2_rem) and (VV_junc15__Qout3_rem >= VV_junc15__Qout4_rem) else 0)
    VV_junc15__beta4 = (1 if (VV_junc15__is_split == 1) and (VV_junc15__bc4_is_out == 1) and (VV_junc15__alpha4 == 0) and (VV_junc15__Qout4_rem > VV_junc15__Qout1_rem) and (VV_junc15__Qout4_rem > VV_junc15__Qout2_rem) and (VV_junc15__Qout4_rem > VV_junc15__Qout3_rem) else 0)
    VV_junc15__D_F = (VV_junc15__D1 if VV_junc15__feed1 == 1 else (VV_junc15__D2 if VV_junc15__feed2 == 1 else (VV_junc15__D3 if VV_junc15__feed3 == 1 else (VV_junc15__D4 if VV_junc15__feed4 == 1 else VV_junc15__D1))))
    VV_junc15__D_alpha = (VV_junc15__D1 if VV_junc15__alpha1 == 1 else (VV_junc15__D2 if VV_junc15__alpha2 == 1 else (VV_junc15__D3 if VV_junc15__alpha3 == 1 else (VV_junc15__D4 if VV_junc15__alpha4 == 1 else VV_junc15__D3))))
    VV_junc15__D_beta = (VV_junc15__D1 if VV_junc15__beta1 == 1 else (VV_junc15__D2 if VV_junc15__beta2 == 1 else (VV_junc15__D3 if VV_junc15__beta3 == 1 else (VV_junc15__D4 if VV_junc15__beta4 == 1 else VV_junc15__D4))))
    VV_junc15__v_alpha = (VV_junc15__Qout1 if VV_junc15__alpha1 == 1 else (VV_junc15__Qout2 if VV_junc15__alpha2 == 1 else (VV_junc15__Qout3 if VV_junc15__alpha3 == 1 else (VV_junc15__Qout4 if VV_junc15__alpha4 == 1 else 0))))
    VV_junc15__v_beta = (VV_junc15__Qout1 if VV_junc15__beta1 == 1 else (VV_junc15__Qout2 if VV_junc15__beta2 == 1 else (VV_junc15__Qout3 if VV_junc15__beta3 == 1 else (VV_junc15__Qout4 if VV_junc15__beta4 == 1 else 0))))
    PV29__H_down_target = PV29__s_v_d*(PV29__H_mean+PV29__gamma_mirror*(PV29__H_mean-PV29__H_up))+(1-PV29__s_v_d)*PV29__H_mean
    PV30__H_down_target = PV30__s_v_d*(PV30__H_mean+PV30__gamma_mirror*(PV30__H_mean-PV30__H_up))+(1-PV30__s_v_d)*PV30__H_mean
    V29__H_down_target = V29__s_v*(V29__H_mean+V29__gamma_mirror*(V29__H_mean-V29__H_up))+(1-V29__s_v)*V29__H_mean
    V30__H_down_target = V30__s_v*(V30__H_mean+V30__gamma_mirror*(V30__H_mean-V30__H_up))+(1-V30__s_v)*V30__H_mean
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
    V7__H_down_target = V7__s_v*(V7__H_mean+V7__gamma_mirror*(V7__H_mean-V7__H_up))+(1-V7__s_v)*V7__H_mean
    V8__H_down_target = V8__s_v*(V8__H_mean+V8__gamma_mirror*(V8__H_mean-V8__H_up))+(1-V8__s_v)*V8__H_mean
    VV_junc5__FQB_alpha = (VV_junc5__v_alpha+VV_junc5__div_0)/(VV_junc5__v_alpha+VV_junc5__v_beta+2*VV_junc5__div_0)
    VV_junc5__B = 1+6.98*(1-VV_junc5__H_mean)/(VV_junc5__D_F*1e6)
    VV_junc5__A = -6.96*np.log(VV_junc5__D_alpha*1e6/(VV_junc5__D_beta*1e6))/(VV_junc5__D_F*1e6)
    VV_junc5__X_0 = 0.4/(VV_junc5__D_F*1e6)
    VV_junc5__y_raw = (VV_junc5__FQB_alpha-VV_junc5__X_0)/(1-2*VV_junc5__X_0+VV_junc5__div_0)
    VV_junc5__y = min(max(VV_junc5__y_raw, VV_junc5__div_0y), 1-VV_junc5__div_0y)
    V9__H_down_target = V9__s_v*(V9__H_mean+V9__gamma_mirror*(V9__H_mean-V9__H_up))+(1-V9__s_v)*V9__H_mean
    V10__H_down_target = V10__s_v*(V10__H_mean+V10__gamma_mirror*(V10__H_mean-V10__H_up))+(1-V10__s_v)*V10__H_mean
    VV_junc6__FQB_alpha = (VV_junc6__v_alpha+VV_junc6__div_0)/(VV_junc6__v_alpha+VV_junc6__v_beta+2*VV_junc6__div_0)
    VV_junc6__B = 1+6.98*(1-VV_junc6__H_mean)/(VV_junc6__D_F*1e6)
    VV_junc6__A = -6.96*np.log(VV_junc6__D_alpha*1e6/(VV_junc6__D_beta*1e6))/(VV_junc6__D_F*1e6)
    VV_junc6__X_0 = 0.4/(VV_junc6__D_F*1e6)
    VV_junc6__y_raw = (VV_junc6__FQB_alpha-VV_junc6__X_0)/(1-2*VV_junc6__X_0+VV_junc6__div_0)
    VV_junc6__y = min(max(VV_junc6__y_raw, VV_junc6__div_0y), 1-VV_junc6__div_0y)
    V11__H_down_target = V11__s_v*(V11__H_mean+V11__gamma_mirror*(V11__H_mean-V11__H_up))+(1-V11__s_v)*V11__H_mean
    V12__H_down_target = V12__s_v*(V12__H_mean+V12__gamma_mirror*(V12__H_mean-V12__H_up))+(1-V12__s_v)*V12__H_mean
    VV_junc7__FQB_alpha = (VV_junc7__v_alpha+VV_junc7__div_0)/(VV_junc7__v_alpha+VV_junc7__v_beta+2*VV_junc7__div_0)
    VV_junc7__B = 1+6.98*(1-VV_junc7__H_mean)/(VV_junc7__D_F*1e6)
    VV_junc7__A = -6.96*np.log(VV_junc7__D_alpha*1e6/(VV_junc7__D_beta*1e6))/(VV_junc7__D_F*1e6)
    VV_junc7__X_0 = 0.4/(VV_junc7__D_F*1e6)
    VV_junc7__y_raw = (VV_junc7__FQB_alpha-VV_junc7__X_0)/(1-2*VV_junc7__X_0+VV_junc7__div_0)
    VV_junc7__y = min(max(VV_junc7__y_raw, VV_junc7__div_0y), 1-VV_junc7__div_0y)
    V13__H_down_target = V13__s_v*(V13__H_mean+V13__gamma_mirror*(V13__H_mean-V13__H_up))+(1-V13__s_v)*V13__H_mean
    V14__H_down_target = V14__s_v*(V14__H_mean+V14__gamma_mirror*(V14__H_mean-V14__H_up))+(1-V14__s_v)*V14__H_mean
    VV_junc8__FQB_alpha = (VV_junc8__v_alpha+VV_junc8__div_0)/(VV_junc8__v_alpha+VV_junc8__v_beta+2*VV_junc8__div_0)
    VV_junc8__B = 1+6.98*(1-VV_junc8__H_mean)/(VV_junc8__D_F*1e6)
    VV_junc8__A = -6.96*np.log(VV_junc8__D_alpha*1e6/(VV_junc8__D_beta*1e6))/(VV_junc8__D_F*1e6)
    VV_junc8__X_0 = 0.4/(VV_junc8__D_F*1e6)
    VV_junc8__y_raw = (VV_junc8__FQB_alpha-VV_junc8__X_0)/(1-2*VV_junc8__X_0+VV_junc8__div_0)
    VV_junc8__y = min(max(VV_junc8__y_raw, VV_junc8__div_0y), 1-VV_junc8__div_0y)
    VV_junc9__FQB_alpha = (VV_junc9__v_alpha+VV_junc9__div_0)/(VV_junc9__v_alpha+VV_junc9__v_beta+2*VV_junc9__div_0)
    VV_junc9__B = 1+6.98*(1-VV_junc9__H_mean)/(VV_junc9__D_F*1e6)
    VV_junc9__A = -6.96*np.log(VV_junc9__D_alpha*1e6/(VV_junc9__D_beta*1e6))/(VV_junc9__D_F*1e6)
    VV_junc9__X_0 = 0.4/(VV_junc9__D_F*1e6)
    VV_junc9__y_raw = (VV_junc9__FQB_alpha-VV_junc9__X_0)/(1-2*VV_junc9__X_0+VV_junc9__div_0)
    VV_junc9__y = min(max(VV_junc9__y_raw, VV_junc9__div_0y), 1-VV_junc9__div_0y)
    VV_junc10__FQB_alpha = (VV_junc10__v_alpha+VV_junc10__div_0)/(VV_junc10__v_alpha+VV_junc10__v_beta+2*VV_junc10__div_0)
    VV_junc10__B = 1+6.98*(1-VV_junc10__H_mean)/(VV_junc10__D_F*1e6)
    VV_junc10__A = -6.96*np.log(VV_junc10__D_alpha*1e6/(VV_junc10__D_beta*1e6))/(VV_junc10__D_F*1e6)
    VV_junc10__X_0 = 0.4/(VV_junc10__D_F*1e6)
    VV_junc10__y_raw = (VV_junc10__FQB_alpha-VV_junc10__X_0)/(1-2*VV_junc10__X_0+VV_junc10__div_0)
    VV_junc10__y = min(max(VV_junc10__y_raw, VV_junc10__div_0y), 1-VV_junc10__div_0y)
    VV_junc11__FQB_alpha = (VV_junc11__v_alpha+VV_junc11__div_0)/(VV_junc11__v_alpha+VV_junc11__v_beta+2*VV_junc11__div_0)
    VV_junc11__B = 1+6.98*(1-VV_junc11__H_mean)/(VV_junc11__D_F*1e6)
    VV_junc11__A = -6.96*np.log(VV_junc11__D_alpha*1e6/(VV_junc11__D_beta*1e6))/(VV_junc11__D_F*1e6)
    VV_junc11__X_0 = 0.4/(VV_junc11__D_F*1e6)
    VV_junc11__y_raw = (VV_junc11__FQB_alpha-VV_junc11__X_0)/(1-2*VV_junc11__X_0+VV_junc11__div_0)
    VV_junc11__y = min(max(VV_junc11__y_raw, VV_junc11__div_0y), 1-VV_junc11__div_0y)
    VV_junc12__FQB_alpha = (VV_junc12__v_alpha+VV_junc12__div_0)/(VV_junc12__v_alpha+VV_junc12__v_beta+2*VV_junc12__div_0)
    VV_junc12__B = 1+6.98*(1-VV_junc12__H_mean)/(VV_junc12__D_F*1e6)
    VV_junc12__A = -6.96*np.log(VV_junc12__D_alpha*1e6/(VV_junc12__D_beta*1e6))/(VV_junc12__D_F*1e6)
    VV_junc12__X_0 = 0.4/(VV_junc12__D_F*1e6)
    VV_junc12__y_raw = (VV_junc12__FQB_alpha-VV_junc12__X_0)/(1-2*VV_junc12__X_0+VV_junc12__div_0)
    VV_junc12__y = min(max(VV_junc12__y_raw, VV_junc12__div_0y), 1-VV_junc12__div_0y)
    VV_junc13__FQB_alpha = (VV_junc13__v_alpha+VV_junc13__div_0)/(VV_junc13__v_alpha+VV_junc13__v_beta+2*VV_junc13__div_0)
    VV_junc13__B = 1+6.98*(1-VV_junc13__H_mean)/(VV_junc13__D_F*1e6)
    VV_junc13__A = -6.96*np.log(VV_junc13__D_alpha*1e6/(VV_junc13__D_beta*1e6))/(VV_junc13__D_F*1e6)
    VV_junc13__X_0 = 0.4/(VV_junc13__D_F*1e6)
    VV_junc13__y_raw = (VV_junc13__FQB_alpha-VV_junc13__X_0)/(1-2*VV_junc13__X_0+VV_junc13__div_0)
    VV_junc13__y = min(max(VV_junc13__y_raw, VV_junc13__div_0y), 1-VV_junc13__div_0y)
    VV_junc14__FQB_alpha = (VV_junc14__v_alpha+VV_junc14__div_0)/(VV_junc14__v_alpha+VV_junc14__v_beta+2*VV_junc14__div_0)
    VV_junc14__B = 1+6.98*(1-VV_junc14__H_mean)/(VV_junc14__D_F*1e6)
    VV_junc14__A = -6.96*np.log(VV_junc14__D_alpha*1e6/(VV_junc14__D_beta*1e6))/(VV_junc14__D_F*1e6)
    VV_junc14__X_0 = 0.4/(VV_junc14__D_F*1e6)
    VV_junc14__y_raw = (VV_junc14__FQB_alpha-VV_junc14__X_0)/(1-2*VV_junc14__X_0+VV_junc14__div_0)
    VV_junc14__y = min(max(VV_junc14__y_raw, VV_junc14__div_0y), 1-VV_junc14__div_0y)
    VV_junc15__FQB_alpha = (VV_junc15__v_alpha+VV_junc15__div_0)/(VV_junc15__v_alpha+VV_junc15__v_beta+2*VV_junc15__div_0)
    VV_junc15__B = 1+6.98*(1-VV_junc15__H_mean)/(VV_junc15__D_F*1e6)
    VV_junc15__A = -6.96*np.log(VV_junc15__D_alpha*1e6/(VV_junc15__D_beta*1e6))/(VV_junc15__D_F*1e6)
    VV_junc15__X_0 = 0.4/(VV_junc15__D_F*1e6)
    VV_junc15__y_raw = (VV_junc15__FQB_alpha-VV_junc15__X_0)/(1-2*VV_junc15__X_0+VV_junc15__div_0)
    VV_junc15__y = min(max(VV_junc15__y_raw, VV_junc15__div_0y), 1-VV_junc15__div_0y)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc2__ph = np.log(VV_junc2__y/(1-VV_junc2__y))
    VV_junc3__ph = np.log(VV_junc3__y/(1-VV_junc3__y))
    VV_junc4__ph = np.log(VV_junc4__y/(1-VV_junc4__y))
    VV_junc5__ph = np.log(VV_junc5__y/(1-VV_junc5__y))
    VV_junc6__ph = np.log(VV_junc6__y/(1-VV_junc6__y))
    VV_junc7__ph = np.log(VV_junc7__y/(1-VV_junc7__y))
    VV_junc8__ph = np.log(VV_junc8__y/(1-VV_junc8__y))
    VV_junc9__ph = np.log(VV_junc9__y/(1-VV_junc9__y))
    VV_junc10__ph = np.log(VV_junc10__y/(1-VV_junc10__y))
    VV_junc11__ph = np.log(VV_junc11__y/(1-VV_junc11__y))
    VV_junc12__ph = np.log(VV_junc12__y/(1-VV_junc12__y))
    VV_junc13__ph = np.log(VV_junc13__y/(1-VV_junc13__y))
    VV_junc14__ph = np.log(VV_junc14__y/(1-VV_junc14__y))
    VV_junc15__ph = np.log(VV_junc15__y/(1-VV_junc15__y))
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
    VV_junc8__FQE_alpha = 1/(1+np.exp(-(VV_junc8__A+VV_junc8__B*VV_junc8__ph)))
    VV_junc8__H_VV_out_alpha = VV_junc8__H_mean*VV_junc8__FQE_alpha/(VV_junc8__FQB_alpha+VV_junc8__div_0)
    VV_junc8__H_VV_out_beta = VV_junc8__H_mean*(1-VV_junc8__FQE_alpha)/(1-VV_junc8__FQB_alpha+VV_junc8__div_0)
    VV_junc8__H_split1 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha1 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta1 == 1 else V7__H_R_out))
    VV_junc8__H_split2 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha2 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta2 == 1 else VV_junc8__H_to2))
    VV_junc8__H_split3 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha3 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta3 == 1 else PV15__H_L_out))
    VV_junc8__H_split4 = (VV_junc8__H_VV_out_alpha if VV_junc8__alpha4 == 1 else (VV_junc8__H_VV_out_beta if VV_junc8__beta4 == 1 else PV16__H_L_out))
    VV_junc8__H_daughter1 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split1 if VV_junc8__is_split == 1 else V7__H_R_out))
    VV_junc8__H_daughter2 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split2 if VV_junc8__is_split == 1 else VV_junc8__H_to2))
    VV_junc8__H_daughter3 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split3 if VV_junc8__is_split == 1 else PV15__H_L_out))
    VV_junc8__H_daughter4 = (VV_junc8__H_mean if VV_junc8__is_merge == 1 else (VV_junc8__H_split4 if VV_junc8__is_split == 1 else PV16__H_L_out))
    VV_junc8__H_from1_target = (VV_junc8__H_daughter1 if VV_junc8__bc1_is_out == 1 else V7__H_R_out)
    VV_junc8__H_from2_target = (VV_junc8__H_daughter2 if VV_junc8__bc2_is_out == 1 else VV_junc8__H_to2)
    VV_junc8__H_from3_target = (VV_junc8__H_daughter3 if VV_junc8__bc3_is_out == 1 else PV15__H_L_out)
    VV_junc8__H_from4_target = (VV_junc8__H_daughter4 if VV_junc8__bc4_is_out == 1 else PV16__H_L_out)
    VV_junc9__FQE_alpha = 1/(1+np.exp(-(VV_junc9__A+VV_junc9__B*VV_junc9__ph)))
    VV_junc9__H_VV_out_alpha = VV_junc9__H_mean*VV_junc9__FQE_alpha/(VV_junc9__FQB_alpha+VV_junc9__div_0)
    VV_junc9__H_VV_out_beta = VV_junc9__H_mean*(1-VV_junc9__FQE_alpha)/(1-VV_junc9__FQB_alpha+VV_junc9__div_0)
    VV_junc9__H_split1 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha1 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta1 == 1 else V8__H_R_out))
    VV_junc9__H_split2 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha2 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta2 == 1 else VV_junc9__H_to2))
    VV_junc9__H_split3 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha3 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta3 == 1 else PV17__H_L_out))
    VV_junc9__H_split4 = (VV_junc9__H_VV_out_alpha if VV_junc9__alpha4 == 1 else (VV_junc9__H_VV_out_beta if VV_junc9__beta4 == 1 else PV18__H_L_out))
    VV_junc9__H_daughter1 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split1 if VV_junc9__is_split == 1 else V8__H_R_out))
    VV_junc9__H_daughter2 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split2 if VV_junc9__is_split == 1 else VV_junc9__H_to2))
    VV_junc9__H_daughter3 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split3 if VV_junc9__is_split == 1 else PV17__H_L_out))
    VV_junc9__H_daughter4 = (VV_junc9__H_mean if VV_junc9__is_merge == 1 else (VV_junc9__H_split4 if VV_junc9__is_split == 1 else PV18__H_L_out))
    VV_junc9__H_from1_target = (VV_junc9__H_daughter1 if VV_junc9__bc1_is_out == 1 else V8__H_R_out)
    VV_junc9__H_from2_target = (VV_junc9__H_daughter2 if VV_junc9__bc2_is_out == 1 else VV_junc9__H_to2)
    VV_junc9__H_from3_target = (VV_junc9__H_daughter3 if VV_junc9__bc3_is_out == 1 else PV17__H_L_out)
    VV_junc9__H_from4_target = (VV_junc9__H_daughter4 if VV_junc9__bc4_is_out == 1 else PV18__H_L_out)
    VV_junc10__FQE_alpha = 1/(1+np.exp(-(VV_junc10__A+VV_junc10__B*VV_junc10__ph)))
    VV_junc10__H_VV_out_alpha = VV_junc10__H_mean*VV_junc10__FQE_alpha/(VV_junc10__FQB_alpha+VV_junc10__div_0)
    VV_junc10__H_VV_out_beta = VV_junc10__H_mean*(1-VV_junc10__FQE_alpha)/(1-VV_junc10__FQB_alpha+VV_junc10__div_0)
    VV_junc10__H_split1 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha1 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta1 == 1 else V9__H_R_out))
    VV_junc10__H_split2 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha2 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta2 == 1 else VV_junc10__H_to2))
    VV_junc10__H_split3 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha3 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta3 == 1 else PV19__H_L_out))
    VV_junc10__H_split4 = (VV_junc10__H_VV_out_alpha if VV_junc10__alpha4 == 1 else (VV_junc10__H_VV_out_beta if VV_junc10__beta4 == 1 else PV20__H_L_out))
    VV_junc10__H_daughter1 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split1 if VV_junc10__is_split == 1 else V9__H_R_out))
    VV_junc10__H_daughter2 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split2 if VV_junc10__is_split == 1 else VV_junc10__H_to2))
    VV_junc10__H_daughter3 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split3 if VV_junc10__is_split == 1 else PV19__H_L_out))
    VV_junc10__H_daughter4 = (VV_junc10__H_mean if VV_junc10__is_merge == 1 else (VV_junc10__H_split4 if VV_junc10__is_split == 1 else PV20__H_L_out))
    VV_junc10__H_from1_target = (VV_junc10__H_daughter1 if VV_junc10__bc1_is_out == 1 else V9__H_R_out)
    VV_junc10__H_from2_target = (VV_junc10__H_daughter2 if VV_junc10__bc2_is_out == 1 else VV_junc10__H_to2)
    VV_junc10__H_from3_target = (VV_junc10__H_daughter3 if VV_junc10__bc3_is_out == 1 else PV19__H_L_out)
    VV_junc10__H_from4_target = (VV_junc10__H_daughter4 if VV_junc10__bc4_is_out == 1 else PV20__H_L_out)
    VV_junc11__FQE_alpha = 1/(1+np.exp(-(VV_junc11__A+VV_junc11__B*VV_junc11__ph)))
    VV_junc11__H_VV_out_alpha = VV_junc11__H_mean*VV_junc11__FQE_alpha/(VV_junc11__FQB_alpha+VV_junc11__div_0)
    VV_junc11__H_VV_out_beta = VV_junc11__H_mean*(1-VV_junc11__FQE_alpha)/(1-VV_junc11__FQB_alpha+VV_junc11__div_0)
    VV_junc11__H_split1 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha1 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta1 == 1 else V10__H_R_out))
    VV_junc11__H_split2 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha2 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta2 == 1 else VV_junc11__H_to2))
    VV_junc11__H_split3 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha3 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta3 == 1 else PV21__H_L_out))
    VV_junc11__H_split4 = (VV_junc11__H_VV_out_alpha if VV_junc11__alpha4 == 1 else (VV_junc11__H_VV_out_beta if VV_junc11__beta4 == 1 else PV22__H_L_out))
    VV_junc11__H_daughter1 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split1 if VV_junc11__is_split == 1 else V10__H_R_out))
    VV_junc11__H_daughter2 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split2 if VV_junc11__is_split == 1 else VV_junc11__H_to2))
    VV_junc11__H_daughter3 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split3 if VV_junc11__is_split == 1 else PV21__H_L_out))
    VV_junc11__H_daughter4 = (VV_junc11__H_mean if VV_junc11__is_merge == 1 else (VV_junc11__H_split4 if VV_junc11__is_split == 1 else PV22__H_L_out))
    VV_junc11__H_from1_target = (VV_junc11__H_daughter1 if VV_junc11__bc1_is_out == 1 else V10__H_R_out)
    VV_junc11__H_from2_target = (VV_junc11__H_daughter2 if VV_junc11__bc2_is_out == 1 else VV_junc11__H_to2)
    VV_junc11__H_from3_target = (VV_junc11__H_daughter3 if VV_junc11__bc3_is_out == 1 else PV21__H_L_out)
    VV_junc11__H_from4_target = (VV_junc11__H_daughter4 if VV_junc11__bc4_is_out == 1 else PV22__H_L_out)
    VV_junc12__FQE_alpha = 1/(1+np.exp(-(VV_junc12__A+VV_junc12__B*VV_junc12__ph)))
    VV_junc12__H_VV_out_alpha = VV_junc12__H_mean*VV_junc12__FQE_alpha/(VV_junc12__FQB_alpha+VV_junc12__div_0)
    VV_junc12__H_VV_out_beta = VV_junc12__H_mean*(1-VV_junc12__FQE_alpha)/(1-VV_junc12__FQB_alpha+VV_junc12__div_0)
    VV_junc12__H_split1 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha1 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta1 == 1 else V11__H_R_out))
    VV_junc12__H_split2 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha2 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta2 == 1 else VV_junc12__H_to2))
    VV_junc12__H_split3 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha3 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta3 == 1 else PV23__H_L_out))
    VV_junc12__H_split4 = (VV_junc12__H_VV_out_alpha if VV_junc12__alpha4 == 1 else (VV_junc12__H_VV_out_beta if VV_junc12__beta4 == 1 else PV24__H_L_out))
    VV_junc12__H_daughter1 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split1 if VV_junc12__is_split == 1 else V11__H_R_out))
    VV_junc12__H_daughter2 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split2 if VV_junc12__is_split == 1 else VV_junc12__H_to2))
    VV_junc12__H_daughter3 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split3 if VV_junc12__is_split == 1 else PV23__H_L_out))
    VV_junc12__H_daughter4 = (VV_junc12__H_mean if VV_junc12__is_merge == 1 else (VV_junc12__H_split4 if VV_junc12__is_split == 1 else PV24__H_L_out))
    VV_junc12__H_from1_target = (VV_junc12__H_daughter1 if VV_junc12__bc1_is_out == 1 else V11__H_R_out)
    VV_junc12__H_from2_target = (VV_junc12__H_daughter2 if VV_junc12__bc2_is_out == 1 else VV_junc12__H_to2)
    VV_junc12__H_from3_target = (VV_junc12__H_daughter3 if VV_junc12__bc3_is_out == 1 else PV23__H_L_out)
    VV_junc12__H_from4_target = (VV_junc12__H_daughter4 if VV_junc12__bc4_is_out == 1 else PV24__H_L_out)
    VV_junc13__FQE_alpha = 1/(1+np.exp(-(VV_junc13__A+VV_junc13__B*VV_junc13__ph)))
    VV_junc13__H_VV_out_alpha = VV_junc13__H_mean*VV_junc13__FQE_alpha/(VV_junc13__FQB_alpha+VV_junc13__div_0)
    VV_junc13__H_VV_out_beta = VV_junc13__H_mean*(1-VV_junc13__FQE_alpha)/(1-VV_junc13__FQB_alpha+VV_junc13__div_0)
    VV_junc13__H_split1 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha1 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta1 == 1 else V12__H_R_out))
    VV_junc13__H_split2 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha2 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta2 == 1 else VV_junc13__H_to2))
    VV_junc13__H_split3 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha3 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta3 == 1 else PV25__H_L_out))
    VV_junc13__H_split4 = (VV_junc13__H_VV_out_alpha if VV_junc13__alpha4 == 1 else (VV_junc13__H_VV_out_beta if VV_junc13__beta4 == 1 else PV26__H_L_out))
    VV_junc13__H_daughter1 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split1 if VV_junc13__is_split == 1 else V12__H_R_out))
    VV_junc13__H_daughter2 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split2 if VV_junc13__is_split == 1 else VV_junc13__H_to2))
    VV_junc13__H_daughter3 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split3 if VV_junc13__is_split == 1 else PV25__H_L_out))
    VV_junc13__H_daughter4 = (VV_junc13__H_mean if VV_junc13__is_merge == 1 else (VV_junc13__H_split4 if VV_junc13__is_split == 1 else PV26__H_L_out))
    VV_junc13__H_from1_target = (VV_junc13__H_daughter1 if VV_junc13__bc1_is_out == 1 else V12__H_R_out)
    VV_junc13__H_from2_target = (VV_junc13__H_daughter2 if VV_junc13__bc2_is_out == 1 else VV_junc13__H_to2)
    VV_junc13__H_from3_target = (VV_junc13__H_daughter3 if VV_junc13__bc3_is_out == 1 else PV25__H_L_out)
    VV_junc13__H_from4_target = (VV_junc13__H_daughter4 if VV_junc13__bc4_is_out == 1 else PV26__H_L_out)
    VV_junc14__FQE_alpha = 1/(1+np.exp(-(VV_junc14__A+VV_junc14__B*VV_junc14__ph)))
    VV_junc14__H_VV_out_alpha = VV_junc14__H_mean*VV_junc14__FQE_alpha/(VV_junc14__FQB_alpha+VV_junc14__div_0)
    VV_junc14__H_VV_out_beta = VV_junc14__H_mean*(1-VV_junc14__FQE_alpha)/(1-VV_junc14__FQB_alpha+VV_junc14__div_0)
    VV_junc14__H_split1 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha1 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta1 == 1 else V13__H_R_out))
    VV_junc14__H_split2 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha2 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta2 == 1 else VV_junc14__H_to2))
    VV_junc14__H_split3 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha3 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta3 == 1 else PV27__H_L_out))
    VV_junc14__H_split4 = (VV_junc14__H_VV_out_alpha if VV_junc14__alpha4 == 1 else (VV_junc14__H_VV_out_beta if VV_junc14__beta4 == 1 else PV28__H_L_out))
    VV_junc14__H_daughter1 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split1 if VV_junc14__is_split == 1 else V13__H_R_out))
    VV_junc14__H_daughter2 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split2 if VV_junc14__is_split == 1 else VV_junc14__H_to2))
    VV_junc14__H_daughter3 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split3 if VV_junc14__is_split == 1 else PV27__H_L_out))
    VV_junc14__H_daughter4 = (VV_junc14__H_mean if VV_junc14__is_merge == 1 else (VV_junc14__H_split4 if VV_junc14__is_split == 1 else PV28__H_L_out))
    VV_junc14__H_from1_target = (VV_junc14__H_daughter1 if VV_junc14__bc1_is_out == 1 else V13__H_R_out)
    VV_junc14__H_from2_target = (VV_junc14__H_daughter2 if VV_junc14__bc2_is_out == 1 else VV_junc14__H_to2)
    VV_junc14__H_from3_target = (VV_junc14__H_daughter3 if VV_junc14__bc3_is_out == 1 else PV27__H_L_out)
    VV_junc14__H_from4_target = (VV_junc14__H_daughter4 if VV_junc14__bc4_is_out == 1 else PV28__H_L_out)
    VV_junc15__FQE_alpha = 1/(1+np.exp(-(VV_junc15__A+VV_junc15__B*VV_junc15__ph)))
    VV_junc15__H_VV_out_alpha = VV_junc15__H_mean*VV_junc15__FQE_alpha/(VV_junc15__FQB_alpha+VV_junc15__div_0)
    VV_junc15__H_VV_out_beta = VV_junc15__H_mean*(1-VV_junc15__FQE_alpha)/(1-VV_junc15__FQB_alpha+VV_junc15__div_0)
    VV_junc15__H_split1 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha1 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta1 == 1 else V14__H_R_out))
    VV_junc15__H_split2 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha2 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta2 == 1 else VV_junc15__H_to2))
    VV_junc15__H_split3 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha3 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta3 == 1 else PV29__H_L_out))
    VV_junc15__H_split4 = (VV_junc15__H_VV_out_alpha if VV_junc15__alpha4 == 1 else (VV_junc15__H_VV_out_beta if VV_junc15__beta4 == 1 else PV30__H_L_out))
    VV_junc15__H_daughter1 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split1 if VV_junc15__is_split == 1 else V14__H_R_out))
    VV_junc15__H_daughter2 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split2 if VV_junc15__is_split == 1 else VV_junc15__H_to2))
    VV_junc15__H_daughter3 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split3 if VV_junc15__is_split == 1 else PV29__H_L_out))
    VV_junc15__H_daughter4 = (VV_junc15__H_mean if VV_junc15__is_merge == 1 else (VV_junc15__H_split4 if VV_junc15__is_split == 1 else PV30__H_L_out))
    VV_junc15__H_from1_target = (VV_junc15__H_daughter1 if VV_junc15__bc1_is_out == 1 else V14__H_R_out)
    VV_junc15__H_from2_target = (VV_junc15__H_daughter2 if VV_junc15__bc2_is_out == 1 else VV_junc15__H_to2)
    VV_junc15__H_from3_target = (VV_junc15__H_daughter3 if VV_junc15__bc3_is_out == 1 else PV29__H_L_out)
    VV_junc15__H_from4_target = (VV_junc15__H_daughter4 if VV_junc15__bc4_is_out == 1 else PV30__H_L_out)
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
    VV_junc8__H_from1 = VV_junc8__w_out1*VV_junc8__H_from1_target
    VV_junc8__H_from2 = VV_junc8__w_out2*VV_junc8__H_from2_target
    VV_junc8__H_from3 = VV_junc8__w_out3*VV_junc8__H_from3_target
    VV_junc8__H_from4 = VV_junc8__w_out4*VV_junc8__H_from4_target
    VV_junc8__RBC_out = VV_junc8__Qout1*VV_junc8__H_from1+VV_junc8__Qout2*VV_junc8__H_from2+VV_junc8__Qout3*VV_junc8__H_from3+VV_junc8__Qout4*VV_junc8__H_from4
    VV_junc9__H_from1 = VV_junc9__w_out1*VV_junc9__H_from1_target
    VV_junc9__H_from2 = VV_junc9__w_out2*VV_junc9__H_from2_target
    VV_junc9__H_from3 = VV_junc9__w_out3*VV_junc9__H_from3_target
    VV_junc9__H_from4 = VV_junc9__w_out4*VV_junc9__H_from4_target
    VV_junc9__RBC_out = VV_junc9__Qout1*VV_junc9__H_from1+VV_junc9__Qout2*VV_junc9__H_from2+VV_junc9__Qout3*VV_junc9__H_from3+VV_junc9__Qout4*VV_junc9__H_from4
    VV_junc10__H_from1 = VV_junc10__w_out1*VV_junc10__H_from1_target
    VV_junc10__H_from2 = VV_junc10__w_out2*VV_junc10__H_from2_target
    VV_junc10__H_from3 = VV_junc10__w_out3*VV_junc10__H_from3_target
    VV_junc10__H_from4 = VV_junc10__w_out4*VV_junc10__H_from4_target
    VV_junc10__RBC_out = VV_junc10__Qout1*VV_junc10__H_from1+VV_junc10__Qout2*VV_junc10__H_from2+VV_junc10__Qout3*VV_junc10__H_from3+VV_junc10__Qout4*VV_junc10__H_from4
    VV_junc11__H_from1 = VV_junc11__w_out1*VV_junc11__H_from1_target
    VV_junc11__H_from2 = VV_junc11__w_out2*VV_junc11__H_from2_target
    VV_junc11__H_from3 = VV_junc11__w_out3*VV_junc11__H_from3_target
    VV_junc11__H_from4 = VV_junc11__w_out4*VV_junc11__H_from4_target
    VV_junc11__RBC_out = VV_junc11__Qout1*VV_junc11__H_from1+VV_junc11__Qout2*VV_junc11__H_from2+VV_junc11__Qout3*VV_junc11__H_from3+VV_junc11__Qout4*VV_junc11__H_from4
    VV_junc12__H_from1 = VV_junc12__w_out1*VV_junc12__H_from1_target
    VV_junc12__H_from2 = VV_junc12__w_out2*VV_junc12__H_from2_target
    VV_junc12__H_from3 = VV_junc12__w_out3*VV_junc12__H_from3_target
    VV_junc12__H_from4 = VV_junc12__w_out4*VV_junc12__H_from4_target
    VV_junc12__RBC_out = VV_junc12__Qout1*VV_junc12__H_from1+VV_junc12__Qout2*VV_junc12__H_from2+VV_junc12__Qout3*VV_junc12__H_from3+VV_junc12__Qout4*VV_junc12__H_from4
    VV_junc13__H_from1 = VV_junc13__w_out1*VV_junc13__H_from1_target
    VV_junc13__H_from2 = VV_junc13__w_out2*VV_junc13__H_from2_target
    VV_junc13__H_from3 = VV_junc13__w_out3*VV_junc13__H_from3_target
    VV_junc13__H_from4 = VV_junc13__w_out4*VV_junc13__H_from4_target
    VV_junc13__RBC_out = VV_junc13__Qout1*VV_junc13__H_from1+VV_junc13__Qout2*VV_junc13__H_from2+VV_junc13__Qout3*VV_junc13__H_from3+VV_junc13__Qout4*VV_junc13__H_from4
    VV_junc14__H_from1 = VV_junc14__w_out1*VV_junc14__H_from1_target
    VV_junc14__H_from2 = VV_junc14__w_out2*VV_junc14__H_from2_target
    VV_junc14__H_from3 = VV_junc14__w_out3*VV_junc14__H_from3_target
    VV_junc14__H_from4 = VV_junc14__w_out4*VV_junc14__H_from4_target
    VV_junc14__RBC_out = VV_junc14__Qout1*VV_junc14__H_from1+VV_junc14__Qout2*VV_junc14__H_from2+VV_junc14__Qout3*VV_junc14__H_from3+VV_junc14__Qout4*VV_junc14__H_from4
    VV_junc15__H_from1 = VV_junc15__w_out1*VV_junc15__H_from1_target
    VV_junc15__H_from2 = VV_junc15__w_out2*VV_junc15__H_from2_target
    VV_junc15__H_from3 = VV_junc15__w_out3*VV_junc15__H_from3_target
    VV_junc15__H_from4 = VV_junc15__w_out4*VV_junc15__H_from4_target
    VV_junc15__RBC_out = VV_junc15__Qout1*VV_junc15__H_from1+VV_junc15__Qout2*VV_junc15__H_from2+VV_junc15__Qout3*VV_junc15__H_from3+VV_junc15__Qout4*VV_junc15__H_from4

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
        "VV_junc8__vj2": VV_junc8__vj2,
        "VV_junc8__D1": VV_junc8__D1,
        "VV_junc8__D2": VV_junc8__D2,
        "VV_junc8__D3": VV_junc8__D3,
        "VV_junc8__D4": VV_junc8__D4,
        "VV_junc8__w_in2": VV_junc8__w_in2,
        "VV_junc8__w_out2": VV_junc8__w_out2,
        "VV_junc8__Qin2": VV_junc8__Qin2,
        "VV_junc8__Qout2": VV_junc8__Qout2,
        "VV_junc8__q_us": VV_junc8__q_us,
        "VV_junc8__q": VV_junc8__q,
        "VV_junc8__bc2_is_in": VV_junc8__bc2_is_in,
        "VV_junc8__bc2_is_out": VV_junc8__bc2_is_out,
        "VV_junc8__C_max12": VV_junc8__C_max12,
        "PV15__R_constriction": PV15__R_constriction,
        "PV15__H_L_in": PV15__H_L_in,
        "PV15__H_R_in": PV15__H_R_in,
        "PV15__q_us": PV15__q_us,
        "PV15__q": PV15__q,
        "PV15__C": PV15__C,
        "PV15__Z": PV15__Z,
        "PV15__mu_45": PV15__mu_45,
        "PV15__u": PV15__u,
        "PV16__R_constriction": PV16__R_constriction,
        "PV16__H_L_in": PV16__H_L_in,
        "PV16__H_R_in": PV16__H_R_in,
        "PV16__q_us": PV16__q_us,
        "PV16__q": PV16__q,
        "PV16__C": PV16__C,
        "PV16__Z": PV16__Z,
        "PV16__mu_45": PV16__mu_45,
        "PV16__u": PV16__u,
        "V15__H_L_in": V15__H_L_in,
        "V15__H_R_in": V15__H_R_in,
        "V15__q_us": V15__q_us,
        "V15__q": V15__q,
        "V15__C": V15__C,
        "V15__Z": V15__Z,
        "V15__mu_45": V15__mu_45,
        "V15__u": V15__u,
        "V16__H_L_in": V16__H_L_in,
        "V16__H_R_in": V16__H_R_in,
        "V16__q_us": V16__q_us,
        "V16__q": V16__q,
        "V16__C": V16__C,
        "V16__Z": V16__Z,
        "V16__mu_45": V16__mu_45,
        "V16__u": V16__u,
        "VV_junc9__vj2": VV_junc9__vj2,
        "VV_junc9__D1": VV_junc9__D1,
        "VV_junc9__D2": VV_junc9__D2,
        "VV_junc9__D3": VV_junc9__D3,
        "VV_junc9__D4": VV_junc9__D4,
        "VV_junc9__w_in2": VV_junc9__w_in2,
        "VV_junc9__w_out2": VV_junc9__w_out2,
        "VV_junc9__Qin2": VV_junc9__Qin2,
        "VV_junc9__Qout2": VV_junc9__Qout2,
        "VV_junc9__q_us": VV_junc9__q_us,
        "VV_junc9__q": VV_junc9__q,
        "VV_junc9__bc2_is_in": VV_junc9__bc2_is_in,
        "VV_junc9__bc2_is_out": VV_junc9__bc2_is_out,
        "VV_junc9__C_max12": VV_junc9__C_max12,
        "PV17__R_constriction": PV17__R_constriction,
        "PV17__H_L_in": PV17__H_L_in,
        "PV17__H_R_in": PV17__H_R_in,
        "PV17__q_us": PV17__q_us,
        "PV17__q": PV17__q,
        "PV17__C": PV17__C,
        "PV17__Z": PV17__Z,
        "PV17__mu_45": PV17__mu_45,
        "PV17__u": PV17__u,
        "PV18__R_constriction": PV18__R_constriction,
        "PV18__H_L_in": PV18__H_L_in,
        "PV18__H_R_in": PV18__H_R_in,
        "PV18__q_us": PV18__q_us,
        "PV18__q": PV18__q,
        "PV18__C": PV18__C,
        "PV18__Z": PV18__Z,
        "PV18__mu_45": PV18__mu_45,
        "PV18__u": PV18__u,
        "V17__H_L_in": V17__H_L_in,
        "V17__H_R_in": V17__H_R_in,
        "V17__q_us": V17__q_us,
        "V17__q": V17__q,
        "V17__C": V17__C,
        "V17__Z": V17__Z,
        "V17__mu_45": V17__mu_45,
        "V17__u": V17__u,
        "V18__H_L_in": V18__H_L_in,
        "V18__H_R_in": V18__H_R_in,
        "V18__q_us": V18__q_us,
        "V18__q": V18__q,
        "V18__C": V18__C,
        "V18__Z": V18__Z,
        "V18__mu_45": V18__mu_45,
        "V18__u": V18__u,
        "VV_junc10__vj2": VV_junc10__vj2,
        "VV_junc10__D1": VV_junc10__D1,
        "VV_junc10__D2": VV_junc10__D2,
        "VV_junc10__D3": VV_junc10__D3,
        "VV_junc10__D4": VV_junc10__D4,
        "VV_junc10__w_in2": VV_junc10__w_in2,
        "VV_junc10__w_out2": VV_junc10__w_out2,
        "VV_junc10__Qin2": VV_junc10__Qin2,
        "VV_junc10__Qout2": VV_junc10__Qout2,
        "VV_junc10__q_us": VV_junc10__q_us,
        "VV_junc10__q": VV_junc10__q,
        "VV_junc10__bc2_is_in": VV_junc10__bc2_is_in,
        "VV_junc10__bc2_is_out": VV_junc10__bc2_is_out,
        "VV_junc10__C_max12": VV_junc10__C_max12,
        "PV19__R_constriction": PV19__R_constriction,
        "PV19__H_L_in": PV19__H_L_in,
        "PV19__H_R_in": PV19__H_R_in,
        "PV19__q_us": PV19__q_us,
        "PV19__q": PV19__q,
        "PV19__C": PV19__C,
        "PV19__Z": PV19__Z,
        "PV19__mu_45": PV19__mu_45,
        "PV19__u": PV19__u,
        "PV20__R_constriction": PV20__R_constriction,
        "PV20__H_L_in": PV20__H_L_in,
        "PV20__H_R_in": PV20__H_R_in,
        "PV20__q_us": PV20__q_us,
        "PV20__q": PV20__q,
        "PV20__C": PV20__C,
        "PV20__Z": PV20__Z,
        "PV20__mu_45": PV20__mu_45,
        "PV20__u": PV20__u,
        "V19__H_L_in": V19__H_L_in,
        "V19__H_R_in": V19__H_R_in,
        "V19__q_us": V19__q_us,
        "V19__q": V19__q,
        "V19__C": V19__C,
        "V19__Z": V19__Z,
        "V19__mu_45": V19__mu_45,
        "V19__u": V19__u,
        "V20__H_L_in": V20__H_L_in,
        "V20__H_R_in": V20__H_R_in,
        "V20__q_us": V20__q_us,
        "V20__q": V20__q,
        "V20__C": V20__C,
        "V20__Z": V20__Z,
        "V20__mu_45": V20__mu_45,
        "V20__u": V20__u,
        "VV_junc11__vj2": VV_junc11__vj2,
        "VV_junc11__D1": VV_junc11__D1,
        "VV_junc11__D2": VV_junc11__D2,
        "VV_junc11__D3": VV_junc11__D3,
        "VV_junc11__D4": VV_junc11__D4,
        "VV_junc11__w_in2": VV_junc11__w_in2,
        "VV_junc11__w_out2": VV_junc11__w_out2,
        "VV_junc11__Qin2": VV_junc11__Qin2,
        "VV_junc11__Qout2": VV_junc11__Qout2,
        "VV_junc11__q_us": VV_junc11__q_us,
        "VV_junc11__q": VV_junc11__q,
        "VV_junc11__bc2_is_in": VV_junc11__bc2_is_in,
        "VV_junc11__bc2_is_out": VV_junc11__bc2_is_out,
        "VV_junc11__C_max12": VV_junc11__C_max12,
        "PV21__R_constriction": PV21__R_constriction,
        "PV21__H_L_in": PV21__H_L_in,
        "PV21__H_R_in": PV21__H_R_in,
        "PV21__q_us": PV21__q_us,
        "PV21__q": PV21__q,
        "PV21__C": PV21__C,
        "PV21__Z": PV21__Z,
        "PV21__mu_45": PV21__mu_45,
        "PV21__u": PV21__u,
        "PV22__R_constriction": PV22__R_constriction,
        "PV22__H_L_in": PV22__H_L_in,
        "PV22__H_R_in": PV22__H_R_in,
        "PV22__q_us": PV22__q_us,
        "PV22__q": PV22__q,
        "PV22__C": PV22__C,
        "PV22__Z": PV22__Z,
        "PV22__mu_45": PV22__mu_45,
        "PV22__u": PV22__u,
        "V21__H_L_in": V21__H_L_in,
        "V21__H_R_in": V21__H_R_in,
        "V21__q_us": V21__q_us,
        "V21__q": V21__q,
        "V21__C": V21__C,
        "V21__Z": V21__Z,
        "V21__mu_45": V21__mu_45,
        "V21__u": V21__u,
        "V22__H_L_in": V22__H_L_in,
        "V22__H_R_in": V22__H_R_in,
        "V22__q_us": V22__q_us,
        "V22__q": V22__q,
        "V22__C": V22__C,
        "V22__Z": V22__Z,
        "V22__mu_45": V22__mu_45,
        "V22__u": V22__u,
        "VV_junc12__vj2": VV_junc12__vj2,
        "VV_junc12__D1": VV_junc12__D1,
        "VV_junc12__D2": VV_junc12__D2,
        "VV_junc12__D3": VV_junc12__D3,
        "VV_junc12__D4": VV_junc12__D4,
        "VV_junc12__w_in2": VV_junc12__w_in2,
        "VV_junc12__w_out2": VV_junc12__w_out2,
        "VV_junc12__Qin2": VV_junc12__Qin2,
        "VV_junc12__Qout2": VV_junc12__Qout2,
        "VV_junc12__q_us": VV_junc12__q_us,
        "VV_junc12__q": VV_junc12__q,
        "VV_junc12__bc2_is_in": VV_junc12__bc2_is_in,
        "VV_junc12__bc2_is_out": VV_junc12__bc2_is_out,
        "VV_junc12__C_max12": VV_junc12__C_max12,
        "PV23__R_constriction": PV23__R_constriction,
        "PV23__H_L_in": PV23__H_L_in,
        "PV23__H_R_in": PV23__H_R_in,
        "PV23__q_us": PV23__q_us,
        "PV23__q": PV23__q,
        "PV23__C": PV23__C,
        "PV23__Z": PV23__Z,
        "PV23__mu_45": PV23__mu_45,
        "PV23__u": PV23__u,
        "PV24__R_constriction": PV24__R_constriction,
        "PV24__H_L_in": PV24__H_L_in,
        "PV24__H_R_in": PV24__H_R_in,
        "PV24__q_us": PV24__q_us,
        "PV24__q": PV24__q,
        "PV24__C": PV24__C,
        "PV24__Z": PV24__Z,
        "PV24__mu_45": PV24__mu_45,
        "PV24__u": PV24__u,
        "V23__H_L_in": V23__H_L_in,
        "V23__H_R_in": V23__H_R_in,
        "V23__q_us": V23__q_us,
        "V23__q": V23__q,
        "V23__C": V23__C,
        "V23__Z": V23__Z,
        "V23__mu_45": V23__mu_45,
        "V23__u": V23__u,
        "V24__H_L_in": V24__H_L_in,
        "V24__H_R_in": V24__H_R_in,
        "V24__q_us": V24__q_us,
        "V24__q": V24__q,
        "V24__C": V24__C,
        "V24__Z": V24__Z,
        "V24__mu_45": V24__mu_45,
        "V24__u": V24__u,
        "VV_junc13__vj2": VV_junc13__vj2,
        "VV_junc13__D1": VV_junc13__D1,
        "VV_junc13__D2": VV_junc13__D2,
        "VV_junc13__D3": VV_junc13__D3,
        "VV_junc13__D4": VV_junc13__D4,
        "VV_junc13__w_in2": VV_junc13__w_in2,
        "VV_junc13__w_out2": VV_junc13__w_out2,
        "VV_junc13__Qin2": VV_junc13__Qin2,
        "VV_junc13__Qout2": VV_junc13__Qout2,
        "VV_junc13__q_us": VV_junc13__q_us,
        "VV_junc13__q": VV_junc13__q,
        "VV_junc13__bc2_is_in": VV_junc13__bc2_is_in,
        "VV_junc13__bc2_is_out": VV_junc13__bc2_is_out,
        "VV_junc13__C_max12": VV_junc13__C_max12,
        "PV25__R_constriction": PV25__R_constriction,
        "PV25__H_L_in": PV25__H_L_in,
        "PV25__H_R_in": PV25__H_R_in,
        "PV25__q_us": PV25__q_us,
        "PV25__q": PV25__q,
        "PV25__C": PV25__C,
        "PV25__Z": PV25__Z,
        "PV25__mu_45": PV25__mu_45,
        "PV25__u": PV25__u,
        "PV26__R_constriction": PV26__R_constriction,
        "PV26__H_L_in": PV26__H_L_in,
        "PV26__H_R_in": PV26__H_R_in,
        "PV26__q_us": PV26__q_us,
        "PV26__q": PV26__q,
        "PV26__C": PV26__C,
        "PV26__Z": PV26__Z,
        "PV26__mu_45": PV26__mu_45,
        "PV26__u": PV26__u,
        "V25__H_L_in": V25__H_L_in,
        "V25__H_R_in": V25__H_R_in,
        "V25__q_us": V25__q_us,
        "V25__q": V25__q,
        "V25__C": V25__C,
        "V25__Z": V25__Z,
        "V25__mu_45": V25__mu_45,
        "V25__u": V25__u,
        "V26__H_L_in": V26__H_L_in,
        "V26__H_R_in": V26__H_R_in,
        "V26__q_us": V26__q_us,
        "V26__q": V26__q,
        "V26__C": V26__C,
        "V26__Z": V26__Z,
        "V26__mu_45": V26__mu_45,
        "V26__u": V26__u,
        "VV_junc14__vj2": VV_junc14__vj2,
        "VV_junc14__D1": VV_junc14__D1,
        "VV_junc14__D2": VV_junc14__D2,
        "VV_junc14__D3": VV_junc14__D3,
        "VV_junc14__D4": VV_junc14__D4,
        "VV_junc14__w_in2": VV_junc14__w_in2,
        "VV_junc14__w_out2": VV_junc14__w_out2,
        "VV_junc14__Qin2": VV_junc14__Qin2,
        "VV_junc14__Qout2": VV_junc14__Qout2,
        "VV_junc14__q_us": VV_junc14__q_us,
        "VV_junc14__q": VV_junc14__q,
        "VV_junc14__bc2_is_in": VV_junc14__bc2_is_in,
        "VV_junc14__bc2_is_out": VV_junc14__bc2_is_out,
        "VV_junc14__C_max12": VV_junc14__C_max12,
        "PV27__R_constriction": PV27__R_constriction,
        "PV27__H_L_in": PV27__H_L_in,
        "PV27__H_R_in": PV27__H_R_in,
        "PV27__q_us": PV27__q_us,
        "PV27__q": PV27__q,
        "PV27__C": PV27__C,
        "PV27__Z": PV27__Z,
        "PV27__mu_45": PV27__mu_45,
        "PV27__u": PV27__u,
        "PV28__R_constriction": PV28__R_constriction,
        "PV28__H_L_in": PV28__H_L_in,
        "PV28__H_R_in": PV28__H_R_in,
        "PV28__q_us": PV28__q_us,
        "PV28__q": PV28__q,
        "PV28__C": PV28__C,
        "PV28__Z": PV28__Z,
        "PV28__mu_45": PV28__mu_45,
        "PV28__u": PV28__u,
        "V27__H_L_in": V27__H_L_in,
        "V27__H_R_in": V27__H_R_in,
        "V27__q_us": V27__q_us,
        "V27__q": V27__q,
        "V27__C": V27__C,
        "V27__Z": V27__Z,
        "V27__mu_45": V27__mu_45,
        "V27__u": V27__u,
        "V28__H_L_in": V28__H_L_in,
        "V28__H_R_in": V28__H_R_in,
        "V28__q_us": V28__q_us,
        "V28__q": V28__q,
        "V28__C": V28__C,
        "V28__Z": V28__Z,
        "V28__mu_45": V28__mu_45,
        "V28__u": V28__u,
        "VV_junc15__vj2": VV_junc15__vj2,
        "VV_junc15__D1": VV_junc15__D1,
        "VV_junc15__D2": VV_junc15__D2,
        "VV_junc15__D3": VV_junc15__D3,
        "VV_junc15__D4": VV_junc15__D4,
        "VV_junc15__w_in2": VV_junc15__w_in2,
        "VV_junc15__w_out2": VV_junc15__w_out2,
        "VV_junc15__Qin2": VV_junc15__Qin2,
        "VV_junc15__Qout2": VV_junc15__Qout2,
        "VV_junc15__q_us": VV_junc15__q_us,
        "VV_junc15__q": VV_junc15__q,
        "VV_junc15__bc2_is_in": VV_junc15__bc2_is_in,
        "VV_junc15__bc2_is_out": VV_junc15__bc2_is_out,
        "VV_junc15__C_max12": VV_junc15__C_max12,
        "PV29__R_constriction": PV29__R_constriction,
        "PV29__H_L_in": PV29__H_L_in,
        "PV29__H_R_in": PV29__H_R_in,
        "PV29__q_us": PV29__q_us,
        "PV29__q": PV29__q,
        "PV29__C": PV29__C,
        "PV29__Z": PV29__Z,
        "PV29__mu_45": PV29__mu_45,
        "PV29__u": PV29__u,
        "PV30__R_constriction": PV30__R_constriction,
        "PV30__H_L_in": PV30__H_L_in,
        "PV30__H_R_in": PV30__H_R_in,
        "PV30__q_us": PV30__q_us,
        "PV30__q": PV30__q,
        "PV30__C": PV30__C,
        "PV30__Z": PV30__Z,
        "PV30__mu_45": PV30__mu_45,
        "PV30__u": PV30__u,
        "V29__H_L_in": V29__H_L_in,
        "V29__H_R_in": V29__H_R_in,
        "V29__q_us": V29__q_us,
        "V29__q": V29__q,
        "V29__C": V29__C,
        "V29__Z": V29__Z,
        "V29__mu_45": V29__mu_45,
        "V29__u": V29__u,
        "V30__H_L_in": V30__H_L_in,
        "V30__H_R_in": V30__H_R_in,
        "V30__q_us": V30__q_us,
        "V30__q": V30__q,
        "V30__C": V30__C,
        "V30__Z": V30__Z,
        "V30__mu_45": V30__mu_45,
        "V30__u": V30__u,
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
        "VV_junc8__RBC_volume_init": VV_junc8__RBC_volume_init,
        "VV_junc8__H_mean": VV_junc8__H_mean,
        "VV_junc8__C_max123": VV_junc8__C_max123,
        "VV_junc8__C": VV_junc8__C,
        "PV15__RBC_volume_init": PV15__RBC_volume_init,
        "PV15__H_mean": PV15__H_mean,
        "PV15__hem_dep_u_rel": PV15__hem_dep_u_rel,
        "PV15__u_mmHg": PV15__u_mmHg,
        "PV16__RBC_volume_init": PV16__RBC_volume_init,
        "PV16__H_mean": PV16__H_mean,
        "PV16__hem_dep_u_rel": PV16__hem_dep_u_rel,
        "PV16__u_mmHg": PV16__u_mmHg,
        "V15__RBC_volume_init": V15__RBC_volume_init,
        "V15__H_mean": V15__H_mean,
        "V15__hem_dep_u_rel": V15__hem_dep_u_rel,
        "V15__u_mmHg": V15__u_mmHg,
        "V16__RBC_volume_init": V16__RBC_volume_init,
        "V16__H_mean": V16__H_mean,
        "V16__hem_dep_u_rel": V16__hem_dep_u_rel,
        "V16__u_mmHg": V16__u_mmHg,
        "VV_junc9__RBC_volume_init": VV_junc9__RBC_volume_init,
        "VV_junc9__H_mean": VV_junc9__H_mean,
        "VV_junc9__C_max123": VV_junc9__C_max123,
        "VV_junc9__C": VV_junc9__C,
        "PV17__RBC_volume_init": PV17__RBC_volume_init,
        "PV17__H_mean": PV17__H_mean,
        "PV17__hem_dep_u_rel": PV17__hem_dep_u_rel,
        "PV17__u_mmHg": PV17__u_mmHg,
        "PV18__RBC_volume_init": PV18__RBC_volume_init,
        "PV18__H_mean": PV18__H_mean,
        "PV18__hem_dep_u_rel": PV18__hem_dep_u_rel,
        "PV18__u_mmHg": PV18__u_mmHg,
        "V17__RBC_volume_init": V17__RBC_volume_init,
        "V17__H_mean": V17__H_mean,
        "V17__hem_dep_u_rel": V17__hem_dep_u_rel,
        "V17__u_mmHg": V17__u_mmHg,
        "V18__RBC_volume_init": V18__RBC_volume_init,
        "V18__H_mean": V18__H_mean,
        "V18__hem_dep_u_rel": V18__hem_dep_u_rel,
        "V18__u_mmHg": V18__u_mmHg,
        "VV_junc10__RBC_volume_init": VV_junc10__RBC_volume_init,
        "VV_junc10__H_mean": VV_junc10__H_mean,
        "VV_junc10__C_max123": VV_junc10__C_max123,
        "VV_junc10__C": VV_junc10__C,
        "PV19__RBC_volume_init": PV19__RBC_volume_init,
        "PV19__H_mean": PV19__H_mean,
        "PV19__hem_dep_u_rel": PV19__hem_dep_u_rel,
        "PV19__u_mmHg": PV19__u_mmHg,
        "PV20__RBC_volume_init": PV20__RBC_volume_init,
        "PV20__H_mean": PV20__H_mean,
        "PV20__hem_dep_u_rel": PV20__hem_dep_u_rel,
        "PV20__u_mmHg": PV20__u_mmHg,
        "V19__RBC_volume_init": V19__RBC_volume_init,
        "V19__H_mean": V19__H_mean,
        "V19__hem_dep_u_rel": V19__hem_dep_u_rel,
        "V19__u_mmHg": V19__u_mmHg,
        "V20__RBC_volume_init": V20__RBC_volume_init,
        "V20__H_mean": V20__H_mean,
        "V20__hem_dep_u_rel": V20__hem_dep_u_rel,
        "V20__u_mmHg": V20__u_mmHg,
        "VV_junc11__RBC_volume_init": VV_junc11__RBC_volume_init,
        "VV_junc11__H_mean": VV_junc11__H_mean,
        "VV_junc11__C_max123": VV_junc11__C_max123,
        "VV_junc11__C": VV_junc11__C,
        "PV21__RBC_volume_init": PV21__RBC_volume_init,
        "PV21__H_mean": PV21__H_mean,
        "PV21__hem_dep_u_rel": PV21__hem_dep_u_rel,
        "PV21__u_mmHg": PV21__u_mmHg,
        "PV22__RBC_volume_init": PV22__RBC_volume_init,
        "PV22__H_mean": PV22__H_mean,
        "PV22__hem_dep_u_rel": PV22__hem_dep_u_rel,
        "PV22__u_mmHg": PV22__u_mmHg,
        "V21__RBC_volume_init": V21__RBC_volume_init,
        "V21__H_mean": V21__H_mean,
        "V21__hem_dep_u_rel": V21__hem_dep_u_rel,
        "V21__u_mmHg": V21__u_mmHg,
        "V22__RBC_volume_init": V22__RBC_volume_init,
        "V22__H_mean": V22__H_mean,
        "V22__hem_dep_u_rel": V22__hem_dep_u_rel,
        "V22__u_mmHg": V22__u_mmHg,
        "VV_junc12__RBC_volume_init": VV_junc12__RBC_volume_init,
        "VV_junc12__H_mean": VV_junc12__H_mean,
        "VV_junc12__C_max123": VV_junc12__C_max123,
        "VV_junc12__C": VV_junc12__C,
        "PV23__RBC_volume_init": PV23__RBC_volume_init,
        "PV23__H_mean": PV23__H_mean,
        "PV23__hem_dep_u_rel": PV23__hem_dep_u_rel,
        "PV23__u_mmHg": PV23__u_mmHg,
        "PV24__RBC_volume_init": PV24__RBC_volume_init,
        "PV24__H_mean": PV24__H_mean,
        "PV24__hem_dep_u_rel": PV24__hem_dep_u_rel,
        "PV24__u_mmHg": PV24__u_mmHg,
        "V23__RBC_volume_init": V23__RBC_volume_init,
        "V23__H_mean": V23__H_mean,
        "V23__hem_dep_u_rel": V23__hem_dep_u_rel,
        "V23__u_mmHg": V23__u_mmHg,
        "V24__RBC_volume_init": V24__RBC_volume_init,
        "V24__H_mean": V24__H_mean,
        "V24__hem_dep_u_rel": V24__hem_dep_u_rel,
        "V24__u_mmHg": V24__u_mmHg,
        "VV_junc13__RBC_volume_init": VV_junc13__RBC_volume_init,
        "VV_junc13__H_mean": VV_junc13__H_mean,
        "VV_junc13__C_max123": VV_junc13__C_max123,
        "VV_junc13__C": VV_junc13__C,
        "PV25__RBC_volume_init": PV25__RBC_volume_init,
        "PV25__H_mean": PV25__H_mean,
        "PV25__hem_dep_u_rel": PV25__hem_dep_u_rel,
        "PV25__u_mmHg": PV25__u_mmHg,
        "PV26__RBC_volume_init": PV26__RBC_volume_init,
        "PV26__H_mean": PV26__H_mean,
        "PV26__hem_dep_u_rel": PV26__hem_dep_u_rel,
        "PV26__u_mmHg": PV26__u_mmHg,
        "V25__RBC_volume_init": V25__RBC_volume_init,
        "V25__H_mean": V25__H_mean,
        "V25__hem_dep_u_rel": V25__hem_dep_u_rel,
        "V25__u_mmHg": V25__u_mmHg,
        "V26__RBC_volume_init": V26__RBC_volume_init,
        "V26__H_mean": V26__H_mean,
        "V26__hem_dep_u_rel": V26__hem_dep_u_rel,
        "V26__u_mmHg": V26__u_mmHg,
        "VV_junc14__RBC_volume_init": VV_junc14__RBC_volume_init,
        "VV_junc14__H_mean": VV_junc14__H_mean,
        "VV_junc14__C_max123": VV_junc14__C_max123,
        "VV_junc14__C": VV_junc14__C,
        "PV27__RBC_volume_init": PV27__RBC_volume_init,
        "PV27__H_mean": PV27__H_mean,
        "PV27__hem_dep_u_rel": PV27__hem_dep_u_rel,
        "PV27__u_mmHg": PV27__u_mmHg,
        "PV28__RBC_volume_init": PV28__RBC_volume_init,
        "PV28__H_mean": PV28__H_mean,
        "PV28__hem_dep_u_rel": PV28__hem_dep_u_rel,
        "PV28__u_mmHg": PV28__u_mmHg,
        "V27__RBC_volume_init": V27__RBC_volume_init,
        "V27__H_mean": V27__H_mean,
        "V27__hem_dep_u_rel": V27__hem_dep_u_rel,
        "V27__u_mmHg": V27__u_mmHg,
        "V28__RBC_volume_init": V28__RBC_volume_init,
        "V28__H_mean": V28__H_mean,
        "V28__hem_dep_u_rel": V28__hem_dep_u_rel,
        "V28__u_mmHg": V28__u_mmHg,
        "VV_junc15__RBC_volume_init": VV_junc15__RBC_volume_init,
        "VV_junc15__H_mean": VV_junc15__H_mean,
        "VV_junc15__C_max123": VV_junc15__C_max123,
        "VV_junc15__C": VV_junc15__C,
        "PV29__RBC_volume_init": PV29__RBC_volume_init,
        "PV29__H_mean": PV29__H_mean,
        "PV29__hem_dep_u_rel": PV29__hem_dep_u_rel,
        "PV29__u_mmHg": PV29__u_mmHg,
        "PV30__RBC_volume_init": PV30__RBC_volume_init,
        "PV30__H_mean": PV30__H_mean,
        "PV30__hem_dep_u_rel": PV30__hem_dep_u_rel,
        "PV30__u_mmHg": PV30__u_mmHg,
        "V29__RBC_volume_init": V29__RBC_volume_init,
        "V29__H_mean": V29__H_mean,
        "V29__hem_dep_u_rel": V29__hem_dep_u_rel,
        "V29__u_mmHg": V29__u_mmHg,
        "V30__RBC_volume_init": V30__RBC_volume_init,
        "V30__H_mean": V30__H_mean,
        "V30__hem_dep_u_rel": V30__hem_dep_u_rel,
        "V30__u_mmHg": V30__u_mmHg,
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
        "V8__mu": V8__mu,
        "V8__R": V8__R,
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
        "V10__mu": V10__mu,
        "V10__R": V10__R,
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
        "V12__mu": V12__mu,
        "V12__R": V12__R,
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
        "V14__mu": V14__mu,
        "V14__R": V14__R,
        "VV_junc8__u": VV_junc8__u,
        "VV_junc8__u_mmHg": VV_junc8__u_mmHg,
        "VV_junc8__u_d": VV_junc8__u_d,
        "VV_junc8__u_d_mmHg": VV_junc8__u_d_mmHg,
        "PV15__mu": PV15__mu,
        "PV15__R": PV15__R,
        "PV15__v": PV15__v,
        "PV15__v_d": PV15__v_d,
        "PV16__mu": PV16__mu,
        "PV16__R": PV16__R,
        "PV16__v": PV16__v,
        "PV16__v_d": PV16__v_d,
        "V15__mu": V15__mu,
        "V15__R": V15__R,
        "V15__v": V15__v,
        "V16__mu": V16__mu,
        "V16__R": V16__R,
        "V16__v": V16__v,
        "VV_junc9__u": VV_junc9__u,
        "VV_junc9__u_mmHg": VV_junc9__u_mmHg,
        "VV_junc9__u_d": VV_junc9__u_d,
        "VV_junc9__u_d_mmHg": VV_junc9__u_d_mmHg,
        "PV17__mu": PV17__mu,
        "PV17__R": PV17__R,
        "PV17__v": PV17__v,
        "PV17__v_d": PV17__v_d,
        "PV18__mu": PV18__mu,
        "PV18__R": PV18__R,
        "PV18__v": PV18__v,
        "PV18__v_d": PV18__v_d,
        "V17__mu": V17__mu,
        "V17__R": V17__R,
        "V17__v": V17__v,
        "V18__mu": V18__mu,
        "V18__R": V18__R,
        "V18__v": V18__v,
        "VV_junc10__u": VV_junc10__u,
        "VV_junc10__u_mmHg": VV_junc10__u_mmHg,
        "VV_junc10__u_d": VV_junc10__u_d,
        "VV_junc10__u_d_mmHg": VV_junc10__u_d_mmHg,
        "PV19__mu": PV19__mu,
        "PV19__R": PV19__R,
        "PV19__v": PV19__v,
        "PV19__v_d": PV19__v_d,
        "PV20__mu": PV20__mu,
        "PV20__R": PV20__R,
        "PV20__v": PV20__v,
        "PV20__v_d": PV20__v_d,
        "V19__mu": V19__mu,
        "V19__R": V19__R,
        "V19__v": V19__v,
        "V20__mu": V20__mu,
        "V20__R": V20__R,
        "V20__v": V20__v,
        "VV_junc11__u": VV_junc11__u,
        "VV_junc11__u_mmHg": VV_junc11__u_mmHg,
        "VV_junc11__u_d": VV_junc11__u_d,
        "VV_junc11__u_d_mmHg": VV_junc11__u_d_mmHg,
        "PV21__mu": PV21__mu,
        "PV21__R": PV21__R,
        "PV21__v": PV21__v,
        "PV21__v_d": PV21__v_d,
        "PV22__mu": PV22__mu,
        "PV22__R": PV22__R,
        "PV22__v": PV22__v,
        "PV22__v_d": PV22__v_d,
        "V21__mu": V21__mu,
        "V21__R": V21__R,
        "V21__v": V21__v,
        "V22__mu": V22__mu,
        "V22__R": V22__R,
        "V22__v": V22__v,
        "VV_junc12__u": VV_junc12__u,
        "VV_junc12__u_mmHg": VV_junc12__u_mmHg,
        "VV_junc12__u_d": VV_junc12__u_d,
        "VV_junc12__u_d_mmHg": VV_junc12__u_d_mmHg,
        "PV23__mu": PV23__mu,
        "PV23__R": PV23__R,
        "PV23__v": PV23__v,
        "PV23__v_d": PV23__v_d,
        "PV24__mu": PV24__mu,
        "PV24__R": PV24__R,
        "PV24__v": PV24__v,
        "PV24__v_d": PV24__v_d,
        "V23__mu": V23__mu,
        "V23__R": V23__R,
        "V23__v": V23__v,
        "V24__mu": V24__mu,
        "V24__R": V24__R,
        "V24__v": V24__v,
        "VV_junc13__u": VV_junc13__u,
        "VV_junc13__u_mmHg": VV_junc13__u_mmHg,
        "VV_junc13__u_d": VV_junc13__u_d,
        "VV_junc13__u_d_mmHg": VV_junc13__u_d_mmHg,
        "PV25__mu": PV25__mu,
        "PV25__R": PV25__R,
        "PV25__v": PV25__v,
        "PV25__v_d": PV25__v_d,
        "PV26__mu": PV26__mu,
        "PV26__R": PV26__R,
        "PV26__v": PV26__v,
        "PV26__v_d": PV26__v_d,
        "V25__mu": V25__mu,
        "V25__R": V25__R,
        "V25__v": V25__v,
        "V26__mu": V26__mu,
        "V26__R": V26__R,
        "V26__v": V26__v,
        "VV_junc14__u": VV_junc14__u,
        "VV_junc14__u_mmHg": VV_junc14__u_mmHg,
        "VV_junc14__u_d": VV_junc14__u_d,
        "VV_junc14__u_d_mmHg": VV_junc14__u_d_mmHg,
        "PV27__mu": PV27__mu,
        "PV27__R": PV27__R,
        "PV27__v": PV27__v,
        "PV27__v_d": PV27__v_d,
        "PV28__mu": PV28__mu,
        "PV28__R": PV28__R,
        "PV28__v": PV28__v,
        "PV28__v_d": PV28__v_d,
        "V27__mu": V27__mu,
        "V27__R": V27__R,
        "V27__v": V27__v,
        "V28__mu": V28__mu,
        "V28__R": V28__R,
        "V28__v": V28__v,
        "VV_junc15__u": VV_junc15__u,
        "VV_junc15__u_mmHg": VV_junc15__u_mmHg,
        "VV_junc15__u_d": VV_junc15__u_d,
        "VV_junc15__u_d_mmHg": VV_junc15__u_d_mmHg,
        "PV29__mu": PV29__mu,
        "PV29__R": PV29__R,
        "PV29__v": PV29__v,
        "PV29__v_d": PV29__v_d,
        "PV30__mu": PV30__mu,
        "PV30__R": PV30__R,
        "PV30__v": PV30__v,
        "PV30__v_d": PV30__v_d,
        "V29__mu": V29__mu,
        "V29__R": V29__R,
        "V29__v": V29__v,
        "V30__mu": V30__mu,
        "V30__R": V30__R,
        "V30__v": V30__v,
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
        "V7__v": V7__v,
        "V8__v": V8__v,
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
        "V9__v": V9__v,
        "V10__v": V10__v,
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
        "V11__v": V11__v,
        "V12__v": V12__v,
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
        "V13__v": V13__v,
        "V14__v": V14__v,
        "VV_junc8__vj1": VV_junc8__vj1,
        "VV_junc8__vj3": VV_junc8__vj3,
        "VV_junc8__vj4": VV_junc8__vj4,
        "VV_junc8__w_in1": VV_junc8__w_in1,
        "VV_junc8__w_in3": VV_junc8__w_in3,
        "VV_junc8__w_in4": VV_junc8__w_in4,
        "VV_junc8__w_out1": VV_junc8__w_out1,
        "VV_junc8__w_out3": VV_junc8__w_out3,
        "VV_junc8__w_out4": VV_junc8__w_out4,
        "VV_junc8__Qin1": VV_junc8__Qin1,
        "VV_junc8__Qin3": VV_junc8__Qin3,
        "VV_junc8__Qin4": VV_junc8__Qin4,
        "VV_junc8__Qout1": VV_junc8__Qout1,
        "VV_junc8__Qout3": VV_junc8__Qout3,
        "VV_junc8__Qout4": VV_junc8__Qout4,
        "VV_junc8__Qin_tot": VV_junc8__Qin_tot,
        "VV_junc8__Qout_tot": VV_junc8__Qout_tot,
        "VV_junc8__v": VV_junc8__v,
        "VV_junc8__bc1_is_in": VV_junc8__bc1_is_in,
        "VV_junc8__bc3_is_in": VV_junc8__bc3_is_in,
        "VV_junc8__bc4_is_in": VV_junc8__bc4_is_in,
        "VV_junc8__bc1_is_out": VV_junc8__bc1_is_out,
        "VV_junc8__bc3_is_out": VV_junc8__bc3_is_out,
        "VV_junc8__bc4_is_out": VV_junc8__bc4_is_out,
        "PV15__w_v": PV15__w_v,
        "PV15__w_v_d": PV15__w_v_d,
        "PV15__H_up": PV15__H_up,
        "PV15__s_v_d": PV15__s_v_d,
        "PV15__H_L_out": PV15__H_L_out,
        "PV15__H_R_out": PV15__H_R_out,
        "PV15__v_pos": PV15__v_pos,
        "PV15__v_neg": PV15__v_neg,
        "PV15__v_d_pos": PV15__v_d_pos,
        "PV15__v_d_neg": PV15__v_d_neg,
        "PV15__H_volume_L": PV15__H_volume_L,
        "PV15__H_volume_R": PV15__H_volume_R,
        "PV15__v_mm3_s": PV15__v_mm3_s,
        "PV15__v_d_mm3_s": PV15__v_d_mm3_s,
        "PV16__w_v": PV16__w_v,
        "PV16__w_v_d": PV16__w_v_d,
        "PV16__H_up": PV16__H_up,
        "PV16__s_v_d": PV16__s_v_d,
        "PV16__H_L_out": PV16__H_L_out,
        "PV16__H_R_out": PV16__H_R_out,
        "PV16__v_pos": PV16__v_pos,
        "PV16__v_neg": PV16__v_neg,
        "PV16__v_d_pos": PV16__v_d_pos,
        "PV16__v_d_neg": PV16__v_d_neg,
        "PV16__H_volume_L": PV16__H_volume_L,
        "PV16__H_volume_R": PV16__H_volume_R,
        "PV16__v_mm3_s": PV16__v_mm3_s,
        "PV16__v_d_mm3_s": PV16__v_d_mm3_s,
        "V15__w_v": V15__w_v,
        "V15__H_up": V15__H_up,
        "V15__s_v": V15__s_v,
        "V15__H_L_out": V15__H_L_out,
        "V15__H_R_out": V15__H_R_out,
        "V15__v_pos": V15__v_pos,
        "V15__v_neg": V15__v_neg,
        "V15__H_volume_L": V15__H_volume_L,
        "V15__H_volume_R": V15__H_volume_R,
        "V15__v_mm3_s": V15__v_mm3_s,
        "V16__w_v": V16__w_v,
        "V16__H_up": V16__H_up,
        "V16__s_v": V16__s_v,
        "V16__H_L_out": V16__H_L_out,
        "V16__H_R_out": V16__H_R_out,
        "V16__v_pos": V16__v_pos,
        "V16__v_neg": V16__v_neg,
        "V16__H_volume_L": V16__H_volume_L,
        "V16__H_volume_R": V16__H_volume_R,
        "V16__v_mm3_s": V16__v_mm3_s,
        "VV_junc9__vj1": VV_junc9__vj1,
        "VV_junc9__vj3": VV_junc9__vj3,
        "VV_junc9__vj4": VV_junc9__vj4,
        "VV_junc9__w_in1": VV_junc9__w_in1,
        "VV_junc9__w_in3": VV_junc9__w_in3,
        "VV_junc9__w_in4": VV_junc9__w_in4,
        "VV_junc9__w_out1": VV_junc9__w_out1,
        "VV_junc9__w_out3": VV_junc9__w_out3,
        "VV_junc9__w_out4": VV_junc9__w_out4,
        "VV_junc9__Qin1": VV_junc9__Qin1,
        "VV_junc9__Qin3": VV_junc9__Qin3,
        "VV_junc9__Qin4": VV_junc9__Qin4,
        "VV_junc9__Qout1": VV_junc9__Qout1,
        "VV_junc9__Qout3": VV_junc9__Qout3,
        "VV_junc9__Qout4": VV_junc9__Qout4,
        "VV_junc9__Qin_tot": VV_junc9__Qin_tot,
        "VV_junc9__Qout_tot": VV_junc9__Qout_tot,
        "VV_junc9__v": VV_junc9__v,
        "VV_junc9__bc1_is_in": VV_junc9__bc1_is_in,
        "VV_junc9__bc3_is_in": VV_junc9__bc3_is_in,
        "VV_junc9__bc4_is_in": VV_junc9__bc4_is_in,
        "VV_junc9__bc1_is_out": VV_junc9__bc1_is_out,
        "VV_junc9__bc3_is_out": VV_junc9__bc3_is_out,
        "VV_junc9__bc4_is_out": VV_junc9__bc4_is_out,
        "PV17__w_v": PV17__w_v,
        "PV17__w_v_d": PV17__w_v_d,
        "PV17__H_up": PV17__H_up,
        "PV17__s_v_d": PV17__s_v_d,
        "PV17__H_L_out": PV17__H_L_out,
        "PV17__H_R_out": PV17__H_R_out,
        "PV17__v_pos": PV17__v_pos,
        "PV17__v_neg": PV17__v_neg,
        "PV17__v_d_pos": PV17__v_d_pos,
        "PV17__v_d_neg": PV17__v_d_neg,
        "PV17__H_volume_L": PV17__H_volume_L,
        "PV17__H_volume_R": PV17__H_volume_R,
        "PV17__v_mm3_s": PV17__v_mm3_s,
        "PV17__v_d_mm3_s": PV17__v_d_mm3_s,
        "PV18__w_v": PV18__w_v,
        "PV18__w_v_d": PV18__w_v_d,
        "PV18__H_up": PV18__H_up,
        "PV18__s_v_d": PV18__s_v_d,
        "PV18__H_L_out": PV18__H_L_out,
        "PV18__H_R_out": PV18__H_R_out,
        "PV18__v_pos": PV18__v_pos,
        "PV18__v_neg": PV18__v_neg,
        "PV18__v_d_pos": PV18__v_d_pos,
        "PV18__v_d_neg": PV18__v_d_neg,
        "PV18__H_volume_L": PV18__H_volume_L,
        "PV18__H_volume_R": PV18__H_volume_R,
        "PV18__v_mm3_s": PV18__v_mm3_s,
        "PV18__v_d_mm3_s": PV18__v_d_mm3_s,
        "V17__w_v": V17__w_v,
        "V17__H_up": V17__H_up,
        "V17__s_v": V17__s_v,
        "V17__H_L_out": V17__H_L_out,
        "V17__H_R_out": V17__H_R_out,
        "V17__v_pos": V17__v_pos,
        "V17__v_neg": V17__v_neg,
        "V17__H_volume_L": V17__H_volume_L,
        "V17__H_volume_R": V17__H_volume_R,
        "V17__v_mm3_s": V17__v_mm3_s,
        "V18__w_v": V18__w_v,
        "V18__H_up": V18__H_up,
        "V18__s_v": V18__s_v,
        "V18__H_L_out": V18__H_L_out,
        "V18__H_R_out": V18__H_R_out,
        "V18__v_pos": V18__v_pos,
        "V18__v_neg": V18__v_neg,
        "V18__H_volume_L": V18__H_volume_L,
        "V18__H_volume_R": V18__H_volume_R,
        "V18__v_mm3_s": V18__v_mm3_s,
        "VV_junc10__vj1": VV_junc10__vj1,
        "VV_junc10__vj3": VV_junc10__vj3,
        "VV_junc10__vj4": VV_junc10__vj4,
        "VV_junc10__w_in1": VV_junc10__w_in1,
        "VV_junc10__w_in3": VV_junc10__w_in3,
        "VV_junc10__w_in4": VV_junc10__w_in4,
        "VV_junc10__w_out1": VV_junc10__w_out1,
        "VV_junc10__w_out3": VV_junc10__w_out3,
        "VV_junc10__w_out4": VV_junc10__w_out4,
        "VV_junc10__Qin1": VV_junc10__Qin1,
        "VV_junc10__Qin3": VV_junc10__Qin3,
        "VV_junc10__Qin4": VV_junc10__Qin4,
        "VV_junc10__Qout1": VV_junc10__Qout1,
        "VV_junc10__Qout3": VV_junc10__Qout3,
        "VV_junc10__Qout4": VV_junc10__Qout4,
        "VV_junc10__Qin_tot": VV_junc10__Qin_tot,
        "VV_junc10__Qout_tot": VV_junc10__Qout_tot,
        "VV_junc10__v": VV_junc10__v,
        "VV_junc10__bc1_is_in": VV_junc10__bc1_is_in,
        "VV_junc10__bc3_is_in": VV_junc10__bc3_is_in,
        "VV_junc10__bc4_is_in": VV_junc10__bc4_is_in,
        "VV_junc10__bc1_is_out": VV_junc10__bc1_is_out,
        "VV_junc10__bc3_is_out": VV_junc10__bc3_is_out,
        "VV_junc10__bc4_is_out": VV_junc10__bc4_is_out,
        "PV19__w_v": PV19__w_v,
        "PV19__w_v_d": PV19__w_v_d,
        "PV19__H_up": PV19__H_up,
        "PV19__s_v_d": PV19__s_v_d,
        "PV19__H_L_out": PV19__H_L_out,
        "PV19__H_R_out": PV19__H_R_out,
        "PV19__v_pos": PV19__v_pos,
        "PV19__v_neg": PV19__v_neg,
        "PV19__v_d_pos": PV19__v_d_pos,
        "PV19__v_d_neg": PV19__v_d_neg,
        "PV19__H_volume_L": PV19__H_volume_L,
        "PV19__H_volume_R": PV19__H_volume_R,
        "PV19__v_mm3_s": PV19__v_mm3_s,
        "PV19__v_d_mm3_s": PV19__v_d_mm3_s,
        "PV20__w_v": PV20__w_v,
        "PV20__w_v_d": PV20__w_v_d,
        "PV20__H_up": PV20__H_up,
        "PV20__s_v_d": PV20__s_v_d,
        "PV20__H_L_out": PV20__H_L_out,
        "PV20__H_R_out": PV20__H_R_out,
        "PV20__v_pos": PV20__v_pos,
        "PV20__v_neg": PV20__v_neg,
        "PV20__v_d_pos": PV20__v_d_pos,
        "PV20__v_d_neg": PV20__v_d_neg,
        "PV20__H_volume_L": PV20__H_volume_L,
        "PV20__H_volume_R": PV20__H_volume_R,
        "PV20__v_mm3_s": PV20__v_mm3_s,
        "PV20__v_d_mm3_s": PV20__v_d_mm3_s,
        "V19__w_v": V19__w_v,
        "V19__H_up": V19__H_up,
        "V19__s_v": V19__s_v,
        "V19__H_L_out": V19__H_L_out,
        "V19__H_R_out": V19__H_R_out,
        "V19__v_pos": V19__v_pos,
        "V19__v_neg": V19__v_neg,
        "V19__H_volume_L": V19__H_volume_L,
        "V19__H_volume_R": V19__H_volume_R,
        "V19__v_mm3_s": V19__v_mm3_s,
        "V20__w_v": V20__w_v,
        "V20__H_up": V20__H_up,
        "V20__s_v": V20__s_v,
        "V20__H_L_out": V20__H_L_out,
        "V20__H_R_out": V20__H_R_out,
        "V20__v_pos": V20__v_pos,
        "V20__v_neg": V20__v_neg,
        "V20__H_volume_L": V20__H_volume_L,
        "V20__H_volume_R": V20__H_volume_R,
        "V20__v_mm3_s": V20__v_mm3_s,
        "VV_junc11__vj1": VV_junc11__vj1,
        "VV_junc11__vj3": VV_junc11__vj3,
        "VV_junc11__vj4": VV_junc11__vj4,
        "VV_junc11__w_in1": VV_junc11__w_in1,
        "VV_junc11__w_in3": VV_junc11__w_in3,
        "VV_junc11__w_in4": VV_junc11__w_in4,
        "VV_junc11__w_out1": VV_junc11__w_out1,
        "VV_junc11__w_out3": VV_junc11__w_out3,
        "VV_junc11__w_out4": VV_junc11__w_out4,
        "VV_junc11__Qin1": VV_junc11__Qin1,
        "VV_junc11__Qin3": VV_junc11__Qin3,
        "VV_junc11__Qin4": VV_junc11__Qin4,
        "VV_junc11__Qout1": VV_junc11__Qout1,
        "VV_junc11__Qout3": VV_junc11__Qout3,
        "VV_junc11__Qout4": VV_junc11__Qout4,
        "VV_junc11__Qin_tot": VV_junc11__Qin_tot,
        "VV_junc11__Qout_tot": VV_junc11__Qout_tot,
        "VV_junc11__v": VV_junc11__v,
        "VV_junc11__bc1_is_in": VV_junc11__bc1_is_in,
        "VV_junc11__bc3_is_in": VV_junc11__bc3_is_in,
        "VV_junc11__bc4_is_in": VV_junc11__bc4_is_in,
        "VV_junc11__bc1_is_out": VV_junc11__bc1_is_out,
        "VV_junc11__bc3_is_out": VV_junc11__bc3_is_out,
        "VV_junc11__bc4_is_out": VV_junc11__bc4_is_out,
        "PV21__w_v": PV21__w_v,
        "PV21__w_v_d": PV21__w_v_d,
        "PV21__H_up": PV21__H_up,
        "PV21__s_v_d": PV21__s_v_d,
        "PV21__H_L_out": PV21__H_L_out,
        "PV21__H_R_out": PV21__H_R_out,
        "PV21__v_pos": PV21__v_pos,
        "PV21__v_neg": PV21__v_neg,
        "PV21__v_d_pos": PV21__v_d_pos,
        "PV21__v_d_neg": PV21__v_d_neg,
        "PV21__H_volume_L": PV21__H_volume_L,
        "PV21__H_volume_R": PV21__H_volume_R,
        "PV21__v_mm3_s": PV21__v_mm3_s,
        "PV21__v_d_mm3_s": PV21__v_d_mm3_s,
        "PV22__w_v": PV22__w_v,
        "PV22__w_v_d": PV22__w_v_d,
        "PV22__H_up": PV22__H_up,
        "PV22__s_v_d": PV22__s_v_d,
        "PV22__H_L_out": PV22__H_L_out,
        "PV22__H_R_out": PV22__H_R_out,
        "PV22__v_pos": PV22__v_pos,
        "PV22__v_neg": PV22__v_neg,
        "PV22__v_d_pos": PV22__v_d_pos,
        "PV22__v_d_neg": PV22__v_d_neg,
        "PV22__H_volume_L": PV22__H_volume_L,
        "PV22__H_volume_R": PV22__H_volume_R,
        "PV22__v_mm3_s": PV22__v_mm3_s,
        "PV22__v_d_mm3_s": PV22__v_d_mm3_s,
        "V21__w_v": V21__w_v,
        "V21__H_up": V21__H_up,
        "V21__s_v": V21__s_v,
        "V21__H_L_out": V21__H_L_out,
        "V21__H_R_out": V21__H_R_out,
        "V21__v_pos": V21__v_pos,
        "V21__v_neg": V21__v_neg,
        "V21__H_volume_L": V21__H_volume_L,
        "V21__H_volume_R": V21__H_volume_R,
        "V21__v_mm3_s": V21__v_mm3_s,
        "V22__w_v": V22__w_v,
        "V22__H_up": V22__H_up,
        "V22__s_v": V22__s_v,
        "V22__H_L_out": V22__H_L_out,
        "V22__H_R_out": V22__H_R_out,
        "V22__v_pos": V22__v_pos,
        "V22__v_neg": V22__v_neg,
        "V22__H_volume_L": V22__H_volume_L,
        "V22__H_volume_R": V22__H_volume_R,
        "V22__v_mm3_s": V22__v_mm3_s,
        "VV_junc12__vj1": VV_junc12__vj1,
        "VV_junc12__vj3": VV_junc12__vj3,
        "VV_junc12__vj4": VV_junc12__vj4,
        "VV_junc12__w_in1": VV_junc12__w_in1,
        "VV_junc12__w_in3": VV_junc12__w_in3,
        "VV_junc12__w_in4": VV_junc12__w_in4,
        "VV_junc12__w_out1": VV_junc12__w_out1,
        "VV_junc12__w_out3": VV_junc12__w_out3,
        "VV_junc12__w_out4": VV_junc12__w_out4,
        "VV_junc12__Qin1": VV_junc12__Qin1,
        "VV_junc12__Qin3": VV_junc12__Qin3,
        "VV_junc12__Qin4": VV_junc12__Qin4,
        "VV_junc12__Qout1": VV_junc12__Qout1,
        "VV_junc12__Qout3": VV_junc12__Qout3,
        "VV_junc12__Qout4": VV_junc12__Qout4,
        "VV_junc12__Qin_tot": VV_junc12__Qin_tot,
        "VV_junc12__Qout_tot": VV_junc12__Qout_tot,
        "VV_junc12__v": VV_junc12__v,
        "VV_junc12__bc1_is_in": VV_junc12__bc1_is_in,
        "VV_junc12__bc3_is_in": VV_junc12__bc3_is_in,
        "VV_junc12__bc4_is_in": VV_junc12__bc4_is_in,
        "VV_junc12__bc1_is_out": VV_junc12__bc1_is_out,
        "VV_junc12__bc3_is_out": VV_junc12__bc3_is_out,
        "VV_junc12__bc4_is_out": VV_junc12__bc4_is_out,
        "PV23__w_v": PV23__w_v,
        "PV23__w_v_d": PV23__w_v_d,
        "PV23__H_up": PV23__H_up,
        "PV23__s_v_d": PV23__s_v_d,
        "PV23__H_L_out": PV23__H_L_out,
        "PV23__H_R_out": PV23__H_R_out,
        "PV23__v_pos": PV23__v_pos,
        "PV23__v_neg": PV23__v_neg,
        "PV23__v_d_pos": PV23__v_d_pos,
        "PV23__v_d_neg": PV23__v_d_neg,
        "PV23__H_volume_L": PV23__H_volume_L,
        "PV23__H_volume_R": PV23__H_volume_R,
        "PV23__v_mm3_s": PV23__v_mm3_s,
        "PV23__v_d_mm3_s": PV23__v_d_mm3_s,
        "PV24__w_v": PV24__w_v,
        "PV24__w_v_d": PV24__w_v_d,
        "PV24__H_up": PV24__H_up,
        "PV24__s_v_d": PV24__s_v_d,
        "PV24__H_L_out": PV24__H_L_out,
        "PV24__H_R_out": PV24__H_R_out,
        "PV24__v_pos": PV24__v_pos,
        "PV24__v_neg": PV24__v_neg,
        "PV24__v_d_pos": PV24__v_d_pos,
        "PV24__v_d_neg": PV24__v_d_neg,
        "PV24__H_volume_L": PV24__H_volume_L,
        "PV24__H_volume_R": PV24__H_volume_R,
        "PV24__v_mm3_s": PV24__v_mm3_s,
        "PV24__v_d_mm3_s": PV24__v_d_mm3_s,
        "V23__w_v": V23__w_v,
        "V23__H_up": V23__H_up,
        "V23__s_v": V23__s_v,
        "V23__H_L_out": V23__H_L_out,
        "V23__H_R_out": V23__H_R_out,
        "V23__v_pos": V23__v_pos,
        "V23__v_neg": V23__v_neg,
        "V23__H_volume_L": V23__H_volume_L,
        "V23__H_volume_R": V23__H_volume_R,
        "V23__v_mm3_s": V23__v_mm3_s,
        "V24__w_v": V24__w_v,
        "V24__H_up": V24__H_up,
        "V24__s_v": V24__s_v,
        "V24__H_L_out": V24__H_L_out,
        "V24__H_R_out": V24__H_R_out,
        "V24__v_pos": V24__v_pos,
        "V24__v_neg": V24__v_neg,
        "V24__H_volume_L": V24__H_volume_L,
        "V24__H_volume_R": V24__H_volume_R,
        "V24__v_mm3_s": V24__v_mm3_s,
        "VV_junc13__vj1": VV_junc13__vj1,
        "VV_junc13__vj3": VV_junc13__vj3,
        "VV_junc13__vj4": VV_junc13__vj4,
        "VV_junc13__w_in1": VV_junc13__w_in1,
        "VV_junc13__w_in3": VV_junc13__w_in3,
        "VV_junc13__w_in4": VV_junc13__w_in4,
        "VV_junc13__w_out1": VV_junc13__w_out1,
        "VV_junc13__w_out3": VV_junc13__w_out3,
        "VV_junc13__w_out4": VV_junc13__w_out4,
        "VV_junc13__Qin1": VV_junc13__Qin1,
        "VV_junc13__Qin3": VV_junc13__Qin3,
        "VV_junc13__Qin4": VV_junc13__Qin4,
        "VV_junc13__Qout1": VV_junc13__Qout1,
        "VV_junc13__Qout3": VV_junc13__Qout3,
        "VV_junc13__Qout4": VV_junc13__Qout4,
        "VV_junc13__Qin_tot": VV_junc13__Qin_tot,
        "VV_junc13__Qout_tot": VV_junc13__Qout_tot,
        "VV_junc13__v": VV_junc13__v,
        "VV_junc13__bc1_is_in": VV_junc13__bc1_is_in,
        "VV_junc13__bc3_is_in": VV_junc13__bc3_is_in,
        "VV_junc13__bc4_is_in": VV_junc13__bc4_is_in,
        "VV_junc13__bc1_is_out": VV_junc13__bc1_is_out,
        "VV_junc13__bc3_is_out": VV_junc13__bc3_is_out,
        "VV_junc13__bc4_is_out": VV_junc13__bc4_is_out,
        "PV25__w_v": PV25__w_v,
        "PV25__w_v_d": PV25__w_v_d,
        "PV25__H_up": PV25__H_up,
        "PV25__s_v_d": PV25__s_v_d,
        "PV25__H_L_out": PV25__H_L_out,
        "PV25__H_R_out": PV25__H_R_out,
        "PV25__v_pos": PV25__v_pos,
        "PV25__v_neg": PV25__v_neg,
        "PV25__v_d_pos": PV25__v_d_pos,
        "PV25__v_d_neg": PV25__v_d_neg,
        "PV25__H_volume_L": PV25__H_volume_L,
        "PV25__H_volume_R": PV25__H_volume_R,
        "PV25__v_mm3_s": PV25__v_mm3_s,
        "PV25__v_d_mm3_s": PV25__v_d_mm3_s,
        "PV26__w_v": PV26__w_v,
        "PV26__w_v_d": PV26__w_v_d,
        "PV26__H_up": PV26__H_up,
        "PV26__s_v_d": PV26__s_v_d,
        "PV26__H_L_out": PV26__H_L_out,
        "PV26__H_R_out": PV26__H_R_out,
        "PV26__v_pos": PV26__v_pos,
        "PV26__v_neg": PV26__v_neg,
        "PV26__v_d_pos": PV26__v_d_pos,
        "PV26__v_d_neg": PV26__v_d_neg,
        "PV26__H_volume_L": PV26__H_volume_L,
        "PV26__H_volume_R": PV26__H_volume_R,
        "PV26__v_mm3_s": PV26__v_mm3_s,
        "PV26__v_d_mm3_s": PV26__v_d_mm3_s,
        "V25__w_v": V25__w_v,
        "V25__H_up": V25__H_up,
        "V25__s_v": V25__s_v,
        "V25__H_L_out": V25__H_L_out,
        "V25__H_R_out": V25__H_R_out,
        "V25__v_pos": V25__v_pos,
        "V25__v_neg": V25__v_neg,
        "V25__H_volume_L": V25__H_volume_L,
        "V25__H_volume_R": V25__H_volume_R,
        "V25__v_mm3_s": V25__v_mm3_s,
        "V26__w_v": V26__w_v,
        "V26__H_up": V26__H_up,
        "V26__s_v": V26__s_v,
        "V26__H_L_out": V26__H_L_out,
        "V26__H_R_out": V26__H_R_out,
        "V26__v_pos": V26__v_pos,
        "V26__v_neg": V26__v_neg,
        "V26__H_volume_L": V26__H_volume_L,
        "V26__H_volume_R": V26__H_volume_R,
        "V26__v_mm3_s": V26__v_mm3_s,
        "VV_junc14__vj1": VV_junc14__vj1,
        "VV_junc14__vj3": VV_junc14__vj3,
        "VV_junc14__vj4": VV_junc14__vj4,
        "VV_junc14__w_in1": VV_junc14__w_in1,
        "VV_junc14__w_in3": VV_junc14__w_in3,
        "VV_junc14__w_in4": VV_junc14__w_in4,
        "VV_junc14__w_out1": VV_junc14__w_out1,
        "VV_junc14__w_out3": VV_junc14__w_out3,
        "VV_junc14__w_out4": VV_junc14__w_out4,
        "VV_junc14__Qin1": VV_junc14__Qin1,
        "VV_junc14__Qin3": VV_junc14__Qin3,
        "VV_junc14__Qin4": VV_junc14__Qin4,
        "VV_junc14__Qout1": VV_junc14__Qout1,
        "VV_junc14__Qout3": VV_junc14__Qout3,
        "VV_junc14__Qout4": VV_junc14__Qout4,
        "VV_junc14__Qin_tot": VV_junc14__Qin_tot,
        "VV_junc14__Qout_tot": VV_junc14__Qout_tot,
        "VV_junc14__v": VV_junc14__v,
        "VV_junc14__bc1_is_in": VV_junc14__bc1_is_in,
        "VV_junc14__bc3_is_in": VV_junc14__bc3_is_in,
        "VV_junc14__bc4_is_in": VV_junc14__bc4_is_in,
        "VV_junc14__bc1_is_out": VV_junc14__bc1_is_out,
        "VV_junc14__bc3_is_out": VV_junc14__bc3_is_out,
        "VV_junc14__bc4_is_out": VV_junc14__bc4_is_out,
        "PV27__w_v": PV27__w_v,
        "PV27__w_v_d": PV27__w_v_d,
        "PV27__H_up": PV27__H_up,
        "PV27__s_v_d": PV27__s_v_d,
        "PV27__H_L_out": PV27__H_L_out,
        "PV27__H_R_out": PV27__H_R_out,
        "PV27__v_pos": PV27__v_pos,
        "PV27__v_neg": PV27__v_neg,
        "PV27__v_d_pos": PV27__v_d_pos,
        "PV27__v_d_neg": PV27__v_d_neg,
        "PV27__H_volume_L": PV27__H_volume_L,
        "PV27__H_volume_R": PV27__H_volume_R,
        "PV27__v_mm3_s": PV27__v_mm3_s,
        "PV27__v_d_mm3_s": PV27__v_d_mm3_s,
        "PV28__w_v": PV28__w_v,
        "PV28__w_v_d": PV28__w_v_d,
        "PV28__H_up": PV28__H_up,
        "PV28__s_v_d": PV28__s_v_d,
        "PV28__H_L_out": PV28__H_L_out,
        "PV28__H_R_out": PV28__H_R_out,
        "PV28__v_pos": PV28__v_pos,
        "PV28__v_neg": PV28__v_neg,
        "PV28__v_d_pos": PV28__v_d_pos,
        "PV28__v_d_neg": PV28__v_d_neg,
        "PV28__H_volume_L": PV28__H_volume_L,
        "PV28__H_volume_R": PV28__H_volume_R,
        "PV28__v_mm3_s": PV28__v_mm3_s,
        "PV28__v_d_mm3_s": PV28__v_d_mm3_s,
        "V27__w_v": V27__w_v,
        "V27__H_up": V27__H_up,
        "V27__s_v": V27__s_v,
        "V27__H_L_out": V27__H_L_out,
        "V27__H_R_out": V27__H_R_out,
        "V27__v_pos": V27__v_pos,
        "V27__v_neg": V27__v_neg,
        "V27__H_volume_L": V27__H_volume_L,
        "V27__H_volume_R": V27__H_volume_R,
        "V27__v_mm3_s": V27__v_mm3_s,
        "V28__w_v": V28__w_v,
        "V28__H_up": V28__H_up,
        "V28__s_v": V28__s_v,
        "V28__H_L_out": V28__H_L_out,
        "V28__H_R_out": V28__H_R_out,
        "V28__v_pos": V28__v_pos,
        "V28__v_neg": V28__v_neg,
        "V28__H_volume_L": V28__H_volume_L,
        "V28__H_volume_R": V28__H_volume_R,
        "V28__v_mm3_s": V28__v_mm3_s,
        "VV_junc15__vj1": VV_junc15__vj1,
        "VV_junc15__vj3": VV_junc15__vj3,
        "VV_junc15__vj4": VV_junc15__vj4,
        "VV_junc15__w_in1": VV_junc15__w_in1,
        "VV_junc15__w_in3": VV_junc15__w_in3,
        "VV_junc15__w_in4": VV_junc15__w_in4,
        "VV_junc15__w_out1": VV_junc15__w_out1,
        "VV_junc15__w_out3": VV_junc15__w_out3,
        "VV_junc15__w_out4": VV_junc15__w_out4,
        "VV_junc15__Qin1": VV_junc15__Qin1,
        "VV_junc15__Qin3": VV_junc15__Qin3,
        "VV_junc15__Qin4": VV_junc15__Qin4,
        "VV_junc15__Qout1": VV_junc15__Qout1,
        "VV_junc15__Qout3": VV_junc15__Qout3,
        "VV_junc15__Qout4": VV_junc15__Qout4,
        "VV_junc15__Qin_tot": VV_junc15__Qin_tot,
        "VV_junc15__Qout_tot": VV_junc15__Qout_tot,
        "VV_junc15__v": VV_junc15__v,
        "VV_junc15__bc1_is_in": VV_junc15__bc1_is_in,
        "VV_junc15__bc3_is_in": VV_junc15__bc3_is_in,
        "VV_junc15__bc4_is_in": VV_junc15__bc4_is_in,
        "VV_junc15__bc1_is_out": VV_junc15__bc1_is_out,
        "VV_junc15__bc3_is_out": VV_junc15__bc3_is_out,
        "VV_junc15__bc4_is_out": VV_junc15__bc4_is_out,
        "PV29__w_v": PV29__w_v,
        "PV29__w_v_d": PV29__w_v_d,
        "PV29__H_up": PV29__H_up,
        "PV29__s_v_d": PV29__s_v_d,
        "PV29__H_L_out": PV29__H_L_out,
        "PV29__H_R_out": PV29__H_R_out,
        "PV29__v_pos": PV29__v_pos,
        "PV29__v_neg": PV29__v_neg,
        "PV29__v_d_pos": PV29__v_d_pos,
        "PV29__v_d_neg": PV29__v_d_neg,
        "PV29__H_volume_L": PV29__H_volume_L,
        "PV29__H_volume_R": PV29__H_volume_R,
        "PV29__v_mm3_s": PV29__v_mm3_s,
        "PV29__v_d_mm3_s": PV29__v_d_mm3_s,
        "PV30__w_v": PV30__w_v,
        "PV30__w_v_d": PV30__w_v_d,
        "PV30__H_up": PV30__H_up,
        "PV30__s_v_d": PV30__s_v_d,
        "PV30__H_L_out": PV30__H_L_out,
        "PV30__H_R_out": PV30__H_R_out,
        "PV30__v_pos": PV30__v_pos,
        "PV30__v_neg": PV30__v_neg,
        "PV30__v_d_pos": PV30__v_d_pos,
        "PV30__v_d_neg": PV30__v_d_neg,
        "PV30__H_volume_L": PV30__H_volume_L,
        "PV30__H_volume_R": PV30__H_volume_R,
        "PV30__v_mm3_s": PV30__v_mm3_s,
        "PV30__v_d_mm3_s": PV30__v_d_mm3_s,
        "V29__w_v": V29__w_v,
        "V29__H_up": V29__H_up,
        "V29__s_v": V29__s_v,
        "V29__H_L_out": V29__H_L_out,
        "V29__H_R_out": V29__H_R_out,
        "V29__v_pos": V29__v_pos,
        "V29__v_neg": V29__v_neg,
        "V29__H_volume_L": V29__H_volume_L,
        "V29__H_volume_R": V29__H_volume_R,
        "V29__v_mm3_s": V29__v_mm3_s,
        "V30__w_v": V30__w_v,
        "V30__H_up": V30__H_up,
        "V30__s_v": V30__s_v,
        "V30__H_L_out": V30__H_L_out,
        "V30__H_R_out": V30__H_R_out,
        "V30__v_pos": V30__v_pos,
        "V30__v_neg": V30__v_neg,
        "V30__H_volume_L": V30__H_volume_L,
        "V30__H_volume_R": V30__H_volume_R,
        "V30__v_mm3_s": V30__v_mm3_s,
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
        "VV_junc8__n_in": VV_junc8__n_in,
        "VV_junc8__n_out": VV_junc8__n_out,
        "VV_junc8__RBC_in": VV_junc8__RBC_in,
        "VV_junc8__v_mm3_s": VV_junc8__v_mm3_s,
        "VV_junc8__junction_type": VV_junc8__junction_type,
        "VV_junc8__is_split": VV_junc8__is_split,
        "VV_junc8__is_merge": VV_junc8__is_merge,
        "VV_junc8__feed1": VV_junc8__feed1,
        "VV_junc8__feed2": VV_junc8__feed2,
        "VV_junc8__feed3": VV_junc8__feed3,
        "VV_junc8__feed4": VV_junc8__feed4,
        "VV_junc8__alpha1": VV_junc8__alpha1,
        "VV_junc8__alpha2": VV_junc8__alpha2,
        "VV_junc8__alpha3": VV_junc8__alpha3,
        "VV_junc8__alpha4": VV_junc8__alpha4,
        "VV_junc8__Qout1_rem": VV_junc8__Qout1_rem,
        "VV_junc8__Qout2_rem": VV_junc8__Qout2_rem,
        "VV_junc8__Qout3_rem": VV_junc8__Qout3_rem,
        "VV_junc8__Qout4_rem": VV_junc8__Qout4_rem,
        "VV_junc8__beta1": VV_junc8__beta1,
        "VV_junc8__beta2": VV_junc8__beta2,
        "VV_junc8__beta3": VV_junc8__beta3,
        "VV_junc8__beta4": VV_junc8__beta4,
        "VV_junc8__D_F": VV_junc8__D_F,
        "VV_junc8__D_alpha": VV_junc8__D_alpha,
        "VV_junc8__D_beta": VV_junc8__D_beta,
        "VV_junc8__v_alpha": VV_junc8__v_alpha,
        "VV_junc8__v_beta": VV_junc8__v_beta,
        "PV15__H_down_target": PV15__H_down_target,
        "PV16__H_down_target": PV16__H_down_target,
        "V15__H_down_target": V15__H_down_target,
        "V16__H_down_target": V16__H_down_target,
        "VV_junc9__n_in": VV_junc9__n_in,
        "VV_junc9__n_out": VV_junc9__n_out,
        "VV_junc9__RBC_in": VV_junc9__RBC_in,
        "VV_junc9__v_mm3_s": VV_junc9__v_mm3_s,
        "VV_junc9__junction_type": VV_junc9__junction_type,
        "VV_junc9__is_split": VV_junc9__is_split,
        "VV_junc9__is_merge": VV_junc9__is_merge,
        "VV_junc9__feed1": VV_junc9__feed1,
        "VV_junc9__feed2": VV_junc9__feed2,
        "VV_junc9__feed3": VV_junc9__feed3,
        "VV_junc9__feed4": VV_junc9__feed4,
        "VV_junc9__alpha1": VV_junc9__alpha1,
        "VV_junc9__alpha2": VV_junc9__alpha2,
        "VV_junc9__alpha3": VV_junc9__alpha3,
        "VV_junc9__alpha4": VV_junc9__alpha4,
        "VV_junc9__Qout1_rem": VV_junc9__Qout1_rem,
        "VV_junc9__Qout2_rem": VV_junc9__Qout2_rem,
        "VV_junc9__Qout3_rem": VV_junc9__Qout3_rem,
        "VV_junc9__Qout4_rem": VV_junc9__Qout4_rem,
        "VV_junc9__beta1": VV_junc9__beta1,
        "VV_junc9__beta2": VV_junc9__beta2,
        "VV_junc9__beta3": VV_junc9__beta3,
        "VV_junc9__beta4": VV_junc9__beta4,
        "VV_junc9__D_F": VV_junc9__D_F,
        "VV_junc9__D_alpha": VV_junc9__D_alpha,
        "VV_junc9__D_beta": VV_junc9__D_beta,
        "VV_junc9__v_alpha": VV_junc9__v_alpha,
        "VV_junc9__v_beta": VV_junc9__v_beta,
        "PV17__H_down_target": PV17__H_down_target,
        "PV18__H_down_target": PV18__H_down_target,
        "V17__H_down_target": V17__H_down_target,
        "V18__H_down_target": V18__H_down_target,
        "VV_junc10__n_in": VV_junc10__n_in,
        "VV_junc10__n_out": VV_junc10__n_out,
        "VV_junc10__RBC_in": VV_junc10__RBC_in,
        "VV_junc10__v_mm3_s": VV_junc10__v_mm3_s,
        "VV_junc10__junction_type": VV_junc10__junction_type,
        "VV_junc10__is_split": VV_junc10__is_split,
        "VV_junc10__is_merge": VV_junc10__is_merge,
        "VV_junc10__feed1": VV_junc10__feed1,
        "VV_junc10__feed2": VV_junc10__feed2,
        "VV_junc10__feed3": VV_junc10__feed3,
        "VV_junc10__feed4": VV_junc10__feed4,
        "VV_junc10__alpha1": VV_junc10__alpha1,
        "VV_junc10__alpha2": VV_junc10__alpha2,
        "VV_junc10__alpha3": VV_junc10__alpha3,
        "VV_junc10__alpha4": VV_junc10__alpha4,
        "VV_junc10__Qout1_rem": VV_junc10__Qout1_rem,
        "VV_junc10__Qout2_rem": VV_junc10__Qout2_rem,
        "VV_junc10__Qout3_rem": VV_junc10__Qout3_rem,
        "VV_junc10__Qout4_rem": VV_junc10__Qout4_rem,
        "VV_junc10__beta1": VV_junc10__beta1,
        "VV_junc10__beta2": VV_junc10__beta2,
        "VV_junc10__beta3": VV_junc10__beta3,
        "VV_junc10__beta4": VV_junc10__beta4,
        "VV_junc10__D_F": VV_junc10__D_F,
        "VV_junc10__D_alpha": VV_junc10__D_alpha,
        "VV_junc10__D_beta": VV_junc10__D_beta,
        "VV_junc10__v_alpha": VV_junc10__v_alpha,
        "VV_junc10__v_beta": VV_junc10__v_beta,
        "PV19__H_down_target": PV19__H_down_target,
        "PV20__H_down_target": PV20__H_down_target,
        "V19__H_down_target": V19__H_down_target,
        "V20__H_down_target": V20__H_down_target,
        "VV_junc11__n_in": VV_junc11__n_in,
        "VV_junc11__n_out": VV_junc11__n_out,
        "VV_junc11__RBC_in": VV_junc11__RBC_in,
        "VV_junc11__v_mm3_s": VV_junc11__v_mm3_s,
        "VV_junc11__junction_type": VV_junc11__junction_type,
        "VV_junc11__is_split": VV_junc11__is_split,
        "VV_junc11__is_merge": VV_junc11__is_merge,
        "VV_junc11__feed1": VV_junc11__feed1,
        "VV_junc11__feed2": VV_junc11__feed2,
        "VV_junc11__feed3": VV_junc11__feed3,
        "VV_junc11__feed4": VV_junc11__feed4,
        "VV_junc11__alpha1": VV_junc11__alpha1,
        "VV_junc11__alpha2": VV_junc11__alpha2,
        "VV_junc11__alpha3": VV_junc11__alpha3,
        "VV_junc11__alpha4": VV_junc11__alpha4,
        "VV_junc11__Qout1_rem": VV_junc11__Qout1_rem,
        "VV_junc11__Qout2_rem": VV_junc11__Qout2_rem,
        "VV_junc11__Qout3_rem": VV_junc11__Qout3_rem,
        "VV_junc11__Qout4_rem": VV_junc11__Qout4_rem,
        "VV_junc11__beta1": VV_junc11__beta1,
        "VV_junc11__beta2": VV_junc11__beta2,
        "VV_junc11__beta3": VV_junc11__beta3,
        "VV_junc11__beta4": VV_junc11__beta4,
        "VV_junc11__D_F": VV_junc11__D_F,
        "VV_junc11__D_alpha": VV_junc11__D_alpha,
        "VV_junc11__D_beta": VV_junc11__D_beta,
        "VV_junc11__v_alpha": VV_junc11__v_alpha,
        "VV_junc11__v_beta": VV_junc11__v_beta,
        "PV21__H_down_target": PV21__H_down_target,
        "PV22__H_down_target": PV22__H_down_target,
        "V21__H_down_target": V21__H_down_target,
        "V22__H_down_target": V22__H_down_target,
        "VV_junc12__n_in": VV_junc12__n_in,
        "VV_junc12__n_out": VV_junc12__n_out,
        "VV_junc12__RBC_in": VV_junc12__RBC_in,
        "VV_junc12__v_mm3_s": VV_junc12__v_mm3_s,
        "VV_junc12__junction_type": VV_junc12__junction_type,
        "VV_junc12__is_split": VV_junc12__is_split,
        "VV_junc12__is_merge": VV_junc12__is_merge,
        "VV_junc12__feed1": VV_junc12__feed1,
        "VV_junc12__feed2": VV_junc12__feed2,
        "VV_junc12__feed3": VV_junc12__feed3,
        "VV_junc12__feed4": VV_junc12__feed4,
        "VV_junc12__alpha1": VV_junc12__alpha1,
        "VV_junc12__alpha2": VV_junc12__alpha2,
        "VV_junc12__alpha3": VV_junc12__alpha3,
        "VV_junc12__alpha4": VV_junc12__alpha4,
        "VV_junc12__Qout1_rem": VV_junc12__Qout1_rem,
        "VV_junc12__Qout2_rem": VV_junc12__Qout2_rem,
        "VV_junc12__Qout3_rem": VV_junc12__Qout3_rem,
        "VV_junc12__Qout4_rem": VV_junc12__Qout4_rem,
        "VV_junc12__beta1": VV_junc12__beta1,
        "VV_junc12__beta2": VV_junc12__beta2,
        "VV_junc12__beta3": VV_junc12__beta3,
        "VV_junc12__beta4": VV_junc12__beta4,
        "VV_junc12__D_F": VV_junc12__D_F,
        "VV_junc12__D_alpha": VV_junc12__D_alpha,
        "VV_junc12__D_beta": VV_junc12__D_beta,
        "VV_junc12__v_alpha": VV_junc12__v_alpha,
        "VV_junc12__v_beta": VV_junc12__v_beta,
        "PV23__H_down_target": PV23__H_down_target,
        "PV24__H_down_target": PV24__H_down_target,
        "V23__H_down_target": V23__H_down_target,
        "V24__H_down_target": V24__H_down_target,
        "VV_junc13__n_in": VV_junc13__n_in,
        "VV_junc13__n_out": VV_junc13__n_out,
        "VV_junc13__RBC_in": VV_junc13__RBC_in,
        "VV_junc13__v_mm3_s": VV_junc13__v_mm3_s,
        "VV_junc13__junction_type": VV_junc13__junction_type,
        "VV_junc13__is_split": VV_junc13__is_split,
        "VV_junc13__is_merge": VV_junc13__is_merge,
        "VV_junc13__feed1": VV_junc13__feed1,
        "VV_junc13__feed2": VV_junc13__feed2,
        "VV_junc13__feed3": VV_junc13__feed3,
        "VV_junc13__feed4": VV_junc13__feed4,
        "VV_junc13__alpha1": VV_junc13__alpha1,
        "VV_junc13__alpha2": VV_junc13__alpha2,
        "VV_junc13__alpha3": VV_junc13__alpha3,
        "VV_junc13__alpha4": VV_junc13__alpha4,
        "VV_junc13__Qout1_rem": VV_junc13__Qout1_rem,
        "VV_junc13__Qout2_rem": VV_junc13__Qout2_rem,
        "VV_junc13__Qout3_rem": VV_junc13__Qout3_rem,
        "VV_junc13__Qout4_rem": VV_junc13__Qout4_rem,
        "VV_junc13__beta1": VV_junc13__beta1,
        "VV_junc13__beta2": VV_junc13__beta2,
        "VV_junc13__beta3": VV_junc13__beta3,
        "VV_junc13__beta4": VV_junc13__beta4,
        "VV_junc13__D_F": VV_junc13__D_F,
        "VV_junc13__D_alpha": VV_junc13__D_alpha,
        "VV_junc13__D_beta": VV_junc13__D_beta,
        "VV_junc13__v_alpha": VV_junc13__v_alpha,
        "VV_junc13__v_beta": VV_junc13__v_beta,
        "PV25__H_down_target": PV25__H_down_target,
        "PV26__H_down_target": PV26__H_down_target,
        "V25__H_down_target": V25__H_down_target,
        "V26__H_down_target": V26__H_down_target,
        "VV_junc14__n_in": VV_junc14__n_in,
        "VV_junc14__n_out": VV_junc14__n_out,
        "VV_junc14__RBC_in": VV_junc14__RBC_in,
        "VV_junc14__v_mm3_s": VV_junc14__v_mm3_s,
        "VV_junc14__junction_type": VV_junc14__junction_type,
        "VV_junc14__is_split": VV_junc14__is_split,
        "VV_junc14__is_merge": VV_junc14__is_merge,
        "VV_junc14__feed1": VV_junc14__feed1,
        "VV_junc14__feed2": VV_junc14__feed2,
        "VV_junc14__feed3": VV_junc14__feed3,
        "VV_junc14__feed4": VV_junc14__feed4,
        "VV_junc14__alpha1": VV_junc14__alpha1,
        "VV_junc14__alpha2": VV_junc14__alpha2,
        "VV_junc14__alpha3": VV_junc14__alpha3,
        "VV_junc14__alpha4": VV_junc14__alpha4,
        "VV_junc14__Qout1_rem": VV_junc14__Qout1_rem,
        "VV_junc14__Qout2_rem": VV_junc14__Qout2_rem,
        "VV_junc14__Qout3_rem": VV_junc14__Qout3_rem,
        "VV_junc14__Qout4_rem": VV_junc14__Qout4_rem,
        "VV_junc14__beta1": VV_junc14__beta1,
        "VV_junc14__beta2": VV_junc14__beta2,
        "VV_junc14__beta3": VV_junc14__beta3,
        "VV_junc14__beta4": VV_junc14__beta4,
        "VV_junc14__D_F": VV_junc14__D_F,
        "VV_junc14__D_alpha": VV_junc14__D_alpha,
        "VV_junc14__D_beta": VV_junc14__D_beta,
        "VV_junc14__v_alpha": VV_junc14__v_alpha,
        "VV_junc14__v_beta": VV_junc14__v_beta,
        "PV27__H_down_target": PV27__H_down_target,
        "PV28__H_down_target": PV28__H_down_target,
        "V27__H_down_target": V27__H_down_target,
        "V28__H_down_target": V28__H_down_target,
        "VV_junc15__n_in": VV_junc15__n_in,
        "VV_junc15__n_out": VV_junc15__n_out,
        "VV_junc15__RBC_in": VV_junc15__RBC_in,
        "VV_junc15__v_mm3_s": VV_junc15__v_mm3_s,
        "VV_junc15__junction_type": VV_junc15__junction_type,
        "VV_junc15__is_split": VV_junc15__is_split,
        "VV_junc15__is_merge": VV_junc15__is_merge,
        "VV_junc15__feed1": VV_junc15__feed1,
        "VV_junc15__feed2": VV_junc15__feed2,
        "VV_junc15__feed3": VV_junc15__feed3,
        "VV_junc15__feed4": VV_junc15__feed4,
        "VV_junc15__alpha1": VV_junc15__alpha1,
        "VV_junc15__alpha2": VV_junc15__alpha2,
        "VV_junc15__alpha3": VV_junc15__alpha3,
        "VV_junc15__alpha4": VV_junc15__alpha4,
        "VV_junc15__Qout1_rem": VV_junc15__Qout1_rem,
        "VV_junc15__Qout2_rem": VV_junc15__Qout2_rem,
        "VV_junc15__Qout3_rem": VV_junc15__Qout3_rem,
        "VV_junc15__Qout4_rem": VV_junc15__Qout4_rem,
        "VV_junc15__beta1": VV_junc15__beta1,
        "VV_junc15__beta2": VV_junc15__beta2,
        "VV_junc15__beta3": VV_junc15__beta3,
        "VV_junc15__beta4": VV_junc15__beta4,
        "VV_junc15__D_F": VV_junc15__D_F,
        "VV_junc15__D_alpha": VV_junc15__D_alpha,
        "VV_junc15__D_beta": VV_junc15__D_beta,
        "VV_junc15__v_alpha": VV_junc15__v_alpha,
        "VV_junc15__v_beta": VV_junc15__v_beta,
        "PV29__H_down_target": PV29__H_down_target,
        "PV30__H_down_target": PV30__H_down_target,
        "V29__H_down_target": V29__H_down_target,
        "V30__H_down_target": V30__H_down_target,
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
        "V7__H_down_target": V7__H_down_target,
        "V8__H_down_target": V8__H_down_target,
        "VV_junc5__FQB_alpha": VV_junc5__FQB_alpha,
        "VV_junc5__B": VV_junc5__B,
        "VV_junc5__A": VV_junc5__A,
        "VV_junc5__X_0": VV_junc5__X_0,
        "VV_junc5__y_raw": VV_junc5__y_raw,
        "VV_junc5__y": VV_junc5__y,
        "V9__H_down_target": V9__H_down_target,
        "V10__H_down_target": V10__H_down_target,
        "VV_junc6__FQB_alpha": VV_junc6__FQB_alpha,
        "VV_junc6__B": VV_junc6__B,
        "VV_junc6__A": VV_junc6__A,
        "VV_junc6__X_0": VV_junc6__X_0,
        "VV_junc6__y_raw": VV_junc6__y_raw,
        "VV_junc6__y": VV_junc6__y,
        "V11__H_down_target": V11__H_down_target,
        "V12__H_down_target": V12__H_down_target,
        "VV_junc7__FQB_alpha": VV_junc7__FQB_alpha,
        "VV_junc7__B": VV_junc7__B,
        "VV_junc7__A": VV_junc7__A,
        "VV_junc7__X_0": VV_junc7__X_0,
        "VV_junc7__y_raw": VV_junc7__y_raw,
        "VV_junc7__y": VV_junc7__y,
        "V13__H_down_target": V13__H_down_target,
        "V14__H_down_target": V14__H_down_target,
        "VV_junc8__FQB_alpha": VV_junc8__FQB_alpha,
        "VV_junc8__B": VV_junc8__B,
        "VV_junc8__A": VV_junc8__A,
        "VV_junc8__X_0": VV_junc8__X_0,
        "VV_junc8__y_raw": VV_junc8__y_raw,
        "VV_junc8__y": VV_junc8__y,
        "VV_junc9__FQB_alpha": VV_junc9__FQB_alpha,
        "VV_junc9__B": VV_junc9__B,
        "VV_junc9__A": VV_junc9__A,
        "VV_junc9__X_0": VV_junc9__X_0,
        "VV_junc9__y_raw": VV_junc9__y_raw,
        "VV_junc9__y": VV_junc9__y,
        "VV_junc10__FQB_alpha": VV_junc10__FQB_alpha,
        "VV_junc10__B": VV_junc10__B,
        "VV_junc10__A": VV_junc10__A,
        "VV_junc10__X_0": VV_junc10__X_0,
        "VV_junc10__y_raw": VV_junc10__y_raw,
        "VV_junc10__y": VV_junc10__y,
        "VV_junc11__FQB_alpha": VV_junc11__FQB_alpha,
        "VV_junc11__B": VV_junc11__B,
        "VV_junc11__A": VV_junc11__A,
        "VV_junc11__X_0": VV_junc11__X_0,
        "VV_junc11__y_raw": VV_junc11__y_raw,
        "VV_junc11__y": VV_junc11__y,
        "VV_junc12__FQB_alpha": VV_junc12__FQB_alpha,
        "VV_junc12__B": VV_junc12__B,
        "VV_junc12__A": VV_junc12__A,
        "VV_junc12__X_0": VV_junc12__X_0,
        "VV_junc12__y_raw": VV_junc12__y_raw,
        "VV_junc12__y": VV_junc12__y,
        "VV_junc13__FQB_alpha": VV_junc13__FQB_alpha,
        "VV_junc13__B": VV_junc13__B,
        "VV_junc13__A": VV_junc13__A,
        "VV_junc13__X_0": VV_junc13__X_0,
        "VV_junc13__y_raw": VV_junc13__y_raw,
        "VV_junc13__y": VV_junc13__y,
        "VV_junc14__FQB_alpha": VV_junc14__FQB_alpha,
        "VV_junc14__B": VV_junc14__B,
        "VV_junc14__A": VV_junc14__A,
        "VV_junc14__X_0": VV_junc14__X_0,
        "VV_junc14__y_raw": VV_junc14__y_raw,
        "VV_junc14__y": VV_junc14__y,
        "VV_junc15__FQB_alpha": VV_junc15__FQB_alpha,
        "VV_junc15__B": VV_junc15__B,
        "VV_junc15__A": VV_junc15__A,
        "VV_junc15__X_0": VV_junc15__X_0,
        "VV_junc15__y_raw": VV_junc15__y_raw,
        "VV_junc15__y": VV_junc15__y,
        "VV_junc1__ph": VV_junc1__ph,
        "VV_junc2__ph": VV_junc2__ph,
        "VV_junc3__ph": VV_junc3__ph,
        "VV_junc4__ph": VV_junc4__ph,
        "VV_junc5__ph": VV_junc5__ph,
        "VV_junc6__ph": VV_junc6__ph,
        "VV_junc7__ph": VV_junc7__ph,
        "VV_junc8__ph": VV_junc8__ph,
        "VV_junc9__ph": VV_junc9__ph,
        "VV_junc10__ph": VV_junc10__ph,
        "VV_junc11__ph": VV_junc11__ph,
        "VV_junc12__ph": VV_junc12__ph,
        "VV_junc13__ph": VV_junc13__ph,
        "VV_junc14__ph": VV_junc14__ph,
        "VV_junc15__ph": VV_junc15__ph,
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
        "VV_junc8__FQE_alpha": VV_junc8__FQE_alpha,
        "VV_junc8__H_VV_out_alpha": VV_junc8__H_VV_out_alpha,
        "VV_junc8__H_VV_out_beta": VV_junc8__H_VV_out_beta,
        "VV_junc8__H_split1": VV_junc8__H_split1,
        "VV_junc8__H_split2": VV_junc8__H_split2,
        "VV_junc8__H_split3": VV_junc8__H_split3,
        "VV_junc8__H_split4": VV_junc8__H_split4,
        "VV_junc8__H_daughter1": VV_junc8__H_daughter1,
        "VV_junc8__H_daughter2": VV_junc8__H_daughter2,
        "VV_junc8__H_daughter3": VV_junc8__H_daughter3,
        "VV_junc8__H_daughter4": VV_junc8__H_daughter4,
        "VV_junc8__H_from1_target": VV_junc8__H_from1_target,
        "VV_junc8__H_from2_target": VV_junc8__H_from2_target,
        "VV_junc8__H_from3_target": VV_junc8__H_from3_target,
        "VV_junc8__H_from4_target": VV_junc8__H_from4_target,
        "VV_junc9__FQE_alpha": VV_junc9__FQE_alpha,
        "VV_junc9__H_VV_out_alpha": VV_junc9__H_VV_out_alpha,
        "VV_junc9__H_VV_out_beta": VV_junc9__H_VV_out_beta,
        "VV_junc9__H_split1": VV_junc9__H_split1,
        "VV_junc9__H_split2": VV_junc9__H_split2,
        "VV_junc9__H_split3": VV_junc9__H_split3,
        "VV_junc9__H_split4": VV_junc9__H_split4,
        "VV_junc9__H_daughter1": VV_junc9__H_daughter1,
        "VV_junc9__H_daughter2": VV_junc9__H_daughter2,
        "VV_junc9__H_daughter3": VV_junc9__H_daughter3,
        "VV_junc9__H_daughter4": VV_junc9__H_daughter4,
        "VV_junc9__H_from1_target": VV_junc9__H_from1_target,
        "VV_junc9__H_from2_target": VV_junc9__H_from2_target,
        "VV_junc9__H_from3_target": VV_junc9__H_from3_target,
        "VV_junc9__H_from4_target": VV_junc9__H_from4_target,
        "VV_junc10__FQE_alpha": VV_junc10__FQE_alpha,
        "VV_junc10__H_VV_out_alpha": VV_junc10__H_VV_out_alpha,
        "VV_junc10__H_VV_out_beta": VV_junc10__H_VV_out_beta,
        "VV_junc10__H_split1": VV_junc10__H_split1,
        "VV_junc10__H_split2": VV_junc10__H_split2,
        "VV_junc10__H_split3": VV_junc10__H_split3,
        "VV_junc10__H_split4": VV_junc10__H_split4,
        "VV_junc10__H_daughter1": VV_junc10__H_daughter1,
        "VV_junc10__H_daughter2": VV_junc10__H_daughter2,
        "VV_junc10__H_daughter3": VV_junc10__H_daughter3,
        "VV_junc10__H_daughter4": VV_junc10__H_daughter4,
        "VV_junc10__H_from1_target": VV_junc10__H_from1_target,
        "VV_junc10__H_from2_target": VV_junc10__H_from2_target,
        "VV_junc10__H_from3_target": VV_junc10__H_from3_target,
        "VV_junc10__H_from4_target": VV_junc10__H_from4_target,
        "VV_junc11__FQE_alpha": VV_junc11__FQE_alpha,
        "VV_junc11__H_VV_out_alpha": VV_junc11__H_VV_out_alpha,
        "VV_junc11__H_VV_out_beta": VV_junc11__H_VV_out_beta,
        "VV_junc11__H_split1": VV_junc11__H_split1,
        "VV_junc11__H_split2": VV_junc11__H_split2,
        "VV_junc11__H_split3": VV_junc11__H_split3,
        "VV_junc11__H_split4": VV_junc11__H_split4,
        "VV_junc11__H_daughter1": VV_junc11__H_daughter1,
        "VV_junc11__H_daughter2": VV_junc11__H_daughter2,
        "VV_junc11__H_daughter3": VV_junc11__H_daughter3,
        "VV_junc11__H_daughter4": VV_junc11__H_daughter4,
        "VV_junc11__H_from1_target": VV_junc11__H_from1_target,
        "VV_junc11__H_from2_target": VV_junc11__H_from2_target,
        "VV_junc11__H_from3_target": VV_junc11__H_from3_target,
        "VV_junc11__H_from4_target": VV_junc11__H_from4_target,
        "VV_junc12__FQE_alpha": VV_junc12__FQE_alpha,
        "VV_junc12__H_VV_out_alpha": VV_junc12__H_VV_out_alpha,
        "VV_junc12__H_VV_out_beta": VV_junc12__H_VV_out_beta,
        "VV_junc12__H_split1": VV_junc12__H_split1,
        "VV_junc12__H_split2": VV_junc12__H_split2,
        "VV_junc12__H_split3": VV_junc12__H_split3,
        "VV_junc12__H_split4": VV_junc12__H_split4,
        "VV_junc12__H_daughter1": VV_junc12__H_daughter1,
        "VV_junc12__H_daughter2": VV_junc12__H_daughter2,
        "VV_junc12__H_daughter3": VV_junc12__H_daughter3,
        "VV_junc12__H_daughter4": VV_junc12__H_daughter4,
        "VV_junc12__H_from1_target": VV_junc12__H_from1_target,
        "VV_junc12__H_from2_target": VV_junc12__H_from2_target,
        "VV_junc12__H_from3_target": VV_junc12__H_from3_target,
        "VV_junc12__H_from4_target": VV_junc12__H_from4_target,
        "VV_junc13__FQE_alpha": VV_junc13__FQE_alpha,
        "VV_junc13__H_VV_out_alpha": VV_junc13__H_VV_out_alpha,
        "VV_junc13__H_VV_out_beta": VV_junc13__H_VV_out_beta,
        "VV_junc13__H_split1": VV_junc13__H_split1,
        "VV_junc13__H_split2": VV_junc13__H_split2,
        "VV_junc13__H_split3": VV_junc13__H_split3,
        "VV_junc13__H_split4": VV_junc13__H_split4,
        "VV_junc13__H_daughter1": VV_junc13__H_daughter1,
        "VV_junc13__H_daughter2": VV_junc13__H_daughter2,
        "VV_junc13__H_daughter3": VV_junc13__H_daughter3,
        "VV_junc13__H_daughter4": VV_junc13__H_daughter4,
        "VV_junc13__H_from1_target": VV_junc13__H_from1_target,
        "VV_junc13__H_from2_target": VV_junc13__H_from2_target,
        "VV_junc13__H_from3_target": VV_junc13__H_from3_target,
        "VV_junc13__H_from4_target": VV_junc13__H_from4_target,
        "VV_junc14__FQE_alpha": VV_junc14__FQE_alpha,
        "VV_junc14__H_VV_out_alpha": VV_junc14__H_VV_out_alpha,
        "VV_junc14__H_VV_out_beta": VV_junc14__H_VV_out_beta,
        "VV_junc14__H_split1": VV_junc14__H_split1,
        "VV_junc14__H_split2": VV_junc14__H_split2,
        "VV_junc14__H_split3": VV_junc14__H_split3,
        "VV_junc14__H_split4": VV_junc14__H_split4,
        "VV_junc14__H_daughter1": VV_junc14__H_daughter1,
        "VV_junc14__H_daughter2": VV_junc14__H_daughter2,
        "VV_junc14__H_daughter3": VV_junc14__H_daughter3,
        "VV_junc14__H_daughter4": VV_junc14__H_daughter4,
        "VV_junc14__H_from1_target": VV_junc14__H_from1_target,
        "VV_junc14__H_from2_target": VV_junc14__H_from2_target,
        "VV_junc14__H_from3_target": VV_junc14__H_from3_target,
        "VV_junc14__H_from4_target": VV_junc14__H_from4_target,
        "VV_junc15__FQE_alpha": VV_junc15__FQE_alpha,
        "VV_junc15__H_VV_out_alpha": VV_junc15__H_VV_out_alpha,
        "VV_junc15__H_VV_out_beta": VV_junc15__H_VV_out_beta,
        "VV_junc15__H_split1": VV_junc15__H_split1,
        "VV_junc15__H_split2": VV_junc15__H_split2,
        "VV_junc15__H_split3": VV_junc15__H_split3,
        "VV_junc15__H_split4": VV_junc15__H_split4,
        "VV_junc15__H_daughter1": VV_junc15__H_daughter1,
        "VV_junc15__H_daughter2": VV_junc15__H_daughter2,
        "VV_junc15__H_daughter3": VV_junc15__H_daughter3,
        "VV_junc15__H_daughter4": VV_junc15__H_daughter4,
        "VV_junc15__H_from1_target": VV_junc15__H_from1_target,
        "VV_junc15__H_from2_target": VV_junc15__H_from2_target,
        "VV_junc15__H_from3_target": VV_junc15__H_from3_target,
        "VV_junc15__H_from4_target": VV_junc15__H_from4_target,
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
        "VV_junc8__H_from1": VV_junc8__H_from1,
        "VV_junc8__H_from2": VV_junc8__H_from2,
        "VV_junc8__H_from3": VV_junc8__H_from3,
        "VV_junc8__H_from4": VV_junc8__H_from4,
        "VV_junc8__RBC_out": VV_junc8__RBC_out,
        "VV_junc9__H_from1": VV_junc9__H_from1,
        "VV_junc9__H_from2": VV_junc9__H_from2,
        "VV_junc9__H_from3": VV_junc9__H_from3,
        "VV_junc9__H_from4": VV_junc9__H_from4,
        "VV_junc9__RBC_out": VV_junc9__RBC_out,
        "VV_junc10__H_from1": VV_junc10__H_from1,
        "VV_junc10__H_from2": VV_junc10__H_from2,
        "VV_junc10__H_from3": VV_junc10__H_from3,
        "VV_junc10__H_from4": VV_junc10__H_from4,
        "VV_junc10__RBC_out": VV_junc10__RBC_out,
        "VV_junc11__H_from1": VV_junc11__H_from1,
        "VV_junc11__H_from2": VV_junc11__H_from2,
        "VV_junc11__H_from3": VV_junc11__H_from3,
        "VV_junc11__H_from4": VV_junc11__H_from4,
        "VV_junc11__RBC_out": VV_junc11__RBC_out,
        "VV_junc12__H_from1": VV_junc12__H_from1,
        "VV_junc12__H_from2": VV_junc12__H_from2,
        "VV_junc12__H_from3": VV_junc12__H_from3,
        "VV_junc12__H_from4": VV_junc12__H_from4,
        "VV_junc12__RBC_out": VV_junc12__RBC_out,
        "VV_junc13__H_from1": VV_junc13__H_from1,
        "VV_junc13__H_from2": VV_junc13__H_from2,
        "VV_junc13__H_from3": VV_junc13__H_from3,
        "VV_junc13__H_from4": VV_junc13__H_from4,
        "VV_junc13__RBC_out": VV_junc13__RBC_out,
        "VV_junc14__H_from1": VV_junc14__H_from1,
        "VV_junc14__H_from2": VV_junc14__H_from2,
        "VV_junc14__H_from3": VV_junc14__H_from3,
        "VV_junc14__H_from4": VV_junc14__H_from4,
        "VV_junc14__RBC_out": VV_junc14__RBC_out,
        "VV_junc15__H_from1": VV_junc15__H_from1,
        "VV_junc15__H_from2": VV_junc15__H_from2,
        "VV_junc15__H_from3": VV_junc15__H_from3,
        "VV_junc15__H_from4": VV_junc15__H_from4,
        "VV_junc15__RBC_out": VV_junc15__RBC_out,
    }