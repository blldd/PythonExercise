# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/9 10:29 AM
@Author  : ddlee
@File    : code1.py
"""
import random

"""
5083. Bigram 分词 
给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，
其中 second 紧随 first 出现，third 紧随 second 出现。
对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

示例 1：
输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

示例 2：
输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
"""


class Solution:
    def findOcurrences(self, text, first, second):
        res = []

        corpus = text.split()
        l = len(corpus)
        # print(corpus)
        for idx, word in enumerate(corpus):
            if word == first and idx + 2 < l and corpus[idx + 1] == second:
                res.append(corpus[idx + 2])

        return res


if __name__ == '__main__':
    text = "we will we will rock you we"
    first = "we"
    second = "will"
    print(Solution().findOcurrences(text, first, second))
