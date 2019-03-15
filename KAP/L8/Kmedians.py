# -*- coding: utf-8 -*-
"""
Created on Wed Dec  19  18:28:53 2017

@author: Don
"""

import re
import time

import numpy as np
from Pre.Vectorize import Vector
from sklearn import random_projection


transformer = random_projection.SparseRandomProjection()
DataPath = 'E:/ECNU/Course/KnowledgeAna/tag_data_set/'


def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None


def disEclud(vecA, vecB):
    return sum(abs(vecA - vecB))


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        maxJ = max(dataSet[:, j])
        rangeJ = float(maxJ - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def Kmedians(dataset, k, distMean=disEclud, createCent=randCent):
    m = shape(dataset)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataset, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            mindist = inf
            minindex = -1
            for j in range(k):
                distJI = distMean(centroids[j, :], dataset[i, :])
                if distJI < mindist:
                    mindist = distJI
                    minindex = j
            if clusterAssment[i, 0] != minindex:
                clusterChanged = True
            clusterAssment[i, :] = minindex, mindist ** 2
        # print(centroids)
        for cent in range(k):
            ptsInClust = dataset[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = median(ptsInClust, axis=0)
    return centroids, clusterAssment


if __name__ == '__main__':

    MAE_TOTAL = 0

    QID_LIST = list(range(201, 251))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    for QID in QID_LIST:

        print('Kmedians for query ' + QID)

        vector = Vector(QID)
        word, weight, idx = vector.get_vector()

        print('Using PCA to reduce the dimension...')
        oldDimension = weight.shape[1]
        pca = PCA(n_components=1000)
        weight = pca.fit_transform(weight)
        print('reduce the dimension from ' + str(oldDimension) + ' to ' + str(weight.shape[1]))

        train_set = dict()
        f = line_reader(DataPath + 'dataSet/' + QID + '/trainSet')
        line = next(f)
        d = len(weight[0])

        print('loading training set...')
        cnt = 0
        while line:
            content = re.split('\s+', line)
            doc = content[0]
            score = float(content[1])
            train_set.setdefault(doc, score)
            cnt += 1
            line = next(f)

        trainTemp = sorted(train_set.items(), key=lambda asd: asd[1], reverse=True)
        train_set_class1 = trainTemp[:200]
        train_set_calss0 = trainTemp[-200:]
        cnt = 0
        for oneline in train_set_class1:
            if cnt == 0:
                X_train = np.array(weight[idx[oneline[0]]]).reshape(cnt + 1, d)
                Y_train = np.array([1]).reshape(cnt + 1, 1)
            else:
                X_train = np.concatenate((X_train, np.array(weight[idx[oneline[0]]]).reshape(1, d)), axis=0).reshape(
                    cnt + 1, d)
                Y_train = np.concatenate((Y_train, np.array([1]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
            cnt += 1

        for oneline in train_set_calss0:
            X_train = np.concatenate((X_train, np.array(weight[idx[oneline[0]]]).reshape(1, d)), axis=0).reshape(
                cnt + 1, d)
            Y_train = np.concatenate((Y_train, np.array([0]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
            cnt += 1

        print("training set Tagged...")

        test_set = dict()
        f = line_reader(DataPath + 'dataSet/' + QID + '/testSet')
        line = next(f)
        print('loading testing set...')
        cnt = 0
        while line:
            content = re.split('\s+', line)
            doc = content[0]
            score = float(content[1])
            test_set.setdefault(doc, score)
            cnt += 1
            line = next(f)

        testTemp = sorted(test_set.items(), key=lambda asd: asd[1], reverse=True)
        test_set_class1 = testTemp[:40]
        test_set_class0 = testTemp[-40:]
        cnt = 0
        for oneline in test_set_class1:
            if cnt == 0:
                X_test = np.array(weight[idx[oneline[0]]]).reshape(cnt + 1, d)
                Y_test = np.array([1]).reshape(cnt + 1, 1)
            else:
                X_test = np.concatenate((X_test, np.array(weight[idx[oneline[0]]]).reshape(1, d)), axis=0).reshape(
                    cnt + 1, d)
                Y_test = np.concatenate((Y_test, np.array([1]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
            cnt += 1

        for oneline in test_set_class0:
            X_test = np.concatenate((X_test, np.array(weight[idx[oneline[0]]]).reshape(1, d)), axis=0).reshape(cnt + 1,
                                                                                                               d)
            Y_test = np.concatenate((Y_test, np.array([0]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
            cnt += 1

        print("test set Tagged...")

        print("Calculate the probability")

        _, clusterAssment = Kmedians(X_train, 2)
    Y_hat = []
    Y_hat = clusterAssment[:, 0]

Y_hat = Y_hat.tolist()

print("Predict...")

Y_hat = []
Y_hat = clf.predict(X_test)
Y_hat = Y_hat[:, np.newaxis]
MAE = np.mean(np.abs(Y_hat - Y_test))
print('MAE: %f' % MAE)

test_set = test_set_class1 + test_set_class0

with open('results/' + 'Kmedians' + '.res', 'a') as f:
    for idx, line in enumerate(test_set):
        f.write(QID + ' ' + line[0] + ' ')
        f.write(str(float(Y_hat[idx, :])))
        f.write('\n')
    f.write('\n MAE: %f \n' % MAE)
    f.write('-------------------------------\n')
print('========================================\n')
