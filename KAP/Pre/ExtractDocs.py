# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:36:58 2017

@author: Don
"""
import os
import re
import time
import urllib
import chardet

start_t = time.time()
line_cnt = 0

# with open('../dataset/documents.txt', 'r', encoding='ascii', errors='ignore') as f:
#     with open('../dataset/split_documents.txt', 'w') as sf:
#         for line in f:
#             line_cnt += 1
#             print(line_cnt)
#             sf.write(line.replace('<article>', '\n<article>'))

with open('../dataset/split_documents.txt', 'r', encoding="ascii", errors="ignore") as f:
    articles = re.findall(r"<article(?:.*?)>(?:.*?)"
                          r"<article_id(?:.*?)>(.*?)</article_id>(?:.*?)"
                          r"<title(?:.*?)>(.*?)</title>(?:.*?)"
                          r"<body(?:.*?)>(.*?)</body>(?:.*?)"
                          r"</article>",
                          f.read(),
                          re.S)

for a in articles:
    print(a[0])
    doc_path = '../../../title_documents/'
    if not os.path.exists(doc_path):
        os.mkdir(doc_path)
    with open(doc_path + a[0].strip(), 'w') as f:
        f.write(a[1] + '\n')
        # f.write(a[2])

end_t = time.time()
print('Time: %d' % (end_t - start_t))
