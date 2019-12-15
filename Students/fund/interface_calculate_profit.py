# -*- coding: utf-8 -*-
"""
@Time    : 2019/11/25 10:36 PM
@Author  : ddlee
@File    : interface_calculate_profit.py
"""
import sys


import datetime
import pandas as pd
import numpy as np


def interface_calculate_profit(
    in_file, start_date, end_date, init_capital=5, add_capital=1, reverse=False
):
    """

    Args:
        in_file: excel文件路径
        start_date: 收益计算开始日期
        end_date: 收益计算结束日期
        init_capital: 初始本金
        add_capital: 加仓本金
        reverse: 是否买空，reverse=True 对应 卖空，reverse=False 对应 买多

    Returns:

    """

    # 输入表格
    raw_df = pd.read_excel(in_file)

    assert "日期" in raw_df.columns, "必须包含 日期 列"
    assert "开盘价(元)" in raw_df.columns, "必须包含 开盘价(元) 列"

    # 日期列
    _date = raw_df["日期"]
    if _date.size < 2:
        print("请检查输入数据是否有误！")

    if _date[0] > _date[1]:
        print("日期呈下降趋势，进行翻转，如末尾有格式错误数据，请删除！")
        raw_df = raw_df[::-1]

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # 确保输入的日期范围有效！
    assert raw_df["日期"][0] <= start_date, "请检查输入的日期是否超出了范围！"
    assert start_date <= end_date, "请检查输入的日期是否有误！"
    price = None

    # 本金， 初始本金money即init_money
    capital = init_capital
    # 收益
    profit = 0
    period = 5
    cnt = 0
    # 控制 每五天一个周期
    flag = False
    for idx in range(raw_df.shape[0]):
        if flag == True:
            price = raw_df["开盘价(元)"][idx]
            # print(price)
            # 因为下面的判断要多加一次，这里设为-1
            cnt = -1
            flag = False

        # print(raw_df["日期"][idx].strftime('%Y-%m-%d'))
        if raw_df["日期"][idx] > end_date:
            break

        if raw_df["日期"][idx] < start_date:
            continue
        elif raw_df["日期"][idx] == start_date:
            # 记录初始价格
            price = raw_df["开盘价(元)"][idx]
        else:
            # raw_df["日期"][idx] > start_date
            cnt += 1
            if cnt == period:
                flag = True
                price_now = raw_df["开盘价(元)"][idx]
                # 涨跌幅
                chg = (price_now - price) / price
                # 如果卖空策略，将涨跌幅取反
                if reverse:
                    chg = -chg
                profit += capital * chg * 10
                print(
                    "price_now : {} price : {} chg : {} capital : {} profit : {}".format(
                        price_now, price, chg, capital, profit
                    )
                )
                # 如果涨跌幅为正 加仓，否则不加。
                if chg > 0:
                    capital += add_capital

    return profit


if __name__ == "__main__":

    in_file = "50ETF周度期权.xls"
    start_date = "2006-01-05"
    end_date = "2006-04-05"
    init_capital = 5
    add_capital = 1
    reverse = False
    profit = interface_calculate_profit(
        in_file,
        start_date,
        end_date,
        init_capital=init_capital,
        add_capital=add_capital,
        reverse=reverse,
    )
    print(
        "start_date : {}, end_date : {}, init_capital : {}, add_capital : {}, 卖空 : {}, profit : {}\n".format(
            start_date, end_date, init_capital, add_capital, reverse, profit
        )
    )

    start_date = "2006-08-02"
    end_date = "2006-09-18"
    init_capital = 5
    add_capital = 1
    reverse = True
    profit = interface_calculate_profit(
        in_file, start_date, end_date, init_capital=5, add_capital=1, reverse=True
    )
    print(
        "start_date : {}, end_date : {}, init_capital : {}, add_capital : {}, 卖空 : {}, profit : {}\n".format(
            start_date, end_date, init_capital, add_capital, reverse, profit
        )
    )
