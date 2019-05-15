# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 10:29 AM
@Author  : ddlee
@File    : code1.py
"""


class Solution:
    def isRobotBounded(self, instructions):
        dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]

        start = [0, 0]
        idx = 0
        # idxs = []
        for i in range(4):
            for dir in instructions:
                if dir == "G":
                    # idxs.append(idx)
                    tmp = dirs[idx]
                    start[0] += tmp[0]
                    start[1] += tmp[1]
                if dir == "L":
                    idx += 1
                    idx %= 4
                    # idxs.append(idx)

                if dir == "R":
                    idx -= 1
                    idx %= 4

                    # idxs.append(idx)


            if start[0] == 0 and start[1] == 0:
                return True

        return False

if __name__ == '__main__':
    S = "LLGRL"
    # S = "GL"
    print(Solution().isRobotBounded(S))
