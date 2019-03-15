# -*- coding: utf-8 -*-

import os


# s = "I\tam\ta\t\tchinese"
# str = s.strip()
# print str
# arr = str.split("\t")
# print arr
#
# os.mkdir("newdir")

# set1 = set()
# set1.add(1)
# set1.add(1)
# set1.add(1)
# set1.add(1)
# set1.add(1)
#
# print set1

# for i in range(10):
#     if i == 3:
#         break
#     else:
#         print(i)


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


# for n in fab(5):
#     print n

class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

#
# for n in Fab(5):
#     print n




import xlrd

new_excel = "DataALL.xlsx"
new_tsv = "new_data.tsv"
col_name_set = ("商品编号", "商品名称", "商品规格型号", "备注")

def sub_str_dataset(filename, sep):
    with open(filename) as fin, open("time_dblp_test.dat", "w") as fout:
        for line in fin:
            user, item, rating = line.strip().split(sep)
            fout.write("u" + user + "\t" + "i" + item + "\t" + rating + "\t" + "978300760" + "\n")

def _read_data(in_file, col_name_set):
    data = xlrd.open_workbook(in_file)
    for table in data.sheets():
        nrows = table.nrows
        for i in range(nrows):
            # match col index
            if i == 0:
                col_ids = []
                for j in range(table.ncols):
                    if table.cell_value(0, j).strip() in col_name_set:
                        col_ids.append(j)

            row = table.row_values(i)

            # Convert all values to unicode.
            row = map(unicode, row)
            queryProductID, queryName, querySpec, queryNote = row[col_ids[0]], row[col_ids[1]], row[col_ids[2]], row[
                col_ids[3]]

            if len(queryProductID) < 10:
                queryProductID += u'0' * (10 - len(queryProductID))

            yield (queryProductID, queryName, querySpec, queryNote)
    #         arr[i] = (queryProductID, queryName, querySpec, queryNote)
    # return arr


def excel2csv(new_excel):
    with open(new_tsv, "w") as fout:
        visited = set()
        # cnt = 0
        for queryProductID, queryName, querySpec, queryNote in _read_data(new_excel, col_name_set):
            line = "\t".join([queryProductID, queryName, querySpec, queryNote])
            if line in visited:
                # cnt += 1
                # print(cnt)
                continue
            visited.add(line)
            fout.write(line + "\n")

if __name__ == '__main__':
    # class Employee:
    #     '所有员工的基类tesst'
    #     empCount = 0
    #
    #     def __init__(self, name, salary):
    #         self.name = name
    #         self.salary = salary
    #         Employee.empCount += 1
    #
    #     def displayCount(self):
    #         print "Total Employee %d" % Employee.empCount
    #
    #     def displayEmployee(self):
    #         print "Name : ", self.name, ", Salary: ", self.salary
    #
    #
    # print "Employee.__doc__:", Employee.__doc__
    # print "Employee.__name__:", Employee.__name__
    # print "Employee.__module__:", Employee.__module__
    # print "Employee.__bases__:", Employee.__bases__
    # print "Employee.__dict__:", Employee.__dict__
    # # try:
    # #     a = 8/0
    # #     # fh = open("testfile", "w")
    # #     # fh.write("这是一个测试文件，用于测试异常!!")
    # # except ZeroDivisionError:
    # #     print "integer division or modulo by zero"
    # # finally:
    # #     print ""
    #
    # # excel2csv(new_excel)
    #
    filename = "dblp_test.dat"
    # # # split_dataset(filename, 0.6, "\t")
    # # # print("split successfully...")
    # # # rw_dataset(filename, "::")
    sub_str_dataset(filename, "\t")
    pass
