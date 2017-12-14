# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:23:31 2017

@author: jsx
主要功能：
将多个TXT文件合并为一个TXT文件

"""
import os
def mergeFile(path):
    files = os.listdir(path)
    outFile = open('merge.txt','w')
    for file in files:
        f = os.path.join(path,file)
        for txt in open(f,'r'):
            outFile.write(txt)
        outFile.write('\n')
    outFile.close()
    
path = "E:\\1_pre_data\\7"
mergeFile(path)
print '合并文件Done!'
        
