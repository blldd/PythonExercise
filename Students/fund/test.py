# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/20 8:45 AM
@Author  : ddlee
@File    : test.py
"""
import pandas as pd


# a = pd.Series([12,2,59,9,10])
# print(a)
# index = a.argsort()
# print(index)
# print(a.take(index))


from pandas import DataFrame
import pandas as pd
import numpy as np

df = DataFrame(np.random.randn(4, 5), columns=["A", "B", "C", "D", "E"])

print(df)

df["Col_sum"] = df.apply(lambda x: x.sum(), axis=1)
print(df)

df.loc["Row_sum"] = df.apply(lambda x: x.sum())
print(df)
