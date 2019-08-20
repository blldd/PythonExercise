# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/19 10:58 PM
@Author  : ddlee
@File    : 721accountsMerge.py
"""
import collections


class Solution:
    def accountsMerge(self, accounts):
        l = len(accounts)
        if l <= 1:
            return accounts

        dictt = collections.defaultdict(set)
        for i in range(l):
            for mail in accounts[i][1:]:
                dictt[mail].add(i)
        print(dictt)



if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]

    print(Solution().accountsMerge(accounts))
