# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/16 10:59 AM
@Author  : ddlee
@File    : code3.py
"""
import copy

"""
1095. 山脉数组中查找目标值
（这是一个 交互式问题 ）

给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

如果不存在这样的下标 index，就请返回 -1。

 

所谓山脉数组，即数组 A 假如是一个山脉数组的话，需要满足如下条件：

首先，A.length >= 3

其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度


示例 1：
输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。

示例 2：
输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。

"""

"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""


class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        return self.arr[index]

    def length(self):
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target, mountain_arr):
        res = -1
        l = mountain_arr.length()

        def binary_search_target(l_idx, r_idx, target, ascend=True):
            res = -1

            if ascend:
                while l_idx <= r_idx:
                    m_idx = (l_idx + r_idx) // 2
                    mid = mountain_arr.get(m_idx)
                    if mid > target:
                        r_idx = m_idx - 1
                    elif mid == target:
                        res = m_idx
                        break
                    elif mid < target:
                        l_idx = m_idx + 1
            else:
                while l_idx <= r_idx:
                    m_idx = (l_idx + r_idx) // 2
                    mid = mountain_arr.get(m_idx)
                    if mid < target:
                        r_idx = m_idx - 1
                    elif mid == target:
                        res = m_idx
                        break
                    elif mid > target:
                        l_idx = m_idx + 1

            return res

        def binary_search_topid(l_idx, r_idx):
            t_idx = -1

            while l_idx <= r_idx:
                m_idx = (l_idx + r_idx) // 2
                mid = mountain_arr.get(m_idx)
                if mid < mountain_arr.get(m_idx - 1) and mid > mountain_arr.get(m_idx + 1):
                    r_idx = m_idx - 1
                elif mid > mountain_arr.get(m_idx - 1) and mid > mountain_arr.get(m_idx + 1):
                    t_idx = m_idx
                    break
                elif mid > mountain_arr.get(m_idx - 1) and mid < mountain_arr.get(m_idx + 1):
                    l_idx = m_idx + 1

            return t_idx

        l_idx, r_idx = 0, l - 1

        t_idx = binary_search_topid(l_idx, r_idx)
        # top = mountain_arr.get(t_idx)

        res = binary_search_target(l_idx, t_idx, target, ascend=True)
        if res == -1:
            res = binary_search_target(t_idx, r_idx, target, ascend=False)

        return res


if __name__ == '__main__':
    array = [3,5,3,2,0]

    mountain_arr = MountainArray(array)
    target = 0

    print(Solution().findInMountainArray(target, mountain_arr))
