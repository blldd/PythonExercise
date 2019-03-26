# -*- coding:UTF-8 -*-

def perm(arr, stack):
    if not arr:
        print(stack)     # 到树的最后，输出结果
        tmp = stack.copy()
        res.append(tmp)

    else:               # 没有到树的叶子节点的时候，使用递归继续往下找。
        for i in range(len(arr)):
            stack.append(arr[i])
            del arr[i]
            perm(arr, stack)
            arr.insert(i, stack.pop())

arr=[1,2,3]
stack=[]
res = []
# for i in perm(arr, stack):
#     print(i)
perm(arr, stack)
print(res)

def str_sort(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list


# str_list = str_sort("123")
# print(str_list)