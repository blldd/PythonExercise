# -*- coding:UTF-8 -*-
import scipy.io as sio
import sklearn
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


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


def function_plot():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    COS = np.cos(X)
    EXP = 1 - np.exp(X - 1)
    COM = 1 - np.exp(COS - 1)

    fig = plt.figure(figsize=(20, 7))
    plt.subplot(131)
    plt.plot(X, COS, label='cos(x)', linewidth='3')
    plt.fill_between(X, COS, where=(0 < X) & (X < np.pi), facecolor='#acc2d9')
    # plt.xlim(-np.pi, np.pi)
    # plt.xlabel(u"x")
    # plt.ylabel(u"y")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, which='major')
    plt.legend(fontsize=14)

    plt.subplot(132)
    plt.plot(X, EXP, label='1 - np.exp(x - 1)', linewidth='3')
    # plt.xlim(-np.pi, np.pi)
    # plt.ylim(-8, 2)
    # plt.xlabel(u"x")
    # plt.ylabel(u"y")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, which='major')
    plt.legend(fontsize=14)

    plt.subplot(133)
    plt.plot(X, COM, label='1 - np.exp(cos(x) - 1)', linewidth='3')
    plt.fill_between(X, COM, where=(0 < X) & (X < np.pi), facecolor='#acc2d9')
    # plt.xlim(-np.pi, np.pi)
    # plt.xlabel(u"x")
    # plt.ylabel(u"y")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, which='major')
    plt.legend(fontsize=14)

    # plt.savefig('function_fig.png', dpi=520)
    # plt.savefig('function_fig.eps')
    plt.show()


def angle_plot(angle_path):
    radar_pos_arr = [[80, 0, 0], [30, 60, 0], [55, 110, 0], [105, 110, 0], [130, 60, 0]]
    trace_pos_arr = [[21, 32, 22], [55, 72, 22], [89, 65, 22], [120, 105, 22]]

    # fig = plt.figure(figsize=(18, 7))
    # ax = fig.add_subplot(131, projection='3d')
    fig = plt.figure(figsize=(10, 7))
    # plt.title('Minimize Number of UAV Solution')
    ax = fig.add_subplot(111, projection='3d')

    x = [k[0] for k in trace_pos_arr]
    y = [k[1] for k in trace_pos_arr]
    z = [k[2] for k in trace_pos_arr]

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.plot(x, y, z, c='g', label='UAV Trajectory')

    x = [k[0] for k in trace_pos_arr]
    y = [k[1] for k in trace_pos_arr]
    z = [k[2] for k in trace_pos_arr]

    for cnt, (i, j, k) in enumerate(zip(x, y, z)):
        label = 'position %d' % (cnt)
        ax.text(i - 10, j, k, label)
    ax.text(40, 36, 22, "line 1")
    ax.text(63, 66, 21.8, "line 2")
    ax.text(90, 100, 21.8, "line 3")

    ax.scatter(x, y, z, c='r', label='UAV Position')
    ax.legend()

    plt.savefig(angle_path, dpi=520)
    plt.show()


def trajectory_plot(trajectory_path):
    radar_pos_arr = [[80, 0, 0], [30, 60, 0], [55, 110, 0], [105, 110, 0], [130, 60, 0]]
    trace_pos_arr = [[21, 32, 22], [55, 72, 22], [89, 65, 22], [120, 105, 22]]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x = [k[0] for k in trace_pos_arr]
    y = [k[1] for k in trace_pos_arr]
    z = [k[2] for k in trace_pos_arr]
    for cnt, (i, j, k) in enumerate(zip(x, y, z)):
        label = 'moment %d' % (cnt + 1)
        ax.text(i, j, k, label)

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.scatter(x, y, z, c='g', label='UAV Trajectory')

    x = [k[0] for k in radar_pos_arr]
    y = [k[1] for k in radar_pos_arr]
    z = [k[2] for k in radar_pos_arr]
    for cnt, (i, j, k) in enumerate(zip(x, y, z)):
        label = 'radar %d' % (cnt + 1)
        ax.text(i, j, k, label)

    ax.scatter(x, y, z, c='r', label='Radar Position')
    ax.legend()

    plt.savefig(trajectory_path, dpi=520)
    plt.show()


def trajectory_plot2(trajectory_path):
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # COS = np.cos(X)
    radar_pos_arr = [[30, 0], [55, 0], [80, 0], [105, 0], [130, 0]]
    trace_pos_arr = [[21, 52], [89, 65], [140, 70]]
    x = [k[0] for k in trace_pos_arr]
    y = [k[1] for k in trace_pos_arr]
    fig = plt.figure(figsize=(10, 7))
    plt.scatter(x, y, label='trace position', linewidth='2')
    for cnt, (i, j) in enumerate(zip(x, y)):
        plt.annotate("moment %d" % (cnt + 1), xy=(i, j))

    x = [k[0] for k in radar_pos_arr]
    y = [k[1] for k in radar_pos_arr]
    plt.scatter(x, y, label='radar position', linewidth='2')
    for cnt, (i, j) in enumerate(zip(x, y)):
        plt.annotate("radar %d" % (cnt + 1), xy=(i, j))

    mid_x = []
    mid_y = []
    for s in range(0, 3):
        for i in range(s, s+3):
            mid_x.append((radar_pos_arr[i][0] + trace_pos_arr[s][0]) / 2.0)
            mid_y.append((radar_pos_arr[i][1] + trace_pos_arr[s][1]) / 2.0)
    plt.scatter(mid_x, mid_y, label='UAV position', color='b')
    for cnt, (i, j) in enumerate(zip(mid_x, mid_y)):
        plt.annotate("UAV %d" % (cnt + 1), xy=(i, j))


    for s in range(3):
        for i in range(s, s + 3):
            # i = random.randint(0, 2)
            x = [radar_pos_arr[i][0], trace_pos_arr[s][0]]
            y = [radar_pos_arr[i][1], trace_pos_arr[s][1]]
            if s == 0:
                c = 'r'
            elif s == 1:
                c = 'g'
            else:
                c = 'b'
            plt.plot(x, y, color=c)

    # plt.fill_between(X, COS, where=(0 < X) & (X < np.pi), facecolor='#acc2d9')
    # plt.xlim(-np.pi, np.pi)
    # plt.xlabel(u"x")
    # plt.ylabel(u"y")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, which='major')
    plt.legend(fontsize=14)

    plt.savefig(trajectory_path, dpi=520)
    plt.savefig('trajectory_fig2.eps')
    plt.show()


def trajectory_plot3(trajectory_path):
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # COS = np.cos(X)
    radar_pos_arr = [[30, 0], [55, 0], [80, 0], [105, 0], [130, 0]]
    trace_pos_arr = [[21, 52], [55, 72], [89, 65]]
    x = [k[0] for k in trace_pos_arr]
    y = [k[1] for k in trace_pos_arr]
    fig = plt.figure(figsize=(10, 7))
    plt.scatter(x, y, label='trajectory', linewidth='2')
    for cnt, (i, j) in enumerate(zip(x, y)):
        plt.annotate("moment %d" % (cnt + 1), xy=(i, j), fontsize=14)

    x = [k[0] for k in radar_pos_arr]
    y = [k[1] for k in radar_pos_arr]
    plt.scatter(x, y, label='radar position', linewidth='2')
    for cnt, (i, j) in enumerate(zip(x, y)):
        plt.annotate("radar %d" % (cnt + 1), xy=(i, j))

    for s in range(2):
        for i in range(s, s + 3):
            # i = random.randint(s, s + 3)
            x = [radar_pos_arr[i][0], trace_pos_arr[s][0], 2 * trace_pos_arr[s][0] - radar_pos_arr[i][0]]
            y = [radar_pos_arr[i][1], trace_pos_arr[s][1], 2 * trace_pos_arr[s][1] - radar_pos_arr[i][1]]
            if s == 0:
                c = 'r'
            elif s == 1:
                c = 'g'
            else:
                c = 'b'
            plt.plot(x, y, color=c)

    uav_x = [26.5, 37, 36, 55, 66, 70]
    uav_y = [20, 28, 39, 30, 40, 50]
    plt.scatter(uav_x, uav_y, label='uav position', linewidth='2')
    plt.scatter([50], [40], label='uav1 moment 1 position', linewidth='2')
    plt.scatter([10], [69], label='moment 1\'', linewidth='2')
    plt.annotate("moment 1'", xy=(10, 69), fontsize=14)

    x = [radar_pos_arr[3][0], 50, 2 * 50 - radar_pos_arr[3][0]]
    y = [radar_pos_arr[3][1], 40, 2 * 40 - radar_pos_arr[3][1]]
    plt.plot(x, y, color='y')
    plt.plot([70, 50], [50, 40], ':', color='b', label='uav1 trace at moment 1 2')
    #
    # for i in range(1, 4):
    #     # i = random.randint(1, 3)
    #     x = [radar_pos_arr[i][0], trace_pos_arr[1][0]]
    #     y = [radar_pos_arr[i][1], trace_pos_arr[1][1]]
    #     plt.plot(x, y, color='g')

    # plt.fill_between(X, COS, where=(0 < X) & (X < np.pi), facecolor='#acc2d9')
    # plt.xlim(-np.pi, np.pi)
    # plt.xlabel(u"x")
    # plt.ylabel(u"y")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, which='major')
    plt.legend(fontsize=14)

    plt.savefig(trajectory_path, dpi=520)
    plt.savefig('trajectory_fig3.eps')
    plt.show()


if __name__ == '__main__':
    angle_path = "angle_fig.png"
    trajectory_path2 = "trajectory_fig2.png"
    trajectory_path3 = "trajectory_fig3.png"

    function_plot()
    # angle_plot(angle_path)
    # trajectory_plot2(trajectory_path2)
    # trajectory_plot3(trajectory_path3)
