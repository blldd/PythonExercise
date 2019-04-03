# -*- coding:UTF-8 -*-
import re
import sys

if __name__ == "__main__":
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    Q = int(sys.stdin.readline().strip())

    if Q < 1 or Q > 100000 or len(A) < 1 or len(A) > 500000 or len(B) < 1 or len(B) > 100:
        print("error")

    res = []
    for i in range(Q):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))

        l, r = line[0], line[1]
        # ans = re.findall(B, A[l-1:r])

        str_s = A[l-1:r]
        str_p = B
        length  = len(str_p)
        ans = 0
        for k in range(len(str_s) - length+1):
            if str_p == str_s[k:k+length]:
                ans += 1

        res.append(ans)

    for i in res:
        print(i)

# # -*- coding:UTF-8 -*-
#
# import sys
#
#
# def shrink(s):
#     length = len(s)
#     if length % 2 == 1:
#         return s
#     if length % 2 == 0 and s[:(length // 2)] == s[(length // 2):]:
#         return shrink(s[:(length // 2)])
#     else:
#         return s
#
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     length = len(line)
#
#     if length > 1000000:
#         print("error")
#
#     line = shrink(line)
#     # print(line)
#     cnt = 0
#     _set = set()
#     for i in range(length):
#         tmp = line[i:] + line[:i]
#         if tmp not in _set:
#             cnt += 1
#             _set.add(tmp)
#
#     print(cnt)

# import math
#
#
# def sieve(size):
#     sieve = [True] * size
#
#     sieve[0] = False
#
#     sieve[1] = False
#
#     for i in range(2, int(math.sqrt(size)) + 1):
#
#         k = i * 2
#
#         while k < size:
#             sieve[k] = False
#
#             k += i
#
#     return sum(1 for x in sieve if x)
#
#
# print(sieve(10000000000))
