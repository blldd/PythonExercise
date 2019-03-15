# -*- coding:UTF-8 -*-
import re
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer



vectorizer = CountVectorizer()
transformer = TfidfTransformer()
# line = "https://3241fafd.com https://3241fafd.com  k7777"
# line = re.sub('https?://\S*\.[a-z]{2,5}', ' URL ', line, count=0)
# line = re.sub('\d+(?:,\d{3})*(?:\.\d+)?', ' NUM ', line)
#
# tokens = re.sub('[^a-zA-Z0-9]+', ' ', line)
# print(line)
# print(tokens)
# print(re.split('\s+', tokens))
# tokens = list(filter(lambda x: (x not in ["the", "a"]) and (len(x) > 1), re.split('\s+', tokens)))
# print(tokens)

corpus = ['wonder happi pi day', 'bell beer brand raspberri ale', 'happy day happy day']
vec = vectorizer.fit_transform(corpus)
print(vec)
tfidf = transformer.fit_transform(vec)
print(tfidf)