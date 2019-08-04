# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/2 11:42 AM
@Author  : ddlee
@File    : pearson.py
"""
import numpy as np
from scipy.stats import pearsonr

np.random.seed(0)
size = 300
x = np.random.normal(0, 1, size)

# Pearson相关系数的一个明显缺陷是，作为特征排序机制，他只对线性关系敏感。
# 如果关系是非线性的，即便两个变量具有一一对应的关系，Pearson相关性也可能会接近 。

print("Lower noise", pearsonr(x, x + np.random.normal(0, 1, size)))
print("Higher noise", pearsonr(x, x + np.random.normal(0, 10, size)))