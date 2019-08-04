# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/26 19:28 AM
@Author  : ddlee
@File    : section_6_jingzhi.py
"""

import os
import time

from tqdm import tqdm
from xlrd import xldate_as_tuple

from util_tools import *
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

    return raw_df

def time_span_diff(in_file, time_span):
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


def summary(in_file, left_border=5, right_border=11):
    raw_df = get_raw_df(in_file, sheet_names)
    df = raw_df
    last = ["" for _ in range(4+1)]
    jingzhi_zuida=[]
    huiche_zuida=[]
    for time_span in range(left_border, right_border):
        idx_list, val_list = time_span_diff(in_file, time_span)
        mid_df = pd.DataFrame(
            {str(time_span) + "idx": pd.Series(idx_list), str(time_span) + "val": pd.Series(val_list)})
        df = df.join(mid_df)

        # 净值	区间最大值	最大回撤
        jingzhi, qujianzuida, zuidahuiche = [], [], []
        for i in range(raw_df.shape[0]):
            if i < right_border - 1:
                jz = ""
                qjzd = ""
                zdhc = ""

                jingzhi.append(jz)
                qujianzuida.append(qjzd)
                zuidahuiche.append(zdhc)

            elif i == right_border - 1:
                jz = 1
                qjzd = 1
                zdhc = 0

                jingzhi.append(jz)
                qujianzuida.append(qjzd)
                zuidahuiche.append(zdhc)

            else:
                jz = jingzhi[i - 1] + val_list[i] / 500000
                jingzhi.append(jz)

                qjzd = max(jingzhi[right_border - 1:])
                qujianzuida.append(qjzd)

                zdhc = jz - qjzd
                zuidahuiche.append(zdhc)

            # jingzhi.append(jz)
            # qujianzuida.append(qjzd)
            # zuidahuiche.append(zdhc)

        last.append('')
        last.append('')
        last.append(jz)
        last.append('')
        last.append(min(zuidahuiche[right_border - 1:]))

        jingzhi_zuida.append(jz)
        huiche_zuida.append(zdhc)

        right_df = pd.DataFrame({str(time_span) + "jz": pd.Series(jingzhi),
                                 str(time_span) + "qjzd": pd.Series(qujianzuida),
                                 str(time_span) + "zdhc": pd.Series(zuidahuiche)})
        df = df.join(right_df)

    df.loc['last'] = last

    jingzhi_zuida_sort_idx = np.argsort(jingzhi_zuida)
    df.loc['jingzhi_zuida'] = jingzhi_zuida_sort_idx[-1] + 4 + 2
    huiche_zuida_sort_idx = np.argsort(huiche_zuida)
    df.loc['huiche_zuida'] = huiche_zuida_sort_idx[-1] + 4 + 2

    to_file = in_file.strip(".xlsx") + "_jingzhi_" + datesuffix + ".xlsx"
    df.to_excel(to_file, index=False, sheet_name=sheet_names[0])

    print("Save path:", to_file)
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join("data", "四因子盈亏数据_summary_2019-08-04.xlsx")
    sheet_names = ["因子盈亏"]  # 要处理的sheet下标，可以是多个
    factors = ["反转最后一小时", "反转前两天", "前三天", "前两天"]
    cols = ["B", "C", "D", "E"]

    summary(in_file, left_border=5, right_border=11)
