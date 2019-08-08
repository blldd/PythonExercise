# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/8 7:58 PM
@Author  : ddlee
@File    : 64minPathSum.py
"""

"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid):
        def dfs(grid, i, j, res):
            return res

        res = 0
        res = dfs(grid, 0, 0, res)
        return


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print(Solution().minPathSum(grid))
