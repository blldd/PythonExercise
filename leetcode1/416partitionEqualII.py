# -*- coding: utf-8 -*-
# @ 2019-08-10
# @ Li Dedong

# coding=utf-8
import random
import copy


def test_input():
    arr = [-300]
    for i in range(100):
        n = random.randint(-10, 20)
        if n < 0:
            n -= 100
        elif n > 0:
            n += 100
        else:
            continue
        arr.append(n)
    return arr


arr = test_input()


def incomplete_solution(arr):
    total = sum(arr)
    half = total / 2
    print(total, half)
    possibleSolution = {0: []}
    for i in arr:
        possibleSum = possibleSolution.keys()
        for k in possibleSum:
            now = i + k
            if (now not in possibleSum):
                valueList = possibleSolution[k]
                nowList = copy.copy(valueList)
                nowList.append(i)
                possibleSolution[now] = nowList
                if (now == half):
                    print("exactly match")
                    # print(nowList)
                    return nowList
    # now we can not found a perfect solution, so here to find the closest
    print(len(possibleSolution.keys()))
    # TODO... find the closest solution
    possibleSolution = {0: []}
    for i in arr:
        possibleSum = possibleSolution.keys()
        for k in possibleSum:
            now = i + k
            if (now not in possibleSum):
                valueList = possibleSolution[k]
                nowList = copy.copy(valueList)
                nowList.append(i)
                possibleSolution[now] = nowList
                if (now > half):
                    print("exactly match")
                    return nowList


if __name__ == '__main__':
    #arr = [1, 2, 3, 4, 233, 12, 123]  # test_input()
    n = incomplete_solution(arr)
    for i in n:
        arr.remove(i)
    print(n)
    print(sum(n))
    print(arr)
    print(sum(arr))