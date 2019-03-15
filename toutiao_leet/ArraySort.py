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
    给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
    找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
     
    对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
    """

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.step = 0
                    self.dfs(grid, i, j)
                    res = max(res, self.step)

        return res

    def dfs(self, grid, x, y):
        """
        :type grid: List[list[int]]
        :type x: int
        :type y: int
        :rtype : None
        """
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] != 1:
            return
        grid[x][y] = -1
        self.step += 1
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x - 1, y)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    output += 1
                    self.dfs(grid, i, j)
        return output

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            self.dfs(grid, i - 1, j)
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            self.dfs(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            self.dfs(grid, i, j - 1)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            self.dfs(grid, i, j + 1)

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
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        m = {}
        res = 0
        for i in nums:
            if i not in m:
                l = 0
                r = 0
                if i - 1 in m:
                    l = m[i - 1]
                if i + 1 in m:
                    r = m[i + 1]
                m[i] = 1 + r + l
                m[i + r] = 1 + r + l
                m[i - l] = 1 + r + l
                res = max(res, m[i])
        return res

    """
    给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    给定 n 和 k，返回第 k 个排列。
    说明：
    给定 n 的范围是 [1, 9]。
    给定 k 的范围是[1,  n!]。
    """

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        if n < 1 or k < 1:
            return None
        nums = list(range(1, n + 1))
        nums = map(str, nums)
        perm = self.permute(nums)
        for i in perm:
            ans.append("".join(list(i)))
        return ans[k - 1]

    def permute(self, nums):
        if nums is None:
            return []
        if nums == []:
            return [[]]
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        # 找到对应的n应该对应的fac坐标,就是在第一项确定的情况一下，有(n-1)!种组合
        i = n - 1
        # 构建序列，这个num是用来储存我们当前可以添加的数的，也是为避免重复
        num = list(range(1, n + 1))
        ret = ""
        while i >= 0:
            # a用来获得我们要求的那一位在num里的下标
            a, b = k // self.fac[i], k % self.fac[i]
            # 如果刚好整除干净，证明还在上一层
            if b == 0:
                a -= 1

            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b
            # 如果刚好整除完，则我们已经可以知道接下来的排序情况了，它一定是最大的
            # 所以把剩下的可选的数字reverse来制造这种效果
            if b == 0:
                for i in reversed(num):
                    ret += str(i)
                break
        return ret

    """
    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
    
    示例 1:
    
    输入: 
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    输出: 2 
    说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
    第2个学生自己在一个朋友圈。所以返回2。
    超时
    """

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        friends = []
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    friends.append([i, j])
        print(friends)
        length = len(friends)
        if length < 1:
            return res
        for i in range(length):
            for j in range(length):
                if set(friends[i]).intersection(set(friends[j])):
                    friends[i] = friends[j] = list(set(friends[i]).union(set(friends[j])))
        print(friends)
        friends = [tuple(sorted(t)) for t in friends]
        res = len(set(friends))
        return res

    """
    （1）可以先找到一个人，把这个人的所有朋友都入队。 
    （2）然后依次出队，把朋友的朋友都入队，已经入过队列的，则不再入队（是不是广度优先搜索）。 
    （3）直到不再有朋友入队，而且已经出队完成，说明现在已经组成了一个朋友圈。 
    （4）然后把剩下的没被分到朋友圈里面的，同学，再次入队，进行下一个朋友圈的计算，依次循环直到结束。
    """

    def findCircleNum1(self, M):

        queue, cnt = [0], 0  # [0] 表示第一个人，题目已经给出至少一个人。 cnt 记录朋友圈的个数
        visited = [0] * len(M)  # 0 表示没有访问过，1 表示已经访问过了。
        visited[0] = 1

        while len(queue):  # 队列不为空
            i = queue.pop()  # 出队一个人
            for j in range(len(M[i])):
                if visited[j] or i == j or M[i][j] == 0:  # 访问过了，或者是自己，或者不是朋友关系，则不加
                    continue
                queue.append(j)  # 入队
                visited[j] = 1  # 此人已经访问过

            if not len(queue):  # 队列为空
                cnt += 1  # 朋友圈数 加一
                if sum(visited) < len(visited):  # 如何还有人没有被分到朋友圈
                    idx = visited.index(0)  # 继续入队一个人
                    queue.append(idx)
                    visited[idx] = 1
        return cnt


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

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    # print(Solution().maxAreaOfIsland(grid))
    #
    # print(Solution().numIslands(grid))

    nums = [1, 3, 5, 4, 2, 3, 4, 5]
    target = 0
    # print(Solution().search(nums, target))

    # print(Solution().findLengthOfLCIS(nums))

    k = 3
    # print(Solution().findKthLargest(nums, k))

    # print(Solution().longestConsecutive2(nums))

    n = 3
    # print(Solution().getPermutation(n, k))

    # print(list(itertools.permutations([1, 2, 3, 4])))
    # print(Solution().permute(list(range(1, 4))))

    # grid = [[1, 0, 0],
    #         [0, 1, 0],
    #         [0, 0, 1]]
    grid = [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]]
    grid = [[1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]]
    # print(Solution().findCircleNum1(grid))

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
