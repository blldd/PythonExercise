# -*- coding:UTF-8 -*-
"""
#
##
###
####
#####
"""

"""
  #
 ###
#####
"""






def print_hash():
    a = int(input('how many lines'))
    for i in range(1, a + 1):
        for space in range(a - i):
            print " ",
        for hash in range(2 * i - 1):
            print "#",
        print


if __name__ == '__main__':
    # print_hash()
    l = [3,6,2,5,7]
    print l
    # print l.sort()
    print sorted(l)
    print l
