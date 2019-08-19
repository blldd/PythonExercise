# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/19 9:51 PM
@Author  : ddlee
@File    : 102levelOrder.py
"""

from util_tools import build_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        pass


if __name__ == '__main__':
    arr = [3, 9, 20, "", "", 15, 7]
    root = build_tree(arr)

    print(Solution().levelOrder(root))
