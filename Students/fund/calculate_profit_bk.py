# -*- coding: utf-8 -*-
"""
@Time    : 2019/11/04 8:36 PM
@Author  : ddlee
@File    : calculate_profit.py
"""
import sys

"""
calculate 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def split_k_fold(in_file, k=10):
    """split to k fold

    Args:
        in_file:
        k:

    Returns:

    """
    raw_df = pd.read_excel(in_file)

    batch_size = (
        raw_df.shape[0] // k if raw_df.shape[0] % k == 0 else raw_df.shape[0] // k + 1
    )
    writer = pd.ExcelWriter(in_file.split(".")[0] + "_split.xlsx")

    for i in range(k):
        batch_df = raw_df[i * batch_size : (i + 1) * batch_size]
        batch_df.to_excel(writer, sheet_name=str(i), index=False)
    writer.save()


def process(in_file, index="收盘点位", strategy=0.08, start=100):
    """calculate profit while use strategy.

    Args:
        in_file:
        index: 对比指标
        strategy: 策略，如0.08, 可任意修改
        start: 起始资金

    Returns:

    """
    raw_df = pd.read_excel(in_file, sheet_name=0)
    sequence_data = raw_df[index][::-1].values

    # plt.plot(range(len(sequence_data)), sequence_data, color="r")
    # plt.show()

    sequence_data = list(map(lambda x: x.replace(",", ""), sequence_data))
    sequence_data = list(map(float, sequence_data))
    # sequence_data = sequence_data[-1000:]

    # 全部财产
    all_money = start
    # 股票数量
    amount = None
    # money status
    is_cashe = True

    # init
    local_min = sys.maxsize
    local_max = -sys.maxsize
    last = sequence_data[0]
    now = sequence_data[1]

    # ascend or not
    is_ascend = 0 if last > now else 1

    profit_list = []
    status_list = []
    amount_list = []
    local_min_list = []
    local_max_list = []

    for price in sequence_data[1:]:
        if price < last and is_ascend == 0:
            if amount and (local_max - price) / local_max > strategy:
                # full out
                all_money = price * amount

                amount = None
                is_cashe = True
                local_max = -sys.maxsize
                pass

        elif price < last and is_ascend == 1:
            local_max = last if last > local_max else local_max
            if amount and (local_max - price) / local_max > strategy:
                # full out
                all_money = price * amount

                amount = None
                is_cashe = True
                local_max = -sys.maxsize
                pass
            is_ascend = 0

        elif price > last and is_ascend == 1:
            if is_cashe and (price - local_min) / local_min > strategy:
                # full in
                amount = all_money / price
                is_cashe = False
                local_min = sys.maxsize
                pass

        elif price > last and is_ascend == 0:
            local_min = last if last < local_min else local_min
            if is_cashe and (price - local_min) / local_min > strategy:
                # full in
                amount = all_money / price
                is_cashe = False
                local_min = sys.maxsize
                pass
            is_ascend = 1

        all_money = price * amount if not is_cashe else all_money

        last = price
        profit_list.append(all_money)
        status_list.append("空仓" if is_cashe else "满仓")
        amount_list.append(amount)
        local_min_list.append(local_min)
        local_max_list.append(local_max)

    # print(results)

    profit_list = profit_list[::-1]
    profit_col = pd.DataFrame(profit_list, columns=["收益"])

    status_list = status_list[::-1]
    status_col = pd.DataFrame(status_list, columns=["状态"])

    amount_list = amount_list[::-1]
    amount_col = pd.DataFrame(amount_list, columns=["持仓"])

    local_min_list = local_min_list[::-1]
    local_min_col = pd.DataFrame(local_min_list, columns=["上次卖出之后的最低点"])
    local_max_list = local_max_list[::-1]
    local_max_col = pd.DataFrame(local_max_list, columns=["上次买入之后的最高点"])

    all_df = pd.concat(
        [raw_df, profit_col, status_col, amount_col, local_min_col, local_max_col],
        axis=1,
    )
    to_file = in_file.split(".")[0] + str(strategy) + ".xlsx"
    all_df.to_excel(to_file, index=False)
    print("save to file: {}".format(to_file))
    return (all_money, is_cashe)


if __name__ == "__main__":
    in_file = "道琼斯工业指数行情统计.xlsx"
    # split_k_fold(in_file)
    # in_file = "道琼斯工业指数行情统计_split.xlsx"

    # index: 对比指标
    # stratege: 策略，如0.08, 可任意修改
    # start: 起始资金

    all_money = process(in_file, index="收盘点位", strategy=0.08, start=100)
    print(all_money)
