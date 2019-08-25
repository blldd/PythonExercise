import re
import os
import sys
from collections import defaultdict
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def dfs(word, path, res, start, dic):
    '''
    :param word: target word
    :param path: start word to target word paths
    :param res: all paths
    :param start: start word
    :param dic: dictionary words
    :return: use deep first search method to update res variable and find all valid paths.
    '''
    if word == start:
        path.append(word)
        res.append(path[::-1])
    else:
        for w in dic[word]:
            dfs(w, path + [word], res, start, dic)

def find(start, end, words):
    '''
    :param start: start word
    :param end:  target word
    :param words: dictionary words
    :return: Ture of False means find the path from start to target, if exist a path also return it.
    '''
    words = set(words)
    if end not in words :
        return False, []
    curr = {start}
    dic = defaultdict(list)
    while curr:
        words -= curr
        next = set()
        for word in curr:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word_ = word[:i] + c + word[i + 1:]
                    if word_ in words:
                        next.add(word_)
                        dic[word_].append(word)
        if end in next:
            break
        curr = next
    res = []
    dfs(end, [], res, start, dic)
    if len(res) == 0:
        return False, []
    return True, res[0]

fname = input("Enter dictionary name: ")
if not os.path.isfile(fname):
    sys.exit('Message: Invalid Dictionary Name!')
file = open(fname)
lines = file.readlines()
while True:
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
        words.append(word)
  target = input("Enter target word:")
  break

count = 0
path = [start]
seen = {start : True}
exist, path = find(start, target, words)
if exist:
  print(len(path) - 1, path)
else:
  print("No path found")

