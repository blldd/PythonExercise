# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/16 8:49 PM
@Author  : ddlee
@File    : 523checkSubarraySum.py
"""


class Solution:
    # 超时
    def checkSubarraySum1(self, arr, target):
        l = len(arr)
        if l < 1:
            return False

        for i in range(l):
            for j in range(i + 2, l + 1):
                tmp = sum(arr[i:j])
                if target == tmp:
                    return True

                if target != 0 and tmp % target == 0:
                    return True

        return False

    # 超时
    def checkSubarraySum2(self, arr, target):
        l = len(arr)
        if l <= 1:
            return False

        l = l - 1
        dp = [[0 for _ in range(l)] for _ in range(l)]
        dp[0][0] = arr[0] + arr[1]

        if (target == 0 and dp[0][0] == 0) or (target != 0 and (dp[0][0] % target) == 0):
            return True

        for i in range(l):
            for j in range(i + 1):
                if i != j:
                    dp[i][j] = dp[i - 1][j] + arr[i + 1]
                else:
                    dp[i][j] = arr[i] + arr[i + 1]
                if (target == 0 and dp[i][j] == 0) or (target != 0 and (dp[i][j] % target) == 0):
                    return True
        return False
        # for i in dp:
        #     print i

    # 同余法
    # Sa - Sb  = n*k
    # Sa = Sb mod k
    def checkSubarraySum(self, arr, target):
        l = len(arr)
        if l <= 1:
            return False

        target = abs(target)
        if target == 0:
            for i in range(1, l):
                if ((arr[i] == 0) & (arr[i - 1] == 0)):
                    return True
            return False

        # 字典存储余数
        d = set()
        sum = arr[0]
        d.add(sum % target)
        # case [1,1] k=2
        d.add(0)

        for i in range(1, l):
            sum += arr[i]
            tmp = sum % target
            # 0 0 这种
            if ((arr[i] % target == 0) & (arr[i - 1] % target == 0)):
                return True
            # 1 0 这种 case
            if arr[i] % target == 0:
                continue
            if tmp not in d:
                d.add(tmp)
            else:
                return True
        return False


if __name__ == '__main__':
    arr = [23, 2, 4, 6, 7]
    target = 6
    arr = [1, 1]
    target = 2

    print(Solution().checkSubarraySum(arr, target))
    print(Solution().checkSubarraySum1(arr, target))
