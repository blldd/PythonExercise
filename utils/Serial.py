# -*- coding:UTF-8 -*-
import argparse
import pickle
import gc
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os

# 使用dump()将数据序列化到文件中
# fw = open('../out/paraFile.txt', 'wb')
# # Pickle the list using the highest protocol available.
# pickle.dump(paraList, fw, -1)
# fw.close()

# 使用load()将数据从文件中序列化读出
fr = open('../data/paraFileP.txt', 'rb')
data1 = pickle.load(fr)
print("%"*10)
print(data1)
fr.close()

with open('../data/paraFileP.txt', 'rb') as fr:
    data = pickle.load(fr)

    print(data)


'''
import json  
  
fw = open('test.txt', 'w')  
for i in xrange(10):  
    json.dump([i], fw)  
    print(>>fw #换行，便于阅读  )
fw.close()  
  
  
fp = open('test.txt')  
for line in fp:  
    #一是消除load文件到空的情况  
    #而是正好和上面的换行对应起来，便于阅读  
    lst = json.loads(line)  
    print(lst, type(lst)  )
fp.close()  
'''