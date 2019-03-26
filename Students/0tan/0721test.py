# -*- coding: UTF-8 -*-

"""
a = 153
x = 3
y = 5
z = 1


a = 987

a = 9473
"""
a = 153
i = 0

# s = "hello "
#
# print(len(s))
s = "hello"
print(s)
s = s[::-2]
print(s)
#
# for i in s:
#     print(i)
#
# for i in str(a)[::-1]:
#     print(i)
#
# arr = [1, 2, 3, 4, 5]
# tmp = a
# while i < len(str(a)):
#     print((tmp % 10))
#     tmp = tmp / 10
#     i += 1

"""
水仙花数
153 = 1^3 + 5^3 + 3^3

100 - 999
^   位运算   10--》1010     1--》1   2--》10      4--》100    8--》1000 
1010 & 1000 = 1000   1010 || 1000 = 1010  1010^1000 = 0010
10<<2 = 1000
5*2=10   *2= 20
101<<1=1010   <<1 =10100

"""

a = 100
while a < 1000:
    tep = a
    if a == ((a % 10) ** 3 + ((a / 10) % 10) ** 3 + (a / 100) ** 3):
        print(a)
    a += 1

"""
1 2 3 3 2 4 4 6 7 7 6
arr = [1,2,2,3,3,4,4,5,5,6,6,7,7]


时间复杂度
n
n*n   O(n^2)   
O(n)


空间复杂度


"""
arr = [3, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

# for i in arr:
#     a = 0
#     for j in arr:
#         if i == j:
#             a += 1
#     if a == 1:
#         print(i)

"""
位运算：
& || not ^ 
^  
O(n)
1
10 ^ 10 = 00
11 ^ 11 = 00
100 ^ 100 = 000
101 ^ 101 = 000
110 ^ 110 = 000
111 ^ 111 = 000
1^0 = 1
print(1)

"""

# tmp = 0
# for i in arr:
#     tmp ^= i
# print(tmp)

import numpy as np
import pandas as pd
import random
import time
import calendar

print(arr)

narr = np.array(arr)
print(narr)


