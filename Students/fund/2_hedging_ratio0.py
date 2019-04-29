# -*- coding:UTF-8 -*-
import os
import time
from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def process(in_file, sheet_names):
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


def get_hands_num(in_file, sheet_names):
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
    hands_num = min(N_list) / min(Q_list)
    row = ["", "", "", "", "", "", "", "", "", "", "", "", "", hands_num, "", "", ""]
    rows.append(row)

    return hands_num


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑2：确定对冲比例.xlsx")
    sheet_names = ["最大回撤比"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
