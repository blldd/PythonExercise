# -*- coding:UTF-8 -*-

def perm(list,stack):
    if not list:
        print(stack)    # 到树的最后，输出结果

    else:               # 没有到树的叶子节点的时候，使用递归继续往下找。
        for i in range(len(list)):
            stack.append(list[i])
            del list[i]
            perm(list,stack)
            list.insert(i,stack.pop())

# list=[1,2,3]
# stack=[]
# perm(list, stack)


def str_sort(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list


str_list = str_sort("123")
print(str_list)