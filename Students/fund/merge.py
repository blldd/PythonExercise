# -*- coding:UTF-8 -*-
import os
import time
from util_tools import *
from xlrd import xldate_as_tuple
from conf import tmp_dir

datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def process(in_file, IC_file, IH_file):
    ic_dict = {}
    ih_dict = {}

    for row in read_excel_row(IC_file, range(5)):
        if int(row[0]) in ic_dict:
            ic_dict[int(row[0])].append(row)
        else:
            ic_dict[int(row[0])] = [row]

    for row in read_excel_row(IH_file, range(5)):
        if int(row[0]) in ih_dict:
            ih_dict[int(row[0])].append(row)
        else:
            ih_dict[int(row[0])] = [row]

    rows = []
    for _date, B, C, D, E, F, G, H in read_excel_row(in_file, range(8)):
        if not _date:
            continue
        if int(_date) not in ic_dict:
            _date = datetime(*xldate_as_tuple(_date, 0))
            _date = _date.strftime('%Y-%m-%d')
            row = [_date, B, C, D, E, F, G, H]
            rows.append(row)
        else:
            for idx, minutes in enumerate(ic_dict[int(_date)]):
                _date = minutes[0]
                # B = minutes[1]
                C = minutes[4]
                # D = ih_dict[int(_date)][idx][1]
                E = ih_dict[int(_date)][idx][4]

                _date = datetime(*xldate_as_tuple(_date, 0))
                _date = _date.strftime('%Y-%m-%d %H:%M:%S ')

                if isinstance(C, float) and isinstance(E, float):
                    G = F * ((C - B) * 200 - (E - D) * 300)
                    row = [_date, B, C, D, E, F, G, H]
                    rows.append(row)
                else:
                    row = [_date, "", "", "", "", "", "", ""]
                    rows.append(row)

    header = ["日期", "IC开盘价", "IC收盘价	", "IH开盘价", "IH收盘价", "全天强度IC方向", "全天强度当日收盘价盈亏", "全天强度当日收盘价盈亏"]
    to_file = in_file.strip(".xlsx") + datesuffix + ".xlsx"
    write_rows2excel(to_file, rows, header)


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "因子汇总分钟级别.xlsx")
    IC_file = os.path.join(tmp_dir, "IC分钟数据.xlsx")
    IH_file = os.path.join(tmp_dir, "IH分钟数据.xlsx")

    process(in_file, IC_file, IH_file)
