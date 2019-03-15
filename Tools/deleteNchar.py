# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:32:42 2017

@author: 18201
"""

f = open("test.txt", "rb")
r = open("test.py", "w+")
corpus = bytes.decode(f.read()).split("\n")
line = f.readline()
for i in range(len(corpus)):
    s = corpus[i][5:]
    print(s)
    r.write(s + "\n")
    line = f.readline()
f.close()
r.close()
