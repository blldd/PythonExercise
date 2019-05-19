# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:59 AM
@Author  : ddlee
@File    : code3.py
"""


class Solution:
    """
    5065. 最长字符串链  显示英文描述

    给出一个单词列表，其中每个单词都由小写英文字母组成。
    如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。
    例如，"abc" 是 "abac" 的前身。
    词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，
    其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。
    从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。

    示例：
    输入：["a","b","ba","bca","bda","bdca"]
    输出：4
    解释：最长单词链之一为 "a","ba","bda","bdca"。
    """

    def longestStrChain(self, words):
        l = len(words)
        if l < 2:
            return l

        def check(a, b):
            if len(b) == len(a) + 1:
                seta = set(a)
                setb = set(b)
                for char in seta:
                    if char not in setb:
                        return False
                return True
            else:
                return False

        dp = [1 for i in range(l)]
        # dp[0] = 1
        for i in range(1, l):
            for idx in range(1, i)[::-1]:
                if check(words[i - idx], words[i]):
                    dp[i] = max(dp[i], dp[i - idx] + 1)
                else:
                    dp[i] = max(dp[i], dp[i - idx])
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    # words = ["a", "b", "ba", "bca", "bda", "bdca"]
    words = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
             "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
    print(Solution().longestStrChain(words))
