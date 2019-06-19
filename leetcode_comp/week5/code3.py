# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/9 10:59 AM
@Author  : ddlee
@File    : code3.py
"""
import copy

"""
5084. 根到叶路径上的不足节点
给定二叉树的根 root，考虑所有从根到叶的路径：从根到任何叶的路径。 （叶节点是没有子节点的节点。）

如果交于节点 node 的每个根到叶路径的总和严格小于限制 limit，则该节点为不足节点。

同时删除所有不足节点，并返回生成的二叉树的根。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sufficientSubset(self, root, limit):
        return


if __name__ == '__main__':
    arr1 = [1, 1, 1, 1, 1]
    arr2 = [1, 0, 1]
    print(Solution().addNegabinary(arr1, arr2))
