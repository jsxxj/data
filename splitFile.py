# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:40:03 2017

@author: jsx

主要功能：
按行分割文件
"""

#encoding = utf-8
import os

LIMIT = 40
file_count = 0
url_list =[]

with open("protxt.txt") as f:
    for line in f:
        #根据行进行分割文件
        url_list.append(line)
        if len(url_list)<LIMIT:
            continue
        file_name = str(file_count)+".txt"
        with open(file_name,"w") as file:
            for url in url_list[:-1]:
                file.write(url)
            file.write(url_list[-1].strip())
            url_list= []
            file_count +=1

if url_list:
    file_name = str(file_count)+".txt"
    with open(file_name,"w") as file:
        for url in url_list:
            file.write(url)
 
filePath = os.getcwd()+'\\'+"SplitTxt"
if (os.path.exists(filePath)):
    pass
else:
    os.mkdir(filePath)
    
file.save(filePath+"\\"+file_name)
 
print 'Done'
