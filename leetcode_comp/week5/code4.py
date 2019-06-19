# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/9 11:04 AM
@Author  : ddlee
@File    : code4.py
"""
import collections
import numpy as np

"""
5086. 不同字符的最小子序列
返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。

示例 1：
输入："cdadabcc"
输出："adbc"

示例 2：
输入："abcd"
输出："abcd"

示例 3：
输入："ecbacba"
输出："eacb"

示例 4：
输入："leetcode"
输出："letcod"
"""


class Solution:
    def smallestSubsequence(self, text):
        res = ""
        _set = set(text)

        def recursive(res, text, _set):
            if not _set or not text:
                return res

            l = len(text)
            for i in range(l)[::-1]:
                tail_str = text[i:]

                flag = True
                for ch in _set:
                    if ch not in tail_str:
                        flag = False
                        break

                if flag == True:
                    head_str = text[:i]

                    if head_str:
                        node = min(head_str)
                        res += node
                        text = text[i:]
                        _set.remove(node)
                    else:
                        node = text[0]
                        res += node
                        text = text[1:]
                        _set.remove(node)
                    break

            return recursive(res, text, _set)

        return recursive(res, text, _set)


if __name__ == "__main__":
    text = "cdadabcc"
    print(Solution().smallestSubsequence(text))
