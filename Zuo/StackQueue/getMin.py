# -*- coding:UTF-8 -*-
"""
实现一个栈， 在基本功能的基础上，实现返回占中最小元素的操作
- pop push getMin 时间复杂度 O(1)
- 设计的栈类型可以使用现成的结构
"""
import sys

class Solution(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.minist = sys.maxsize

    def get_min(self):
        return self.min_stack[-1]

    def push(self, x):
        self.stack.append(x)
        if x < self.minist:
            self.min_stack.append(x)
            self.minist = x
        else:
            self.min_stack.append(self.minist)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

if __name__ == '__main__':
    obj = Solution()
    obj.push(3)
    obj.push(1)
    obj.push(5)
    obj.push(2)
    # obj.pop()
    _top = obj.top()
    _min = obj.get_min()
    print(_top)
    print(_min)
