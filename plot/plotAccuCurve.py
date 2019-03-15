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
accuRecords = []
for i in range(len(corpus)):
    line = corpus[i]
    if line != "":
        factorRecord = float(line.split("\t")[1])
        accuRecord = float(line.split("\t")[3])
        factorRecords.append(factorRecord)
        accuRecords.append(accuRecord)

# plt.plot(factorRecords)
plt.plot(accuRecords)
# plt.plot(records, '-.o')
plt.savefig("../out/3AccuCurve.png")
plt.title("accuracy curve")
plt.xlabel("population")
plt.ylabel("accuracy")
plt.show()
