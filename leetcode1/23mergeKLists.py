# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/25 9:12 PM
@Author  : ddlee
@File    : 23mergeKLists.py
"""

# Definition for singly-linked list.
from util_tools import build_linklist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        pass


if __name__ == '__main__':
    arr = [1, 4, 5, 7]
    head1 = build_linklist(arr)

    arr = [1, 2, 3, 4]
    head2 = build_linklist(arr)

    arr = [2, 6, 8, 9]
    head3 = build_linklist(arr)
    arr = [head1, head2, head3]

    root = Solution().mergeKLists(arr)
    while root:
        print(root.val)
        root = root.next
