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


def process(in_file, index="收盘点位", strategy=0.08, start=100):
    raw_df = pd.read_excel(in_file)
    sequence_data = raw_df[index][::-1].values

    sequence_data = list(map(lambda x: x.replace(",", ""), sequence_data))
    sequence_data = list(map(float, sequence_data))
    # sequence_data = sequence_data[-1000:]

    # 全部财产
    all_money = start
    # 股票数量
    amount = None

    # init
    local_min = None
    local_max = None
    last = sequence_data[0]
    now = sequence_data[1]

    # ascend or not
    is_ascend = 0 if last > now else 1

    # money status
    is_cashe = True

    results = []

    for price in sequence_data[1:]:
        if price < last and is_ascend == 0:
            if local_max and amount and (local_max - price) / local_max > strategy:
                # full out
                all_money = price * amount
                is_cashe = True
                pass
            last = price

        elif price < last and is_ascend == 1:
            local_max = last
            if local_max and amount and (local_max - price) / local_max > strategy:
                # full out
                all_money = price * amount
                is_cashe = True
                pass
            is_ascend = 0

        elif price > last and is_ascend == 1:
            if local_min is not None and (price - local_min) / local_min > strategy:
                # full in
                amount = all_money / price
                is_cashe = False
                pass

            last = price

        elif price > last and is_ascend == 0:
            local_min = last
            if local_min is not None and (price - local_min) / local_min > strategy:
                # full in
                amount = all_money / price
                is_cashe = False
                pass
            is_ascend = 1

        results.append(all_money)

    # print(results)

    results = results[::-1]
    col = pd.DataFrame(results, columns=["收益"])

    all_df = pd.concat([raw_df, col], axis=1)
    all_df.to_excel(in_file.split(".")[0] + str(strategy) + ".xlsx", index=False)

    return (all_money, is_cashe)


if __name__ == "__main__":

    in_file = "道琼斯工业指数行情统计.xlsx"

    # index: 对比指标
    # stratege: 策略，如0.08, 可任意修改
    # start: 起始资金
    all_money = process(in_file, index="收盘点位", strategy=0.08, start=100)
    print(all_money)
