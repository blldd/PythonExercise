# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/4 2:34 PM
@Author  : ddlee
@File    : findRedundantDirectedConnection.py
"""
"""
685. 冗余连接 II
在本问题中，有根树指满足以下条件的有向图。
该树只有一个根节点，所有其他节点都是该根节点的后继。
每一个节点只有一个父节点，除了根节点没有父节点。

输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。 
每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u and v和顶点的边，其中父节点u是子节点v的一个父节点。

返回一条能删除的边，使得剩下的图是有N个节点的有根树。
若有多个答案，返回最后出现在给定二维数组的答案。

示例 1:
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的有向图如下:
  1
 / \
v   v
2-->3
"""


class Solution:
    def findRedundantDirectedConnection(self, edges):
        pass


if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    print(Solution().findRedundantDirectedConnection(edges))