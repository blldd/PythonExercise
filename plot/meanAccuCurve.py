# -*- coding:UTF-8 -*-

import argparse
import pickle
import gc
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os,sys
import matplotlib.ticker as mtick

f = open("../out/3paraResult.txt",'rb')
corpus = bytes.decode(f.read()).split("\n")

factorRecords = []
accuRecords = []
for i in range(len(corpus)):
    line = corpus[i]
    if line != "":
        factorRecord = float(line.split("\t")[1])
        accuRecord = float(line.split("\t")[3])
        factorRecords.append(factorRecord)
        accuRecords.append(accuRecord)

meanRecords = [0]*30
meanRecord = 0
cnt = 0
for rec in accuRecords:
    index = int(cnt/20)
    # tmp = rec/20
    tmp = rec / 20
    meanRecords[index] += tmp
    cnt += 1
print(cnt)
# plt.plot(factorRecords)
plt.plot(meanRecords)
# plt.plot(records, '-.o')
plt.savefig("../out/2MeanAccuCurve.png")
plt.title("mean accuracy curve")
ax = plt.gca()  # 获取当前图像的坐标轴信息
# ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
fmt='%.2f'
yticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(yticks)

plt.xlabel("generation")
plt.ylabel("mean accuracy(%)")
plt.show()
