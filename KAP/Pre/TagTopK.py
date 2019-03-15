# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:36:58 2017

@author: Don
"""
import os
import re

def line_reader(file):
    """
    read a file line by line
    :param file:
    :return:
    """
    with open(file, 'r') as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()
    yield None

def splitData(file, k):

    None_file = line_reader(file)
    None_dict = dict()
    line = next(None_file)

    while line:
        #cnt += 1
        content = re.split('\s+', line)
        doc = content[0]
        score = float(content[1])
        None_dict.setdefault(doc, score)
        line = next(None_file)

    reverse_dict = sorted(None_dict.items(), key=lambda item:item[1], reverse = True)    #排序后的返回值是一个list，原字典中的名值对被转换为了list中的元组
    pos_dict = reverse_dict[:k]
    neg_dict = reverse_dict[-k:]
    return pos_dict, neg_dict
#print(len(pos_dict))
#print(neg_dict)


def saveFile(file, pos_dict, neg_dict):
    with open(file, 'a') as f:
        for doc in pos_dict:
            f.write(doc[0] + ' ' + '1' + '\n')

    with open(file, 'a') as f:
        for doc in neg_dict:
            f.write(doc[0] + ' ' + '0' + '\n')

if __name__ == '__main__':
    set_path = '../tag_data_set/'

    for i in range(201,251):
        if not os.path.exists(set_path + str(i) + '/'):
            os.mkdir(set_path + str(i) + '/')
        trainfile = '../data_set/' + str(i) + '/train_set'
        pos_dict, neg_dict = splitData(trainfile, 200)
        tagfile_name = set_path + str(i) + '/train_set'
        saveFile(tagfile_name, pos_dict, neg_dict)

        testfile = 'F:/ECNU/Course/KnowledgeAna/data_set/' + str(i) + '/test_set'
        pos_dict_test, neg_dict_test = splitData(testfile, 50)
        testfile_tag = set_path + str(i) + '/test_set'
        saveFile(testfile_tag, pos_dict_test, neg_dict_test)






'''

with open(tag_file, 'a') as f:
    for doc in pos_dict:
        f.write(doc[0] + ' ' + str(doc[1]) + ' ' + '1' + '\n')

tag_file = line_reader('F:/ECNU/Course/KnowledgeAna/tag_data_set/201/test_set')
with open(tag_file, 'a') as f:
    cnt = 0
    for doc in reverse_dict.keys():
        if cnt < 200:
            f.write(doc + ' ' + reverse_dict[doc] + ' ' + '1' + '\n')  # query 下对应的  title    以及相应的  score
            cnt += 1
with open(tag_file, 'a') as f:
    cnt = 0
    for doc in normal_dict.keys():
        if cnt < 200:
            f.write(doc + ' ' + normal_dict[doc]['score'] + ' ' + '0' + '\n')  # query 下对应的  title    以及相应的  score
            cnt += 1
'''