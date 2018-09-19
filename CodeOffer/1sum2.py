# -*- coding:utf-8 -*-

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp
        return num1


if __name__ == '__main__':
    num1 = 5
    num2 = 7
    print(Solution().Add(num1, num2))
