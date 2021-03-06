# -*- coding:UTF-8 -*-
import os
import time

from tqdm import tqdm

from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def process(in_file, sheet_names, last=3):
    to_file = in_file.strip(".xlsx") + "_" + sheet_names[0] + "_" + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)

    B_list = []
    G_list = []
    cnt = 0
    rows = []
    last_row = [0, 0, 0, 0]
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        B_list.append(B)
        G_list.append(G)
        cnt += 1
        if cnt < last:
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

            if cnt == last:
                P, Q = "", ""
            else:
                P = 1 if last_row[0] > last_row[1] else -1
                Q = 1 if last_row[2] > last_row[3] else -1
            last_row = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)

    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "IC(当天收盘-前三天开盘）/前三天开盘", "IH(当天收盘-前三天开盘）/前三天开盘", "IC（前三天开盘-当天收盘）/当天收盘",
                             "IH（前三天开盘-当天收盘）/当天收盘",
                             "LM相比", "NO相比"], sheet_name=sheet_names[0])
    writer.save()
    print("Save path:", to_file)
    print("Done!")

def get_intensity(in_file, sheet_names, last=3):
    B_list = []
    G_list = []
    cnt = 0
    rows = []
    last_row = [0, 0, 0, 0]

    P_list = []
    Q_list = []
    for (_date, B, C, D, E, F, G, H, I, J, K) in tqdm(read_excel_row_by_sheet(in_file, sheet_names, range(11))):
        B_list.append(B)
        G_list.append(G)
        cnt += 1
        if cnt < last:
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            P, Q = "", ""
            P_list.append(P)
            Q_list.append(Q)
            row = [_date, B, C, D, E, F, G, H, I, J, K, "", "", "", "", "", ""]
            rows.append(row)
            continue

        if isinstance(C, float):
            L = (C - B_list[-3]) / B_list[-3]
            M = (H - G_list[-3]) / G_list[-3]
            N = (B_list[-3] - C) / C
            O = (G_list[-3] - H) / H

            if cnt == last:
                P, Q = "", ""
            else:
                P = 1 if last_row[0] > last_row[1] else -1
                Q = 1 if last_row[2] > last_row[3] else -1
            last_row = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            P_list.append(P)
            Q_list.append(Q)
            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)
    return P_list, Q_list


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑1：多因子排列.xlsx")
    sheet_names = ["当天收盘与前三天开盘"]  # 要处理的sheet下标，可以是多个

    # process(in_file, sheet_names)
    print(get_intensity(in_file, sheet_names))
