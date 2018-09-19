# -*- coding:UTF-8 -*-
import scipy.io as sio
import sklearn
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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


if __name__ == '__main__':

    dataFile = 'data_ 22.mat'
    data = sio.loadmat(dataFile)["savedata"]
    print(data.shape)
    print(data)
    #
    # in_file = "trace_data.xls"
    # radar_pos_arr = [[80, 0, 0], [30, 60, 0], [55, 110, 0], [105, 110, 0], [130, 60, 0]]
    # trace_pos_arr = _read_excel_file(in_file)
    #
    # # fig = plt.figure(figsize=(18, 7))
    # # ax = fig.add_subplot(131, projection='3d')
    # fig = plt.figure(figsize=(10, 7))
    # # plt.title('Minimize Number of UAV Solution')
    # ax = fig.add_subplot(111, projection='3d')
    #
    # X = np.arange(-4, 4, 0.25)
    # Y = np.arange(-4, 4, 0.25)
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    #
    # x = [k[0] / 1000 for k in trace_pos_arr]
    # y = [k[1] / 1000 for k in trace_pos_arr]
    # z = [k[2] / 1000 for k in trace_pos_arr]
    #
    # ax.set_xlabel('X (km)')
    # ax.set_ylabel('Y (km)')
    # ax.set_zlabel('Z (km)')
    # # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    # ax.plot(x, y, z, c='g', label='UAV Trajectory')
    #
    # x = [k[0] for k in radar_pos_arr]
    # y = [k[1] for k in radar_pos_arr]
    # z = [k[2] for k in radar_pos_arr]
    # # # 遍历每一个点，使用text将y值显示
    # # for i, j in zip(x, y):
    # #     ax.annotate("%d" % (i), xy=(i, j))
    #
    # for i, j, k in zip(x, y, z):
    #     label = '(%d, %d, %d)' % (i, j, k)
    #     ax.text(i, j, k, label)
    #
    # ax.scatter(x, y, z, c='r', label='Radars Position')
    # ax.legend()
    #
    # plt.show()
