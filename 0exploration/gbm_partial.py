# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-18

"""Example Google style docstrings."""
from random import shuffle

from sklearn.model_selection import train_test_split


def iter_minibatches(minibatch_size=1000):
    '''
	迭代器
	给定文件流（比如一个大文件），每次输出minibatch_size行，默认选择1k行
	将输出转化成numpy输出，返回X, y
	'''
    X = []
    y = []
    cur_line_num = 0

    train_data, train_label, train_weight, test_data, test_label, test_file = load_data()
    train_data, train_label = shuffle(train_data, train_label, random_state=0)  # random_state=0用于记录打乱位置 保证每次打乱位置不变
    print(type(train_label), train_label)

    for data_x, label_y in zip(train_data, train_label):
        X.append(data_x)
        y.append(label_y)

        cur_line_num += 1
        if cur_line_num >= minibatch_size:
            X, y = np.array(X), np.array(y)  # 将数据转成numpy的array类型并返回
            yield X, y
            X, y = [], []
            cur_line_num = 0


def lightgbmTest():
    import lightgbm as lgb
    # 第一步，初始化模型为None，设置模型参数
    gbm = None
    params = {
        'task': 'train',
        'application': 'regression',  # 目标函数
        'boosting_type': 'gbdt',  # 设置提升类型
        'learning_rate': 0.01,  # 学习速率
        'num_leaves': 50,  # 叶子节点数
        'tree_learner': 'serial',
        'min_data_in_leaf': 100,
        'metric': ['l1', 'l2', 'rmse'],  # l1:mae, l2:mse  # 评估函数
        'max_bin': 255,
        'num_trees': 300
    }

    # 第二步，流式读取数据(每次10万)
    minibatch_train_iterators = iter_minibatches(minibatch_size=10000)

    for i, (X_, y_) in enumerate(minibatch_train_iterators):
        # 创建lgb的数据集
        # y_ = list(map(float, y_))  # 将numpy.ndarray转变为list

        X_train, X_test, y_train, y_test = train_test_split(X_, y_, test_size=0.1, random_state=0)
        y_train = y_train.ravel()
        lgb_train = lgb.Dataset(X_train, y_train)
        lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

        # 第三步：增量训练模型
        # 重点来了，通过 init_model 和 keep_training_booster 两个参数实现增量训练
        gbm = lgb.train(params,
                        lgb_train,
                        num_boost_round=1000,
                        valid_sets=lgb_eval,
                        init_model=gbm,  # 如果gbm不为None，那么就是在上次的基础上接着训练
                        # feature_name=x_cols,
                        early_stopping_rounds=10,
                        verbose_eval=False,
                        keep_training_booster=True)  # 增量训练

        print("{} time".format(i))  # 当前次数
        # 输出模型评估分数
        score_train = dict([(s[1], s[2]) for s in gbm.eval_train()])
        print('当前模型在训练集的得分是：mae=%.4f, mse=%.4f, rmse=%.4f'
              % (score_train['l1'], score_train['l2'], score_train['rmse']))

    return gbm
