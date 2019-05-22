# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 11:04 AM
@Author  : ddlee
@File    : code4.py
"""


class Solution:
    """
    1049. 最后一块石头的重量 II  显示英文描述

    有一堆石头，每块石头的重量都是正整数。

    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

    示例：
    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
    """

    def lastStoneWeightII(self, stones):
        '''动态规划 背包问题'''
        l = len(stones)
        if l < 1:
            return 0

        half = sum(stones) // 2  # 背包最大放的重量
        dp = [[0 for j in range(half + 1)] for i in range(l + 1)]
        for i in range(1, l + 1):
            for j in range(1, half + 1):
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])

        for i in dp:
            print(i)
        return sum(stones) - (2 * dp[-1][-1])


if __name__ == "__main__":
    # string = "Ask not what your country can do for you, but what you can do for your country"
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeightII(stones))
