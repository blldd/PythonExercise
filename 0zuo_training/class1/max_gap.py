# -*- coding:UTF-8 -*-

"""
给定一个数组，求如果排序之后，相邻两数的最大差值。要求时间复杂度O(N)，且要求不能用非基于比较的排序。

"""
import sys


def bucket(val, length, min_num, max_num):
    return ((val - min_num) * length // (max_num - min_num))


def max_gap(vals):
    res = 0
    if len(vals) < 2:
        return res
    length = len(vals)
    min_num = sys.maxsize
    max_num = -sys.maxsize - 1
    # print(min_num)
    # print(max_num)
    for i in range(length):
        min_num = min(min_num, vals[i])
        max_num = max(max_num, vals[i])
    # print(min_num)
    # print(max_num)
    if min_num == max_num:
        return 0
    hasNum = [False for i in range(length + 1)]
    maxs = [0 for i in range(length + 1)]
    mins = [0 for i in range(length + 1)]
    # print(hasNum)
    # print(maxs)

    for i in range(length):
        bid = bucket(vals[i], length, min_num, max_num)
        print(bid)
        mins[bid] = min(mins[bid], vals[i]) if hasNum[bid] else vals[i]
        maxs[bid] = max(maxs[bid], vals[i]) if hasNum[bid] else vals[i]
        hasNum[bid] = True
    lastMax = maxs[0]
    for i in range(1, length + 1):
        if hasNum[i]:
            res = max(res, mins[i] - lastMax)
            lastMax = maxs[i]
    return res


if __name__ == '__main__':
    vals = [5, 7, 16, 18, 21, 26, 35]
    print(max_gap(vals))

    """
    testTime = 500000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = copyArray(arr1)
        if max_gap(arr1) != comparator(arr2):
            succeed = False
            break
    res = "succeed!" if succeed else "try one more time...."
    print(res)
    """
