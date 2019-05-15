# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 10:59 AM
@Author  : ddlee
@File    : code3.py
"""

class Solution:
    """
    给出整数数组 A，将该数组分隔为长度最多为 K 的几个（连续）子数组。
    分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。
    返回给定数组完成分隔后的最大和。


    输入：A = [1,15,7,9,2,5,10], K = 3
    输出：84
    解释：A 变为 [15,15,15,9,10,10,10]
    """

    def maxSumAfterPartitioning(self, A, K):
        """
        理解错题意，该解法针对：
        给出整数数组 A，将该数组分隔为为 K 个（连续）子数组。
        分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。
        返回给定数组完成分隔后的最大和。
        :param A:
        :param K:
        :return:
        """
        sorted_idxs = sorted(range(len(A)), key=A.__getitem__, reverse=True)
        top_k = sorted_idxs[:K]
        print(top_k)

        res = 0

        flag = [0 for i in range(len(A))]
        for i in top_k:
            flag[i] = 1
            res += A[i]
        print(flag)
        for i in top_k:
            for j in range(i)[::-1]:
                if flag[j] == 0:
                    flag[j] = 1
                    res += A[i]
                else:
                    break
            if i + 1 < len(A):
                for j in range(i + 1, len(A)):
                    if flag[j] == 0:
                        flag[j] = 1
                        res += A[i]
                    else:
                        break
        return res

    def maxSumAfterPartitioning2(self, A, K):
        l = len(A)
        dp = [0 for i in range(l+1)]

        for i in range(l):
            maxi = 0
            rb = min(i + K, l)  # right bound
            for j in range(i, rb):
                maxi = max(maxi, A[j])
                dp[j + 1] = max(dp[j + 1], dp[i] + (j + 1 - i) * maxi)
        # print(dp)
        return dp[l]

if __name__ == '__main__':
    A = [1, 15, 7, 9, 2, 5, 10]
    K = 4
    A = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    K = 4
    print(Solution().maxSumAfterPartitioning2(A, K))
