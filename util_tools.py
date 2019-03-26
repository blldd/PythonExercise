# -*- coding:UTF-8 -*-

import functools
import time
import random
import json
import numpy as np
import xlrd
import xlwt
import pandas as pd
import os
import logging
from logging.handlers import TimedRotatingFileHandler
import yaml
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
import scipy.stats
from datetime import datetime
datesuffix = time.strftime("%Y-%m-%d", time.localtime())


def excute_time_log(func):
    """
    装饰器，用来打印函数运行时间
    用法：函数名前 加 @excute_time_log
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t1 = time.time()
        res = func(*args, **kw)
        print('Method {%s} excute in %sms.' % (func.__name__, 1000 * (time.time() - t1)))
        return res

    return wrapper


def read_excel_row(in_file, col_idxs):
    """
    :param in_file: 待读取Excel文件路径
    :param col_idxs: 待读取列编号，如[1,3,5] 表示第2，4，6列
    :return:
    """
    data = xlrd.open_workbook(in_file)
    for table in data.sheets():
        nrows = table.nrows
        for i in range(nrows):
            if i == 0:
                continue
            row = table.row_values(i)
            one_row = []
            for col_idx in col_idxs:
                one_row.append(row[col_idx])
            yield tuple(one_row)


def write_rows_to_excel(header, rows, to_file):
    """
    todo 即将废弃，推荐使用 write_rows2excel 方法
    :param header:
    :param rows:
    :param to_file:
    :return:
    """
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet1')
    row_index = 0
    row_index = _write_row_in_sheet(row_index, header, sheet)
    for row in rows:
        row_index = _write_row_in_sheet(row_index, row, sheet)
    workbook.save(to_file)


def _write_row_in_sheet(row_index, row, sheet):
    for i, item in enumerate(row):
        sheet.write(row_index, i, item)
    return row_index + 1


def write_rows_to_sheet(workbook, sheet_name, header, rows, to_file):
    """
    todo 即将废弃，推荐使用 write_rows2sheet 方法
    :param workbook:
    :param sheet_name:
    :param header:
    :param rows:
    :param to_file:
    :return:
    """
    sheet = workbook.add_sheet(sheet_name)
    row_index = 0
    row_index = _write_row_in_sheet(row_index, header, sheet)
    for row in rows:
        row_index = _write_row_in_sheet(row_index, row, sheet)
    workbook.save(to_file)


def write_rows2excel(to_file, rows, header=None):
    """
    写入数据到Excel，如果数据量大于1048575行，自动分sheet，每1000000行分为一个sheet
    :param to_file: 写入文件名
    :param rows: 待写入数据，二维数组
    :param header: 列名
    :return:
    """
    row_num = len(rows)
    if row_num < 1:
        print("写入数据为空！")
    elif row_num > 1048575:
        if header == None:
            header = range(len(rows[0]))
        writer = pd.ExcelWriter(to_file)
        for i in range(0, len(rows), 1000000):
            rows_slice = rows[i:i + 1000000]
            df = pd.DataFrame(rows_slice)
            df.columns = header
            df.to_excel(writer, index=False, sheet_name=str(i + 1) + "-" + str(i + 1000000))
        writer.save()
    else:
        if header == None:
            header = range(len(rows[0]))
        writer = pd.ExcelWriter(to_file)
        df = pd.DataFrame(rows)
        df.columns = header
        df.to_excel(writer, index=False, sheet_name="sheet1")
        writer.save()


def write_rows2sheet(writer, rows, header, sheet_name="sheet1"):
    """
    写入数据到指定sheet，为了不同数据写入不同sheet，用户可以多次调用此方法
    :param writer: 预先定义好的writer
    :param rows: 待写入数据
    :param header: 列名
    :param sheet_name: sheet名
    :return:
    """
    df = pd.DataFrame(rows)
    df.columns = header
    df.to_excel(writer, index=False, sheet_name=sheet_name)


def get_sort_idx(vals):
    """
    :param vals: 输入数组数据
    :return: 数组排序的下标
    """
    return sorted(range(len(vals)), key=vals.__getitem__)


def get_sort_idx_by_np(vals):
    """
    :param vals: 输入数组数据
    :return: 数组排序的下标
    """
    return np.argsort(vals)


def reservoir_sampling(fin, k, sample_list):
    """
    蓄水池采样
    :param fin:待采样数组
    :param k:采样数量
    :return:采样好的结果数组
    """
    i = 0
    for x in fin:
        if i < k:
            sample_list.append(x)
        else:
            r = random.randint(0, i - 1)
            if r < k:
                sample_list[r] = x
        i += 1
    return sample_list


def json2doc(in_file, col_names, header, sep="\t"):
    """
    json文件转文本文件
    :param in_file: json文件路径
    :param col_names:读取json文件的指定键名 列表
    :param header: 列名
    :param sep: 分割符，tsv文件对应"\t"，csv文件对应","，默认输出tsv文件
    :return:
    """
    to_file = in_file.split(".")[0] + ".tsv"
    with open(in_file, encoding='utf-8') as fin, open(to_file, "w", encoding="utf-8") as fout:
        fout.write(header + "\n")
        instances = json.load(fin)
        for instance in instances:
            row = []
            for col_name in col_names:
                col = instance[col_name].strip() if instance[col_name] != None else ""
                row.append(col)
            line = sep.join(row)
            fout.write(line + "\n")
    print(to_file)

def save_json_file(instances, to_file):
    """
    :param instances:  [{"code": code, "name": name, ...}, {...}, ...]
    :param to_file:指定输出文件
    :return:
    """
    with open(to_file, "w", encoding='utf-8') as fout:
        json.dump(instances, fout, ensure_ascii=False, indent=2)

