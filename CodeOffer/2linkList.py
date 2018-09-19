# -*- coding:UTF-8 -*-
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(listNode):
    # write code here
    l = []
    head = listNode
    while head:
        l.insert(0, head.val)
        head = head.next
    return l


if __name__ == '__main__':
    list_node = ListNode(1)
    list_node_2 = ListNode(2)
    list_node.next = list_node_2
    print printListFromTailToHead(list_node)
