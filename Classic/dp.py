# -*- coding:UTF-8 -*-

def palindrome_seq(s):
    """
    给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长
    :return:
    """
    length = len(s)
    if length < 2:
        return 0
    rs = s[::-1]
    dp = [[0 for i in range(length + 1)] for j in range(length + 1)]
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            if s[i - 1] == rs[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            # dp[i][j] = dp[i - 1][j - 1] + 1 if s[i - 1] == rs[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
    for i in dp:
        print(i)
    return length - dp[length][length]


def lis(s):
    """
    好像有bug
    :param s:
    :return:
    """
    length = len(s)
    if length < 2:
        return length
    dp = [[0 for j in range(length + 1)] for i in range(length + 1)]
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            if s[i - 1] < s[j - 1] and i < j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    for i in dp:
        print(i)
    return dp


def lis2(s):
    """
    最长上升子序列，一维存储
    :param s:
    :return:
    """
    length = len(s)
    if length < 2:
        return length
    dp = [1 for i in range(length + 1)]
    dp[0] = 0

    for i in range(1, length + 1):
        for j in range(i, length + 1):
            if s[i - 1] < s[j - 1]:
                dp[j] = max(dp[i] + 1, dp[j])
    return dp

def lis3(s):
    """
    将原来的dp数组的存储由 数值 换成 该序列中，上升子序列长度为i的上升子序列，的最小末尾数值
    这其实就是一种几近贪心的思想：
    我们当前的上升子序列长度如果已经确定，那么如果这种长度的子序列的结尾元素越小，
    后面的元素就可以更方便地加入到这条我们臆测的、可作为结果、的上升子序列中。
    :param s:
    :return:
    """
    length = len(s)
    if length < 2:
        return length
    dp = [1 for i in range(length + 1)]
    dp[0] = 0




if __name__ == '__main__':
    s = "google"
    # print(palindrome_seq(s))
    s = [5, 2, 1, 4, 6, 9, 7, 8]
    lis(s)
    print(lis2(s))
