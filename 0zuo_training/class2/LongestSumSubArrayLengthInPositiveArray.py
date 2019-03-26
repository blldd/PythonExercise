# -*- coding:UTF-8 -*-

def longest_sum_subarr_positive(arr, target):
    """
    给定一个数组 arr，该数组无序，但每个值均为正数，再给定一个正数 k。
    求 arr 的 所有子 数组中所有元素相加和为 k 的最长子数组长度。 例如，arr=[1,2,1,1,1]，k=3。
    累加和为 3 的最长子数组为[1,1,1]，所以结果返回 3。
    要求:时间复杂度O(N)，额外空间复杂度O(1)

    ** 双指针 **
    """
    length = len(arr)
    if length < 1 or target <= 0:
        return 0
    l = 0
    r = 1
    sum = arr[0]
    max_sub = 0
    while r < length:
        if sum == target:
            max_sub = max(max_sub, r - l)
            sum -= arr[l]
            l += 1

        if sum > target:
            sum -= arr[l]
            l += 1

        elif sum < target:
            sum += arr[r]
            r += 1
    return max_sub


def longest_sum_subarr(arr, target):
    """
    给定一个数组 arr，该数组无序，但每个值均 可能为负数 ，再给定一个正数 k。
    求 arr 的 所有子 数组中所有元素相加和为 k 的最长子数组长度。 例如，arr=[1,2,1,1,1]，k=3。
    累加和为 3 的最长子数组为[1,1,1]，所以结果返回 3。
    要求:时间复杂度O(N)，额外空间复杂度O(1)

    ** 由于有负数 不是递增 不能用双指针 用辅助空间 **
    """
    length = len(arr)
    if length < 1 or target <= 0:
        return 0

    sum = 0
    ans = 0

    map = {}
    map[0] = -1

    for i in range(length):
        sum += arr[i]
        if sum - target in map:
            ans = max(ans, i - map[sum - target])
        if sum not in map:
            map[sum] = i
    return ans


def longest_subarr_lt_k(arr, target):
    """
    给定一个无序数组 arr，其中元素可正、可负、可 0，给定一个整数 k。
    求 arr 所 有的子数组 中累加和小于或等于 k 的最长子数组长度。
    例如:arr=[3,-2,-4,0,6]，k=-2，相加和小于或等于-2 的最长子数组为{3,-2,- 4,0}，所以结果返回4。
    """
    length = len(arr)
    if length < 1 or target <= 0:
        return 0

    min_sums = [0 for i in range(length)]
    min_sum_ends = [0 for i in range(length)]
    min_sums[-1] = arr[-1]
    min_sum_ends[-1] = length - 1

    for i in range(length - 1)[::-1]:
        if min_sums[i + 1] < 0:
            min_sums[i] = arr[i] + min_sums[i + 1]
            min_sum_ends[i] = min_sum_ends[i + 1]
        else:
            min_sums[i] = arr[i]
            min_sum_ends[i] = i

    end = 0
    sum = 0
    res = 0
    # i是窗口的最左的位置，end是窗口最右位置的下一个位置
    for i in range(length):
        # while循环结束之后：
        # 1) 如果以i开头的情况下，累加和<=k的最长子数组是arr[i..end-1]，看看这个子数组长度能不能更新res；
        # 2) 如果以i开头的情况下，累加和<=k的最长子数组比arr[i..end-1]短，更新还是不更新res都不会影响最终结果；
        while end < length and sum + min_sums[end] <= target:
            sum += min_sums[end]
            end = min_sum_ends[end] + 1
        res = max(res, end - i)
        if end > i:  # 窗口内还有数
            sum -= arr[i]
        else:
            end = i + 1  # 窗口内已经没有数了，说明从i开头的所有子数组累加和都不可能<=k
    return res


if __name__ == '__main__':
    arr = [3, 2, 1, 1, 1, 1, 1, 4, 2, 1, 1, 1, 1]
    target = 7
    print(longest_sum_subarr_positive(arr, target))
    print(longest_sum_subarr(arr, target))
    print(longest_subarr_lt_k(arr, target))
