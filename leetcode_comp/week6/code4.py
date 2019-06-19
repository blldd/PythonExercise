# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/16 11:04 AM
@Author  : ddlee
@File    : code4.py
"""
import collections
import numpy as np

"""
1092. 最短公共超序列

给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。
如果答案不止一个，则可以返回满足条件的任意一个答案。
（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），
可以得到字符串 S，那么 S 就是 T 的子序列）

示例：
输入：str1 = "abac", str2 = "cab"
输出："cabac"
解释：
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。
"""


class Solution:
    def shortestCommonSupersequence(self, str1, str2):

        # 最长公共子序列
        def longest_common_sequence(input_x, input_y):
            lcsequence_mat, flag = longest_common_sequence_dp(input_x, input_y)
            i = len(input_x)
            j = len(input_y)
            lcs = []
            get_lcs(input_x, input_y, i, j, flag, lcs)
            print((lcsequence_mat[-1][-1], lcs))
            return lcs

        def longest_common_sequence_dp(input_x, input_y):
            xlen = len(input_x) + 1
            ylen = len(input_y) + 1
            dp = [([0] * ylen) for i in range(xlen)]
            flag = [([0] * ylen) for i in range(xlen)]
            for i in range(1, xlen):
                for j in range(1, ylen):
                    if input_x[i - 1] == input_y[j - 1]:  # 不在边界上，相等就加一
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        flag[i][j] = 0
                    elif dp[i - 1][j] > dp[i][j - 1]:  # 不相等
                        dp[i][j] = dp[i - 1][j]
                        flag[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                        flag[i][j] = -1
            # for dp_line in dp:
            #     print(dp_line)
            return dp, flag

        def get_lcs(input_x, input_y, i, j, flag, lcs):
            if (i == 0 or j == 0):
                return
            if flag[i][j] == 0:
                get_lcs(input_x, input_y, i - 1, j - 1, flag, lcs)
                lcs.append(input_x[i - 1])
            elif (flag[i][j] == 1):
                get_lcs(input_x, input_y, i - 1, j, flag, lcs)
            else:
                get_lcs(input_x, input_y, i, j - 1, flag, lcs)
            return lcs

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        lcs = longest_common_sequence(str1,  str2)

        res = ""
        id = 0

        for ch in str2:
            if id < len(lcs):
                if ch != lcs[id]:
                    res += ch
                else:
                    res += lcs[id]
                    id += 1
            else:
                res += ch
        print(res)
        id = 0
        for ch in str1:
            if id < len(lcs):
                if ch != lcs[id]:
                    res += ch
                else:
                    # res += lcs[id]
                    id += 1
            else:
                res += ch

        return res




if __name__ == "__main__":
    str1 = "abac"
    str2 = "cab"

    str1 = "bbbaaaba"
    str2 = "bbababbb"
    # bbababbbbaa
    # bbabaaababb
    print(Solution().shortestCommonSupersequence(str1, str2))
