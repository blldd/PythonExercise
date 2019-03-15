import numpy as np

arr = [3, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

print arr

print arr + arr
narr1 = np.array(arr)
print narr1
narr2 = np.array(arr)
print narr1 + narr2

print np.ones((3, 5))

arr = np.array([1, 3, 2, 4, 5])
print arr.argsort()[-3:]

name = 'Tim'
langs = ['AS3', 'Lua', 'C']
info = {'name': 'Tim', 'sex': 'Male', 'age': 23}

if name and langs and info:
    print('All True!')  # All True!

import math

print math.floor(3.5)
print math.ceil(3.5)

numList = []
from operator import mul

prod = reduce(mul, numList, 1)
print prod

# a, *b, c = [1, 2, 3, 4, 5]
# print(a)
# print(b)
# print(c)
print arr
tmp = [x ** 2 for x in arr]
print tmp

tmp = (x ** 2 for x in arr)
print next(tmp)
print next(tmp)

for p in np.itertools.permutations([1, 2, 3, 4]):
    print ''.join(str(x) for x in p)
