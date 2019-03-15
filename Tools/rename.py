a# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:07:50 2017

@author: 18201
"""

import os 
 
def renameFile(path):
 
    direList=os.listdir(path)
    for d in direList:                 #0-9文件夹
        #print(d)
        direPath = os.path.join(path, d)
        fileList = os.listdir(direPath)
        for f in fileList:             #0-9文件夹下的图片文件
            #print(f)
            filePath = os.path.join(direPath,f)
            if os.path.isfile(filePath):
                #print(filePath)
                if(len(f.split("-")) > 1):
                    portion = f.split("-")[1]
                    newName = d + "_" + portion
                elif(len(f.split("_")) > 1):
                    portion = f.split("_")[0]
                    newName = d + "_" + portion + ".png"
                else:
                    newName = d + "_0" + ".png"
                newNamePath=os.path.join(direPath,newName)
                os.rename(filePath,newNamePath)
                print("new we are handleding the {0}".format(newName))
    print("all work is done!")

path = "F:\\Projects\\Elevator\\cvtest\\test"
renameFile(path)    
#import rename
#path="/home/chicho/test/sootAndroidOut/"
#rename.renameFile(path)
#if __name__== "__main__":
#    rename.renameFile(path)