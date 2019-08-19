# -*- coding: utf-8 -*-
# @ 2019-08-12
# @ Li Dedong

import os


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


if __name__ == '__main__':
    source_path = '/Users/lidedong/Desktop/3_lable/'
    relative_path = 'Image/'

    fileList = get_file_list(source_path, [])

    with open("list.txt", "w", encoding="utf-8") as fout:
        for file in fileList:
            if file[-3:] == 'JPG':
                new_file = file.replace(source_path, relative_path) + "\n"
                fout.write(new_file)
    print("Done !")
