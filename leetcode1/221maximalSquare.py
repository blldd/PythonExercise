# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/18 8:09 AM
@Author  : ddlee
@File    : 221maximalSquare.py
"""
import math


class Solution:
    def maximalSquare1(self, matrix):
        if len(matrix) < 1:
            return 0

        matrix = [list(map(int, row)) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    if matrix[i - 1][j - 1] == 1:
                        for ind in range(1, int(math.sqrt(dp[i - 1][j - 1]) + 1)):
                            if matrix[i - ind][j] == 1 and matrix[i][j - ind] == 1:
                                dp[i][j] = int(pow(ind + 1, 2))
                            else:
                                dp[i][j] = int(pow(ind + 1 - 1, 2))
                                break
                    else:
                        dp[i][j] = 1
        return max(map(max,dp))

    """
    计算边长，比上一种方案好
    """
    def maximalSquare(self, matrix):
        if len(matrix) < 1:
            return 0

        matrix = [list(map(int, row)) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        for i in dp:
            print(i)
        return pow(max(map(max,dp)), 2)


if __name__ == '__main__':
    mat = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "0", "1", "0"]]
    # mat = [["1", "0", "0"],
    #        ["0", "0", "0"],
    #        ["1", "1", "1"]]
    # mat = [["1"], ["0"]]
    # mat = [["0", "0", "0", "1"],
    #        ["1", "1", "0", "1"],
    #        ["1", "1", "1", "1"],
    #        ["0", "1", "1", "1"],
    #        ["0", "1", "1", "1"]]

    print(Solution().maximalSquare(mat))

    # dp = [[0, 0, 0], [0, 6, 3], [0, 0, 0], [0, 19, 0], [3, 12, 5]]
    # print(max(dp))
    # print(max(max(dp)))
    # print(max(map(max,dp)))
