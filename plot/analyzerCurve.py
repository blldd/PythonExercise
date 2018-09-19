# -*- coding:UTF-8 -*-

import argparse
import pickle
import gc
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os,sys

f = open("../out/3paraResult.txt",'rb')
corpus = bytes.decode(f.read()).split("\n")

factorRecords = []
for i in range(len(corpus)):
    line = corpus[i]
    if line != "":
        factorRecord = float(line.split("\t")[0])
        factorRecords.append(factorRecord)

plt.scatter(list(range(len(factorRecords))), factorRecords)
# plt.plot(records, '-.o')
plt.savefig("../out/3analyzerCurve.png")
plt.title("Analyzer Scatter")
plt.xlabel("population")
plt.ylabel("analyzer")
plt.show()
