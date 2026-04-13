/*
   There are a total of 212 entries in the algebraic variable array.
   There are a total of 23 entries in each of the rate and state variable arrays.
   There are a total of 85 entries in the constant variable array.
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
 * ALGEBRAIC[34] is w_v in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[35] is w_v_d in component PP_capillary_H_D_I (dimensionless).
 * STATES[0] is H_link_R in component PP_capillary_H_D_I (dimensionless).
 * STATES[1] is H_link_L in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[1] is H_L_in in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[2] is H_R_in in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[96] is H_up in component PP_capillary_H_D_I (dimensionless).
 * STATES[2] is H_down in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[132] is H_down_target in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[126] is s_v_d in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[36] is H_L_out in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[37] is H_R_out in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[38] is RBC_volume in component PP_capillary_H_D_I (m3).
 * CONSTANTS[54] is RBC_volume_init in component PP_capillary_H_D_I (m3).
 * ALGEBRAIC[97] is v_pos in component PP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[98] is v_neg in component PP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[99] is v_d_pos in component PP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[100] is v_d_neg in component PP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[39] is H_mean in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[40] is H_volume_L in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[41] is H_volume_R in component PP_capillary_H_D_I (dimensionless).
 * STATES[3] is q_C in component PP_capillary_H_D_I (m3).
 * ALGEBRAIC[3] is q in component PP_capillary_H_D_I (m3).
 * CONSTANTS[44] is q_us in component PP_capillary_H_D_I (m3).
 * CONSTANTS[45] is C in component PP_capillary_H_D_I (m6_per_J).
 * CONSTANTS[48] is Z in component PP_capillary_H_D_I (dimensionless).
 * CONSTANTS[58] is mu_45 in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[42] is mu in component PP_capillary_H_D_I (Js_per_m3).
 * ALGEBRAIC[43] is hem_dep_u_rel in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[44] is R in component PP_capillary_H_D_I (Js_per_m6).
 * ALGEBRAIC[45] is v in component PP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[101] is v_mm3_s in component PP_capillary_H_D_I (mm3_per_s).
 * ALGEBRAIC[4] is u in component PP_capillary_H_D_I (J_per_m3).
 * ALGEBRAIC[5] is u_mmHg in component PP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[46] is v_d in component PP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[102] is v_d_mm3_s in component PP_capillary_H_D_I (mm3_per_s).
 * CONSTANTS[15] is div_0 in component parameters_global (dimensionless).
 * CONSTANTS[16] is div_0y in component parameters_global (dimensionless).
 * CONSTANTS[17] is v_threshold in component parameters_global (m3_per_s).
 * CONSTANTS[18] is k in component parameters_global (dimensionless).
 * CONSTANTS[19] is r_VV_junc1 in component parameters (metre).
 * CONSTANTS[20] is vbc2_VV_junc1 in component parameters (m3_per_s).
 * ALGEBRAIC[103] is vj1 in component VV_junction_H_D_I (m3_per_s).
 * CONSTANTS[63] is vj2 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[127] is vj3 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[133] is vj4 in component VV_junction_H_D_I (m3_per_s).
 * CONSTANTS[21] is H_to2_VV_junc1 in component parameters (dimensionless).
 * ALGEBRAIC[194] is H_split1 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[195] is H_split2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[196] is H_split3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[197] is H_split4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[198] is H_daughter1 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[199] is H_daughter2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[200] is H_daughter3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[201] is H_daughter4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[202] is H_from1_target in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[203] is H_from2_target in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[204] is H_from3_target in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[205] is H_from4_target in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[206] is H_from1 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[207] is H_from2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[208] is H_from3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[209] is H_from4 in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[22] is r_bc2_VV_junc1 in component parameters (metre).
 * CONSTANTS[65] is D1 in component VV_junction_H_D_I (metre).
 * CONSTANTS[66] is D2 in component VV_junction_H_D_I (metre).
 * CONSTANTS[69] is D3 in component VV_junction_H_D_I (metre).
 * CONSTANTS[70] is D4 in component VV_junction_H_D_I (metre).
 * ALGEBRAIC[138] is w_in1 in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[71] is w_in2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[139] is w_in3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[140] is w_in4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[141] is w_out1 in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[72] is w_out2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[142] is w_out3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[143] is w_out4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[144] is Qin1 in component VV_junction_H_D_I (m3_per_s).
 * CONSTANTS[73] is Qin2 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[145] is Qin3 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[146] is Qin4 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[148] is Qout1 in component VV_junction_H_D_I (m3_per_s).
 * CONSTANTS[74] is Qout2 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[149] is Qout3 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[150] is Qout4 in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[147] is Qin_tot in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[151] is Qout_tot in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[152] is bc1_is_in in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[75] is bc2_is_in in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[153] is bc3_is_in in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[154] is bc4_is_in in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[155] is bc1_is_out in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[76] is bc2_is_out in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[156] is bc3_is_out in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[157] is bc4_is_out in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[159] is n_in in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[158] is n_out in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[160] is junction_type in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[161] is is_split in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[162] is is_merge in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[163] is feed1 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[164] is feed2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[165] is feed3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[166] is feed4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[167] is alpha1 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[168] is alpha2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[169] is alpha3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[170] is alpha4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[171] is Qout1_rem in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[172] is Qout2_rem in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[173] is Qout3_rem in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[174] is Qout4_rem in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[175] is beta1 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[176] is beta2 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[177] is beta3 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[178] is beta4 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[179] is D_F in component VV_junction_H_D_I (metre).
 * ALGEBRAIC[180] is D_alpha in component VV_junction_H_D_I (metre).
 * ALGEBRAIC[181] is D_beta in component VV_junction_H_D_I (metre).
 * ALGEBRAIC[182] is v_alpha in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[183] is v_beta in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[184] is FQB_alpha in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[191] is FQE_alpha in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[185] is B in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[186] is A in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[187] is X_0 in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[190] is ph in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[188] is y_raw in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[189] is y in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[192] is H_VV_out_alpha in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[193] is H_VV_out_beta in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[210] is RBC_in in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[211] is RBC_out in component VV_junction_H_D_I (m3_per_s).
 * CONSTANTS[55] is RBC_volume_init in component VV_junction_H_D_I (m3).
 * STATES[4] is RBC_volume in component VV_junction_H_D_I (m3).
 * ALGEBRAIC[6] is H_mean in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[23] is C_conn2_VV_junc1 in component parameters (m6_per_J).
 * CONSTANTS[56] is C_max12 in component VV_junction_H_D_I (m6_per_J).
 * CONSTANTS[64] is C_max123 in component VV_junction_H_D_I (m6_per_J).
 * CONSTANTS[68] is C in component VV_junction_H_D_I (m6_per_J).
 * STATES[5] is q_C in component VV_junction_H_D_I (m3).
 * STATES[6] is q_C_d in component VV_junction_H_D_I (m3).
 * ALGEBRAIC[0] is q in component VV_junction_H_D_I (m3).
 * CONSTANTS[46] is q_us in component VV_junction_H_D_I (m3).
 * CONSTANTS[24] is R in component parameters_global (Js_per_m6).
 * ALGEBRAIC[7] is u in component VV_junction_H_D_I (J_per_m3).
 * ALGEBRAIC[8] is u_mmHg in component VV_junction_H_D_I (dimensionless).
 * ALGEBRAIC[11] is v in component VV_junction_H_D_I (m3_per_s).
 * ALGEBRAIC[12] is v_mm3_s in component VV_junction_H_D_I (mm3_per_s).
 * ALGEBRAIC[9] is u_d in component VV_junction_H_D_I (J_per_m3).
 * ALGEBRAIC[10] is u_d_mmHg in component VV_junction_H_D_I (dimensionless).
 * CONSTANTS[25] is R_constriction_base in component parameters_global (Js_per_m6).
 * CONSTANTS[26] is R_constriction_final_PV1 in component parameters (Js_per_m6).
 * ALGEBRAIC[13] is R_constriction in component PP_pericyte_H_D_I (Js_per_m6).
 * CONSTANTS[27] is tau_sig in component parameters_global (second).
 * CONSTANTS[28] is t0 in component parameters_global (second).
 * CONSTANTS[29] is r_PV1 in component parameters (metre).
 * ALGEBRAIC[47] is w_v in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[48] is w_v_d in component PP_pericyte_H_D_I (dimensionless).
 * STATES[7] is H_link_R in component PP_pericyte_H_D_I (dimensionless).
 * STATES[8] is H_link_L in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[14] is H_L_in in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[15] is H_R_in in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[104] is H_up in component PP_pericyte_H_D_I (dimensionless).
 * STATES[9] is H_down in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[134] is H_down_target in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[128] is s_v_d in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[49] is H_L_out in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[50] is H_R_out in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[51] is RBC_volume in component PP_pericyte_H_D_I (m3).
 * CONSTANTS[57] is RBC_volume_init in component PP_pericyte_H_D_I (m3).
 * ALGEBRAIC[105] is v_pos in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[106] is v_neg in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[107] is v_d_pos in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[108] is v_d_neg in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[52] is H_mean in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[53] is H_volume_L in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[54] is H_volume_R in component PP_pericyte_H_D_I (dimensionless).
 * STATES[10] is q_C in component PP_pericyte_H_D_I (m3).
 * ALGEBRAIC[16] is q in component PP_pericyte_H_D_I (m3).
 * CONSTANTS[47] is q_us in component PP_pericyte_H_D_I (m3).
 * CONSTANTS[62] is C in component PP_pericyte_H_D_I (m6_per_J).
 * CONSTANTS[77] is Z in component PP_pericyte_H_D_I (dimensionless).
 * CONSTANTS[78] is mu_45 in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[55] is mu in component PP_pericyte_H_D_I (Js_per_m3).
 * ALGEBRAIC[56] is hem_dep_u_rel in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[57] is R in component PP_pericyte_H_D_I (Js_per_m6).
 * ALGEBRAIC[58] is v in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[109] is v_mm3_s in component PP_pericyte_H_D_I (mm3_per_s).
 * ALGEBRAIC[17] is u in component PP_pericyte_H_D_I (J_per_m3).
 * ALGEBRAIC[18] is u_mmHg in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[59] is v_d in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[110] is v_d_mm3_s in component PP_pericyte_H_D_I (mm3_per_s).
 * CONSTANTS[30] is R_constriction_final_PV2 in component parameters (Js_per_m6).
 * ALGEBRAIC[19] is R_constriction in component PP_pericyte_H_D_I (Js_per_m6).
 * CONSTANTS[31] is r_PV2 in component parameters (metre).
 * ALGEBRAIC[60] is w_v in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[61] is w_v_d in component PP_pericyte_H_D_I (dimensionless).
 * STATES[11] is H_link_R in component PP_pericyte_H_D_I (dimensionless).
 * STATES[12] is H_link_L in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[20] is H_L_in in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[21] is H_R_in in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[111] is H_up in component PP_pericyte_H_D_I (dimensionless).
 * STATES[13] is H_down in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[135] is H_down_target in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[129] is s_v_d in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[62] is H_L_out in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[63] is H_R_out in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[64] is RBC_volume in component PP_pericyte_H_D_I (m3).
 * CONSTANTS[59] is RBC_volume_init in component PP_pericyte_H_D_I (m3).
 * ALGEBRAIC[112] is v_pos in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[113] is v_neg in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[114] is v_d_pos in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[115] is v_d_neg in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[65] is H_mean in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[66] is H_volume_L in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[67] is H_volume_R in component PP_pericyte_H_D_I (dimensionless).
 * STATES[14] is q_C in component PP_pericyte_H_D_I (m3).
 * ALGEBRAIC[22] is q in component PP_pericyte_H_D_I (m3).
 * CONSTANTS[49] is q_us in component PP_pericyte_H_D_I (m3).
 * CONSTANTS[67] is C in component PP_pericyte_H_D_I (m6_per_J).
 * CONSTANTS[79] is Z in component PP_pericyte_H_D_I (dimensionless).
 * CONSTANTS[80] is mu_45 in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[68] is mu in component PP_pericyte_H_D_I (Js_per_m3).
 * ALGEBRAIC[69] is hem_dep_u_rel in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[70] is R in component PP_pericyte_H_D_I (Js_per_m6).
 * ALGEBRAIC[71] is v in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[116] is v_mm3_s in component PP_pericyte_H_D_I (mm3_per_s).
 * ALGEBRAIC[23] is u in component PP_pericyte_H_D_I (J_per_m3).
 * ALGEBRAIC[25] is u_mmHg in component PP_pericyte_H_D_I (dimensionless).
 * ALGEBRAIC[72] is v_d in component PP_pericyte_H_D_I (m3_per_s).
 * ALGEBRAIC[117] is v_d_mm3_s in component PP_pericyte_H_D_I (mm3_per_s).
 * CONSTANTS[32] is H_L_out_RHS_V1 in component parameters (dimensionless).
 * CONSTANTS[33] is r_V1 in component parameters (metre).
 * CONSTANTS[34] is u_out_V1 in component parameters (J_per_m3).
 * ALGEBRAIC[73] is w_v in component VP_capillary_H_D_I (dimensionless).
 * STATES[15] is H_link_R in component VP_capillary_H_D_I (dimensionless).
 * STATES[16] is H_link_L in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[24] is H_L_in in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[26] is H_R_in in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[118] is H_up in component VP_capillary_H_D_I (dimensionless).
 * STATES[17] is H_down in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[136] is H_down_target in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[130] is s_v in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[74] is H_L_out in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[75] is H_R_out in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[76] is RBC_volume in component VP_capillary_H_D_I (m3).
 * CONSTANTS[60] is RBC_volume_init in component VP_capillary_H_D_I (m3).
 * ALGEBRAIC[119] is v_pos in component VP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[120] is v_neg in component VP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[77] is H_mean in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[78] is H_volume_L in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[79] is H_volume_R in component VP_capillary_H_D_I (dimensionless).
 * STATES[18] is q_C in component VP_capillary_H_D_I (m3).
 * ALGEBRAIC[27] is q in component VP_capillary_H_D_I (m3).
 * CONSTANTS[50] is q_us in component VP_capillary_H_D_I (m3).
 * CONSTANTS[51] is C in component VP_capillary_H_D_I (m6_per_J).
 * CONSTANTS[81] is Z in component VP_capillary_H_D_I (dimensionless).
 * CONSTANTS[82] is mu_45 in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[80] is mu in component VP_capillary_H_D_I (Js_per_m3).
 * ALGEBRAIC[81] is hem_dep_u_rel in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[82] is R in component VP_capillary_H_D_I (Js_per_m6).
 * ALGEBRAIC[83] is v in component VP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[121] is v_mm3_s in component VP_capillary_H_D_I (mm3_per_s).
 * ALGEBRAIC[28] is u in component VP_capillary_H_D_I (J_per_m3).
 * ALGEBRAIC[30] is u_mmHg in component VP_capillary_H_D_I (dimensionless).
 * CONSTANTS[35] is H_L_out_RHS_V2 in component parameters (dimensionless).
 * CONSTANTS[36] is r_V2 in component parameters (metre).
 * CONSTANTS[37] is u_out_V2 in component parameters (J_per_m3).
 * ALGEBRAIC[84] is w_v in component VP_capillary_H_D_I (dimensionless).
 * STATES[19] is H_link_R in component VP_capillary_H_D_I (dimensionless).
 * STATES[20] is H_link_L in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[29] is H_L_in in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[31] is H_R_in in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[122] is H_up in component VP_capillary_H_D_I (dimensionless).
 * STATES[21] is H_down in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[137] is H_down_target in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[131] is s_v in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[85] is H_L_out in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[86] is H_R_out in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[87] is RBC_volume in component VP_capillary_H_D_I (m3).
 * CONSTANTS[61] is RBC_volume_init in component VP_capillary_H_D_I (m3).
 * ALGEBRAIC[123] is v_pos in component VP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[124] is v_neg in component VP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[88] is H_mean in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[89] is H_volume_L in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[90] is H_volume_R in component VP_capillary_H_D_I (dimensionless).
 * STATES[22] is q_C in component VP_capillary_H_D_I (m3).
 * ALGEBRAIC[32] is q in component VP_capillary_H_D_I (m3).
 * CONSTANTS[52] is q_us in component VP_capillary_H_D_I (m3).
 * CONSTANTS[53] is C in component VP_capillary_H_D_I (m6_per_J).
 * CONSTANTS[83] is Z in component VP_capillary_H_D_I (dimensionless).
 * CONSTANTS[84] is mu_45 in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[91] is mu in component VP_capillary_H_D_I (Js_per_m3).
 * ALGEBRAIC[92] is hem_dep_u_rel in component VP_capillary_H_D_I (dimensionless).
 * ALGEBRAIC[93] is R in component VP_capillary_H_D_I (Js_per_m6).
 * ALGEBRAIC[94] is v in component VP_capillary_H_D_I (m3_per_s).
 * ALGEBRAIC[125] is v_mm3_s in component VP_capillary_H_D_I (mm3_per_s).
 * ALGEBRAIC[33] is u in component VP_capillary_H_D_I (J_per_m3).
 * ALGEBRAIC[95] is u_mmHg in component VP_capillary_H_D_I (dimensionless).
 * CONSTANTS[38] is l_inlet in component parameters (metre).
 * CONSTANTS[39] is l_VV_junc1 in component parameters (metre).
 * CONSTANTS[40] is l_PV1 in component parameters (metre).
 * CONSTANTS[41] is l_PV2 in component parameters (metre).
 * CONSTANTS[42] is l_V1 in component parameters (metre).
 * CONSTANTS[43] is l_V2 in component parameters (metre).
 * RATES[0] is d/dt H_link_R in component PP_capillary_H_D_I (dimensionless).
 * RATES[1] is d/dt H_link_L in component PP_capillary_H_D_I (dimensionless).
 * RATES[2] is d/dt H_down in component PP_capillary_H_D_I (dimensionless).
 * RATES[3] is d/dt q_C in component PP_capillary_H_D_I (m3).
 * RATES[4] is d/dt RBC_volume in component VV_junction_H_D_I (m3).
 * RATES[5] is d/dt q_C in component VV_junction_H_D_I (m3).
 * RATES[6] is d/dt q_C_d in component VV_junction_H_D_I (m3).
 * RATES[7] is d/dt H_link_R in component PP_pericyte_H_D_I (dimensionless).
 * RATES[8] is d/dt H_link_L in component PP_pericyte_H_D_I (dimensionless).
 * RATES[9] is d/dt H_down in component PP_pericyte_H_D_I (dimensionless).
 * RATES[10] is d/dt q_C in component PP_pericyte_H_D_I (m3).
 * RATES[11] is d/dt H_link_R in component PP_pericyte_H_D_I (dimensionless).
 * RATES[12] is d/dt H_link_L in component PP_pericyte_H_D_I (dimensionless).
 * RATES[13] is d/dt H_down in component PP_pericyte_H_D_I (dimensionless).
 * RATES[14] is d/dt q_C in component PP_pericyte_H_D_I (m3).
 * RATES[15] is d/dt H_link_R in component VP_capillary_H_D_I (dimensionless).
 * RATES[16] is d/dt H_link_L in component VP_capillary_H_D_I (dimensionless).
 * RATES[17] is d/dt H_down in component VP_capillary_H_D_I (dimensionless).
 * RATES[18] is d/dt q_C in component VP_capillary_H_D_I (m3).
 * RATES[19] is d/dt H_link_R in component VP_capillary_H_D_I (dimensionless).
 * RATES[20] is d/dt H_link_L in component VP_capillary_H_D_I (dimensionless).
 * RATES[21] is d/dt H_down in component VP_capillary_H_D_I (dimensionless).
 * RATES[22] is d/dt q_C in component VP_capillary_H_D_I (m3).
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
CONSTANTS[17] = 1E-18;
CONSTANTS[18] = 1000;
CONSTANTS[19] = 0.000006;
CONSTANTS[20] = 0;
CONSTANTS[21] = 0;
CONSTANTS[22] = 0;
CONSTANTS[23] = 8.51E-22;
CONSTANTS[24] = 1000000000000000;
CONSTANTS[25] = 0;
CONSTANTS[26] = 0;
CONSTANTS[27] = 1;
CONSTANTS[28] = 500;
CONSTANTS[29] = 0.000006;
CONSTANTS[30] = 0;
CONSTANTS[31] = 0.000006;
CONSTANTS[32] = 0.45;
CONSTANTS[33] = 0.0000055;
CONSTANTS[34] = 6632.7695;
CONSTANTS[35] = 0.45;
CONSTANTS[36] = 0.0000055;
CONSTANTS[37] = 6632.7695;
CONSTANTS[38] = 0.0003;
CONSTANTS[39] = 0.000001;
CONSTANTS[40] = 0.000015;
CONSTANTS[41] = 0.000015;
CONSTANTS[42] = 0.00025;
CONSTANTS[43] = 0.00025;
CONSTANTS[44] =   3.14159265358979*pow(CONSTANTS[8], 2.00000)*CONSTANTS[38];
CONSTANTS[45] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[38])/133.322;
CONSTANTS[46] =   3.14159265358979*pow(CONSTANTS[19], 2.00000)*CONSTANTS[39];
CONSTANTS[47] =   3.14159265358979*pow(CONSTANTS[29], 2.00000)*CONSTANTS[40];
CONSTANTS[48] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[8]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[8]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[8]*1.00000e+06, 12.0000));
CONSTANTS[49] =   3.14159265358979*pow(CONSTANTS[31], 2.00000)*CONSTANTS[41];
CONSTANTS[50] =   3.14159265358979*pow(CONSTANTS[33], 2.00000)*CONSTANTS[42];
CONSTANTS[51] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[42])/133.322;
CONSTANTS[52] =   3.14159265358979*pow(CONSTANTS[36], 2.00000)*CONSTANTS[43];
CONSTANTS[53] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[43])/133.322;
CONSTANTS[54] =  CONSTANTS[0]*CONSTANTS[44];
CONSTANTS[55] =  CONSTANTS[0]*CONSTANTS[46];
CONSTANTS[56] = (CONSTANTS[45]>CONSTANTS[23] ? CONSTANTS[45] : CONSTANTS[45]<=CONSTANTS[23] ? CONSTANTS[23] : 0.0/0.0);
CONSTANTS[57] =  CONSTANTS[0]*CONSTANTS[47];
CONSTANTS[58] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[8]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[8]*1.00000e+06, 0.645000));
CONSTANTS[59] =  CONSTANTS[0]*CONSTANTS[49];
CONSTANTS[60] =  CONSTANTS[0]*CONSTANTS[50];
CONSTANTS[61] =  CONSTANTS[0]*CONSTANTS[52];
CONSTANTS[62] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[40])/133.322;
CONSTANTS[63] = CONSTANTS[20];
CONSTANTS[64] = (CONSTANTS[56]>CONSTANTS[62] ? CONSTANTS[56] : CONSTANTS[56]<=CONSTANTS[62] ? CONSTANTS[62] : 0.0/0.0);
CONSTANTS[65] =  2.00000*CONSTANTS[8];
CONSTANTS[66] =  2.00000*CONSTANTS[22];
CONSTANTS[67] = (  3.14159265358979*pow(8.50000e-09, 2.00000)*CONSTANTS[41])/133.322;
CONSTANTS[68] = (CONSTANTS[64]>CONSTANTS[67] ? CONSTANTS[64] : CONSTANTS[64]<=CONSTANTS[67] ? CONSTANTS[67] : 0.0/0.0);
CONSTANTS[69] =  2.00000*CONSTANTS[29];
CONSTANTS[70] =  2.00000*CONSTANTS[31];
CONSTANTS[71] = 0.500000+ (1.00000/ 3.14159265358979)*atan(CONSTANTS[63]/CONSTANTS[13]);
CONSTANTS[72] = 1.00000 - CONSTANTS[71];
CONSTANTS[73] =  CONSTANTS[71]*CONSTANTS[63];
CONSTANTS[74] =  CONSTANTS[72]*- CONSTANTS[63];
CONSTANTS[75] = (CONSTANTS[73]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
CONSTANTS[76] = (CONSTANTS[74]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
CONSTANTS[77] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[29]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[29]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[29]*1.00000e+06, 12.0000));
CONSTANTS[78] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[29]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[29]*1.00000e+06, 0.645000));
CONSTANTS[79] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[31]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[31]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[31]*1.00000e+06, 12.0000));
CONSTANTS[80] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[31]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[31]*1.00000e+06, 0.645000));
CONSTANTS[81] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[33]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[33]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[33]*1.00000e+06, 12.0000));
CONSTANTS[82] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[33]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[33]*1.00000e+06, 0.645000));
CONSTANTS[83] =  (0.800000+exp( - 0.0750000*2.00000*CONSTANTS[36]*1.00000e+06))*(- 1.00000+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[36]*1.00000e+06, 12.0000)))+1.00000/(1.00000+ pow(10.0000, - 11.0000)*pow( 2.00000*CONSTANTS[36]*1.00000e+06, 12.0000));
CONSTANTS[84] = ( 6.00000*exp( - 0.0850000*2.00000*CONSTANTS[36]*1.00000e+06)+3.20000) -  2.44000*exp( - 0.0600000*pow( 2.00000*CONSTANTS[36]*1.00000e+06, 0.645000));
STATES[0] = CONSTANTS[0];
STATES[1] = CONSTANTS[0];
STATES[2] = CONSTANTS[0];
STATES[3] = CONSTANTS[7];
STATES[4] = CONSTANTS[55];
STATES[5] = CONSTANTS[7];
STATES[6] = CONSTANTS[7];
STATES[7] = CONSTANTS[0];
STATES[8] = CONSTANTS[0];
STATES[9] = CONSTANTS[0];
STATES[10] = CONSTANTS[7];
STATES[11] = CONSTANTS[0];
STATES[12] = CONSTANTS[0];
STATES[13] = CONSTANTS[0];
STATES[14] = CONSTANTS[7];
STATES[15] = CONSTANTS[0];
STATES[16] = CONSTANTS[0];
STATES[17] = CONSTANTS[0];
STATES[18] = CONSTANTS[7];
STATES[19] = CONSTANTS[0];
STATES[20] = CONSTANTS[0];
STATES[21] = CONSTANTS[0];
STATES[22] = CONSTANTS[7];
}
void
computeRates(double VOI, double* CONSTANTS, double* RATES, double* STATES, double* ALGEBRAIC)
{
RATES[1] = (CONSTANTS[2] - STATES[1])/CONSTANTS[12];
RATES[15] = (CONSTANTS[32] - STATES[15])/CONSTANTS[12];
RATES[19] = (CONSTANTS[35] - STATES[19])/CONSTANTS[12];
ALGEBRAIC[1] = STATES[1];
ALGEBRAIC[2] = STATES[0];
ALGEBRAIC[3] = CONSTANTS[44]+STATES[3];
ALGEBRAIC[4] = STATES[3]/CONSTANTS[45]+CONSTANTS[11];
ALGEBRAIC[7] = STATES[5]/(CONSTANTS[68]/2.00000)+CONSTANTS[11];
ALGEBRAIC[9] = STATES[6]/(CONSTANTS[68]/2.00000)+CONSTANTS[11];
ALGEBRAIC[13] = CONSTANTS[25]+(CONSTANTS[26] - CONSTANTS[25])/(1.00000+exp(- (VOI - CONSTANTS[28])/CONSTANTS[27]));
ALGEBRAIC[14] = STATES[8];
ALGEBRAIC[15] = STATES[7];
ALGEBRAIC[16] = CONSTANTS[47]+STATES[10];
ALGEBRAIC[17] = STATES[10]/CONSTANTS[62]+CONSTANTS[11];
ALGEBRAIC[19] = CONSTANTS[25]+(CONSTANTS[30] - CONSTANTS[25])/(1.00000+exp(- (VOI - CONSTANTS[28])/CONSTANTS[27]));
ALGEBRAIC[20] = STATES[12];
ALGEBRAIC[21] = STATES[11];
ALGEBRAIC[22] = CONSTANTS[49]+STATES[14];
ALGEBRAIC[23] = STATES[14]/CONSTANTS[67]+CONSTANTS[11];
ALGEBRAIC[24] = STATES[16];
ALGEBRAIC[26] = STATES[15];
ALGEBRAIC[27] = CONSTANTS[50]+STATES[18];
ALGEBRAIC[28] = STATES[18]/CONSTANTS[51]+CONSTANTS[11];
ALGEBRAIC[29] = STATES[20];
ALGEBRAIC[31] = STATES[19];
ALGEBRAIC[32] = CONSTANTS[52]+STATES[22];
ALGEBRAIC[33] = STATES[22]/CONSTANTS[53]+CONSTANTS[11];
rootfind_0(VOI, CONSTANTS, RATES, STATES, ALGEBRAIC, pret);
RATES[3] = ALGEBRAIC[45] - ALGEBRAIC[46];
ALGEBRAIC[11] = (ALGEBRAIC[7] - ALGEBRAIC[9])/CONSTANTS[24];
RATES[5] = (ALGEBRAIC[46]+CONSTANTS[20]) - ALGEBRAIC[11];
RATES[6] = (ALGEBRAIC[11] - ALGEBRAIC[58]) - ALGEBRAIC[71];
RATES[7] = (ALGEBRAIC[74] - STATES[7])/CONSTANTS[12];
RATES[10] = ALGEBRAIC[58] - ALGEBRAIC[59];
RATES[11] = (ALGEBRAIC[85] - STATES[11])/CONSTANTS[12];
RATES[14] = ALGEBRAIC[71] - ALGEBRAIC[72];
RATES[16] = (ALGEBRAIC[50] - STATES[16])/CONSTANTS[12];
RATES[18] = ALGEBRAIC[59] - ALGEBRAIC[83];
RATES[20] = (ALGEBRAIC[63] - STATES[20])/CONSTANTS[12];
RATES[22] = ALGEBRAIC[72] - ALGEBRAIC[94];
ALGEBRAIC[96] =  ALGEBRAIC[35]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[35])*ALGEBRAIC[2];
ALGEBRAIC[126] = fabs(ALGEBRAIC[46])/(fabs(ALGEBRAIC[46])+CONSTANTS[6]);
ALGEBRAIC[132] =  ALGEBRAIC[126]*(ALGEBRAIC[39]+ CONSTANTS[3]*(ALGEBRAIC[39] - ALGEBRAIC[96]))+ (1.00000 - ALGEBRAIC[126])*ALGEBRAIC[39];
RATES[2] = (ALGEBRAIC[132] - STATES[2])/CONSTANTS[4];
ALGEBRAIC[104] =  ALGEBRAIC[48]*ALGEBRAIC[14]+ (1.00000 - ALGEBRAIC[48])*ALGEBRAIC[15];
ALGEBRAIC[128] = fabs(ALGEBRAIC[59])/(fabs(ALGEBRAIC[59])+CONSTANTS[6]);
ALGEBRAIC[134] =  ALGEBRAIC[128]*(ALGEBRAIC[52]+ CONSTANTS[3]*(ALGEBRAIC[52] - ALGEBRAIC[104]))+ (1.00000 - ALGEBRAIC[128])*ALGEBRAIC[52];
RATES[9] = (ALGEBRAIC[134] - STATES[9])/CONSTANTS[4];
ALGEBRAIC[111] =  ALGEBRAIC[61]*ALGEBRAIC[20]+ (1.00000 - ALGEBRAIC[61])*ALGEBRAIC[21];
ALGEBRAIC[129] = fabs(ALGEBRAIC[72])/(fabs(ALGEBRAIC[72])+CONSTANTS[6]);
ALGEBRAIC[135] =  ALGEBRAIC[129]*(ALGEBRAIC[65]+ CONSTANTS[3]*(ALGEBRAIC[65] - ALGEBRAIC[111]))+ (1.00000 - ALGEBRAIC[129])*ALGEBRAIC[65];
RATES[13] = (ALGEBRAIC[135] - STATES[13])/CONSTANTS[4];
ALGEBRAIC[118] =  ALGEBRAIC[73]*ALGEBRAIC[24]+ (1.00000 - ALGEBRAIC[73])*ALGEBRAIC[26];
ALGEBRAIC[130] = fabs(ALGEBRAIC[83])/(fabs(ALGEBRAIC[83])+CONSTANTS[6]);
ALGEBRAIC[136] =  ALGEBRAIC[130]*(ALGEBRAIC[77]+ CONSTANTS[3]*(ALGEBRAIC[77] - ALGEBRAIC[118]))+ (1.00000 - ALGEBRAIC[130])*ALGEBRAIC[77];
RATES[17] = (ALGEBRAIC[136] - STATES[17])/CONSTANTS[4];
ALGEBRAIC[122] =  ALGEBRAIC[84]*ALGEBRAIC[29]+ (1.00000 - ALGEBRAIC[84])*ALGEBRAIC[31];
ALGEBRAIC[131] = fabs(ALGEBRAIC[94])/(fabs(ALGEBRAIC[94])+CONSTANTS[6]);
ALGEBRAIC[137] =  ALGEBRAIC[131]*(ALGEBRAIC[88]+ CONSTANTS[3]*(ALGEBRAIC[88] - ALGEBRAIC[122]))+ (1.00000 - ALGEBRAIC[131])*ALGEBRAIC[88];
RATES[21] = (ALGEBRAIC[137] - STATES[21])/CONSTANTS[4];
ALGEBRAIC[103] = ALGEBRAIC[46];
ALGEBRAIC[138] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[103]/CONSTANTS[13]);
ALGEBRAIC[141] = 1.00000 - ALGEBRAIC[138];
ALGEBRAIC[148] =  ALGEBRAIC[141]*- ALGEBRAIC[103];
ALGEBRAIC[127] = - ALGEBRAIC[58];
ALGEBRAIC[139] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[127]/CONSTANTS[13]);
ALGEBRAIC[142] = 1.00000 - ALGEBRAIC[139];
ALGEBRAIC[149] =  ALGEBRAIC[142]*- ALGEBRAIC[127];
ALGEBRAIC[133] = - ALGEBRAIC[71];
ALGEBRAIC[140] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[133]/CONSTANTS[13]);
ALGEBRAIC[143] = 1.00000 - ALGEBRAIC[140];
ALGEBRAIC[150] =  ALGEBRAIC[143]*- ALGEBRAIC[133];
ALGEBRAIC[155] = (ALGEBRAIC[148]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[144] =  ALGEBRAIC[138]*ALGEBRAIC[103];
ALGEBRAIC[152] = (ALGEBRAIC[144]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[145] =  ALGEBRAIC[139]*ALGEBRAIC[127];
ALGEBRAIC[153] = (ALGEBRAIC[145]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[146] =  ALGEBRAIC[140]*ALGEBRAIC[133];
ALGEBRAIC[154] = (ALGEBRAIC[146]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[159] = ALGEBRAIC[152]+CONSTANTS[75]+ALGEBRAIC[153]+ALGEBRAIC[154];
ALGEBRAIC[160] = (ALGEBRAIC[159]==1.00000 ? 1.00000 : ALGEBRAIC[159]>=2.00000 ? - 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[161] = (ALGEBRAIC[160]==1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[167] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[155]==1.00000&&ALGEBRAIC[148]>=CONSTANTS[74]&&ALGEBRAIC[148]>=ALGEBRAIC[149]&&ALGEBRAIC[148]>=ALGEBRAIC[150] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[171] = (ALGEBRAIC[167]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[148] : 0.0/0.0);
ALGEBRAIC[168] = (ALGEBRAIC[161]==1.00000&&CONSTANTS[76]==1.00000&&CONSTANTS[74]>ALGEBRAIC[148]&&CONSTANTS[74]>=ALGEBRAIC[149]&&CONSTANTS[74]>=ALGEBRAIC[150] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[172] = (ALGEBRAIC[168]==1.00000 ? 0.00000 : 1 ? CONSTANTS[74] : 0.0/0.0);
ALGEBRAIC[156] = (ALGEBRAIC[149]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[169] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[156]==1.00000&&ALGEBRAIC[149]>ALGEBRAIC[148]&&ALGEBRAIC[149]>CONSTANTS[74]&&ALGEBRAIC[149]>=ALGEBRAIC[150] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[173] = (ALGEBRAIC[169]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[149] : 0.0/0.0);
ALGEBRAIC[157] = (ALGEBRAIC[150]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[170] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[157]==1.00000&&ALGEBRAIC[150]>ALGEBRAIC[148]&&ALGEBRAIC[150]>CONSTANTS[74]&&ALGEBRAIC[150]>ALGEBRAIC[149] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[174] = (ALGEBRAIC[170]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[150] : 0.0/0.0);
ALGEBRAIC[175] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[155]==1.00000&&ALGEBRAIC[167]==0.00000&&ALGEBRAIC[171]>=ALGEBRAIC[172]&&ALGEBRAIC[171]>=ALGEBRAIC[173]&&ALGEBRAIC[171]>=ALGEBRAIC[174] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[182] = (ALGEBRAIC[167]==1.00000 ? ALGEBRAIC[148] : ALGEBRAIC[168]==1.00000 ? CONSTANTS[74] : ALGEBRAIC[169]==1.00000 ? ALGEBRAIC[149] : ALGEBRAIC[170]==1.00000 ? ALGEBRAIC[150] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[176] = (ALGEBRAIC[161]==1.00000&&CONSTANTS[76]==1.00000&&ALGEBRAIC[168]==0.00000&&ALGEBRAIC[172]>ALGEBRAIC[171]&&ALGEBRAIC[172]>=ALGEBRAIC[173]&&ALGEBRAIC[172]>=ALGEBRAIC[174] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[177] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[156]==1.00000&&ALGEBRAIC[169]==0.00000&&ALGEBRAIC[173]>ALGEBRAIC[171]&&ALGEBRAIC[173]>ALGEBRAIC[172]&&ALGEBRAIC[173]>=ALGEBRAIC[174] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[178] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[157]==1.00000&&ALGEBRAIC[170]==0.00000&&ALGEBRAIC[174]>ALGEBRAIC[171]&&ALGEBRAIC[174]>ALGEBRAIC[172]&&ALGEBRAIC[174]>ALGEBRAIC[173] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[183] = (ALGEBRAIC[175]==1.00000 ? ALGEBRAIC[148] : ALGEBRAIC[176]==1.00000 ? CONSTANTS[74] : ALGEBRAIC[177]==1.00000 ? ALGEBRAIC[149] : ALGEBRAIC[178]==1.00000 ? ALGEBRAIC[150] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[184] = (ALGEBRAIC[182]+CONSTANTS[15])/(ALGEBRAIC[182]+ALGEBRAIC[183]+ 2.00000*CONSTANTS[15]);
ALGEBRAIC[163] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[144]>=CONSTANTS[73]&&ALGEBRAIC[144]>=ALGEBRAIC[145]&&ALGEBRAIC[144]>=ALGEBRAIC[146] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[164] = (ALGEBRAIC[161]==1.00000&&CONSTANTS[73]>ALGEBRAIC[144]&&CONSTANTS[73]>=ALGEBRAIC[145]&&CONSTANTS[73]>=ALGEBRAIC[146] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[165] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[145]>ALGEBRAIC[144]&&ALGEBRAIC[145]>CONSTANTS[73]&&ALGEBRAIC[145]>=ALGEBRAIC[146] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[166] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[146]>ALGEBRAIC[144]&&ALGEBRAIC[146]>CONSTANTS[73]&&ALGEBRAIC[146]>ALGEBRAIC[145] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[179] = (ALGEBRAIC[163]==1.00000 ? CONSTANTS[65] : ALGEBRAIC[164]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[165]==1.00000 ? CONSTANTS[69] : ALGEBRAIC[166]==1.00000 ? CONSTANTS[70] : 1 ? CONSTANTS[65] : 0.0/0.0);
ALGEBRAIC[6] = STATES[4]/(CONSTANTS[46]+CONSTANTS[15]);
ALGEBRAIC[185] = 1.00000+( 6.98000*(1.00000 - ALGEBRAIC[6]))/( ALGEBRAIC[179]*1.00000e+06);
ALGEBRAIC[180] = (ALGEBRAIC[167]==1.00000 ? CONSTANTS[65] : ALGEBRAIC[168]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[169]==1.00000 ? CONSTANTS[69] : ALGEBRAIC[170]==1.00000 ? CONSTANTS[70] : 1 ? CONSTANTS[69] : 0.0/0.0);
ALGEBRAIC[181] = (ALGEBRAIC[175]==1.00000 ? CONSTANTS[65] : ALGEBRAIC[176]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[177]==1.00000 ? CONSTANTS[69] : ALGEBRAIC[178]==1.00000 ? CONSTANTS[70] : 1 ? CONSTANTS[70] : 0.0/0.0);
ALGEBRAIC[186] = ( - 6.96000*log(( ALGEBRAIC[180]*1.00000e+06)/( ALGEBRAIC[181]*1.00000e+06)))/( ALGEBRAIC[179]*1.00000e+06);
ALGEBRAIC[187] = 0.400000/( ALGEBRAIC[179]*1.00000e+06);
ALGEBRAIC[188] = (ALGEBRAIC[184] - ALGEBRAIC[187])/((1.00000 -  2.00000*ALGEBRAIC[187])+CONSTANTS[15]);
ALGEBRAIC[189] = multi_min(2, multi_max(2, ALGEBRAIC[188], CONSTANTS[16]), 1.00000 - CONSTANTS[16]);
ALGEBRAIC[190] = log(ALGEBRAIC[189]/(1.00000 - ALGEBRAIC[189]));
ALGEBRAIC[191] = 1.00000/(1.00000+exp(- (ALGEBRAIC[186]+ ALGEBRAIC[185]*ALGEBRAIC[190])));
ALGEBRAIC[192] = ( ALGEBRAIC[6]*ALGEBRAIC[191])/(ALGEBRAIC[184]+CONSTANTS[15]);
ALGEBRAIC[193] = ( ALGEBRAIC[6]*(1.00000 - ALGEBRAIC[191]))/((1.00000 - ALGEBRAIC[184])+CONSTANTS[15]);
ALGEBRAIC[194] = (ALGEBRAIC[167]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[175]==1.00000 ? ALGEBRAIC[193] : 1 ? ALGEBRAIC[37] : 0.0/0.0);
ALGEBRAIC[162] = (ALGEBRAIC[160]==- 1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[198] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[194] : 1 ? ALGEBRAIC[37] : 0.0/0.0);
ALGEBRAIC[202] = (ALGEBRAIC[155]==1.00000 ? ALGEBRAIC[198] : 1 ? ALGEBRAIC[37] : 0.0/0.0);
ALGEBRAIC[206] =  ALGEBRAIC[141]*ALGEBRAIC[202];
RATES[0] = (ALGEBRAIC[206] - STATES[0])/CONSTANTS[12];
ALGEBRAIC[196] = (ALGEBRAIC[169]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[177]==1.00000 ? ALGEBRAIC[193] : 1 ? ALGEBRAIC[49] : 0.0/0.0);
ALGEBRAIC[200] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[196] : 1 ? ALGEBRAIC[49] : 0.0/0.0);
ALGEBRAIC[204] = (ALGEBRAIC[156]==1.00000 ? ALGEBRAIC[200] : 1 ? ALGEBRAIC[49] : 0.0/0.0);
ALGEBRAIC[208] =  ALGEBRAIC[142]*ALGEBRAIC[204];
RATES[8] = (ALGEBRAIC[208] - STATES[8])/CONSTANTS[12];
ALGEBRAIC[197] = (ALGEBRAIC[170]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[178]==1.00000 ? ALGEBRAIC[193] : 1 ? ALGEBRAIC[62] : 0.0/0.0);
ALGEBRAIC[201] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[197] : 1 ? ALGEBRAIC[62] : 0.0/0.0);
ALGEBRAIC[205] = (ALGEBRAIC[157]==1.00000 ? ALGEBRAIC[201] : 1 ? ALGEBRAIC[62] : 0.0/0.0);
ALGEBRAIC[209] =  ALGEBRAIC[143]*ALGEBRAIC[205];
RATES[12] = (ALGEBRAIC[209] - STATES[12])/CONSTANTS[12];
ALGEBRAIC[210] =  ALGEBRAIC[144]*ALGEBRAIC[37]+ CONSTANTS[73]*CONSTANTS[21]+ ALGEBRAIC[145]*ALGEBRAIC[49]+ ALGEBRAIC[146]*ALGEBRAIC[62];
ALGEBRAIC[195] = (ALGEBRAIC[168]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[176]==1.00000 ? ALGEBRAIC[193] : 1 ? CONSTANTS[21] : 0.0/0.0);
ALGEBRAIC[199] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[195] : 1 ? CONSTANTS[21] : 0.0/0.0);
ALGEBRAIC[203] = (CONSTANTS[76]==1.00000 ? ALGEBRAIC[199] : 1 ? CONSTANTS[21] : 0.0/0.0);
ALGEBRAIC[207] =  CONSTANTS[72]*ALGEBRAIC[203];
ALGEBRAIC[211] =  ALGEBRAIC[148]*ALGEBRAIC[206]+ CONSTANTS[74]*ALGEBRAIC[207]+ ALGEBRAIC[149]*ALGEBRAIC[208]+ ALGEBRAIC[150]*ALGEBRAIC[209];
RATES[4] = ALGEBRAIC[210] - ALGEBRAIC[211];
}
void
computeVariables(double VOI, double* CONSTANTS, double* RATES, double* STATES, double* ALGEBRAIC)
{
ALGEBRAIC[1] = STATES[1];
ALGEBRAIC[2] = STATES[0];
ALGEBRAIC[3] = CONSTANTS[44]+STATES[3];
ALGEBRAIC[4] = STATES[3]/CONSTANTS[45]+CONSTANTS[11];
ALGEBRAIC[7] = STATES[5]/(CONSTANTS[68]/2.00000)+CONSTANTS[11];
ALGEBRAIC[9] = STATES[6]/(CONSTANTS[68]/2.00000)+CONSTANTS[11];
ALGEBRAIC[13] = CONSTANTS[25]+(CONSTANTS[26] - CONSTANTS[25])/(1.00000+exp(- (VOI - CONSTANTS[28])/CONSTANTS[27]));
ALGEBRAIC[14] = STATES[8];
ALGEBRAIC[15] = STATES[7];
ALGEBRAIC[16] = CONSTANTS[47]+STATES[10];
ALGEBRAIC[17] = STATES[10]/CONSTANTS[62]+CONSTANTS[11];
ALGEBRAIC[19] = CONSTANTS[25]+(CONSTANTS[30] - CONSTANTS[25])/(1.00000+exp(- (VOI - CONSTANTS[28])/CONSTANTS[27]));
ALGEBRAIC[20] = STATES[12];
ALGEBRAIC[21] = STATES[11];
ALGEBRAIC[22] = CONSTANTS[49]+STATES[14];
ALGEBRAIC[23] = STATES[14]/CONSTANTS[67]+CONSTANTS[11];
ALGEBRAIC[24] = STATES[16];
ALGEBRAIC[26] = STATES[15];
ALGEBRAIC[27] = CONSTANTS[50]+STATES[18];
ALGEBRAIC[28] = STATES[18]/CONSTANTS[51]+CONSTANTS[11];
ALGEBRAIC[29] = STATES[20];
ALGEBRAIC[31] = STATES[19];
ALGEBRAIC[32] = CONSTANTS[52]+STATES[22];
ALGEBRAIC[33] = STATES[22]/CONSTANTS[53]+CONSTANTS[11];
ALGEBRAIC[11] = (ALGEBRAIC[7] - ALGEBRAIC[9])/CONSTANTS[24];
ALGEBRAIC[96] =  ALGEBRAIC[35]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[35])*ALGEBRAIC[2];
ALGEBRAIC[126] = fabs(ALGEBRAIC[46])/(fabs(ALGEBRAIC[46])+CONSTANTS[6]);
ALGEBRAIC[132] =  ALGEBRAIC[126]*(ALGEBRAIC[39]+ CONSTANTS[3]*(ALGEBRAIC[39] - ALGEBRAIC[96]))+ (1.00000 - ALGEBRAIC[126])*ALGEBRAIC[39];
ALGEBRAIC[104] =  ALGEBRAIC[48]*ALGEBRAIC[14]+ (1.00000 - ALGEBRAIC[48])*ALGEBRAIC[15];
ALGEBRAIC[128] = fabs(ALGEBRAIC[59])/(fabs(ALGEBRAIC[59])+CONSTANTS[6]);
ALGEBRAIC[134] =  ALGEBRAIC[128]*(ALGEBRAIC[52]+ CONSTANTS[3]*(ALGEBRAIC[52] - ALGEBRAIC[104]))+ (1.00000 - ALGEBRAIC[128])*ALGEBRAIC[52];
ALGEBRAIC[111] =  ALGEBRAIC[61]*ALGEBRAIC[20]+ (1.00000 - ALGEBRAIC[61])*ALGEBRAIC[21];
ALGEBRAIC[129] = fabs(ALGEBRAIC[72])/(fabs(ALGEBRAIC[72])+CONSTANTS[6]);
ALGEBRAIC[135] =  ALGEBRAIC[129]*(ALGEBRAIC[65]+ CONSTANTS[3]*(ALGEBRAIC[65] - ALGEBRAIC[111]))+ (1.00000 - ALGEBRAIC[129])*ALGEBRAIC[65];
ALGEBRAIC[118] =  ALGEBRAIC[73]*ALGEBRAIC[24]+ (1.00000 - ALGEBRAIC[73])*ALGEBRAIC[26];
ALGEBRAIC[130] = fabs(ALGEBRAIC[83])/(fabs(ALGEBRAIC[83])+CONSTANTS[6]);
ALGEBRAIC[136] =  ALGEBRAIC[130]*(ALGEBRAIC[77]+ CONSTANTS[3]*(ALGEBRAIC[77] - ALGEBRAIC[118]))+ (1.00000 - ALGEBRAIC[130])*ALGEBRAIC[77];
ALGEBRAIC[122] =  ALGEBRAIC[84]*ALGEBRAIC[29]+ (1.00000 - ALGEBRAIC[84])*ALGEBRAIC[31];
ALGEBRAIC[131] = fabs(ALGEBRAIC[94])/(fabs(ALGEBRAIC[94])+CONSTANTS[6]);
ALGEBRAIC[137] =  ALGEBRAIC[131]*(ALGEBRAIC[88]+ CONSTANTS[3]*(ALGEBRAIC[88] - ALGEBRAIC[122]))+ (1.00000 - ALGEBRAIC[131])*ALGEBRAIC[88];
ALGEBRAIC[103] = ALGEBRAIC[46];
ALGEBRAIC[138] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[103]/CONSTANTS[13]);
ALGEBRAIC[141] = 1.00000 - ALGEBRAIC[138];
ALGEBRAIC[148] =  ALGEBRAIC[141]*- ALGEBRAIC[103];
ALGEBRAIC[127] = - ALGEBRAIC[58];
ALGEBRAIC[139] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[127]/CONSTANTS[13]);
ALGEBRAIC[142] = 1.00000 - ALGEBRAIC[139];
ALGEBRAIC[149] =  ALGEBRAIC[142]*- ALGEBRAIC[127];
ALGEBRAIC[133] = - ALGEBRAIC[71];
ALGEBRAIC[140] = 0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[133]/CONSTANTS[13]);
ALGEBRAIC[143] = 1.00000 - ALGEBRAIC[140];
ALGEBRAIC[150] =  ALGEBRAIC[143]*- ALGEBRAIC[133];
ALGEBRAIC[155] = (ALGEBRAIC[148]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[144] =  ALGEBRAIC[138]*ALGEBRAIC[103];
ALGEBRAIC[152] = (ALGEBRAIC[144]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[145] =  ALGEBRAIC[139]*ALGEBRAIC[127];
ALGEBRAIC[153] = (ALGEBRAIC[145]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[146] =  ALGEBRAIC[140]*ALGEBRAIC[133];
ALGEBRAIC[154] = (ALGEBRAIC[146]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[159] = ALGEBRAIC[152]+CONSTANTS[75]+ALGEBRAIC[153]+ALGEBRAIC[154];
ALGEBRAIC[160] = (ALGEBRAIC[159]==1.00000 ? 1.00000 : ALGEBRAIC[159]>=2.00000 ? - 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[161] = (ALGEBRAIC[160]==1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[167] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[155]==1.00000&&ALGEBRAIC[148]>=CONSTANTS[74]&&ALGEBRAIC[148]>=ALGEBRAIC[149]&&ALGEBRAIC[148]>=ALGEBRAIC[150] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[171] = (ALGEBRAIC[167]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[148] : 0.0/0.0);
ALGEBRAIC[168] = (ALGEBRAIC[161]==1.00000&&CONSTANTS[76]==1.00000&&CONSTANTS[74]>ALGEBRAIC[148]&&CONSTANTS[74]>=ALGEBRAIC[149]&&CONSTANTS[74]>=ALGEBRAIC[150] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[172] = (ALGEBRAIC[168]==1.00000 ? 0.00000 : 1 ? CONSTANTS[74] : 0.0/0.0);
ALGEBRAIC[156] = (ALGEBRAIC[149]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[169] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[156]==1.00000&&ALGEBRAIC[149]>ALGEBRAIC[148]&&ALGEBRAIC[149]>CONSTANTS[74]&&ALGEBRAIC[149]>=ALGEBRAIC[150] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[173] = (ALGEBRAIC[169]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[149] : 0.0/0.0);
ALGEBRAIC[157] = (ALGEBRAIC[150]>CONSTANTS[17] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[170] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[157]==1.00000&&ALGEBRAIC[150]>ALGEBRAIC[148]&&ALGEBRAIC[150]>CONSTANTS[74]&&ALGEBRAIC[150]>ALGEBRAIC[149] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[174] = (ALGEBRAIC[170]==1.00000 ? 0.00000 : 1 ? ALGEBRAIC[150] : 0.0/0.0);
ALGEBRAIC[175] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[155]==1.00000&&ALGEBRAIC[167]==0.00000&&ALGEBRAIC[171]>=ALGEBRAIC[172]&&ALGEBRAIC[171]>=ALGEBRAIC[173]&&ALGEBRAIC[171]>=ALGEBRAIC[174] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[182] = (ALGEBRAIC[167]==1.00000 ? ALGEBRAIC[148] : ALGEBRAIC[168]==1.00000 ? CONSTANTS[74] : ALGEBRAIC[169]==1.00000 ? ALGEBRAIC[149] : ALGEBRAIC[170]==1.00000 ? ALGEBRAIC[150] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[176] = (ALGEBRAIC[161]==1.00000&&CONSTANTS[76]==1.00000&&ALGEBRAIC[168]==0.00000&&ALGEBRAIC[172]>ALGEBRAIC[171]&&ALGEBRAIC[172]>=ALGEBRAIC[173]&&ALGEBRAIC[172]>=ALGEBRAIC[174] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[177] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[156]==1.00000&&ALGEBRAIC[169]==0.00000&&ALGEBRAIC[173]>ALGEBRAIC[171]&&ALGEBRAIC[173]>ALGEBRAIC[172]&&ALGEBRAIC[173]>=ALGEBRAIC[174] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[178] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[157]==1.00000&&ALGEBRAIC[170]==0.00000&&ALGEBRAIC[174]>ALGEBRAIC[171]&&ALGEBRAIC[174]>ALGEBRAIC[172]&&ALGEBRAIC[174]>ALGEBRAIC[173] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[183] = (ALGEBRAIC[175]==1.00000 ? ALGEBRAIC[148] : ALGEBRAIC[176]==1.00000 ? CONSTANTS[74] : ALGEBRAIC[177]==1.00000 ? ALGEBRAIC[149] : ALGEBRAIC[178]==1.00000 ? ALGEBRAIC[150] : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[184] = (ALGEBRAIC[182]+CONSTANTS[15])/(ALGEBRAIC[182]+ALGEBRAIC[183]+ 2.00000*CONSTANTS[15]);
ALGEBRAIC[163] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[144]>=CONSTANTS[73]&&ALGEBRAIC[144]>=ALGEBRAIC[145]&&ALGEBRAIC[144]>=ALGEBRAIC[146] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[164] = (ALGEBRAIC[161]==1.00000&&CONSTANTS[73]>ALGEBRAIC[144]&&CONSTANTS[73]>=ALGEBRAIC[145]&&CONSTANTS[73]>=ALGEBRAIC[146] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[165] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[145]>ALGEBRAIC[144]&&ALGEBRAIC[145]>CONSTANTS[73]&&ALGEBRAIC[145]>=ALGEBRAIC[146] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[166] = (ALGEBRAIC[161]==1.00000&&ALGEBRAIC[146]>ALGEBRAIC[144]&&ALGEBRAIC[146]>CONSTANTS[73]&&ALGEBRAIC[146]>ALGEBRAIC[145] ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[179] = (ALGEBRAIC[163]==1.00000 ? CONSTANTS[65] : ALGEBRAIC[164]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[165]==1.00000 ? CONSTANTS[69] : ALGEBRAIC[166]==1.00000 ? CONSTANTS[70] : 1 ? CONSTANTS[65] : 0.0/0.0);
ALGEBRAIC[6] = STATES[4]/(CONSTANTS[46]+CONSTANTS[15]);
ALGEBRAIC[185] = 1.00000+( 6.98000*(1.00000 - ALGEBRAIC[6]))/( ALGEBRAIC[179]*1.00000e+06);
ALGEBRAIC[180] = (ALGEBRAIC[167]==1.00000 ? CONSTANTS[65] : ALGEBRAIC[168]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[169]==1.00000 ? CONSTANTS[69] : ALGEBRAIC[170]==1.00000 ? CONSTANTS[70] : 1 ? CONSTANTS[69] : 0.0/0.0);
ALGEBRAIC[181] = (ALGEBRAIC[175]==1.00000 ? CONSTANTS[65] : ALGEBRAIC[176]==1.00000 ? CONSTANTS[66] : ALGEBRAIC[177]==1.00000 ? CONSTANTS[69] : ALGEBRAIC[178]==1.00000 ? CONSTANTS[70] : 1 ? CONSTANTS[70] : 0.0/0.0);
ALGEBRAIC[186] = ( - 6.96000*log(( ALGEBRAIC[180]*1.00000e+06)/( ALGEBRAIC[181]*1.00000e+06)))/( ALGEBRAIC[179]*1.00000e+06);
ALGEBRAIC[187] = 0.400000/( ALGEBRAIC[179]*1.00000e+06);
ALGEBRAIC[188] = (ALGEBRAIC[184] - ALGEBRAIC[187])/((1.00000 -  2.00000*ALGEBRAIC[187])+CONSTANTS[15]);
ALGEBRAIC[189] = multi_min(2, multi_max(2, ALGEBRAIC[188], CONSTANTS[16]), 1.00000 - CONSTANTS[16]);
ALGEBRAIC[190] = log(ALGEBRAIC[189]/(1.00000 - ALGEBRAIC[189]));
ALGEBRAIC[191] = 1.00000/(1.00000+exp(- (ALGEBRAIC[186]+ ALGEBRAIC[185]*ALGEBRAIC[190])));
ALGEBRAIC[192] = ( ALGEBRAIC[6]*ALGEBRAIC[191])/(ALGEBRAIC[184]+CONSTANTS[15]);
ALGEBRAIC[193] = ( ALGEBRAIC[6]*(1.00000 - ALGEBRAIC[191]))/((1.00000 - ALGEBRAIC[184])+CONSTANTS[15]);
ALGEBRAIC[194] = (ALGEBRAIC[167]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[175]==1.00000 ? ALGEBRAIC[193] : 1 ? ALGEBRAIC[37] : 0.0/0.0);
ALGEBRAIC[162] = (ALGEBRAIC[160]==- 1.00000 ? 1.00000 : 1 ? 0.00000 : 0.0/0.0);
ALGEBRAIC[198] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[194] : 1 ? ALGEBRAIC[37] : 0.0/0.0);
ALGEBRAIC[202] = (ALGEBRAIC[155]==1.00000 ? ALGEBRAIC[198] : 1 ? ALGEBRAIC[37] : 0.0/0.0);
ALGEBRAIC[206] =  ALGEBRAIC[141]*ALGEBRAIC[202];
ALGEBRAIC[196] = (ALGEBRAIC[169]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[177]==1.00000 ? ALGEBRAIC[193] : 1 ? ALGEBRAIC[49] : 0.0/0.0);
ALGEBRAIC[200] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[196] : 1 ? ALGEBRAIC[49] : 0.0/0.0);
ALGEBRAIC[204] = (ALGEBRAIC[156]==1.00000 ? ALGEBRAIC[200] : 1 ? ALGEBRAIC[49] : 0.0/0.0);
ALGEBRAIC[208] =  ALGEBRAIC[142]*ALGEBRAIC[204];
ALGEBRAIC[197] = (ALGEBRAIC[170]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[178]==1.00000 ? ALGEBRAIC[193] : 1 ? ALGEBRAIC[62] : 0.0/0.0);
ALGEBRAIC[201] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[197] : 1 ? ALGEBRAIC[62] : 0.0/0.0);
ALGEBRAIC[205] = (ALGEBRAIC[157]==1.00000 ? ALGEBRAIC[201] : 1 ? ALGEBRAIC[62] : 0.0/0.0);
ALGEBRAIC[209] =  ALGEBRAIC[143]*ALGEBRAIC[205];
ALGEBRAIC[210] =  ALGEBRAIC[144]*ALGEBRAIC[37]+ CONSTANTS[73]*CONSTANTS[21]+ ALGEBRAIC[145]*ALGEBRAIC[49]+ ALGEBRAIC[146]*ALGEBRAIC[62];
ALGEBRAIC[195] = (ALGEBRAIC[168]==1.00000 ? ALGEBRAIC[192] : ALGEBRAIC[176]==1.00000 ? ALGEBRAIC[193] : 1 ? CONSTANTS[21] : 0.0/0.0);
ALGEBRAIC[199] = (ALGEBRAIC[162]==1.00000 ? ALGEBRAIC[6] : ALGEBRAIC[161]==1.00000 ? ALGEBRAIC[195] : 1 ? CONSTANTS[21] : 0.0/0.0);
ALGEBRAIC[203] = (CONSTANTS[76]==1.00000 ? ALGEBRAIC[199] : 1 ? CONSTANTS[21] : 0.0/0.0);
ALGEBRAIC[207] =  CONSTANTS[72]*ALGEBRAIC[203];
ALGEBRAIC[211] =  ALGEBRAIC[148]*ALGEBRAIC[206]+ CONSTANTS[74]*ALGEBRAIC[207]+ ALGEBRAIC[149]*ALGEBRAIC[208]+ ALGEBRAIC[150]*ALGEBRAIC[209];
ALGEBRAIC[0] = CONSTANTS[46]+STATES[5]+STATES[6];
ALGEBRAIC[5] = ALGEBRAIC[4]/133.322;
ALGEBRAIC[8] = ALGEBRAIC[7]/133.322;
ALGEBRAIC[10] = ALGEBRAIC[9]/133.322;
ALGEBRAIC[12] = ALGEBRAIC[11]/CONSTANTS[14];
ALGEBRAIC[18] = ALGEBRAIC[17]/133.322;
ALGEBRAIC[25] = ALGEBRAIC[23]/133.322;
ALGEBRAIC[30] = ALGEBRAIC[28]/133.322;
ALGEBRAIC[95] = ALGEBRAIC[33]/133.322;
ALGEBRAIC[97] =  ALGEBRAIC[34]*ALGEBRAIC[45];
ALGEBRAIC[98] =  (1.00000 - ALGEBRAIC[34])*- ALGEBRAIC[45];
ALGEBRAIC[99] =  ALGEBRAIC[35]*ALGEBRAIC[46];
ALGEBRAIC[100] =  (1.00000 - ALGEBRAIC[35])*- ALGEBRAIC[46];
ALGEBRAIC[101] = ALGEBRAIC[45]/CONSTANTS[14];
ALGEBRAIC[102] = ALGEBRAIC[46]/CONSTANTS[14];
ALGEBRAIC[105] =  ALGEBRAIC[47]*ALGEBRAIC[58];
ALGEBRAIC[106] =  (1.00000 - ALGEBRAIC[47])*- ALGEBRAIC[58];
ALGEBRAIC[107] =  ALGEBRAIC[48]*ALGEBRAIC[59];
ALGEBRAIC[108] =  (1.00000 - ALGEBRAIC[48])*- ALGEBRAIC[59];
ALGEBRAIC[109] = ALGEBRAIC[58]/CONSTANTS[14];
ALGEBRAIC[110] = ALGEBRAIC[59]/CONSTANTS[14];
ALGEBRAIC[112] =  ALGEBRAIC[60]*ALGEBRAIC[71];
ALGEBRAIC[113] =  (1.00000 - ALGEBRAIC[60])*- ALGEBRAIC[71];
ALGEBRAIC[114] =  ALGEBRAIC[61]*ALGEBRAIC[72];
ALGEBRAIC[115] =  (1.00000 - ALGEBRAIC[61])*- ALGEBRAIC[72];
ALGEBRAIC[116] = ALGEBRAIC[71]/CONSTANTS[14];
ALGEBRAIC[117] = ALGEBRAIC[72]/CONSTANTS[14];
ALGEBRAIC[119] =  ALGEBRAIC[73]*ALGEBRAIC[83];
ALGEBRAIC[120] =  (1.00000 - ALGEBRAIC[73])*- ALGEBRAIC[83];
ALGEBRAIC[121] = ALGEBRAIC[83]/CONSTANTS[14];
ALGEBRAIC[123] =  ALGEBRAIC[84]*ALGEBRAIC[94];
ALGEBRAIC[124] =  (1.00000 - ALGEBRAIC[84])*- ALGEBRAIC[94];
ALGEBRAIC[125] = ALGEBRAIC[94]/CONSTANTS[14];
ALGEBRAIC[147] = ALGEBRAIC[144]+CONSTANTS[73]+ALGEBRAIC[145]+ALGEBRAIC[146];
ALGEBRAIC[151] = ALGEBRAIC[148]+CONSTANTS[74]+ALGEBRAIC[149]+ALGEBRAIC[150];
ALGEBRAIC[158] = ALGEBRAIC[155]+CONSTANTS[76]+ALGEBRAIC[156]+ALGEBRAIC[157];
}

void objfunc_0(double *p, double *hx, int m, int n, void *adata)
{
  struct rootfind_info* rfi = (struct rootfind_info*)adata;
#define VOI rfi->aVOI
#define CONSTANTS rfi->aCONSTANTS
#define RATES rfi->aRATES
#define STATES rfi->aSTATES
#define ALGEBRAIC rfi->aALGEBRAIC
#define pret rfi->aPRET
  ALGEBRAIC[34] = p[0];
  ALGEBRAIC[35] = p[1];
  ALGEBRAIC[36] = p[2];
  ALGEBRAIC[37] = p[3];
  ALGEBRAIC[38] = p[4];
  ALGEBRAIC[39] = p[5];
  ALGEBRAIC[40] = p[6];
  ALGEBRAIC[41] = p[7];
  ALGEBRAIC[42] = p[8];
  ALGEBRAIC[43] = p[9];
  ALGEBRAIC[44] = p[10];
  ALGEBRAIC[45] = p[11];
  ALGEBRAIC[46] = p[12];
  ALGEBRAIC[47] = p[13];
  ALGEBRAIC[48] = p[14];
  ALGEBRAIC[49] = p[15];
  ALGEBRAIC[50] = p[16];
  ALGEBRAIC[51] = p[17];
  ALGEBRAIC[52] = p[18];
  ALGEBRAIC[53] = p[19];
  ALGEBRAIC[54] = p[20];
  ALGEBRAIC[55] = p[21];
  ALGEBRAIC[56] = p[22];
  ALGEBRAIC[57] = p[23];
  ALGEBRAIC[58] = p[24];
  ALGEBRAIC[59] = p[25];
  ALGEBRAIC[60] = p[26];
  ALGEBRAIC[61] = p[27];
  ALGEBRAIC[62] = p[28];
  ALGEBRAIC[63] = p[29];
  ALGEBRAIC[64] = p[30];
  ALGEBRAIC[65] = p[31];
  ALGEBRAIC[66] = p[32];
  ALGEBRAIC[67] = p[33];
  ALGEBRAIC[68] = p[34];
  ALGEBRAIC[69] = p[35];
  ALGEBRAIC[70] = p[36];
  ALGEBRAIC[71] = p[37];
  ALGEBRAIC[72] = p[38];
  ALGEBRAIC[73] = p[39];
  ALGEBRAIC[74] = p[40];
  ALGEBRAIC[75] = p[41];
  ALGEBRAIC[76] = p[42];
  ALGEBRAIC[77] = p[43];
  ALGEBRAIC[78] = p[44];
  ALGEBRAIC[79] = p[45];
  ALGEBRAIC[80] = p[46];
  ALGEBRAIC[81] = p[47];
  ALGEBRAIC[82] = p[48];
  ALGEBRAIC[83] = p[49];
  ALGEBRAIC[84] = p[50];
  ALGEBRAIC[85] = p[51];
  ALGEBRAIC[86] = p[52];
  ALGEBRAIC[87] = p[53];
  ALGEBRAIC[88] = p[54];
  ALGEBRAIC[89] = p[55];
  ALGEBRAIC[90] = p[56];
  ALGEBRAIC[91] = p[57];
  ALGEBRAIC[92] = p[58];
  ALGEBRAIC[93] = p[59];
  ALGEBRAIC[94] = p[60];
  hx[0] = ALGEBRAIC[34] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[45]/CONSTANTS[13]));
  hx[1] = ALGEBRAIC[35] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[46]/CONSTANTS[13]));
  hx[2] = ALGEBRAIC[36] - ( (1.00000 - ALGEBRAIC[35])*STATES[2]+ ALGEBRAIC[35]*ALGEBRAIC[1]);
  hx[3] = ALGEBRAIC[37] - ( ALGEBRAIC[35]*STATES[2]+ (1.00000 - ALGEBRAIC[35])*ALGEBRAIC[2]);
  hx[4] = ALGEBRAIC[38] - ( ALGEBRAIC[45]*ALGEBRAIC[40] -  ALGEBRAIC[46]*ALGEBRAIC[41])/(ALGEBRAIC[45]+ALGEBRAIC[46]);
  hx[5] = ALGEBRAIC[39] - ALGEBRAIC[38]/ALGEBRAIC[3];
  hx[6] = ALGEBRAIC[40] - ( ALGEBRAIC[34]*ALGEBRAIC[1]+ (1.00000 - ALGEBRAIC[34])*ALGEBRAIC[36]);
  hx[7] = ALGEBRAIC[41] - ( ALGEBRAIC[35]*ALGEBRAIC[37]+ (1.00000 - ALGEBRAIC[35])*ALGEBRAIC[2]);
  hx[8] = ALGEBRAIC[42] -  ALGEBRAIC[43]*CONSTANTS[9];
  hx[9] = ALGEBRAIC[43] - (1.00000+ (( (CONSTANTS[58] - 1.00000)*(pow(1.00000 - ALGEBRAIC[39], CONSTANTS[48]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[48]) - 1.00000))*pow(( 2.00000*CONSTANTS[8]*1.00000e+06)/( 2.00000*CONSTANTS[8]*1.00000e+06 - 1.10000), 2.00000));
  hx[10] = ALGEBRAIC[44] - ( 8.00000*ALGEBRAIC[42]*CONSTANTS[38])/(  3.14159265358979*pow(CONSTANTS[8], 4.00000));
  hx[11] = ALGEBRAIC[45] - (CONSTANTS[10] - ALGEBRAIC[4])/(ALGEBRAIC[44]/2.00000);
  hx[12] = ALGEBRAIC[46] - (ALGEBRAIC[4] - ALGEBRAIC[7])/(ALGEBRAIC[44]/2.00000);
  hx[13] = ALGEBRAIC[47] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[58]/CONSTANTS[13]));
  hx[14] = ALGEBRAIC[48] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[59]/CONSTANTS[13]));
  hx[15] = ALGEBRAIC[49] - ( (1.00000 - ALGEBRAIC[48])*STATES[9]+ ALGEBRAIC[48]*ALGEBRAIC[14]);
  hx[16] = ALGEBRAIC[50] - ( ALGEBRAIC[48]*STATES[9]+ (1.00000 - ALGEBRAIC[48])*ALGEBRAIC[15]);
  hx[17] = ALGEBRAIC[51] - ( ALGEBRAIC[58]*ALGEBRAIC[53] -  ALGEBRAIC[59]*ALGEBRAIC[54])/(ALGEBRAIC[58]+ALGEBRAIC[59]);
  hx[18] = ALGEBRAIC[52] - ALGEBRAIC[51]/ALGEBRAIC[16];
  hx[19] = ALGEBRAIC[53] - ( ALGEBRAIC[47]*ALGEBRAIC[14]+ (1.00000 - ALGEBRAIC[47])*ALGEBRAIC[49]);
  hx[20] = ALGEBRAIC[54] - ( ALGEBRAIC[48]*ALGEBRAIC[50]+ (1.00000 - ALGEBRAIC[48])*ALGEBRAIC[15]);
  hx[21] = ALGEBRAIC[55] -  ALGEBRAIC[56]*CONSTANTS[9];
  hx[22] = ALGEBRAIC[56] - (1.00000+ (( (CONSTANTS[78] - 1.00000)*(pow(1.00000 - ALGEBRAIC[52], CONSTANTS[77]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[77]) - 1.00000))*pow(( 2.00000*CONSTANTS[29]*1.00000e+06)/( 2.00000*CONSTANTS[29]*1.00000e+06 - 1.10000), 2.00000));
  hx[23] = ALGEBRAIC[57] - (( 8.00000*ALGEBRAIC[55]*CONSTANTS[40])/(  3.14159265358979*pow(CONSTANTS[29], 4.00000))+ALGEBRAIC[13]);
  hx[24] = ALGEBRAIC[58] - (ALGEBRAIC[9] - ALGEBRAIC[17])/(ALGEBRAIC[57]/2.00000);
  hx[25] = ALGEBRAIC[59] - (ALGEBRAIC[17] - ALGEBRAIC[28])/(ALGEBRAIC[57]/2.00000);
  hx[26] = ALGEBRAIC[60] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[71]/CONSTANTS[13]));
  hx[27] = ALGEBRAIC[61] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[72]/CONSTANTS[13]));
  hx[28] = ALGEBRAIC[62] - ( (1.00000 - ALGEBRAIC[61])*STATES[13]+ ALGEBRAIC[61]*ALGEBRAIC[20]);
  hx[29] = ALGEBRAIC[63] - ( ALGEBRAIC[61]*STATES[13]+ (1.00000 - ALGEBRAIC[61])*ALGEBRAIC[21]);
  hx[30] = ALGEBRAIC[64] - ( ALGEBRAIC[71]*ALGEBRAIC[66] -  ALGEBRAIC[72]*ALGEBRAIC[67])/(ALGEBRAIC[71]+ALGEBRAIC[72]);
  hx[31] = ALGEBRAIC[65] - ALGEBRAIC[64]/ALGEBRAIC[22];
  hx[32] = ALGEBRAIC[66] - ( ALGEBRAIC[60]*ALGEBRAIC[20]+ (1.00000 - ALGEBRAIC[60])*ALGEBRAIC[62]);
  hx[33] = ALGEBRAIC[67] - ( ALGEBRAIC[61]*ALGEBRAIC[63]+ (1.00000 - ALGEBRAIC[61])*ALGEBRAIC[21]);
  hx[34] = ALGEBRAIC[68] -  ALGEBRAIC[69]*CONSTANTS[9];
  hx[35] = ALGEBRAIC[69] - (1.00000+ (( (CONSTANTS[80] - 1.00000)*(pow(1.00000 - ALGEBRAIC[65], CONSTANTS[79]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[79]) - 1.00000))*pow(( 2.00000*CONSTANTS[31]*1.00000e+06)/( 2.00000*CONSTANTS[31]*1.00000e+06 - 1.10000), 2.00000));
  hx[36] = ALGEBRAIC[70] - (( 8.00000*ALGEBRAIC[68]*CONSTANTS[41])/(  3.14159265358979*pow(CONSTANTS[31], 4.00000))+ALGEBRAIC[19]);
  hx[37] = ALGEBRAIC[71] - (ALGEBRAIC[9] - ALGEBRAIC[23])/(ALGEBRAIC[70]/2.00000);
  hx[38] = ALGEBRAIC[72] - (ALGEBRAIC[23] - ALGEBRAIC[33])/(ALGEBRAIC[70]/2.00000);
  hx[39] = ALGEBRAIC[73] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[83]/CONSTANTS[13]));
  hx[40] = ALGEBRAIC[74] - ( (1.00000 - ALGEBRAIC[73])*STATES[17]+ ALGEBRAIC[73]*ALGEBRAIC[24]);
  hx[41] = ALGEBRAIC[75] - ( ALGEBRAIC[73]*STATES[17]+ (1.00000 - ALGEBRAIC[73])*ALGEBRAIC[26]);
  hx[42] = ALGEBRAIC[76] - ( ALGEBRAIC[59]*ALGEBRAIC[78] -  ALGEBRAIC[83]*ALGEBRAIC[79])/(ALGEBRAIC[59]+ALGEBRAIC[83]);
  hx[43] = ALGEBRAIC[77] - ALGEBRAIC[76]/ALGEBRAIC[27];
  hx[44] = ALGEBRAIC[78] - ( ALGEBRAIC[73]*ALGEBRAIC[24]+ (1.00000 - ALGEBRAIC[73])*ALGEBRAIC[74]);
  hx[45] = ALGEBRAIC[79] - ( ALGEBRAIC[73]*ALGEBRAIC[75]+ (1.00000 - ALGEBRAIC[73])*ALGEBRAIC[26]);
  hx[46] = ALGEBRAIC[80] -  ALGEBRAIC[81]*CONSTANTS[9];
  hx[47] = ALGEBRAIC[81] - (1.00000+ (( (CONSTANTS[82] - 1.00000)*(pow(1.00000 - ALGEBRAIC[77], CONSTANTS[81]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[81]) - 1.00000))*pow(( 2.00000*CONSTANTS[33]*1.00000e+06)/( 2.00000*CONSTANTS[33]*1.00000e+06 - 1.10000), 2.00000));
  hx[48] = ALGEBRAIC[82] - ( 8.00000*ALGEBRAIC[80]*CONSTANTS[42])/(  3.14159265358979*pow(CONSTANTS[33], 4.00000));
  hx[49] = ALGEBRAIC[83] - (ALGEBRAIC[28] - CONSTANTS[34])/ALGEBRAIC[82];
  hx[50] = ALGEBRAIC[84] - (0.500000+ (1.00000/ 3.14159265358979)*atan(ALGEBRAIC[94]/CONSTANTS[13]));
  hx[51] = ALGEBRAIC[85] - ( (1.00000 - ALGEBRAIC[84])*STATES[21]+ ALGEBRAIC[84]*ALGEBRAIC[29]);
  hx[52] = ALGEBRAIC[86] - ( ALGEBRAIC[84]*STATES[21]+ (1.00000 - ALGEBRAIC[84])*ALGEBRAIC[31]);
  hx[53] = ALGEBRAIC[87] - ( ALGEBRAIC[72]*ALGEBRAIC[89] -  ALGEBRAIC[94]*ALGEBRAIC[90])/(ALGEBRAIC[72]+ALGEBRAIC[94]);
  hx[54] = ALGEBRAIC[88] - ALGEBRAIC[87]/ALGEBRAIC[32];
  hx[55] = ALGEBRAIC[89] - ( ALGEBRAIC[84]*ALGEBRAIC[29]+ (1.00000 - ALGEBRAIC[84])*ALGEBRAIC[85]);
  hx[56] = ALGEBRAIC[90] - ( ALGEBRAIC[84]*ALGEBRAIC[86]+ (1.00000 - ALGEBRAIC[84])*ALGEBRAIC[31]);
  hx[57] = ALGEBRAIC[91] -  ALGEBRAIC[92]*CONSTANTS[9];
  hx[58] = ALGEBRAIC[92] - (1.00000+ (( (CONSTANTS[84] - 1.00000)*(pow(1.00000 - ALGEBRAIC[88], CONSTANTS[83]) - 1.00000))/(pow(1.00000 - CONSTANTS[0], CONSTANTS[83]) - 1.00000))*pow(( 2.00000*CONSTANTS[36]*1.00000e+06)/( 2.00000*CONSTANTS[36]*1.00000e+06 - 1.10000), 2.00000));
  hx[59] = ALGEBRAIC[93] - ( 8.00000*ALGEBRAIC[91]*CONSTANTS[43])/(  3.14159265358979*pow(CONSTANTS[36], 4.00000));
  hx[60] = ALGEBRAIC[94] - (ALGEBRAIC[33] - CONSTANTS[37])/ALGEBRAIC[93];
#undef VOI
#undef CONSTANTS
#undef RATES
#undef STATES
#undef ALGEBRAIC
#undef pret
}
void rootfind_0(double VOI, double* CONSTANTS, double* RATES,
double* STATES, double* ALGEBRAIC, int* pret)
{
  static double p[61] = {0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1};
  double bp[61], work[LM_DIF_WORKSZ(61, 61)];
  struct rootfind_info rfi;
  rfi.aVOI = VOI;
  rfi.aCONSTANTS = CONSTANTS;
  rfi.aRATES = RATES;
  rfi.aSTATES = STATES;
  rfi.aALGEBRAIC = ALGEBRAIC;
  rfi.aPRET = pret;
  do_levmar(objfunc_0, p, bp, work, pret, 61, &rfi);
  ALGEBRAIC[34] = p[0];
  ALGEBRAIC[35] = p[1];
  ALGEBRAIC[36] = p[2];
  ALGEBRAIC[37] = p[3];
  ALGEBRAIC[38] = p[4];
  ALGEBRAIC[39] = p[5];
  ALGEBRAIC[40] = p[6];
  ALGEBRAIC[41] = p[7];
  ALGEBRAIC[42] = p[8];
  ALGEBRAIC[43] = p[9];
  ALGEBRAIC[44] = p[10];
  ALGEBRAIC[45] = p[11];
  ALGEBRAIC[46] = p[12];
  ALGEBRAIC[47] = p[13];
  ALGEBRAIC[48] = p[14];
  ALGEBRAIC[49] = p[15];
  ALGEBRAIC[50] = p[16];
  ALGEBRAIC[51] = p[17];
  ALGEBRAIC[52] = p[18];
  ALGEBRAIC[53] = p[19];
  ALGEBRAIC[54] = p[20];
  ALGEBRAIC[55] = p[21];
  ALGEBRAIC[56] = p[22];
  ALGEBRAIC[57] = p[23];
  ALGEBRAIC[58] = p[24];
  ALGEBRAIC[59] = p[25];
  ALGEBRAIC[60] = p[26];
  ALGEBRAIC[61] = p[27];
  ALGEBRAIC[62] = p[28];
  ALGEBRAIC[63] = p[29];
  ALGEBRAIC[64] = p[30];
  ALGEBRAIC[65] = p[31];
  ALGEBRAIC[66] = p[32];
  ALGEBRAIC[67] = p[33];
  ALGEBRAIC[68] = p[34];
  ALGEBRAIC[69] = p[35];
  ALGEBRAIC[70] = p[36];
  ALGEBRAIC[71] = p[37];
  ALGEBRAIC[72] = p[38];
  ALGEBRAIC[73] = p[39];
  ALGEBRAIC[74] = p[40];
  ALGEBRAIC[75] = p[41];
  ALGEBRAIC[76] = p[42];
  ALGEBRAIC[77] = p[43];
  ALGEBRAIC[78] = p[44];
  ALGEBRAIC[79] = p[45];
  ALGEBRAIC[80] = p[46];
  ALGEBRAIC[81] = p[47];
  ALGEBRAIC[82] = p[48];
  ALGEBRAIC[83] = p[49];
  ALGEBRAIC[84] = p[50];
  ALGEBRAIC[85] = p[51];
  ALGEBRAIC[86] = p[52];
  ALGEBRAIC[87] = p[53];
  ALGEBRAIC[88] = p[54];
  ALGEBRAIC[89] = p[55];
  ALGEBRAIC[90] = p[56];
  ALGEBRAIC[91] = p[57];
  ALGEBRAIC[92] = p[58];
  ALGEBRAIC[93] = p[59];
  ALGEBRAIC[94] = p[60];
}
