# -*- coding: utf-8 -*-
# @ 2019-08-07
# @ Li Dedong


import os


def rename_dirs(root_dir, label=''):
    for s in os.listdir(root_dir):
        from_dir = os.path.join(root_dir, s)
        if os.path.isdir(from_dir) and s[-2:] != '-' + label:

            to_dir = from_dir + '-' + label
            if os.path.exists(to_dir):
                cmd = "mv {} {}".format(from_dir + '/*', to_dir)
                print(cmd)
                os.system(cmd)
                os.rmdir(from_dir)
            else:
                cmd = "mv {} {}".format(from_dir, to_dir)
                print(cmd)
                os.system(cmd)
    return


source_path = '/Users/lidedong/Desktop/3_lable/D_其他清晰'
rename_dirs(source_path, label='D')
