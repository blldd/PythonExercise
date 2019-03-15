# -*- coding: utf-8 -*-



print('hello world')

print('1\t2\t3\t4')
print("10\t20\t30\t40")

"""
1\t2\t3\t4
10 20 30 40

1byte = 8bit
1 0 1
2 00 01 10 11
8 = 2^8= 256

0100010100001111111
10=1010
1=1
0=0
2=10
"""
# list []
#               0           1       2
classmates = ['Michael', 'Bob', 'Tracy']   # 数组 list
#               -3         -2       -1

#    -3 -2 -1 0 1 2 3
print len(classmates)

q=['hello']
print(len(str(['100'])))   # str ‘100’

print classmates

classmates.append('Adam')    # 追加

print(classmates)

classmates.pop()             # 弹出
print(classmates)

print("#################")


classmates.insert(2, 'Jack')  # 插入
print(classmates)

# tuple ()

tuple1 = ('Michael', 'Bob', 'Tracy')
print(tuple1[0])


print("###############")
s = set([1,1,2,3,4,4, 44])   # set 是无序   无重复的  堆
print(s)
s.add(1)    # 加入
print(s)
s.add(1)
print(s)

s.remove(44)     # 删除
print(s)


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}    # dict 字典


d = {'k1':"v1", 'k2':'v2'}





