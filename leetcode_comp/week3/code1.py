# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:29 AM
@Author  : ddlee
@File    : code1.py
"""
import random

"""
1051. 高度检查器  
拍年度纪念照时，要求学生按照高度非递减的顺序排列。

返回没有站在正确位置的学生人数。（该人数是能让所有学生以不递减高度排列的必要移动人数。）

示例：
输入：[1,1,4,2,1,3]
输出：3
解释：
高度为 4、3 和最后一个 1 的学生没有站在正确的位置。
"""


class Solution:
    def heightChecker(self, heights):
        l = len(heights)
        if l < 2:
            return 0

        sorted_heights = sorted(heights)
        # print(sorted_heights)
        cnt = 0
        for i in range(l):
            if sorted_heights[i] != heights[i]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    heights = [1, 1, 4, 2, 1, 3]
    print(Solution().heightChecker(heights))
