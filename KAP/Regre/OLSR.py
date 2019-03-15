# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 22:35:45 2017

@author: Don
"""

import re
import time

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


class OLSR(object):
    def __init__(self):
        self.W = np.zeros(1)

    def __getattr__(self, item):
        pass

    def train(self, X, Y):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        print("X_ : ")
        print(X_)
        self.W = np.dot(np.dot(np.linalg.pinv(np.dot(X_.T, X_)), X_.T), Y)       #

    def predict(self, X):
        X_ = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        return np.dot(X_, self.W)


if __name__ == '__main__':
    QID_LIST = list(range(201, 202))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    for QID in QID_LIST:
        print('OLSR for query ' + QID)
        olsr = OLSR()
        vector = Vector(QID)
        word, weight, idx = vector.get_vector()
        print('PCA...')
        print('dimension: ' + str(weight.shape[1]))
        PCA_start_t = time.time()
        pca = PCA(n_components=1000)
        weight = pca.fit_transform(weight)
        PCA_end_t = time.time()
        print('new dimension: ' + str(weight.shape[1]))
        print('PCA time: %d' % (PCA_end_t - PCA_start_t))

        train_set = dict()
        f = line_reader('F:/ECNU/Course/KnowledgeAna/data_set/' + QID + '/train_set')
        line = next(f)                                  #    next(iterator[, default])    Return the next item from the iterator.
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
        olsr.train(X_train, Y_train)                                                        #train
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
        Y_hat = olsr.predict(X_test)                                                      #predict
        MAE = np.mean(np.abs(Y_hat - Y_test))
        print('MAE: %f' % MAE)
        # print(Y_hat)
        with open('F:/ECNU/Course/KnowledgeAna/results/OLSR/' + QID, 'w') as f:
            for idx, doc in enumerate(test_set.keys()):
                f.write(QID + ' ' + doc + ' ')
                f.write(str(float(Y_hat[idx, :])))
                f.write('\n')
            f.write('\n MAE: %f' % MAE)
        print('===================================\n')

