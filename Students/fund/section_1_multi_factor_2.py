# -*- coding:UTF-8 -*-
import os
import time

from tqdm import tqdm

from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir
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

    L_list, M_list, N_list, O_list, P_list, Q_list = [], [], [], [], [], []

    cnt = 0
    last = [0, 0, 0, 0]
    for i in tqdm(range(len(raw_rows) - 1)):
        cnt += 1
        L = (raw_df['B'][i + 1] - raw_df['B'][i]) / raw_df['B'][i]
        M = (raw_df['G'][i + 1] - raw_df['G'][i]) / raw_df['G'][i]
        N = (raw_df['B'][i] - raw_df['B'][i + 1]) / raw_df['B'][i + 1]
        O = (raw_df['G'][i] - raw_df['G'][i + 1]) / raw_df['G'][i + 1]
        if cnt == 1:
            P, Q = "", ""
        else:
            P = 1 if last[0] > last[1] else -1
            Q = 1 if last[2] > last[3] else -1
        last = [L, M, N, O]

        L_list.append(L)
        M_list.append(M)
        N_list.append(N)
        O_list.append(O)
        P_list.append(P)
        Q_list.append(Q)
        """
        L2=(B3-B2)/B2
        M2=(G3-G2)/G2
        N2=(B2-B3)/B3
        O2=(G2-G3)/G3
        
        P3=IF(L2>M2,1,-1)
        Q3=IF(N2>O2,1,-1)
        """

    all_generate_df = pd.DataFrame({'L': pd.Series(L_list), 'M': pd.Series(M_list),
                                    'N': pd.Series(N_list), 'O': pd.Series(O_list),
                                    'P': pd.Series(P_list), 'Q': pd.Series(Q_list)})
    df = raw_df.join(all_generate_df)
    df.columns = ["日期", "IC开盘价(元)", "IC收盘价(元)",
                  "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                  "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                  "IC(下日开盘-开盘）/开盘", "IH(下日开盘-开盘）/开盘",
                  "IC（开盘-下日开盘）/下日开盘", "IH（开盘-下日开盘）/下日开盘",
                  "LM相比", "NO相比"]
    to_file = in_file.strip(".xlsx") + "_" + sheet_names[0] + "_" + datesuffix + ".xlsx"
    df.to_excel(to_file, index=False, sheet_name=sheet_names[0])

    print("Save path:", to_file)
    print("Done!")


def get_intensity(in_file, sheet_names):
    raw_rows = prepare_data(in_file, sheet_names)
    raw_df = pd.DataFrame(raw_rows, columns=["_date", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

    L_list, M_list, N_list, O_list, P_list, Q_list = [], [], [], [], [], []

    cnt = 0
    last = [0, 0, 0, 0]
    for i in tqdm(range(len(raw_rows) - 1)):
        cnt += 1
        L = (raw_df['B'][i + 1] - raw_df['B'][i]) / raw_df['B'][i]
        M = (raw_df['G'][i + 1] - raw_df['G'][i]) / raw_df['G'][i]
        N = (raw_df['B'][i] - raw_df['B'][i + 1]) / raw_df['B'][i + 1]
        O = (raw_df['G'][i] - raw_df['G'][i + 1]) / raw_df['G'][i + 1]
        if cnt == 1:
            P, Q = "", ""
        else:
            P = 1 if last[0] > last[1] else -1
            Q = 1 if last[2] > last[3] else -1
        last = [L, M, N, O]

        L_list.append(L)
        M_list.append(M)
        N_list.append(N)
        O_list.append(O)
        P_list.append(P)
        Q_list.append(Q)
    return P_list, Q_list


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑1：多因子排列.xlsx")
    sheet_names = ["当天开盘与下日开盘"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
    # print(get_intensity(in_file, sheet_names))
