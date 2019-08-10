# -*- coding: utf-8 -*-
# @ 2019-08-09
# @ Li Dedong

import io
import os
import glob
from wand.image import Image
from wand.color import Color
from PyPDF2 import PdfFileReader, PdfFileWriter

memo = {}


def getPdfReader(filename):
    reader = memo.get(filename, None)
    if reader is None:
        reader = PdfFileReader(filename, strict=False)
        memo[filename] = reader
    return reader


def _run_convert(pdfile, savedfilename, page_index, index, res=120):
    pageObj = pdfile.getPage(page_index)  # 获取pdf的第page_index页
    dst_pdf = PdfFileWriter()
    dst_pdf.addPage(pageObj)
    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)
    img = Image(file=pdf_bytes, resolution=res)

    img.format = 'png'

    img.compression_quality = 90
    img.background_color = Color("white")

    img_path = '%s%04d.jpg' % (savedfilename, index)
    img.save(filename=img_path)
    print(img_path)
    img.destroy()


def dealPerPdf(path, file, index):
    savedfilename = path.split('/')[-1].split('-')[0] + '_'
    savedfilename = path + '/2_' + savedfilename  # 要保存的图片文件名

    new_path = os.path.join(path, file)
    pdfile = getPdfReader(new_path)  # 打开pdf文件句柄
    page_nums = pdfile.getNumPages()  # 获取pdf总页数

    for page_index in range(page_nums):
        # print(index)
        _run_convert(pdfile, savedfilename, page_index, index)
        index = index + 1
    return index


def getAllfiles(path):
    files = os.listdir(path)
    files.sort()
    index = 0
    for file in files:
        new_path = path + '/' + file;
        if os.path.isdir(new_path):
            getAllfiles(new_path)
        elif os.path.isfile(new_path):
            is_pdf = file.split('.')[-1]
            if is_pdf != 'pdf':
                continue
            index = dealPerPdf(path, file, index)
            index = index + 1


def DealBatchPdf(path):
    getAllfiles(path)


if __name__ == '__main__':


    # 将pdf文件转为jpg图片文件
    # ./PDF_FILE_NAME 为pdf文件路径和名称
    image_pdf = Image(filename='/Users/lidedong/Desktop/3_lable/A_文字pdf/010011941775312-A/010011941775312_2575583714.PDF', resolution=300)
    image_jpeg = image_pdf.convert('jpg')

    # wand已经将PDF中所有的独立页面都转成了独立的二进制图像对象。我们可以遍历这个大对象，并把它们加入到req_image序列中去。
    req_image = []
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpg'))

    # 遍历req_image,保存为图片文件
    i = 0
    for img in req_image:
        ff = open(str(i) + '.jpg', 'wb')
        ff.write(img)
        ff.close()
        i += 1
