# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 11:04 AM
@Author  : ddlee
@File    : code4.py
"""
import collections

"""
1054. 距离相等的条形码
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

示例 1：
输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]

示例 2：
输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
"""


class Solution:
    def rearrangeBarcodes(self, barcodes):
        l = len(barcodes)
        if l <= 2:
            return barcodes

        res = [0 for i in range(l)]
        d = collections.Counter(barcodes)
        for item in d.items():
            key, times = item
            for i in range(times):
                res



if __name__ == "__main__":
    # string = "Ask not what your country can do for you, but what you can do for your country"
    barcodes = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(Solution().rearrangeBarcodes(barcodes))
