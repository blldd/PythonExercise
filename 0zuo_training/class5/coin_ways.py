# -*- coding:UTF-8 -*-

def coin(arr, target):
    """
    给定一个正数数组arr，arr[i]表示第i种货币的面值，可以使用任意张。
    给定一个正 target，返回组成aim的方法数有多少种?
    动态规划优化状态依赖的技巧
    :return:
    """
    if len(arr) < 1 or target < 0:
        return 0
    return process(arr, 0, target)


def process(arr, index, target):
    res = 0
    if index == len(arr):
        res = 1 if target == 0 else 0
    else:
        i = 0
        while arr[index] * i <= target:
            res += process(arr, index + 1, target - arr[index] * i)
            i += 1
    return res


def coin_dp_compress(arr, target):
    """
    给定一个正数数组arr，arr[i]表示第i种货币的面值，可以使用任意张。
    给定一个正 target，返回组成aim的方法数有多少种?
    动态规划优化状态依赖的技巧
    :return:
    """
    if len(arr) < 1 or target < 0:
        return 0

    dp = [0 for i in range(target + 1)]
    j = 0
    while arr[0] * j <= target:
        dp[arr[0] * j] = 1
        j += 1

    for i in range(1, len(arr)):
        for j in range(1, target + 1):
            dp[j] += dp[j - arr[i]] if j - arr[i] >= 0 else 0

    print(dp)
    return dp[target]


def coin_dp(arr, target):
    if len(arr) < 1 or target < 0:
        return 0

    dp = [[0 for i in range(target + 1)] for j in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 1
    j = 0
    while arr[0] * j <= target:
        dp[0][arr[0] * j] = 1
        j += 1

    for i in range(1, len(arr)):
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i][j - arr[i]] if j - arr[i] >= 0 else 0
    for i in dp:
        print(i)
    return dp[len(arr) - 1][target]


if __name__ == '__main__':
    arr = [1, 2, 5, 10, 25]
    target = 20
    print(coin_dp_compress(arr, target))
    print(coin_dp(arr, target))
