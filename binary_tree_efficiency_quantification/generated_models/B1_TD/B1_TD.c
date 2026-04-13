/*
   There are a total of 207 entries in the algebraic variable array.
   There are a total of 28 entries in each of the rate and state variable arrays.
   There are a total of 86 entries in the constant variable array.
 */
/*
 * VOI is time in component environment (second).
 * CONSTANTS[0] is H_global_L in component parameters_global (dimensionless).
 * CONSTANTS[1] is H_global_R in component parameters_global (dimensionless).
 * CONSTANTS[2] is H_R_out_LHS_inlet in component parameters (dimensionless).
 * CONSTANTS[3] is gamma_mirror in component parameters_global (dimensionless).
 * CONSTANTS[4] is tau_H_down in component parameters_global (second).
 * CONSTANTS[5] is tau_H_mean in component parameters_global (second).
 * CONSTANTS[6] is v_eps in component parameters_global (m3_per_s).
 * CONSTANTS[7] is q_C_init in component parameters_global (m3).
 * CONSTANTS[8] is r_inlet in component parameters (metre).
 * CONSTANTS[9] is mu_plasma in component parameters_global (Js_per_m3).
 * CONSTANTS[10] is u_in_inlet in component parameters (J_per_m3).
 * CONSTANTS[11] is u_ext in component parameters_global (J_per_m3).
 * CONSTANTS[12] is tau_link in component parameters_global (second).
 * CONSTANTS[13] is v_scale in component parameters_global (m3_per_s).
 * CONSTANTS[14] is one_mm3 in component parameters_global (m3).
 * ALGEBRAIC[12] is w_v in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[20] is w_v_d in component PP_capillary_H_D (dimensionless).
 * STATES[0] is H_link_R in component PP_capillary_H_D (dimensionless).
 * STATES[1] is H_link_L in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[1] is H_L_in in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[2] is H_R_in in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[21] is H_up in component PP_capillary_H_D (dimensionless).
 * STATES[2] is H_down in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[27] is H_down_target in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[25] is s_v_d in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[24] is H_L_out in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[26] is H_R_out in component PP_capillary_H_D (dimensionless).
 * STATES[3] is RBC_volume in component PP_capillary_H_D (m3).
 * CONSTANTS[55] is RBC_volume_init in component PP_capillary_H_D (m3).
 * ALGEBRAIC[13] is v_pos in component PP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[14] is v_neg in component PP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[22] is v_d_pos in component PP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[23] is v_d_neg in component PP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[4] is H_mean in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[28] is H_mass_L in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[30] is H_mass_R in component PP_capillary_H_D (dimensionless).
 * STATES[4] is q_C in component PP_capillary_H_D (m3).
 * ALGEBRAIC[3] is q in component PP_capillary_H_D (m3).
 * CONSTANTS[45] is q_us in component PP_capillary_H_D (m3).
 * CONSTANTS[46] is C in component PP_capillary_H_D (m6_per_J).
 * CONSTANTS[49] is Z in component PP_capillary_H_D (dimensionless).
 * CONSTANTS[59] is mu_45 in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[6] is mu in component PP_capillary_H_D (Js_per_m3).
 * ALGEBRAIC[5] is hem_dep_u_rel in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[7] is R in component PP_capillary_H_D (Js_per_m6).
 * ALGEBRAIC[10] is v in component PP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[11] is v_mm3_s in component PP_capillary_H_D (mm3_per_s).
 * ALGEBRAIC[8] is u in component PP_capillary_H_D (J_per_m3).
 * ALGEBRAIC[9] is u_mmHg in component PP_capillary_H_D (dimensionless).
 * ALGEBRAIC[18] is v_d in component PP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[19] is v_d_mm3_s in component PP_capillary_H_D (mm3_per_s).
 * CONSTANTS[15] is div_0 in component parameters_global (dimensionless).
 * CONSTANTS[16] is div_0y in component parameters_global (dimensionless).
 * CONSTANTS[17] is tau_junc in component parameters_global (second).
 * CONSTANTS[18] is v_threshold in component parameters_global (m3_per_s).
 * CONSTANTS[19] is k in component parameters_global (dimensionless).
 * CONSTANTS[20] is r_VV_junc1 in component parameters (metre).
 * CONSTANTS[21] is vbc2_VV_junc1 in component parameters (m3_per_s).
 * ALGEBRAIC[29] is vj1 in component VV_junction_H_D (m3_per_s).
 * CONSTANTS[64] is vj2 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[53] is vj3 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[74] is vj4 in component VV_junction_H_D (m3_per_s).
 * CONSTANTS[22] is H_to2_VV_junc1 in component parameters (dimensionless).
 * ALGEBRAIC[120] is H_split1 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[121] is H_split2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[152] is H_split3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[187] is H_split4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[122] is H_daughter1 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[123] is H_daughter2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[159] is H_daughter3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[194] is H_daughter4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[124] is H_from1_target in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[125] is H_from2_target in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[163] is H_from3_target in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[199] is H_from4_target in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[126] is H_from1 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[127] is H_from2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[166] is H_from3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[203] is H_from4 in component VV_junction_H_D (dimensionless).
 * CONSTANTS[23] is r_bc2_VV_junc1 in component parameters (metre).
 * CONSTANTS[66] is D1 in component VV_junction_H_D (metre).
 * CONSTANTS[67] is D2 in component VV_junction_H_D (metre).
 * CONSTANTS[70] is D3 in component VV_junction_H_D (metre).
 * CONSTANTS[71] is D4 in component VV_junction_H_D (metre).
 * ALGEBRAIC[31] is w_in1 in component VV_junction_H_D (dimensionless).
 * CONSTANTS[72] is w_in2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[54] is w_in3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[76] is w_in4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[32] is w_out1 in component VV_junction_H_D (dimensionless).
 * CONSTANTS[73] is w_out2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[55] is w_out3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[77] is w_out4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[33] is Qin1 in component VV_junction_H_D (m3_per_s).
 * CONSTANTS[74] is Qin2 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[56] is Qin3 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[78] is Qin4 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[34] is Qout1 in component VV_junction_H_D (m3_per_s).
 * CONSTANTS[75] is Qout2 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[57] is Qout3 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[80] is Qout4 in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[79] is Qin_tot in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[81] is Qout_tot in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[35] is bc1_is_in in component VV_junction_H_D (dimensionless).
 * CONSTANTS[76] is bc2_is_in in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[58] is bc3_is_in in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[82] is bc4_is_in in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[36] is bc1_is_out in component VV_junction_H_D (dimensionless).
 * CONSTANTS[77] is bc2_is_out in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[59] is bc3_is_out in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[83] is bc4_is_out in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[85] is n_in in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[84] is n_out in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[86] is junction_type in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[87] is is_split in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[88] is is_merge in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[89] is feed1 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[90] is feed2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[91] is feed3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[92] is feed4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[93] is alpha1 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[94] is alpha2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[95] is alpha3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[96] is alpha4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[97] is Qout1_rem in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[98] is Qout2_rem in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[99] is Qout3_rem in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[100] is Qout4_rem in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[101] is beta1 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[102] is beta2 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[103] is beta3 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[104] is beta4 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[105] is D_F in component VV_junction_H_D (metre).
 * ALGEBRAIC[106] is D_alpha in component VV_junction_H_D (metre).
 * ALGEBRAIC[107] is D_beta in component VV_junction_H_D (metre).
 * ALGEBRAIC[108] is v_alpha in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[109] is v_beta in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[110] is FQB_alpha in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[117] is FQE_alpha in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[111] is B in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[112] is A in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[113] is X_0 in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[116] is ph in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[114] is y_raw in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[115] is y in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[118] is H_VV_out_alpha in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[119] is H_VV_out_beta in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[205] is RBC_in in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[206] is RBC_out in component VV_junction_H_D (m3_per_s).
 * CONSTANTS[56] is RBC_volume_init in component VV_junction_H_D (m3).
 * STATES[5] is RBC_volume in component VV_junction_H_D (m3).
 * ALGEBRAIC[15] is H_mean in component VV_junction_H_D (dimensionless).
 * CONSTANTS[24] is C_conn2_VV_junc1 in component parameters (m6_per_J).
 * CONSTANTS[57] is C_max12 in component VV_junction_H_D (m6_per_J).
 * CONSTANTS[65] is C_max123 in component VV_junction_H_D (m6_per_J).
 * CONSTANTS[69] is C in component VV_junction_H_D (m6_per_J).
 * STATES[6] is q_C in component VV_junction_H_D (m3).
 * STATES[7] is q_C_d in component VV_junction_H_D (m3).
 * ALGEBRAIC[0] is q in component VV_junction_H_D (m3).
 * CONSTANTS[47] is q_us in component VV_junction_H_D (m3).
 * CONSTANTS[25] is R in component parameters_global (Js_per_m6).
 * ALGEBRAIC[16] is u in component VV_junction_H_D (J_per_m3).
 * ALGEBRAIC[17] is u_mmHg in component VV_junction_H_D (dimensionless).
 * ALGEBRAIC[39] is v in component VV_junction_H_D (m3_per_s).
 * ALGEBRAIC[40] is v_mm3_s in component VV_junction_H_D (mm3_per_s).
 * ALGEBRAIC[37] is u_d in component VV_junction_H_D (J_per_m3).
 * ALGEBRAIC[38] is u_d_mmHg in component VV_junction_H_D (dimensionless).
 * CONSTANTS[26] is R_constriction_base in component parameters_global (Js_per_m6).
 * CONSTANTS[27] is R_constriction_final_PV1 in component parameters (Js_per_m6).
 * ALGEBRAIC[41] is R_constriction in component PP_pericyte_H_D (Js_per_m6).
 * CONSTANTS[28] is tau_sig in component parameters_global (second).
 * CONSTANTS[29] is t0 in component parameters_global (second).
 * CONSTANTS[30] is r_PV1 in component parameters (metre).
 * ALGEBRAIC[60] is w_v in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[141] is w_v_d in component PP_pericyte_H_D (dimensionless).
 * STATES[8] is H_link_R in component PP_pericyte_H_D (dimensionless).
 * STATES[9] is H_link_L in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[42] is H_L_in in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[43] is H_R_in in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[144] is H_up in component PP_pericyte_H_D (dimensionless).
 * STATES[10] is H_down in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[157] is H_down_target in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[150] is s_v_d in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[147] is H_L_out in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[151] is H_R_out in component PP_pericyte_H_D (dimensionless).
 * STATES[11] is RBC_volume in component PP_pericyte_H_D (m3).
 * CONSTANTS[58] is RBC_volume_init in component PP_pericyte_H_D (m3).
 * ALGEBRAIC[61] is v_pos in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[62] is v_neg in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[145] is v_d_pos in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[146] is v_d_neg in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[45] is H_mean in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[158] is H_mass_L in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[162] is H_mass_R in component PP_pericyte_H_D (dimensionless).
 * STATES[12] is q_C in component PP_pericyte_H_D (m3).
 * ALGEBRAIC[44] is q in component PP_pericyte_H_D (m3).
 * CONSTANTS[48] is q_us in component PP_pericyte_H_D (m3).
 * CONSTANTS[63] is C in component PP_pericyte_H_D (m6_per_J).
 * CONSTANTS[78] is Z in component PP_pericyte_H_D (dimensionless).
 * CONSTANTS[79] is mu_45 in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[47] is mu in component PP_pericyte_H_D (Js_per_m3).
 * ALGEBRAIC[46] is hem_dep_u_rel in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[48] is R in component PP_pericyte_H_D (Js_per_m6).
 * ALGEBRAIC[51] is v in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[52] is v_mm3_s in component PP_pericyte_H_D (mm3_per_s).
 * ALGEBRAIC[49] is u in component PP_pericyte_H_D (J_per_m3).
 * ALGEBRAIC[50] is u_mmHg in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[139] is v_d in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[142] is v_d_mm3_s in component PP_pericyte_H_D (mm3_per_s).
 * CONSTANTS[31] is R_constriction_final_PV2 in component parameters (Js_per_m6).
 * ALGEBRAIC[63] is R_constriction in component PP_pericyte_H_D (Js_per_m6).
 * CONSTANTS[32] is r_PV2 in component parameters (metre).
 * ALGEBRAIC[128] is w_v in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[178] is w_v_d in component PP_pericyte_H_D (dimensionless).
 * STATES[13] is H_link_R in component PP_pericyte_H_D (dimensionless).
 * STATES[14] is H_link_L in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[64] is H_L_in in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[65] is H_R_in in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[181] is H_up in component PP_pericyte_H_D (dimensionless).
 * STATES[15] is H_down in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[195] is H_down_target in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[188] is s_v_d in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[182] is H_L_out in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[189] is H_R_out in component PP_pericyte_H_D (dimensionless).
 * STATES[16] is RBC_volume in component PP_pericyte_H_D (m3).
 * CONSTANTS[60] is RBC_volume_init in component PP_pericyte_H_D (m3).
 * ALGEBRAIC[130] is v_pos in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[131] is v_neg in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[183] is v_d_pos in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[184] is v_d_neg in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[67] is H_mean in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[196] is H_mass_L in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[200] is H_mass_R in component PP_pericyte_H_D (dimensionless).
 * STATES[17] is q_C in component PP_pericyte_H_D (m3).
 * ALGEBRAIC[66] is q in component PP_pericyte_H_D (m3).
 * CONSTANTS[50] is q_us in component PP_pericyte_H_D (m3).
 * CONSTANTS[68] is C in component PP_pericyte_H_D (m6_per_J).
 * CONSTANTS[80] is Z in component PP_pericyte_H_D (dimensionless).
 * CONSTANTS[81] is mu_45 in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[69] is mu in component PP_pericyte_H_D (Js_per_m3).
 * ALGEBRAIC[68] is hem_dep_u_rel in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[70] is R in component PP_pericyte_H_D (Js_per_m6).
 * ALGEBRAIC[72] is v in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[75] is v_mm3_s in component PP_pericyte_H_D (mm3_per_s).
 * ALGEBRAIC[71] is u in component PP_pericyte_H_D (J_per_m3).
 * ALGEBRAIC[73] is u_mmHg in component PP_pericyte_H_D (dimensionless).
 * ALGEBRAIC[176] is v_d in component PP_pericyte_H_D (m3_per_s).
 * ALGEBRAIC[179] is v_d_mm3_s in component PP_pericyte_H_D (mm3_per_s).
 * CONSTANTS[33] is H_L_out_RHS_V1 in component parameters (dimensionless).
 * CONSTANTS[34] is r_V1 in component parameters (metre).
 * CONSTANTS[35] is u_out_V1 in component parameters (J_per_m3).
 * ALGEBRAIC[148] is w_v in component VP_capillary_H_D (dimensionless).
 * STATES[18] is H_link_R in component VP_capillary_H_D (dimensionless).
 * STATES[19] is H_link_L in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[129] is H_L_in in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[132] is H_R_in in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[153] is H_up in component VP_capillary_H_D (dimensionless).
 * STATES[20] is H_down in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[164] is H_down_target in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[160] is s_v in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[154] is H_L_out in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[161] is H_R_out in component VP_capillary_H_D (dimensionless).
 * STATES[21] is RBC_volume in component VP_capillary_H_D (m3).
 * CONSTANTS[61] is RBC_volume_init in component VP_capillary_H_D (m3).
 * ALGEBRAIC[155] is v_pos in component VP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[156] is v_neg in component VP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[134] is H_mean in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[165] is H_mass_L in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[167] is H_mass_R in component VP_capillary_H_D (dimensionless).
 * STATES[22] is q_C in component VP_capillary_H_D (m3).
 * ALGEBRAIC[133] is q in component VP_capillary_H_D (m3).
 * CONSTANTS[51] is q_us in component VP_capillary_H_D (m3).
 * CONSTANTS[52] is C in component VP_capillary_H_D (m6_per_J).
 * CONSTANTS[82] is Z in component VP_capillary_H_D (dimensionless).
 * CONSTANTS[83] is mu_45 in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[136] is mu in component VP_capillary_H_D (Js_per_m3).
 * ALGEBRAIC[135] is hem_dep_u_rel in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[137] is R in component VP_capillary_H_D (Js_per_m6).
 * ALGEBRAIC[143] is v in component VP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[149] is v_mm3_s in component VP_capillary_H_D (mm3_per_s).
 * ALGEBRAIC[138] is u in component VP_capillary_H_D (J_per_m3).
 * ALGEBRAIC[140] is u_mmHg in component VP_capillary_H_D (dimensionless).
 * CONSTANTS[36] is H_L_out_RHS_V2 in component parameters (dimensionless).
 * CONSTANTS[37] is r_V2 in component parameters (metre).
 * CONSTANTS[38] is u_out_V2 in component parameters (J_per_m3).
 * ALGEBRAIC[185] is w_v in component VP_capillary_H_D (dimensionless).
 * STATES[23] is H_link_R in component VP_capillary_H_D (dimensionless).
 * STATES[24] is H_link_L in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[168] is H_L_in in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[169] is H_R_in in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[190] is H_up in component VP_capillary_H_D (dimensionless).
 * STATES[25] is H_down in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[201] is H_down_target in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[197] is s_v in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[191] is H_L_out in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[198] is H_R_out in component VP_capillary_H_D (dimensionless).
 * STATES[26] is RBC_volume in component VP_capillary_H_D (m3).
 * CONSTANTS[62] is RBC_volume_init in component VP_capillary_H_D (m3).
 * ALGEBRAIC[192] is v_pos in component VP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[193] is v_neg in component VP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[171] is H_mean in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[202] is H_mass_L in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[204] is H_mass_R in component VP_capillary_H_D (dimensionless).
 * STATES[27] is q_C in component VP_capillary_H_D (m3).
 * ALGEBRAIC[170] is q in component VP_capillary_H_D (m3).
 * CONSTANTS[53] is q_us in component VP_capillary_H_D (m3).
 * CONSTANTS[54] is C in component VP_capillary_H_D (m6_per_J).
 * CONSTANTS[84] is Z in component VP_capillary_H_D (dimensionless).
 * CONSTANTS[85] is mu_45 in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[173] is mu in component VP_capillary_H_D (Js_per_m3).
 * ALGEBRAIC[172] is hem_dep_u_rel in component VP_capillary_H_D (dimensionless).
 * ALGEBRAIC[174] is R in component VP_capillary_H_D (Js_per_m6).
 * ALGEBRAIC[180] is v in component VP_capillary_H_D (m3_per_s).
 * ALGEBRAIC[186] is v_mm3_s in component VP_capillary_H_D (mm3_per_s).
 * ALGEBRAIC[175] is u in component VP_capillary_H_D (J_per_m3).
 * ALGEBRAIC[177] is u_mmHg in component VP_capillary_H_D (dimensionless).
 * CONSTANTS[39] is l_inlet in component parameters (metre).
 * CONSTANTS[40] is l_VV_junc1 in component parameters (metre).
 * CONSTANTS[41] is l_PV1 in component parameters (metre).
 * CONSTANTS[42] is l_PV2 in component parameters (metre).
 * CONSTANTS[43] is l_V1 in component parameters (metre).
 * CONSTANTS[44] is l_V2 in component parameters (metre).
 * RATES[0] is d/dt H_link_R in component PP_capillary_H_D (dimensionless).
 * RATES[1] is d/dt H_link_L in component PP_capillary_H_D (dimensionless).
 * RATES[2] is d/dt H_down in component PP_capillary_H_D (dimensionless).
 * RATES[3] is d/dt RBC_volume in component PP_capillary_H_D (m3).
 * RATES[4] is d/dt q_C in component PP_capillary_H_D (m3).
 * RATES[5] is d/dt RBC_volume in component VV_junction_H_D (m3).
 * RATES[6] is d/dt q_C in component VV_junction_H_D (m3).
 * RATES[7] is d/dt q_C_d in component VV_junction_H_D (m3).
 * RATES[8] is d/dt H_link_R in component PP_pericyte_H_D (dimensionless).
 * RATES[9] is d/dt H_link_L in component PP_pericyte_H_D (dimensionless).
 * RATES[10] is d/dt H_down in component PP_pericyte_H_D (dimensionless).
 * RATES[11] is d/dt RBC_volume in component PP_pericyte_H_D (m3).
 * RATES[12] is d/dt q_C in component PP_pericyte_H_D (m3).
 * RATES[13] is d/dt H_link_R in component PP_pericyte_H_D (dimensionless).
 * RATES[14] is d/dt H_link_L in component PP_pericyte_H_D (dimensionless).
 * RATES[15] is d/dt H_down in component PP_pericyte_H_D (dimensionless).
 * RATES[16] is d/dt RBC_volume in component PP_pericyte_H_D (m3).
 * RATES[17] is d/dt q_C in component PP_pericyte_H_D (m3).
 * RATES[18] is d/dt H_link_R in component VP_capillary_H_D (dimensionless).
 * RATES[19] is d/dt H_link_L in component VP_capillary_H_D (dimensionless).
 * RATES[20] is d/dt H_down in component VP_capillary_H_D (dimensionless).
 * RATES[21] is d/dt RBC_volume in component VP_capillary_H_D (m3).
 * RATES[22] is d/dt q_C in component VP_capillary_H_D (m3).
 * RATES[23] is d/dt H_link_R in component VP_capillary_H_D (dimensionless).
 * RATES[24] is d/dt H_link_L in component VP_capillary_H_D (dimensionless).
 * RATES[25] is d/dt H_down in component VP_capillary_H_D (dimensionless).
 * RATES[26] is d/dt RBC_volume in component VP_capillary_H_D (m3).
 * RATES[27] is d/dt q_C in component VP_capillary_H_D (m3).
 */
void
initConsts(double* CONSTANTS, double* RATES, double *STATES)
{
CONSTANTS[0] = 0.45;
CONSTANTS[1] = 0.45;
CONSTANTS[2] = 0.45;
CONSTANTS[3] = 0.1;
CONSTANTS[4] = 0.001;
CONSTANTS[5] = 0.001;
CONSTANTS[6] = 1E-30;
CONSTANTS[7] = 0;
CONSTANTS[8] = 0.000006;
CONSTANTS[9] = 0.001;
CONSTANTS[10] = 6666.1;
CONSTANTS[11] = 133;
CONSTANTS[12] = 0.001;
CONSTANTS[13] = 1E-50;
CONSTANTS[14] = 0.000000001;
CONSTANTS[15] = 1E-25;
CONSTANTS[16] = 0.00000001;
CONSTANTS[17] = 0.0001;
CONSTANTS[18] = 1E-18;
CONSTANTS[19] = 1000;
CONSTANTS[20] = 0.000006;
CONSTANTS[21] = 0;
CONSTANTS[22] = 0;
CONSTANTS[23] = 0;
CONSTANTS[24] = 8.51E-22;
CONSTANTS[25] = 1000000000000000;
CONSTANTS[26] = 0;
CONSTANTS[27] = 0;
CONSTANTS[28] = 1;
CONSTANTS[29] = 500;
CONSTANTS[30] = 0.000006;
CONSTANTS[31] = 0;
CONSTANTS[32] = 0.000006;
CONSTANTS[33] = 0.45;
CONSTANTS[34] = 0.0000055;
CONSTANTS[35] = 6632.7695;
CONSTANTS[36] = 0.45;
CONSTANTS[37] = 0.0000055;
CONSTANTS[38] = 6632.7695;
CONSTANTS[39] = 0.0003;
CONSTANTS[40] = 0.000001;
CONSTANTS[41] = 0.000015;
CONSTANTS[42] = 0.000015;
CONSTANTS[43] = 0.00025;
CONSTANTS[44] = 0.00025;
CONSTANTS[45] =   3.14159265358979*pow(CONSTANTS[8], 2.00000)*CONSTANTS[39];
CONSTANTS[46] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[39])/133.322;
CONSTANTS[47] =   3.14159265358979*pow(CONSTANTS[20], 2.00000)*CONSTANTS[40];
CONSTANTS[48] =   3.14159265358979*pow(CONSTANTS[30], 2.00000)*CONSTANTS[41];
CONSTANTS[49] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[8]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[8]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[8]*1.00000e+06, 12.0000));
CONSTANTS[50] =   3.14159265358979*pow(CONSTANTS[32], 2.00000)*CONSTANTS[42];
CONSTANTS[51] =   3.14159265358979*pow(CONSTANTS[34], 2.00000)*CONSTANTS[43];
CONSTANTS[52] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[43])/133.322;
CONSTANTS[53] =   3.14159265358979*pow(CONSTANTS[37], 2.00000)*CONSTANTS[44];
CONSTANTS[54] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[44])/133.322;
CONSTANTS[55] =  CONSTANTS[0]*CONSTANTS[45];
CONSTANTS[56] =  CONSTANTS[0]*CONSTANTS[47];
CONSTANTS[57] = (CONSTANTS[46]>CONSTANTS[24] ? CONSTANTS[46] : CONSTANTS[46]<=CONSTANTS[24] ? CONSTANTS[24] : 0.0/0.0);
CONSTANTS[58] =  CONSTANTS[0]*CONSTANTS[48];
CONSTANTS[59] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[8]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[8]*1.00000e+06, 0.645000));
CONSTANTS[60] =  CONSTANTS[0]*CONSTANTS[50];
CONSTANTS[61] =  CONSTANTS[0]*CONSTANTS[51];
CONSTANTS[62] =  CONSTANTS[0]*CONSTANTS[53];
CONSTANTS[63] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[41])/133.322;
CONSTANTS[64] = CONSTANTS[21];
CONSTANTS[65] = (CONSTANTS[57]>CONSTANTS[63] ? CONSTANTS[57] : CONSTANTS[57]<=CONSTANTS[63] ? CONSTANTS[63] : 0.0/0.0);
CONSTANTS[66] =  2.00000*CONSTANTS[8];
CONSTANTS[67] =  2.00000*CONSTANTS[23];
CONSTANTS[68] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[42])/133.322;
CONSTANTS[69] = (CONSTANTS[65]>CONSTANTS[68] ? CONSTANTS[65] : CONSTANTS[65]<=CONSTANTS[68] ? CONSTANTS[68] : 0.0/0.0);
CONSTANTS[70] =  2.00000*CONSTANTS[30];
CONSTANTS[71] =  2.00000*CONSTANTS[32];
CONSTANTS[72] = 0.500000+ (1.00000/ 3.14159265358979)*atan(CONSTANTS[64]/CONSTANTS[13]);
CONSTANTS[73] = 1.00000 - CONSTANTS[72];
CONSTANTS[74] =  CONSTANTS[72]*CONSTANTS[64];
CONSTANTS[75] =  CONSTANTS[73]*- CONSTANTS[64];
CONSTANTS[76] = (CONSTANTS[74]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
CONSTANTS[77] = (CONSTANTS[75]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
CONSTANTS[78] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[30]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[30]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[30]*1.00000e+06, 12.0000));
CONSTANTS[79] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[30]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[30]*1.00000e+06, 0.645000));
CONSTANTS[80] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[32]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[32]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[32]*1.00000e+06, 12.0000));
CONSTANTS[81] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[32]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[32]*1.00000e+06, 0.645000));
CONSTANTS[82] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[34]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[34]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[34]*1.00000e+06, 12.0000));
CONSTANTS[83] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[34]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[34]*1.00000e+06, 0.645000));
CONSTANTS[84] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[37]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[37]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[37]*1.00000e+06, 12.0000));
CONSTANTS[85] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[37]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[37]*1.00000e+06, 0.645000));
STATES[0] = CONSTANTS[0];
STATES[1] = CONSTANTS[0];
STATES[2] = CONSTANTS[0];
STATES[3] = CONSTANTS[55];
STATES[4] = CONSTANTS[7];
STATES[5] = CONSTANTS[56];
STATES[6] = CONSTANTS[7];
STATES[7] = CONSTANTS[7];
STATES[8] = CONSTANTS[0];
STATES[9] = CONSTANTS[0];
STATES[10] = CONSTANTS[0];
STATES[11] = CONSTANTS[58];
STATES[12] = CONSTANTS[7];
STATES[13] = CONSTANTS[0];
STATES[14] = CONSTANTS[0];
STATES[15] = CONSTANTS[0];
STATES[16] = CONSTANTS[60];
STATES[17] = CONSTANTS[7];
STATES[18] = CONSTANTS[0];
STATES[19] = CONSTANTS[0];
STATES[20] = CONSTANTS[0];
STATES[21] = CONSTANTS[61];
STATES[22] = CONSTANTS[7];
STATES[23] = CONSTANTS[0];
STATES[24] = CONSTANTS[0];
STATES[25] = CONSTANTS[0];
STATES[26] = CONSTANTS[62];
STATES[27] = CONSTANTS[7];
}
void
computeRates(double VOI, double* CONSTANTS, double* RATES, double* STATES, double* ALGEBRAIC)
{
RATES[1] = (CONSTANTS[2] - STATES[1])/CONSTANTS[12];
RATES[18] = (CONSTANTS[33] - STATES[18])/CONSTANTS[12];
RATES[23] = (CONSTANTS[36] - STATES[23])/CONSTANTS[12];
ALGEBRAIC[3] = CONSTANTS[45]+STATES[4];
ALGEBRAIC[4] = STATES[3]/ALGEBRAIC[3];
ALGEBRAIC[5] = 1.00000+ (( (CONSTANTS[59] - 1.00000)*(pow(1.00000 - ALGEBRAIC[4], CONSTANTS[49]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[49]) - 1.00000))*pow(( 2.00000*CONSTANTS[8]*1.00000e+06)/( 2.00000*CONSTANTS[8]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[6] =  ALGEBRAIC[5]*CONSTANTS[9];
ALGEBRAIC[7] = ( 8.00000*ALGEBRAIC[6]*CONSTANTS[39])/(  3.14159265358979*pow(CONSTANTS[8], 4.00000));
ALGEBRAIC[8] = STATES[4]/CONSTANTS[46]+CONSTANTS[11];
ALGEBRAIC[10] = (CONSTANTS[10] - ALGEBRAIC[8])/(ALGEBRAIC[7]/2.00000);
ALGEBRAIC[16] = STATES[6]/(CONSTANTS[69]/2.00000)+CONSTANTS[11];
ALGEBRAIC[18] = (ALGEBRAIC[8] - ALGEBRAIC[16])/(ALGEBRAIC[7]/2.00000);
RATES[4] = ALGEBRAIC[10] - ALGEBRAIC[18];
ALGEBRAIC[20] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[18]/CONSTANTS[13]);
ALGEBRAIC[1] = STATES[1];
ALGEBRAIC[2] = STATES[0];
ALGEBRAIC[21] =  ALGEBRAIC[20]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[20])*ALGEBRAIC[2];
ALGEBRAIC[25] = fabs(ALGEBRAIC[18])/(fabs(ALGEBRAIC[18])+CONSTANTS[6]);
ALGEBRAIC[27] =  ALGEBRAIC[25]*(ALGEBRAIC[4]+ CONSTANTS[3]*(ALGEBRAIC[4] - ALGEBRAIC[21]))+ (1.00000 - ALGEBRAIC[25])*ALGEBRAIC[4];
RATES[2] = (ALGEBRAIC[27] - STATES[2])/CONSTANTS[4];
ALGEBRAIC[12] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[10]/CONSTANTS[13]);
ALGEBRAIC[24] =  (1.00000 - ALGEBRAIC[20])*STATES[2]+ ALGEBRAIC[20]*ALGEBRAIC[1];
ALGEBRAIC[28] =  ALGEBRAIC[12]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[12])*ALGEBRAIC[24];
ALGEBRAIC[26] =  ALGEBRAIC[20]*STATES[2]+ (1.00000 - ALGEBRAIC[20])*ALGEBRAIC[2];
ALGEBRAIC[30] =  ALGEBRAIC[20]*ALGEBRAIC[26]+ (1.00000 - ALGEBRAIC[20])*ALGEBRAIC[2];
RATES[3] =  ALGEBRAIC[10]*ALGEBRAIC[28] -  ALGEBRAIC[18]*ALGEBRAIC[30];
ALGEBRAIC[37] = STATES[7]/(CONSTANTS[69]/2.00000)+CONSTANTS[11];
ALGEBRAIC[39] = (ALGEBRAIC[16] - ALGEBRAIC[37])/CONSTANTS[25];
RATES[6] = (ALGEBRAIC[18]+CONSTANTS[21]) - ALGEBRAIC[39];
ALGEBRAIC[41] = CONSTANTS[26]+(CONSTANTS[27] - CONSTANTS[26])/(1.00000+exp(- (VOI - CONSTANTS[29])/CONSTANTS[28]));
ALGEBRAIC[44] = CONSTANTS[48]+STATES[12];
ALGEBRAIC[45] = STATES[11]/ALGEBRAIC[44];
ALGEBRAIC[46] = 1.00000+ (( (CONSTANTS[79] - 1.00000)*(pow(1.00000 - ALGEBRAIC[45], CONSTANTS[78]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[78]) - 1.00000))*pow(( 2.00000*CONSTANTS[30]*1.00000e+06)/( 2.00000*CONSTANTS[30]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[47] =  ALGEBRAIC[46]*CONSTANTS[9];
ALGEBRAIC[48] = ( 8.00000*ALGEBRAIC[47]*CONSTANTS[41])/(  3.14159265358979*pow(CONSTANTS[30], 4.00000))+ALGEBRAIC[41];
ALGEBRAIC[49] = STATES[12]/CONSTANTS[63]+CONSTANTS[11];
ALGEBRAIC[51] = (ALGEBRAIC[37] - ALGEBRAIC[49])/(ALGEBRAIC[48]/2.00000);
ALGEBRAIC[63] = CONSTANTS[26]+(CONSTANTS[31] - CONSTANTS[26])/(1.00000+exp(- (VOI - CONSTANTS[29])/CONSTANTS[28]));
ALGEBRAIC[66] = CONSTANTS[50]+STATES[17];
ALGEBRAIC[67] = STATES[16]/ALGEBRAIC[66];
ALGEBRAIC[68] = 1.00000+ (( (CONSTANTS[81] - 1.00000)*(pow(1.00000 - ALGEBRAIC[67], CONSTANTS[80]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[80]) - 1.00000))*pow(( 2.00000*CONSTANTS[32]*1.00000e+06)/( 2.00000*CONSTANTS[32]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[69] =  ALGEBRAIC[68]*CONSTANTS[9];
ALGEBRAIC[70] = ( 8.00000*ALGEBRAIC[69]*CONSTANTS[42])/(  3.14159265358979*pow(CONSTANTS[32], 4.00000))+ALGEBRAIC[63];
ALGEBRAIC[71] = STATES[17]/CONSTANTS[68]+CONSTANTS[11];
ALGEBRAIC[72] = (ALGEBRAIC[37] - ALGEBRAIC[71])/(ALGEBRAIC[70]/2.00000);
RATES[7] = (ALGEBRAIC[39] - ALGEBRAIC[51]) - ALGEBRAIC[72];
ALGEBRAIC[29] = ALGEBRAIC[18];
ALGEBRAIC[31] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[29]/CONSTANTS[13]);
ALGEBRAIC[32] = 1.00000 - ALGEBRAIC[31];
ALGEBRAIC[34] =  ALGEBRAIC[32]*- ALGEBRAIC[29];
ALGEBRAIC[53] = - ALGEBRAIC[51];
ALGEBRAIC[54] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[53]/CONSTANTS[13]);
ALGEBRAIC[55] = 1.00000 - ALGEBRAIC[54];
ALGEBRAIC[57] =  ALGEBRAIC[55]*- ALGEBRAIC[53];
ALGEBRAIC[74] = - ALGEBRAIC[72];
ALGEBRAIC[76] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[74]/CONSTANTS[13]);
ALGEBRAIC[77] = 1.00000 - ALGEBRAIC[76];
ALGEBRAIC[80] =  ALGEBRAIC[77]*- ALGEBRAIC[74];
ALGEBRAIC[36] = (ALGEBRAIC[34]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[33] =  ALGEBRAIC[31]*ALGEBRAIC[29];
ALGEBRAIC[35] = (ALGEBRAIC[33]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[56] =  ALGEBRAIC[54]*ALGEBRAIC[53];
ALGEBRAIC[58] = (ALGEBRAIC[56]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[78] =  ALGEBRAIC[76]*ALGEBRAIC[74];
ALGEBRAIC[82] = (ALGEBRAIC[78]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[85] = ALGEBRAIC[35]+CONSTANTS[76]+ALGEBRAIC[58]+ALGEBRAIC[82];
ALGEBRAIC[86] = (ALGEBRAIC[85]==1.00000 ? 1.00000 : ALGEBRAIC[85]>=2.00000 ? - 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[87] = (ALGEBRAIC[86]==1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[93] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[36]==1.00000&&ALGEBRAIC[34]>=CONSTANTS[75]&&ALGEBRAIC[34]>=ALGEBRAIC[57]&&ALGEBRAIC[34]>=ALGEBRAIC[80] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[97] = (ALGEBRAIC[93]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[34] : 0.0/0.0);
ALGEBRAIC[94] = (ALGEBRAIC[87]==1.00000&&CONSTANTS[77]==1.00000&&CONSTANTS[75]>ALGEBRAIC[34]&&CONSTANTS[75]>=ALGEBRAIC[57]&&CONSTANTS[75]>=ALGEBRAIC[80] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[98] = (ALGEBRAIC[94]==1.00000 ? 0.00000 : 1 ? CONSTANTS[75] : 0.0/0.0);
ALGEBRAIC[59] = (ALGEBRAIC[57]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[95] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[59]==1.00000&&ALGEBRAIC[57]>ALGEBRAIC[34]&&ALGEBRAIC[57]>CONSTANTS[75]&&ALGEBRAIC[57]>=ALGEBRAIC[80] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[99] = (ALGEBRAIC[95]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[57] : 0.0/0.0);
ALGEBRAIC[83] = (ALGEBRAIC[80]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[96] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[83]==1.00000&&ALGEBRAIC[80]>ALGEBRAIC[34]&&ALGEBRAIC[80]>CONSTANTS[75]&&ALGEBRAIC[80]>ALGEBRAIC[57] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[100] = (ALGEBRAIC[96]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[80] : 0.0/0.0);
ALGEBRAIC[101] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[36]==1.00000&&ALGEBRAIC[93]==0.00000&&ALGEBRAIC[97]>=ALGEBRAIC[98]&&ALGEBRAIC[97]>=ALGEBRAIC[99]&&ALGEBRAIC[97]>=ALGEBRAIC[100] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[108] = (ALGEBRAIC[93]==1.00000 ? ALGEBRAIC[34] : ALGEBRAIC[94]==1.00000 ? CONSTANTS[75] : ALGEBRAIC[95]==1.00000 ? ALGEBRAIC[57] : ALGEBRAIC[96]==1.00000 ? ALGEBRAIC[80] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[102] = (ALGEBRAIC[87]==1.00000&&CONSTANTS[77]==1.00000&&ALGEBRAIC[94]==0.00000&&ALGEBRAIC[98]>ALGEBRAIC[97]&&ALGEBRAIC[98]>=ALGEBRAIC[99]&&ALGEBRAIC[98]>=ALGEBRAIC[100] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[103] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[59]==1.00000&&ALGEBRAIC[95]==0.00000&&ALGEBRAIC[99]>ALGEBRAIC[97]&&ALGEBRAIC[99]>ALGEBRAIC[98]&&ALGEBRAIC[99]>=ALGEBRAIC[100] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[104] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[83]==1.00000&&ALGEBRAIC[96]==0.00000&&ALGEBRAIC[100]>ALGEBRAIC[97]&&ALGEBRAIC[100]>ALGEBRAIC[98]&&ALGEBRAIC[100]>ALGEBRAIC[99] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[109] = (ALGEBRAIC[101]==1.00000 ? ALGEBRAIC[34] : ALGEBRAIC[102]==1.00000 ? CONSTANTS[75] : ALGEBRAIC[103]==1.00000 ? ALGEBRAIC[57] : ALGEBRAIC[104]==1.00000 ? ALGEBRAIC[80] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[110] = (ALGEBRAIC[108]+CONSTANTS[15])/(ALGEBRAIC[108]+ALGEBRAIC[109]+ 2.00000*CONSTANTS[15]);
ALGEBRAIC[89] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[33]>=CONSTANTS[74]&&ALGEBRAIC[33]>=ALGEBRAIC[56]&&ALGEBRAIC[33]>=ALGEBRAIC[78] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[90] = (ALGEBRAIC[87]==1.00000&&CONSTANTS[74]>ALGEBRAIC[33]&&CONSTANTS[74]>=ALGEBRAIC[56]&&CONSTANTS[74]>=ALGEBRAIC[78] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[91] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[56]>ALGEBRAIC[33]&&ALGEBRAIC[56]>CONSTANTS[74]&&ALGEBRAIC[56]>=ALGEBRAIC[78] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[92] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[78]>ALGEBRAIC[33]&&ALGEBRAIC[78]>CONSTANTS[74]&&ALGEBRAIC[78]>ALGEBRAIC[56] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[105] = (ALGEBRAIC[89]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[90]==1.00000 ? CONSTANTS[67] : ALGEBRAIC[91]==1.00000 ? CONSTANTS[70] : ALGEBRAIC[92]==1.00000 ? CONSTANTS[71] : 1 ? CONSTANTS[66] : 0.0/0.0);
ALGEBRAIC[15] = STATES[5]/(CONSTANTS[47]+CONSTANTS[15]);
ALGEBRAIC[111] = 1.00000+( 6.98000*(1.00000 - ALGEBRAIC[15]))/( ALGEBRAIC[105]*1.00000e+06);
ALGEBRAIC[106] = (ALGEBRAIC[93]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[94]==1.00000 ? CONSTANTS[67] : ALGEBRAIC[95]==1.00000 ? CONSTANTS[70] : ALGEBRAIC[96]==1.00000 ? CONSTANTS[71] : 1 ? CONSTANTS[70] : 0.0/0.0);
ALGEBRAIC[107] = (ALGEBRAIC[101]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[102]==1.00000 ? CONSTANTS[67] : ALGEBRAIC[103]==1.00000 ? CONSTANTS[70] : ALGEBRAIC[104]==1.00000 ? CONSTANTS[71] : 1 ? CONSTANTS[71] : 0.0/0.0);
ALGEBRAIC[112] = ( - 6.96000*log(( ALGEBRAIC[106]*1.00000e+06)/( ALGEBRAIC[107]*1.00000e+06)))/( ALGEBRAIC[105]*1.00000e+06);
ALGEBRAIC[113] = 0.400000/( ALGEBRAIC[105]*1.00000e+06);
ALGEBRAIC[114] = (ALGEBRAIC[110] - ALGEBRAIC[113])/((1.00000 -  2.00000*ALGEBRAIC[113])+CONSTANTS[15]);
ALGEBRAIC[115] = multi_min(2, multi_max(2, ALGEBRAIC[114], CONSTANTS[16]), 1.00000 - CONSTANTS[16]);
ALGEBRAIC[116] = log(ALGEBRAIC[115]/(1.00000 - ALGEBRAIC[115]));
ALGEBRAIC[117] = 1.00000/(1.00000+exp(- (ALGEBRAIC[112]+ ALGEBRAIC[111]*ALGEBRAIC[116])));
ALGEBRAIC[118] = ( ALGEBRAIC[15]*ALGEBRAIC[117])/(ALGEBRAIC[110]+CONSTANTS[15]);
ALGEBRAIC[119] = ( ALGEBRAIC[15]*(1.00000 - ALGEBRAIC[117]))/((1.00000 - ALGEBRAIC[110])+CONSTANTS[15]);
ALGEBRAIC[120] = (ALGEBRAIC[93]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[101]==1.00000 ? ALGEBRAIC[119] : 1 ? ALGEBRAIC[26] : 0.0/0.0);
ALGEBRAIC[88] = (ALGEBRAIC[86]==- 1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[122] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[120] : 1 ? ALGEBRAIC[26] : 0.0/0.0);
ALGEBRAIC[124] = (ALGEBRAIC[36]==1.00000 ? ALGEBRAIC[122] : 1 ? ALGEBRAIC[26] : 0.0/0.0);
ALGEBRAIC[126] =  ALGEBRAIC[32]*ALGEBRAIC[124];
RATES[0] = (ALGEBRAIC[126] - STATES[0])/CONSTANTS[12];
ALGEBRAIC[138] = STATES[22]/CONSTANTS[52]+CONSTANTS[11];
ALGEBRAIC[139] = (ALGEBRAIC[49] - ALGEBRAIC[138])/(ALGEBRAIC[48]/2.00000);
RATES[12] = ALGEBRAIC[51] - ALGEBRAIC[139];
ALGEBRAIC[133] = CONSTANTS[51]+STATES[22];
ALGEBRAIC[134] = STATES[21]/ALGEBRAIC[133];
ALGEBRAIC[135] = 1.00000+ (( (CONSTANTS[83] - 1.00000)*(pow(1.00000 - ALGEBRAIC[134], CONSTANTS[82]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[82]) - 1.00000))*pow(( 2.00000*CONSTANTS[34]*1.00000e+06)/( 2.00000*CONSTANTS[34]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[136] =  ALGEBRAIC[135]*CONSTANTS[9];
ALGEBRAIC[137] = ( 8.00000*ALGEBRAIC[136]*CONSTANTS[43])/(  3.14159265358979*pow(CONSTANTS[34], 4.00000));
ALGEBRAIC[143] = (ALGEBRAIC[138] - CONSTANTS[35])/ALGEBRAIC[137];
RATES[22] = ALGEBRAIC[139] - ALGEBRAIC[143];
ALGEBRAIC[148] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[143]/CONSTANTS[13]);
ALGEBRAIC[129] = STATES[19];
ALGEBRAIC[154] =  (1.00000 - ALGEBRAIC[148])*STATES[20]+ ALGEBRAIC[148]*ALGEBRAIC[129];
RATES[8] = (ALGEBRAIC[154] - STATES[8])/CONSTANTS[12];
ALGEBRAIC[141] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[139]/CONSTANTS[13]);
ALGEBRAIC[43] = STATES[8];
ALGEBRAIC[151] =  ALGEBRAIC[141]*STATES[10]+ (1.00000 - ALGEBRAIC[141])*ALGEBRAIC[43];
RATES[19] = (ALGEBRAIC[151] - STATES[19])/CONSTANTS[12];
ALGEBRAIC[42] = STATES[9];
ALGEBRAIC[144] =  ALGEBRAIC[141]*ALGEBRAIC[42]+ (1.00000 - ALGEBRAIC[141])*ALGEBRAIC[43];
ALGEBRAIC[150] = fabs(ALGEBRAIC[139])/(fabs(ALGEBRAIC[139])+CONSTANTS[6]);
ALGEBRAIC[157] =  ALGEBRAIC[150]*(ALGEBRAIC[45]+ CONSTANTS[3]*(ALGEBRAIC[45] - ALGEBRAIC[144]))+ (1.00000 - ALGEBRAIC[150])*ALGEBRAIC[45];
RATES[10] = (ALGEBRAIC[157] - STATES[10])/CONSTANTS[4];
ALGEBRAIC[60] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[51]/CONSTANTS[13]);
ALGEBRAIC[147] =  (1.00000 - ALGEBRAIC[141])*STATES[10]+ ALGEBRAIC[141]*ALGEBRAIC[42];
ALGEBRAIC[158] =  ALGEBRAIC[60]*ALGEBRAIC[42]+ (1.00000 - ALGEBRAIC[60])*ALGEBRAIC[147];
ALGEBRAIC[162] =  ALGEBRAIC[141]*ALGEBRAIC[151]+ (1.00000 - ALGEBRAIC[141])*ALGEBRAIC[43];
RATES[11] =  ALGEBRAIC[51]*ALGEBRAIC[158] -  ALGEBRAIC[139]*ALGEBRAIC[162];
ALGEBRAIC[132] = STATES[18];
ALGEBRAIC[153] =  ALGEBRAIC[148]*ALGEBRAIC[129]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[132];
ALGEBRAIC[160] = fabs(ALGEBRAIC[143])/(fabs(ALGEBRAIC[143])+CONSTANTS[6]);
ALGEBRAIC[164] =  ALGEBRAIC[160]*(ALGEBRAIC[134]+ CONSTANTS[3]*(ALGEBRAIC[134] - ALGEBRAIC[153]))+ (1.00000 - ALGEBRAIC[160])*ALGEBRAIC[134];
RATES[20] = (ALGEBRAIC[164] - STATES[20])/CONSTANTS[4];
ALGEBRAIC[152] = (ALGEBRAIC[95]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[103]==1.00000 ? ALGEBRAIC[119] : 1 ? ALGEBRAIC[147] : 0.0/0.0);
ALGEBRAIC[159] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[152] : 1 ? ALGEBRAIC[147] : 0.0/0.0);
ALGEBRAIC[163] = (ALGEBRAIC[59]==1.00000 ? ALGEBRAIC[159] : 1 ? ALGEBRAIC[147] : 0.0/0.0);
ALGEBRAIC[166] =  ALGEBRAIC[55]*ALGEBRAIC[163];
RATES[9] = (ALGEBRAIC[166] - STATES[9])/CONSTANTS[12];
ALGEBRAIC[165] =  ALGEBRAIC[148]*ALGEBRAIC[129]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[154];
ALGEBRAIC[161] =  ALGEBRAIC[148]*STATES[20]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[132];
ALGEBRAIC[167] =  ALGEBRAIC[148]*ALGEBRAIC[161]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[132];
RATES[21] =  ALGEBRAIC[139]*ALGEBRAIC[165] -  ALGEBRAIC[143]*ALGEBRAIC[167];
ALGEBRAIC[175] = STATES[27]/CONSTANTS[54]+CONSTANTS[11];
ALGEBRAIC[176] = (ALGEBRAIC[71] - ALGEBRAIC[175])/(ALGEBRAIC[70]/2.00000);
RATES[17] = ALGEBRAIC[72] - ALGEBRAIC[176];
ALGEBRAIC[170] = CONSTANTS[53]+STATES[27];
ALGEBRAIC[171] = STATES[26]/ALGEBRAIC[170];
ALGEBRAIC[172] = 1.00000+ (( (CONSTANTS[85] - 1.00000)*(pow(1.00000 - ALGEBRAIC[171], CONSTANTS[84]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[84]) - 1.00000))*pow(( 2.00000*CONSTANTS[37]*1.00000e+06)/( 2.00000*CONSTANTS[37]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[173] =  ALGEBRAIC[172]*CONSTANTS[9];
ALGEBRAIC[174] = ( 8.00000*ALGEBRAIC[173]*CONSTANTS[44])/(  3.14159265358979*pow(CONSTANTS[37], 4.00000));
ALGEBRAIC[180] = (ALGEBRAIC[175] - CONSTANTS[38])/ALGEBRAIC[174];
RATES[27] = ALGEBRAIC[176] - ALGEBRAIC[180];
ALGEBRAIC[185] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[180]/CONSTANTS[13]);
ALGEBRAIC[168] = STATES[24];
ALGEBRAIC[191] =  (1.00000 - ALGEBRAIC[185])*STATES[25]+ ALGEBRAIC[185]*ALGEBRAIC[168];
RATES[13] = (ALGEBRAIC[191] - STATES[13])/CONSTANTS[12];
ALGEBRAIC[178] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[176]/CONSTANTS[13]);
ALGEBRAIC[65] = STATES[13];
ALGEBRAIC[189] =  ALGEBRAIC[178]*STATES[15]+ (1.00000 - ALGEBRAIC[178])*ALGEBRAIC[65];
RATES[24] = (ALGEBRAIC[189] - STATES[24])/CONSTANTS[12];
ALGEBRAIC[64] = STATES[14];
ALGEBRAIC[181] =  ALGEBRAIC[178]*ALGEBRAIC[64]+ (1.00000 - ALGEBRAIC[178])*ALGEBRAIC[65];
ALGEBRAIC[188] = fabs(ALGEBRAIC[176])/(fabs(ALGEBRAIC[176])+CONSTANTS[6]);
ALGEBRAIC[195] =  ALGEBRAIC[188]*(ALGEBRAIC[67]+ CONSTANTS[3]*(ALGEBRAIC[67] - ALGEBRAIC[181]))+ (1.00000 - ALGEBRAIC[188])*ALGEBRAIC[67];
RATES[15] = (ALGEBRAIC[195] - STATES[15])/CONSTANTS[4];
ALGEBRAIC[128] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[72]/CONSTANTS[13]);
ALGEBRAIC[182] =  (1.00000 - ALGEBRAIC[178])*STATES[15]+ ALGEBRAIC[178]*ALGEBRAIC[64];
ALGEBRAIC[196] =  ALGEBRAIC[128]*ALGEBRAIC[64]+ (1.00000 - ALGEBRAIC[128])*ALGEBRAIC[182];
ALGEBRAIC[200] =  ALGEBRAIC[178]*ALGEBRAIC[189]+ (1.00000 - ALGEBRAIC[178])*ALGEBRAIC[65];
RATES[16] =  ALGEBRAIC[72]*ALGEBRAIC[196] -  ALGEBRAIC[176]*ALGEBRAIC[200];
ALGEBRAIC[169] = STATES[23];
ALGEBRAIC[190] =  ALGEBRAIC[185]*ALGEBRAIC[168]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[169];
ALGEBRAIC[197] = fabs(ALGEBRAIC[180])/(fabs(ALGEBRAIC[180])+CONSTANTS[6]);
ALGEBRAIC[201] =  ALGEBRAIC[197]*(ALGEBRAIC[171]+ CONSTANTS[3]*(ALGEBRAIC[171] - ALGEBRAIC[190]))+ (1.00000 - ALGEBRAIC[197])*ALGEBRAIC[171];
RATES[25] = (ALGEBRAIC[201] - STATES[25])/CONSTANTS[4];
ALGEBRAIC[187] = (ALGEBRAIC[96]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[104]==1.00000 ? ALGEBRAIC[119] : 1 ? ALGEBRAIC[182] : 0.0/0.0);
ALGEBRAIC[194] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[187] : 1 ? ALGEBRAIC[182] : 0.0/0.0);
ALGEBRAIC[199] = (ALGEBRAIC[83]==1.00000 ? ALGEBRAIC[194] : 1 ? ALGEBRAIC[182] : 0.0/0.0);
ALGEBRAIC[203] =  ALGEBRAIC[77]*ALGEBRAIC[199];
RATES[14] = (ALGEBRAIC[203] - STATES[14])/CONSTANTS[12];
ALGEBRAIC[202] =  ALGEBRAIC[185]*ALGEBRAIC[168]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[191];
ALGEBRAIC[198] =  ALGEBRAIC[185]*STATES[25]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[169];
ALGEBRAIC[204] =  ALGEBRAIC[185]*ALGEBRAIC[198]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[169];
RATES[26] =  ALGEBRAIC[176]*ALGEBRAIC[202] -  ALGEBRAIC[180]*ALGEBRAIC[204];
ALGEBRAIC[205] =  ALGEBRAIC[33]*ALGEBRAIC[26]+ CONSTANTS[74]*CONSTANTS[22]+ ALGEBRAIC[56]*ALGEBRAIC[147]+ ALGEBRAIC[78]*ALGEBRAIC[182];
ALGEBRAIC[121] = (ALGEBRAIC[94]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[102]==1.00000 ? ALGEBRAIC[119] : 1 ? CONSTANTS[22] : 0.0/0.0);
ALGEBRAIC[123] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[121] : 1 ? CONSTANTS[22] : 0.0/0.0);
ALGEBRAIC[125] = (CONSTANTS[77]==1.00000 ? ALGEBRAIC[123] : 1 ? CONSTANTS[22] : 0.0/0.0);
ALGEBRAIC[127] =  CONSTANTS[73]*ALGEBRAIC[125];
ALGEBRAIC[206] =  ALGEBRAIC[34]*ALGEBRAIC[126]+ CONSTANTS[75]*ALGEBRAIC[127]+ ALGEBRAIC[57]*ALGEBRAIC[166]+ ALGEBRAIC[80]*ALGEBRAIC[203];
RATES[5] = ALGEBRAIC[205] - ALGEBRAIC[206];
}
void
computeVariables(double VOI, double* CONSTANTS, double* RATES, double* STATES, double* ALGEBRAIC)
{
ALGEBRAIC[3] = CONSTANTS[45]+STATES[4];
ALGEBRAIC[4] = STATES[3]/ALGEBRAIC[3];
ALGEBRAIC[5] = 1.00000+ (( (CONSTANTS[59] - 1.00000)*(pow(1.00000 - ALGEBRAIC[4], CONSTANTS[49]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[49]) - 1.00000))*pow(( 2.00000*CONSTANTS[8]*1.00000e+06)/( 2.00000*CONSTANTS[8]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[6] =  ALGEBRAIC[5]*CONSTANTS[9];
ALGEBRAIC[7] = ( 8.00000*ALGEBRAIC[6]*CONSTANTS[39])/(  3.14159265358979*pow(CONSTANTS[8], 4.00000));
ALGEBRAIC[8] = STATES[4]/CONSTANTS[46]+CONSTANTS[11];
ALGEBRAIC[10] = (CONSTANTS[10] - ALGEBRAIC[8])/(ALGEBRAIC[7]/2.00000);
ALGEBRAIC[16] = STATES[6]/(CONSTANTS[69]/2.00000)+CONSTANTS[11];
ALGEBRAIC[18] = (ALGEBRAIC[8] - ALGEBRAIC[16])/(ALGEBRAIC[7]/2.00000);
ALGEBRAIC[20] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[18]/CONSTANTS[13]);
ALGEBRAIC[1] = STATES[1];
ALGEBRAIC[2] = STATES[0];
ALGEBRAIC[21] =  ALGEBRAIC[20]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[20])*ALGEBRAIC[2];
ALGEBRAIC[25] = fabs(ALGEBRAIC[18])/(fabs(ALGEBRAIC[18])+CONSTANTS[6]);
ALGEBRAIC[27] =  ALGEBRAIC[25]*(ALGEBRAIC[4]+ CONSTANTS[3]*(ALGEBRAIC[4] - ALGEBRAIC[21]))+ (1.00000 - ALGEBRAIC[25])*ALGEBRAIC[4];
ALGEBRAIC[12] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[10]/CONSTANTS[13]);
ALGEBRAIC[24] =  (1.00000 - ALGEBRAIC[20])*STATES[2]+ ALGEBRAIC[20]*ALGEBRAIC[1];
ALGEBRAIC[28] =  ALGEBRAIC[12]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[12])*ALGEBRAIC[24];
ALGEBRAIC[26] =  ALGEBRAIC[20]*STATES[2]+ (1.00000 - ALGEBRAIC[20])*ALGEBRAIC[2];
ALGEBRAIC[30] =  ALGEBRAIC[20]*ALGEBRAIC[26]+ (1.00000 - ALGEBRAIC[20])*ALGEBRAIC[2];
ALGEBRAIC[37] = STATES[7]/(CONSTANTS[69]/2.00000)+CONSTANTS[11];
ALGEBRAIC[39] = (ALGEBRAIC[16] - ALGEBRAIC[37])/CONSTANTS[25];
ALGEBRAIC[41] = CONSTANTS[26]+(CONSTANTS[27] - CONSTANTS[26])/(1.00000+exp(- (VOI - CONSTANTS[29])/CONSTANTS[28]));
ALGEBRAIC[44] = CONSTANTS[48]+STATES[12];
ALGEBRAIC[45] = STATES[11]/ALGEBRAIC[44];
ALGEBRAIC[46] = 1.00000+ (( (CONSTANTS[79] - 1.00000)*(pow(1.00000 - ALGEBRAIC[45], CONSTANTS[78]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[78]) - 1.00000))*pow(( 2.00000*CONSTANTS[30]*1.00000e+06)/( 2.00000*CONSTANTS[30]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[47] =  ALGEBRAIC[46]*CONSTANTS[9];
ALGEBRAIC[48] = ( 8.00000*ALGEBRAIC[47]*CONSTANTS[41])/(  3.14159265358979*pow(CONSTANTS[30], 4.00000))+ALGEBRAIC[41];
ALGEBRAIC[49] = STATES[12]/CONSTANTS[63]+CONSTANTS[11];
ALGEBRAIC[51] = (ALGEBRAIC[37] - ALGEBRAIC[49])/(ALGEBRAIC[48]/2.00000);
ALGEBRAIC[63] = CONSTANTS[26]+(CONSTANTS[31] - CONSTANTS[26])/(1.00000+exp(- (VOI - CONSTANTS[29])/CONSTANTS[28]));
ALGEBRAIC[66] = CONSTANTS[50]+STATES[17];
ALGEBRAIC[67] = STATES[16]/ALGEBRAIC[66];
ALGEBRAIC[68] = 1.00000+ (( (CONSTANTS[81] - 1.00000)*(pow(1.00000 - ALGEBRAIC[67], CONSTANTS[80]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[80]) - 1.00000))*pow(( 2.00000*CONSTANTS[32]*1.00000e+06)/( 2.00000*CONSTANTS[32]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[69] =  ALGEBRAIC[68]*CONSTANTS[9];
ALGEBRAIC[70] = ( 8.00000*ALGEBRAIC[69]*CONSTANTS[42])/(  3.14159265358979*pow(CONSTANTS[32], 4.00000))+ALGEBRAIC[63];
ALGEBRAIC[71] = STATES[17]/CONSTANTS[68]+CONSTANTS[11];
ALGEBRAIC[72] = (ALGEBRAIC[37] - ALGEBRAIC[71])/(ALGEBRAIC[70]/2.00000);
ALGEBRAIC[29] = ALGEBRAIC[18];
ALGEBRAIC[31] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[29]/CONSTANTS[13]);
ALGEBRAIC[32] = 1.00000 - ALGEBRAIC[31];
ALGEBRAIC[34] =  ALGEBRAIC[32]*- ALGEBRAIC[29];
ALGEBRAIC[53] = - ALGEBRAIC[51];
ALGEBRAIC[54] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[53]/CONSTANTS[13]);
ALGEBRAIC[55] = 1.00000 - ALGEBRAIC[54];
ALGEBRAIC[57] =  ALGEBRAIC[55]*- ALGEBRAIC[53];
ALGEBRAIC[74] = - ALGEBRAIC[72];
ALGEBRAIC[76] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[74]/CONSTANTS[13]);
ALGEBRAIC[77] = 1.00000 - ALGEBRAIC[76];
ALGEBRAIC[80] =  ALGEBRAIC[77]*- ALGEBRAIC[74];
ALGEBRAIC[36] = (ALGEBRAIC[34]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[33] =  ALGEBRAIC[31]*ALGEBRAIC[29];
ALGEBRAIC[35] = (ALGEBRAIC[33]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[56] =  ALGEBRAIC[54]*ALGEBRAIC[53];
ALGEBRAIC[58] = (ALGEBRAIC[56]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[78] =  ALGEBRAIC[76]*ALGEBRAIC[74];
ALGEBRAIC[82] = (ALGEBRAIC[78]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[85] = ALGEBRAIC[35]+CONSTANTS[76]+ALGEBRAIC[58]+ALGEBRAIC[82];
ALGEBRAIC[86] = (ALGEBRAIC[85]==1.00000 ? 1.00000 : ALGEBRAIC[85]>=2.00000 ? - 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[87] = (ALGEBRAIC[86]==1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[93] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[36]==1.00000&&ALGEBRAIC[34]>=CONSTANTS[75]&&ALGEBRAIC[34]>=ALGEBRAIC[57]&&ALGEBRAIC[34]>=ALGEBRAIC[80] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[97] = (ALGEBRAIC[93]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[34] : 0.0/0.0);
ALGEBRAIC[94] = (ALGEBRAIC[87]==1.00000&&CONSTANTS[77]==1.00000&&CONSTANTS[75]>ALGEBRAIC[34]&&CONSTANTS[75]>=ALGEBRAIC[57]&&CONSTANTS[75]>=ALGEBRAIC[80] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[98] = (ALGEBRAIC[94]==1.00000 ? 0.00000 : 1 ? CONSTANTS[75] : 0.0/0.0);
ALGEBRAIC[59] = (ALGEBRAIC[57]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[95] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[59]==1.00000&&ALGEBRAIC[57]>ALGEBRAIC[34]&&ALGEBRAIC[57]>CONSTANTS[75]&&ALGEBRAIC[57]>=ALGEBRAIC[80] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[99] = (ALGEBRAIC[95]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[57] : 0.0/0.0);
ALGEBRAIC[83] = (ALGEBRAIC[80]>CONSTANTS[18] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[96] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[83]==1.00000&&ALGEBRAIC[80]>ALGEBRAIC[34]&&ALGEBRAIC[80]>CONSTANTS[75]&&ALGEBRAIC[80]>ALGEBRAIC[57] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[100] = (ALGEBRAIC[96]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[80] : 0.0/0.0);
ALGEBRAIC[101] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[36]==1.00000&&ALGEBRAIC[93]==0.00000&&ALGEBRAIC[97]>=ALGEBRAIC[98]&&ALGEBRAIC[97]>=ALGEBRAIC[99]&&ALGEBRAIC[97]>=ALGEBRAIC[100] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[108] = (ALGEBRAIC[93]==1.00000 ? ALGEBRAIC[34] : ALGEBRAIC[94]==1.00000 ? CONSTANTS[75] : ALGEBRAIC[95]==1.00000 ? ALGEBRAIC[57] : ALGEBRAIC[96]==1.00000 ? ALGEBRAIC[80] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[102] = (ALGEBRAIC[87]==1.00000&&CONSTANTS[77]==1.00000&&ALGEBRAIC[94]==0.00000&&ALGEBRAIC[98]>ALGEBRAIC[97]&&ALGEBRAIC[98]>=ALGEBRAIC[99]&&ALGEBRAIC[98]>=ALGEBRAIC[100] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[103] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[59]==1.00000&&ALGEBRAIC[95]==0.00000&&ALGEBRAIC[99]>ALGEBRAIC[97]&&ALGEBRAIC[99]>ALGEBRAIC[98]&&ALGEBRAIC[99]>=ALGEBRAIC[100] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[104] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[83]==1.00000&&ALGEBRAIC[96]==0.00000&&ALGEBRAIC[100]>ALGEBRAIC[97]&&ALGEBRAIC[100]>ALGEBRAIC[98]&&ALGEBRAIC[100]>ALGEBRAIC[99] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[109] = (ALGEBRAIC[101]==1.00000 ? ALGEBRAIC[34] : ALGEBRAIC[102]==1.00000 ? CONSTANTS[75] : ALGEBRAIC[103]==1.00000 ? ALGEBRAIC[57] : ALGEBRAIC[104]==1.00000 ? ALGEBRAIC[80] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[110] = (ALGEBRAIC[108]+CONSTANTS[15])/(ALGEBRAIC[108]+ALGEBRAIC[109]+ 2.00000*CONSTANTS[15]);
ALGEBRAIC[89] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[33]>=CONSTANTS[74]&&ALGEBRAIC[33]>=ALGEBRAIC[56]&&ALGEBRAIC[33]>=ALGEBRAIC[78] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[90] = (ALGEBRAIC[87]==1.00000&&CONSTANTS[74]>ALGEBRAIC[33]&&CONSTANTS[74]>=ALGEBRAIC[56]&&CONSTANTS[74]>=ALGEBRAIC[78] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[91] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[56]>ALGEBRAIC[33]&&ALGEBRAIC[56]>CONSTANTS[74]&&ALGEBRAIC[56]>=ALGEBRAIC[78] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[92] = (ALGEBRAIC[87]==1.00000&&ALGEBRAIC[78]>ALGEBRAIC[33]&&ALGEBRAIC[78]>CONSTANTS[74]&&ALGEBRAIC[78]>ALGEBRAIC[56] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[105] = (ALGEBRAIC[89]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[90]==1.00000 ? CONSTANTS[67] : ALGEBRAIC[91]==1.00000 ? CONSTANTS[70] : ALGEBRAIC[92]==1.00000 ? CONSTANTS[71] : 1 ? CONSTANTS[66] : 0.0/0.0);
ALGEBRAIC[15] = STATES[5]/(CONSTANTS[47]+CONSTANTS[15]);
ALGEBRAIC[111] = 1.00000+( 6.98000*(1.00000 - ALGEBRAIC[15]))/( ALGEBRAIC[105]*1.00000e+06);
ALGEBRAIC[106] = (ALGEBRAIC[93]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[94]==1.00000 ? CONSTANTS[67] : ALGEBRAIC[95]==1.00000 ? CONSTANTS[70] : ALGEBRAIC[96]==1.00000 ? CONSTANTS[71] : 1 ? CONSTANTS[70] : 0.0/0.0);
ALGEBRAIC[107] = (ALGEBRAIC[101]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[102]==1.00000 ? CONSTANTS[67] : ALGEBRAIC[103]==1.00000 ? CONSTANTS[70] : ALGEBRAIC[104]==1.00000 ? CONSTANTS[71] : 1 ? CONSTANTS[71] : 0.0/0.0);
ALGEBRAIC[112] = ( - 6.96000*log(( ALGEBRAIC[106]*1.00000e+06)/( ALGEBRAIC[107]*1.00000e+06)))/( ALGEBRAIC[105]*1.00000e+06);
ALGEBRAIC[113] = 0.400000/( ALGEBRAIC[105]*1.00000e+06);
ALGEBRAIC[114] = (ALGEBRAIC[110] - ALGEBRAIC[113])/((1.00000 -  2.00000*ALGEBRAIC[113])+CONSTANTS[15]);
ALGEBRAIC[115] = multi_min(2, multi_max(2, ALGEBRAIC[114], CONSTANTS[16]), 1.00000 - CONSTANTS[16]);
ALGEBRAIC[116] = log(ALGEBRAIC[115]/(1.00000 - ALGEBRAIC[115]));
ALGEBRAIC[117] = 1.00000/(1.00000+exp(- (ALGEBRAIC[112]+ ALGEBRAIC[111]*ALGEBRAIC[116])));
ALGEBRAIC[118] = ( ALGEBRAIC[15]*ALGEBRAIC[117])/(ALGEBRAIC[110]+CONSTANTS[15]);
ALGEBRAIC[119] = ( ALGEBRAIC[15]*(1.00000 - ALGEBRAIC[117]))/((1.00000 - ALGEBRAIC[110])+CONSTANTS[15]);
ALGEBRAIC[120] = (ALGEBRAIC[93]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[101]==1.00000 ? ALGEBRAIC[119] : 1 ? ALGEBRAIC[26] : 0.0/0.0);
ALGEBRAIC[88] = (ALGEBRAIC[86]==- 1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[122] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[120] : 1 ? ALGEBRAIC[26] : 0.0/0.0);
ALGEBRAIC[124] = (ALGEBRAIC[36]==1.00000 ? ALGEBRAIC[122] : 1 ? ALGEBRAIC[26] : 0.0/0.0);
ALGEBRAIC[126] =  ALGEBRAIC[32]*ALGEBRAIC[124];
ALGEBRAIC[138] = STATES[22]/CONSTANTS[52]+CONSTANTS[11];
ALGEBRAIC[139] = (ALGEBRAIC[49] - ALGEBRAIC[138])/(ALGEBRAIC[48]/2.00000);
ALGEBRAIC[133] = CONSTANTS[51]+STATES[22];
ALGEBRAIC[134] = STATES[21]/ALGEBRAIC[133];
ALGEBRAIC[135] = 1.00000+ (( (CONSTANTS[83] - 1.00000)*(pow(1.00000 - ALGEBRAIC[134], CONSTANTS[82]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[82]) - 1.00000))*pow(( 2.00000*CONSTANTS[34]*1.00000e+06)/( 2.00000*CONSTANTS[34]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[136] =  ALGEBRAIC[135]*CONSTANTS[9];
ALGEBRAIC[137] = ( 8.00000*ALGEBRAIC[136]*CONSTANTS[43])/(  3.14159265358979*pow(CONSTANTS[34], 4.00000));
ALGEBRAIC[143] = (ALGEBRAIC[138] - CONSTANTS[35])/ALGEBRAIC[137];
ALGEBRAIC[148] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[143]/CONSTANTS[13]);
ALGEBRAIC[129] = STATES[19];
ALGEBRAIC[154] =  (1.00000 - ALGEBRAIC[148])*STATES[20]+ ALGEBRAIC[148]*ALGEBRAIC[129];
ALGEBRAIC[141] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[139]/CONSTANTS[13]);
ALGEBRAIC[43] = STATES[8];
ALGEBRAIC[151] =  ALGEBRAIC[141]*STATES[10]+ (1.00000 - ALGEBRAIC[141])*ALGEBRAIC[43];
ALGEBRAIC[42] = STATES[9];
ALGEBRAIC[144] =  ALGEBRAIC[141]*ALGEBRAIC[42]+ (1.00000 - ALGEBRAIC[141])*ALGEBRAIC[43];
ALGEBRAIC[150] = fabs(ALGEBRAIC[139])/(fabs(ALGEBRAIC[139])+CONSTANTS[6]);
ALGEBRAIC[157] =  ALGEBRAIC[150]*(ALGEBRAIC[45]+ CONSTANTS[3]*(ALGEBRAIC[45] - ALGEBRAIC[144]))+ (1.00000 - ALGEBRAIC[150])*ALGEBRAIC[45];
ALGEBRAIC[60] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[51]/CONSTANTS[13]);
ALGEBRAIC[147] =  (1.00000 - ALGEBRAIC[141])*STATES[10]+ ALGEBRAIC[141]*ALGEBRAIC[42];
ALGEBRAIC[158] =  ALGEBRAIC[60]*ALGEBRAIC[42]+ (1.00000 - ALGEBRAIC[60])*ALGEBRAIC[147];
ALGEBRAIC[162] =  ALGEBRAIC[141]*ALGEBRAIC[151]+ (1.00000 - ALGEBRAIC[141])*ALGEBRAIC[43];
ALGEBRAIC[132] = STATES[18];
ALGEBRAIC[153] =  ALGEBRAIC[148]*ALGEBRAIC[129]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[132];
ALGEBRAIC[160] = fabs(ALGEBRAIC[143])/(fabs(ALGEBRAIC[143])+CONSTANTS[6]);
ALGEBRAIC[164] =  ALGEBRAIC[160]*(ALGEBRAIC[134]+ CONSTANTS[3]*(ALGEBRAIC[134] - ALGEBRAIC[153]))+ (1.00000 - ALGEBRAIC[160])*ALGEBRAIC[134];
ALGEBRAIC[152] = (ALGEBRAIC[95]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[103]==1.00000 ? ALGEBRAIC[119] : 1 ? ALGEBRAIC[147] : 0.0/0.0);
ALGEBRAIC[159] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[152] : 1 ? ALGEBRAIC[147] : 0.0/0.0);
ALGEBRAIC[163] = (ALGEBRAIC[59]==1.00000 ? ALGEBRAIC[159] : 1 ? ALGEBRAIC[147] : 0.0/0.0);
ALGEBRAIC[166] =  ALGEBRAIC[55]*ALGEBRAIC[163];
ALGEBRAIC[165] =  ALGEBRAIC[148]*ALGEBRAIC[129]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[154];
ALGEBRAIC[161] =  ALGEBRAIC[148]*STATES[20]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[132];
ALGEBRAIC[167] =  ALGEBRAIC[148]*ALGEBRAIC[161]+ (1.00000 - ALGEBRAIC[148])*ALGEBRAIC[132];
ALGEBRAIC[175] = STATES[27]/CONSTANTS[54]+CONSTANTS[11];
ALGEBRAIC[176] = (ALGEBRAIC[71] - ALGEBRAIC[175])/(ALGEBRAIC[70]/2.00000);
ALGEBRAIC[170] = CONSTANTS[53]+STATES[27];
ALGEBRAIC[171] = STATES[26]/ALGEBRAIC[170];
ALGEBRAIC[172] = 1.00000+ (( (CONSTANTS[85] - 1.00000)*(pow(1.00000 - ALGEBRAIC[171], CONSTANTS[84]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[84]) - 1.00000))*pow(( 2.00000*CONSTANTS[37]*1.00000e+06)/( 2.00000*CONSTANTS[37]*1.00000e+06 - 1.10000), 2.00000);
ALGEBRAIC[173] =  ALGEBRAIC[172]*CONSTANTS[9];
ALGEBRAIC[174] = ( 8.00000*ALGEBRAIC[173]*CONSTANTS[44])/(  3.14159265358979*pow(CONSTANTS[37], 4.00000));
ALGEBRAIC[180] = (ALGEBRAIC[175] - CONSTANTS[38])/ALGEBRAIC[174];
ALGEBRAIC[185] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[180]/CONSTANTS[13]);
ALGEBRAIC[168] = STATES[24];
ALGEBRAIC[191] =  (1.00000 - ALGEBRAIC[185])*STATES[25]+ ALGEBRAIC[185]*ALGEBRAIC[168];
ALGEBRAIC[178] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[176]/CONSTANTS[13]);
ALGEBRAIC[65] = STATES[13];
ALGEBRAIC[189] =  ALGEBRAIC[178]*STATES[15]+ (1.00000 - ALGEBRAIC[178])*ALGEBRAIC[65];
ALGEBRAIC[64] = STATES[14];
ALGEBRAIC[181] =  ALGEBRAIC[178]*ALGEBRAIC[64]+ (1.00000 - ALGEBRAIC[178])*ALGEBRAIC[65];
ALGEBRAIC[188] = fabs(ALGEBRAIC[176])/(fabs(ALGEBRAIC[176])+CONSTANTS[6]);
ALGEBRAIC[195] =  ALGEBRAIC[188]*(ALGEBRAIC[67]+ CONSTANTS[3]*(ALGEBRAIC[67] - ALGEBRAIC[181]))+ (1.00000 - ALGEBRAIC[188])*ALGEBRAIC[67];
ALGEBRAIC[128] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[72]/CONSTANTS[13]);
ALGEBRAIC[182] =  (1.00000 - ALGEBRAIC[178])*STATES[15]+ ALGEBRAIC[178]*ALGEBRAIC[64];
ALGEBRAIC[196] =  ALGEBRAIC[128]*ALGEBRAIC[64]+ (1.00000 - ALGEBRAIC[128])*ALGEBRAIC[182];
ALGEBRAIC[200] =  ALGEBRAIC[178]*ALGEBRAIC[189]+ (1.00000 - ALGEBRAIC[178])*ALGEBRAIC[65];
ALGEBRAIC[169] = STATES[23];
ALGEBRAIC[190] =  ALGEBRAIC[185]*ALGEBRAIC[168]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[169];
ALGEBRAIC[197] = fabs(ALGEBRAIC[180])/(fabs(ALGEBRAIC[180])+CONSTANTS[6]);
ALGEBRAIC[201] =  ALGEBRAIC[197]*(ALGEBRAIC[171]+ CONSTANTS[3]*(ALGEBRAIC[171] - ALGEBRAIC[190]))+ (1.00000 - ALGEBRAIC[197])*ALGEBRAIC[171];
ALGEBRAIC[187] = (ALGEBRAIC[96]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[104]==1.00000 ? ALGEBRAIC[119] : 1 ? ALGEBRAIC[182] : 0.0/0.0);
ALGEBRAIC[194] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[187] : 1 ? ALGEBRAIC[182] : 0.0/0.0);
ALGEBRAIC[199] = (ALGEBRAIC[83]==1.00000 ? ALGEBRAIC[194] : 1 ? ALGEBRAIC[182] : 0.0/0.0);
ALGEBRAIC[203] =  ALGEBRAIC[77]*ALGEBRAIC[199];
ALGEBRAIC[202] =  ALGEBRAIC[185]*ALGEBRAIC[168]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[191];
ALGEBRAIC[198] =  ALGEBRAIC[185]*STATES[25]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[169];
ALGEBRAIC[204] =  ALGEBRAIC[185]*ALGEBRAIC[198]+ (1.00000 - ALGEBRAIC[185])*ALGEBRAIC[169];
ALGEBRAIC[205] =  ALGEBRAIC[33]*ALGEBRAIC[26]+ CONSTANTS[74]*CONSTANTS[22]+ ALGEBRAIC[56]*ALGEBRAIC[147]+ ALGEBRAIC[78]*ALGEBRAIC[182];
ALGEBRAIC[121] = (ALGEBRAIC[94]==1.00000 ? ALGEBRAIC[118] : ALGEBRAIC[102]==1.00000 ? ALGEBRAIC[119] : 1 ? CONSTANTS[22] : 0.0/0.0);
ALGEBRAIC[123] = (ALGEBRAIC[88]==1.00000 ? ALGEBRAIC[15] : ALGEBRAIC[87]==1.00000 ? ALGEBRAIC[121] : 1 ? CONSTANTS[22] : 0.0/0.0);
ALGEBRAIC[125] = (CONSTANTS[77]==1.00000 ? ALGEBRAIC[123] : 1 ? CONSTANTS[22] : 0.0/0.0);
ALGEBRAIC[127] =  CONSTANTS[73]*ALGEBRAIC[125];
ALGEBRAIC[206] =  ALGEBRAIC[34]*ALGEBRAIC[126]+ CONSTANTS[75]*ALGEBRAIC[127]+ ALGEBRAIC[57]*ALGEBRAIC[166]+ ALGEBRAIC[80]*ALGEBRAIC[203];
ALGEBRAIC[0] = CONSTANTS[47]+STATES[6]+STATES[7];
ALGEBRAIC[9] = ALGEBRAIC[8]/133.322;
ALGEBRAIC[11] = ALGEBRAIC[10]/CONSTANTS[14];
ALGEBRAIC[13] =  ALGEBRAIC[12]*ALGEBRAIC[10];
ALGEBRAIC[14] =  (1.00000 - ALGEBRAIC[12])*- ALGEBRAIC[10];
ALGEBRAIC[17] = ALGEBRAIC[16]/133.322;
ALGEBRAIC[19] = ALGEBRAIC[18]/CONSTANTS[14];
ALGEBRAIC[22] =  ALGEBRAIC[20]*ALGEBRAIC[18];
ALGEBRAIC[23] =  (1.00000 - ALGEBRAIC[20])*- ALGEBRAIC[18];
ALGEBRAIC[38] = ALGEBRAIC[37]/133.322;
ALGEBRAIC[40] = ALGEBRAIC[39]/CONSTANTS[14];
ALGEBRAIC[50] = ALGEBRAIC[49]/133.322;
ALGEBRAIC[52] = ALGEBRAIC[51]/CONSTANTS[14];
ALGEBRAIC[61] =  ALGEBRAIC[60]*ALGEBRAIC[51];
ALGEBRAIC[62] =  (1.00000 - ALGEBRAIC[60])*- ALGEBRAIC[51];
ALGEBRAIC[73] = ALGEBRAIC[71]/133.322;
ALGEBRAIC[75] = ALGEBRAIC[72]/CONSTANTS[14];
ALGEBRAIC[79] = ALGEBRAIC[33]+CONSTANTS[74]+ALGEBRAIC[56]+ALGEBRAIC[78];
ALGEBRAIC[81] = ALGEBRAIC[34]+CONSTANTS[75]+ALGEBRAIC[57]+ALGEBRAIC[80];
ALGEBRAIC[84] = ALGEBRAIC[36]+CONSTANTS[77]+ALGEBRAIC[59]+ALGEBRAIC[83];
ALGEBRAIC[130] =  ALGEBRAIC[128]*ALGEBRAIC[72];
ALGEBRAIC[131] =  (1.00000 - ALGEBRAIC[128])*- ALGEBRAIC[72];
ALGEBRAIC[140] = ALGEBRAIC[138]/133.322;
ALGEBRAIC[142] = ALGEBRAIC[139]/CONSTANTS[14];
ALGEBRAIC[145] =  ALGEBRAIC[141]*ALGEBRAIC[139];
ALGEBRAIC[146] =  (1.00000 - ALGEBRAIC[141])*- ALGEBRAIC[139];
ALGEBRAIC[149] = ALGEBRAIC[143]/CONSTANTS[14];
ALGEBRAIC[155] =  ALGEBRAIC[148]*ALGEBRAIC[143];
ALGEBRAIC[156] =  (1.00000 - ALGEBRAIC[148])*- ALGEBRAIC[143];
ALGEBRAIC[177] = ALGEBRAIC[175]/133.322;
ALGEBRAIC[179] = ALGEBRAIC[176]/CONSTANTS[14];
ALGEBRAIC[183] =  ALGEBRAIC[178]*ALGEBRAIC[176];
ALGEBRAIC[184] =  (1.00000 - ALGEBRAIC[178])*- ALGEBRAIC[176];
ALGEBRAIC[186] = ALGEBRAIC[180]/CONSTANTS[14];
ALGEBRAIC[192] =  ALGEBRAIC[185]*ALGEBRAIC[180];
ALGEBRAIC[193] =  (1.00000 - ALGEBRAIC[185])*- ALGEBRAIC[180];
}
