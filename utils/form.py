# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:22:47 2018

@author: L
"""
import os, sys
import numpy as np

f = open("../data/3paraResultRaw.txt", 'rb')
r = open("../out/3paraResult.txt", "w+")
corpus = bytes.decode(f.read()).split("\n")

for i in range(len(corpus)):
    words = corpus[i]
    if words:

        word_list = words.split("\t")
        try:
            tmp = int(np.ceil(float(word_list[0]) * 4))
        except ValueError:
            print("error on line %d", (i))

        word_list[0] = str(tmp)
        r.write('\t'.join(word_list))
        r.write('\n')
r.close()
f.close()