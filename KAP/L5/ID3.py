# -*- coding: utf-8 -*-
"""
Created on Wed Nov  21 18:28:53 2017

@author: Don
"""

import re
import time
from math import log
import operator
import numpy as np
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier

from Pre.Vectorize import Vector

def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None

class ID3(object):
    def __init__(self):
        self.W = np.zeros(1)

    def __getattr__(self, item):
        pass

    def calcShannonEnt(dataSet):
        numEntries = len(dataSet)
        labelCounts = {}
        for featVec in dataSet:  # the the number of unique elements and their occurance
            currentLabel = featVec[-1]
            if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / numEntries
            shannonEnt -= prob * log(prob, 2)  # log base 2
        return shannonEnt

    def splitDataSet(dataSet, axis, value):
        retDataSet = []
        for featVec in dataSet:
            if featVec[axis] == value:
                reducedFeatVec = featVec[:axis]  # chop out axis used for splitting
                reducedFeatVec.extend(featVec[axis + 1:])
                retDataSet.append(reducedFeatVec)
        return retDataSet

    def chooseBestFeatureToSplit(dataSet):
        numFeatures = len(dataSet[0]) - 1  # the last column is used for the labels
        baseEntropy = ID3.calcShannonEnt(dataSet)
        bestInfoGain = 0.0;
        bestFeature = -1
        for i in range(numFeatures):  # iterate over all the features
            featList = [example[i] for example in dataSet]  # create a list of all the examples of this feature
            uniqueVals = set(featList)  # get a set of unique values
            newEntropy = 0.0
            for value in uniqueVals:
                subDataSet = ID3.splitDataSet(dataSet, i, value)
                prob = len(subDataSet) / float(len(dataSet))
                newEntropy += prob * ID3.calcShannonEnt(subDataSet)
            infoGain = baseEntropy - newEntropy  # calculate the info gain; ie reduction in entropy
            if (infoGain > bestInfoGain):  # compare this to the best gain so far
                bestInfoGain = infoGain  # if better than current best, set to best
                bestFeature = i
        return bestFeature  # returns an integer

    def majorityCnt(classList):
        classCount = {}
        for vote in classList:
            if vote not in classCount.keys(): classCount[vote] = 0
            classCount[vote] += 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    def createTree(dataSet, labels):
        classList = [example[-1] for example in dataSet]
        #print(classList)
        if classList.count(classList[0]) == len(classList):
            return classList[0]                      # stop splitting when all of the classes are equal
        if len(dataSet[0]) == 1:                     # stop splitting when there are no more features in dataSet
            return ID3.majorityCnt(classList)
        bestFeat = ID3.chooseBestFeatureToSplit(dataSet)
        bestFeatLabel = labels[bestFeat]
        myTree = {bestFeatLabel: {}}
        del (labels[bestFeat])
        featValues = [example[bestFeat] for example in dataSet]
        uniqueVals = set(featValues)
        for value in uniqueVals:
            subLabels = labels[:]  # copy all of labels, so trees don't mess up existing labels
            myTree[bestFeatLabel][value] = ID3.createTree(ID3.splitDataSet(dataSet, bestFeat, value), subLabels)
        return myTree

    """利用决策树判断新数据点"""

    def classify(inputTree, featLabels, testVec):
        firstSides = list(inputTree.keys())             # 第一个分类特征
        firstStr = firstSides[0]                        # 找到输入的第一个元素
        #print(featLabels)
        #print(firstSides)
        secondDict = inputTree[firstStr]                # 二级字典
        #print(firstStr)
        #print(featLabels)
        #featIndex = featLabels.index('7')
        #print(featIndex)
        featIndex = featLabels.index(firstStr)          # 当前特征值在数据集的位置,返回时索引
        key = testVec[featIndex]                        # 拿到新数据点的当前特征的特征值
        valueOfFeat = secondDict.get(key)                   # 根据特征值 划分数据点
        if isinstance(valueOfFeat, dict):               # 如果不是叶节点，迭代；
            classLabel = ID3.classify(valueOfFeat, featLabels, testVec)
        else:
            classLabel = valueOfFeat                    # 如果是叶节点，返回标签类
        return classLabel

    def train(self, X, Y, k):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        m, n = np.shape(X_)
        I = np.eye(n)
        print("X_ : ")
        print(X_)
        self.W = np.dot(np.dot(np.linalg.pinv(np.add(np.dot(X_.T, X_), k * I)), X_.T), Y)       #

    def predict(self, X):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        return np.dot(X_, self.W)

if __name__ == '__main__':
    QID_LIST = list(range(201, 210))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    with open('F:/ECNU/Course/KnowledgeAna/results/ID3.res', 'a') as res:
        MAE_TOTAL = 0
        for QID in QID_LIST:
            print('ID3 for query ' + QID)


            #lasso = Lasso()
            vector = Vector(QID)
            word, weight, idx = vector.get_vector()
            print('PCA...')
            print('dimension: ' + str(weight.shape[1]))
            PCA_start_t = time.time()
            pca = PCA(n_components=10)
            weight = pca.fit_transform(weight)
            PCA_end_t = time.time()
            print('new dimension: ' + str(weight.shape[1]))
            print('PCA time: %d' % (PCA_end_t - PCA_start_t))

            # tag_data_set    train
            train_set = dict()
            f = line_reader('F:/ECNU/Course/KnowledgeAna/tag_data_set/' + QID + '/train_set')
            line = next(f)                                  #    next(iterator[, default])    Return the next item from the iterator.
            d = len(weight[0])
            print('loading taged training set...')
            cnt = 0
            while line:
                content = re.split('\s+', line)
                doc = content[0]
                score = float(content[1])
                train_set.setdefault(doc, score)
                if cnt == 0:
                    X_train = np.array(weight[idx[doc]]).reshape(cnt+1, d)
                    Y_train = np.array([score]).reshape(cnt+1, 1)
                else:
                    X_train = np.concatenate((X_train, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(cnt+1, d)
                    Y_train = np.concatenate((Y_train, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
                cnt += 1
                line = next(f)

            # X_train_PCA =

            print('training...')
            train_start_t = time.time()
            #lasso.train(X_train, Y_train)                                                        #train
            #call sklearn.Lasso()
            #trainDataSet = np.concatenate((X_train, Y_train), axis=1)
            trainDataSet = np.hstack((X_train, Y_train))
            featureNum = len(X_train[1])
            labels = list(range(0, featureNum))
            labels = list(map(lambda x: str(x), labels))
            #print(labels)
            ID3Tree = ID3.createTree(trainDataSet.tolist(), labels)
            print(ID3Tree)
            train_end_t = time.time()
            print('training finish, cost time: %d' % (train_end_t - train_start_t))

            #tag_data_set     test
            test_set = dict()
            f = line_reader('F:/ECNU/Course/KnowledgeAna/tag_data_set/' + QID + '/test_set')
            line = next(f)
            print('loading taged testing set...')
            cnt = 0
            while line:
                content = re.split('\s+', line)
                doc = content[0]
                score = float(content[1])
                test_set.setdefault(doc, score)
                if cnt == 0:
                    X_test = np.array(weight[idx[doc]]).reshape(cnt + 1, d)
                    Y_test = np.array([score]).reshape(cnt + 1, 1)
                else:
                    X_test = np.concatenate((X_test, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(cnt + 1, d)
                    Y_test = np.concatenate((Y_test, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
                cnt += 1
                line = next(f)

            #call sklearn.Lasso()
            #clflasso = Lasso().fit(X_train, Y_train)

            print('predicting...')
            Y_hat = []
            labels = list(range(0, featureNum))
            labels = list(map(lambda x: str(x), labels))
            for line in X_test:
                Y_predict = ID3.classify(ID3Tree, labels, line.tolist())                                                      #predict
                Y_predict

                Y_hat.append(np.int(Y_predict))

            MAE = np.mean(np.abs(Y_hat - Y_test))
            print('MAE: %f' % MAE)
            # print(Y_hat)

            for idx, doc in enumerate(test_set.keys()):
                if idx >= cnt:
                    break
                res.write(QID + ' ' + doc + ' ')
                res.write(str(float(Y_hat[idx])))
                res.write('\n')
            MAE_TOTAL += MAE / 50
            print(QID + ' MAE: %f' % MAE)
            print('===================================\n')
            res.write('\n MAE: %f \n' % MAE)
        res.write('===================================\n')
        res.write('\nMAE: %f' % MAE_TOTAL)

