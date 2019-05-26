# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 10:53 AM
@Author  : ddlee
@File    : code2.py
"""
import sys

"""
1052. 爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。
每分钟都有一些顾客（customers[i]）进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 
当书店老板生气时，那一分钟的顾客就会不满意，否则他们是满意的。
书店老板知道一个秘密技巧，可以让自己连续 X 分钟不生气，但只能使用一次。
返回全天可满足的最大客户数量。
 
示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
可满足的最大客户数 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""


class Solution:
    def maxSatisfied1(self, customers, grumpy, X) -> int:
        l = len(grumpy)
        if l <= X:
            return sum(customers)

        res = sys.maxsize
        for i in range(l - X + 1):
            new_grumpy = grumpy[:i] + [0] * X + grumpy[i + X:]
            # print(new_grumpy)
            tmp = 0
            for j in range(l):
                if new_grumpy[j] == 1:
                    tmp += customers[j]
                    # print(tmp)
            res = min(res, tmp)
            # print(res)
        return sum(customers) - res

    def maxSatisfied2(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        # for i in range(len(grumpy)):
        #     grumpy[i] = 1 - grumpy[i]

        l = len(grumpy)
        if l <= X:
            return sum(customers)

        dp = [0 for i in range(l + 1)]
        cnt = 0
        for i in range(l):
            if not grumpy[i]:
                cnt += customers[i]
            dp[i + 1] = dp[i] + customers[i] * grumpy[i]
        print(dp)
        print(cnt)

        ans = 0
        for i in range(1, l + 1):
            j = max(i - X, 0)
            ans = max(ans, cnt + dp[i] - dp[j])

        return ans

    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        now = 0
        ans = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                now += customers[i]
        print(now)
        for i in range(X):
            if grumpy[i] == 1:
                now += customers[i]
        print(now)

        ans = max(now, ans)
        for head in range(len(customers) - X):
            if grumpy[head] == 1:
                now -= customers[head]
            if grumpy[head + X] == 1:
                now += customers[head + X]
            ans = max(now, ans)
        return ans


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
    # customers = [4, 10, 10]
    # grumpy = [1, 1, 0]
    X = 3

    print(Solution().maxSatisfied(customers, grumpy, X))
