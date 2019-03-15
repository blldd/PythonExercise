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

train_file = line_reader('F:/ECNU/Course/KnowledgeAna/train.res')
train_set = dict()
line = next(train_file)
cnt = 0
while line:
    cnt += 1
    content = re.split('\s+', line)
    query = content[0]
    doc = content[2]
    score = content[4]
    train_set.setdefault(query, dict())
    train_set[query].setdefault(doc, dict())
    train_set[query][doc]['score'] = score
    line = next(train_file)

test_file = line_reader('F:/ECNU/Course/KnowledgeAna/test.res')
test_set = dict()
line = next(test_file)
cnt = 0
while line:
    cnt += 1
    content = re.split('\s+', line)
    query = content[0]
    doc = content[2]
    score = content[4]
    test_set.setdefault(query, dict())
    test_set[query].setdefault(doc, dict())
    test_set[query][doc]['score'] = score
    line = next(test_file)

set_path = 'F:/ECNU/Course/KnowledgeAna/data_set/'
corpus = dict()
for query in train_set.keys():
    if not os.path.exists(set_path + query + '/'):
        os.mkdir(set_path + query + '/')
    with open(set_path + query + '/train_set', 'w') as f:
        for doc in train_set[query].keys():
            f.write(doc + ' ' + train_set[query][doc]['score'] + '\n')         #query 下对应的  title    以及相应的  score
    with open(set_path + query + '/test_set', 'w') as f:
        for doc in test_set[query].keys():
            f.write(doc + ' ' + test_set[query][doc]['score'] + '\n')
