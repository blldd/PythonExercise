class Solution(object):
    def canPartition(self, nums):
        """
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
        for i in range(len(nums)):
            for j in range(half_sum, nums[i] - 1, -1):
                dp[j] = 1 if dp[j] or dp[j - nums[i]] else 0
        print(dp)
        return dp[half_sum] == 1


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    print(Solution().canPartition(nums))
