# -*- coding:UTF-8 -*-

def get_dp_arb(arr, money):
    """
    :param arbitrary:
    :param money:
    :return:
    """
    length = len(arr)
    if arr == None or length == 0:
        return None
    dp = [[0 for j in range(money + 1)] for i in range(length)]
    for i in range(length):
        dp[i][0] = 1
    j = 1
    while arr[0] * j <= money:
        dp[0][arr[0] * j] = 1
        j += 1
    for i in range(1, length):
        for j in range(1, money + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i][j - arr[i]] if j - arr[i] >= 0 else 0
    return dp


def get_dp_one(arr, money):
    """
    :param arr:
    :param money:
    :return:
    """
    length = len(arr)
    if arr == None or length == 0:
        return None
    dp = [[0 for j in range(money + 1)] for i in range(length)]
    for i in range(length):
        dp[i][0] = 1
    if arr[0] <= money:
        dp[0][arr[0]] = 1
    for i in range(1, length):
        for j in range(1, money + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i - 1][j - arr[i]] if j - arr[i] >= 0 else 0
    return dp


def money_ways(arbitrary, onlyone, money):
    """
	现有n1+n2种面值的硬币，其中前n1种为普通币，可以取任意枚，
	后n2种为纪念币，每种最多只能取一枚，每种硬币有一个面值，问能用多少种方法拼出m的面值?
    :return:
    """
    if money < 0:
        return 0
    if (arbitrary == None or len(arbitrary) == 0) and (onlyone == None or len(onlyone) == 0):
        return 1 if money == 0 else 0
    dparb = get_dp_arb(arbitrary, money)
    dpone = get_dp_one(onlyone, money)
    if dparb == None:
        return dpone[len(dpone) - 1][money]
    if dpone == None:
        return dparb[len(dparb) - 1][money]
    res = 0
    for i in range(money + 1):
        res += dparb[len(dparb) - 1][i] * dpone[len(dpone) - 1][money - i]
    return res


if __name__ == '__main__':
    money_ways()
