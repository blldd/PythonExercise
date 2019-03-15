#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import pickle
import pandas as pd

df = pd.read_excel("E:\\Workspace\\PyCharm\\PythonExercise\\Tools\\trace_data.xls")
print(df)
print(df.keys())

writer = pd.ExcelWriter('output.xlsx')
df1 = pd.DataFrame(data={'col1': [1, 1], 'col2': [2, 2]})
df1.to_excel(writer, 'Sheet1')
writer.save()

# for iter in range(10):
#     s1 = "\r[%s%s]%0.2f%%" % ("*" * iter, " " * (10 - iter), iter * 100.0 / (10 - 1))
#     sys.stdout.write(s1)
#     # sys.stdout.flush()
#     time.sleep(1)
#
#
# with open('../dblp/unnormemb_v.pkl', 'rb') as f:
#     data = pickle.load(f)
#
# for i in data.keys():
#     print(i, data[i])
