# -*- coding:utf-8 -*-

# 文件操作
with open('paper.txt', 'r') as f, open('paper1.txt', 'w') as fout:
    for line in f.readlines():
        if line == ' \n':
            fout.write(line)
        fout.write(line.strip('\n'))
