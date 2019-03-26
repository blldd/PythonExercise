

# todo


wnl = WordNetLemmatizer()


def word_lemma(word, pos):
    return str(wnl.lemmatize(word.lower(), pos))


porter_stemmer = PorterStemmer()


def word_stemmer(word):
    return porter_stemmer.stem(word)


def change_PosTag(POStag):
    flag = 0
    if POStag == "NN" or POStag == "NNS" or POStag == "NNP" or POStag == "NNPS":
        POStag = "n"
        flag = 1
    if POStag == "VB" or POStag == "VBD" or POStag == "VBG" or POStag == "VBN" or POStag == "VBP" or POStag == "VBZ":
        POStag = "v"
        flag = 1
    if POStag == "JJ" or POStag == "JJR" or POStag == "JJS":
        POStag = "a"
        flag = 1
    if POStag == "RB" or POStag == "RBR" or POStag == "RBS":
        POStag = "r"
        flag = 1
    if flag == 0:
        POStag = "\\"
    return POStag


def set_dict_key_value(dict, key):
    if key not in dict:
        dict[key] = 0
    dict[key] += 1


# 在字典中删除 value < threshold 的item
def removeItemsInDict(dict, threshold=1):
    if threshold > 1:
        for key in list(dict.keys()):
            if dict[key] < threshold:
                dict.pop(key)


# 将字典中的keys写入指定文件, 排序
def write_dict_keys_to_file(dict, file_path):
    with open(file_path, "w") as file_out:
        file_out.write("\n".join([str(key) for key in sorted(dict.keys())]))


# 将字典写入指定文件, 按key从大到小排序
def write_dict_to_file(dict, file_path):
    with open(file_path, "w") as file_out:
        file_out.write("\n".join(
            ["%s %s" % (str(key), str(dict[key])) for key in sorted(dict.keys(), reverse=True)]))
        # for key in sorted(dict.keys(),reverse=True):
        #     "%s %s" % (str(key), dict[key])


def singleton(cls):
    instances = {}

    def _singleton(*args, **kw):
        if (cls, args) not in instances:
            instances[(cls, args)] = cls(*args, **kw)
        return instances[(cls, args)]

    return _singleton


# key : index; index 从1开始
def load_dict_from_file(dict_file_path):
    # with codecs.open(dict_file_path, encoding="utf-8") as dict_file:
    with open(dict_file_path) as dict_file:
        d = {}
        lines = [line.strip() for line in dict_file]
        for index, line in enumerate(lines):
            if line == "":
                continue
            d[line] = index + 1
        return d


# key : value
def load_key_value_dict_from_file(dict_file_path):
    dict = {}
    dict_file = open(dict_file_path)
    lines = [line.strip() for line in dict_file]
    dict_file.close()

    for line in lines:
        if line == "":
            continue
        key, value = line.split("\t")
        dict[key] = eval(value)
    return dict


def get_feature_by_feat(dict, feat):
    feat_dict = {}
    if feat in dict:
        feat_dict[dict[feat]] = 1
    return Feature("", len(dict), feat_dict)


# [0, 1, 0, 1]
def get_feature_by_list(list):
    feat_dict = {}
    for index, item in enumerate(list):
        if item != 0:
            feat_dict[index + 1] = item
    return Feature("", len(list), feat_dict)


# bow feature  dict = {word:idx} feat_list = [word1, word2...]
def get_feature_by_feat_list(dict, feat_list):
    feat_dict = {}
    for feat in feat_list:
        if feat in dict:
            feat_dict[dict[feat]] = 1
    return Feature("", len(dict), feat_dict)


# tf  feature
def get_feature_by_feat_list_tf(dict, feat_list):
    feat_dict = {}
    for feat in feat_list:
        if feat in dict:
            if dict[feat] not in feat_dict:
                feat_dict[dict[feat]] = 0
            feat_dict[dict[feat]] += 1
    return Feature("", len(dict), feat_dict)


# dict = {word:idx} feat_dict = {word: value of feature}
# dict = {happy:2332} feat_dict = {happy: 3.2}
def get_feature_by_feat_dict(dict, feat_dict):
    new_feat_dict = {}
    for feat in feat_dict:
        if feat in dict:
            new_feat_dict[dict[feat]] = feat_dict[feat]
    return Feature("", len(dict), new_feat_dict)


''' 合并 feature_list中的所有feature '''


def mergeFeatures(feature_list, name=""):
    # print("-"*80)
    # print("\n".join([feature_file.feat_string+feature_file.name for feature_file in feature_list]))
    dimension = 0
    feat_string = ""
    for feature in feature_list:
        if dimension == 0:  # 第一个
            feat_string = feature.feat_string
        else:
            if feature.feat_string != "":
                # 修改当前feature的index
                temp = ""
                for item in feature.feat_string.split(" "):
                    index, value = item.split(":")
                    temp += " %d:%s" % (int(index) + dimension, value)
                feat_string += temp
        dimension += feature.dimension

    merged_feature = Feature(name, dimension, {})
    merged_feature.feat_string = feat_string.strip()
    return merged_feature


def write_example_list_to_file(example_list, to_file):
    with open(to_file, "w") as fout:
        fout.write(
            "\n".join([example.content + " # " + example.comment for example in example_list]))


# 去除标点符号
def remove_punctuation(text):
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    return re.sub(r, ' ', text).strip()


# 将list中所有字符串去掉hashtag变成小写
def remove_hashtag_convert_to_lower(tokens):
    res = []
    for token in tokens:
        if token.startswith("#") and not token.startswith("#XXX"):
            token = token[1:].lower()
        if token.strip() == "":
            continue
        res.append(token)
    return res


def _get_max_dim(in_path):
    with open(in_path) as fin:
        max_dim = 0
        for line in fin:
            feature = line.strip().split(" ", 1)[-1].split(" #")[0]
            dim = 0
            if feature != "":
                dim = int(feature.split(" ")[-1].split(":")[0])
            if dim > max_dim:
                max_dim = dim

        return max_dim


def _add_max_dim_for_file(in_file, max_dim):
    # 在dev中给某个维度加 train_max_dim:0
    with open(in_file) as fin:
        new_lines = []
        flag = 0
        for line in fin:
            if flag == 1:
                new_lines.append(line.strip())
            else:
                target, feature_comment = line.strip().split(" ", 1)
                feature, comment = feature_comment.split("#")
                feature = feature.strip()
                comment = comment.strip()

                dim = 0
                if feature != "":
                    dim = int(feature.split(" ")[-1].split(":")[0])

                if dim < max_dim:
                    feature += " %d:0" % (max_dim)
                    new_line = "%s %s # %s" % (target, feature, comment)
                    new_lines.append(new_line)
                    flag = 1
                else:
                    new_lines.append(line.strip())

    with open(in_file, "w") as fout:
        fout.write("\n".join(new_lines))


def handle_train_test_dim(train_path, dev_path):
    train_max_dim = _get_max_dim(train_path)
    dev_max_dim = _get_max_dim(dev_path)

    if train_max_dim > dev_max_dim:
        # 在dev中给某个维度加 train_max_dim:0
        _add_max_dim_for_file(dev_path, train_max_dim)

    if dev_max_dim > train_max_dim:
        # 在train中给某个维度加 train_max_dim:0
        _add_max_dim_for_file(train_path, dev_max_dim)


import json


def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )


def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )


def _byteify(data, ignore_dicts=False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [_byteify(item, ignore_dicts=True) for item in data]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data


def make_dirs(dirs):
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)


def listdir_no_hidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def check_pairwise_vector(v1, v2):
    if isinstance(v1, list):
        v1 = np.array(v1)
    if isinstance(v2, list):
        v2 = np.array(v2)

    if v1.shape != v2.shape:
        raise ValueError("v1 and v2 should be of same shape. They were "
                         "respectively %r and %r long." % (v1.shape, v2.shape))
    return v1, v2


def cosine_distance(v1, v2):
    """
    :param v1: numpy vector
    :param v2: numpy vector
    :return:
    """
    v1 = normalize(v1)
    v2 = normalize(v2)
    v1, v2 = check_pairwise_vector(v1, v2)

    # cosine = np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))
    #
    # if np.isnan(cosine):
    #    cosine = 1.

    cosine = (v1 * v2).sum()

    return 1. - cosine


def manhattan_distance(v1, v2):
    v1, v2 = check_pairwise_vector(v1, v2)

    diff = v1 - v2
    K = np.abs(diff).sum()

    return K


def euclidean_distance(v1, v2):
    v1, v2 = check_pairwise_vector(v1, v2)

    diff = v1 - v2
    K = np.sqrt((diff ** 2).sum())

    return K


def chebyshev_distance(v1, v2):
    v1, v2 = check_pairwise_vector(v1, v2)

    diff = v1 - v2
    K = np.abs(diff).max()

    return K


LinearKernel = {
    'cosine': cosine_distance,
    'euclidean': euclidean_distance,
    'manhattan': manhattan_distance,
    'chebyshev_distance': chebyshev_distance
}


def normalize(v):
    norm = np.linalg.norm(v, 2)
    if norm == 0:
        return v
    return v / norm


def get_linear_kernel(v1, v2):
    linear_kernel_feats = []
    linear_kernel_names = []
    for function_name in LinearKernel:
        function = LinearKernel[function_name]
        K = function(v1, v2)
        linear_kernel_feats.append(K)
        linear_kernel_names.append(function_name)
    # return linear_kernel_feats, linear_kernel_names
    return linear_kernel_feats


def pearsonr_stat(v1, v2):
    v1, v2 = check_pairwise_vector(v1, v2)

    r, prob = scipy.stats.pearsonr(v1, v2)

    return r


def spearmanr_stat(v1, v2):
    v1, v2 = check_pairwise_vector(v1, v2)

    r, prob = scipy.stats.spearmanr(v1, v2)

    return r


def kendalltau_stat(v1, v2):
    v1, v2 = check_pairwise_vector(v1, v2)

    r, prob = scipy.stats.kendalltau(v1, v2)

    return r


StatKernel = {
    'pearsonr': pearsonr_stat,
    'spearmanr': spearmanr_stat,
    'kendalltau': kendalltau_stat
}


def get_stat_kernel(v1, v2):
    feats = []
    names = []
    for function_name in StatKernel:
        function = StatKernel[function_name]
        K = function(v1, v2)
        feats.append(K)
        names.append(function_name)

    "nan"
    feats = [0.0 if np.isnan(feat) else feat for feat in feats]
    # return feats, names
    return feats


def polynomial(v1, v2, degree=3, gamma=None, coef0=1):
    """
    K(X, Y) = (gamma <X, Y> + coef0)^degree
    :param v1: numpy vector
    :param v2:
    :return:
    """
    v1, v2 = check_pairwise_vector(v1, v2)

    if gamma is None:
        gamma = 1.0 / v1.shape[0]

    K = np.dot(v1, v2)
    K *= gamma
    K += coef0
    K **= degree
    return K


def rbf(v1, v2, gamma=None):
    """
     K(x, y) = exp(-gamma ||x-y||^2)
    :param v1:
    :param v2:
    :param gamma:
    :return:
    """
    v1, v2 = check_pairwise_vector(v1, v2)

    if gamma is None:
        gamma = 1.0 / v1.shape[0]

    K = euclidean_distance(v1, v2)
    K *= -gamma
    K = np.exp(K)
    return K


def laplacian(v1, v2, gamma=None):
    """
     K(x, y) = exp(-gamma ||x-y||_1)
    :param v1:
    :param v2:
    :return:
    """
    v1, v2 = check_pairwise_vector(v1, v2)

    if gamma is None:
        gamma = 1.0 / v1.shape[0]

    K = manhattan_distance(v1, v2)
    K *= -gamma
    K = np.exp(K)
    return K


def sigmoid(v1, v2, gamma=None, coef0=1):
    """
    K(X, Y) = tanh(gamma <X, Y> + coef0)
    :param v1:
    :param v2:
    :return:
    """
    v1, v2 = check_pairwise_vector(v1, v2)

    if gamma is None:
        gamma = 1.0 / v1.shape[0]

    K = np.dot(v1, v2)
    K *= gamma
    K += coef0
    K = np.tanh(K)  # compute tanh in-place
    return K


NonLinearKernel = {
    # 'additive_chi2': additive_chi2,
    # 'chi2': chi2,
    'polynomial': polynomial,
    'rbf': rbf,
    'laplacian': laplacian,
    'sigmoid': sigmoid
}


def get_non_linear_kernel(v1, v2):
    non_linear_feats = []
    non_linear_names = []
    for function_name in NonLinearKernel:
        function = NonLinearKernel[function_name]
        K = function(v1, v2)
        non_linear_feats.append(K)
        non_linear_names.append(function_name)
    # return non_linear_feats, non_linear_names
    return non_linear_feats


def get_all_kernel(v1, v2):
    """
    :param v1:
    :param v2:
    :return:

    example:
        X = [0, 1]
        Y = [1, 0]

        ('euclidean', 2)
        ('cosine', 1.0)
        ('manhattan', 2)
        ('spearmanr', -0.99999999999999989)
        ('kendalltau', -0.99999999999999989)
        ('pearsonr', -1.0)
        ('additive_chi2', -1.0)
        ('sigmoid', 0.76159415595576485)
        ('chi2', 0.36787944117144233)
        ('laplacian', 0.36787944117144233)
        ('polynomial', 1.0)
        ('rbf', 0.36787944117144233)
    """

    linear_kernel_feats = []
    # linear_kernel_names = []
    # linear_kernel_feats, linear_kernel_names = get_linear_kernel(v1, v2)
    linear_kernel_feats = get_linear_kernel(v1, v2)
    stat_kernel_feats = []
    # stat_kernel_names = []
    # stat_kernel_feats, stat_kernel_names = get_stat_kernel(v1, v2)
    stat_kernel_feats = get_stat_kernel(v1, v2)
    non_linear_feats = []
    # non_linear_names = []
    # non_linear_feats, non_linear_names = get_non_linear_kernel(v1, v2)
    non_linear_feats = get_non_linear_kernel(v1, v2)

    all_feats = linear_kernel_feats + stat_kernel_feats + non_linear_feats
    # all_names = linear_kernel_names + stat_kernel_names + non_linear_names

    # return all_feats, all_names
    return all_feats


def condition2sql(query_equal, query_like):
    condition_sql = u" WHERE 1=1"

    # For equal.
    for key, value in query_equal.iteritems():

        if value is None or value.strip() == "":
            continue

        if isinstance(value, str) or isinstance(value, unicode):
            condition_sql += u" and %s = '%s' " % (key, value)

        if isinstance(value, bool) or isinstance(value, int):
            condition_sql += u" and %s = %s " % (key, value)

    # For like.
    for key, value in query_like.iteritems():
        if key is None or key.strip() == "" or value is None or value.strip() == "":
            continue
        condition_sql += u" and %s like '%%%%%s%%%%' " % (key, value)

    return condition_sql


def dict_to_insert_sql(table_name, **key_values):
    keys, values = [], []
    for key, value in key_values.iteritems():
        keys.append(key)
        if isinstance(value, str) or isinstance(value, unicode):
            values.append("'%s'" % value)
        elif isinstance(value, datetime):
            if config.engine_type == "oracle":
                values.append("to_date('%s' , 'yyyy-mm-dd hh24:mi:ss')"
                              % value.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                values.append("'%s'" % value.strftime('%Y-%m-%d %H:%M:%S'))
        elif isinstance(value, float):
            values.append("%f" % value)
        elif isinstance(value, int):
            values.append("%d" % value)
        else:
            raise TypeError("Value type error: key=%s, value type: %s" % (key, type(value)))
    values = map(unicode, values)
    sql = u"insert into %s (%s) values (%s)" % (table_name, ", ".join(keys), ", ".join(values))
    return sql


def get_logger(name=__file__, level=logging.INFO, log_file="log.txt"):
    logger = logging.getLogger(name)

    if getattr(logger, '_init_done__', None):
        logger.setLevel(level)
        return logger

    logger._init_done__ = True
    logger.propagate = False
    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(0)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    del logger.handlers[:]
    logger.addHandler(handler)
    logger.addHandler(file_handler)

    return logger


