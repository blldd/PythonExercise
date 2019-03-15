# -*- coding: utf-8 -*-
"""
Created on Wed Nov  14 22:35:46 2017

@author: Don
"""

import re
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from KAP.Pre.Vectorize import Vector


def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None


class LWLR(object):
    def __init__(self):
        self.W = np.zeros(1)

    def __getattr__(self, item):
        pass

    def predict(self, x, X, Y, bandwidth=1.0):
        x_ = np.concatenate((np.ones((1, 1)), x), axis=1)
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        K = np.eye(X_.shape[0])
        for row in range(X_.shape[0]):
            diff = x_ - X_[row, :]
            K[row, row] = np.exp(diff.dot(diff.T)/(-2 * bandwidth ** 2))
        Z = X_.T.dot(K).dot(X_)
        self.W = np.linalg.pinv(Z).dot(X_.T).dot(K).dot(Y)
        return x_.dot(self.W)

if __name__ == '__main__':

    QID_LIST = list(range(201, 251))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    with open('/home/dean/Desktop/data/results/lwl.res', 'a') as res:
        MAE_TOTAL = 0
        for QID in QID_LIST:
            print('LWL for query ' + QID)
            lwlr = LWLR()
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
                y_hat = lwlr.predict(row.reshape(1, X_test.shape[1]), X_train, Y_train, bandwidth=2)
                print(cnt)
                Y_hat.append(y_hat)
                if cnt > 100:
                    break
            Y_hat = np.array(Y_hat).reshape((cnt, Y_test.shape[1]))
            MAE = np.mean(np.abs(Y_hat - Y_test[:cnt, ]))
            # print(Y_hat)
            for idx, doc in enumerate(test_set.keys()):
                if idx >= cnt:
                    break
                res.write(QID + ' ' + doc + ' ')
                res.write(str(float(Y_hat[idx, :])))
                res.write('\n')
            MAE_TOTAL += MAE/50
            print(QID + ' MAE: %f' % MAE)
            print('===================================\n')
        res.write('\nMAE: %f' % MAE_TOTAL)