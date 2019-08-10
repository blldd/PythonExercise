# -*- coding: utf-8 -*-
# @ 2019-08-09
# @ Li Dedong


import os

from PIL import Image


def get_file_list(path, file_list):
    """
    获取path下的所有文件列表
    :param path:
    :param file_list:
    :return:
    """
    if os.path.isfile(path):
        file_list.append(path)
    elif os.path.isdir(path):
        for s in os.listdir(path):
            new_path = os.path.join(path, s)
            get_file_list(new_path, file_list)
    return file_list

def process():
    from_path = '/Users/lidedong/Desktop/3_lable'

    file_list = get_file_list(from_path, [])
    cnt = 0
    for file in file_list:
        if file[-3:]  == 'PDF':
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    process()