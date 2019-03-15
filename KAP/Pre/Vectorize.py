# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:36:58 2017

@author: Don
"""

import re
import time
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


class Vector(object):
    def __init__(self, qid):
        self.train_file = '../data_set/' + qid + '/train_set'
        self.test_file = '../data_set/' + qid + '/test_set'
        self.train_set = dict()
        self.test_set = dict()

        with open(self.train_file, 'r') as f:
            for line in f:
                token = re.split('\s+', line)
                self.train_set.setdefault(token[0], token[1])

        with open(self.test_file, 'r') as f:
            for line in f:
                token = re.split('\s+', line)
                self.test_set.setdefault(token[0], token[1])

        self.corpus = []
        self.doc_idx = dict()
        idx = 0
        #print(self.train_set.keys())
        #print(list(self.train_set.keys()))

        for doc in list(self.train_set.keys()) + list(self.test_set.keys()):
            try:
                with open('../../../clean_documents/' + doc, 'r') as f:
                    self.corpus.append(f.read())
                    self.doc_idx.setdefault(doc, idx)
                    idx += 1
            except Exception as e:
                print(e)
                print(doc)
        # print(len(list(self.train_set.keys()) + list(self.test_set.keys())))
        # print(idx)
        self.vectorizer = CountVectorizer()
        self.transformer = TfidfTransformer()
        #print(self.corpus)                                    #['deport go green left week', '', 'embassi afghanistan ottawa']
        vec = self.vectorizer.fit_transform(self.corpus)
        # print(vec)     #  (9991, 5652)	1
        self.tfidf = self.transformer.fit_transform(self.vectorizer.fit_transform(self.corpus))
        #print(self.tfidf)                                     #  (9992, 2064)	0.394127944462
        self.word = self.vectorizer.get_feature_names()
        #print(self.word)                                      #['aa', 'aaa', 'aacut', 'aadio', 'aadnesen']
        self.weight = self.tfidf.toarray()
        #print(self.weight)                                    #[[ 0.  0.  0. ...,  0.  0.  0.] [ 0.  0.  0. ...,  0.  0.  0.]]

    def get_vector(self):
        return self.word, self.weight, self.doc_idx

if __name__ == '__main__':
    start_t = time.time()
    vector = Vector('201')
    word, weight, doc_idx = vector.get_vector()
    print(word)
    print(len(weight[12]))
    print(doc_idx)
    end_t = time.time()
    print('Time: %d' % (end_t - start_t))

