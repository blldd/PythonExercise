# -*- coding:UTF-8 -*-


def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None  # s节点没有前任节点
    Q.add(s)  # 从s开始搜索
    while Q:
        u = Q.pop()
        print(u)
        print(P)
        print(S)
        for v in G[u].difference(P, S):  # 得到新节点
            Q.add(v)
            P[v] = u  # 记录前任节点
    return P


def components(G):
    comp = []
    seen = set()
    for u in range(9):
        if u in seen:
            continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp


# if __name__ == "__main__":
#     a, b, c, d, e, f, g, h, i = range(9)
#     N = [
#         {b, c, d},  # a
#         {a, d},  # b
#         {a, d},  # c
#         {a, c, d},  # d
#         {g, f},  # e
#         {e, g},  # f
#         {e, f},  # g
#         {i},  # h
#         {h}  # i
#     ]
#     comp = components(N)
#     print(comp)

def rec_dfs(G, s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)


def iter_dfs(G, s):
    S = set()
    Q = []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u


# if __name__ == "__main__":
#     a, b, c, d, e, f, g, h, i = range(9)
#     G = [{b, c, d, e, f},  # a
#          {c, e},  # b
#          {d},  # c
#          {e},  # d
#          {f},  # e
#          {c, g, h},  # f
#          {f, h},  # g
#          {f, g}  # h
#          ]
#     print(list(iter_dfs(G, a)))  # [0, 5, 7, 6, 2, 3, 4, 1]
#


def iddfs(G, s):
    yielded = set()

    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0: return
        if S is None: S = set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurse(G, u, d - 1, S):
                yield v

    n = len(G)
    for d in range(n):
        if len(yielded) == n:
            break
        for u in recurse(G, s, d):
            yield u


#
# if __name__ == "__main__":
#     a, b, c, d, e, f, g, h, i = range(9)
#     N = [
#         {b, c, d},  # a
#         {a, d},  # b
#         {a, d},  # c
#         {a, b, c},  # d
#         {g, f},  # e
#         {e, g},  # f
#         {e, f},  # g
#         {i},  # h
#         {h}  # i
#     ]
#
#     G = [{b, c, d, e, f},  # a
#          {c, e},  # b
#          {d},  # c
#          {e},  # d
#          {f},  # e
#          {c, g, h},  # f
#          {f, h},  # g
#          {f, g}  # h
#          ]
#
#     p = list(iddfs(G, 0))  # [0, 1, 2, 3, 4, 5, 6, 7]
#     m = list(iddfs(N, 0))  # [0, 1, 2, 3]
#     print(p)
#     print(m)


# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空
from collections import deque


def bfs(node):
    if node is None:
        return
    queue = deque()
    nodeSet = set()
    queue.put(node)
    nodeSet.add(node)
    while not queue.empty():
        cur = queue.get()  # 弹出元素
        print(cur.value)  # 打印元素值
        for next in cur.nexts:  # 遍历元素的邻接节点
            if next not in nodeSet:  # 若邻接节点没有入过队，加入队列并登记
                nodeSet.add(next)
                queue.put(next)


# 图的深度优先遍历
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空
def dfs(node):
    if node is None:
        return
    nodeSet = set()
    stack = []
    print(node.value)
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        cur = stack.pop()  # 弹出最近入栈的节点
        for next in cur.nexts:  # 遍历该节点的邻接节点
            if next not in nodeSet:  # 如果邻接节点不重复
                stack.append(cur)  # 把节点压入
                stack.append(next)  # 把邻接节点压入
                set.add(next)  # 登记节点
                print(next.value)  # 打印节点值
                break  # 退出，保持深度优先


if __name__ == "__main__":
    dfs()
