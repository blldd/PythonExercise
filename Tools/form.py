# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:22:47 2018

@author: L
"""
import os,sys
import numpy as np

f = open("paraResult.txt",'rb')
r = open("paraResultP.txt","w+")
corpus = bytes.decode(f.read()).split("\n")

for i in range(len(corpus)):
    words = corpus[i]
    if words != "":
        
        word_list = words.split("\t")
        try:
            tmp = int(np.ceil(float(word_list[0])*4))
        except ValueError:
            print("error on line %d",(i))
        r.write(str(tmp) + '\t')
        
        r.write(word_list[1] + '\t' + word_list[2] + '\t' + word_list[3])
        r.write('\n')
r.close()
f.close()