# -*- coding:UTF-8 -*-
import os
import time
from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def process(in_file, sheet_names):
    to_file = in_file.strip(".xlsx") + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)

    B_list = []
    G_list = []
    cnt = 0
    rows = []
    last = [0, 0, 0, 0]
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        B_list.append(B)
        G_list.append(G)
        cnt += 1
        if cnt < 3:
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')
            row = [_date, B, C, D, E, F, G, H, I, J, K, "", "", "", "", "", ""]
            rows.append(row)
            continue

        if isinstance(C, float):
            L = (C - B_list[-3]) / B_list[-3]
            M = (H - G_list[-3]) / G_list[-3]
            N = (B_list[-3] - C) / C
            O = (G_list[-3] - H) / H

            if cnt == 3:
                P, Q = "", ""
            else:
                P = 1 if last[0] > last[1] else -1
                Q = 1 if last[2] > last[3] else -1
            last = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)

    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "IC净值", "IC区间最大", "IC最大回撤",
                             "IH净值", "IH区间最大", "IH最大回撤"], sheet_name="最大回撤比")
    writer.save()
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑2：确定对冲比例.xlsx")
    sheet_names = ["最大回撤比"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
