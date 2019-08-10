# -*- coding: utf-8 -*-
# @ 2019-08-06
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



source_path = '/Users/lidedong/Desktop/3_lable/'

fileList = get_file_list(source_path, [])
affix = ['TIF', 'JPG', 'PNG']

root_path = '/Users/lidedong/Desktop/'
pdf_path = '/Users/lidedong/Desktop/PDF/'

img_cnt = 0
pdf_cnt = 0
oth_cnt = 0
for file in fileList:
    if file[-3:] in affix:
        print(file)
        fp = open(file, 'rb')
        im = Image.open(fp)
        im.show()

        label = input("please input lable:")
        while label not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
            print("PLEASE INPUT RIGHT LABEL!!!!!! ex: 'a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'")
            label = input("please input lable:")

        save_path = root_path + label.upper() + '/' + file.split('/')[-2] + '-' + label.upper()
        os.makedirs(save_path, exist_ok=True)

        cmd = "cp {} {}".format(file, save_path)
        print(cmd)
        os.system(cmd)

        im.close()
        fp.close()

        img_cnt += 1
        print("img {} done...\n".format(img_cnt))

    elif file[-3:] in affix == 'PDF':
        print(file)

        label = input("please input lable:")
        while label not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
            print("PLEASE INPUT RIGHT LABEL!!!!!! ex: 'a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'")
            label = input("please input lable:")

        save_path = pdf_path + label.upper() + '/' + file.split('/')[-2] + '-' + label.upper()
        os.makedirs(save_path, exist_ok=True)

        cmd = "cp {} {}".format(file, save_path)
        print(cmd)
        os.system(cmd)

        pdf_cnt += 1
        print("pdf {} done...\n".format(pdf_cnt))

    else:
        print("other file {} {}".format(file, oth_cnt))


#Recursively Remove Empty Directories, During do something like os.remove(file)
# import os
# for root, dirs, files in os.walk(path, topdown=False):
#     # do something like os.remove(file)
#     if not os.listdir(root):
#         os.rmdir(root)

#Recursively Remove Empty Directories
# import os
# for root, dirs, files in os.walk(path, topdown=False):
#     if not files and not dirs:
#         os.rmdir(root)