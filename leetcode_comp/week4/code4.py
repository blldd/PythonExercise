# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/2 11:04 AM
@Author  : ddlee
@File    : code4.py
"""
import collections
import numpy as np

"""
5075. 元素和为目标值的子矩阵数量
给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。
如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。

示例 1：
输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
输出：4
解释：四个只含 0 的 1x1 子矩阵。

示例 2：
输入：matrix = [[1,-1],[-1,1]], target = 0
输出：5
解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        height = len(matrix)
        width = len(matrix[0])

        cnt = 0

        np_arr = np.array(matrix)
        print(np_arr[0:2][1])
        for i in range(height):
            for j in range(width):
                for k in range(j, width):
                    if matrix[i][j:k + 1] and sum(matrix[i][j:k + 1]) == target:
                        cnt += 1

        return cnt


if __name__ == "__main__":
    matrix = [[1, -1],
              [-1, 1]]
    matrix = [[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))
