# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 11:04 AM
@Author  : ddlee
@File    : code4.py
"""


class Solution:
    """
    给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。
    返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）

    输入："banana"
    输出："ana"

    输入："abcd"
    输出：""

    此解法超内存
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
