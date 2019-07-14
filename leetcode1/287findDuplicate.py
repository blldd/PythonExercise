# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/1 9:56 PM
@Author  : ddlee
@File    : 287findDuplicate.py
"""

"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


class Solution:
    def findDuplicate1(self, nums):
        l = len(nums)
        _max = 0
        _min = float('inf')

        for i in nums:
            if i > _max:
                _max = i
            if i < _min:
                _min = i

        if _min == _max:
            return _min

        n = _max - _min + 1

        return (sum(nums) - (_max + _min) * n // 2) // (l - n)

    def findDuplicate(self, nums):
        l = len(nums)
        _max = 0
        _min = float('inf')

        for i in nums:
            if i > _max:
                _max = i
            if i < _min:
                _min = i

        if _min == _max:
            return _min

        def get_num_btw_mn(nums, m, n):
            res = 0
            for i in nums:
                if i <= n and i >= m:
                    res += 1
            return res

        left = 0
        right = _max

        while left <= right:
            mid = (left +  right) // 2

            res = get_num_btw_mn(nums, left, mid)
            if res == mid - left + 1:
                left = mid
            elif res > mid - left + 1:
                left = mid
            elif res < mid - left + 1:
                pass




if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    nums = [1, 2, 2, 2, 2]
    nums = [1, 4, 4, 2, 4]

    print(Solution().findDuplicate(nums))