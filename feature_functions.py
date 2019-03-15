# -*- coding:UTF-8 -*-

from __future__ import division
import numpy as np
import util_tools
from nltk.translate.bleu_score import sentence_bleu


def lucene_score(instance):
    score = instance["score"]
    return util.get_feature_by_list([score])


def lcs_length(instance):
    queryName = instance["queryName"]
    querySpec = instance["querySpec"]

    productName = instance["productName"]
    productSpec = instance["productSpec"]

    features = [
        len(_longest_common_subsequence(queryName, productName)),
        len(_longest_common_subsequence(querySpec, productSpec)),
    ]

    return util_tools.get_feature_by_list(features)


def lss_length(instance):
    queryName = instance["queryName"]
    querySpec = instance["querySpec"]

    productName = instance["productName"]
    productSpec = instance["productSpec"]

    features = [
        len(_longest_common_substring(queryName, productName)),
        len(_longest_common_substring(querySpec, productSpec)),
    ]

    return util_tools.get_feature_by_list(features)


def levenshtein_distance(instance):
    queryName = instance["queryName"]
    querySpec = instance["querySpec"]

    productName = instance["productName"]
    productSpec = instance["productSpec"]

    features = [
        _levenshtein_distance(queryName, productName),
        _levenshtein_distance(querySpec, productSpec),
    ]

    return util_tools.get_feature_by_list(features)


def overlap(instance):
    queryName = instance["queryName"]
    querySpec = instance["querySpec"]

    productName = instance["productName"]
    productSpec = instance["productSpec"]

    queryName = set(list(queryName))
    querySpec = set(list(querySpec))
    productName = set(list(productName))
    productSpec = set(list(productSpec))

    features = []
    features += _overlap(queryName, productName)
    features += _overlap(querySpec, productSpec)

    return util_tools.get_feature_by_list(features)


def _overlap(a, b):
    features = [
        len(a),
        len(b),
        len(a - b),
        len(b - a),
        len(a | b),
        len(a & b),
        len(a) / len(b) if len(b) != 0 else 0,
        len(b) / len(a) if len(a) != 0 else 0,
        len(a & b) / len(a | b) if len(a | b) != 0 else 0, # Jaccard coefficient
        2 * len(a & b) / (len(a) + len(b)) if (len(a) + len(b)) != 0 else 0, # Dice coefficient
        len(a & b) / len(a) if len(a) != 0 else 0 # Overlap coefficient:
    ]

    return features


def note(instance):
    queryName = instance["queryName"]
    querySpec = instance["querySpec"]

    productNote = instance["productNote"]

    features = [
        len(_longest_common_subsequence(queryName, productNote)),
        len(_longest_common_subsequence(querySpec, productNote)),
        len(_longest_common_substring(queryName, productNote)),
        len(_longest_common_substring(querySpec, productNote)),
        _levenshtein_distance(queryName, productNote),
        _levenshtein_distance(querySpec, productNote),
    ]

    queryName = set(list(queryName))
    querySpec = set(list(querySpec))
    productNote = set(list(productNote))
    features += _overlap(queryName, productNote)
    features += _overlap(querySpec, productNote)

    return util_tools.get_feature_by_list(features)


def spec(instance):
    querySpec = instance["querySpec"]
    productSpec = instance["productSpec"]

    a = set(querySpec.split(u"|"))
    b = set(productSpec.split(u"|"))

    features = []
    features += _overlap(a, b)

    return util_tools.get_feature_by_list(features)


def bleu(instance):
    queryName = list(instance["queryName"])
    querySpec = list(instance["querySpec"])

    productName = list(instance["productName"])
    productSpec = list(instance["productSpec"])

    features = [
        _bleu_score(queryName, productName),
        _bleu_score(querySpec, productSpec)
    ]

    return util_tools.get_feature_by_list(features)


def _bleu_score(a, b):
    candidate = a
    reference = [b]
    score = sentence_bleu(reference, candidate)
    return score


''' 一些距离计算方法 '''
# 最长公共子序列（LCS）, 获取是a, b的最长公共子序列
def _longest_common_subsequence(a, b):
    lengths = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            assert a[x - 1] == b[y - 1]
            result = a[x - 1] + result
            x -= 1
            y -= 1
    return result


# 最长公共子串（LSS）
def _longest_common_substring(a, b):
    m = [[0] * (1 + len(b)) for i in range(1 + len(a))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(a)):
        for y in range(1, 1 + len(b)):
            if a[x - 1] == b[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return a[x_longest - longest: x_longest]


# 编辑距离
def _levenshtein_distance(input_x, input_y):
    xlen = len(input_x) + 1  # 此处需要多开辟一个元素存储最后一轮的计算结果
    ylen = len(input_y) + 1

    dp = np.zeros(shape=(xlen, ylen), dtype=int)
    for i in range(0, xlen):
        dp[i][0] = i
    for j in range(0, ylen):
        dp[0][j] = j

    for i in range(1, xlen):
        for j in range(1, ylen):
            if input_x[i - 1] == input_y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[xlen - 1][ylen - 1]