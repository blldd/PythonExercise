# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/22 2:16 PM
@Author  : ddlee
@File    : auc_scipy.py
"""

from sklearn import metrics
import numpy as np


def auc_fun(true, pred):
    fpr, tpr, thresholds = metrics.roc_curve(true, pred, pos_label=1)
    print(fpr)
    print(tpr)
    return metrics.auc(fpr, tpr)


true = np.array([1, 1, 0, 0, 1])
pred = np.array([0.5, 0.6, 0.55, 0.4, 0.7])
print(auc_fun(true, pred))
