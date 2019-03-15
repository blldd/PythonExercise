# -*- coding: utf-8 -*-
"""
Created on Wed Nov  20 16:22:32 2017

@author: Don
"""

import re
import time

import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import Lasso
from Pre.Vectorize import Vector

def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None

'''
class Lasso(object):
    def __init__(self):
        self.W = np.zeros(1)

    def __getattr__(self, item):
        pass

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
'''

if __name__ == '__main__':
    QID_LIST = list(range(201, 203))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    with open('F:/ECNU/Course/KnowledgeAna/results/Lasso.res', 'a') as res:
        MAE_TOTAL = 0
        for QID in QID_LIST:
            print('Lasso for query ' + QID)


            #lasso = Lasso()
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
            #lasso.train(X_train, Y_train)                                                        #train
            #call sklearn.Lasso()
            clflasso = Lasso().fit(10000*X_train, Y_train)
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

            #call sklearn.Lasso()
            #clflasso = Lasso().fit(X_train, Y_train)

            print('predicting...')
            Y_hat = clflasso.predict(10000*X_test)                                                      #predict
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
        res.write('\nMAE: %f' % MAE_TOTAL)