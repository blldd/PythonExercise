# -*- coding:UTF-8 -*-
import numpy as np
import scipy.io as sio
import sklearn
import xlrd
import matplotlib.pyplot as plt
import xlsxwriter
import random
from mpl_toolkits.mplot3d import Axes3D
import json


def _read_excel_file(in_file):
    trace_pos_arr = []
    data = xlrd.open_workbook(in_file)
    for table in data.sheets():
        nrows = table.nrows
        for i in range(nrows):
            if i == 0:
                continue
            row = table.row_values(i)
            # Convert all values to unicode.
            # row = map(unicode, row)
            trace_id, trace_x, trace_y, trace_z = int(row[0]), int(row[1]), int(row[2]), int(row[3])

            # yield (trace_id, trace_x, trace_y, trace_z)
            trace_pos_arr.append([trace_x, trace_y, trace_z])
    return trace_pos_arr


def _write2excel(traces, to_file):
    workbook = xlsxwriter.Workbook(to_file)
    sheet = workbook.add_worksheet()
    idx = 0
    time = 0
    idx = _write_row_in_sheet(idx, ["x", "y", "z"], sheet, time)
    for trace in traces:
        if trace is None:
            continue
        print(trace)
        print(len(trace))

        org_1 = trace[0][0]
        org_2 = trace[0][1]
        org_3 = trace[0][2]
        time = trace[0][3]
        row = [org_1, org_2, org_3]

        idx = _write_row_in_sheet(idx, row, sheet, time)
    workbook.close()

def _write2excel2(traces, to_file):
    workbook = xlsxwriter.Workbook(to_file)
    sheet = workbook.add_worksheet()
    idx = 0
    time = 0
    idx = _write_row_in_sheet(idx, ["x", "y", "z"], sheet, time)

    for trace in traces:
        row = []
        for i in range(len(trace)):
            org = trace[i]
            row.append(org)
        idx = _write_row_in_sheet(idx, row, sheet, time)
    workbook.close()

def _write2excel3(traces, to_file):
    workbook = xlsxwriter.Workbook(to_file)
    sheet = workbook.add_worksheet()
    idx = 0
    time = 0
    idx = _write_row_in_sheet(idx, ["x", "y", "z"], sheet, time)

    for trace in traces:
        print(trace)
        idx = _write_row_in_sheet2(idx, trace, sheet, time)
    workbook.close()

def _write_row_in_sheet2(row_index, trace, sheet, time, format=None):
    for j in range(len(trace)):
        row = trace[j][:3]
        time = trace[j][-1]
        for i, item in enumerate(row):
            sheet.write(row_index, time * 3 + 1 + i, round(item, 1), format)
    return row_index + 1

def _write_row_in_sheet(row_index, row, sheet, time, format=None):
    for i, item in enumerate(row):
        sheet.write(row_index, time * 3 + 1 + i, item, format)
    return row_index + 1


def _rw_excel_file(in_file, to_file):
    trace_pos_arr = []
    data = xlrd.open_workbook(in_file)
    for table in data.sheets():
        nrows = table.nrows
        for i in range(nrows):
            if i == 0:
                continue
            row = table.row_values(i)
            row_out = []
            for j in range(len(row)):
                if row[j] == "":
                    row_out.append(row[j])

                else:
                    print(row[j])
                    tmp = round(row[j], 1)
                    row_out.append(tmp)
            # trace_id, trace_x, trace_y, trace_z = int(row[0]), int(row[1]), int(row[2]), int(row[3])

            # yield (trace_id, trace_x, trace_y, trace_z)
            trace_pos_arr.append(row_out)

    workbook = xlsxwriter.Workbook(to_file)
    sheet = workbook.add_worksheet()
    idx = 0
    time = 0
    idx = _write_row_in_sheet(idx, ["x", "y", "z"], sheet, time)

    for trace in trace_pos_arr:
        print(trace)
        idx = _write_row_in_sheet(idx, trace, sheet, time)
    workbook.close()



if __name__ == '__main__':
    in_file = "result1.xlsx"
    out_file = "E18102690098_1.xlsx"
    _rw_excel_file(in_file, out_file)


    """  
    # read
    fake_trace = _read_excel_file("fake_trace.xls")
    print(fake_trace)
    traces_res = []
    trace_res = []
    for k in range(4):
        for i in range(len(fake_trace)):
            for j in range(3):
                random.seed(9)
                tmp = fake_trace[i][j] + round(1000 * np.random.randn(), 1)
                trace_res.append(tmp)
        traces_res.append(trace_res)
        print(trace_res)


    _write2excel2(traces_res, "result2.xlsx")

    """

    """
    xyz = []
    # for i in range(2, 1037):
    #     dataFile = 'schedual_9/data_%s.mat' % (i)
    #     data = sio.loadmat(dataFile)["savedata"]['x'][0][0][100:].reshape(9, 20)
    #     # print(data)
    #     # data = sio.loadmat(dataFile)["savedata"]['y'][0][0].reshape(1, 4)[0]
    #     data = list(data)
    #     xyz.append(data)
    # # xyz.sort(key=lambda x: x[2])  # 雷达个数大于3
    # print(xyz)
    # cnt = 0
    #
    # for i in range(len(xyz)):
    #     if xyz[i][2] == 0:
    #         cnt += 1
    #     else:
    #         break
    # xyz = xyz[:cnt]
    # xyz.sort(key=lambda x: (x[1],x[0]))
    # xyz.sort(key=lambda x: (x[0]))
    # xyz = xyz[0]
    # print(xyz)

    dataFile = 'schedual_9/data_58.mat'
    data = sio.loadmat(dataFile)["savedata"]['x'][0][0][100:].reshape(9, 20)
    data_dots_x = sio.loadmat(dataFile)["savedata"]['dots'][0][0][0][0][0]
    data_dots_y = sio.loadmat(dataFile)["savedata"]['dots'][0][0][0][0][1]
    data_dots_z = sio.loadmat(dataFile)["savedata"]['dots'][0][0][0][0][2]
    # print(data_dots_x)

    # fig = plt.figure(figsize=(10, 7))
    # ax = fig.add_subplot(111, projection='3d')
    # ax.set_xlabel('X (km)')
    # ax.set_ylabel('Y (km)')
    # ax.set_zlabel('Z (km)')

    traces = []
    for i in range(9):
        tmp = []
        p = []
        chk = -1
        for j in range(20):
            index = int(data[i][j])
            if index >= 1 and index <= 5:
                index -= 1
                tmp.append([data_dots_x[index][j], data_dots_y[index][j], data_dots_z[index][j], j])
                if chk == j:
                    continue
                chk = j
        print(tmp)
        traces.append(tmp)

    _write2excel3(traces, "result3.xlsx")
    """
    # p1 = path[0][:3]+[path[0][-1]]
    # x = [k[0] for k in p1]
    # y = [k[1] for k in p1]
    # z = [k[2] for k in p1]
    # ax.plot(x, y, z, color='b', label='UAV Trajectory 1')
    #
    # p2 = path[1][:3] + [path[1][-1]]
    # x = [k[0] for k in p2]
    # y = [k[1] for k in p2]
    # z = [k[2] for k in p2]
    # ax.plot(x, y, z, color='g', label='UAV Trajectory 2')

    # x = [k[0] for k in radar_pos_arr]
    # y = [k[1] for k in radar_pos_arr]
    # z = [k[2] for k in radar_pos_arr]
    # for cnt, (i, j, k) in enumerate(zip(x, y, z)):
    #     label = 'radar %d' % (cnt + 1)
    #     ax.text(i, j, k, label)
    #
    # ax.scatter(x, y, z, c='r', label='Radar Position')
    # ax.legend()

    # plt.savefig("path", dpi=520)
    # plt.show()
