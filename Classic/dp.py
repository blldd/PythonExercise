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
            dp[i][j] = dp[i - 1][j - 1] + 1 if s[i-1] == rs[j-1] else max(dp[i][j - 1], dp[i - 1][j])
    for i in dp:
        print(i)
    return length - dp[length][length]


if __name__ == '__main__':
    s = "google"
    print(palindrome_seq(s))
