# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:36:58 2017

@author: Don
"""
import os
import re
import time
import sys
sys.path.append("../../../PythonExercise")
import numpy as np
from sklearn.decomposition import PCA

from KAP.Pre.Vectorize import Vector


def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class LogisticRegression(object):
    def __init__(self):
        self.W = np.zeros(1)

    def __getattr__(self, item):
        pass

    def train(self, X, Y, alpha=0.001, iter=500):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        m, n = np.shape(X_)
        self.W = np.random.normal(0.1, 0.5, (n, 1))
        for i in range(iter):
            h = sigmoid(np.dot(X_, self.W))
            L = np.sum(Y * np.log(h) - (1 - Y) * np.log(1 - h)) / m
            # print(L)
            self.W = self.W - alpha * np.dot(X_.T, (h - Y))

    def predict(self, X):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        return sigmoid(np.dot(X_, self.W))


if __name__ == '__main__':

    QID_LIST = list(range(201, 251))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    for QID in QID_LIST:
        print('logistic regression for query ' + QID)
        lr = LogisticRegression()
        vector = Vector(QID)
        word, weight, idx = vector.get_vector()
        print('PCA...')
        print('dimension: ' + str(weight.shape[1]))
        PCA_start_t = time.time()
        pca = PCA(n_components=1000)                                                 #PCA
        weight = pca.fit_transform(weight)
        # weight = transformer.fit_transform(weight)
        PCA_end_t = time.time()
        print('new dimension: ' + str(weight.shape[1]))
        print('PCA time: %d' % (PCA_end_t - PCA_start_t))

        train_set = dict()
        f = line_reader('../data_set/' + QID + '/train_set')
        line = next(f)
        d = len(weight[0])
        print('loading training set...')
        cnt = 0
        pos_cnt = 0
        neg_cnt = 0
        while line:
            content = re.split('\s+', line)
            doc = content[0]
            score = float(content[1])
            if score > 32:
                score = 1
                pos_cnt += 1
            elif score < 28:
                score = 0
                neg_cnt += 1
            else:
                line = next(f)
                continue
            train_set.setdefault(doc, score)
            if cnt == 0:
                X_train = np.array(weight[idx[doc]]).reshape(cnt + 1, d)
                Y_train = np.array([score]).reshape(cnt + 1, 1)
            else:
                X_train = np.concatenate((X_train, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(cnt + 1,d)
                Y_train = np.concatenate((Y_train, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
            cnt += 1
            line = next(f)
        print(pos_cnt)
        print(neg_cnt)
        print('training...')
        train_start_t = time.time()
        lr.train(X_train, Y_train, alpha=0.001, iter=5000)                                #train
        train_end_t = time.time()
        print('training finish, cost time: %d' % (train_end_t - train_start_t))

        test_set = dict()
        f = line_reader('../data_set/' + QID + '/test_set')
        line = next(f)
        print('loading testing set...')
        cnt = 0
        while line:
            content = re.split('\s+', line)
            doc = content[0]
            score = float(content[1])
            if score > 32:
                score = 1
            elif score < 28:
                score = 0
            else:
                line = next(f)
                continue
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
        Y_hat = lr.predict(X_test)                                                 #predict
        MAE = np.mean(np.abs(Y_hat - Y_test))
        print('MAE: %f' % MAE)
        # print(Y_hat)
        res_path = '../results/linear_regression/'
        if not os.path.exists(res_path):
            os.mkdir(res_path)
        with open(res_path + QID, 'w') as f:
            for idx, doc in enumerate(test_set.keys()):
                f.write(QID + ' ' + doc + ' ')
                f.write(str(float(Y_hat[idx, :])))
                f.write('\n')
            f.write('\n MAE: %f' % MAE)
        print('===================================\n')