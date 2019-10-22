# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-18

"""Example Google style docstrings."""

import xgboost as xgb
from sklearn.datasets import load_digits  # 训练数据

xgb_params_01 = {}

digits_2class = load_digits(2)
X_2class = digits_2class['data']
y_2class = digits_2class['target']

# dtrain_2class = xgb.DMatrix(X_2class, label=y_2class)
# gbdt_03 = xgb.train(xgb_params_01, dtrain_2class, num_boost_round=3)  # 训练三棵树的模型
# print(gbdt_03.get_dump())  # 显示模型
# gbdt_03a = xgb.train(xgb_params_01, dtrain_2class, num_boost_round=7, xgb_model=gbdt_03)  # 在原模型基础上继续训练
# print(gbdt_03a.get_dump())

print("**" * 40)


xgb_params_01 = {}
xgb_params_02 = {'process_type': 'update',
                 'updater': 'refresh',
                 'refresh_leaf': True}

digits_2class = load_digits(2)
X_2class = digits_2class['data']
y_2class = digits_2class['target']

dtrain_2class = xgb.DMatrix(X_2class, label=y_2class)
gbdt_03 = xgb.train(xgb_params_01, dtrain_2class, num_boost_round=3)  # 训练三棵树的模型
print(gbdt_03.get_dump())  # 显示模型
gbdt_03a = xgb.train(xgb_params_02, dtrain_2class, num_boost_round=3, xgb_model=gbdt_03)  # 在原模型基础上继续训练
print(gbdt_03a.get_dump())
