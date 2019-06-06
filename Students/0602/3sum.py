# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/2 4:34 PM
@Author  : ddlee
@File    : 3sum.py
"""
import time


def three_sum_1(arr, target):
    # for i in arr:
    #     print(i)
    res = []
    for id1, value1 in enumerate(arr):
        for id2, value2 in enumerate(arr[id1 + 1:]):
            value3 = target - value1 - value2
            if value3 in arr[id2 + 1:]:
                res.append([value1, value2, value3])
    return res


def three_sum2(arr, target):
    # N * N * N
    res = set()
    for id1 in range(len(arr)):
        value1 = arr[id1]

        for id2 in range(id1 + 1, len(arr)):
            value2 = arr[id2]

            value3 = target - value1 - value2

            if value3 in arr[id2 + 1:]:
                res.add((value1, value2, value3))
    return res


def three_sum(arr, target):
    # N * N
    arr = sorted(arr)

    res = set()
    for i in range(len(arr)):
        left = i
        right = len(arr) - 1
        while left < right:
            tmp = arr[left] + arr[right] + arr[i]
            if tmp == target:
                res.add((arr[left], arr[right], arr[i]))
                left += 1
            elif tmp > target:
                right -= 1
            else:
                left += 1
    return res

if __name__ == '__main__':
    arr = list(range(100))
    target = 8
    start = time.time()
    for i in range(100):
        three_sum(arr, target)
    print(time.time() - start)
