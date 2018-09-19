# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The test file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
import glob
import os
import xlrd
import xlsxwriter
import xlwt


def main(in_files, to_dir):
    for in_file in glob.glob(in_files):
        to_1_file = to_dir + "/1" + os.path.split(in_file)[-1]
        to_2_file = to_dir + "/2" + os.path.split(in_file)[-1]
        print("%s -> %s" % (in_file, to_1_file))
        print("%s -> %s" % (in_file, to_2_file))
        workbook = xlrd.open_workbook(in_file)
        table = workbook.sheets()[0]
        nrows = table.nrows
        header = None
        one_rows = []
        two_rows = []
        for i in range(nrows):
            row = table.row_values(i)
            if i == 0:
                header = row
            elif i%3 == 0:
                one_rows.append(row)
            else:
                two_rows.append(row)

        _write_rows_to_excel(header, one_rows, to_1_file)
        _write_rows_to_excel(header, two_rows, to_2_file)


def _write_rows_to_excel(header, rows, to_file):
    workbook = xlsxwriter.Workbook(to_file)
    sheet = workbook.add_worksheet()
    row_index = 0
    row_index = _write_row_in_sheet(row_index, header, sheet)
    for row in rows:
        row_index = _write_row_in_sheet(row_index, row, sheet)
    workbook.close()


def _write_row_in_sheet(row_index, row, sheet):
    for i, item in enumerate(row):
        sheet.write(row_index, i, item)
    return row_index + 1


if __name__ == '__main__':
    main("../data/gd_20171218.test.xls", to_dir="../out")