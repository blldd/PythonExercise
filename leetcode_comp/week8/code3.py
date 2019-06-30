# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/16 10:59 AM
@Author  : ddlee
@File    : code3.py
"""
import copy

"""
1105. 填充书架
附近的家居城促销，你买回了一直心仪的可调节书架，打算把自己的书都整理到新的书架上。
你把要摆放的书 books 都整理好，叠成一摞：从上往下，第 i 本书的厚度为 books[i][0]，高度为 books[i][1]。
按顺序 将这些书摆放到总宽度为 shelf_width 的书架上。
先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelf_width），然后再建一层书架。
重复这个过程，直到把所有的书都放在书架上。
需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。 
例如，如果这里有 5 本书，那么可能的一种摆放情况是：
第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之
以这种方式布置书架，返回书架整体可能的最小高度。

输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
输出：6
解释：
3 层书架的高度和为 1 + 3 + 2 = 6 。
第 2 本书不必放在第一层书架上。

动态规划解
"""


class Solution:
    def minHeightShelves1(self, books, shelf_width):
        res = 0
        books = sorted(books, key=lambda x: x[1])
        print(books)

        width = 0
        row = []
        book_tmp = []
        while books:
            book = books.pop()
            if width + book[0] <= shelf_width:
                row.append(book)
                width += book[0]
            else:
                book_tmp.append(book)

            if width == shelf_width:
                one_row_max_height = max([x[1] for x in row])
                res += one_row_max_height
                row = []
                width = 0
                while book_tmp:
                    books.append(book_tmp.pop())

        one_row_max_height = max([x[1] for x in row])
        res += one_row_max_height

        return res

    def minHeightShelves(self, books, shelf_width):
        res = 0
        books = books[::-1]
        print(books)

        width = 0
        row = []
        book_tmp = []
        while books:
            book = books.pop()
            if width + book[0] <= shelf_width:
                row.append(book)
                width += book[0]
            else:
                book_tmp.append(book)
                while book_tmp:
                    books.append(book_tmp.pop())
                one_row_max_height = max([x[1] for x in row])
                res += one_row_max_height
                row = []
                width = 0

            if width == shelf_width:
                one_row_max_height = max([x[1] for x in row])
                res += one_row_max_height
                row = []
                width = 0

        if row:
            one_row_max_height = max([x[1] for x in row])
            res += one_row_max_height

        return res


if __name__ == '__main__':
    books = [[1, 1], [2, 3], [3, 3], [1, 1], [1, 1], [1, 1], [2, 2]]
    shelf_width = 4

    # books = [[7, 3], [8, 7], [2, 7], [2, 5]]
    # shelf_width = 10

    print(Solution().minHeightShelves(books, shelf_width))
