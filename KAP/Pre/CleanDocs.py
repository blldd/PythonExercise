# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:36:58 2017

@author: Don
"""

import os
import re
import time
import nltk
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')
stem = SnowballStemmer('english').stem
wlem = WordNetLemmatizer().lemmatize
stop_words = list(stopwords.words('english'))
path = '../../../title_documents/'
clean_path = '../../../clean_documents/'
docs = os.listdir(path)

marks = ['URL', 'DATE', 'NUM']
cnt = 0
start_t = time.time()
for doc in docs:
    cnt += 1
    if cnt % 1000 == 0:
        print('No %d : %s' % (cnt, doc))
    file = open(path + doc, 'r')

    if not os.path.exists(clean_path):
        os.mkdir(clean_path)
    out_put = open(clean_path + doc, 'w')
    ##############################
    for src_line in file:
        line = src_line.strip().lower()
        if len(line) < 1:
            continue
        # url
        line = re.sub('https?://\S*\.[a-z]{2,5}', ' URL ', line)
        line = re.sub('[^|\s+]\S*\.(?:com|cn|org)', ' URL ', line)
        line = re.sub('url\(\S*\)', ' URL ', line)
        # image
        # line = re.sub('[^|\s+]\S*\.(?:jpg|png|jpge|gif)', ' IMAGE ', line)
        # date
        line = re.sub('\d{2,4}[-/\\\.]\d{1,2}[-/\\\.]\d{1,2}', ' DATE ', line)
        # num
        line = re.sub('\d+(?:,\d{3})*(?:\.\d+)?', ' NUM ', line)
        # symbol
        tokens = re.sub('[^a-zA-Z0-9]+', ' ', line)  # 所有非单词

        tokens = list(filter(lambda x: (x not in stop_words) and (len(x) > 1), re.split('\s+', tokens)))
        tokens = list(map(lambda x: x if x in marks else wlem(x), tokens))
        tokens = list(map(lambda x: x if x in marks else stem(x), tokens))

        out_put.write(' '.join(tokens))
    ##############################
    out_put.close()
    file.close()

end_t = time.time()

print('\nTime: %d' % (end_t - start_t))
