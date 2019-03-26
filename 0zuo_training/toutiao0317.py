# -*- coding:UTF-8 -*-


def solve(s):
    n = len(s)
    r = list(s[:min(len(s), 2)])
    for i in range(2, n):
        if s[i] == r[-1] == r[-2]:
            continue
        if s[i] == r[-1] and len(r) > 2 and r[-2] == r[-3]:
            continue
        r.append(s[i])
    return ''.join(r)


for test_case in range(int(input())):
    print(solve(input()))
