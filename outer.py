# -*- coding:utf-8 -*-
'''原始数据去除野值'''
'''具体方法：'''
'''将原始数据划分成窗口，求每个窗口的均值，标准差'''
'''比较每个点和其窗口的均值 '''
'''若：数据点-均值>N*标准差，则认为该点是野值 '''

import os
import math
winLen = 100000
N=5

def readFile(path,newFile):
    data = []
    f = open(path)
    line = f.readline()
    while line:
        value = line.split('\t')[0]
        time = line.split('\t')[1]
        data.append((time,value))
        line = f.readline()

    '''划分窗口'''
    i = 0
    windows = []
    while(i<len(data)):
        w = []
        j = 0
        while(j<winLen and i<len(data)):  
            w.append(data[i])
            j+=1
            i+=1
        windows.append(w)

    '''计算每个窗口的均值，标准差'''
    for w in windows:
        std = 0.0
        avg = 0.0
        
        for i in range(0,len(w)):
            avg += float(w[i][0])
        avg /= len(w)
        
        for i in range(0,len(w)):
            std += (float(w[i][0])-avg)*(float(w[i][0])-avg)
        std /= len(w)
        std = math.sqrt(std)

        i = 0
        while(i<len(w)):
            if(abs(float(w[i][0])-avg)>N*std):
                w.remove(w[i])
                i-=1
            i+=1
        
    '''将去野值后的数据写入文件''' 
    f = open(newFile,'w')
    for w in windows:
        for data in w:
            f.write(data[1])
            f.write('\t')
            f.write(data[0])

    f.close()
    


if(__name__=='__main__'):
    originalFile = 'original data'
    '''处理过野值的文件放入removeFile文件夹'''
    removeFile = originalFile+"_outlier Remove"
    newPath = os.getcwd()+'\\'+removeFile
    if(os.path.exists(removeFile)==False):
        os.mkdir(newPath)
    
    fileList = os.listdir(os.getcwd()+'\\'+originalFile)
    for file in fileList:
        path = os.getcwd()+'\\'+originalFile+'\\'+file
        newFile = newPath + '\\'+file
        readFile(path,newFile)
   
