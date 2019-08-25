import unittest
import re
from collections import defaultdict
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def dfs(word, path, res, start, dic):
    if word == start:
        path.append(word)
        res.append(path[::-1])
    else:
        for w in dic[word]:
            dfs(w, path + [word], res, start, dic)

def find(start, end, words):
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
fname = 'dictionary.txt'
file = open(fname)
lines = file.readlines()

class Test(unittest.TestCase):
    def test1(self):
        start = 'abased'
        target = 'abaser'
        while True:
            words = []
            for line in lines:
                word = line.rstrip()
                if len(word) == len(start):
                    words.append(word)
            break
        exist, path = find(start, target, words)
        if exist:
            result = str(len(path) - 1) + ' '+str(path)
        else:
            result = "No path found"
        self.assertEqual(result, "1 ['abased', 'abaser']")
    def test2(self):
        start = 'abas'
        target = 'aa'
        while True:
            words = []
            for line in lines:
                word = line.rstrip()
                if len(word) == len(start):
                    words.append(word)
            break
        exist, path = find(start, target, words)
        if exist:
            result = str(len(path) - 1) + ' '+str(path)
        else:
            result = "No path found"
        self.assertEqual(result, "No path found")
    def test3(self):
        start = 'lead'
        target = 'gold'
        while True:
            words = []
            for line in lines:
                word = line.rstrip()
                if len(word) == len(start):
                    words.append(word)
            break
        exist, path = find(start, target, words)
        if exist:
            result = str(len(path) - 1) + ' '+str(path)
        else:
            result = "No path found"
        self.assertEqual(result, "3 ['lead', 'load', 'goad', 'gold']")
unittest.main()
