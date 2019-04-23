# -*- coding:UTF-8 -*-


import random
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/Library/Fonts/Songti.ttc')


def draw():
    # 定义热图的横纵坐标
    xLabel = ['A', 'B', 'C', 'D', 'E']
    yLabel = ['1', '2', '3', '4', '5']

    # 准备数据阶段，利用random生成二维数据（5*5）
    data = []
    for i in range(5):
        temp = []
        for j in range(5):
            k = random.randint(0, 100)
            temp.append(k)
        data.append(temp)

    # 作图阶段
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_yticks(range(len(yLabel)))
    ax.set_yticklabels(yLabel, fontproperties=font)
    ax.set_xticks(range(len(xLabel)))
    ax.set_xticklabels(xLabel)

    im = ax.imshow(data, cmap=plt.cm.hot_r)

    plt.colorbar(im)

    plt.title("This is a title中文", fontproperties=font)

    plt.show()


d = draw()

"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a random dataset
data = pd.DataFrame(np.random.random((10, 6)),
                    columns=["Iron Man", "CaptainAmerica", "BlackWidow", "Thor", "Hulk", "Hawkeye"])

print(data)

# Plot the heatmap
heatmap_plot = sns.heatmap(data, center=0, cmap='gist_ncar')

plt.show()


#cmap(颜色)
#
# f, (ax1,ax2) = plt.subplots(figsize = (6,4),nrows=2)
#
# # cmap用cubehelix map颜色
# cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
# sns.heatmap(data, linewidths = 0.05, ax = ax1, vmax=900, vmin=0, cmap=cmap)
# ax1.set_title('cubehelix map')
# ax1.set_xlabel('')
# ax1.set_xticklabels([]) #设置x轴图例为空值
# ax1.set_ylabel('kind')
#
# # cmap用matplotlib colormap
# sns.heatmap(data, linewidths = 0.05, ax = ax2, vmax=900, vmin=0, cmap='rainbow')
# # rainbow为 matplotlib 的colormap名称
# ax2.set_title('matplotlib colormap')
# ax2.set_xlabel('region')
# ax2.set_ylabel('kind')
"""