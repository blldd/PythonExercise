# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import datetime
import time
import random

from matplotlib.font_manager import FontProperties

myfont = FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=14)
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# from apscheduler.schedulers.blocking import BlockingScheduler

#
# def job():
#     now = datetime.datetime.now() + datetime.timedelta(days=-1)
#     print now
#     da = now.date()
#     print da
#     print datetime.date.today()
#
#
# def my_job():
#     print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print time.strftime('%Y-%m-%d', time.localtime(time.time()))
#     print (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
#     print datetime.datetime.now().strftime("%Y-%m-%d")
#     # print time.strftime('%Y-%m-%d %H:%M:%S', datetime.datetime.now() + datetime.timedelta(days=-1))
#     # print time.time() + datetime.timedelta(days=-1)
#
#
# def main():
#     # BlockingScheduler
#     scheduler = BlockingScheduler()
#     scheduler.add_job(job, 'cron', day_of_week='0-6', hour=0, minute=1)
#     scheduler.add_job(my_job, 'interval', seconds=1)
#     scheduler.start()


def _plot_summary(summary_file, img_file):
    with open(summary_file) as fin:
        x = []
        y_precision_product = []
        y_precision_susp = []
        for line in fin:
            num, right_part = line.strip().split(":")
            precision_product, precision_susp = right_part.split(" ")
            x.append(float(num))
            y_precision_product.append(float(precision_product))
            y_precision_susp.append(float(precision_susp))

    plt.figure(figsize=(10, 7))

    plt.plot(x, y_precision_product, '*-', label=u"预测可疑且给出正确商品编号准确率(%)")
    plt.plot(x, y_precision_susp, 'm--', label=u"预测可疑准确率(%)")

    plt.ylabel(u"准确率（%）", fontproperties=myfont, fontsize=18)
    plt.xlabel(u"阈值", fontproperties=myfont, fontsize=18)
    plt.title(u"200条数据（20180315）预测性能与阈值关系", fontproperties=myfont, fontsize=28, color='blue')

    # 遍历每一个点，使用text将y值显示
    for i, j in zip(x, y_precision_product):
        plt.annotate("%.1f" % (j * 100), xy=(i, j))

    for i, j in zip(x, y_precision_susp):
        plt.annotate("%.1f" % (j * 100), xy=(i, j))

    plt.grid(True, which='major')
    plt.legend(prop=myfont)
    plt.savefig(img_file, dpi=500)


if __name__ == '__main__':

    summary_file = "200summary.txt"
    img_file = "200summary.png"
    _plot_summary(summary_file, img_file)
