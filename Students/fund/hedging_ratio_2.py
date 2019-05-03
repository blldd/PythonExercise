# -*- coding:UTF-8 -*-
import os
import time

from tqdm import tqdm

from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir
import math

datesuffix = time.strftime("%Y-%m-%d", time.localtime())

def avg(arr):
    new_arr = []
    for i in arr:
        if isinstance(i, float):
            new_arr.append(i)
    return sum(new_arr) / len(new_arr)

def process(in_file, sheet_names):
    to_file = in_file.strip(".xlsx") + "_"+ sheet_names[0] + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)

    L_list = []
    M_list = []
    cnt = 0
    rows = []
    for (_date, B, C, D, E, F, G, H, I, J, K) in tqdm(read_excel_row_by_sheet(in_file, sheet_names, range(11))):
        cnt += 1
        if isinstance(C, float):
            L = C * 200
            L_list.append(L)
            M = H * 300
            M_list.append(M)

            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d %H:%M:%S')

            row = [_date, B, C, D, E, F, G, H, I, J, K, L, M]
            rows.append(row)


    row = ["", "", "", "", "", "", "", "", "", "", "", avg(L_list), avg(M_list)]
    rows.append(row)
    row = ["", "", "", "", "", "", "", "", "", "", "", avg(L_list) / avg(M_list), ""]
    rows.append(row)
    write_rows2sheet(writer, rows,
                     header=["日期", "IC开盘价(元)", "IC收盘价(元)",
                             "IC结算价", "最高价(元)", "最低价(元)", "IH开盘价(元)",
                             "IH收盘价(元)", "IH结算价", "最高价(元)", "最低价(元)",
                             "", ""], sheet_name="合约总金额日平均比")
    writer.save()
    print("Save path:", to_file)
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "逻辑2：确定对冲比例.xlsx")
    sheet_names = ["合约总金额日平均比"]  # 要处理的sheet下标，可以是多个

    process(in_file, sheet_names)
