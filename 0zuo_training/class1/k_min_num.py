# -*- coding:UTF-8 -*-
import random


def generate_sorted_arr(len, max_value):
    res = [random.randint(0, max_value) for i in range(len)]
    return sorted(res)


def get_sorted_arr(arr1, arr2):
    if len(arr1) < 1 or len(arr2) < 1:
        return None
    length = len(arr1) + len(arr2)
    res = [0 for i in range(length)]
    for idx, i in enumerate(arr1):
        res[idx] = i
    for idx, i in enumerate(arr2):
        res[idx + len(arr1)] = i
    return sorted(res)


def get_up_median(shorts, s1, e1, longs, s2, e2):
    while s1 < e1:
        mid1 = (s1 + e1) // 2
        mid2 = (s2 + e2) // 2
        offset = ((e1 - s1 + 1) & 1) ^ 1
        if shorts[mid1] > longs[mid2]:
            e1 = mid1
            s2 = mid2 + offset
        elif shorts[mid1] < longs[mid2]:
            s1 = mid1 + offset
            e2 = mid2
        else:
            return shorts[mid1]

    return min(shorts[s1], longs[s2])


def find_kth_num(arr1, arr2, kth):
    if len(arr1) < 0 or len(arr2) < 0:
        return None
    if kth < 1 or kth > len(arr1) + len(arr2):
        return None
    longs = arr1 if len(arr1) >= len(arr2) else arr2
    shorts = arr1 if len(arr1) < len(arr2) else arr2
    l = len(longs)
    s = len(shorts)
    if kth <= s:
        return get_up_median(shorts, 0, kth - 1, longs, 0, kth - 1)
    if kth > l:
        if shorts[kth - l - 1] >= longs[l - 1]:
            return shorts[kth - l - 1]
        if longs[kth - s - 1] >= shorts[s - 1]:
            return longs[kth - s - 1]
        return get_up_median(shorts, kth - l, s - l, longs, kth - s, l - 1)
    if longs[kth - s - 1] >= shorts[s - 1]:
        return longs[kth - s - 1]
    return get_up_median(shorts, 0, s - 1, longs, kth - s, kth - 1)


if __name__ == '__main__':
    """
    给定两个一维int数组A和B. 其中:
    A是长度为m、元素从小到大排好序的有序数组。
	B是长度为n、元素从小到大排好序的有序数组。
	希望从A和B数组中，找出最大的k个数字，
	要求:使用尽量少的比较次数。
	"""
    len1 = 10
    len2 = 23
    max_value1 = 20
    max_value2 = 100
    arr1 = generate_sorted_arr(len1, max_value1)
    arr2 = generate_sorted_arr(len2, max_value2)
    print(arr1)
    print(arr2)
    sorted_all = get_sorted_arr(arr1, arr2)
    print(sorted_all)
    kth = 17
    print(sorted_all[kth - 1])

    print(find_kth_num(arr1, arr2, kth))
