# coding=utf-8
import sys
import math


def NB_train(datas, labels):
    n = len(datas)
    m = len(datas[0])
    train_data = [[0 for j in range(m)] for i in range(n)]
    for idx, data in enumerate(datas):
        max_num = max(data)
        min_num = min(data)
        mid = (max_num + min_num) / 2
        for idx1, i in enumerate(data):
            if i >= mid:
                train_data[idx][idx1] = 1
            else:
                train_data[idx][idx1] = 0

    pOut = sum(labels) / n
    p0nums = [0.0 for i in range(n)]
    p1nums = [0.0 for i in range(n)]
    p0denom = 0.0
    p1denom = 0.0
    for i in range(n):
        if labels[i] == 1:
            for j in range(m):
                p1nums[j] += train_data[i][j]
            p1denom += sum(train_data[i])
        else:
            for j in range(m):
                p0nums[j] += train_data[i][j]
            p0denom += sum(train_data[i])
    p1vect = [i / p1denom for i in p1nums]
    p0vect = [i / p0denom for i in p0nums]
    return p0vect, p1vect, pOut


def NB_predict(test_data, p0vect, p1vect, pOut):
    n = len(test_data)
    p1 = 0.0
    for i in range(n):
        p1 += (test_data[i] * p1vect[i])
    p1 += math.log(pOut)

    p0 = 0.0
    for i in range(n):
        p0 += (test_data[i] * p0vect[i])
    p0 += math.log(1.0 - pOut)
    return p1 / p0


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip()
    labels = list(map(int, line.split()))

    ans = 0
    train_datas = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        train_data = list(map(int, line.split()))
        train_datas.append(train_data)

    line = sys.stdin.readline().strip()
    test_data = list(map(int, line.split()))

    p0vect, p1vect, pOut = NB_train(train_datas, labels)
    ans = NB_predict(test_data, p0vect, p1vect, pOut)
    print("%.3f" % ans)