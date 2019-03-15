# -*- coding:UTF-8 -*-

def most_eor(arr):
    """
	给出n个数字 a_1,...,a_n，问最多有多少不重叠的非空区间，使得每个区间内数字的 xor都等于0。
    :param arr:
    :return:
    """
    ans = 0
    xor = 0
    length = len(arr)

    mosts = [0 for i in range(length)]
    map = {}
    map[0] = -1

    for i in range(length):
        xor ^= arr[i]
        if xor in map:
            pre = map[xor]
            mosts[i] = 1 if pre == -1 else (mosts[pre] + 1)
        if i > 0:
            mosts[i] = max(mosts[i-1], mosts[i])
        map[xor] = i
        ans = max(ans, mosts[i])
    return ans


if __name__ == '__main__':
    arr = [1, 1, 1, 3, 2, 1, 1, 3]
    print(most_eor(arr))