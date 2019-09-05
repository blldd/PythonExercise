# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/5 9:33 PM
@Author  : ddlee
@File    : josephus.py
"""


def josephus(n, m):
    """
    :param n: 总人数
    :param m: 每数到m去除
    :return: 返回最后一个人的下标
    """

    if n == 1:
        return 0
    else:
        return (josephus(n - 1, m) + m) % n


if __name__ == '__main__':
    n = 3
    m = 2
    ans = josephus(n, m)
    print(ans)
