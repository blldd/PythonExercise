# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/26 19:28 AM
@Author  : ddlee
@File    : section_5_time_span_diff.py
"""

import os
import time

from tqdm import tqdm

from util_tools import *
from xlrd import xldate_as_tuple
import pandas as pd

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def prepare_data(in_file, sheet_names):
    raw_rows = []
    for (_date, B, C, D, E) in read_excel_row_by_sheet(in_file, sheet_names, range(5)):
        _date = datetime(*xldate_as_tuple(_date, 0))
        _date = _date.strftime('%Y-%m-%d %H:%M:%S')
        row = [_date, B, C, D, E]
        raw_rows.append(row)
    return raw_rows


def get_raw_df(in_file, sheet_names):
    raw_rows = prepare_data(in_file, sheet_names)
    raw_df = pd.DataFrame(raw_rows, columns=["_date", "B", "C", "D", "E"])
    # 因为和填充到下一行，为避免最后一行数据未计算，补充一行数据
    # raw_df.loc[raw_df.shape[0] + 1] = 0

    return raw_df


def time_span_diff(in_file, sheet_names, time_span):
    raw_df = get_raw_df(in_file, sheet_names)

    F_list, G_list, H_list, I_list, J_list, K_list = [], [], [], [], [], []
    for i in tqdm(range(raw_df.shape[0])):
        if i < time_span:
            F, G, H, I, J, K = "", "", "", "", "", ""

        else:
            F = raw_df['B'][i - time_span:i].sum()
            G = raw_df['C'][i - time_span:i].sum()
            H = raw_df['D'][i - time_span:i].sum()
            I = raw_df['E'][i - time_span:i].sum()
            vals = [F, G, H, I]
            # 值排序，返回最大的下标
            sort_idx = np.argsort(vals)
            # 值最大的下标
            idx = sort_idx[-1]
            J = factors[idx]
            # 对应的值
            K = raw_df[cols[idx]][i]

        F_list.append(F)
        G_list.append(G)
        H_list.append(H)
        I_list.append(I)
        J_list.append(J)
        K_list.append(K)

    # right = pd.DataFrame({'F': pd.Series(F_list), 'G': pd.Series(G_list),
    #                       'H': pd.Series(H_list), 'I': pd.Series(I_list),
    #                       'J': pd.Series(J_list), 'K': pd.Series(K_list)})
    # df = raw_df.join(right)
    # df.columns = ["日期", "反转最后一小时", "反转前两天", "前三天", "前两天", "反转最后一小时", "反转前两天", "前三天", "前两天", "最大值对应下标", "最大值"]
    # to_file = in_file.strip(".xlsx") + "_" + str(time_span) + "_" + datesuffix + ".xlsx"
    # df.to_excel(to_file, index=False, sheet_name=sheet_names[0])
    #
    # print("Save path:", to_file)
    # print("Done!")

    return (J_list, K_list)


def time_span_diff_with_cols(in_file, usecols, time_span):
    raw_df = pd.read_excel(in_file, usecols=usecols)

    col_names = raw_df.columns
    generate_cols = [[] for _ in range(usecols)]
    result_cols = [[] for _ in range(2)]

    for i in tqdm(range(raw_df.shape[0])):
        vals = []
        for j, col in enumerate(generate_cols):
            if i < time_span:
                tmp_val = ""
            else:
                tmp_val = float(raw_df.iloc[:, [j + 1]][i - time_span:i].sum())
            # vals = [F, G, H, I]
            vals.append(tmp_val)

            # F_list.append(F)
            generate_cols[j].append(tmp_val)

        if i < time_span:
            result_cols[0].append("")
            result_cols[1].append("")
        else:
            # 值排序，返回最大的下标
            sort_idx = np.argsort(vals)
            # 值最大的下标
            idx = sort_idx[-1]
            J = col_names[idx + 1]
            # 对应的值
            K = raw_df.iloc[i, idx + 1]
            result_cols[0].append(J)
            result_cols[1].append(K)

    # columns = ['gen' + i for i in col_names[1:]]
    # middle = pd.DataFrame(map(list, zip(*generate_cols)), columns=columns)
    # right = pd.DataFrame(map(list, zip(*result_cols)))
    #
    # df = raw_df.join(middle)
    # df = df.join(right)
    # # df.columns = ["日期", "反转最后一小时", "反转前两天", "前三天", "前两天", "反转最后一小时", "反转前两天", "前三天", "前两天", "最大值对应下标", "最大值"]
    # to_file = in_file.strip(".xlsx") + "_" + str(time_span) + "_" + datesuffix + ".xlsx"
    # df.to_excel(to_file, index=False, sheet_name=sheet_names[0])
    #
    # print("Save path:", to_file)
    # print("Done!")

    return result_cols


def summary(in_file, usecols=3):
    raw_df = pd.read_excel(in_file, usecols=usecols)
    df = raw_df
    for time_span in range(5, 11):
        idx_list, val_list = time_span_diff_with_cols(in_file, usecols, time_span)
        right = pd.DataFrame({str(time_span) + "idx": pd.Series(idx_list), str(time_span) + "val": pd.Series(val_list)})
        df = df.join(right)
    to_file = in_file.strip(".xlsx") + "_summary_" + datesuffix + ".xlsx"
    df.to_excel(to_file, index=False, sheet_name=sheet_names[0])

    print("Save path:", to_file)
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join("data", "四因子盈亏数据.xlsx")
    sheet_names = ["因子盈亏"]  # 要处理的sheet下标，可以是多个
    factors = ["反转最后一小时", "反转前两天", "前三天", "前两天"]
    cols = ["B", "C", "D", "E"]

    summary(in_file, usecols=4)
