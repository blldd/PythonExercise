# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:53 AM
@Author  : ddlee
@File    : code2.py
"""


class Solution:
    """
    5064. 删除字符串中的所有相邻重复项  显示英文描述
    给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

    在 S 上反复执行重复项删除操作，直到无法继续删除。

    在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
    输入："abbaca"
    输出："ca"
    解释：
    例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
    之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
    """

    def removeDuplicates(self, S):
        start = 0
        while S:
            l = len(S)
            if l < 2:
                return S
            cnt = start + 1
            for i in range(start, l - 1):
                if S[i] == S[i + 1]:
                    S = S[:i] + S[i+2:]
                    if i > 0:
                        start = i-1
                    break
                else:
                    cnt += 1
            if cnt == l:
                return S
        return ""

if __name__ == '__main__':
    S = "ffjfaldjjtttn"
    print(Solution().removeDuplicates(S))
