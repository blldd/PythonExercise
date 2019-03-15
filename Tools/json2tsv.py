# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:47:47 2017

@author: Don
"""
# encoding: UTF-8
import re

fin = open('documents.json','rb')            #byte读取
fout = open('docu.tsv','w',encoding='utf-8') #utf-8不然写入会出现GBK错误

id_buf = []  
title_buf = []  
body_buf = [] 

reg_id = re.compile(r'"_id" : "[A-Za-z0-9].*", "t')
reg_title  = re.compile(r'"title" : "[A-Za-z0-9].*", "co') 
reg_body = re.compile(r'"body" : "[A-Za-z0-9].*"')

for line in fin:
    temp_id = re.search(reg_id,line.decode('utf-8'))    
    if temp_id:
        id2string = temp_id.group(0)
    id2string = id2string[9:-5]
    
    temp_title = re.search(reg_title,line.decode('utf-8'))
    if temp_title:
        title2string = temp_title.group(0)
    title2string = title2string[11:-6]
    
    temp_body = re.search(reg_body,line.decode('utf-8'))
    if temp_body:
        body2string = temp_body.group(0)
    body2string = body2string[10:-1]
        

    fout.writelines(id2string + "\t" +title2string + "\t"+ body2string+"\n")
    
    id2string = ""
    title2string = ""
    body2string = ""
fout.close()
fin.close()


















