# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:24:10 2017

@author: Don
"""

import os  
import time  
  
def mkSubFile(lines,srcName,sub):  
    [des_filename, extname] = os.path.splitext(srcName)  
#    extname = '.tsv'
    filename  = des_filename + '_' + str(sub) + extname  
    print( 'make file: %s' %filename)  
    fout = open(filename,'wb')  
    try:  
        fout.writelines(lines)  
        return sub + 1  
    finally:  
        fout.close()  
  
def splitByLineCount(filename,count):  
    fin = open(filename,'rb')  
    try:     
        buf = []  
        sub = 1  
        for line in fin:  
            buf.append(line)  
            if len(buf) == count:  
                sub = mkSubFile(buf,filename,sub)  
                buf = []  
        if len(buf) != 0:  
            sub = mkSubFile(buf,filename,sub)     
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    splitByLineCount('docu.tsv',10000)  
    end = time.time()  
    print('time is %d seconds ' % (end - begin))  