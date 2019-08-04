# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/26 19:28 AM
@Author  : ddlee
@File    : section_6_jingzhi.py
"""

import os
import time

from tqdm import tqdm

from util_tools import *
import pandas as pd

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


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


def summary(in_file, usecols=4, left_border=5, right_border=11):
    raw_df = pd.read_excel(in_file, usecols=usecols)
    df = raw_df
    last = ["" for _ in range(usecols+1)]
    jingzhi_zuida=[]
    huiche_zuida=[]
    for time_span in range(left_border, right_border):
        idx_list, val_list = time_span_diff_with_cols(in_file, usecols, time_span)
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
    df.loc['jingzhi_zuida'] = jingzhi_zuida_sort_idx[-1] + usecols + 2
    huiche_zuida_sort_idx = np.argsort(huiche_zuida)
    df.loc['huiche_zuida'] = huiche_zuida_sort_idx[-1] + usecols + 2

    to_file = in_file.strip(".xlsx") + "_jingzhi_" + datesuffix + ".xlsx"
    df.to_excel(to_file, index=False, sheet_name=sheet_names[0])

    print("Save path:", to_file)
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join("data", "四因子盈亏数据_summary_2019-08-04.xlsx")
    sheet_names = ["因子盈亏"]  # 要处理的sheet下标，可以是多个

    summary(in_file, usecols=3, left_border=5, right_border=11)
