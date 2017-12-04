# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 21:37:44 2017

@author: jsx
"""
import os

def splitxt(filePath):
    LIMIT = 1440
    file_count = 0
    url_list =[]
    files = os.listdir(filePath)
    for file in files:
        fileName = os.path.splitext(file)
        fr = os.path.join(filePath,file)
        f = open(fr)
        for line in f:
            #根据行进行分割文件
            url_list.append(line)
            if len(url_list)<LIMIT:
                continue
            newfilePath = filePath +'\\'+"SplitTxt"
            if (os.path.exists(newfilePath)):
                pass
            else:
                os.mkdir(newfilePath)
               
            file_name = newfilePath +'\\'+ fileName[0] + '_' + str(file_count)+".txt"
            
            ##print file_name
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

if __name__ == '__main__':
    filePath="E:\\TimingData\\shijieData"
    splitxt(filePath)
    print 'OK'
