# -*- coding:utf-8 -*-

"""

"""


class Solution:
    def sort(self, arr):
        # write code here
        tmp = 0
        lastChangeInd = 0
        sortBorder = len(arr) - 1
        for i in range(len(arr)):
            isSorted = True
            for j in range(sortBorder):
                if arr[j] > arr[j + 1]:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp
                    isSorted = False
                    lastChangeInd = j
            sortBorder = lastChangeInd
            if isSorted:
                break


if __name__ == '__main__':
    arr = [3, 4, 2, 1, 5, 6, 7, 8]
    # print(Solution().sort(arr))
    print(arr)
