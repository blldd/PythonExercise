# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:59 AM
@Author  : ddlee
@File    : code3.py
"""
import copy

"""
1053. 交换一次的排列
给出一个正整数数组 A（元素不一定不同），
返回可以在一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的按字典序排列小于 A 的最大排列。
如果无法这样做，就返回原数组。

示例 1：
输入：[3,2,1]
输出：[3,1,2]
解释：
交换 2 和 1。
"""


class Solution:
    def prevPermOpt1(self, A):
        l = len(A)
        if l < 2:
            return A

        res = []
        ma = 0
        for i in range(l)[::-1]:
            tmp = [i for i in A]
            flag = 0
            for j in range(i)[::-1]:
                if A[j] > A[i]:
                    tmp[i] = A[j]
                    tmp[j] = A[i]
                    flag = 1
                    break

            su = 0
            for i in tmp:
                su = su * 10 + i
            if su > ma and flag == 1:
                res = tmp
                ma = su

        return res if res else A


if __name__ == '__main__':
    A = [6, 1, 5, 9, 1, 1, 9, 7, 7, 9, 7, 6, 2, 7, 3, 4, 5, 1, 7, 6, 3, 5, 3, 1, 4, 7, 1, 1, 8, 8, 9, 1, 9, 5, 1, 6, 5,
         4, 7, 3, 2, 7, 4, 9, 7, 6, 2, 5, 7, 4, 3, 7, 5, 5, 4, 4, 2, 1, 3, 1, 6, 4, 8, 7, 5, 9, 3, 1, 4, 4, 7, 5, 3, 7,
         2, 4, 4, 8, 5, 4, 8, 1, 1, 3, 4, 3, 5, 4, 8, 1, 5, 4, 9, 8, 4, 5, 3, 1, 1, 3]
    A = [5, 3, 1, 1, 3]
    A = [1, 1, 5]
    print(Solution().prevPermOpt1(A))
