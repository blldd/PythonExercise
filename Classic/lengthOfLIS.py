# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/17 9:11 AM
@Author  : ddlee
@File    : lengthOfLIS.py
"""
import sys


class Solution:
    def lengthOfLIS_1(self, nums) -> int:
        l = len(nums) + 1

        dp = [1 for i in range(l)]
        dp[0] = 0
        for i in range(1, l):
            for j in range(i, l):
                if nums[i - 1] < nums[j - 1]:
                    dp[j] = max(dp[i] + 1, dp[j])
        # print(dp)
        return max(dp)

    def lengthOfLIS(self, nums) -> int:
        l = len(nums)
        if l < 2:
            return l

        tail = [sys.maxsize]

        for num in nums:
            # 找到大于等于 num 的第 1 个数
            le = 0
            ri = len(tail)
            while le < ri:
                mid = le + (ri - le) // 2
                if tail[mid] < num:
                    le = mid + 1
                else:
                    ri = mid
            if le == len(tail):
                tail.append(num)
            else:
                tail[le] = num

        # print(tail)
        return len(tail)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [4, 10, 4, 3, 8, 9]

    print(Solution().lengthOfLIS(nums))
