# -*- coding:UTF-8 -*-
import numpy as np


# 朴素匹配
def naive_match(s, p):
    m = len(s);
    n = len(p)
    for i in range(m - n + 1):  # 起始指针i
        if s[i:i + n] == p:
            return True
    return False


# KMP
def kmp_match(s, p):
    m = len(s);
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret


def print_lcsequence(input_x, input_y, i, j, flag, lcs):
    if (i == 0 or j == 0):
        return
    if flag[i][j] == 0:
        print_lcsequence(input_x, input_y, i - 1, j - 1, flag, lcs)
        lcs.append(input_x[i - 1])
    elif (flag[i][j] == 1):
        print_lcsequence(input_x, input_y, i - 1, j, flag, lcs)
    else:
        print_lcsequence(input_x, input_y, i, j - 1, flag, lcs)
    return lcs


def lcsequence(input_x, input_y):
    lcsequence_mat, flag = lcsequence_dp(input_x, input_y)
    i = len(input_x)
    j = len(input_y)
    lcs = []
    lcs = print_lcsequence(input_x, input_y, i, j, flag, lcs)
    print((lcsequence_mat[-1][-1], lcs))


# 最长公共子序列
def lcsequence_dp(input_x, input_y):
    # input_y as column, input_x as row
    dp = [([0] * (len(input_y) + 1)) for i in range(len(input_x) + 1)]
    flag = [([0] * (len(input_y) + 1)) for i in range(len(input_x) + 1)]
    for i in range(1, len(input_x) + 1):
        for j in range(1, len(input_y) + 1):
            if input_x[i - 1] == input_y[j - 1]:  # 不在边界上，相等就加一
                dp[i][j] = dp[i - 1][j - 1] + 1
                flag[i][j] = 0
            elif dp[i - 1][j] > dp[i][j - 1]:  # 不相等
                dp[i][j] = dp[i - 1][j]
                flag[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1]
                flag[i][j] = -1
    for dp_line in dp:
        print(dp_line)
    return dp, flag


# 最长公共子串
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    for i in record:
        print(i)
    return str1[p - maxNum:p], maxNum


# 编辑距离
def _levenshtein_distance(input_x, input_y):
    xlen = len(input_x) + 1  # 此处需要多开辟一个元素存储最后一轮的计算结果
    ylen = len(input_y) + 1

    dp = np.zeros(shape=(xlen, ylen), dtype=int)
    for i in range(0, xlen):
        dp[i][0] = i
    for j in range(0, ylen):
        dp[0][j] = j

    for i in range(1, xlen):
        for j in range(1, ylen):
            if input_x[i - 1] == input_y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[xlen - 1][ylen - 1]


if __name__ == '__main__':
    # print(naive_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
    # print(partial_table("ABCDABD"))
    # print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))

    x = "beauty"
    y = "batyu"

    print(lcsequence(x, y))
    print(getNumofCommonSubstr(x, y))
