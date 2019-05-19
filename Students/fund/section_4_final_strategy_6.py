# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/18 14:59 AM
@Author  : ddlee
@File    : section_4_final_strategy_6.py
"""

import os
import time

from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir
from Students.fund.section_1_multi_factor_6 import get_intensity
from Students.fund.section_2_hedging_ratio_0 import get_hands_num
from Students.fund.section_3_profit_loss_6 import get_positive_profit
import pandas as pd

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def prepare_data(in_file, sheet_names):
    raw_rows = []
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        _date = datetime(*xldate_as_tuple(_date, 0))
        _date = _date.strftime('%Y-%m-%d %H:%M:%S')
        row = [_date, B, C, D, E, F, G, H, I, J, K]
        raw_rows.append(row)
    return raw_rows


def process(in_file, sheet_names):
    raw_rows = prepare_data(in_file, sheet_names)
    raw_df = pd.DataFrame(raw_rows, columns=["_date", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

    # 调用逻辑1获取
    L_list, M_list = get_intensity(in_file, sheet_names)

    # 调用逻辑2获取，如需使用，将下面两行反注释，并注释下面的第三行
    # hands_num = get_hands_num(in_file, sheet_names)
    # N_list, O_list = [hands_num] * len(L_list), [hands_num] * len(L_list)
    N_list, O_list = [1] * len(L_list), [1] * len(L_list)

    # 调用逻辑3获取，
    P_list, AA_list = get_positive_profit(in_file, sheet_names)

    right = pd.DataFrame({'L': pd.Series(L_list), 'M': pd.Series(M_list),
                          'N': pd.Series(N_list), 'O': pd.Series(O_list),
                          'P': pd.Series(P_list), 'AA': pd.Series(AA_list)})
    df = raw_df.join(right)

    _, Q_list, R_list, S_list, T_list, U_list, V_list, W_list, X_list, Y_list, Z_list, \
    _, AB_list, AC_list, AD_list, AE_list, AF_list, AG_list, AH_list, AI_list, AJ_list, AK_list \
        = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

    for i in range(len(L_list)):
        if i < 3:
            _, Q, R, S, T, U, V, W, X, Y, Z, _, AB, AC, AD, AE, AF, AG, AH, AI, AJ, AK \
                = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

            Q_list.append(Q)
            R_list.append(R)
            S_list.append(S)
            T_list.append(T)
            U_list.append(U)
            V_list.append(V)
            W_list.append(W)
            X_list.append(X)
            Y_list.append(Y)
            Z_list.append(Z)

            AB_list.append(AB)
            AC_list.append(AC)
            AD_list.append(AD)
            AE_list.append(AE)
            AF_list.append(AF)
            AG_list.append(AG)
            AH_list.append(AH)
            AI_list.append(AI)
            AJ_list.append(AJ)
            AK_list.append(AK)
        else:
            Q = df['L'][i] * ((df['C'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['H'][i] - df['G'][i]) * 300 * df['O'][i])
            R = -20000 if Q < -20000 else Q
            S = df['L'][i] * ((df['E'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['J'][i] - df['G'][i]) * 300 * df['O'][i])
            T = -20000 if S < -20000 else S
            U = df['L'][i] * ((df['F'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['K'][i] - df['G'][i]) * 300 * df['O'][i])
            V = -20000 if U < -20000 else U
            W = -20000 - df['P'][i] if ((T == -20000 or V == -20000) and R != -20000) else 0
            X = -20000 - Q if ((T == -20000 or V == -20000) and R != -20000) else 0
            Y = -20000 if X < -20000 else W
            Z = Y - 20000 if ((T == -20000 or V == -20000) and R != -20000) else df['P'][i]

            AB = df['M'][i] * ((df['C'][i] - df['B'][i]) * 200 * df['N'][i] -
                               (df['H'][i] - df['G'][i]) * 300 * df['O'][i])
            AC = -20000 if AB < -20000 else AB
            AD = df['M'][i] * ((df['E'][i] - df['B'][i]) * 200 * df['N'][i] -
                               (df['J'][i] - df['G'][i]) * 300 * df['O'][i])
            AE = -20000 if AD < -20000 else AD
            AF = df['M'][i] * ((df['F'][i] - df['B'][i]) * 200 * df['N'][i] -
                               (df['K'][i] - df['G'][i]) * 300 * df['O'][i])
            AG = -20000 if AF < -20000 else AF
            AH = -20000 - df['AA'][i] if ((AE == -20000 or AG == -20000) and AC != -20000) else 0
            AI = -20000 - AB if ((AE == -20000 or AG == -20000) and AC != -20000) else 0
            AJ = -20000 if AI < -20000 else AH
            AK = AJ - 20000 if ((AE == -20000 or AG == -20000) and AC != -20000) else df['AA'][i]
            """
            P -> 3的V列
            Q = L3*((C3-B3)*200*N3-(H3-G3)*300*O3)
            R=IF(Q3<-20000,-20000,Q3)
            S=((E3-B3)*200*N3-(J3-G3)*300*O3)*L3
            T=IF(S3<-20000,-20000,S3)
            U=((F3-B3)*200*N3-(K3-G3)*300*O3)*L3
            V=IF(U3<-20000,-20000,U3)
            W=IF(AND(OR(T3=-20000,V3=-20000),R3<>-20000),-20000-P3,0)
            X=IF(AND(OR(T3=-20000,V3=-20000),R3<>-20000),-20000-Q3,0)
            Y=IF(X3<-20000,-20000,W3)
            Z=IF(AND(OR(T3=-20000,V3=-20000),R3<>-20000),Y3+-20000,P3)

            AA -> 3的AC列
            AB=M3*((C3-B3)*200*N3-(H3-G3)*300*O3)
            AC=IF(AB3<-20000,-20000,AB3)
            AD=((E3-B3)*200*N3-(J3-G3)*300*O3)*M3
            AE=IF(AD3<-20000,-20000,AD3)
            AF=((F3-B3)*200*N3-(K3-G3)*300*O3)*M3
            AG=IF(AF3<-20000,-20000,AF3)
            AH=IF(AND(OR(AE3=-20000,AG3=-20000),AC3<>-20000),-20000-AA3,0)
            AI=IF(AND(OR(AE3=-20000,AG3=-20000),AC3<>-20000),-20000-AB3,0)
            AJ=IF(AI3<-20000,-20000,AH3)
            AK=IF(AND(OR(AE3=-20000,AG3=-20000),AC3<>-20000),AJ3+-20000,AA3)
            """

            Q_list.append(Q)
            R_list.append(R)
            S_list.append(S)
            T_list.append(T)
            U_list.append(U)
            V_list.append(V)
            W_list.append(W)
            X_list.append(X)
            Y_list.append(Y)
            Z_list.append(Z)

            AB_list.append(AB)
            AC_list.append(AC)
            AD_list.append(AD)
            AE_list.append(AE)
            AF_list.append(AF)
            AG_list.append(AG)
            AH_list.append(AH)
            AI_list.append(AI)
            AJ_list.append(AJ)
            AK_list.append(AK)

    right = pd.DataFrame({'Q': pd.Series(Q_list), 'R': pd.Series(R_list),
                          'S': pd.Series(S_list), 'T': pd.Series(T_list),
                          'U': pd.Series(U_list), 'V': pd.Series(V_list),
                          'W': pd.Series(W_list), 'X': pd.Series(X_list),
                          'Y': pd.Series(Y_list), 'Z': pd.Series(Z_list),
                          'AB': pd.Series(AB_list), 'AC': pd.Series(AC_list),
                          'AD': pd.Series(AD_list), 'AE': pd.Series(AE_list),
                          'AF': pd.Series(AF_list), 'AG': pd.Series(AG_list),
                          'AH': pd.Series(AH_list), 'AI': pd.Series(AI_list),
                          'AJ': pd.Series(AJ_list), 'AK': pd.Series(AK_list)})

    all_generate_df = pd.DataFrame({'L': pd.Series(L_list), 'M': pd.Series(M_list),
                                    'N': pd.Series(N_list), 'O': pd.Series(O_list),
                                    'P': pd.Series(P_list),
                                    'Q': pd.Series(Q_list), 'R': pd.Series(R_list),
                                    'S': pd.Series(S_list), 'T': pd.Series(T_list),
                                    'U': pd.Series(U_list), 'V': pd.Series(V_list),
                                    'W': pd.Series(W_list), 'X': pd.Series(X_list),
                                    'Y': pd.Series(Y_list), 'Z': pd.Series(Z_list),
                                    'AA': pd.Series(AA_list),
                                    'AB': pd.Series(AB_list), 'AC': pd.Series(AC_list),
                                    'AD': pd.Series(AD_list), 'AE': pd.Series(AE_list),
                                    'AF': pd.Series(AF_list), 'AG': pd.Series(AG_list),
                                    'AH': pd.Series(AH_list), 'AI': pd.Series(AI_list),
                                    'AJ': pd.Series(AJ_list), 'AK': pd.Series(AK_list)})
    df = raw_df.join(all_generate_df)

    df.columns = ["日期", "IC开盘价(元)", "IC收盘价(元)", "IC结算价", "IC最高价(元)", "IC最低价(元)",
                  "IH开盘价(元)", "IH收盘价(元)", "IH结算价", "IH最高价(元)", "IH最低价(元)",
                  "正向", "反转", "IC手数（默认为1）", "IH手数（默认为1）",
                  "正向盈亏（第二天开盘价），考虑盘中止损重开仓", "正向盈亏（当天收盘价）", "止损正向盈亏（当天收盘价）",
                  "正向当天最高价回撤", "正向当天最高价回撤止损", "正向当天最低价回撤", "正向当天最低价回撤止损",
                  "正向，最高价、最低价，当日盈亏", "", "正向，最高价、最低价止损后，当日盈亏",
                  "正向，排除盘中止损，但实际未止损情况的，当天盈亏", "反向盈亏（第二天开盘价），考虑盘中止损重开仓",
                  "反向，收盘当日盈利", "反向，收盘当日盈利可以止损", "反向当天最高价回撤", "反向当天最高价回撤止损",
                  "反向当天最低价回撤", "反向当天最低价回撤止损", "反向，最高价、最低价，当日盈亏", "",
                  "反向，最高价、最低价止损后，当日盈亏", "反向，排除盘中止损，但实际未止损情况的，当天盈亏"]
    to_file = in_file.strip(".xlsx") + datesuffix + ".xlsx"
    df.to_excel(to_file, index=False, sheet_name="当天收盘与前三天开盘")

    print("Save path:", to_file)
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑4：盘中已止损，但实际未止损.xlsx")
    sheet_names = ["当天收盘与前三天开盘"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
