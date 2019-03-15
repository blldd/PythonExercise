# -*- coding:UTF-8 -*-
"""
The multithread file.

Authors: dedong (ddlecnu@gmail.com)
"""
import time
from multiprocessing import Pool

#
# def run(fn):
#     # fn: 函数参数是数据列表的一个元素
#     time.sleep(1)
#     return fn * fn
#
#
# if __name__ == "__main__":
#     testFL = [1, 2, 3, 4, 5, 6]
#     print 'shunxu:'  # 顺序执行(也就是串行执行，单进程)
#     s = time.time()
#     for fn in testFL:
#         run(fn)
#
#     e1 = time.time()
#     print "顺序执行时间：", int(e1 - s)
#
#     print 'concurrent:'  # 创建多个进程，并行执行
#     pool = Pool(5)  # 创建拥有5个进程数量的进程池
#     # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
#     rl = pool.map(run, testFL)
#     pool.close()  # 关闭进程池，不再接受新的进程
#     pool.join()  # 主进程阻塞等待子进程的退出
#     e2 = time.time()
#     print "并行执行时间：", int(e2 - e1)
#     print rl

#
# import time
# from multiprocessing import Pool
#
#
# def run(fn):
#     time.sleep(2)
#     print fn
#
#
# if __name__ == "__main__":
#     """
#     output:
#     1
#     23
#
#     4
#     5
#     time : 3.90700006485
#     当有多个进程并行执行时，每个进程得到的时间片时间不一样，哪个进程接受哪个请求以及执行完成时间都是不定的，
#     所以会出现输出乱序的情况。那为什么又会有没这行和空行的情况呢？因为有可能在执行第一个进程时，
#     刚要打印换行符时，切换到另一个进程，这样就极有可能两个数字打印到同一行，
#     并且再次切换回第一个进程时会打印一个换行符，所以就会出现空行的情况。
#     """
#     startTime = time.time()
#     testFL = [1, 2, 3, 4, 5]
#     pool = Pool(10)  # 可以同时跑10个进程
#     pool.map(run, testFL)
#     pool.close()
#     pool.join()
#     endTime = time.time()
#     print "time :", endTime - startTime


# 实例

import os
import time
from multiprocessing import Pool


def getFile(path):
    # 获取目录下的文件list
    fileList = []
    for root, dirs, files in list(os.walk(path)):
        for i in files:
            if i.endswith('.txt') or i.endswith('.10w'):
                fileList.append(root + "\\" + i)
    return fileList


def operFile(filePath):
    # 统计每个文件中行数和字符数，并返回
    filePath = filePath
    fp = open(filePath)
    content = fp.readlines()
    fp.close()
    lines = len(content)
    alphaNum = 0
    for i in content:
        alphaNum += len(i.strip('\n'))
    return lines, alphaNum, filePath


def out(list1, writeFilePath):
    # 将统计结果写入结果文件中
    fileLines = 0
    charNum = 0
    fp = open(writeFilePath, 'a')
    for i in list1:
        fp.write(i[2] + " 行数：" + str(i[0]) + " 字符数：" + str(i[1]) + "\n")
        fileLines += i[0]
        charNum += i[1]
    fp.close()
    print fileLines, charNum


if __name__ == "__main__":
    # 创建多个进程去统计目录中所有文件的行数和字符数
    startTime = time.time()
    filePath = "E:\\Workspace\\PyCharm\\KAP\\dataset"
    fileList = getFile(filePath)
    print(fileList)
    pool = Pool(5)
    resultList = pool.map(operFile, fileList)
    pool.close()
    pool.join()

    writeFilePath = "E:\\Workspace\\PyCharm\\KAP\\dataset\\res.txt"
    print resultList
    out(resultList, writeFilePath)
    endTime = time.time()
    print "used time is ", endTime - startTime
