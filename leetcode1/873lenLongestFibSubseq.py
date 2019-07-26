# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/24 10:32 PM
@Author  : ddlee
@File    : 873lenLongestFibSubseq.py
"""
"""
873. 最长的斐波那契子序列的长度
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：

n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

（回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

示例 1：
输入: [1,2,3,4,5,6,7,8]
输出: 5
解释:
最长的斐波那契式子序列为：[1,2,3,5,8] 。

示例 2：
输入: [1,3,7,11,12,14,18]
输出: 3
解释:
最长的斐波那契式子序列有：
[1,11,12]，[3,11,14] 以及 [7,11,18] 。
"""


class Solution:
    def lenLongestFibSubseq(self, A):
        l = len(A)
        if l < 3:
            return l

        dp = [[2 for _ in range(l + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):
            for j in range(i + 2, l + 1):
                for k in range(i + 1, j-1):
                    if A[j - 1] == A[k - 1] + A[i - 1]:
                        dp[i][j] = max(dp[i][j], dp[i][k] + 1)
                    # else:
                    #     dp[i][j] = dp[i][k]
        for i in dp:
            print(i)


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution().lenLongestFibSubseq(A))
