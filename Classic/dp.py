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


def maxProductAfterCutting(n):
    """
    剪绳子, 求乘积最大
    :param n:
    :return:
    """
    if n < 2:
        return 0
    if n == 2:
        return 1
    max_list = [0, 1, 2]
    for i in range(3, n + 1):
        if i < n:
            m = i
        else:
            m = 0
        for j in range(1, i // 2 + 1):
            tmp = max_list[j] * max_list[i - j]
            m = max(m, tmp)

        max_list.append(m)
    print(max_list)
    return max_list[n]


def penguin_merge_near(arr):
    """
    企鹅合体，只能合体一次，只能和左右其中的一个合体，合体即乘积，有可能为负数
    :param arr:
    :return:
    """
    length = len(arr)
    if length < 1:
        return 0
    elif length == 1:
        return arr[0]
    elif length == 2:
        return max(arr[0] + arr[1], arr[0] * arr[1])

    dp = [0 for i in range(length + 1)]
    dp[1] = arr[0]
    dp[2] = max(arr[0] + arr[1], arr[0] * arr[1])
    if length > 2:
        for i in range(3, length + 1):
            dp[i] = max(dp[i - 1] + arr[i - 1], dp[i - 2] + arr[i - 1] * arr[i - 2])
    return dp[-1]


def penguin_merge(arr):
    """
    企鹅合体，只能合体一次，合体即乘积，有可能为负数
    由于不指定顺序，因此可以先排序，-5, -3, 0, 1, 3, 5
    :param arr:
    :return:
    """
    length = len(arr)

    arr = sorted(arr)
    if length < 1:
        return 0
    elif length == 1:
        return arr[0]
    elif length == 2:
        return max(arr[0] + arr[1], arr[0] * arr[1])

    ans = 0
    if length > 2:
        l = 0
        r = length - 1
        while r > 0:
            if arr[r-1] > 1:
                ans += arr[r] * arr[r-1]
                r -= 2
            else:
                break
        while l < r:
            if arr[l+1] <= 0:
                ans += arr[l] * arr[l+1]
                l += 2
            else:
                break
        while l <= r:
            ans += arr[l]
            l += 1
    return ans




if __name__ == '__main__':
    s = "google"
    # print(palindrome_seq(s))
    s = [5, 2, 1, 4, 6, 9, 7, 8]
    # lis(s)
    # print(lis2(s))
    # print(maxProductAfterCutting(16))
    s = [-5, -3, 0, 1, 3, 5]
    print(penguin_merge(s))
