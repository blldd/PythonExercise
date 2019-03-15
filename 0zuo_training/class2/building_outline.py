# -*- coding:UTF-8 -*-
from collections import OrderedDict


class Node:
    def __init__(self, x, is_add, h):
        self.x = x
        self.is_add = is_add
        self.h = h


def building_outline(mat):
    nodes = [None for i in range(len(mat) * 2)]
    for i in range(len(mat)):
        nodes[i * 2] = Node(mat[i][0], True, mat[i][2])
        nodes[i * 2 + 1] = Node(mat[i][1], False, mat[i][2])
    nodes = sorted(nodes, key=lambda node: node.x)
    # print(nodes)
    map_height_times = OrderedDict()
    map_value_height = {}

    for i in range(len(nodes)):
        if nodes[i].is_add:
            if nodes[i].h not in map_height_times:
                map_height_times[nodes[i].h] = 1
            else:
                map_height_times[nodes[i].h] += 1
        else:
            if map_height_times[nodes[i].h] == 1:
                map_height_times.pop(nodes[i].h)
            else:
                map_height_times[nodes[i].h] -= 1

        if map_height_times == None:
            map_value_height[nodes[i].x] = 0
        else:
            map_value_height[nodes[i].x] = map_height_times.popitem()[0]

    res = []
    start = 0
    pre_height = 0
    for item in map_value_height:
        if pre_height != item[1]:
            if pre_height != 0:
                res.append([start, item[0], pre_height])
            start = item[0]
            pre_height = item[1]
    return res


if __name__ == '__main__':
    mat = [[2, 5, 6], [1, 7, 4]]
    building_outline(mat)
