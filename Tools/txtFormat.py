# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:17:08 2017
将txt文件以一定格式输出
例如：
输入：
Aa01A01= 人 士 人物 人士 人氏 人选
输出：
人
士;人物;人士;人氏;人选
士
人物;人士;人氏;人选;人
人物
人士;人氏;人选;人;士
人士
人氏;人选;人;士;人物
人氏
人选;人;士;人物;人士
人选
人;士;人物;人士;人氏
@author: Don
"""
fopen=open("F:\\ana_work\\3\\syn.txt",'rb')  
lines=fopen.readlines()
#print(lines.count)

fw=open("synonym_test_format.txt","w+")  

for line in lines:
    byteLine = bytes.decode(line)[9:]
    array = byteLine.split()   #split wherever space is
    tmp = list.copy(array)
    
    for item in array:
        tmp.remove(item)
        fw.write(item + '\n')
        for it in tmp:
            s = s + it + ';'
        fw.write(s[:len(s)-1] + '\n')
        s = ''
        tmp.append(item)
    #file.write(byteLine)
file.close()
fopen.close()