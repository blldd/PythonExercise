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

    header = ["日期", "IC开盘价", "IC收盘价	", "IH开盘价", "IH收盘价", "全天强度IC方向", "全天强度当日收盘价盈亏", "全天强度当日收盘价盈亏", "新加列"]
    to_file = in_file.strip(".xlsx") + datesuffix + ".xlsx"
    writer = pd.ExcelWriter(to_file)

    excel_data = xlrd.open_workbook(in_file)
    for table in excel_data.sheets():
        rows = []
        for _date, B, C, D, E, F, G, H in read_sheet_row(table, range(8)):
            if not _date:
                continue
            if int(_date) not in ic_dict:
                _date = datetime(*xldate_as_tuple(_date, 0))
                _date = _date.strftime('%Y-%m-%d')
                row = [_date, B, C, D, E, F, G, H, ""]
                rows.append(row)
            else:
                I = 0
                cnt_num = 0
                for idx, minutes in enumerate(ic_dict[int(_date)]):
                    _date = minutes[0]
                    tmp_date = _date
                    # B = minutes[1]
                    C = minutes[4]
                    # D = ih_dict[int(_date)][idx][1]
                    E = ih_dict[int(_date)][idx][4]

                    _date = datetime(*xldate_as_tuple(_date, 0))
                    _date = _date.strftime('%Y-%m-%d %H:%M:%S')

                    if isinstance(C, float) and isinstance(E, float):
                        G = F * ((C - B) * 200 - (E - D) * 300)

                        if G < -20000 and float(tmp_date) >= int(tmp_date) + 0.384722222225 \
                                and float(tmp_date) <= int(tmp_date) + 0.635416666664:
                            print("I = 1!!!!!!!!", _date)
                            I = 1
                        if _date[11:] == "15:00:00" and I == 1:
                            cnt_num = cnt_num + 1
                            print(cnt_num, tmp_date, _date)

                            row = [_date, B, C, D, E, F, G, H, I]
                            rows.append(row)
                            I = 0
                        else:
                            row = [_date, B, C, D, E, F, G, H, ""]
                            rows.append(row)

                    else:
                        if _date[11:] == "15:00:00" and I == 1:
                            row = [_date, "", "", "", "", "", "", "", I]
                            rows.append(row)
                        else:
                            row = [_date, "", "", "", "", "", "", "", ""]
                            rows.append(row)

        write_rows2sheet(writer, rows, header, sheet_name=table.name)
    writer.save()
    print("Done!")


if __name__ == '__main__':
    in_file = os.path.join(tmp_dir, "因子汇总分钟级别.xlsx")
    IC_file = os.path.join(tmp_dir, "IC分钟数据.xlsx")
    IH_file = os.path.join(tmp_dir, "IH分钟数据.xlsx")

    process(in_file, IC_file, IH_file)
