# -*- coding: utf-8 -*-

# 数据类型： int 整数类型   string 字符串类型  float浮点数 0.1 0.2
# 32, 34, 129, 2309
# 11    “11”  “hello”  'h'  "had"   0.2
# variable =

# print "hello world!"
#
# for i in range(11):
#     print(i)
#
# a = 1
#
# if a == 1:
#     print "a==1"

# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 1 10
# 0010100000001111000100010100100010010100100100
# 00000000->byte
# 0->bit  8bit->byte字节  e->byte   我-》byte

# if acsii == 24:
#     exit()

for i in range(1, 10):
    s = ""
    for j in range(i, 10):
        s = s + "%d*%d = %d \t" % (i, j, i * j)
        # s += "%d*%d = %d \t" %(i, j, i*j)
    print(s)

print("#" * 50)
list = ["minecraft", 783, 2.234, "john", 12.3]
tinylist = [123, "john"]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
list[1] = 784
print(list)


print("#" * 50)
tuple = ("minecraft", 783, 2.234, "john", 12.3)
tinytuple = (123, "john")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)
print(tuple)

"""
第二次课程作业
将1-100 每十个 打印一行，每一行中用tab隔开
并且将数字存入列表numlist

"""

numlist = []
for i in range(10):
    numlist.append(i)
print(numlist)

print("#" * 50)
dict = {}
dict["one"] = "this is one"
dict[2] = "this is two"
tinydict = {"name": "john", "code": 6743, "dept": "sales"}
print(dict["one"])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())


