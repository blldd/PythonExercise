# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:32:27 2017

@author: Don

#locally weighted scatterplot smoothing
"""

import re
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from KAP.Pre.Vectorize import Vector

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


class LOESS(object):                         #locally weighted scatterplot smoothing
    def __init__(self):
        self.W = np.zeros(1)

    def __getattr__(self, item):
        pass

    def predict(self, x_pred, X, Y, bandwidth=0.5):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        x_pred_ = x_pred.reshape((1, len(x_pred)))
        x_pred_ = np.concatenate((np.ones((x_pred_.shape[0], 1)), x_pred_), axis=1)
        m = X_.shape[0]
        n = X_.shape[1]
        self.W = np.random.normal(0, 0.1, (n, 1))
        K = self.kernel(x_pred_, X_, bandwidth)
        Y_ = K * Y
        X_ = K * X_
        self.W = np.dot(np.dot(np.linalg.pinv(np.dot(X_.T, X_)), X_.T), Y_)
        return np.dot(x_pred_, self.W)

    def kernel(self, x, X_train, bandwidth=1):
        dist = []
        for row in x - X_train:
            dist.append(np.sum(np.square(row)))
        D = np.array(dist).reshape((X_train.shape[0], 1))
        return np.exp(-D/(2 * bandwidth))


if __name__ == '__main__':
    QID_LIST = list(range(201, 202))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    for QID in QID_LIST:
        print('linear regression for query ' + QID)
        loess = LOESS()
        vector = Vector(QID)
        word, weight, idx = vector.get_vector()
        print('PCA...')
        print('dimension: ' + str(weight.shape[1]))
        PCA_start_t = time.time()
        pca = PCA(n_components=1000)
        weight = pca.fit_transform(weight)
        # weight = transformer.fit_transform(weight)
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
                X_train = np.array(weight[idx[doc]]).reshape(cnt + 1, d)
                Y_train = np.array([score]).reshape(cnt + 1, 1)
            else:
                X_train = np.concatenate((X_train, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(cnt + 1,
                                                                                                              d)
                Y_train = np.concatenate((Y_train, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
            cnt += 1
            line = next(f)

        # print('training...')
        # train_start_t = time.time()
        # lr.train(X_train, Y_train, alpha=3, iter=5000)
        # train_end_t = time.time()
        # print('training finish, cost time: %d' % (train_end_t - train_start_t))

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
        Y_hat = []
        cnt = 0
        for row in X_test:
            cnt += 1
            y_hat = loess.predict(row, X_train, Y_train, bandwidth=0.05)
            print(cnt)
            Y_hat.append(y_hat)
            if cnt > 100:
                break
        Y_hat = np.array(Y_hat).reshape((cnt, Y_test.shape[1]))
        MAE = np.mean(np.abs(Y_hat - Y_test[:cnt, ]))
        print('MAE: %f' % MAE)
        # print(Y_hat)
        with open('F:/ECNU/Course/KnowledgeAna/results/LOESS/' + QID, 'w') as f:
            for idx, doc in enumerate(test_set.keys()):
                if idx >=   cnt:
                    break
                f.write(QID + ' ' + doc + ' ')
                f.write(str(float(Y_hat[idx, :])))
                f.write('\n')
            f.write('\n MAE: %f' % MAE)
        print('===================================\n')

