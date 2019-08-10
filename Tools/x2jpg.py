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


def IsValidImage(img_path):
    """
    判断文件是否为有效（完整）的图片
    :param img_path:图片路径
    :return:True：有效 False：无效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except Exception as e:
        print("ERROR: {}\nPATH: {}\n".format(e, img_path))
        bValid = False
    return bValid


def img2jpg(img_file, from_path, to_path):
    """
    转换图片格式
    :param img_file:图片路径
    :return: True：成功 False：失败
    """
    success_list = []
    valid_fail_list = []
    trans_fail_list = []
    if IsValidImage(img_file):
        try:
            str = img_file.rsplit(".", 1)
            jpg_file = str[0] + ".jpg"
            jpg_file = jpg_file.replace(from_path, to_path)

            im = Image.open(img_file)
            save_path = "/".join(jpg_file.split('/')[:-1])
            os.makedirs(save_path, exist_ok=True)

            im.save(jpg_file)
            success_list.append(img_file)
        except Exception as e:
            trans_fail_list.append(img_file)
            print("TRANSFER ERROR: {}\n".format(e))

    else:
        valid_fail_list.append(img_file)
    return (success_list, valid_fail_list, trans_fail_list)


def batch_transfer(from_path, to_path):
    """
    批量转换图片为jpg格式
    :param from_path:
    :param to_path:
    :return:
    """
    os.makedirs(to_path, exist_ok=True)
    file_list = get_file_list(from_path, [])
    for file in file_list:
        img2jpg(file, from_path, to_path)



if __name__ == '__main__':
    # img_path = 'wjk.png'
    # img_path = '/Users/lidedong/Desktop/3_lable/C_手写模糊/010081600213078-C/010081600213078_1091477349.png'
    # print(img2jpg(img_path))

    from_path = '/Users/lidedong/Desktop/3_lable'
    to_path = '/Users/lidedong/Desktop/3_img'
    # img_path.replace(from_path, to_path)
    batch_transfer(from_path, to_path)
