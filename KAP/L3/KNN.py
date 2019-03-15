# -*- coding: utf-8 -*-
"""
Created on Wed Nov  12 22:35:46 2017

@author: Don
"""

import re
import sys
import time
import numpy as np
from collections import Counter
from sklearn.neighbors import BallTree
from sklearn.decomposition import PCA
from KAP.Pre.Vectorize import Vector


def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None


class KNN(object):
    def __init__(self):
        pass

    def classify(self, x, X, Y, K):
        tree = BallTree(X)
        d, idx = tree.query([x], k=K)
        Y_ = Y.reshape(-1)                             #行向量
        vote = [Y_[i] for i in idx.reshape(-1)]
        return sorted(dict(Counter(vote)).items(), key=lambda d: d[1], reverse=True)[0][0]


if __name__ == '__main__':
    QID_LIST = list(range(201, 251))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    with open('F:/ECNU/Course/KnowledgeAna/results/knn.res', 'w') as res:
        MAE_TOTAL = 0
        for QID in QID_LIST:
            print('KNN for query ' + QID)
            knn = KNN()
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
                    X_train = np.concatenate((X_train, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(
                        cnt + 1, d)
                    Y_train = np.concatenate((Y_train, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
                cnt += 1
                line = next(f)

            # split positive/negative samples
            y_max = np.max(Y_train)
            y_min = np.min(Y_train)
            positive_score = y_max - (y_max - y_min) / 3
            negative_score = y_min + (y_max - y_min) / 3
            positive_idx = 0
            negative_idx = X_train.shape[0]
            for i in range(Y_train.shape[0]):
                if Y_train[i] > positive_score:
                    positive_idx = i
                if Y_train[i] > negative_score:
                    negative_idx = i
                    break
            #print(positive_idx)
            #print(positive_score)
            #print(negative_idx)
            #print(negative_score)
            X_train = np.concatenate((X_train[:positive_idx, ], X_train[negative_idx:, ]), axis=0)
            Y_train = np.concatenate((np.ones((positive_idx, 1)), np.zeros((X_train.shape[0] - negative_idx, 1))),
                                     axis=0)

            test_set = dict()
            f = line_reader('F:/ECNU/Course/KnowledgeAna/data_set/' + QID + '/test_set')
            line = next(f)
            print('loading testing set...')
            cnt = 0
            while line:
                content = re.split('\s+', line)
                doc = content[0]
                score = float(content[1])
                if score > positive_score:
                    score = 1
                elif score < negative_score:
                    score = 0
                else:
                    line = next(f)
                    continue
                test_set.setdefault(doc, score)
                if cnt == 0:
                    X_test = np.array(weight[idx[doc]]).reshape(cnt + 1, d)
                    Y_test = np.array([score]).reshape(cnt + 1, 1)
                else:
                    X_test = np.concatenate((X_test, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(cnt + 1,
                                                                                                                d)
                    Y_test = np.concatenate((Y_test, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
                cnt += 1
                line = next(f)

            X_test = np.concatenate((X_test[:100, ], X_test[-100:, ]), axis=0)
            Y_test = np.concatenate((np.ones((100, 1)), np.zeros((100, 1))), axis=0)

            print('predicting...')
            Y_hat = []
            max_step = X_test.shape[0]-1
            for i in range(max_step+1):
                bar = '\r[' + '>' * int(i * 50 / max_step) + '-' * (50 - int(i * 50 / max_step)) + ']' + \
                      '%.2f' % float(i * 100 / max_step) + '%'
                print(bar, end='')
                y_hat = knn.classify(X_test[i, :].reshape(1, X_test.shape[1]), X_train, Y_train, K=7)
                Y_hat.append(y_hat)
            print('', end='\n')
            Y_hat = np.array(Y_hat).reshape((X_test.shape[0], Y_test.shape[1]))
            MAE = np.mean(np.abs(Y_hat - Y_test[:X_test.shape[0], ]))
            # print(Y_hat)
            for idx, doc in enumerate(test_set.keys()):
                if idx >= X_test.shape[0]:
                    break
                res.write(QID + ' ' + doc + ' ')
                res.write(str(float(Y_hat[idx, :])))
                res.write('\n')
            MAE_TOTAL += MAE / 50
            print(QID + ' MAE: %f\n\n' % MAE)
        res.write('MAE: %f\n\n' % MAE_TOTAL)
