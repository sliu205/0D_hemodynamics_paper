"""
generated_model.py
===================
Auto-generated from CellML by cellml_to_python.py
DO NOT EDIT BY HAND – re-run the generator instead.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ================================================================
# PARAMETERS  (from model_params.py)
# ================================================================
# Generated from: model_params.py







environment__time                                       = None                             # [second]  *** NOT FOUND ***  environment/time


inlet__H_global_L                                       = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_L
inlet__H_global_R                                       = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_R
inlet__H_R_out_LHS                                      = 0.45                       # [dimensionless]  (constant)  [initial_params.csv]  inlet/H_R_out_LHS
inlet__gamma_mirror                                     = 0.1                        # [dimensionless]  (global)  [B1_TD_parameters.csv]  gamma_mirror
inlet__tau_H_down                                       = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_down
inlet__tau_H_mean                                       = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_mean
inlet__v_eps                                            = 1e-30                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_eps
inlet__q_C_init                                         = 0                          # [m3]  (global)  [B1_TD_parameters.csv]  q_C_init
inlet__r                                                = 6e-06                      # [metre]  (constant)  [initial_params.csv]  inlet/r
inlet__mu_plasma                                        = 0.001                      # [Js_per_m3]  (global)  [B1_TD_parameters.csv]  mu_plasma
inlet__u_in                                             = 6666.1                     # [J_per_m3]  (constant)  [initial_params.csv]  inlet/u_in
inlet__u_ext                                            = 133                        # [J_per_m3]  (global)  [B1_TD_parameters.csv]  u_ext
inlet__tau_link                                         = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_link
inlet__v_scale                                          = 1e-50                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_scale
inlet__one_mm3                                          = 1e-09                      # [m3]  (global)  [B1_TD_parameters.csv]  one_mm3
inlet__w_v                                              = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/w_v
inlet__w_v_d                                            = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/w_v_d
inlet__H_link_R                                         = -1.9984014885135946e-16    # [dimensionless]  (state)  [initial_params.csv]  inlet/H_link_R
inlet__H_link_L                                         = 0.45                       # [dimensionless]  (state)  [initial_params.csv]  inlet/H_link_L
inlet__H_L_in                                           = 0.45                       # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_L_in
inlet__H_R_in                                           = -1.9984014885135946e-16    # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_R_in
inlet__H_up                                             = 0.45000000000000023        # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_up
inlet__H_down                                           = 0.45000000994816686        # [dimensionless]  (state)  [initial_params.csv]  inlet/H_down
inlet__H_down_target                                    = 0.4500000099460112         # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_down_target
inlet__s_v_d                                            = 0.9999999999999999         # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/s_v_d
inlet__H_L_out                                          = 0.45                       # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_L_out
inlet__H_R_out                                          = 0.4500000099481671         # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_R_out
inlet__RBC_volume                                       = 1.5269640297159772e-14     # [m3]  (state)  [initial_params.csv]  inlet/RBC_volume
inlet__RBC_volume_init                                  = 1.5268140296446382e-14     # [m3]  (constant)  [initial_params.csv]  inlet/RBC_volume_init
inlet__v_pos                                            = 6.683363790951124e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_pos
inlet__v_neg                                            = 2.9680097450640023e-30     # [m3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_neg
inlet__v_d_pos                                          = 6.683363790724218e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_d_pos
inlet__v_d_neg                                          = 2.968009744963236e-30      # [m3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_d_neg
inlet__H_mean                                           = 0.45000000904182835        # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_mean
inlet__H_mass_L                                         = 0.45                       # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_mass_L
inlet__H_mass_R                                         = 0.4500000099481673         # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/H_mass_R
inlet__q_C                                              = 3.3326531138933488e-18     # [m3]  (state)  [initial_params.csv]  inlet/q_C
inlet__q                                                = 3.3932533311883623e-14     # [m3]  (algebraic)  [initial_params.csv]  inlet/q
inlet__q_us                                             = 3.392920065876973e-14      # [m3]  (constant)  [initial_params.csv]  inlet/q_us
inlet__C                                                = 5.107485693775874e-22      # [m6_per_J]  (constant)  [initial_params.csv]  inlet/C
inlet__Z                                                = -1.1820960009520325        # [dimensionless]  (constant)  [initial_params.csv]  inlet/Z
inlet__mu_45                                            = 3.5523629350190156         # [dimensionless]  (constant)  [initial_params.csv]  inlet/mu_45
inlet__mu                                               = 0.004093512976500455       # [Js_per_m3]  (algebraic)  [initial_params.csv]  inlet/mu
inlet__hem_dep_u_rel                                    = 4.093512976500454          # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/hem_dep_u_rel
inlet__R                                                = 2412973425262465.0         # [Js_per_m6]  (algebraic)  [initial_params.csv]  inlet/R
inlet__v                                                = 6.683363790951121e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  inlet/v
inlet__v_mm3_s                                          = 6.68336379095112e-06       # [mm3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_mm3_s
inlet__u                                                = 6658.036610390537          # [J_per_m3]  (algebraic)  [initial_params.csv]  inlet/u
inlet__u_mmHg                                           = 49.93951943708118          # [dimensionless]  (algebraic)  [initial_params.csv]  inlet/u_mmHg
inlet__v_d                                              = 6.683363790724215e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_d
inlet__v_d_mm3_s                                        = 6.683363790724214e-06      # [mm3_per_s]  (algebraic)  [initial_params.csv]  inlet/v_d_mm3_s


VV_junc1__div_0                                         = 1e-25                      # [dimensionless]  (global)  [B1_TD_parameters.csv]  div_0
VV_junc1__div_0y                                        = 1e-08                      # [dimensionless]  (global)  [B1_TD_parameters.csv]  div_0y
VV_junc1__tau_junc                                      = 0.0001                     # [second]  (global)  [B1_TD_parameters.csv]  tau_junc
VV_junc1__v_threshold                                   = 1e-18                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_threshold
VV_junc1__k                                             = 1000                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  k
VV_junc1__H_global_L                                    = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_L
VV_junc1__H_global_R                                    = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_R
VV_junc1__q_C_init                                      = 0                          # [m3]  (global)  [B1_TD_parameters.csv]  q_C_init
VV_junc1__r                                             = 6e-06                      # [metre]  (constant)  [initial_params.csv]  VV_junc1/r
VV_junc1__mu_plasma                                     = 0.001                      # [Js_per_m3]  (global)  [B1_TD_parameters.csv]  mu_plasma
VV_junc1__u_ext                                         = 133                        # [J_per_m3]  (global)  [B1_TD_parameters.csv]  u_ext
VV_junc1__v_scale                                       = 1e-50                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_scale
VV_junc1__one_mm3                                       = 1e-09                      # [m3]  (global)  [B1_TD_parameters.csv]  one_mm3
VV_junc1__vbc2                                          = 0.0                        # [m3_per_s]  (constant)  [initial_params.csv]  VV_junc1/vbc2
VV_junc1__vj1                                           = 6.683363790724215e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/vj1
VV_junc1__vj2                                           = 0.0                        # [m3_per_s]  (constant)  [initial_params.csv]  VV_junc1/vj2
VV_junc1__vj3                                           = -3.341681909662474e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/vj3
VV_junc1__vj4                                           = -3.341681880101671e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/vj4
VV_junc1__H_to2                                         = 0.0                        # [dimensionless]  (constant)  [initial_params.csv]  VV_junc1/H_to2
VV_junc1__H_split1                                      = 0.4500000099481671         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_split1
VV_junc1__H_split2                                      = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_split2
VV_junc1__H_split3                                      = 0.4500546438778501         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_split3
VV_junc1__H_split4                                      = 0.45005464222897806        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_split4
VV_junc1__H_daughter1                                   = 0.4500000099481671         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_daughter1
VV_junc1__H_daughter2                                   = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_daughter2
VV_junc1__H_daughter3                                   = 0.4500546438778501         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_daughter3
VV_junc1__H_daughter4                                   = 0.45005464222897806        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_daughter4
VV_junc1__H_from1_target                                = 0.4500000099481671         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from1_target
VV_junc1__H_from2_target                                = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from2_target
VV_junc1__H_from3_target                                = 0.4500546438778501         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from3_target
VV_junc1__H_from4_target                                = 0.45005464222897806        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from4_target
VV_junc1__H_from1                                       = -1.9984014885040183e-16    # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from1
VV_junc1__H_from2                                       = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from2
VV_junc1__H_from3                                       = 0.4500546438778503         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from3
VV_junc1__H_from4                                       = 0.4500546422289783         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_from4
VV_junc1__r_bc2                                         = 0.0                        # [metre]  (constant)  [initial_params.csv]  VV_junc1/r_bc2
VV_junc1__D1                                            = 1.2e-05                    # [metre]  (constant)  [initial_params.csv]  VV_junc1/D1
VV_junc1__D2                                            = 0.0                        # [metre]  (constant)  [initial_params.csv]  VV_junc1/D2
VV_junc1__D3                                            = 1.2e-05                    # [metre]  (constant)  [initial_params.csv]  VV_junc1/D3
VV_junc1__D4                                            = 1.2e-05                    # [metre]  (constant)  [initial_params.csv]  VV_junc1/D4
VV_junc1__w_in1                                         = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/w_in1
VV_junc1__w_in2                                         = 0.5                        # [dimensionless]  (constant)  [initial_params.csv]  VV_junc1/w_in2
VV_junc1__w_in3                                         = -5.551115123125783e-16     # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/w_in3
VV_junc1__w_in4                                         = -5.551115123125783e-16     # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/w_in4
VV_junc1__w_out1                                        = -4.440892098500626e-16     # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/w_out1
VV_junc1__w_out2                                        = 0.5                        # [dimensionless]  (constant)  [initial_params.csv]  VV_junc1/w_out2
VV_junc1__w_out3                                        = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/w_out3
VV_junc1__w_out4                                        = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/w_out4
VV_junc1__Qin1                                          = 6.683363790724218e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qin1
VV_junc1__Qin2                                          = 0.0                        # [m3_per_s]  (constant)  [initial_params.csv]  VV_junc1/Qin2
VV_junc1__Qin3                                          = 1.8550060985403206e-30     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qin3
VV_junc1__Qin4                                          = 1.8550060821307785e-30     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qin4
VV_junc1__Qout1                                         = 2.968009744963236e-30      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout1
VV_junc1__Qout2                                         = -0.0                       # [m3_per_s]  (constant)  [initial_params.csv]  VV_junc1/Qout2
VV_junc1__Qout3                                         = 3.3416819096624756e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout3
VV_junc1__Qout4                                         = 3.3416818801016727e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout4
VV_junc1__Qin_tot                                       = 6.6833637907242215e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qin_tot
VV_junc1__Qout_tot                                      = 6.683363789764151e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout_tot
VV_junc1__bc1_is_in                                     = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/bc1_is_in
VV_junc1__bc2_is_in                                     = 0.0                        # [dimensionless]  (constant)  [initial_params.csv]  VV_junc1/bc2_is_in
VV_junc1__bc3_is_in                                     = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/bc3_is_in
VV_junc1__bc4_is_in                                     = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/bc4_is_in
VV_junc1__bc1_is_out                                    = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/bc1_is_out
VV_junc1__bc2_is_out                                    = 0.0                        # [dimensionless]  (constant)  [initial_params.csv]  VV_junc1/bc2_is_out
VV_junc1__bc3_is_out                                    = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/bc3_is_out
VV_junc1__bc4_is_out                                    = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/bc4_is_out
VV_junc1__n_in                                          = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/n_in
VV_junc1__n_out                                         = 2.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/n_out
VV_junc1__junction_type                                 = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/junction_type
VV_junc1__is_split                                      = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/is_split
VV_junc1__is_merge                                      = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/is_merge
VV_junc1__feed1                                         = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/feed1
VV_junc1__feed2                                         = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/feed2
VV_junc1__feed3                                         = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/feed3
VV_junc1__feed4                                         = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/feed4
VV_junc1__alpha1                                        = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/alpha1
VV_junc1__alpha2                                        = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/alpha2
VV_junc1__alpha3                                        = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/alpha3
VV_junc1__alpha4                                        = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/alpha4
VV_junc1__Qout1_rem                                     = 2.968009744963236e-30      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout1_rem
VV_junc1__Qout2_rem                                     = -0.0                       # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout2_rem
VV_junc1__Qout3_rem                                     = 0.0                        # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout3_rem
VV_junc1__Qout4_rem                                     = 3.3416818801016727e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/Qout4_rem
VV_junc1__beta1                                         = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/beta1
VV_junc1__beta2                                         = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/beta2
VV_junc1__beta3                                         = 0.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/beta3
VV_junc1__beta4                                         = 1.0                        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/beta4
VV_junc1__D_F                                           = 1.2e-05                    # [metre]  (algebraic)  [initial_params.csv]  VV_junc1/D_F
VV_junc1__D_alpha                                       = 1.2e-05                    # [metre]  (algebraic)  [initial_params.csv]  VV_junc1/D_alpha
VV_junc1__D_beta                                        = 1.2e-05                    # [metre]  (algebraic)  [initial_params.csv]  VV_junc1/D_beta
VV_junc1__v_alpha                                       = 3.3416819096624756e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/v_alpha
VV_junc1__v_beta                                        = 3.3416818801016727e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/v_beta
VV_junc1__FQB_alpha                                     = 0.5000000022115213         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/FQB_alpha
VV_junc1__FQE_alpha                                     = 0.5000000031274501         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/FQE_alpha
VV_junc1__B                                             = 1.3198848826239309         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/B
VV_junc1__A                                             = -0.0                       # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/A
VV_junc1__X_0                                           = 0.03333333333333333        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/X_0
VV_junc1__ph                                            = 9.47794815913504e-09       # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/ph
VV_junc1__y_raw                                         = 0.500000002369487          # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/y_raw
VV_junc1__y                                             = 0.500000002369487          # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/y
VV_junc1__H_VV_out_alpha                                = 0.4500546438778501         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_VV_out_alpha
VV_junc1__H_VV_out_beta                                 = 0.45005464222897806        # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_VV_out_beta
VV_junc1__RBC_in                                        = 3.0075137723131196e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/RBC_in
VV_junc1__RBC_out                                       = 3.007878904798418e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/RBC_out
VV_junc1__RBC_volume_init                               = 5.08938009881546e-17       # [m3]  (constant)  [initial_params.csv]  VV_junc1/RBC_volume_init
VV_junc1__RBC_volume                                    = 5.0899981016906383e-17     # [m3]  (state)  [initial_params.csv]  VV_junc1/RBC_volume
VV_junc1__H_mean                                        = 0.4500546430534141         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/H_mean
VV_junc1__C_conn2                                       = 8.51e-22                   # [m6_per_J]  (constant)  [initial_params.csv]  VV_junc1/C_conn2
VV_junc1__C_max12                                       = 8.51e-22                   # [m6_per_J]  (constant)  [initial_params.csv]  VV_junc1/C_max12
VV_junc1__C_max123                                      = 8.51e-22                   # [m6_per_J]  (constant)  [initial_params.csv]  VV_junc1/C_max123
VV_junc1__C                                             = 8.51e-22                   # [m6_per_J]  (constant)  [initial_params.csv]  VV_junc1/C
VV_junc1__q_C                                           = 2.7729721054424635e-18     # [m3]  (state)  [initial_params.csv]  VV_junc1/q_C
VV_junc1__q_C_d                                         = 2.7701283341496695e-18     # [m3]  (state)  [initial_params.csv]  VV_junc1/q_C_d
VV_junc1__q                                             = 1.186404359688246e-16      # [m3]  (algebraic)  [initial_params.csv]  VV_junc1/q
VV_junc1__q_us                                          = 1.1309733552923245e-16     # [m3]  (constant)  [initial_params.csv]  VV_junc1/q_us
VV_junc1__R                                             = 1000000000000000           # [Js_per_m6]  (global)  [B1_TD_parameters.csv]  R
VV_junc1__u                                             = 6649.973220781348          # [J_per_m3]  (algebraic)  [initial_params.csv]  VV_junc1/u
VV_junc1__u_mmHg                                        = 49.87903887416441          # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/u_mmHg
VV_junc1__v                                             = 6.683363790350995e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/v
VV_junc1__v_mm3_s                                       = 6.683363790350995e-06      # [mm3_per_s]  (algebraic)  [initial_params.csv]  VV_junc1/v_mm3_s
VV_junc1__u_d                                           = 6643.289856990997          # [J_per_m3]  (algebraic)  [initial_params.csv]  VV_junc1/u_d
VV_junc1__u_d_mmHg                                      = 49.828909384730174         # [dimensionless]  (algebraic)  [initial_params.csv]  VV_junc1/u_d_mmHg


PV1__R_constriction_base                                = 0                          # [Js_per_m6]  (global)  [B1_TD_parameters.csv]  R_constriction_base
PV1__R_constriction_final                               = 0.0                        # [Js_per_m6]  (constant)  [initial_params.csv]  PV1/R_constriction_final
PV1__R_constriction                                     = 0.0                        # [Js_per_m6]  (algebraic)  [initial_params.csv]  PV1/R_constriction
PV1__tau_sig                                            = 1                          # [second]  (global)  [B1_TD_parameters.csv]  tau_sig
PV1__t0                                                 = 500                        # [second]  (global)  [B1_TD_parameters.csv]  t0
PV1__H_global_L                                         = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_L
PV1__H_global_R                                         = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_R
PV1__gamma_mirror                                       = 0.1                        # [dimensionless]  (global)  [B1_TD_parameters.csv]  gamma_mirror
PV1__tau_H_down                                         = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_down
PV1__tau_H_mean                                         = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_mean
PV1__v_eps                                              = 1e-30                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_eps
PV1__q_C_init                                           = 0                          # [m3]  (global)  [B1_TD_parameters.csv]  q_C_init
PV1__r                                                  = 6e-06                      # [metre]  (constant)  [initial_params.csv]  PV1/r
PV1__mu_plasma                                          = 0.001                      # [Js_per_m3]  (global)  [B1_TD_parameters.csv]  mu_plasma
PV1__u_ext                                              = 133                        # [J_per_m3]  (global)  [B1_TD_parameters.csv]  u_ext
PV1__tau_link                                           = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_link
PV1__v_scale                                            = 1e-50                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_scale
PV1__one_mm3                                            = 1e-09                      # [m3]  (global)  [B1_TD_parameters.csv]  one_mm3
PV1__w_v                                                = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/w_v
PV1__w_v_d                                              = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/w_v_d
PV1__H_link_R                                           = 0.45066594907900703        # [dimensionless]  (state)  [initial_params.csv]  PV1/H_link_R
PV1__H_link_L                                           = 0.45005807512155366        # [dimensionless]  (state)  [initial_params.csv]  PV1/H_link_L
PV1__H_L_in                                             = 0.45005807512155366        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_L_in
PV1__H_R_in                                             = 0.45066594907900703        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_R_in
PV1__H_up                                               = 0.45005807512155366        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_up
PV1__H_down                                             = 0.45066415426369355        # [dimensionless]  (state)  [initial_params.csv]  PV1/H_down
PV1__H_down_target                                      = 0.4506632117512172         # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_down_target
PV1__s_v_d                                              = 0.9999999999999997         # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/s_v_d
PV1__H_L_out                                            = 0.45005807512155366        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_L_out
PV1__H_R_out                                            = 0.45066415426369355        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_R_out
PV1__RBC_volume                                         = 7.645137146985757e-16      # [m3]  (state)  [initial_params.csv]  PV1/RBC_volume
PV1__RBC_volume_init                                    = 7.634070148223191e-16      # [m3]  (constant)  [initial_params.csv]  PV1/RBC_volume_init
PV1__v_pos                                              = 3.3416819096624756e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_pos
PV1__v_neg                                              = 1.4840048788322564e-30     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_neg
PV1__v_d_pos                                            = 3.3416819096022863e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_d_pos
PV1__v_d_neg                                            = 1.484004878805527e-30      # [m3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_d_neg
PV1__H_mean                                             = 0.4506081993303387         # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_mean
PV1__H_mass_L                                           = 0.45005807512155366        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_mass_L
PV1__H_mass_R                                           = 0.45066415426369355        # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/H_mass_R
PV1__q_C                                                = 1.6625090353096748e-19     # [m3]  (state)  [initial_params.csv]  PV1/q_C
PV1__q                                                  = 1.6966262838420179e-15     # [m3]  (algebraic)  [initial_params.csv]  PV1/q
PV1__q_us                                               = 1.696460032938487e-15      # [m3]  (constant)  [initial_params.csv]  PV1/q_us
PV1__C                                                  = 2.553742846887937e-23      # [m6_per_J]  (constant)  [initial_params.csv]  PV1/C
PV1__Z                                                  = -1.1820960009520325        # [dimensionless]  (constant)  [initial_params.csv]  PV1/Z
PV1__mu_45                                              = 3.5523629350190156         # [dimensionless]  (constant)  [initial_params.csv]  PV1/mu_45
PV1__mu                                                 = 0.004101502635175103       # [Js_per_m3]  (algebraic)  [initial_params.csv]  PV1/mu
PV1__hem_dep_u_rel                                      = 4.101502635175104          # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/hem_dep_u_rel
PV1__R                                                  = 120884151572694.98         # [Js_per_m6]  (algebraic)  [initial_params.csv]  PV1/R
PV1__v                                                  = 3.341681909662474e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  PV1/v
PV1__v_mm3_s                                            = 3.341681909662474e-06      # [mm3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_mm3_s
PV1__u                                                  = 6643.087878799759          # [J_per_m3]  (algebraic)  [initial_params.csv]  PV1/u
PV1__u_mmHg                                             = 49.82739441952385          # [dimensionless]  (algebraic)  [initial_params.csv]  PV1/u_mmHg
PV1__v_d                                                = 3.3416819096022847e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_d
PV1__v_d_mm3_s                                          = 3.3416819096022845e-06     # [mm3_per_s]  (algebraic)  [initial_params.csv]  PV1/v_d_mm3_s


PV2__R_constriction_base                                = 0                          # [Js_per_m6]  (global)  [B1_TD_parameters.csv]  R_constriction_base
PV2__R_constriction_final                               = 0.0                        # [Js_per_m6]  (constant)  [initial_params.csv]  PV2/R_constriction_final
PV2__R_constriction                                     = 0.0                        # [Js_per_m6]  (algebraic)  [initial_params.csv]  PV2/R_constriction
PV2__tau_sig                                            = 1                          # [second]  (global)  [B1_TD_parameters.csv]  tau_sig
PV2__t0                                                 = 500                        # [second]  (global)  [B1_TD_parameters.csv]  t0
PV2__H_global_L                                         = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_L
PV2__H_global_R                                         = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_R
PV2__gamma_mirror                                       = 0.1                        # [dimensionless]  (global)  [B1_TD_parameters.csv]  gamma_mirror
PV2__tau_H_down                                         = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_down
PV2__tau_H_mean                                         = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_mean
PV2__v_eps                                              = 1e-30                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_eps
PV2__q_C_init                                           = 0                          # [m3]  (global)  [B1_TD_parameters.csv]  q_C_init
PV2__r                                                  = 6e-06                      # [metre]  (constant)  [initial_params.csv]  PV2/r
PV2__mu_plasma                                          = 0.001                      # [Js_per_m3]  (global)  [B1_TD_parameters.csv]  mu_plasma
PV2__u_ext                                              = 133                        # [J_per_m3]  (global)  [B1_TD_parameters.csv]  u_ext
PV2__tau_link                                           = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_link
PV2__v_scale                                            = 1e-50                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_scale
PV2__one_mm3                                            = 1e-09                      # [m3]  (global)  [B1_TD_parameters.csv]  one_mm3
PV2__w_v                                                = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/w_v
PV2__w_v_d                                              = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/w_v_d
PV2__H_link_R                                           = 0.4506660141504298         # [dimensionless]  (state)  [initial_params.csv]  PV2/H_link_R
PV2__H_link_L                                           = 0.45005807347727317        # [dimensionless]  (state)  [initial_params.csv]  PV2/H_link_L
PV2__H_L_in                                             = 0.45005807347727317        # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_L_in
PV2__H_R_in                                             = 0.4506660141504298         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_R_in
PV2__H_up                                               = 0.45005807347727317        # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_up
PV2__H_down                                             = 0.4506642190463343         # [dimensionless]  (state)  [initial_params.csv]  PV2/H_down
PV2__H_down_target                                      = 0.45066327638993164        # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_down_target
PV2__s_v_d                                              = 0.9999999999999997         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/s_v_d
PV2__H_L_out                                            = 0.45005807347727317        # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_L_out
PV2__H_R_out                                            = 0.4506642190463343         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_R_out
PV2__RBC_volume                                         = 7.645138141429107e-16      # [m3]  (state)  [initial_params.csv]  PV2/RBC_volume
PV2__RBC_volume_init                                    = 7.634070148223191e-16      # [m3]  (constant)  [initial_params.csv]  PV2/RBC_volume_init
PV2__v_pos                                              = 3.3416818801016727e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_pos
PV2__v_neg                                              = 1.4840048657046228e-30     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_neg
PV2__v_d_pos                                            = 3.3416818801167202e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_d_pos
PV2__v_d_neg                                            = 1.4840048657113052e-30     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_d_neg
PV2__H_mean                                             = 0.4506082579433263         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_mean
PV2__H_mass_L                                           = 0.45005807347727317        # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_mass_L
PV2__H_mass_R                                           = 0.4506642190463343         # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/H_mass_R
PV2__q_C                                                = 1.662509035300436e-19      # [m3]  (state)  [initial_params.csv]  PV2/q_C
PV2__q                                                  = 1.6966262838420169e-15     # [m3]  (algebraic)  [initial_params.csv]  PV2/q
PV2__q_us                                               = 1.696460032938487e-15      # [m3]  (constant)  [initial_params.csv]  PV2/q_us
PV2__C                                                  = 2.553742846887937e-23      # [m6_per_J]  (constant)  [initial_params.csv]  PV2/C
PV2__Z                                                  = -1.1820960009520325        # [dimensionless]  (constant)  [initial_params.csv]  PV2/Z
PV2__mu_45                                              = 3.5523629350190156         # [dimensionless]  (constant)  [initial_params.csv]  PV2/mu_45
PV2__mu                                                 = 0.004101503406090829       # [Js_per_m3]  (algebraic)  [initial_params.csv]  PV2/mu
PV2__hem_dep_u_rel                                      = 4.101503406090829          # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/hem_dep_u_rel
PV2__R                                                  = 120884174294000.25         # [Js_per_m6]  (algebraic)  [initial_params.csv]  PV2/R
PV2__v                                                  = 3.341681880101671e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  PV2/v
PV2__v_mm3_s                                            = 3.341681880101671e-06      # [mm3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_mm3_s
PV2__u                                                  = 6643.087878763582          # [J_per_m3]  (algebraic)  [initial_params.csv]  PV2/u
PV2__u_mmHg                                             = 49.8273944192525           # [dimensionless]  (algebraic)  [initial_params.csv]  PV2/u_mmHg
PV2__v_d                                                = 3.3416818801167186e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_d
PV2__v_d_mm3_s                                          = 3.3416818801167182e-06     # [mm3_per_s]  (algebraic)  [initial_params.csv]  PV2/v_d_mm3_s


V1__H_global_L                                          = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_L
V1__H_global_R                                          = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_R
V1__H_L_out_RHS                                         = 0.45                       # [dimensionless]  (constant)  [initial_params.csv]  V1/H_L_out_RHS
V1__gamma_mirror                                        = 0.1                        # [dimensionless]  (global)  [B1_TD_parameters.csv]  gamma_mirror
V1__tau_H_down                                          = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_down
V1__tau_H_mean                                          = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_mean
V1__v_eps                                               = 1e-30                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_eps
V1__q_C_init                                            = 0                          # [m3]  (global)  [B1_TD_parameters.csv]  q_C_init
V1__r                                                   = 5.5e-06                    # [metre]  (constant)  [initial_params.csv]  V1/r
V1__mu_plasma                                           = 0.001                      # [Js_per_m3]  (global)  [B1_TD_parameters.csv]  mu_plasma
V1__u_out                                               = 6632.7695                  # [J_per_m3]  (constant)  [initial_params.csv]  V1/u_out
V1__u_ext                                               = 133                        # [J_per_m3]  (global)  [B1_TD_parameters.csv]  u_ext
V1__tau_link                                            = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_link
V1__v_scale                                             = 1e-50                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_scale
V1__one_mm3                                             = 1e-09                      # [m3]  (global)  [B1_TD_parameters.csv]  one_mm3
V1__w_v                                                 = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  V1/w_v
V1__H_link_R                                            = 0.45                       # [dimensionless]  (state)  [initial_params.csv]  V1/H_link_R
V1__H_link_L                                            = 0.45066506738583584        # [dimensionless]  (state)  [initial_params.csv]  V1/H_link_L
V1__H_L_in                                              = 0.45066506738583584        # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_L_in
V1__H_R_in                                              = 0.45                       # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_R_in
V1__H_up                                                = 0.45066506738583584        # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_up
V1__H_down                                              = 0.4499375638693855         # [dimensionless]  (state)  [initial_params.csv]  V1/H_down
V1__H_down_target                                       = 0.4499377647508902         # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_down_target
V1__s_v                                                 = 0.9999999999999997         # [dimensionless]  (algebraic)  [initial_params.csv]  V1/s_v
V1__H_L_out                                             = 0.45066506738583584        # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_L_out
V1__H_R_out                                             = 0.4499375638693855         # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_R_out
V1__RBC_volume                                          = 1.0692571610648219e-14     # [m3]  (state)  [initial_params.csv]  V1/RBC_volume
V1__RBC_volume_init                                     = 1.0691232499247755e-14     # [m3]  (constant)  [initial_params.csv]  V1/RBC_volume_init
V1__v_pos                                               = 3.341681908423005e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  V1/v_pos
V1__v_neg                                               = 1.484004878281821e-30      # [m3_per_s]  (algebraic)  [initial_params.csv]  V1/v_neg
V1__H_mean                                              = 0.4500038831722489         # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_mean
V1__H_mass_L                                            = 0.45066506738583584        # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_mass_L
V1__H_mass_R                                            = 0.4499375638693855         # [dimensionless]  (algebraic)  [initial_params.csv]  V1/H_mass_R
V1__q_C                                                 = 2.7707624254559425e-18     # [m3]  (state)  [initial_params.csv]  V1/q_C
V1__q                                                   = 2.3761065205198245e-14     # [m3]  (algebraic)  [initial_params.csv]  V1/q
V1__q_us                                                = 2.3758294442772788e-14     # [m3]  (constant)  [initial_params.csv]  V1/q_us
V1__C                                                   = 4.256238078146562e-22      # [m6_per_J]  (constant)  [initial_params.csv]  V1/C
V1__Z                                                   = -1.1691201400706768        # [dimensionless]  (constant)  [initial_params.csv]  V1/Z
V1__mu_45                                               = 3.71461005007079           # [dimensionless]  (constant)  [initial_params.csv]  V1/mu_45
V1__mu                                                  = 0.004351425441490857       # [Js_per_m3]  (algebraic)  [initial_params.csv]  V1/mu
V1__hem_dep_u_rel                                       = 4.351425441490857          # [dimensionless]  (algebraic)  [initial_params.csv]  V1/hem_dep_u_rel
V1__R                                                   = 3027337994985495.5         # [Js_per_m6]  (algebraic)  [initial_params.csv]  V1/R
V1__v                                                   = 3.3416819084230035e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  V1/v
V1__v_mm3_s                                             = 3.3416819084230033e-06     # [mm3_per_s]  (algebraic)  [initial_params.csv]  V1/v_mm3_s
V1__u                                                   = 6642.885900608525          # [J_per_m3]  (algebraic)  [initial_params.csv]  V1/u
V1__u_mmHg                                              = 49.82587945431755          # [dimensionless]  (algebraic)  [initial_params.csv]  V1/u_mmHg


V2__H_global_L                                          = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_L
V2__H_global_R                                          = 0.45                       # [dimensionless]  (global)  [B1_TD_parameters.csv]  H_global_R
V2__H_L_out_RHS                                         = 0.45                       # [dimensionless]  (constant)  [initial_params.csv]  V2/H_L_out_RHS
V2__gamma_mirror                                        = 0.1                        # [dimensionless]  (global)  [B1_TD_parameters.csv]  gamma_mirror
V2__tau_H_down                                          = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_down
V2__tau_H_mean                                          = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_H_mean
V2__v_eps                                               = 1e-30                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_eps
V2__q_C_init                                            = 0                          # [m3]  (global)  [B1_TD_parameters.csv]  q_C_init
V2__r                                                   = 5.5e-06                    # [metre]  (constant)  [initial_params.csv]  V2/r
V2__mu_plasma                                           = 0.001                      # [Js_per_m3]  (global)  [B1_TD_parameters.csv]  mu_plasma
V2__u_out                                               = 6632.7695                  # [J_per_m3]  (constant)  [initial_params.csv]  V2/u_out
V2__u_ext                                               = 133                        # [J_per_m3]  (global)  [B1_TD_parameters.csv]  u_ext
V2__tau_link                                            = 0.001                      # [second]  (global)  [B1_TD_parameters.csv]  tau_link
V2__v_scale                                             = 1e-50                      # [m3_per_s]  (global)  [B1_TD_parameters.csv]  v_scale
V2__one_mm3                                             = 1e-09                      # [m3]  (global)  [B1_TD_parameters.csv]  one_mm3
V2__w_v                                                 = 1.0000000000000004         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/w_v
V2__H_link_R                                            = 0.45                       # [dimensionless]  (state)  [initial_params.csv]  V2/H_link_R
V2__H_link_L                                            = 0.4506651323127141         # [dimensionless]  (state)  [initial_params.csv]  V2/H_link_L
V2__H_L_in                                              = 0.4506651323127141         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_L_in
V2__H_R_in                                              = 0.45                       # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_R_in
V2__H_up                                                = 0.4506651323127141         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_up
V2__H_down                                              = 0.4499375579201643         # [dimensionless]  (state)  [initial_params.csv]  V2/H_down
V2__H_down_target                                       = 0.4499377588271135         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_down_target
V2__s_v                                                 = 0.9999999999999997         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/s_v
V2__H_L_out                                             = 0.4506651323127141         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_L_out
V2__H_R_out                                             = 0.4499375579201643         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_R_out
V2__RBC_volume                                          = 1.0692571622937236e-14     # [m3]  (state)  [initial_params.csv]  V2/RBC_volume
V2__RBC_volume_init                                     = 1.0691232499247755e-14     # [m3]  (constant)  [initial_params.csv]  V2/RBC_volume_init
V2__v_pos                                               = 3.341681878894819e-15      # [m3_per_s]  (algebraic)  [initial_params.csv]  V2/v_pos
V2__v_neg                                               = 1.484004865168672e-30      # [m3_per_s]  (algebraic)  [initial_params.csv]  V2/v_neg
V2__H_mean                                              = 0.45000388368944083        # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_mean
V2__H_mass_L                                            = 0.4506651323127141         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_mass_L
V2__H_mass_R                                            = 0.4499375579201643         # [dimensionless]  (algebraic)  [initial_params.csv]  V2/H_mass_R
V2__q_C                                                 = 2.770762425425145e-18      # [m3]  (state)  [initial_params.csv]  V2/q_C
V2__q                                                   = 2.3761065205198213e-14     # [m3]  (algebraic)  [initial_params.csv]  V2/q
V2__q_us                                                = 2.3758294442772788e-14     # [m3]  (constant)  [initial_params.csv]  V2/q_us
V2__C                                                   = 4.256238078146562e-22      # [m6_per_J]  (constant)  [initial_params.csv]  V2/C
V2__Z                                                   = -1.1691201400706768        # [dimensionless]  (constant)  [initial_params.csv]  V2/Z
V2__mu_45                                               = 3.71461005007079           # [dimensionless]  (constant)  [initial_params.csv]  V2/mu_45
V2__mu                                                  = 0.004351425448817493       # [Js_per_m3]  (algebraic)  [initial_params.csv]  V2/mu
V2__hem_dep_u_rel                                       = 4.351425448817492          # [dimensionless]  (algebraic)  [initial_params.csv]  V2/hem_dep_u_rel
V2__R                                                   = 3027338000082722.5         # [Js_per_m6]  (algebraic)  [initial_params.csv]  V2/R
V2__v                                                   = 3.3416818788948173e-15     # [m3_per_s]  (algebraic)  [initial_params.csv]  V2/v
V2__v_mm3_s                                             = 3.341681878894817e-06      # [mm3_per_s]  (algebraic)  [initial_params.csv]  V2/v_mm3_s
V2__u                                                   = 6642.885900536166          # [J_per_m3]  (algebraic)  [initial_params.csv]  V2/u
V2__u_mmHg                                              = 49.82587945377482          # [dimensionless]  (algebraic)  [initial_params.csv]  V2/u_mmHg


global__H_global_L                                      = 0.45                       # [dimensionless]  (constant)  [initial_params.csv]  global/H_global_L
global__H_global_R                                      = 0.45                       # [dimensionless]  (constant)  [initial_params.csv]  global/H_global_R
global__gamma_mirror                                    = 0.1                        # [dimensionless]  (constant)  [initial_params.csv]  global/gamma_mirror
global__tau_H_down                                      = 0.001                      # [second]  (constant)  [initial_params.csv]  global/tau_H_down
global__tau_H_mean                                      = 0.001                      # [second]  (constant)  [initial_params.csv]  global/tau_H_mean
global__v_eps                                           = 1e-30                      # [m3_per_s]  (constant)  [initial_params.csv]  global/v_eps
global__q_C_init                                        = 0.0                        # [m3]  (constant)  [initial_params.csv]  global/q_C_init
global__mu_plasma                                       = 0.001                      # [Js_per_m3]  (constant)  [initial_params.csv]  global/mu_plasma
global__u_ext                                           = 133.0                      # [J_per_m3]  (constant)  [initial_params.csv]  global/u_ext
global__tau_link                                        = 0.001                      # [second]  (constant)  [initial_params.csv]  global/tau_link
global__v_scale                                         = 1e-50                      # [m3_per_s]  (constant)  [initial_params.csv]  global/v_scale
global__one_mm3                                         = 1e-09                      # [m3]  (constant)  [initial_params.csv]  global/one_mm3
global__div_0                                           = 1e-25                      # [dimensionless]  (constant)  [initial_params.csv]  global/div_0
global__div_0y                                          = 1e-08                      # [dimensionless]  (constant)  [initial_params.csv]  global/div_0y
global__tau_junc                                        = 0.0001                     # [second]  (constant)  [initial_params.csv]  global/tau_junc
global__v_threshold                                     = 1e-18                      # [m3_per_s]  (constant)  [initial_params.csv]  global/v_threshold
global__k                                               = 1000.0                     # [dimensionless]  (constant)  [initial_params.csv]  global/k
global__R                                               = 1000000000000000.0         # [Js_per_m6]  (constant)  [initial_params.csv]  global/R
global__R_constriction_base                             = 0.0                        # [Js_per_m6]  (constant)  [initial_params.csv]  global/R_constriction_base
global__tau_sig                                         = 1.0                        # [second]  (constant)  [initial_params.csv]  global/tau_sig
global__t0                                              = 500.0                      # [second]  (constant)  [initial_params.csv]  global/t0



# ================================================================
# STATE VARIABLES  &  INITIAL CONDITIONS
# ================================================================

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

# Initial condition vector (order matches state_names)
y0 = np.array([
    inlet__H_global_L,  # inlet__H_link_R
    inlet__H_global_L,  # inlet__H_link_L
    inlet__H_global_L,  # inlet__H_down
    inlet__RBC_volume_init,  # inlet__RBC_volume
    inlet__q_C_init,  # inlet__q_C
    VV_junc1__RBC_volume_init,  # VV_junc1__RBC_volume
    VV_junc1__q_C_init,  # VV_junc1__q_C
    VV_junc1__q_C_init,  # VV_junc1__q_C_d
    PV1__H_global_L,  # PV1__H_link_R
    PV1__H_global_L,  # PV1__H_link_L
    PV1__H_global_L,  # PV1__H_down
    PV1__RBC_volume_init,  # PV1__RBC_volume
    PV1__q_C_init,  # PV1__q_C
    PV2__H_global_L,  # PV2__H_link_R
    PV2__H_global_L,  # PV2__H_link_L
    PV2__H_global_L,  # PV2__H_down
    PV2__RBC_volume_init,  # PV2__RBC_volume
    PV2__q_C_init,  # PV2__q_C
    V1__H_global_L,  # V1__H_link_R
    V1__H_global_L,  # V1__H_link_L
    V1__H_global_L,  # V1__H_down
    V1__RBC_volume_init,  # V1__RBC_volume
    V1__q_C_init,  # V1__q_C
    V2__H_global_L,  # V2__H_link_R
    V2__H_global_L,  # V2__H_link_L
    V2__H_global_L,  # V2__H_down
    V2__RBC_volume_init,  # V2__RBC_volume
    V2__q_C_init,  # V2__q_C
])

# ================================================================
# ODE FUNCTION
# ================================================================

def ode_rhs(t, y):
    """
    RHS of the ODE system.
    State vector y is ordered as per state_names.
    """
    # -- unpack states -------------------------------------------
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

    # -- algebraic equations (auto-sorted) ---------------
    inlet__H_L_in = inlet__H_link_L
    inlet__H_R_in = inlet__H_link_R
    PV1__H_L_in = PV1__H_link_L
    PV1__H_R_in = PV1__H_link_R
    PV2__H_L_in = PV2__H_link_L
    PV2__H_R_in = PV2__H_link_R
    V1__H_L_in = V1__H_link_L
    V1__H_R_in = V1__H_link_R
    V2__H_L_in = V2__H_link_L
    V2__H_R_in = V2__H_link_R
    inlet__w_v = 0.5+1/np.pi*np.arctan(inlet__v/inlet__v_scale)  # WARNING: circular dependency
    inlet__w_v_d = 0.5+1/np.pi*np.arctan(inlet__v_d/inlet__v_scale)  # WARNING: circular dependency
    inlet__H_up = inlet__w_v_d*inlet__H_L_in+(1-inlet__w_v_d)*inlet__H_R_in  # WARNING: circular dependency
    inlet__H_down_target = inlet__s_v_d*(inlet__H_mean+inlet__gamma_mirror*(inlet__H_mean-inlet__H_up))+(1-inlet__s_v_d)*inlet__H_mean  # WARNING: circular dependency
    inlet__s_v_d = np.abs(inlet__v_d)/(np.abs(inlet__v_d)+inlet__v_eps)  # WARNING: circular dependency
    inlet__H_L_out = (1-inlet__w_v_d)*inlet__H_down+inlet__w_v_d*inlet__H_L_in  # WARNING: circular dependency
    inlet__H_R_out = inlet__w_v_d*inlet__H_down+(1-inlet__w_v_d)*inlet__H_R_in  # WARNING: circular dependency
    inlet__RBC_volume_init = inlet__H_global_L*inlet__q_us  # WARNING: circular dependency
    inlet__v_pos = inlet__w_v*inlet__v  # WARNING: circular dependency
    inlet__v_neg = (1-inlet__w_v)*-inlet__v  # WARNING: circular dependency
    inlet__v_d_pos = inlet__w_v_d*inlet__v_d  # WARNING: circular dependency
    inlet__v_d_neg = (1-inlet__w_v_d)*-inlet__v_d  # WARNING: circular dependency
    inlet__H_mean = inlet__RBC_volume/inlet__q  # WARNING: circular dependency
    inlet__H_mass_L = inlet__w_v*inlet__H_L_in+(1-inlet__w_v)*inlet__H_L_out  # WARNING: circular dependency
    inlet__H_mass_R = inlet__w_v_d*inlet__H_R_out+(1-inlet__w_v_d)*inlet__H_R_in  # WARNING: circular dependency
    inlet__q_us = np.pi*np.square(inlet__r)*inlet__l  # WARNING: circular dependency
    inlet__q = inlet__q_us+inlet__q_C  # WARNING: circular dependency
    inlet__C = np.pi*np.square(8.5e-9)*inlet__l/133.322  # WARNING: circular dependency
    inlet__Z = (0.8+np.exp(-0.075*2*inlet__r*1e6))*(-1+1/(1+np.power(10, -11)*np.power(2*inlet__r*1e6, 12)))+1/(1+np.power(10, -11)*np.power(2*inlet__r*1e6, 12))  # WARNING: circular dependency
    inlet__mu_45 = 6*np.exp(-0.085*2*inlet__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*inlet__r*1e6, 0.645))  # WARNING: circular dependency
    inlet__mu = inlet__hem_dep_u_rel*inlet__mu_plasma  # WARNING: circular dependency
    inlet__hem_dep_u_rel = 1+(inlet__mu_45-1)*(np.power(1-inlet__H_mean, inlet__Z)-1)/(np.power(1-inlet__H_global_L, inlet__Z)-1)*np.square(2*inlet__r*1e6/(2*inlet__r*1e6-1.1))  # WARNING: circular dependency
    inlet__R = 8*inlet__mu*inlet__l/(np.pi*np.power(inlet__r, 4))  # WARNING: circular dependency
    inlet__v_mm3_s = inlet__v/inlet__one_mm3  # WARNING: circular dependency
    inlet__v = (inlet__u_in-inlet__u)/(inlet__R/2)  # WARNING: circular dependency
    inlet__u_mmHg = inlet__u/133.322  # WARNING: circular dependency
    inlet__u = inlet__q_C/inlet__C+inlet__u_ext  # WARNING: circular dependency
    inlet__v_d_mm3_s = inlet__v_d/inlet__one_mm3  # WARNING: circular dependency
    inlet__v_d = (inlet__u-VV_junc1__u)/(inlet__R/2)  # WARNING: circular dependency
    VV_junc1__vj1 = inlet__v_d  # WARNING: circular dependency
    VV_junc1__vj2 = VV_junc1__vbc2  # WARNING: circular dependency
    VV_junc1__vj3 = -PV1__v  # WARNING: circular dependency
    VV_junc1__vj4 = -PV2__v  # WARNING: circular dependency
    VV_junc1__H_from1 = VV_junc1__w_out1*VV_junc1__H_from1_target  # WARNING: circular dependency
    VV_junc1__H_from2 = VV_junc1__w_out2*VV_junc1__H_from2_target  # WARNING: circular dependency
    VV_junc1__H_from3 = VV_junc1__w_out3*VV_junc1__H_from3_target  # WARNING: circular dependency
    VV_junc1__H_from4 = VV_junc1__w_out4*VV_junc1__H_from4_target  # WARNING: circular dependency
    VV_junc1__D1 = 2*VV_junc1__r_bc1  # WARNING: circular dependency
    VV_junc1__D2 = 2*VV_junc1__r_bc2  # WARNING: circular dependency
    VV_junc1__D3 = 2*VV_junc1__r_bc3  # WARNING: circular dependency
    VV_junc1__D4 = 2*VV_junc1__r_bc4  # WARNING: circular dependency
    VV_junc1__w_in1 = 0.5+1/np.pi*np.arctan(VV_junc1__vj1/VV_junc1__v_scale)  # WARNING: circular dependency
    VV_junc1__w_in2 = 0.5+1/np.pi*np.arctan(VV_junc1__vj2/VV_junc1__v_scale)  # WARNING: circular dependency
    VV_junc1__w_in3 = 0.5+1/np.pi*np.arctan(VV_junc1__vj3/VV_junc1__v_scale)  # WARNING: circular dependency
    VV_junc1__w_in4 = 0.5+1/np.pi*np.arctan(VV_junc1__vj4/VV_junc1__v_scale)  # WARNING: circular dependency
    VV_junc1__w_out1 = 1-VV_junc1__w_in1  # WARNING: circular dependency
    VV_junc1__w_out2 = 1-VV_junc1__w_in2  # WARNING: circular dependency
    VV_junc1__w_out3 = 1-VV_junc1__w_in3  # WARNING: circular dependency
    VV_junc1__w_out4 = 1-VV_junc1__w_in4  # WARNING: circular dependency
    VV_junc1__Qin1 = VV_junc1__w_in1*VV_junc1__vj1  # WARNING: circular dependency
    VV_junc1__Qin2 = VV_junc1__w_in2*VV_junc1__vj2  # WARNING: circular dependency
    VV_junc1__Qin3 = VV_junc1__w_in3*VV_junc1__vj3  # WARNING: circular dependency
    VV_junc1__Qin4 = VV_junc1__w_in4*VV_junc1__vj4  # WARNING: circular dependency
    VV_junc1__Qout1 = VV_junc1__w_out1*-VV_junc1__vj1  # WARNING: circular dependency
    VV_junc1__Qout2 = VV_junc1__w_out2*-VV_junc1__vj2  # WARNING: circular dependency
    VV_junc1__Qout3 = VV_junc1__w_out3*-VV_junc1__vj3  # WARNING: circular dependency
    VV_junc1__Qout4 = VV_junc1__w_out4*-VV_junc1__vj4  # WARNING: circular dependency
    VV_junc1__Qin_tot = VV_junc1__Qin1+VV_junc1__Qin2+VV_junc1__Qin3+VV_junc1__Qin4  # WARNING: circular dependency
    VV_junc1__Qout_tot = VV_junc1__Qout1+VV_junc1__Qout2+VV_junc1__Qout3+VV_junc1__Qout4  # WARNING: circular dependency
    VV_junc1__n_in = VV_junc1__bc1_is_in+VV_junc1__bc2_is_in+VV_junc1__bc3_is_in+VV_junc1__bc4_is_in  # WARNING: circular dependency
    VV_junc1__n_out = VV_junc1__bc1_is_out+VV_junc1__bc2_is_out+VV_junc1__bc3_is_out+VV_junc1__bc4_is_out  # WARNING: circular dependency
    VV_junc1__FQB_alpha = (VV_junc1__v_alpha+VV_junc1__div_0)/(VV_junc1__v_alpha+VV_junc1__v_beta+2*VV_junc1__div_0)  # WARNING: circular dependency
    VV_junc1__FQE_alpha = 1/(1+np.exp(-(VV_junc1__A+VV_junc1__B*VV_junc1__ph)))  # WARNING: circular dependency
    VV_junc1__B = 1+6.98*(1-VV_junc1__H_mean)/(VV_junc1__D_F*1e6)  # WARNING: circular dependency
    VV_junc1__A = -6.96*np.log(VV_junc1__D_alpha*1e6/(VV_junc1__D_beta*1e6))/(VV_junc1__D_F*1e6)  # WARNING: circular dependency
    VV_junc1__X_0 = 0.4/(VV_junc1__D_F*1e6)  # WARNING: circular dependency
    VV_junc1__ph = np.log(VV_junc1__y/(1-VV_junc1__y))  # WARNING: circular dependency
    VV_junc1__y_raw = (VV_junc1__FQB_alpha-VV_junc1__X_0)/(1-2*VV_junc1__X_0+VV_junc1__div_0)  # WARNING: circular dependency
    VV_junc1__y = np.minimum(np.maximum(VV_junc1__y_raw, VV_junc1__div_0y), 1-VV_junc1__div_0y)  # WARNING: circular dependency
    VV_junc1__H_VV_out_alpha = VV_junc1__H_mean*VV_junc1__FQE_alpha/(VV_junc1__FQB_alpha+VV_junc1__div_0)  # WARNING: circular dependency
    VV_junc1__H_VV_out_beta = VV_junc1__H_mean*(1-VV_junc1__FQE_alpha)/(1-VV_junc1__FQB_alpha+VV_junc1__div_0)  # WARNING: circular dependency
    VV_junc1__RBC_in = VV_junc1__Qin1*inlet__H_R_out+VV_junc1__Qin2*VV_junc1__H_to2+VV_junc1__Qin3*PV1__H_L_out+VV_junc1__Qin4*PV2__H_L_out  # WARNING: circular dependency
    VV_junc1__RBC_out = VV_junc1__Qout1*VV_junc1__H_from1+VV_junc1__Qout2*VV_junc1__H_from2+VV_junc1__Qout3*VV_junc1__H_from3+VV_junc1__Qout4*VV_junc1__H_from4  # WARNING: circular dependency
    VV_junc1__RBC_volume_init = VV_junc1__H_global_L*VV_junc1__q_us  # WARNING: circular dependency
    VV_junc1__H_mean = VV_junc1__RBC_volume/(VV_junc1__q_us+VV_junc1__div_0)  # WARNING: circular dependency
    VV_junc1__q_us = np.pi*np.square(VV_junc1__r)*VV_junc1__l  # WARNING: circular dependency
    VV_junc1__q = VV_junc1__q_us+VV_junc1__q_C+VV_junc1__q_C_d  # WARNING: circular dependency
    VV_junc1__v_mm3_s = VV_junc1__v/VV_junc1__one_mm3  # WARNING: circular dependency
    VV_junc1__u = VV_junc1__q_C/(VV_junc1__C/2)+VV_junc1__u_ext  # WARNING: circular dependency
    VV_junc1__u_mmHg = VV_junc1__u/133.322  # WARNING: circular dependency
    VV_junc1__v = (VV_junc1__u-VV_junc1__u_d)/VV_junc1__R  # WARNING: circular dependency
    VV_junc1__u_d = VV_junc1__q_C_d/(VV_junc1__C/2)+VV_junc1__u_ext  # WARNING: circular dependency
    VV_junc1__u_d_mmHg = VV_junc1__u_d/133.322  # WARNING: circular dependency
    VV_junc1__H_split1 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha1 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta1 == 1 else inlet__H_R_out))  # WARNING: circular dependency
    VV_junc1__H_split2 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha2 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta2 == 1 else VV_junc1__H_to2))  # WARNING: circular dependency
    VV_junc1__H_split3 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha3 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta3 == 1 else PV1__H_L_out))  # WARNING: circular dependency
    VV_junc1__H_split4 = (VV_junc1__H_VV_out_alpha if VV_junc1__alpha4 == 1 else (VV_junc1__H_VV_out_beta if VV_junc1__beta4 == 1 else PV2__H_L_out))  # WARNING: circular dependency
    VV_junc1__H_daughter1 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split1 if VV_junc1__is_split == 1 else inlet__H_R_out))  # WARNING: circular dependency
    VV_junc1__H_daughter2 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split2 if VV_junc1__is_split == 1 else VV_junc1__H_to2))  # WARNING: circular dependency
    VV_junc1__H_daughter3 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split3 if VV_junc1__is_split == 1 else PV1__H_L_out))  # WARNING: circular dependency
    VV_junc1__H_daughter4 = (VV_junc1__H_mean if VV_junc1__is_merge == 1 else (VV_junc1__H_split4 if VV_junc1__is_split == 1 else PV2__H_L_out))  # WARNING: circular dependency
    VV_junc1__H_from1_target = (VV_junc1__H_daughter1 if VV_junc1__bc1_is_out == 1 else inlet__H_R_out)  # WARNING: circular dependency
    VV_junc1__H_from2_target = (VV_junc1__H_daughter2 if VV_junc1__bc2_is_out == 1 else VV_junc1__H_to2)  # WARNING: circular dependency
    VV_junc1__H_from3_target = (VV_junc1__H_daughter3 if VV_junc1__bc3_is_out == 1 else PV1__H_L_out)  # WARNING: circular dependency
    VV_junc1__H_from4_target = (VV_junc1__H_daughter4 if VV_junc1__bc4_is_out == 1 else PV2__H_L_out)  # WARNING: circular dependency
    VV_junc1__bc1_is_in = (1 if VV_junc1__Qin1 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc2_is_in = (1 if VV_junc1__Qin2 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc3_is_in = (1 if VV_junc1__Qin3 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc4_is_in = (1 if VV_junc1__Qin4 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc1_is_out = (1 if VV_junc1__Qout1 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc2_is_out = (1 if VV_junc1__Qout2 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc3_is_out = (1 if VV_junc1__Qout3 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__bc4_is_out = (1 if VV_junc1__Qout4 > VV_junc1__v_threshold else 0)  # WARNING: circular dependency
    VV_junc1__junction_type = (1 if VV_junc1__n_in == 1 else (-1 if VV_junc1__n_in >= 2 else 0))  # WARNING: circular dependency
    VV_junc1__is_split = (1 if VV_junc1__junction_type == 1 else 0)  # WARNING: circular dependency
    VV_junc1__is_merge = (1 if VV_junc1__junction_type == -1 else 0)  # WARNING: circular dependency
    VV_junc1__feed1 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin1 >= VV_junc1__Qin2) and (VV_junc1__Qin1 >= VV_junc1__Qin3) and (VV_junc1__Qin1 >= VV_junc1__Qin4) else 0)  # WARNING: circular dependency
    VV_junc1__feed2 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin2 > VV_junc1__Qin1) and (VV_junc1__Qin2 >= VV_junc1__Qin3) and (VV_junc1__Qin2 >= VV_junc1__Qin4) else 0)  # WARNING: circular dependency
    VV_junc1__feed3 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin3 > VV_junc1__Qin1) and (VV_junc1__Qin3 > VV_junc1__Qin2) and (VV_junc1__Qin3 >= VV_junc1__Qin4) else 0)  # WARNING: circular dependency
    VV_junc1__feed4 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__Qin4 > VV_junc1__Qin1) and (VV_junc1__Qin4 > VV_junc1__Qin2) and (VV_junc1__Qin4 > VV_junc1__Qin3) else 0)  # WARNING: circular dependency
    VV_junc1__alpha1 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc1_is_out == 1) and (VV_junc1__Qout1 >= VV_junc1__Qout2) and (VV_junc1__Qout1 >= VV_junc1__Qout3) and (VV_junc1__Qout1 >= VV_junc1__Qout4) else 0)  # WARNING: circular dependency
    VV_junc1__alpha2 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc2_is_out == 1) and (VV_junc1__Qout2 > VV_junc1__Qout1) and (VV_junc1__Qout2 >= VV_junc1__Qout3) and (VV_junc1__Qout2 >= VV_junc1__Qout4) else 0)  # WARNING: circular dependency
    VV_junc1__alpha3 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc3_is_out == 1) and (VV_junc1__Qout3 > VV_junc1__Qout1) and (VV_junc1__Qout3 > VV_junc1__Qout2) and (VV_junc1__Qout3 >= VV_junc1__Qout4) else 0)  # WARNING: circular dependency
    VV_junc1__alpha4 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc4_is_out == 1) and (VV_junc1__Qout4 > VV_junc1__Qout1) and (VV_junc1__Qout4 > VV_junc1__Qout2) and (VV_junc1__Qout4 > VV_junc1__Qout3) else 0)  # WARNING: circular dependency
    VV_junc1__Qout1_rem = (0 if VV_junc1__alpha1 == 1 else VV_junc1__Qout1)  # WARNING: circular dependency
    VV_junc1__Qout2_rem = (0 if VV_junc1__alpha2 == 1 else VV_junc1__Qout2)  # WARNING: circular dependency
    VV_junc1__Qout3_rem = (0 if VV_junc1__alpha3 == 1 else VV_junc1__Qout3)  # WARNING: circular dependency
    VV_junc1__Qout4_rem = (0 if VV_junc1__alpha4 == 1 else VV_junc1__Qout4)  # WARNING: circular dependency
    VV_junc1__beta1 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc1_is_out == 1) and (VV_junc1__alpha1 == 0) and (VV_junc1__Qout1_rem >= VV_junc1__Qout2_rem) and (VV_junc1__Qout1_rem >= VV_junc1__Qout3_rem) and (VV_junc1__Qout1_rem >= VV_junc1__Qout4_rem) else 0)  # WARNING: circular dependency
    VV_junc1__beta2 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc2_is_out == 1) and (VV_junc1__alpha2 == 0) and (VV_junc1__Qout2_rem > VV_junc1__Qout1_rem) and (VV_junc1__Qout2_rem >= VV_junc1__Qout3_rem) and (VV_junc1__Qout2_rem >= VV_junc1__Qout4_rem) else 0)  # WARNING: circular dependency
    VV_junc1__beta3 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc3_is_out == 1) and (VV_junc1__alpha3 == 0) and (VV_junc1__Qout3_rem > VV_junc1__Qout1_rem) and (VV_junc1__Qout3_rem > VV_junc1__Qout2_rem) and (VV_junc1__Qout3_rem >= VV_junc1__Qout4_rem) else 0)  # WARNING: circular dependency
    VV_junc1__beta4 = (1 if (VV_junc1__is_split == 1) and (VV_junc1__bc4_is_out == 1) and (VV_junc1__alpha4 == 0) and (VV_junc1__Qout4_rem > VV_junc1__Qout1_rem) and (VV_junc1__Qout4_rem > VV_junc1__Qout2_rem) and (VV_junc1__Qout4_rem > VV_junc1__Qout3_rem) else 0)  # WARNING: circular dependency
    VV_junc1__D_F = (VV_junc1__D1 if VV_junc1__feed1 == 1 else (VV_junc1__D2 if VV_junc1__feed2 == 1 else (VV_junc1__D3 if VV_junc1__feed3 == 1 else (VV_junc1__D4 if VV_junc1__feed4 == 1 else VV_junc1__D1))))  # WARNING: circular dependency
    VV_junc1__D_alpha = (VV_junc1__D1 if VV_junc1__alpha1 == 1 else (VV_junc1__D2 if VV_junc1__alpha2 == 1 else (VV_junc1__D3 if VV_junc1__alpha3 == 1 else (VV_junc1__D4 if VV_junc1__alpha4 == 1 else VV_junc1__D3))))  # WARNING: circular dependency
    VV_junc1__D_beta = (VV_junc1__D1 if VV_junc1__beta1 == 1 else (VV_junc1__D2 if VV_junc1__beta2 == 1 else (VV_junc1__D3 if VV_junc1__beta3 == 1 else (VV_junc1__D4 if VV_junc1__beta4 == 1 else VV_junc1__D4))))  # WARNING: circular dependency
    VV_junc1__v_alpha = (VV_junc1__Qout1 if VV_junc1__alpha1 == 1 else (VV_junc1__Qout2 if VV_junc1__alpha2 == 1 else (VV_junc1__Qout3 if VV_junc1__alpha3 == 1 else (VV_junc1__Qout4 if VV_junc1__alpha4 == 1 else 0))))  # WARNING: circular dependency
    VV_junc1__v_beta = (VV_junc1__Qout1 if VV_junc1__beta1 == 1 else (VV_junc1__Qout2 if VV_junc1__beta2 == 1 else (VV_junc1__Qout3 if VV_junc1__beta3 == 1 else (VV_junc1__Qout4 if VV_junc1__beta4 == 1 else 0))))  # WARNING: circular dependency
    VV_junc1__C_max12 = (inlet__C if inlet__C > VV_junc1__C_conn2 else (VV_junc1__C_conn2 if inlet__C <= VV_junc1__C_conn2 else 0.0))  # WARNING: circular dependency
    VV_junc1__C_max123 = (VV_junc1__C_max12 if VV_junc1__C_max12 > PV1__C else (PV1__C if VV_junc1__C_max12 <= PV1__C else 0.0))  # WARNING: circular dependency
    VV_junc1__C = (VV_junc1__C_max123 if VV_junc1__C_max123 > PV2__C else (PV2__C if VV_junc1__C_max123 <= PV2__C else 0.0))  # WARNING: circular dependency
    PV1__R_constriction = PV1__R_constriction_base+(PV1__R_constriction_final-PV1__R_constriction_base)/(1+np.exp(-(t-PV1__t0)/PV1__tau_sig))  # WARNING: circular dependency
    PV1__w_v = 0.5+1/np.pi*np.arctan(PV1__v/PV1__v_scale)  # WARNING: circular dependency
    PV1__w_v_d = 0.5+1/np.pi*np.arctan(PV1__v_d/PV1__v_scale)  # WARNING: circular dependency
    PV1__H_up = PV1__w_v_d*PV1__H_L_in+(1-PV1__w_v_d)*PV1__H_R_in  # WARNING: circular dependency
    PV1__H_down_target = PV1__s_v_d*(PV1__H_mean+PV1__gamma_mirror*(PV1__H_mean-PV1__H_up))+(1-PV1__s_v_d)*PV1__H_mean  # WARNING: circular dependency
    PV1__s_v_d = np.abs(PV1__v_d)/(np.abs(PV1__v_d)+PV1__v_eps)  # WARNING: circular dependency
    PV1__H_L_out = (1-PV1__w_v_d)*PV1__H_down+PV1__w_v_d*PV1__H_L_in  # WARNING: circular dependency
    PV1__H_R_out = PV1__w_v_d*PV1__H_down+(1-PV1__w_v_d)*PV1__H_R_in  # WARNING: circular dependency
    PV1__RBC_volume_init = PV1__H_global_L*PV1__q_us  # WARNING: circular dependency
    PV1__v_pos = PV1__w_v*PV1__v  # WARNING: circular dependency
    PV1__v_neg = (1-PV1__w_v)*-PV1__v  # WARNING: circular dependency
    PV1__v_d_pos = PV1__w_v_d*PV1__v_d  # WARNING: circular dependency
    PV1__v_d_neg = (1-PV1__w_v_d)*-PV1__v_d  # WARNING: circular dependency
    PV1__H_mean = PV1__RBC_volume/PV1__q  # WARNING: circular dependency
    PV1__H_mass_L = PV1__w_v*PV1__H_L_in+(1-PV1__w_v)*PV1__H_L_out  # WARNING: circular dependency
    PV1__H_mass_R = PV1__w_v_d*PV1__H_R_out+(1-PV1__w_v_d)*PV1__H_R_in  # WARNING: circular dependency
    PV1__q_us = np.pi*np.square(PV1__r)*PV1__l  # WARNING: circular dependency
    PV1__q = PV1__q_us+PV1__q_C  # WARNING: circular dependency
    PV1__C = np.pi*np.square(8.5e-9)*PV1__l/133.322  # WARNING: circular dependency
    PV1__Z = (0.8+np.exp(-0.075*2*PV1__r*1e6))*(-1+1/(1+np.power(10, -11)*np.power(2*PV1__r*1e6, 12)))+1/(1+np.power(10, -11)*np.power(2*PV1__r*1e6, 12))  # WARNING: circular dependency
    PV1__mu_45 = 6*np.exp(-0.085*2*PV1__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*PV1__r*1e6, 0.645))  # WARNING: circular dependency
    PV1__mu = PV1__hem_dep_u_rel*PV1__mu_plasma  # WARNING: circular dependency
    PV1__hem_dep_u_rel = 1+(PV1__mu_45-1)*(np.power(1-PV1__H_mean, PV1__Z)-1)/(np.power(1-PV1__H_global_L, PV1__Z)-1)*np.square(2*PV1__r*1e6/(2*PV1__r*1e6-1.1))  # WARNING: circular dependency
    PV1__R = 8*PV1__mu*PV1__l/(np.pi*np.power(PV1__r, 4))+PV1__R_constriction  # WARNING: circular dependency
    PV1__v_mm3_s = PV1__v/PV1__one_mm3  # WARNING: circular dependency
    PV1__v = (VV_junc1__u_d-PV1__u)/(PV1__R/2)  # WARNING: circular dependency
    PV1__u_mmHg = PV1__u/133.322  # WARNING: circular dependency
    PV1__u = PV1__q_C/PV1__C+PV1__u_ext  # WARNING: circular dependency
    PV1__v_d_mm3_s = PV1__v_d/PV1__one_mm3  # WARNING: circular dependency
    PV1__v_d = (PV1__u-V1__u)/(PV1__R/2)  # WARNING: circular dependency
    PV2__R_constriction = PV2__R_constriction_base+(PV2__R_constriction_final-PV2__R_constriction_base)/(1+np.exp(-(t-PV2__t0)/PV2__tau_sig))  # WARNING: circular dependency
    PV2__w_v = 0.5+1/np.pi*np.arctan(PV2__v/PV2__v_scale)  # WARNING: circular dependency
    PV2__w_v_d = 0.5+1/np.pi*np.arctan(PV2__v_d/PV2__v_scale)  # WARNING: circular dependency
    PV2__H_up = PV2__w_v_d*PV2__H_L_in+(1-PV2__w_v_d)*PV2__H_R_in  # WARNING: circular dependency
    PV2__H_down_target = PV2__s_v_d*(PV2__H_mean+PV2__gamma_mirror*(PV2__H_mean-PV2__H_up))+(1-PV2__s_v_d)*PV2__H_mean  # WARNING: circular dependency
    PV2__s_v_d = np.abs(PV2__v_d)/(np.abs(PV2__v_d)+PV2__v_eps)  # WARNING: circular dependency
    PV2__H_L_out = (1-PV2__w_v_d)*PV2__H_down+PV2__w_v_d*PV2__H_L_in  # WARNING: circular dependency
    PV2__H_R_out = PV2__w_v_d*PV2__H_down+(1-PV2__w_v_d)*PV2__H_R_in  # WARNING: circular dependency
    PV2__RBC_volume_init = PV2__H_global_L*PV2__q_us  # WARNING: circular dependency
    PV2__v_pos = PV2__w_v*PV2__v  # WARNING: circular dependency
    PV2__v_neg = (1-PV2__w_v)*-PV2__v  # WARNING: circular dependency
    PV2__v_d_pos = PV2__w_v_d*PV2__v_d  # WARNING: circular dependency
    PV2__v_d_neg = (1-PV2__w_v_d)*-PV2__v_d  # WARNING: circular dependency
    PV2__H_mean = PV2__RBC_volume/PV2__q  # WARNING: circular dependency
    PV2__H_mass_L = PV2__w_v*PV2__H_L_in+(1-PV2__w_v)*PV2__H_L_out  # WARNING: circular dependency
    PV2__H_mass_R = PV2__w_v_d*PV2__H_R_out+(1-PV2__w_v_d)*PV2__H_R_in  # WARNING: circular dependency
    PV2__q_us = np.pi*np.square(PV2__r)*PV2__l  # WARNING: circular dependency
    PV2__q = PV2__q_us+PV2__q_C  # WARNING: circular dependency
    PV2__C = np.pi*np.square(8.5e-9)*PV2__l/133.322  # WARNING: circular dependency
    PV2__Z = (0.8+np.exp(-0.075*2*PV2__r*1e6))*(-1+1/(1+np.power(10, -11)*np.power(2*PV2__r*1e6, 12)))+1/(1+np.power(10, -11)*np.power(2*PV2__r*1e6, 12))  # WARNING: circular dependency
    PV2__mu_45 = 6*np.exp(-0.085*2*PV2__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*PV2__r*1e6, 0.645))  # WARNING: circular dependency
    PV2__mu = PV2__hem_dep_u_rel*PV2__mu_plasma  # WARNING: circular dependency
    PV2__hem_dep_u_rel = 1+(PV2__mu_45-1)*(np.power(1-PV2__H_mean, PV2__Z)-1)/(np.power(1-PV2__H_global_L, PV2__Z)-1)*np.square(2*PV2__r*1e6/(2*PV2__r*1e6-1.1))  # WARNING: circular dependency
    PV2__R = 8*PV2__mu*PV2__l/(np.pi*np.power(PV2__r, 4))+PV2__R_constriction  # WARNING: circular dependency
    PV2__v_mm3_s = PV2__v/PV2__one_mm3  # WARNING: circular dependency
    PV2__v = (VV_junc1__u_d-PV2__u)/(PV2__R/2)  # WARNING: circular dependency
    PV2__u_mmHg = PV2__u/133.322  # WARNING: circular dependency
    PV2__u = PV2__q_C/PV2__C+PV2__u_ext  # WARNING: circular dependency
    PV2__v_d_mm3_s = PV2__v_d/PV2__one_mm3  # WARNING: circular dependency
    PV2__v_d = (PV2__u-V2__u)/(PV2__R/2)  # WARNING: circular dependency
    V1__w_v = 0.5+1/np.pi*np.arctan(V1__v/V1__v_scale)  # WARNING: circular dependency
    V1__H_up = V1__w_v*V1__H_L_in+(1-V1__w_v)*V1__H_R_in  # WARNING: circular dependency
    V1__H_down_target = V1__s_v*(V1__H_mean+V1__gamma_mirror*(V1__H_mean-V1__H_up))+(1-V1__s_v)*V1__H_mean  # WARNING: circular dependency
    V1__s_v = np.abs(V1__v)/(np.abs(V1__v)+V1__v_eps)  # WARNING: circular dependency
    V1__H_L_out = (1-V1__w_v)*V1__H_down+V1__w_v*V1__H_L_in  # WARNING: circular dependency
    V1__H_R_out = V1__w_v*V1__H_down+(1-V1__w_v)*V1__H_R_in  # WARNING: circular dependency
    V1__RBC_volume_init = V1__H_global_L*V1__q_us  # WARNING: circular dependency
    V1__v_pos = V1__w_v*V1__v  # WARNING: circular dependency
    V1__v_neg = (1-V1__w_v)*-V1__v  # WARNING: circular dependency
    V1__H_mean = V1__RBC_volume/V1__q  # WARNING: circular dependency
    V1__H_mass_L = V1__w_v*V1__H_L_in+(1-V1__w_v)*V1__H_L_out  # WARNING: circular dependency
    V1__H_mass_R = V1__w_v*V1__H_R_out+(1-V1__w_v)*V1__H_R_in  # WARNING: circular dependency
    V1__q_us = np.pi*np.square(V1__r)*V1__l  # WARNING: circular dependency
    V1__q = V1__q_us+V1__q_C  # WARNING: circular dependency
    V1__C = np.pi*np.square(8.5e-9)*V1__l/133.322  # WARNING: circular dependency
    V1__Z = (0.8+np.exp(-0.075*2*V1__r*1e6))*(-1+1/(1+np.power(10, -11)*np.power(2*V1__r*1e6, 12)))+1/(1+np.power(10, -11)*np.power(2*V1__r*1e6, 12))  # WARNING: circular dependency
    V1__mu_45 = 6*np.exp(-0.085*2*V1__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*V1__r*1e6, 0.645))  # WARNING: circular dependency
    V1__mu = V1__hem_dep_u_rel*V1__mu_plasma  # WARNING: circular dependency
    V1__hem_dep_u_rel = 1+(V1__mu_45-1)*(np.power(1-V1__H_mean, V1__Z)-1)/(np.power(1-V1__H_global_L, V1__Z)-1)*np.square(2*V1__r*1e6/(2*V1__r*1e6-1.1))  # WARNING: circular dependency
    V1__R = 8*V1__mu*V1__l/(np.pi*np.power(V1__r, 4))  # WARNING: circular dependency
    V1__v_mm3_s = V1__v/V1__one_mm3  # WARNING: circular dependency
    V1__v = (V1__u-V1__u_out)/V1__R  # WARNING: circular dependency
    V1__u_mmHg = V1__u/133.322  # WARNING: circular dependency
    V1__u = V1__q_C/V1__C+V1__u_ext  # WARNING: circular dependency
    V2__w_v = 0.5+1/np.pi*np.arctan(V2__v/V2__v_scale)  # WARNING: circular dependency
    V2__H_up = V2__w_v*V2__H_L_in+(1-V2__w_v)*V2__H_R_in  # WARNING: circular dependency
    V2__H_down_target = V2__s_v*(V2__H_mean+V2__gamma_mirror*(V2__H_mean-V2__H_up))+(1-V2__s_v)*V2__H_mean  # WARNING: circular dependency
    V2__s_v = np.abs(V2__v)/(np.abs(V2__v)+V2__v_eps)  # WARNING: circular dependency
    V2__H_L_out = (1-V2__w_v)*V2__H_down+V2__w_v*V2__H_L_in  # WARNING: circular dependency
    V2__H_R_out = V2__w_v*V2__H_down+(1-V2__w_v)*V2__H_R_in  # WARNING: circular dependency
    V2__RBC_volume_init = V2__H_global_L*V2__q_us  # WARNING: circular dependency
    V2__v_pos = V2__w_v*V2__v  # WARNING: circular dependency
    V2__v_neg = (1-V2__w_v)*-V2__v  # WARNING: circular dependency
    V2__H_mean = V2__RBC_volume/V2__q  # WARNING: circular dependency
    V2__H_mass_L = V2__w_v*V2__H_L_in+(1-V2__w_v)*V2__H_L_out  # WARNING: circular dependency
    V2__H_mass_R = V2__w_v*V2__H_R_out+(1-V2__w_v)*V2__H_R_in  # WARNING: circular dependency
    V2__q_us = np.pi*np.square(V2__r)*V2__l  # WARNING: circular dependency
    V2__q = V2__q_us+V2__q_C  # WARNING: circular dependency
    V2__C = np.pi*np.square(8.5e-9)*V2__l/133.322  # WARNING: circular dependency
    V2__Z = (0.8+np.exp(-0.075*2*V2__r*1e6))*(-1+1/(1+np.power(10, -11)*np.power(2*V2__r*1e6, 12)))+1/(1+np.power(10, -11)*np.power(2*V2__r*1e6, 12))  # WARNING: circular dependency
    V2__mu_45 = 6*np.exp(-0.085*2*V2__r*1e6)+3.2-2.44*np.exp(-0.06*np.power(2*V2__r*1e6, 0.645))  # WARNING: circular dependency
    V2__mu = V2__hem_dep_u_rel*V2__mu_plasma  # WARNING: circular dependency
    V2__hem_dep_u_rel = 1+(V2__mu_45-1)*(np.power(1-V2__H_mean, V2__Z)-1)/(np.power(1-V2__H_global_L, V2__Z)-1)*np.square(2*V2__r*1e6/(2*V2__r*1e6-1.1))  # WARNING: circular dependency
    V2__R = 8*V2__mu*V2__l/(np.pi*np.power(V2__r, 4))  # WARNING: circular dependency
    V2__v_mm3_s = V2__v/V2__one_mm3  # WARNING: circular dependency
    V2__v = (V2__u-V2__u_out)/V2__R  # WARNING: circular dependency
    V2__u_mmHg = V2__u/133.322  # WARNING: circular dependency
    V2__u = V2__q_C/V2__C+V2__u_ext  # WARNING: circular dependency

    # -- assemble dydt -----------------------------------
    dydt = np.zeros(len(y))
    dydt[0] = (VV_junc1__H_from1-inlet__H_link_R)/inlet__tau_link  # d(inlet__H_link_R)/dt
    dydt[1] = (inlet__H_R_out_LHS-inlet__H_link_L)/inlet__tau_link  # d(inlet__H_link_L)/dt
    dydt[2] = (inlet__H_down_target-inlet__H_down)/inlet__tau_H_down  # d(inlet__H_down)/dt
    dydt[3] = inlet__v*inlet__H_mass_L-inlet__v_d*inlet__H_mass_R  # d(inlet__RBC_volume)/dt
    dydt[4] = inlet__v-inlet__v_d  # d(inlet__q_C)/dt
    dydt[5] = VV_junc1__RBC_in-VV_junc1__RBC_out  # d(VV_junc1__RBC_volume)/dt
    dydt[6] = inlet__v_d+VV_junc1__vbc2-VV_junc1__v  # d(VV_junc1__q_C)/dt
    dydt[7] = VV_junc1__v-PV1__v-PV2__v  # d(VV_junc1__q_C_d)/dt
    dydt[8] = (V1__H_L_out-PV1__H_link_R)/PV1__tau_link  # d(PV1__H_link_R)/dt
    dydt[9] = (VV_junc1__H_from3-PV1__H_link_L)/PV1__tau_link  # d(PV1__H_link_L)/dt
    dydt[10] = (PV1__H_down_target-PV1__H_down)/PV1__tau_H_down  # d(PV1__H_down)/dt
    dydt[11] = PV1__v*PV1__H_mass_L-PV1__v_d*PV1__H_mass_R  # d(PV1__RBC_volume)/dt
    dydt[12] = PV1__v-PV1__v_d  # d(PV1__q_C)/dt
    dydt[13] = (V2__H_L_out-PV2__H_link_R)/PV2__tau_link  # d(PV2__H_link_R)/dt
    dydt[14] = (VV_junc1__H_from4-PV2__H_link_L)/PV2__tau_link  # d(PV2__H_link_L)/dt
    dydt[15] = (PV2__H_down_target-PV2__H_down)/PV2__tau_H_down  # d(PV2__H_down)/dt
    dydt[16] = PV2__v*PV2__H_mass_L-PV2__v_d*PV2__H_mass_R  # d(PV2__RBC_volume)/dt
    dydt[17] = PV2__v-PV2__v_d  # d(PV2__q_C)/dt
    dydt[18] = (V1__H_L_out_RHS-V1__H_link_R)/V1__tau_link  # d(V1__H_link_R)/dt
    dydt[19] = (PV1__H_R_out-V1__H_link_L)/V1__tau_link  # d(V1__H_link_L)/dt
    dydt[20] = (V1__H_down_target-V1__H_down)/V1__tau_H_down  # d(V1__H_down)/dt
    dydt[21] = PV1__v_d*V1__H_mass_L-V1__v*V1__H_mass_R  # d(V1__RBC_volume)/dt
    dydt[22] = PV1__v_d-V1__v  # d(V1__q_C)/dt
    dydt[23] = (V2__H_L_out_RHS-V2__H_link_R)/V2__tau_link  # d(V2__H_link_R)/dt
    dydt[24] = (PV2__H_R_out-V2__H_link_L)/V2__tau_link  # d(V2__H_link_L)/dt
    dydt[25] = (V2__H_down_target-V2__H_down)/V2__tau_H_down  # d(V2__H_down)/dt
    dydt[26] = PV2__v_d*V2__H_mass_L-V2__v*V2__H_mass_R  # d(V2__RBC_volume)/dt
    dydt[27] = PV2__v_d-V2__v  # d(V2__q_C)/dt

    return dydt

# ================================================================
# SOLVER DRIVER
# ================================================================

if __name__ == "__main__":
    t_start = 0.0
    t_end   = 1000.0
    t_eval  = np.linspace(t_start, t_end, 10001)

    print("Running simulation ...")
    sol = solve_ivp(
        ode_rhs,
        [t_start, t_end],
        y0,
        method="LSODA",
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-12,
        max_step=0.1,
    )

    if sol.success:
        print(f"Solved OK.  {sol.t.shape[0]} time points.")
        idx_v = (state_names.index("inlet__q_C")
                 if "inlet__q_C" in state_names else 0)
        plt.figure()
        plt.plot(sol.t, sol.y[idx_v])
        plt.xlabel("Time (s)")
        plt.ylabel(state_names[idx_v])
        plt.title("State variable trace")
        plt.tight_layout()
        plt.savefig("simulation_output.png", dpi=150)
        print("Plot saved to simulation_output.png")
    else:
        print(f"Solver failed: {sol.message}")
