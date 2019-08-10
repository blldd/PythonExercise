# -*- coding: utf-8 -*-
# @ 2019-08-09
# @ Li Dedong

# coding:utf-8
import io
import os
import glob
from wand.image import Image
from wand.color import Color
from PyPDF2 import PdfFileReader, PdfFileWriter

memo = {}


def get_pdf_reader(filename):
    reader = memo.get(filename, None)
    if reader is None:
        reader = PdfFileReader(filename, strict=False)
        memo[filename] = reader
    return reader


def _run_convert(pdfile, savedfilename, page_index, res=120):
    try:
        pageObj = pdfile.getPage(page_index)  # 获取pdf的第page_index页
        dst_pdf = PdfFileWriter()
        dst_pdf.addPage(pageObj)
        pdf_bytes = io.BytesIO()
        dst_pdf.write(pdf_bytes)
        pdf_bytes.seek(0)
        img = Image(file=pdf_bytes)

        img.format = 'png'

        img.compression_quality = 90
        img.background_color = Color("white")

        img_path = '%s%04d.jpg' % (savedfilename, page_index)
        img.save(filename=img_path)
        print(img_path)
        img.destroy()
    except Exception as e:
        print(e)

def deal_per_pdf(file, from_path, to_path):
    pdfile = get_pdf_reader(file)  # 打开pdf文件句柄
    page_nums = pdfile.getNumPages()  # 获取pdf总页数

    savedfilename = file.split('.')[0]
    savedfilename = savedfilename.replace(from_path, to_path)

    for page_index in range(page_nums):
        _run_convert(pdfile, savedfilename, page_index)
    return


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


def batch_transfer(from_path, to_path):
    file_list = get_file_list(from_path, [])

    index = 0
    for file in file_list:
        save_path = "/".join(file.split('/')[:-1])
        os.makedirs(save_path, exist_ok=True)

        is_pdf = file.split('.')[-1]
        if is_pdf != 'PDF':
            continue
        deal_per_pdf(file, from_path, to_path)
        index = index + 1
    print(index)


if __name__ == '__main__':
    # path = os.getcwd()
    path = '/Users/lidedong/Desktop/3_lable'
    is_batch_deal = True

    if is_batch_deal:
        from_path = '/Users/lidedong/Desktop/3_lable'
        to_path = '/Users/lidedong/Desktop/3_img'
        batch_transfer(from_path, to_path)
    else:
        filename = '001.pdf'  # 要处理的pdf文件名
        deal_per_pdf(path, filename, 0)
