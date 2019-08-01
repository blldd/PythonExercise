# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/31 10:00 PM
@Author  : ddlee
@File    : 673findNumberOfLIS.py
"""
import sys

"""
673. 最长递增子序列的个数

给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""


class Solution:
    def findNumberOfLIS(self, nums):
        l = len(nums)
        if l < 2:
            return l

        cnt_arr = [0]
        cnt = 0
        idx = 0
        tail = [sys.maxsize]
        for num in nums:
            # 找到大于等于 num 的第 1 个数
            # 经典二分查找
            le = 0
            ri = len(tail)
            while le < ri:
                mid = le + (ri - le) // 2
                if tail[mid] >= num:
                    ri = mid
                else:
                    le = mid + 1

            if le == len(tail):
                tail.append(num)
                cnt = 1
                cnt_arr.append(cnt)
                idx += 1
            else:
                tail[le] = num
                cnt += 1
                cnt_arr[idx] = cnt

        print(tail)
        print(cnt_arr)
        res = 1
        for i in cnt_arr:
            res *= i

        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    # nums = [2, 2, 2, 2, 2]
    nums = [1, 2, 4, 3, 5, 4, 7, 2]
    print(Solution().findNumberOfLIS(nums))
