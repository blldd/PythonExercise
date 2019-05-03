# -*- coding:UTF-8 -*-
"""
动态规划：
- 自底向上
就是已经知道了所有递归边界，把所有可能的状态都算出来。
从初始已知的状态出发，向外拓展，最后到达目标状态。

- 自顶向下（“记忆化搜索”）
从最终状态开始，找到可以到达当前状态的状态，如果该状态还没处理，就先处理该状态。
自顶向下通常使用递归实现

-总结
自顶向下，自底向上，只是动态规划实现的套路而已。复杂度并没有多大的变化。
事实上大多时候用自顶向下复杂度会更低，因为可以过滤掉更多无用的状态；
不过自底向上可以避免爆栈问题，而且实现往往实现更为简单。
"""
import sys


# 编辑距离
def levenshtein_distance_dp(input_x, input_y):
    xlen = len(input_x) + 1
    ylen = len(input_y) + 1

    # 此处需要多开辟一个元素存储最后一轮的计算结果
    dp = [[0 for i in range(xlen)] for j in range(ylen)]
    for i in range(xlen):
        dp[i][0] = i
    for j in range(ylen):
        dp[0][j] = j

    for i in range(1, xlen):
        for j in range(1, ylen):
            if input_x[i - 1] == input_y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[xlen - 1][ylen - 1]


# 最长公共子串
def longest_common_substr_dp(str1, str2):
    xlen = len(str1) + 1
    ylen = len(str2) + 1
    record = [[0 for i in range(ylen)] for j in range(xlen)]
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(1, xlen):
        for j in range(1, ylen):
            if str1[i - 1] == str2[j - 1]:
                # 相同则累加
                record[i][j] = record[i - 1][j - 1] + 1
                if record[i][j] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i][j]
                    # 记录最大匹配长度的终止位置
                    p = i
    for i in record:
        print(i)
    return str1[p - maxNum:p], maxNum


# 最长公共子序列
def longest_common_sequence(input_x, input_y):
    lcsequence_mat, flag = longest_common_sequence_dp(input_x, input_y)
    i = len(input_x)
    j = len(input_y)
    lcs = []
    get_lcs(input_x, input_y, i, j, flag, lcs)
    print((lcsequence_mat[-1][-1], lcs))


def longest_common_sequence_dp(input_x, input_y):
    xlen = len(input_x) + 1
    ylen = len(input_y) + 1
    dp = [([0] * ylen) for i in range(xlen)]
    flag = [([0] * ylen) for i in range(xlen)]
    for i in range(1, xlen):
        for j in range(1, ylen):
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


def get_lcs(input_x, input_y, i, j, flag, lcs):
    if (i == 0 or j == 0):
        return
    if flag[i][j] == 0:
        get_lcs(input_x, input_y, i - 1, j - 1, flag, lcs)
        lcs.append(input_x[i - 1])
    elif (flag[i][j] == 1):
        get_lcs(input_x, input_y, i - 1, j, flag, lcs)
    else:
        get_lcs(input_x, input_y, i, j - 1, flag, lcs)
    return lcs


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
            if arr[r - 1] > 1:
                ans += arr[r] * arr[r - 1]
                r -= 2
            else:
                break
        while l < r:
            if arr[l + 1] <= 0:
                ans += arr[l] * arr[l + 1]
                l += 2
            else:
                break
        while l <= r:
            ans += arr[l]
            l += 1
    return ans


def most_eor(arr):
    """
	给出n个数字 a_1,...,a_n，问最多有多少不重叠的非空区间，使得每个区间内数字的 xor都等于0。
    :param arr:
    :return:
    """
    ans = 0
    xor = 0
    length = len(arr)

    mosts = [0 for i in range(length)]
    map = {}
    map[0] = -1

    for i in range(length):
        xor ^= arr[i]
        if xor in map:
            pre = map[xor]  # 找到那个开头位置
            mosts[i] = 1 if pre == -1 else (mosts[pre] + 1)  # 开头位置的最大值 + 1
        if i > 0:
            mosts[i] = max(mosts[i - 1], mosts[i])  # 只依赖前i-1 和 i 两种情况

        map[xor] = i
        ans = max(ans, mosts[i])
    return ans


def coins_min_combine(arr, target):
    if target <= 0 or target > 1024:
        raise ValueError

    dp = [0 for i in range(target + 1)]
    for i in range(1, target + 1):
        c = sys.maxsize
        for coin in arr:
            if i - coin >= 0:
                c = min(c, dp[i - coin] + 1)
        dp[i] = c
    return dp[-1]


def coin_ways(arr, target):
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


def coin_ways_dp_compress(arr, target):
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


def _split_process(pre, rest):
    if rest == 0:
        return 1
    if pre > rest:
        return 0
    ways = 0
    for i in range(pre, rest + 1):
        ways += _split_process(i, rest - i)
    return ways


def split_ways(n):
    if n < 1:
        return 0
    return _split_process(1, n)


# def split_ways_dp(n):
#     if n < 1:
#         return 0
#     dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
#     for i in range(1, n + 1):
#         dp[i][0] = 1
#     for pre in range(1, n + 1)[::-1]:
#         for rest in range(pre, n + 1):
#             for i in range(pre, rest + 1):
#                 dp[pre][rest] += dp[i][rest - i]
#     return dp[1][n]

def split_ways_dp(n):
    if n < 1:
        return 0
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        dp[i][i] = 1
    for pre in range(1, n)[::-1]:
        for rest in range(pre + 1, n + 1):
            dp[pre][rest] = dp[pre + 1][rest] + dp[pre][rest - pre]

    return dp[1][n]


"""
	public static int ways3(int n) {
		if (n < 1) {
			return 0;
		}
		int[][] dp = new int[n + 1][n + 1];
		for (int pre = 1; pre < dp.length; pre++) {
			dp[pre][0] = 1;
		}
		for (int pre = 1; pre < dp.length; pre++) {
			dp[pre][pre] = 1;
		}
		for (int pre = n - 1; pre > 0; pre--) {
			for (int rest = pre + 1; rest <= n; rest++) {
				dp[pre][rest] = dp[pre + 1][rest] + dp[pre][rest - pre];
			}
		}
		return dp[1][n];
	}
"""

if __name__ == '__main__':
    s = "abacdgfdcaba"
    print(palindrome_seq(s))
    print("**" * 10)
    s = [5, 2, 1, 4, 6, 9, 7, 8]
    # lis(s)
    # print(lis2(s))
    # print(maxProductAfterCutting(16))
    s = [-5, -3, 0, 1, 3, 5]
    # print(penguin_merge(s))

    print(coins_min_combine([1, 5, 11], 15))
    print(coin_ways([1, 5, 10], 27))
    print(coin_ways_dp_compress([1, 5, 10], 27))

    # for i in range(10):
    #     print(split_ways(i), split_ways_dp(i))
