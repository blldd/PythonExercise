from math import ceil


class Solution(object):
    def canPartition(self, nums):
        """
        划分成两个和相等的子数组
        转化成 给定数组 和 target 求是否存在子数组能组合成target
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return True
        if sum(nums) % 2 != 0:  ## 总和必须为偶数，否则肯定无法取两个集合的sum相等
            return False
        half_sum = sum(nums) // 2
        dp = [0] * (half_sum + 1)
        dp[0] = 1

        for i in nums:
            for j in range(half_sum, i - 1, -1):
                dp[j] = 1 if dp[j] or dp[j - i] else 0
            print(dp)

        return dp[half_sum] == 1

    def partition_dp(self, nums):
        """
        动态规划
        状态方程：f[j]=Max(f[j-array[i]]+array[i],f[j])
        :param nums:
        :return:
        """
        total = sum(nums)
        current_sum = [0 for i in range(total // 2 + 1)]
        state = [[0 for j in range(total // 2 + 1)] for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(total // 2, nums[i] - 1, -1):
                if current_sum[j] < current_sum[j - nums[i]] + nums[i]:
                    current_sum[j] = current_sum[j - nums[i]] + nums[i]
                    state[i][j] = 1
        for i in state:
            print(i)
        print(current_sum)
        res = []
        j = total // 2
        for i in range(len(nums) - 1, -1, -1):
            if state[i][j]:
                res.append(nums[i])
                j -= nums[i]
        return res


if __name__ == '__main__':
    nums = [5, 2, 3, 5, 7]
    # print(Solution().canPartition(nums))
    print(sum(Solution().partition_dp(nums)))
