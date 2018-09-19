#!/usr/bin/env python
# encoding:utf-8
# __author__: huxianglin
# date: 2016/9/25 12:09
# blog: http://huxianglin.cnblogs.com/ http://xianglinhu.blog.51cto.com/

def perm(list,stack):
    if not list:
        print(stack)    # 到树的最后，输出结果
    else:               # 没有到树的叶子节点的时候，使用递归继续往下找。
        for i in range(len(list)):
            stack.append(list[i])
            del list[i]
            perm(list,stack)
            list.insert(i,stack.pop())

list=[1,2,3]
stack=[]
perm(list,stack)
