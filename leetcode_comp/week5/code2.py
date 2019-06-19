# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/9 10:53 AM
@Author  : ddlee
@File    : code2.py
"""
import sys

"""
5087. 活字印刷 
你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

示例 1：
输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。

示例 2：
输入："AAABBC"
输出：188
"""
from functools import reduce


class Solution:
    def numTilePossibilities(self, tiles):
        l = len(tiles)

        def fac(n):
            return reduce(lambda x, y: x * y, range(1, n + 1))

        def combine(n, c):
            return fac(n) // (fac(c) * fac(n - c))

        def select(tiles, n):
            pass
        return combine(3, 2)


if __name__ == '__main__':
    tiles = "AAB"

    print(Solution().numTilePossibilities(tiles))
