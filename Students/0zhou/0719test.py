# -*- coding: UTF-8 -*-

# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print 'data error'
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print 'it is the %dth day.' % sum
#
#

n = 153

i = n / 100
j = n / 10 % 10
k = n % 10
print(i, j, k)

tmp = n
for i in range(len(str(n))):
    res = tmp % 10
    tmp /= 10
    print(u"第 %d 位: %d" % (len(str(n)) - i, res))

print("*" * 50)

"""
n= 153
"""

# a = range(10)
# print(a)
#
# for i in range(10):
#     print(i)
#
# for i in "hello":
#     print(i)

a = 153
for i in str(a):
    print(i)
print("*" * 150)

x = a % 10
print(x)
y = a / 10 % 10
print(y)
c = a / 100
print(c)

"""
153 = 1**3 + 5**3 + 3*3
100 - 999
1. 取100-1000


"""
for a in range(100, 1000):
    x = a % 10
    y = a / 10 % 10
    c = a / 100
    if a == x ** 3 + y ** 3 + c ** 3:
        print(a)

"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：
"""


# 使用递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


res = fib(3)
print res

"""
"""

import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 暂停一秒
time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

"""
判断100-200之间有多少个素数，并输出所有素数
素数：质数
3 5 7 11
"""

h = 0
leap = 1

for m in range(2, 10):
    # k = int(sqrt(m + 1))
    for i in range(2, m):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % m

"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""


def reduceNum(n):
    print '{} = '.format(n),
    if not isinstance(n, int) or n <= 0:
        print '请输入一个正确的数字 !'
        exit(0)
    elif n in [1]:
        print '{}'.format(n)
    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n /= index  # n 等于 n/index
                if n == 1:
                    print index
                else:  # index 一定是素数
                    print '{} *'.format(index),
                break


reduceNum(90)
reduceNum(100)

"""
   *
  ***
 *****
*******


 *****
  ***
   *
"""
