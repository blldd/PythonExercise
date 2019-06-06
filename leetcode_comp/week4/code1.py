# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/2 10:29 AM
@Author  : ddlee
@File    : code1.py
"""
import random

"""
5076. 字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：
输入：str1 = "LEET", str2 = "CODE"
输出：""
"""


class Solution:
    def gcdOfStrings(self, str1, str2):
        X = ""

        l1 = len(str1)
        l2 = len(str2)

        if l1 < 1 or l2 < 1:
            return X

        '''asure l1 >= l2'''
        if l1 < l2:
            str1, str2 = str2, str1
            l1, l2 = l2, l1

        def get_loop_str(in_str):
            loop_strs = []

            first_ch = in_str[0]
            for i in range(1, l2):
                if in_str[i] == first_ch:
                    loop = i
                    loop_str = in_str[:i]
                    last_str = in_str[i:]
                    flag = True
                    # for ch in last_str:
                    for i in range(0, len(last_str), loop):
                        if last_str[i:i + loop] != loop_str:
                            '''not a loop_str'''
                            flag = False
                            break

                    '''get loop_str'''
                    if i == len(last_str) - loop and flag == True:
                        loop_strs.append(loop_str)
            '''add self'''
            loop_strs.append(in_str)

            return loop_strs

        loop_strs = get_loop_str(str2)

        for ls in loop_strs[::-1]:
            if ls == str1:
                return str1

            loop = len(ls)

            flag = True
            commen_str = ""
            for i in range(0, len(str1), loop):
                if str1[i:i + loop] != ls:
                    '''not a loop_str'''
                    flag = False
                    break
            if i == len(str1) - loop and flag == True:
                commen_str = ls
                return commen_str

        return commen_str


if __name__ == '__main__':
    str1 = "AAAAAAAA"
    str2 = "AAAA"
    print(Solution().gcdOfStrings(str1, str2))
