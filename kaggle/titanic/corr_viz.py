# -*- coding: utf-8 -*-
# @ 2019-07-29
# @ Li Dedong

import json
import os
import logging
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("train.csv")

# plt.figure(figsize=(12, 10))
# foo = sns.heatmap(train.drop('PassengerId', axis=1).corr(), vmax=0.6, square=True, annot=True)
# plt.show()

# plt.figure(figsize=(18, 10))
# cols = ['Survived','Pclass','Age','SibSp','Parch','Fare']
# g = sns.pairplot(data=train.dropna(), vars=cols, size=1.5,
#                  hue='Survived')
# g.set(xticklabels=[])
# plt.savefig("corr")
# plt.show()


# #使用pairplot看不同特征维度pair下数据的空间分布状况
# plt.figure(figsize=(18, 10))
# _=sns.pairplot(train[:50],hue="Pclass",size=1.5)
# plt.savefig("corr")
# plt.show()

plt.figure(figsize=(12,10))
_=sns.corrplot(train,annot=False)
plt.show()
