# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
Reservoir Sampling.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)

Example:
    cat in_file.txt | python reservoir_sampling.py 1000 > to_file.txt

"""
import sys
import random


def _sample(fin, k):
    s, i = [], 0
    for x in fin:
        if i < k:
            s.append(x)
        else:
            r = random.randint(0, i - 1)
            if r < k:
                s[r] = x
        i += 1

    return ''.join(s)


if __name__ == '__main__':
    k = int(sys.argv[1])
    print _sample(sys.stdin, k),