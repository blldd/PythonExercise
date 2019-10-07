# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-09-05

"""Example Google style docstrings."""
import json
import os
import sys


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
    des_path = "/Users/lidedong/Desktop/1117/"
    os.makedirs(des_path, exist_ok=True)
    des_path_a = "/Users/lidedong/Desktop/1117/A/"
    os.makedirs(des_path_a, exist_ok=True)
    des_path_b = "/Users/lidedong/Desktop/1117/B/"
    os.makedirs(des_path_b, exist_ok=True)
    des_path_c = "/Users/lidedong/Desktop/1117/C/"
    os.makedirs(des_path_c, exist_ok=True)
    des_path_d = "/Users/lidedong/Desktop/1117/D/"
    os.makedirs(des_path_d, exist_ok=True)

    path = "/Users/lidedong/Desktop/wbfl/"
    error_list = []

    for i in range(1, 241):
        tmp_path = "/Users/lidedong/Desktop/wbfl/tmp/"

        cmd = "rm -rf {}".format(tmp_path)
        print(cmd)
        os.system(cmd)

        os.makedirs(tmp_path, exist_ok=True)

        image_zip = str(i) + "_image.zip"
        label_zip = str(i) + "_label.zip"

        cmd = "unzip {} -d {}".format(path + image_zip, tmp_path)
        print(cmd)
        os.system(cmd)
        cmd = "unzip {} -d {}".format(path + label_zip, tmp_path)
        print(cmd)
        os.system(cmd)

        json_file_list = get_file_list(tmp_path + "Label", [])

        for json_file in json_file_list:
            if json_file[-12:] != "summary.json":
                json_data = json.load(open(json_file, encoding='UTF-8'))
                for key, val in json_data.items():
                    image_path = key
                    try:
                        if val["体检报告类别"] == "A类":
                            to_path = des_path_a + '/'.join(image_path.split('/')[:-1])
                            os.makedirs(to_path, exist_ok=True)

                            cmd = "cp {} {}".format(tmp_path + image_path, to_path)
                            print(cmd)
                            os.system(cmd)

                        elif val["体检报告类别"] == "B类":
                            to_path = des_path_b + '/'.join(image_path.split('/')[:-1])
                            os.makedirs(to_path, exist_ok=True)

                            cmd = "cp {} {}".format(tmp_path + image_path, to_path)
                            print(cmd)
                            os.system(cmd)

                        elif val["体检报告类别"] == "C类":
                            to_path = des_path_c + '/'.join(image_path.split('/')[:-1])
                            os.makedirs(to_path, exist_ok=True)

                            cmd = "cp {} {}".format(tmp_path + image_path, to_path)
                            print(cmd)
                            os.system(cmd)

                        elif val["体检报告类别"] == "D类":
                            to_path = des_path_d + '/'.join(image_path.split('/')[:-1])
                            os.makedirs(to_path, exist_ok=True)

                            cmd = "cp {} {}".format(tmp_path + image_path, to_path)
                            print(cmd)
                            os.system(cmd)

                        else:
                            print("!!!!!!!!!!{} {}!!!!!!!!!".format(key, val))
                    except Exception as e:
                        print(e)
                        print(key)
                        print(val)
                        error_list.append(key)

    print("error_list:".format(error_list))
    print("Done!")

if __name__ == '__main__':
    process()
