# -*- coding:UTF-8 -*-
import itertools


class Solution:
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
    找出所有满足条件且不重复的三元组。

    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        len1 = len(nums)
        res = []
        if len1 < 3:
            print(res)
        for i in range(len1 - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len1 - 1  # 以下思路与2sum中的快速排序思想一样
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return res

    """
    旋转数组查找
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
    """

    def search_rotate_array(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 先找到两个第二个升序数组的第一项的index
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pol = l
        ans = self.binary_search(target, nums[:pol])
        if ans == -1:
            ans = self.binary_search(target, nums[pol:])
            if ans != -1:
                ans += len(nums[:pol])
        return ans

    def binary_search(self, target, nums):
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
        return index

    def binary_search_rotate_array(self, nums, target):
        l = 0
        r = len(nums) - 1
        while (l < r):
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and nums <= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    """
    输入: [2,2,2,2,2]
    输出: 1
    解释: 最长连续递增序列是 [2], 长度为1。
    [1,3,5,4,2,3,4,5]
    """

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        length = len(nums)
        if length < 1:
            return 0
        if length == 1:
            return 1
        left = 0
        right = 2
        while right <= length and left < right:
            if self.isAscending(nums[left:right]):
                ans = max(ans, right - left)
                right += 1
            else:
                left = right - 1
        return ans

    def isAscending(self, nums):
        length = len(nums)
        if length == 1:
            return True
        for i in range(1, length):
            if nums[i] <= nums[i - 1]:
                return False
        return True

    """
    在未排序的数组中找到第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    """

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        if length < 1 or length < k:
            return None

        nums = sorted(nums)
        nums = nums[::-1]
        return nums[k - 1]

    """
    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
    示例:
    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
    """

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums = sorted(list(set(nums)))
        length = len(nums)
        if length < 1:
            return 0
        if length == 1:
            return 1

        left = 0
        right = 2
        while right <= length and left < right:
            if self.isSequential(nums[left:right]):
                ans = max(ans, right - left)
                right += 1
            else:
                left = right - 1
        return ans

    def isSequential(self, nums):
        length = len(nums)
        if length == 1:
            return True
        for i in range(1, length):
            if nums[i] != nums[i - 1] + 1:
                return False
        return True

    """
    bit
    """

    def longestConsecutive1(self, line):
        data = line
        num = 0
        # 在对应的位置1
        for x in data:
            num = num | (1 << x)
        # 获取二进制字符串
        num = bin(num)[2:]  # 0b111110 str
        # 获得最大连续的1数量
        continuous = 0
        maxcontinuous = 0
        for x in num:
            if x == '0':
                maxcontinuous = max(maxcontinuous, continuous)
                continuous = 0
            else:
                continuous += 1
        return str(maxcontinuous)

    """
    map
    用一个字典存储中间值。遍历数组，对于数字i，找到i-1和i+1对应的value值,如果不存在则记0。
    然后把i的value值设为i-1,i+1的value值之和，并加1，相当于连接起来。
    同时置最左端和最右端的数的value值为i的value值（中间的数都已经出现过，不会再用到了）。
    然后更新一次最大值。
    """

    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solu:
    """
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    """

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length < 1:
            return []
        d = {}
        # 字典存储 最大值 例如[2,3] [2,4] 则存储[2,4]
        for i in intervals:
            if i.start not in d:
                d[i.start] = i.end
            else:
                if i.end > d[i.start]:
                    d[i.start] = i.end
        print(d)
        d = sorted(d.items(), key=lambda x: x[0])
        print(d)

        # intervals = sorted(intervals, key=lambda inter:inter.start)
        # print(intervals[0].start, intervals[0].end, intervals[1].start, intervals[1].end)
        arr = []
        for i in d:
            arr.extend(list(i))
        print(arr)
        for i in range(1, len(arr) - 1, 2):
            if arr[i] >= arr[i + 2]:
                arr[i + 2] = arr[i]
                arr[i] = arr[i + 1] = None
            elif arr[i] >= arr[i + 1]:
                arr[i] = arr[i + 1] = None

        print(arr)
        arr = [i for i in arr if i is not None]
        print(arr)
        res = [arr[i:i + 2] for i in range(0, len(arr), 2)]
        return res

    '''
    [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，
    在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
    '''

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxh = 0
        ind_maxh = 0
        length = len(height)
        for i in range(length):
            if height[i] > maxh:
                maxh = height[i]
                ind_maxh = i
        oneh = 0
        res = 0
        for i in range(ind_maxh):
            if oneh < height[i]:
                oneh = height[i]
                continue
            res += oneh - height[i]
        oneh = 0
        for i in range(length - 1, ind_maxh, -1):
            if oneh < height[i]:
                oneh = height[i]
                continue
            res += oneh - height[i]
        return res


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    # print(Solution().threeSum(nums))

    nums = [1, 3, 5, 4, 2, 3, 4, 5]
    target = 0
    # print(Solution().search(nums, target))

    # print(Solution().findLengthOfLCIS(nums))

    k = 3
    # print(Solution().findKthLargest(nums, k))

    # print(Solution().longestConsecutive2(nums))

    # x = [1,5,3]
    # print(sorted(x))

    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    arr = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
    intervals = []
    for i in arr:
        intervals.append(Interval(i[0], i[1]))
    # print(Solu().merge(intervals))

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solu().trap(height))
