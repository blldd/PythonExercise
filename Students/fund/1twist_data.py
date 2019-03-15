# -*- coding:UTF-8 -*-
import os
import time

from conf import tmp_dir
from util_tools import *
from datetime import datetime
from xlrd import xldate_as_tuple
from tqdm import tqdm


def get_max(vals, col_dict, row_idx):
    sorted_idx = get_sort_idx(vals)

    max_idx = sorted_idx[-1]
    col = col_dict[max_idx]
    return col[row_idx]


def prepare_data(in_file):
    date_list = []
    A_list = []
    B_list = []
    C_list = []
    D_list = []
    E_list = []
    F_list = []
    G_list = []
    H_list = []
    I_list = []
    J_list = []
    K_list = []
    L_list = []

    col_idxs = range(13)
    for _date, A, B, C, D, E, F, G, H, I, J, K, L in read_excel_row(in_file, col_idxs):
        date_list.append(_date)
        A_list.append(A)
        B_list.append(B)
        C_list.append(C)
        D_list.append(D)
        E_list.append(E)
        F_list.append(F)
        G_list.append(G)
        H_list.append(H)
        I_list.append(I)
        J_list.append(J)
        K_list.append(K)
        L_list.append(L)

    return (date_list, A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list, I_list, J_list, K_list, L_list)


def process(in_file, span_list):
    date_list, A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list, I_list, J_list, K_list, L_list = prepare_data(
        in_file)

    length = len(A_list)

    workbook = xlwt.Workbook()

    time_span_profits = []
    for span in tqdm(span_list):
        AA_list = []
        BB_list = []
        CC_list = []
        DD_list = []
        EE_list = []
        FF_list = []
        GG_list = []
        HH_list = []
        II_list = []
        JJ_list = []
        KK_list = []
        LL_list = []

        AAA_list = []
        for row_idx in range(length):
            if row_idx < span:
                AA_list.append(0)
                BB_list.append(0)
                CC_list.append(0)
                DD_list.append(0)
                EE_list.append(0)
                FF_list.append(0)
                GG_list.append(0)
                HH_list.append(0)
                II_list.append(0)
                JJ_list.append(0)
                KK_list.append(0)
                LL_list.append(0)

                AAA_list.append(0)
            else:
                AA = sum(A_list[row_idx - span:row_idx])  # 切片 list[start: end]
                BB = sum(B_list[row_idx - span:row_idx])
                CC = sum(C_list[row_idx - span:row_idx])
                DD = sum(D_list[row_idx - span:row_idx])
                EE = sum(E_list[row_idx - span:row_idx])
                FF = sum(F_list[row_idx - span:row_idx])
                GG = sum(G_list[row_idx - span:row_idx])
                HH = sum(H_list[row_idx - span:row_idx])
                II = sum(I_list[row_idx - span:row_idx])
                JJ = sum(J_list[row_idx - span:row_idx])
                KK = sum(K_list[row_idx - span:row_idx])
                LL = sum(L_list[row_idx - span:row_idx])

                last_time_span_sum_arr = [AA, BB, CC, DD, EE, FF, GG, HH, II, JJ, KK, LL]
                col_dict = [A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list, I_list, J_list, K_list,
                            L_list]

                AAA = get_max(last_time_span_sum_arr, col_dict, row_idx)

                AA_list.append(AA)
                BB_list.append(BB)
                CC_list.append(CC)
                DD_list.append(DD)
                EE_list.append(EE)
                FF_list.append(FF)
                GG_list.append(GG)
                HH_list.append(HH)
                II_list.append(II)
                JJ_list.append(JJ)
                KK_list.append(KK)
                LL_list.append(LL)

                AAA_list.append(AAA)

        rows = []
        for _date, A, B, C, D, E, F, G, H, I, J, K, L, \
            AA, BB, CC, DD, EE, FF, GG, HH, II, JJ, KK, LL, AAA \
                in zip(date_list, A_list, B_list, C_list, D_list, E_list, F_list,
                       G_list, H_list, I_list, J_list, K_list, L_list,
                       AA_list, BB_list, CC_list, DD_list, EE_list, FF_list, GG_list,
                       HH_list, II_list, JJ_list, KK_list, LL_list, AAA_list):
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d')
            row = [_date, A, B, C, D, E, F, G, H, I, J, K, L, AA, BB, CC, DD, EE, FF, GG, HH, II, JJ, KK, LL, AAA]
            rows.append(row)

        to_file = os.path.join(tmp_dir, os.path.split(in_file)[-1].split(".")[0] + datesuffix + ".xls")
        header = ["date", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK", "LL", "AAA"]

        time_span_profit = sum(AAA_list[60:])
        time_span_profits.append(time_span_profit)

        sheet_name = str(span) + "天" + str(int(time_span_profit))
        write_rows_to_sheet(workbook, sheet_name, header, rows, to_file)

        # time_span_profit = sum(AAA_list[60:])
        # time_span_profits.append(time_span_profit)

    # 按最大收益排序，降序排列
    sort_idx = get_sort_idx(time_span_profits)[::-1]
    #
    sort_idx = [str(i + 1) for i in sort_idx]
    print(time_span_profits)
    print(sort_idx)
    print("最大收益的 time span 为：" + sort_idx[0])
    print("按照最大收益 排序为：" + ", ".join(sort_idx))


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "测试.xlsx")
    span_list = [10, 20, 30, 40, 50, 60]
    span_list = [i for i in range(1, 61)]

    process(in_file, span_list)

"""
def process(in_file):
    A_list = []
    B_list = []
    C_list = []
    D_list = []

    E_list = []
    F_list = []
    G_list = []

    H_list = []

    row_idx = 0
    col_idxs = [0, 1, 2, 3]
    for A, B, C, D in read_excel_row(in_file, col_idxs):
        A_list.append(str(A))
        B_list.append(B)
        C_list.append(C)
        D_list.append(D)

        if row_idx < 10:
            E_list.append(0)
            F_list.append(0)
            G_list.append(0)
            H_list.append(0)
        else:
            E = sum(B_list[-11:-1])
            F = sum(C_list[-11:-1])
            G = sum(D_list[-11:-1])

            last_10_sum_arr = [E, F, G]
            col_dict = [B_list, C_list, D_list]

            H = get_max(last_10_sum_arr, col_dict, row_idx)

            E_list.append(E)
            F_list.append(F)
            G_list.append(G)
            H_list.append(H)

        row_idx += 1

    rows = []
    for A, B, C, D, E, F, G, H in zip(A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list):
        row = [A, B, C, D, E, F, G, H]
        rows.append(row)

    to_file = os.path.join(tmp_dir, os.path.split(in_file)[-1].split(".")[0] + datesuffix + ".xls")
    header = ["A", "B", "C", "D", "E", "F", "G", "H"]
    write_rows_to_excel(header, rows, to_file)
"""
