# -*- coding:UTF-8 -*-
import os
import time
from util_tools import *
from xlrd import xldate_as_tuple
from tqdm import tqdm


datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def process(in_file, sheet_names):
    to_file = in_file.strip(".xlsx") + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)

    D_list = []
    I_list = []
    cnt = 0
    rows = []
    last = [0, 0, 0, 0]
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        D_list.append(D)
        I_list.append(I)
        cnt += 1
        if cnt < 2:
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')
            row = [_date, B, C, D, E, F, G, H, I, J, K, "", "", "", "", "", ""]
            rows.append(row)
            continue

        if isinstance(C, float):
            L = (B - D_list[-2]) / D_list[-2]
            M = (G - I_list[-2]) / I_list[-2]
            N = (D_list[-2] - B) / B
            O = (I_list[-2] - G) / G

            if cnt == 1:
                P, Q = "", ""
            else:
                P = 1 if L > M else -1
                Q = 1 if N > O else -1
            last = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)

    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "IC(当天开盘-前日结算）/前日结算", "IH(当天开盘-前日结算）/前日结算", "IC（前日结算-当天开盘）/当天开盘",
                             "IH（前日结算-当天开盘）/当天开盘",
                             "LM相比", "NO相比"], sheet_name=sheet_names[0])
    writer.save()
    print("Save path:", to_file)
    print("Done!")

def get_intensity(in_file, sheet_names, last_row_no=1):
    D_list = []
    I_list = []
    cnt = 0
    rows = []
    last = [0, 0, 0, 0]

    P_list = []
    Q_list = []
    for (_date, B, C, D, E, F, G, H, I, J, K) in read_excel_row_by_sheet(in_file, sheet_names, range(11)):
        D_list.append(D)
        I_list.append(I)
        cnt += 1
        if cnt < last_row_no:
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            P, Q = "", ""
            P_list.append(P)
            Q_list.append(Q)
            row = [_date, B, C, D, E, F, G, H, I, J, K, "", "", "", "", "", ""]
            rows.append(row)
            continue

        if isinstance(C, float):
            L = (B - D_list[-2]) / D_list[-2]
            M = (G - I_list[-2]) / I_list[-2]
            N = (D_list[-2] - B) / B
            O = (I_list[-2] - G) / G
            if cnt == 2:
                P, Q = "", ""
            else:
                P = 1 if L > M else -1
                Q = 1 if N > O else -1
            last = [L, M, N, O]

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            P_list.append(P)
            Q_list.append(Q)
            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
            rows.append(row)
    return P_list, Q_list


if __name__ == '__main__':
    in_file ="D:\\PycharmProjecs\\Project1\\Index_Logic\\Logic1\\Factor9\\期指数据0716.xlsx"
    sheet_names = ["基础数据"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
    # print(get_intensity(in_file, sheet_names))
