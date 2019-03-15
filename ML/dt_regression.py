# -*- coding:UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


# 求得mat的最后一列，也就是目标值的平均值
def regLeaf(mat):
    return np.mean(mat[:, -1])


# 定义误差计算方法：mat最后一列（目标值）的方差乘以个数
def regErr(mat):
    return np.var(mat[:, -1]) * np.shape(mat[:, -1])[0]
    # 生成回归决策树，给出一个元参数：


# 第一个表示分割后误差下降的大小未超过此值，直接作为叶节点输出（带有目标值）
# 第二个参数表示某个节点内含有的节点个数，必须大于这个值，才会进一步分裂
def decisionTreeRegressor(dataSet, ops=(0.0001, 3)):
    feat, val = chooseBestSplit(dataSet, regLeaf, regErr, ops)
    if feat == None:
        return val
    retTree = {}
    retTree['spIndex'] = feat
    retTree['spValue'] = val
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = self.createTree(lSet, leafType, regErr, ops)
    retTree['right'] = self.createTree(rSet, leafType, regErr, ops)
    return retTree


# 根据最佳索引和取值，将数据集分开
def binSplitDataSet(dataSet, bestIndex, bestValue):
    mat0 = dataSet[np.array(dataSet)[:, bestIndex] < bestValue]
    mat1 = dataSet[np.array(dataSet)[:, bestIndex] >= bestValue]
    return mat0, mat1


# 选择最佳切分属性及其对应的属性值
# 所有的属性遍历后，如果误差减少不大，生成叶子节点
# 得到叶节点的条件有3个，标红色的代码
def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(0.0001, 3)):
    tolS = ops[0]
    tolN = ops[1]
    # 所有的样本对应的目标值都相等，则
    if len(set(dataSet[:, -1].T.tolist())) == 1:
        return None, leafType(dataSet)
    m, n = np.shape(dataSet)
    S = errType(dataSet)
    bestS = np.inf
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n):
        for splitVal in set(dataSet[:, featIndex]):
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            # 这个条件约束了分割后的区间长度都不能小于tolN
            if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
                continue
            # 求出分割后的两部分均方误差的和
            newS = errType(mat0) + errType(mat1)
            # 如果newS更小，则让它成为bestS
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    # 说明误差下降的不大
    if S - bestS < tolS:
        return None, leafType(dataSet)
    # 根据最优特征和其对应的取值划分数据集
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    # 满足这种情况，只能是所有的样本点个数小于tolN
    # 此时只给出当前样本的均方误差
    if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
        return None, leafType(dataSet[:, bestIndex])
    return bestIndex, bestValue


def viz():
    # 导入iris数据集
    from sklearn.datasets import load_iris
    from sklearn import tree
    iris = load_iris()
    # 创建决策树分类器
    clf = tree.DecisionTreeClassifier()
    # 训练
    clf = clf.fit(iris.data, iris.target)
    # graphviz 可视化树
    import graphviz
    dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=iris.feature_names,
                                    class_names=iris.target_names,
                                    filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)


if __name__ == '__main__':
    # decisionTreeRegressor()
    viz()
