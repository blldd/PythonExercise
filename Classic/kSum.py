# -*- coding:UTF-8 -*-
"""
The ... file.

Authors: dedong (ddlecnu@gmail.com)
"""

def sum_2(arr, target):
    hash_table = {}
    res = []
    for i in range(len(arr)):
        if target - arr[i] in hash_table:
            res.append([hash_table[target - arr[i]], i])
        hash_table[arr[i]] = i
    return res


def sum_3(arr, target):
    arr.sort()
    len1 = len(arr)
    res = []
    if len1 < 3:
        print(res)
    for i in range(len1 - 1):
        left, right = i + 1, len1 - 1  # 以下思路与2sum中的快速排序思想一样
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target and [arr[i], arr[left], arr[right]] not in res:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1
    print(res)


def sum_3_2(arr, target):  # 3sum问题 解 2
    res = []
    for i, value1 in enumerate(arr):
        for j, value2 in enumerate(arr[i + 1:]):
            if (target - value1 - value2) in arr[i + 2:]:
                minV = min(value1, value2, target - value1 - value2)
                maxV = max(value1, value2, target - value1 - value2)
                midV = target - minV - maxV
                res.append((minV, midV, maxV))
    print(list(set(res)))

def continuous_pos_sum(target):
    res = []
    if target < 1:
        return
    small = 1
    big = 2
    cur_sum = small + big
    mid = (1+target)/2
    while small < mid:
        if cur_sum < target:
            big += 1
            cur_sum += big
        elif cur_sum > target:
            cur_sum -= small
            small += 1
        else:
            res.append([i for i in range(small, big+1)])
            cur_sum -= small
            small += 1
    return res


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 6, 5]
    target = 6

    # print(sum_2(nums, target))
    # sum_3(nums, target)
    # sum_3_2(nums, target)

    print(continuous_pos_sum(15))
