from math import ceil


class Solution(object):
    def canPartition(self, nums):
        """
        划分成两个相等的子数组
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

    def partition1(self, nums):
        """
        和差值最小子数组划分 问题
        有 bug

        :param nums:
        :return:
        """
        length = len(nums)
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        target = ceil(total / 2)

        a_list = []
        b_list = []

        s = 0
        for i in range(length):
            try:
                if s + nums[i] <= target:
                    s += nums[i]
                    a_list.append(nums[i])
                    # nums.pop(i)
                    if abs(s - target) < a_list[0]:
                        break
                else:
                    b_list.append(nums[i])
            except Exception as e:
                print(i, e)
        return a_list, b_list

    def partition(self, nums):
        """
        动态规划
        状态方程：f[i][j]=Max(f[i-1][j-array[i]]+array[i],f[i-1][j])
        :param nums:
        :return:
        """
        length = len(nums)
        nums = sorted(nums, reverse=True)
        total = sum(nums)

        dp = [[0 for j in range(total // 2 + 1)] for i in range(length + 1)]

        for i in range(length):
            for j in range(1, total // 2 + 1):
                dp[i + 1][j] = dp[i][j]
                if nums[i] <= j and dp[i][j - nums[i]] + nums[i] > dp[i][j]:
                    dp[i + 1][j] = dp[i][j - nums[i]] + nums[i]

        for i in dp:
            print(i)


if __name__ == '__main__':
    nums = [2, 2, 3, 5, 5, 9]
    print(Solution().canPartition(nums))
    print(Solution().partition(nums))
