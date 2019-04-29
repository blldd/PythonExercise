# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/28 11:28 AM
@Author  : ddlee
@File    : 3_profit_loss_0.py
"""
import os
import time
from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir

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
    to_file = in_file.strip(".xlsx") + "_" + sheet_names[0] + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)
    rows = []

    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "IC净值", "IC区间最大", "IC最大回撤",
                             "IH净值", "IH区间最大", "IH最大回撤"], sheet_name="最大回撤比")
    writer.save()
    print("Save path:", to_file)
    print("Done!")


"	正向	反转	IC手数（默认为1）	IH手数（默认为1）	正向盈亏(第二天开盘价）	正向盈亏（当天收盘价）	止损正向盈亏（当天收盘价）	正向重开仓盈亏		正向重开仓止损盈亏	正向盈亏（第二天开盘价），考虑盘中止损重开仓	反向盈亏(第二天开盘价）	反向盈亏（当天收盘价）	止损反向盈亏（当天收盘价）	反向重开仓盈亏		反向重开仓止损盈亏	反向盈亏（第二天开盘价），考虑盘中止损重开仓"


def process1(in_file, sheet_names):
    to_file = in_file.strip(".xlsx") + "_" + sheet_names[0] + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)

    L_list = []
    O_list = []
    N_list = []
    Q_list = []
    cnt = 0
    rows = []
    last = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        cnt += 1
        if cnt == 1:
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            L = 1
            L_list.append(L)
            M = max(L_list)
            N = L - M
            N_list.append(N)

            O = 1
            O_list.append(O)
            P = max((O_list))
            Q = O - P
            Q_list.append(Q)

            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)

            last = [_date, B, C, D, E, F, G, H, I, J, K]
            continue

        if isinstance(C, float):
            L = (C - last[2]) / last[2] + L_list[-1]
            L_list.append(L)
            M = max(L_list)
            N = L - M
            N_list.append(N)
            Q_list.append(Q)

            O = (H - last[7]) / last[7] + O_list[-1]
            O_list.append(O)
            P = max((O_list))
            Q = O - P

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)

            last = [_date, B, C, D, E, F, G, H, I, J, K]

    row = ["", "", "", "", "", "", "", "", "", "", "", "", "", min(N_list), "", "", min(Q_list)]
    rows.append(row)
    row = ["", "", "", "", "", "", "", "", "", "", "", "", "", min(N_list) / min(Q_list), "", "", ""]
    rows.append(row)
    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "IC净值", "IC区间最大", "IC最大回撤",
                             "IH净值", "IH区间最大", "IH最大回撤"], sheet_name="最大回撤比")
    writer.save()
    print("Save path:", to_file)
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑3：因子的当日盈亏.xlsx")
    sheet_names = ["当天开盘与收盘"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
