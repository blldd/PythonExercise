# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:29 AM
@Author  : ddlee
@File    : code1.py
"""
import random


class Solution:
    def lastStoneWeight(self, stones):
        stones = sorted(stones, reverse=True)
        print(stones)

        while len(stones) > 1:
            large = stones.pop(0)
            small = stones.pop(0)
            if large - small > 0:
                stones.append(large - small)
                stones = sorted(stones, reverse=True)
        return sum(stones)




if __name__ == '__main__':
    S = [random.randint(1, 10) for i in range(5)]
    # S = "GL"
    print(Solution().lastStoneWeight(S))
