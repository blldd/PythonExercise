# -*- coding:UTF-8 -*-

import sys


def read(group):
    d =  {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
          6:"six",  7:"seven", 9:"nine", 10:"ten", 19:"nineteen", 20:"twenty"}


    if len(group) == 0:
        return ""
    if len(group) == 1:
        return d[int(group)]
    if len(group) == 2 and int(group) <= 20:
        return d[int(group)]
    elif len(group) == 2 and int(group) > 20:
        return
    elif len(group) == 3:
        return d[int(group[0])] + "hundrund" + read(group[1:])


def process(num):

    num_s = str(num)
    length = len(num_s)
    split_arr = []

    while length > 0:
        split_arr.append(num_s[-3:])
        num_s = num_s[:-3]
        length = len(num_s)
    split_arr = split_arr[::-1]
    print(split_arr)

    group_size  = len(split_arr)
    res = ""
    for idx, group in enumerate(split_arr):
        i =  group_size - idx
        gs = read(group)
        res += gs
    print(res)


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
              'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        d2 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        if num == 0: return 'Zero'
        if num <= 20: return d1[num]
        if num < 100:
            t, d = num // 10, num % 10
            return d2[t] + ' ' + d1[d] if d > 0 else d2[t]

        if num < 1000:
            h = num // 100
            if num % 100 == 0:
                return d1[h] + ' Hundred'
            return d1[h] + ' Hundred ' + self.numberToWords(num % 100)

        if num < 10 ** 6:
            th = num // 10 ** 3
            if num % 10 ** 3 == 0:
                return self.numberToWords(th) + ' Thousand'
            return self.numberToWords(th) + ' Thousand ' + self.numberToWords(num % 10 ** 3)

        if num < 10 ** 9:
            mi = num // 10 ** 6
            if num % 10 ** 6 == 0:
                return self.numberToWords(mi) + ' Million'
            return self.numberToWords(mi) + ' Million ' + self.numberToWords(num % 10 ** 6)

        if num < 10 ** 12:
            bi = num // 10 ** 9
            if num % 10 ** 9 == 0:
                return d1[num // 10 ** 9] + ' Billion'
            return self.numberToWords(bi) + ' Billion ' + self.numberToWords(num % 10 ** 9)

if __name__ == '__main__':
    num = 123456
    print(Solution().numberToWords(num))
