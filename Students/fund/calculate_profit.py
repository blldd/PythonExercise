# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/19 6:08 PM
@Author  : ddlee
@File    : top_k.py
"""

"""
calculate 
"""

import pandas as pd
import numpy as np


def group(in_file):
    raw_df = pd.read_excel(in_file)
    raw_df = raw_df.fillna(0)

    classes = raw_df["申万一级行业"].unique()

    class_df_arr = []

    for idx, cls in enumerate(classes):
        class_df = raw_df[raw_df["申万一级行业"] == cls]
        class_df_arr.append((cls, class_df))

    return class_df_arr


def process(in_file, writer, topk=3):
    class_df_arr = group(in_file)

    top3_df = pd.DataFrame()

    for cls, class_df in class_df_arr:

        class_df = class_df.reset_index()
        new_df = class_df.drop(drop_cols + ["index"], axis=1)  # drop不会就地修改，创建副本返回

        for col in ascend_cols:
            if col == "流动资产/总资产" and (cls in {"银行", "非银金融"}):
                new_df[col] = pd.Series([0] * new_df.shape[0])
            else:
                idxs = np.argsort(class_df[col])
                for i, idx in enumerate(idxs):
                    new_df[col][idx] = i + 1

        for col in descend_cols:
            idxs = np.argsort(class_df[col])[::-1]
            for i, idx in enumerate(idxs):
                new_df[col][idx] = i + 1

        # class_df.loc['sum'] = class_df.apply(lambda x: x.sum())
        new_df["sum"] = new_df.apply(lambda x: x.sum(), axis=1)

        dropped_df = class_df[drop_cols]
        new_df = pd.concat([dropped_df, new_df], axis=1)
        new_df = new_df.sort_values(by="sum", ascending=False)
        new_df = new_df.reset_index()
        new_df = new_df.drop(["index"], axis=1)  # drop不会就地修改，创建副本返回

        new_df.to_excel(writer, cls)

        # 各行业top3汇总
        top3_df = pd.concat([top3_df, new_df.iloc[:topk]], ignore_index=True)

    top3_df.to_excel(writer, "top_k汇总")

    writer.save()


if __name__ == "__main__":
    # in_file = "基础数据.xlsx"
    # drop_cols = ["代码", "简称", "申万一级行业"]
    # ascend_cols = [
    #     "总市值（亿元）↓",
    #     "主营业务利润/主营业务收入",
    #     "净利润/主营业务利润",
    #     "流动资产/总资产",
    #     "经营现金流量净额/主营业务收入",
    #     "净资产收益率(%)",
    # ]
    # descend_cols = ["资产负债率(%)"]
    # writer = pd.ExcelWriter(in_file.split(".")[0] + "_score.xlsx")
    #
    # process(in_file, writer)

    in_file = "中证800基础数据.xlsx"
    drop_cols = ["代码", "简称", "申万一级行业"]
    ascend_cols = [
        "流通市值/总市值",
        "主营业务利润/主营业务收入",
        "净利润/主营业务利润",
        "流动资产/总资产",
        "经营现金流量净额(亿元)",
        "经营现金流量净额/主营业务收入",
        "净资产收益率(%)",
    ]
    descend_cols = ["资产负债率(%)"]
    writer = pd.ExcelWriter(in_file.split(".")[0] + "_score.xlsx")

    process(in_file, writer, topk=5)
