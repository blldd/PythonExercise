# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/28 20:28 AM
@Author  : ddlee
@File    : section_3_profit_loss_2.py
"""
import os
import time

from tqdm import tqdm

from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir
from Students.fund.section_1_multi_factor_2 import get_intensity
from Students.fund.section_2_hedging_ratio_0 import get_hands_num
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
    df = pd.DataFrame(raw_rows, columns=["_date", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

    L_list, M_list = get_intensity(in_file, sheet_names)

    # hands_num = get_hands_num(in_file, sheet_names)
    # N_list, O_list = [hands_num] * len(L_list), [hands_num] * len(L_list)
    N_list, O_list = [1] * len(L_list), [1] * len(L_list)

    right = pd.DataFrame({'L': pd.Series(L_list), 'M': pd.Series(M_list),
                          'N': pd.Series(N_list), 'O': pd.Series(O_list)})
    df = df.join(right)

    P_list, Q_list, R_list, S_list, T_list, U_list, V_list, W_list, X_list, Y_list, Z_list, \
    AA_list, AB_list, AC_list = [], [], [], [], [], [], [], [], [], [], [], [], [], []

    for i in tqdm(range(len(raw_rows) - 1)):
        if i == 0:
            P, Q, R, S, T, U, V, W, X, Y, Z, AA, AB, AC = "", "", "", "", "", "", "", "", "", "", "", "", "", ""
            P_list.append(P)
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
            AA_list.append(AA)
            AB_list.append(AB)
            AC_list.append(AC)
        else:
            P = df['L'][i] * ((df['B'][i + 1] - df['B'][i]) * 200 * df['N'][i] -
                              (df['G'][i + 1] - df['G'][i]) * 300 * df['O'][i])
            Q = df['L'][i] * ((df['C'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['H'][i] - df['G'][i]) * 300 * df['O'][i])
            R = -20000 if Q < -20000 else Q
            S = R - P if R == -20000 else 0
            T = R - Q if R == -20000 else 0
            U = -20000 if T < -20000 else S
            V = -20000 + U if R == -20000 else P
            W = df['M'][i] * ((df['B'][i + 1] - df['B'][i]) * 200 * df['N'][i] -
                              (df['G'][i + 1] - df['G'][i]) * 300 * df['O'][i])
            X = df['M'][i] * ((df['C'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['H'][i] - df['G'][i]) * 300 * df['O'][i])
            Y = -20000 if X < -20000 else X
            Z = Y - W if Y == -20000 else 0
            AA = Y - X if Y == -20000 else 0
            AB = -20000 if AA < -20000 else Z
            AC = -20000 + AB if Y == -20000 else W

            P_list.append(P)
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
            AA_list.append(AA)
            AB_list.append(AB)
            AC_list.append(AC)

            """
            S=IF(R3=-20000, R3 - P3, 0)
            T=IF(R3=-20000,R3-Q3,0)
            U=IF(T3<-20000,-20000,S3)
            V=IF(R3=-20000,-20000+U3,P3)
            W=M3*((B4-B3)*200*N3-(G4-G3)*300*O3)
            X=M3*((C3-B3)*200*N3-(H3-G3)*300*O3)
            Y=IF(X3<-20000,-20000,X3)
            Z=IF(Y3=-20000,Y3-W3,0)
            AA=IF(Y3=-20000,Y3-X3,0)
            AB=IF(AA3<-20000,-20000,Z3)
            AC=IF(Y3=-20000,-20000+AB3,W3)
            """
    right = pd.DataFrame({'P': pd.Series(P_list), 'Q': pd.Series(Q_list),
                          'R': pd.Series(R_list), 'S': pd.Series(S_list),
                          'T': pd.Series(T_list), 'U': pd.Series(U_list),
                          'V': pd.Series(V_list), 'W': pd.Series(W_list),
                          'X': pd.Series(X_list), 'Y': pd.Series(Y_list),
                          'Z': pd.Series(Z_list), 'AA': pd.Series(AA_list),
                          'AB': pd.Series(AB_list), 'AC': pd.Series(AC_list)})
    df = df.join(right)
    df.columns = ["日期", "IC开盘价(元)", "IC收盘价(元)",
                  "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                  "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                  "正向", "反转", "IC手数（默认为1）", "IH手数（默认为1）",
                  "正向盈亏(第二天开盘价）", "正向盈亏（当天收盘价）", "止损正向盈亏（当天收盘价）",
                  "正向重开仓盈亏", "", "正向重开仓止损盈亏", "正向盈亏（第二天开盘价），考虑盘中止损重开仓",
                  "反向盈亏(第二天开盘价）", "反向盈亏（当天收盘价）",
                  "止损反向盈亏（当天收盘价）", "反向重开仓盈亏", "", "反向重开仓止损盈亏",
                  "反向盈亏（第二天开盘价），考虑盘中止损重开仓"]
    to_file = in_file.strip(".xlsx") + "_" + sheet_names[0] + "_" + datesuffix + ".xlsx"
    df.to_excel(to_file, index=False, sheet_name=sheet_names[0])

    print("Save path:", to_file)
    print("Done!")


def get_positive_profit(in_file, sheet_names):
    raw_rows = prepare_data(in_file, sheet_names)
    df = pd.DataFrame(raw_rows, columns=["_date", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

    L_list, M_list = get_intensity(in_file, sheet_names)

    # hands_num = get_hands_num(in_file, sheet_names)
    # N_list, O_list = [hands_num] * len(L_list), [hands_num] * len(L_list)
    N_list, O_list = [1] * len(L_list), [1] * len(L_list)

    right = pd.DataFrame({'L': pd.Series(L_list), 'M': pd.Series(M_list),
                          'N': pd.Series(N_list), 'O': pd.Series(O_list)})
    df = df.join(right)

    P_list, Q_list, R_list, S_list, T_list, U_list, V_list, W_list, X_list, Y_list, Z_list, \
    AA_list, AB_list, AC_list = [], [], [], [], [], [], [], [], [], [], [], [], [], []

    for i in tqdm(range(len(raw_rows) - 1)):
        if i == 0:
            P, Q, R, S, T, U, V, W, X, Y, Z, AA, AB, AC = "", "", "", "", "", "", "", "", "", "", "", "", "", ""
            P_list.append(P)
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
            AA_list.append(AA)
            AB_list.append(AB)
            AC_list.append(AC)
        else:
            P = df['L'][i] * ((df['B'][i + 1] - df['B'][i]) * 200 * df['N'][i] -
                              (df['G'][i + 1] - df['G'][i]) * 300 * df['O'][i])
            Q = df['L'][i] * ((df['C'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['H'][i] - df['G'][i]) * 300 * df['O'][i])
            R = -20000 if Q < -20000 else Q
            S = R - P if R == -20000 else 0
            T = R - Q if R == -20000 else 0
            U = -20000 if T < -20000 else S
            V = -20000 + U if R == -20000 else P
            W = df['M'][i] * ((df['B'][i + 1] - df['B'][i]) * 200 * df['N'][i] -
                              (df['G'][i + 1] - df['G'][i]) * 300 * df['O'][i])
            X = df['M'][i] * ((df['C'][i] - df['B'][i]) * 200 * df['N'][i] -
                              (df['H'][i] - df['G'][i]) * 300 * df['O'][i])
            Y = -20000 if X < -20000 else X
            Z = Y - W if Y == -20000 else 0
            AA = Y - X if Y == -20000 else 0
            AB = -20000 if AA < -20000 else Z
            AC = -20000 + AB if Y == -20000 else W

            P_list.append(P)
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
            AA_list.append(AA)
            AB_list.append(AB)
            AC_list.append(AC)

    return V_list, AC_list


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑3：因子的当日盈亏.xlsx")
    sheet_names = ["当天开盘与下日开盘"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
    # print(get_positive_profit(in_file, sheet_names))
