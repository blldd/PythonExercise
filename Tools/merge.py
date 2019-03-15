# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:04:25 2017

@author: Don
"""

#coding=utf-8 
import os
#获取目标文件夹的路径
#filedir = os.getcwd()+'/corpus'
filedir = 'F:/ECNU/Course/KnowledgeAna/results/OLSR'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('result.res','w')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath):
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()