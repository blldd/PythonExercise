# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/16 11:04 AM
@Author  : ddlee
@File    : code4.py
"""
import collections
import numpy as np

"""
1106. 解析布尔表达式 
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。

有效的表达式需遵循以下约定：
"t"，运算结果为 True
"f"，运算结果为 False
"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）

示例 1：
输入：expression = "!(f)"
输出：true

示例 2：
输入：expression = "|(f,t)"
输出：true

示例 3：
输入：expression = "&(t,f)"
输出：false

示例 4：
输入：expression = "|(&(t,f,t),!(t))"
输出：false
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def get_operation_res(arr, op):
            if op == "&":
                for i in arr:
                    if i == 'f':
                        return "f"
                return "t"
            elif op == "|":
                for i in arr:
                    if i == "t":
                        return "t"
                return "f"

            elif op == "!":
                for i in arr:
                    if i == "t":
                        return "f"
                    elif i == "f":
                        return "t"

        stack = []
        for ch in expression:
            if ch != ')':
                stack.append(ch)
            else:
                session = []
                while stack:
                    tmp = stack.pop()
                    if tmp != '(':
                        session.append(tmp)
                    else:
                        op = stack.pop()
                        break
                session = "".join(session)
                session = session.split(",")
                res = get_operation_res(session, op)
                stack.append(res)
        for i in stack:
            if i == 'f':
                return False
            elif i == 't':
                return True


if __name__ == "__main__":
    expression = "!(f)"
    # expression = "|(&(t,f,t),!(t))"
    expression = "|(f,t)"
    expression = "&(t,f)"
    print(Solution().parseBoolExpr(expression))
