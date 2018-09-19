# -*- coding:UTF-8 -*-

import argparse
import pickle
import gc
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os,sys

f = open("../out/2paraResult.txt",'rb')
corpus = bytes.decode(f.read()).split("\n")

scale = (1+26)*13
accuRe99s = []
accuRe95s = []
accuRe93s = []
accuRe90s = []
accuRe85s = []
fitRecords = []
for i in range(len(corpus)):
    line = corpus[i]
    if line != "":
        accuRe99 = float(line.split("\t")[-1])
        accuRe95 = float(line.split("\t")[-5])
        accuRe93 = float(line.split("\t")[-7])
        accuRe90 = float(line.split("\t")[-10])
        accuRe85 = float(line.split("\t")[-15])
        fitRecord = float(line.split("\t")[3])/scale
        accuRe99s.append(accuRe99)
        accuRe95s.append(accuRe95)
        accuRe93s.append(accuRe93)
        accuRe90s.append(accuRe90)
        accuRe85s.append(accuRe85)
        fitRecords.append(fitRecord)

plt.plot(accuRe99s)
plt.plot(accuRe95s)
plt.plot(accuRe93s)
plt.plot(accuRe90s)
plt.plot(accuRe85s)
plt.plot(fitRecords)
# plt.plot(records, '-.o')
plt.savefig("../out/2AccuCurve.png")
plt.title("accuracy curve")
plt.xlabel("population")
plt.ylabel("accuracy")
plt.show()
