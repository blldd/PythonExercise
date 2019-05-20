# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/19 11:04 AM
@Author  : ddlee
@File    : code4.py
"""


class Solution:
    """
    1049. 最后一块石头的重量 II  显示英文描述

    有一堆石头，每块石头的重量都是正整数。

    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

    示例：
    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
    """

    def longestDupSubstring(self, string):
        if not string:
            return None, None

        suffix_array = []
        length = len(string)
        for i in range(length):
            suffix_array.append(string[i:])

        # second, sort suffix array
        start, end = 0, len(suffix_array) - 1
        quick_sort(suffix_array, start, end)
        # third, get the longest repeating substring
        print(suffix_array)
        max_length, repeat_substring = 0, ''
        for i in range(len(suffix_array) - 1):
            common_len, common_substring = find_common_string(suffix_array[i], suffix_array[i + 1])
            if common_len > max_length:
                max_length, repeat_substring = common_len, common_substring
        return max_length, repeat_substring


def quick_sort(suffix_array, start, end):
    if end <= start:
        return

    index1, index2 = start, end
    base = suffix_array[start]
    while index1 < index2:
        while index1 < index2 and suffix_array[index2] >= base:
            index2 -= 1
        suffix_array[index1], suffix_array[index2] = suffix_array[index2], suffix_array[index1]
        while index1 < index2 and suffix_array[index1] <= base:
            index1 += 1
        suffix_array[index2], suffix_array[index1] = suffix_array[index1], suffix_array[index2]

    # suffix_array[index1] = base
    quick_sort(suffix_array, start, index1 - 1)
    quick_sort(suffix_array, index1 + 1, end)


def find_common_string(str1, str2):
    if not str1 or not str2:
        return 0, ''
    index1, index2 = 0, 0
    length, comm_substr = 0, ''
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] == str2[index2]:
            length += 1
            comm_substr += str1[index1]
        else:
            break
        index1 += 1
        index2 += 1
    return length, comm_substr


def find_longest_repeating_strings(string):
    if not string:
        return None, None

    suffix_array = []
    length = len(string)
    for i in range(length):
        suffix_array.append(string[i:])

    # second, sort suffix array
    start, end = 0, len(suffix_array) - 1
    quick_sort(suffix_array, start, end)
    print(suffix_array)

    # third, get the longest repeating substring
    max_length, repeat_substring = 0, ''
    for i in range(len(suffix_array) - 1):
        common_len, common_substring = find_common_string(suffix_array[i], suffix_array[i + 1])
        if common_len > max_length:
            max_length, repeat_substring = common_len, common_substring
    return max_length, repeat_substring


if __name__ == "__main__":
    # string = "Ask not what your country can do for you, but what you can do for your country"
    string = "banana"
    length, substr = find_longest_repeating_strings(string)
    print(length, substr)
