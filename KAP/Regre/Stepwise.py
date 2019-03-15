# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:30:37 2017

@author: Don
"""


import re
import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import linear_model
from KAP.Pre.Vectorize import Vector
from KAP.Regre.OLSR import *


def line_reader(file):
    """
    read a file line by line
    :param file:
    :return:
    """
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None


class SWR(object):
    def __init__(self):
        self.lr = OLSR()
        self.H = np.zeros(1)
        self.k = 0
        self.F = 0

    def F_val(self, k, m, Y, Y_hat):
        ESS = np.sum(np.power(Y_hat - np.mean(Y), 2))
        RSS = np.sum(np.power(Y - Y_hat, 2))
        MSE = ESS / (k - 1)
        MSR = RSS / (m - k)
        return MSE / MSR

    def predict(self, X):
        selected_X = X * self.H
        selected_X = np.delete(selected_X,
                               list(set(range(selected_X.shape[1])) - set(selected_X.nonzero()[1])),
                               axis=1)
        return self.lr.predict(selected_X)

    def forward_selection(self, X, Y, max_feature=3000):
        m = X.shape[0]
        n = X.shape[1]
        self.H = np.zeros((1, n))
        self.H[0, 0] = 1
        self.k = 1
        self.F = 0
        while True:
            # variables traversal
            update = False
            for i in range(n):
                if self.H[0, i] != 1:
                    temp_H = self.H.copy()
                    temp_k = self.k
                    # select i'th variable
                    temp_H[0, i] = 1
                    temp_k += 1
                    selected_X = X * temp_H
                    selected_X = np.delete(selected_X,
                                           list(set(range(selected_X.shape[1])) - set(selected_X.nonzero()[1])),
                                           axis=1)
                    # train linear model
                    temp_lr = OLSR()
                    temp_lr.train(selected_X, Y)
                    Y_hat = temp_lr.predict(selected_X)
                    # cal F val
                    temp_F = self.F_val(temp_k, m, Y, Y_hat)
                    if temp_F > self.F:
                        # update selected features
                        self.F = temp_F
                        self.H = temp_H
                        self.lr = temp_lr
                        self.k += 1
                        update = True
                        print('update')
                        break
            else:
                if not update:
                    break
            if self.k > max_feature or self.k > n:
                break


if __name__ == '__main__':
    # size = 200
    # x1 = np.random.random((size, 1))
    # x2 = np.random.random((size, 1))
    # x3 = np.random.random((size, 1))
    # x4 = np.random.random((size, 1))
    # x5 = np.random.random((size, 1))
    # y = 2 * x3
    # data = np.concatenate((x1, x2, x3, x4, x5), axis=1)
    # swr = SWR()
    # swr.forward_selection(data, y)
    # print(swr.k)
    # print(swr.H)
    # print(swr.lr.W)
    # Y_hat = swr.predict(data)
    # MAE = np.mean(np.abs(Y_hat - y))
    # print(MAE)

    QID_LIST = list(range(242, 251))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    for QID in QID_LIST:
        print('SWR for query ' + QID)
        swr = SWR()
        vector = Vector(QID)
        word, weight, idx = vector.get_vector()
        print('PCA...')
        print('dimension: ' + str(weight.shape[1]))
        PCA_start_t = time.time()
        pca = PCA(n_components=500)
        weight = pca.fit_transform(weight)
        PCA_end_t = time.time()
        print('new dimension: ' + str(weight.shape[1]))
        print('PCA time: %d' % (PCA_end_t - PCA_start_t))

        train_set = dict()
        f = line_reader('F:/ECNU/Course/KnowledgeAna/data_set/' + QID + '/train_set')
        line = next(f)
        d = len(weight[0])
        print('loading training set...')
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
        swr.forward_selection(X_train, Y_train, max_feature=3000)
        print('select ' + str(swr.k) + ' features')
        train_end_t = time.time()
        print('training finish, cost time: %d' % (train_end_t - train_start_t))

        test_set = dict()
        f = line_reader('F:/ECNU/Course/KnowledgeAna/data_set/' + QID + '/test_set')
        line = next(f)
        print('loading testing set...')
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

        print('predicting...')
        Y_hat = swr.predict(X_test)
        MAE = np.mean(np.abs(Y_hat - Y_test))
        print('MAE: %f' % MAE)
        # print(Y_hat)
        with open('F:/ECNU/Course/KnowledgeAna/results/Stepwise/' + QID, 'w') as f:
            for idx, doc in enumerate(test_set.keys()):
                f.write(QID + ' ' + doc + ' ')
                f.write(str(float(Y_hat[idx, :])))
                f.write('\n')
            f.write('\n MAE: %f' % MAE)
        print('===================================\n')



