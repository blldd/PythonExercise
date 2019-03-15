# -*- coding:UTF-8 -*-
import sys


# 贪心算法
# 对记录进行按照单位努力升序排列，计算总成绩缺失，先把分数分配给单位努力最小的值

def calc_time(n, r, avg, records):
    required_score = avg * n
    current_score = sum(record[0] for record in records)
    # 差的分数
    residence = required_score - current_score
    # 判断差的分数
    if residence <= 0:
        return 0
    # 对记录排序
    ordered_records = sorted(records, key=lambda k: k[1])
    # 对排序后的结果进行迭代
    total_time = 0
    for record in ordered_records:
        # 计算可支配空间
        space = r - record[0]
        # 如果当前差的分数大于该记录下可支配空间，则计算时间并将residence更新
        if residence > space:
            total_time += space * record[1]
            residence -= space
        else:
            total_time += residence * record[1]
            break
    return total_time


if __name__ == "__main__":
    try:
        while True:
            paras = sys.stdin.readline().strip()
            n, r, avg = [int(p) for p in paras.split(" ")]
            records = []
            for _ in range(n):
                in_put = sys.stdin.readline().strip()
                records.append(list(map(int, in_put.split(" "))))
            # 传入函数并计算
            required_time = calc_time(n, r, avg, records)
            print(required_time)
    except:
        pass