"""Generated model"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
PV1__C = 2.553742846887937e-23
PV1__H_global_L = 0.45
PV1__H_global_R = 0.45
PV1__R = 1000000000000000.0
PV1__RBC_volume_init = 7.634070148223191e-16
PV1__R_constriction_base = 0.0
PV1__R_constriction_final = 0.0
PV1__Z = -1.1820960009520325
PV1__div_0 = 1e-25
PV1__div_0y = 1e-08
PV1__gamma_mirror = 0.1
PV1__k = 1000.0
PV1__l = 0.000015
PV1__mu_45 = 3.5523629350190156
PV1__mu_plasma = 0.001
PV1__one_mm3 = 1e-09
PV1__q_C_init = 0.0
PV1__q_us = 1.696460032938487e-15
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
PV1__v_threshold = 1e-18
PV2__C = 2.553742846887937e-23
PV2__H_global_L = 0.45
PV2__H_global_R = 0.45
PV2__R = 1000000000000000.0
PV2__RBC_volume_init = 7.634070148223191e-16
PV2__R_constriction_base = 0.0
PV2__R_constriction_final = 0.0
PV2__Z = -1.1820960009520325
PV2__div_0 = 1e-25
PV2__div_0y = 1e-08
PV2__gamma_mirror = 0.1
PV2__k = 1000.0
PV2__l = 0.000015
PV2__mu_45 = 3.5523629350190156
PV2__mu_plasma = 0.001
PV2__one_mm3 = 1e-09
PV2__q_C_init = 0.0
PV2__q_us = 1.696460032938487e-15
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
PV2__v_threshold = 1e-18
V1__C = 4.256238078146562e-22
V1__H_L_out_RHS = 0.45
V1__H_global_L = 0.45
V1__H_global_R = 0.45
V1__R = 1000000000000000.0
V1__RBC_volume_init = 1.0691232499247755e-14
V1__R_constriction_base = 0.0
V1__Z = -1.1691201400706768
V1__div_0 = 1e-25
V1__div_0y = 1e-08
V1__gamma_mirror = 0.1
V1__k = 1000.0
V1__l = 0.00025
V1__mu_45 = 3.71461005007079
V1__mu_plasma = 0.001
V1__one_mm3 = 1e-09
V1__q_C_init = 0.0
V1__q_us = 2.3758294442772788e-14
V1__r = 5.5e-06
V1__t0 = 500.0
V1__tau_H_down = 0.001
V1__tau_H_mean = 0.001
V1__tau_junc = 0.0001
V1__tau_link = 0.001
V1__tau_sig = 1.0
V1__u_ext = 133.0
V1__u_out = 6632.7695
V1__v_eps = 1e-30
V1__v_scale = 1e-50
V1__v_threshold = 1e-18
V2__C = 4.256238078146562e-22
V2__H_L_out_RHS = 0.45
V2__H_global_L = 0.45
V2__H_global_R = 0.45
V2__R = 1000000000000000.0
V2__RBC_volume_init = 1.0691232499247755e-14
V2__R_constriction_base = 0.0
V2__Z = -1.1691201400706768
V2__div_0 = 1e-25
V2__div_0y = 1e-08
V2__gamma_mirror = 0.1
V2__k = 1000.0
V2__l = 0.00025
V2__mu_45 = 3.71461005007079
V2__mu_plasma = 0.001
V2__one_mm3 = 1e-09
V2__q_C_init = 0.0
V2__q_us = 2.3758294442772788e-14
V2__r = 5.5e-06
V2__t0 = 500.0
V2__tau_H_down = 0.001
V2__tau_H_mean = 0.001
V2__tau_junc = 0.0001
V2__tau_link = 0.001
V2__tau_sig = 1.0
V2__u_ext = 133.0
V2__u_out = 6632.7695
V2__v_eps = 1e-30
V2__v_scale = 1e-50
V2__v_threshold = 1e-18
VV_junc1__C = 8.51e-22
VV_junc1__C_conn2 = 8.51e-22
VV_junc1__C_max12 = 8.51e-22
VV_junc1__C_max123 = 8.51e-22
VV_junc1__D1 = 1.2e-05
VV_junc1__D2 = 0.0
VV_junc1__D3 = 1.2e-05
VV_junc1__D4 = 1.2e-05
VV_junc1__H_global_L = 0.45
VV_junc1__H_global_R = 0.45
VV_junc1__H_to2 = 0.0
VV_junc1__Qin2 = 0.0
VV_junc1__Qout2 = -0.0
VV_junc1__R = 1000000000000000.0
VV_junc1__RBC_volume_init = 5.08938009881546e-17
VV_junc1__R_constriction_base = 0.0
VV_junc1__bc2_is_in = 0.0
VV_junc1__bc2_is_out = 0.0
VV_junc1__div_0 = 1e-25
VV_junc1__div_0y = 1e-08
VV_junc1__gamma_mirror = 0.1
VV_junc1__k = 1000.0
VV_junc1__l = 0.000001
VV_junc1__mu_plasma = 0.001
VV_junc1__one_mm3 = 1e-09
VV_junc1__q_C_init = 0.0
VV_junc1__q_us = 1.1309733552923245e-16
VV_junc1__r = 6e-06
VV_junc1__r_bc2 = 0.0
VV_junc1__t0 = 500.0
VV_junc1__tau_H_down = 0.001
VV_junc1__tau_H_mean = 0.001
VV_junc1__tau_junc = 0.0001
VV_junc1__tau_link = 0.001
VV_junc1__tau_sig = 1.0
VV_junc1__u_ext = 133.0
VV_junc1__v_eps = 1e-30
VV_junc1__v_scale = 1e-50
VV_junc1__v_threshold = 1e-18
VV_junc1__vbc2 = 0.0
VV_junc1__vj2 = 0.0
VV_junc1__w_in2 = 0.5
VV_junc1__w_out2 = 0.5
global__H_global_L = 0.45
global__H_global_R = 0.45
global__R = 1000000000000000.0
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
inlet__C = 5.107485693775874e-22
inlet__H_R_out_LHS = 0.45
inlet__H_global_L = 0.45
inlet__H_global_R = 0.45
inlet__R = 1000000000000000.0
inlet__RBC_volume_init = 1.5268140296446382e-14
inlet__R_constriction_base = 0.0
inlet__Z = -1.1820960009520325
inlet__div_0 = 1e-25
inlet__div_0y = 1e-08
inlet__gamma_mirror = 0.1
inlet__k = 1000.0
inlet__l = 0.0003
inlet__mu_45 = 3.5523629350190156
inlet__mu_plasma = 0.001
inlet__one_mm3 = 1e-09
inlet__q_C_init = 0.0
inlet__q_us = 3.392920065876973e-14
inlet__r = 6e-06
inlet__t0 = 500.0
inlet__tau_H_down = 0.001
inlet__tau_H_mean = 0.001
inlet__tau_junc = 0.0001
inlet__tau_link = 0.001
inlet__tau_sig = 1.0
inlet__u_ext = 133.0
inlet__u_in = 6666.1
inlet__v_eps = 1e-30
inlet__v_scale = 1e-50
inlet__v_threshold = 1e-18

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
]

# Initial conditions
y0 = np.array([
    -1.9984014885135946e-16,
    0.45,
    0.45000000994816686,
    1.5269640297159772e-14,
    3.3326531138933488e-18,
    5.0899981016906383e-17,
    2.7729721054424635e-18,
    2.7701283341496695e-18,
    0.45066594907900703,
    0.45005807512155366,
    0.45066415426369355,
    7.645137146985757e-16,
    1.6625090353096748e-19,
    0.4506660141504298,
    0.45005807347727317,
    0.4506642190463343,
    7.645138141429107e-16,
    1.662509035300436e-19,
    0.45,
    0.45066506738583584,
    0.4499375638693855,
    1.0692571610648219e-14,
    2.7707624254559425e-18,
    0.45,
    0.4506651323127141,
    0.4499375579201643,
    1.0692571622937236e-14,
    2.770762425425145e-18,
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

    # Algebraic equations
    inlet__w_v = 0.5+1/np.pi*np.arctan(inlet__v/V2__v_scale)
    inlet__w_v_d = 0.5+1/np.pi*np.arctan(inlet__v_d/V2__v_scale)
    inlet__H_L_in = inlet__H_link_L
    inlet__H_R_in = inlet__H_link_R
    inlet__H_up = inlet__w_v_d*inlet__H_L_in+(1-inlet__w_v_d)*inlet__H_R_in
    inlet__H_down_target = inlet__s_v_d*(inlet__H_mean+V2__gamma_mirror*(inlet__H_mean-inlet__H_up))+(1-inlet__s_v_d)*inlet__H_mean
    inlet__s_v_d = np.abs(inlet__v_d)/(np.abs(inlet__v_d)+V2__v_eps)
    inlet__H_L_out = (1-inlet__w_v_d)*inlet__H_down+inlet__w_v_d*inlet__H_L_in
    inlet__H_R_out = inlet__w_v_d*inlet__H_down+(1-inlet__w_v_d)*inlet__H_R_in
    inlet__RBC_volume_init = V2__H_global_L*inlet__q_us
    inlet__v_pos = inlet__w_v*inlet__v
    inlet__v_neg = (1-inlet__w_v)*-inlet__v
    inlet__v_d_pos = inlet__w_v_d*inlet__v_d
    inlet__v_d_neg = (1-inlet__w_v_d)*-inlet__v_d
    inlet__H_mean = inlet__RBC_volume/inlet__q
    inlet__H_mass_L = inlet__w_v*inlet__H_L_in+(1-inlet__w_v)*inlet__H_L_out
    inlet__H_mass_R = inlet__w_v_d*inlet__H_R_out+(1-inlet__w_v_d)*inlet__H_R_in
    inlet__q = inlet__q_us+inlet__q_C
    inlet__Z = (0.8+np.exp(-0.075*2*inlet__r*1e6))*(-1+1/(1+np.power(10.0, -11)*np.power(2*inlet__r*1e6, 12)))+1/(1+np.power(10.0, -11)*np.power(2*inlet__r*1e6, 12))
    inlet__mu_45 = 6*np.exp(-0.085*2*inlet__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*inlet__r*1e6, 0.645))
    inlet__mu = inlet__hem_dep_u_rel*V2__mu_plasma
    inlet__hem_dep_u_rel = 1+(inlet__mu_45-1)*(np.power(1-inlet__H_mean, inlet__Z)-1)/(np.power(1-V2__H_global_L, inlet__Z)-1)*np.square(2*inlet__r*1e6/(2*inlet__r*1e6-1.1))
    inlet__v_mm3_s = inlet__v/V2__one_mm3
    inlet__v = (inlet__u_in-inlet__u)/(inlet__R/2)
    inlet__u_mmHg = inlet__u/133.322
    inlet__u = inlet__q_C/inlet__C+V2__u_ext
    inlet__v_d_mm3_s = inlet__v_d/V2__one_mm3
    inlet__v_d = (inlet__u-VV_junc1__u)/(inlet__R/2)
    VV_junc1__vj1 = inlet__v_d
    VV_junc1__vj2 = VV_junc1__vbc2
    VV_junc1__vj3 = -PV1__v
    VV_junc1__vj4 = -PV2__v
    VV_junc1__H_from1 = VV_junc1__w_out1*VV_junc1__H_from1_target
    VV_junc1__H_from2 = VV_junc1__w_out2*VV_junc1__H_from2_target
    VV_junc1__H_from3 = VV_junc1__w_out3*VV_junc1__H_from3_target
    VV_junc1__H_from4 = VV_junc1__w_out4*VV_junc1__H_from4_target
    VV_junc1__D1 = 2*inlet__r
    VV_junc1__D2 = 2*VV_junc1__r_bc2
    VV_junc1__D3 = 2*PV1__r
    VV_junc1__D4 = 2*PV2__r
    VV_junc1__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc1__vj1/V2__v_scale)
    VV_junc1__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc1__vj2/V2__v_scale)
    VV_junc1__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc1__vj3/V2__v_scale)
    VV_junc1__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc1__vj4/V2__v_scale)
    VV_junc1__w_out1 = 1-VV_junc1__w_in1
    VV_junc1__w_out2 = 1-VV_junc1__w_in2
    VV_junc1__w_out3 = 1-VV_junc1__w_in3
    VV_junc1__w_out4 = 1-VV_junc1__w_in4
    VV_junc1__Qin1 = VV_junc1__w_in1*VV_junc1__vj1
    VV_junc1__Qin2 = VV_junc1__w_in2*VV_junc1__vj2
    VV_junc1__Qin3 = VV_junc1__w_in3*VV_junc1__vj3
    VV_junc1__Qin4 = VV_junc1__w_in4*VV_junc1__vj4
    VV_junc1__Qout1 = VV_junc1__w_out1*-VV_junc1__vj1
    VV_junc1__Qout2 = VV_junc1__w_out2*-VV_junc1__vj2
    VV_junc1__Qout3 = VV_junc1__w_out3*-VV_junc1__vj3
    VV_junc1__Qout4 = VV_junc1__w_out4*-VV_junc1__vj4
    VV_junc1__Qin_tot = VV_junc1__Qin1+VV_junc1__Qin2+VV_junc1__Qin3+VV_junc1__Qin4
    VV_junc1__Qout_tot = VV_junc1__Qout1+VV_junc1__Qout2+VV_junc1__Qout3+VV_junc1__Qout4
    VV_junc1__n_in = VV_junc1__bc1_is_in+VV_junc1__bc2_is_in+VV_junc1__bc3_is_in+VV_junc1__bc4_is_in
    VV_junc1__n_out = VV_junc1__bc1_is_out+VV_junc1__bc2_is_out+VV_junc1__bc3_is_out+VV_junc1__bc4_is_out
    VV_junc1__FQB_alpha = (VV_junc1__v_alpha+VV_junc1__div_0)/(VV_junc1__v_alpha+VV_junc1__v_beta+2*VV_junc1__div_0)
    VV_junc1__FQE_alpha = 1/(1+np.exp(-(VV_junc1__A+VV_junc1__B*VV_junc1__ph)))
    VV_junc1__B = 1+6.98*(1-VV_junc1__H_mean)/(VV_junc1__D_F*1e6)
    VV_junc1__A = -6.96*np.log(VV_junc1__D_alpha*1e6/(VV_junc1__D_beta*1e6))/(VV_junc1__D_F*1e6)
    VV_junc1__X_0 = 0.4/(VV_junc1__D_F*1e6)
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))
    VV_junc1__y_raw = (VV_junc1__FQB_alpha-VV_junc1__X_0)/(1-2*VV_junc1__X_0+VV_junc1__div_0)
    VV_junc1__y = min(max(VV_junc1__y_raw, VV_junc1__div_0y), 1-VV_junc1__div_0y)
    VV_junc1__H_VV_out_alpha = VV_junc1__H_mean*VV_junc1__FQE_alpha/(VV_junc1__FQB_alpha+VV_junc1__div_0)
    VV_junc1__H_VV_out_beta = VV_junc1__H_mean*(1-VV_junc1__FQE_alpha)/(1-VV_junc1__FQB_alpha+VV_junc1__div_0)
    VV_junc1__RBC_in = VV_junc1__Qin1*inlet__H_R_out+VV_junc1__Qin2*VV_junc1__H_to2+VV_junc1__Qin3*PV1__H_L_out+VV_junc1__Qin4*PV2__H_L_out
    VV_junc1__RBC_out = VV_junc1__Qout1*VV_junc1__H_from1+VV_junc1__Qout2*VV_junc1__H_from2+VV_junc1__Qout3*VV_junc1__H_from3+VV_junc1__Qout4*VV_junc1__H_from4
    VV_junc1__RBC_volume_init = V2__H_global_L*VV_junc1__q_us
    VV_junc1__H_mean = VV_junc1__RBC_volume/(VV_junc1__q_us+VV_junc1__div_0)
    VV_junc1__q = VV_junc1__q_us+VV_junc1__q_C+VV_junc1__q_C_d
    VV_junc1__v_mm3_s = VV_junc1__v/V2__one_mm3
    VV_junc1__u = VV_junc1__q_C/(VV_junc1__C/2)+V2__u_ext
    VV_junc1__u_mmHg = VV_junc1__u/133.322
    VV_junc1__v = (VV_junc1__u-VV_junc1__u_d)/VV_junc1__R
    VV_junc1__u_d = VV_junc1__q_C_d/(VV_junc1__C/2)+V2__u_ext
    VV_junc1__u_d_mmHg = VV_junc1__u_d/133.322
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
    VV_junc1__bc1_is_in = (1 if VV_junc1__Qin1 > VV_junc1__v_threshold else 0)
    VV_junc1__bc2_is_in = (1 if VV_junc1__Qin2 > VV_junc1__v_threshold else 0)
    VV_junc1__bc3_is_in = (1 if VV_junc1__Qin3 > VV_junc1__v_threshold else 0)
    VV_junc1__bc4_is_in = (1 if VV_junc1__Qin4 > VV_junc1__v_threshold else 0)
    VV_junc1__bc1_is_out = (1 if VV_junc1__Qout1 > VV_junc1__v_threshold else 0)
    VV_junc1__bc2_is_out = (1 if VV_junc1__Qout2 > VV_junc1__v_threshold else 0)
    VV_junc1__bc3_is_out = (1 if VV_junc1__Qout3 > VV_junc1__v_threshold else 0)
    VV_junc1__bc4_is_out = (1 if VV_junc1__Qout4 > VV_junc1__v_threshold else 0)
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
    VV_junc1__C_max12 = (inlet__C if inlet__C > VV_junc1__C_conn2 else (VV_junc1__C_conn2 if inlet__C <= VV_junc1__C_conn2 else 0.0))
    VV_junc1__C_max123 = (VV_junc1__C_max12 if VV_junc1__C_max12 > PV1__C else (PV1__C if VV_junc1__C_max12 <= PV1__C else 0.0))
    VV_junc1__C = (VV_junc1__C_max123 if VV_junc1__C_max123 > PV2__C else (PV2__C if VV_junc1__C_max123 <= PV2__C else 0.0))
    PV1__w_v = 0.5+1/np.pi*np.arctan(PV1__v/V2__v_scale)
    PV1__w_v_d = 0.5+1/np.pi*np.arctan(PV1__v_d/V2__v_scale)
    PV1__H_L_in = PV1__H_link_L
    PV1__H_R_in = PV1__H_link_R
    PV1__H_up = PV1__w_v_d*PV1__H_L_in+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__H_down_target = PV1__s_v_d*(PV1__H_mean+V2__gamma_mirror*(PV1__H_mean-PV1__H_up))+(1-PV1__s_v_d)*PV1__H_mean
    PV1__s_v_d = np.abs(PV1__v_d)/(np.abs(PV1__v_d)+V2__v_eps)
    PV1__H_L_out = (1-PV1__w_v_d)*PV1__H_down+PV1__w_v_d*PV1__H_L_in
    PV1__H_R_out = PV1__w_v_d*PV1__H_down+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__RBC_volume_init = V2__H_global_L*PV1__q_us
    PV1__v_pos = PV1__w_v*PV1__v
    PV1__v_neg = (1-PV1__w_v)*-PV1__v
    PV1__v_d_pos = PV1__w_v_d*PV1__v_d
    PV1__v_d_neg = (1-PV1__w_v_d)*-PV1__v_d
    PV1__H_mean = PV1__RBC_volume/PV1__q
    PV1__H_mass_L = PV1__w_v*PV1__H_L_in+(1-PV1__w_v)*PV1__H_L_out
    PV1__H_mass_R = PV1__w_v_d*PV1__H_R_out+(1-PV1__w_v_d)*PV1__H_R_in
    PV1__q = PV1__q_us+PV1__q_C
    PV1__Z = (0.8+np.exp(-0.075*2*PV1__r*1e6))*(-1+1/(1+np.power(10.0, -11)*np.power(2*PV1__r*1e6, 12)))+1/(1+np.power(10.0, -11)*np.power(2*PV1__r*1e6, 12))
    PV1__mu_45 = 6*np.exp(-0.085*2*PV1__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*PV1__r*1e6, 0.645))
    PV1__mu = PV1__hem_dep_u_rel*V2__mu_plasma
    PV1__hem_dep_u_rel = 1+(PV1__mu_45-1)*(np.power(1-PV1__H_mean, PV1__Z)-1)/(np.power(1-V2__H_global_L, PV1__Z)-1)*np.square(2*PV1__r*1e6/(2*PV1__r*1e6-1.1))
    PV1__v_mm3_s = PV1__v/V2__one_mm3
    PV1__v = (VV_junc1__u_d-PV1__u)/(PV1__R/2)
    PV1__u_mmHg = PV1__u/133.322
    PV1__u = PV1__q_C/PV1__C+V2__u_ext
    PV1__v_d_mm3_s = PV1__v_d/V2__one_mm3
    PV1__v_d = (PV1__u-V1__u)/(PV1__R/2)
    PV2__w_v = 0.5+1/np.pi*np.arctan(PV2__v/V2__v_scale)
    PV2__w_v_d = 0.5+1/np.pi*np.arctan(PV2__v_d/V2__v_scale)
    PV2__H_L_in = PV2__H_link_L
    PV2__H_R_in = PV2__H_link_R
    PV2__H_up = PV2__w_v_d*PV2__H_L_in+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__H_down_target = PV2__s_v_d*(PV2__H_mean+V2__gamma_mirror*(PV2__H_mean-PV2__H_up))+(1-PV2__s_v_d)*PV2__H_mean
    PV2__s_v_d = np.abs(PV2__v_d)/(np.abs(PV2__v_d)+V2__v_eps)
    PV2__H_L_out = (1-PV2__w_v_d)*PV2__H_down+PV2__w_v_d*PV2__H_L_in
    PV2__H_R_out = PV2__w_v_d*PV2__H_down+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__RBC_volume_init = V2__H_global_L*PV2__q_us
    PV2__v_pos = PV2__w_v*PV2__v
    PV2__v_neg = (1-PV2__w_v)*-PV2__v
    PV2__v_d_pos = PV2__w_v_d*PV2__v_d
    PV2__v_d_neg = (1-PV2__w_v_d)*-PV2__v_d
    PV2__H_mean = PV2__RBC_volume/PV2__q
    PV2__H_mass_L = PV2__w_v*PV2__H_L_in+(1-PV2__w_v)*PV2__H_L_out
    PV2__H_mass_R = PV2__w_v_d*PV2__H_R_out+(1-PV2__w_v_d)*PV2__H_R_in
    PV2__q = PV2__q_us+PV2__q_C
    PV2__Z = (0.8+np.exp(-0.075*2*PV2__r*1e6))*(-1+1/(1+np.power(10.0, -11)*np.power(2*PV2__r*1e6, 12)))+1/(1+np.power(10.0, -11)*np.power(2*PV2__r*1e6, 12))
    PV2__mu_45 = 6*np.exp(-0.085*2*PV2__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*PV2__r*1e6, 0.645))
    PV2__mu = PV2__hem_dep_u_rel*V2__mu_plasma
    PV2__hem_dep_u_rel = 1+(PV2__mu_45-1)*(np.power(1-PV2__H_mean, PV2__Z)-1)/(np.power(1-V2__H_global_L, PV2__Z)-1)*np.square(2*PV2__r*1e6/(2*PV2__r*1e6-1.1))
    PV2__v_mm3_s = PV2__v/V2__one_mm3
    PV2__v = (VV_junc1__u_d-PV2__u)/(PV2__R/2)
    PV2__u_mmHg = PV2__u/133.322
    PV2__u = PV2__q_C/PV2__C+V2__u_ext
    PV2__v_d_mm3_s = PV2__v_d/V2__one_mm3
    PV2__v_d = (PV2__u-V2__u)/(PV2__R/2)
    V1__w_v = 0.5+1/np.pi*np.arctan(V1__v/V2__v_scale)
    V1__H_L_in = V1__H_link_L
    V1__H_R_in = V1__H_link_R
    V1__H_up = V1__w_v*V1__H_L_in+(1-V1__w_v)*V1__H_R_in
    V1__H_down_target = V1__s_v*(V1__H_mean+V2__gamma_mirror*(V1__H_mean-V1__H_up))+(1-V1__s_v)*V1__H_mean
    V1__s_v = np.abs(V1__v)/(np.abs(V1__v)+V2__v_eps)
    V1__H_L_out = (1-V1__w_v)*V1__H_down+V1__w_v*V1__H_L_in
    V1__H_R_out = V1__w_v*V1__H_down+(1-V1__w_v)*V1__H_R_in
    V1__RBC_volume_init = V2__H_global_L*V1__q_us
    V1__v_pos = V1__w_v*V1__v
    V1__v_neg = (1-V1__w_v)*-V1__v
    V1__H_mean = V1__RBC_volume/V1__q
    V1__H_mass_L = V1__w_v*V1__H_L_in+(1-V1__w_v)*V1__H_L_out
    V1__H_mass_R = V1__w_v*V1__H_R_out+(1-V1__w_v)*V1__H_R_in
    V1__q = V1__q_us+V1__q_C
    V1__Z = (0.8+np.exp(-0.075*2*V1__r*1e6))*(-1+1/(1+np.power(10.0, -11)*np.power(2*V1__r*1e6, 12)))+1/(1+np.power(10.0, -11)*np.power(2*V1__r*1e6, 12))
    V1__mu_45 = 6*np.exp(-0.085*2*V1__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*V1__r*1e6, 0.645))
    V1__mu = V1__hem_dep_u_rel*V2__mu_plasma
    V1__hem_dep_u_rel = 1+(V1__mu_45-1)*(np.power(1-V1__H_mean, V1__Z)-1)/(np.power(1-V2__H_global_L, V1__Z)-1)*np.square(2*V1__r*1e6/(2*V1__r*1e6-1.1))
    V1__v_mm3_s = V1__v/V2__one_mm3
    V1__v = (V1__u-V1__u_out)/V1__R
    V1__u_mmHg = V1__u/133.322
    V1__u = V1__q_C/V1__C+V2__u_ext
    V2__w_v = 0.5+1/np.pi*np.arctan(V2__v/V2__v_scale)
    V2__H_L_in = V2__H_link_L
    V2__H_R_in = V2__H_link_R
    V2__H_up = V2__w_v*V2__H_L_in+(1-V2__w_v)*V2__H_R_in
    V2__H_down_target = V2__s_v*(V2__H_mean+V2__gamma_mirror*(V2__H_mean-V2__H_up))+(1-V2__s_v)*V2__H_mean
    V2__s_v = np.abs(V2__v)/(np.abs(V2__v)+V2__v_eps)
    V2__H_L_out = (1-V2__w_v)*V2__H_down+V2__w_v*V2__H_L_in
    V2__H_R_out = V2__w_v*V2__H_down+(1-V2__w_v)*V2__H_R_in
    V2__RBC_volume_init = V2__H_global_L*V2__q_us
    V2__v_pos = V2__w_v*V2__v
    V2__v_neg = (1-V2__w_v)*-V2__v
    V2__H_mean = V2__RBC_volume/V2__q
    V2__H_mass_L = V2__w_v*V2__H_L_in+(1-V2__w_v)*V2__H_L_out
    V2__H_mass_R = V2__w_v*V2__H_R_out+(1-V2__w_v)*V2__H_R_in
    V2__q = V2__q_us+V2__q_C
    V2__Z = (0.8+np.exp(-0.075*2*V2__r*1e6))*(-1+1/(1+np.power(10.0, -11)*np.power(2*V2__r*1e6, 12)))+1/(1+np.power(10.0, -11)*np.power(2*V2__r*1e6, 12))
    V2__mu_45 = 6*np.exp(-0.085*2*V2__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*V2__r*1e6, 0.645))
    V2__mu = V2__hem_dep_u_rel*V2__mu_plasma
    V2__hem_dep_u_rel = 1+(V2__mu_45-1)*(np.power(1-V2__H_mean, V2__Z)-1)/(np.power(1-V2__H_global_L, V2__Z)-1)*np.square(2*V2__r*1e6/(2*V2__r*1e6-1.1))
    V2__v_mm3_s = V2__v/V2__one_mm3
    V2__v = (V2__u-V2__u_out)/V2__R
    V2__u_mmHg = V2__u/133.322
    V2__u = V2__q_C/V2__C+V2__u_ext
    inlet__q_us = np.pi*np.square(inlet__r)*parameters__l_inlet
    inlet__C = np.pi*np.square(8.5e-9)*parameters__l_inlet/133.322
    inlet__R = 8*inlet__mu*parameters__l_inlet/(np.pi*np.power(inlet__r, 4))
    VV_junc1__q_us = np.pi*np.square(VV_junc1__r)*parameters__l_VV_junc1
    PV1__R_constriction = PV2__R_constriction_base+(PV1__R_constriction_final-PV2__R_constriction_base)/(1+np.exp(-(environment__time-PV2__t0)/PV2__tau_sig))
    PV1__q_us = np.pi*np.square(PV1__r)*parameters__l_PV1
    PV1__C = np.pi*np.square(8.5e-9)*parameters__l_PV1/133.322
    PV1__R = 8*PV1__mu*parameters__l_PV1/(np.pi*np.power(PV1__r, 4))+PV1__R_constriction
    PV2__R_constriction = PV2__R_constriction_base+(PV2__R_constriction_final-PV2__R_constriction_base)/(1+np.exp(-(environment__time-PV2__t0)/PV2__tau_sig))
    PV2__q_us = np.pi*np.square(PV2__r)*parameters__l_PV2
    PV2__C = np.pi*np.square(8.5e-9)*parameters__l_PV2/133.322
    PV2__R = 8*PV2__mu*parameters__l_PV2/(np.pi*np.power(PV2__r, 4))+PV2__R_constriction
    V1__q_us = np.pi*np.square(V1__r)*parameters__l_V1
    V1__C = np.pi*np.square(8.5e-9)*parameters__l_V1/133.322
    V1__R = 8*V1__mu*parameters__l_V1/(np.pi*np.power(V1__r, 4))
    V2__q_us = np.pi*np.square(V2__r)*parameters__l_V2
    V2__C = np.pi*np.square(8.5e-9)*parameters__l_V2/133.322
    V2__R = 8*V2__mu*parameters__l_V2/(np.pi*np.power(V2__r, 4))

    # ODEs
    dydt = np.zeros(len(y))
    dydt[0] = (VV_junc1__H_from1-inlet__H_link_R)/V2__tau_link
    dydt[1] = (inlet__H_R_out_LHS-inlet__H_link_L)/V2__tau_link
    dydt[2] = (inlet__H_down_target-inlet__H_down)/V2__tau_H_down
    dydt[3] = inlet__v*inlet__H_mass_L-inlet__v_d*inlet__H_mass_R
    dydt[4] = inlet__v-inlet__v_d
    dydt[5] = VV_junc1__RBC_in-VV_junc1__RBC_out
    dydt[6] = inlet__v_d+VV_junc1__vbc2-VV_junc1__v
    dydt[7] = VV_junc1__v-PV1__v-PV2__v
    dydt[8] = (V1__H_L_out-PV1__H_link_R)/V2__tau_link
    dydt[9] = (VV_junc1__H_from3-PV1__H_link_L)/V2__tau_link
    dydt[10] = (PV1__H_down_target-PV1__H_down)/V2__tau_H_down
    dydt[11] = PV1__v*PV1__H_mass_L-PV1__v_d*PV1__H_mass_R
    dydt[12] = PV1__v-PV1__v_d
    dydt[13] = (V2__H_L_out-PV2__H_link_R)/V2__tau_link
    dydt[14] = (VV_junc1__H_from4-PV2__H_link_L)/V2__tau_link
    dydt[15] = (PV2__H_down_target-PV2__H_down)/V2__tau_H_down
    dydt[16] = PV2__v*PV2__H_mass_L-PV2__v_d*PV2__H_mass_R
    dydt[17] = PV2__v-PV2__v_d
    dydt[18] = (V1__H_L_out_RHS-V1__H_link_R)/V2__tau_link
    dydt[19] = (PV1__H_R_out-V1__H_link_L)/V2__tau_link
    dydt[20] = (V1__H_down_target-V1__H_down)/V2__tau_H_down
    dydt[21] = PV1__v_d*V1__H_mass_L-V1__v*V1__H_mass_R
    dydt[22] = PV1__v_d-V1__v
    dydt[23] = (V2__H_L_out_RHS-V2__H_link_R)/V2__tau_link
    dydt[24] = (PV2__H_R_out-V2__H_link_L)/V2__tau_link
    dydt[25] = (V2__H_down_target-V2__H_down)/V2__tau_H_down
    dydt[26] = PV2__v_d*V2__H_mass_L-V2__v*V2__H_mass_R
    dydt[27] = PV2__v_d-V2__v

    return dydt

if __name__ == "__main__":
    print("Running simulation...")
    sol = solve_ivp(
        ode_rhs,
        [0, 1000],
        y0,
        method="LSODA",
        t_eval=np.linspace(0, 1000, 10001),
        rtol=1e-8,
        atol=1e-12,
    )
    if sol.success:
        print(f"Success! {sol.t.shape[0]} points")
    else:
        print(f"Failed: {sol.message}")