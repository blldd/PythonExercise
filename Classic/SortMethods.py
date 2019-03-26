# -*- coding:UTF-8 -*-

quick_sort_lam = lambda array: array if len(array) <= 1 else \
    quick_sort_lam([item for item in array[1:] if item <= array[0]]) \
    + [array[0]] + \
    quick_sort_lam([item for item in array[1:] if item > array[0]])


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] >= key:
            right -= 1
        array[left], array[right] = array[right], array[left]
        while left < right and array[left] <= key:
            left += 1
        array[right], array[left] = array[left], array[right]
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


def quick_sort_recur(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort_recur(array, l, q - 1)
        quick_sort_recur(array, q + 1, r)

def partition(nums, left, right):
    key = nums[left]
    while left < right:
        # right下标位置开始，向左边遍历，查找不大于基准数的元素
        while left < right and nums[right] >= key:
            right -= 1
        if left < right:  # 找到小于准基数key的元素,然后交换nums[left],nums[right]
            nums[left], nums[right] = nums[right], nums[left]
        else:  # left〉=right 跳出循环
            break
        # left下标位置开始，向右边遍历，查找不小于基准数的元素
        while left < right and nums[left] < key:
            left += 1
        if left < right:  # 找到比基准数大的元素，然后交换nums[left],nums[right]
            nums[right], nums[left] = nums[left], nums[right]
        else:  # left〉=right 跳出循环
            break
    return left  # 此时 left==right 所以返回right也是可以的


def partition1(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort_stack(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


def bubble_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    for i in range(length)[::-1]:
        for j in range(i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    input = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
    input = [1, 4, 7, 1, 5, 5, 3, 85]
    quick_sort(input, 0, 7)
    print(input)
    # input.sort()
    # res = quick_sort_lam(input)
    # print(res)
    # quick_sort_recur(input, 0, 13)
    # print(input)
    # quick_sort_stack(input, 0, 13)
    # print(input)
    input = [4, 4, 3, 1, 8]
    print(bubble_sort(input))