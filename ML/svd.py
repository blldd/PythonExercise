# -*- coding:UTF-8 -*-

# coding:utf-8

from numpy import *


def loadData():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [3, 3, 3, 0, 0],
            [5, 5, 3, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 6, 6]]


data = loadData()
data = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]
u, sigma, vt = linalg.svd(data)

print(sigma)

sig3 = mat([[sigma[0], 0, 0],
            [0, sigma[1], 0],
            [0, 0, sigma[2]]])

print(u[:, :3] * sig3 * vt[:3, :])
