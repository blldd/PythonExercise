# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:46 PM
@Author  : ddlee
@File    : 3.py
"""

import sys
import collections


def process(values, depend_dict, sequen_dict, arr):
    l = len(values)

    time_dict = {}
    for i in range(l):
        time_dict[i+1] = values[i]
    time_dict = sorted(time_dict.items(), key=lambda x: x[1])
    print(time_dict)

    ans = []

    keys = set(depend_dict.keys())
    pres = set(values).difference(keys)
    print(pres)

    tmp = {}
    for idx, item in enumerate(arr):
        if item[1] == 0:
            tmp[idx+1] = item
            arr.pop(idx)
    print(arr)

    tmp = sorted(tmp.items(), key=lambda x:x[1])

    for i in tmp:
        ans.append(i[0])

    used_set = set(ans)
    print(used_set)

    tmp = []
    todo = []
    for i in used_set:
        if i in sequen_dict:
            todo.extend(sequen_dict[i])
    for i in todo:
        tmp.append(arr[i-1])
        arr.pop(i-1)

    print(arr)



    for key, val in time_dict:
        ans.append(key)


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N, M = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    depend_dict = collections.defaultdict(list)
    sequen_dict = collections.defaultdict(list)
    arr = [[[], 0] for _ in range(N)]
    # print(arr)

    for i in range(M):
        line = sys.stdin.readline().strip()
        a, b = list(map(int, line.split()))
        depend_dict[b].append(a)
        sequen_dict[a].append(b)

        arr[b-1][0].append(a)
        arr[b-1][1] = values[b-1]

    print(depend_dict)
    print(sequen_dict)

    print(arr)

    res = process(values, depend_dict, sequen_dict, arr)
    print(res)
