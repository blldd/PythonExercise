# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/21 9:18 AM
@Author  : ddlee
@File    : pca.py
"""

# 在numpy中实现PCA
# 伪代码
"""
去除平均值
计算协方差矩阵
计算协方差矩阵的特征值和特征向量
将特征值从大到小排序
保留最上面的N个特征向量
将数据转换到上述N个特征向量构建的新空间中
"""
from numpy import *


def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = []
    for line in stringArr:
        datArr.append(list(map(lambda x: float(x), line)))
    return mat(datArr)


# dataMat是用于进行PCA操作的数据集
# topNfeat是可选参数,即应用的N个特征,如果不指定topNfeat的值,那么函数就会返回前9999999个特征,或者原始数据中全部的特征
def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    # 去平均值
    meanRemoved = dataMat - meanVals

    # 计算协方差矩阵
    covMat = cov(meanRemoved, rowvar=0)
    # 计算特征向量和特征值
    eigVals, eigVects = linalg.eig(mat(covMat))
    # 从小到达对N个值排序
    eigValInd = argsort(eigVals)
    # cut off unwanted dimensions
    eigValInd = eigValInd[:-(topNfeat + 1):-1]
    # reorganize eig vects largest to smallest
    redEigVects = eigVects[:, eigValInd]

    # transform data into new dimensions
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


dataMat = loadDataSet('testSet.txt')
lowDMat, reconMat = pca(dataMat, 1)
shape(lowDMat)
# (1000, 1)
# 如果使用如下命令来替换原来的PCA调用
# lowDMat, reconMat = pca(dataMat, 2)
# 即没有剔除任何特征,那么重构之后的数据会和原始数据重合
