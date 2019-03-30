# -*- coding:UTF-8 -*-

# 定义训练数据
import sys

train_data = [[5.1, 3.5, 1.4, 0.2],
              [4.9, 3.0, 1.4, 0.2],

              [7.0, 3.2, 4.7, 1.4],
              [6.4, 3.2, 4.5, 1.5],
              [6.3, 3.3, 6.0, 2.5],
              [5.8, 2.7, 5.1, 1.9]]

# 定义label
label_data = [[1, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [0, 1, 0],
              [0, 0, 1],
              [0, 0, 1]]


def findBestLossAndSplit(train_data, label_data, index):
    """
    :param train_data:
    :param label_data:
    :param index: 表示的第几类
    :return:
    """
    sample_len = len(label_data)
    feature_len = len(train_data[0])
    current_label = []

    # define the minLoss
    minLoss = sys.maxsize

    # feature represents the dimensions of the feature
    feature = 0

    # split represents the detail split value
    split = 0

    # get current label
    for label_index in range(sample_len):
        current_label.append(label_data[label_index][index])

    # trans all features
    for feature_index in range(feature_len):
        ## current feature value
        current_value = []

        for sample_index in range(sample_len):
            current_value.append(train_data[sample_index][feature_index])

        L = 0
        ## different split value
        print(current_value)
        for index in range(len(current_value)):
            R1 = []
            R2 = []
            y1 = 0
            y2 = 0

            for index_1 in range(len(current_value)):
                if current_value[index_1] < current_value[index]:
                    R1.append(index_1)
                else:
                    R2.append(index_1)

            ## calculate the samples for first class
            sum_y = 0
            for index_R1 in R1:
                sum_y += current_label[index_R1]
            if len(R1) != 0:
                y1 = float(sum_y) / float(len(R1))
            else:
                y1 = 0

            ## calculate the samples for second class
            sum_y = 0
            for index_R2 in R2:
                sum_y += current_label[index_R2]
            if len(R2) != 0:
                y2 = float(sum_y) / float(len(R2))
            else:
                y2 = 0

            ## trans all samples to find minium loss and best split
            for index_2 in range(len(current_value)):
                if index_2 in R1:
                    L += pow(float((current_label[index_2] - y1)), 2)
                else:
                    L += pow(float((current_label[index_2] - y2)), 2)

            if L < minLoss:
                feature = feature_index
                split = current_value[index]
                minLoss = L
                print("minLoss")
                print(minLoss)
                print("split")
                print(split)
                print("feature")
                print(feature)
                print("--" * 10)
    return minLoss, split, feature


print(findBestLossAndSplit(train_data, label_data, 0))
