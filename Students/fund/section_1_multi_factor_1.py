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

    rows = []
    last = [0, 0, 0, 0]
    cnt = 0
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        cnt += 1
        if isinstance(C, float):
            L = (C - B) / B
            M = (H - G) / G
            N = (B - C) / C
            O = (G - H) / H
            if cnt == 1:
                P, Q = "", ""
            else:
                P = 1 if last[0] > last[1] else -1
                Q = 1 if last[2] > last[3] else -1
            last = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            row  = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)

    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "IC(收盘-开盘）/开盘", "IH(收盘-开盘）/开盘", "IC（开盘-收盘）/收盘", "IH（开盘-收盘）/收盘",
                             "全天强度", "反转全天强度"], sheet_name="当天开盘与收盘")
    writer.save()
    print("Done!")

def get_intensity(in_file, sheet_names):
    rows = []
    last = [0, 0, 0, 0]
    cnt = 0
    P_list = []
    Q_list = []
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        cnt += 1
        if isinstance(C, float):
            L = (C - B) / B
            M = (H - G) / G
            N = (B - C) / C
            O = (G - H) / H
            if cnt == 1:
                P, Q = "", ""
            else:
                P = 1 if last[0] > last[1] else -1
                Q = 1 if last[2] > last[3] else -1
            last = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            P_list.append(P)
            Q_list.append(Q)
            row  = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)
    return P_list, Q_list


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑1：多因子排列.xlsx")
    sheet_names = ["当天开盘与收盘"]       # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
