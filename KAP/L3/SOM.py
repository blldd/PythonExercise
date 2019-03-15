# -*- coding: utf-8 -*-
"""
Created on Wed Nov  13 22:35:46 2017

@author: Don
"""
import re
import time
import math
import numpy as np
from collections import Counter
from sklearn.neighbors import BallTree
from sklearn.decomposition import PCA
from Pre.Vectorize import Vector


def line_reader(file):
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None


class SOM(object):
    def __init__(self, m, n, X, Y, alpha=0.2, max_iter=100):
        self.m = m
        self.n = n
        self.d = X.shape[1]
        self.size = m * n
        self.data = X
        self.labels = Y.reshape(-1)
        self.alpha = alpha
        self.max_iter = max_iter
        self.weights = np.random.random((self.m, self.n, self.d))
        self.output = np.zeros((self.m, self.n))
        self.data = self.normalize_data()
        self.weights = self.normalize_weight()

    def normalize_data(self):
        new_data = []
        for sample in self.data:
            new_data.append(sample/np.linalg.norm(sample))
        return np.array(new_data).reshape(self.data.shape)

    def normalize_weight(self):
        new_data = []
        for m_dimen in self.weights:
            for weight in m_dimen:
                new_data.append(weight/np.linalg.norm(weight))
        return np.array(new_data).reshape((self.m, self.n, self.d))

    def learning_rate(self, t, r):
        return (self.alpha/(t+1)) * math.exp(-r)

    def find_neighbor(self, m, n, R):
        neighbor = []
        for mi in range(self.m):
            for ni in range(self.n):
                r = int(((mi - m) ** 2 + (ni - n) ** 2) ** 0.5)
                if r <= R:
                    neighbor.append((mi, ni, r))
        return neighbor

    def find_winner(self, x):
        max_sim = 0
        win_m = 0
        win_n = 0
        for mi in range(self.m):
            for ni in range(self.n):
                sim = x.dot(self.weights[mi, ni])
                if sim > max_sim:
                    max_sim = sim
                    win_m = mi
                    win_n = ni
        return win_m, win_n, max_sim

    def train(self):
        R = (self.m ** 2 + self.n ** 2) ** 0.5
        for it in range(self.max_iter):
            for sample in self.data:
                win_m, win_n, max_sim = self.find_winner(sample)
                neighbor = self.find_neighbor(win_m, win_n, R)
                for w in neighbor:
                    mw = w[0]
                    nw = w[1]
                    rw = w[2]
                    self.weights[mw, nw] += self.learning_rate(it, rw) * (sample - self.weights[mw, nw])
                R *= 1 - (it + 1) / self.max_iter
        data_tree = BallTree(self.data)
        for mi in range(self.m):
            for ni in range(self.n):
                dist, idx = data_tree.query([self.weights[mi, ni]], k=10)
                vote = [self.labels[i] for i in idx.reshape(-1)]
                self.output[mi, ni] = int(sorted(dict(Counter(vote)).items(), key=lambda d: d[1], reverse=True)[0][0])

    def predict(self, input_X):
        new_data = []
        for sample in input_X:
            new_data.append(sample / np.linalg.norm(sample))
        X = np.array(new_data).reshape(input_X.shape)
        Y_hat = []
        for sample in X:
            m, n, _ = self.find_winner(sample)
            Y_hat.append(self.output[m, n])
        return np.array(Y_hat).reshape(-1, 1)


if __name__ == '__main__':

    QID_LIST = list(range(201, 251))
    QID_LIST = list(map(lambda x: str(x), QID_LIST))

    with open('F:/ECNU/Course/KnowledgeAna/results/som.res', 'a') as res:
        MAE_TOTAL = 0
        for QID in QID_LIST:
            print('SOM for query ' + QID)
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

            y_max = np.max(Y_train)
            y_min = np.min(Y_train)
            positive_score = np.mean(Y_train[:int(Y_train.shape[0]/2), ])
            negative_score = np.mean(Y_train[int(Y_train.shape[0]/2)+1:, ])
            if positive_score - negative_score < (y_max-y_min)/4:
                positive_score = negative_score + (y_max-y_min)/4
            positive_idx = 0
            negative_idx = X_train.shape[0]
            for i in range(Y_train.shape[0]):
                if float(Y_train[i]) > positive_score:
                    positive_idx = i
                if float(Y_train[i]) > negative_score:
                    negative_idx = i
            print(positive_idx)
            print(positive_score)
            print(negative_idx)
            print(negative_score)
            if positive_idx > 200:
                X_train = np.concatenate((X_train[:positive_idx+1, ], X_train[-positive_idx:, ]), axis=0)
                Y_train = np.concatenate((np.ones((positive_idx, 1)), np.zeros((X_train.shape[0]-positive_idx, 1))),
                                         axis=0)
            else:
                X_train = np.concatenate((X_train[:positive_idx + 1, ], X_train[negative_idx:, ]), axis=0)
                Y_train = np.concatenate((np.ones((positive_idx, 1)), np.zeros((X_train.shape[0] - positive_idx, 1))),
                                         axis=0)

            som = SOM(10, 10, X_train, Y_train, max_iter=100)
            print('clustering...')
            train_start_t = time.time()
            som.train()
            train_end_t = time.time()
            print('clustering finish, cost time: %d' % (train_end_t - train_start_t))

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
                    X_test = np.concatenate((X_test, np.array(weight[idx[doc]]).reshape(1, d)), axis=0).reshape(cnt + 1, d)
                    Y_test = np.concatenate((Y_test, np.array([score]).reshape(1, 1)), axis=0).reshape(cnt + 1, 1)
                cnt += 1
                line = next(f)

            print('predicting...')
            Y_hat = som.predict(X_test)
            MAE = np.mean(np.abs(Y_hat - Y_test[:X_test.shape[0], ]))
            for idx, doc in enumerate(test_set.keys()):
                if idx >= X_test.shape[0]:
                    break
                res.write(QID + ' ' + doc + ' ')
                res.write(str(float(Y_hat[idx, :])))
                res.write('\n')
            MAE_TOTAL += MAE / 50
            print(QID + ' MAE: %f\n\n' % MAE)
        res.write('MAE: %f\n\n' % MAE_TOTAL)
