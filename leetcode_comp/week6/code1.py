# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/16 10:29 AM
@Author  : ddlee
@File    : code1.py
"""
import random

"""
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

"""


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        tmp = arr.copy()

        idx = 0
        for i in range(l):
            if idx < l:
                if tmp[i] == 0:
                    arr[idx] = 0
                    idx += 1
                    if idx < l:
                        arr[idx] = 0
                        idx += 1
                else:
                    arr[idx] = tmp[i]
                    idx += 1
            else:
                break
        print(arr)
        return


if __name__ == '__main__':
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    print(Solution().duplicateZeros(arr))
