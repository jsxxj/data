# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 00:05:51 2017

@author: jsx

主要功能实现：
将一个32*32的矩阵数据文件，按照要求处理成28*28的矩阵文件

"""
from numpy import *

def img2vector(filename):
    # 创建向量
    returnMat = zeros((1,784))

    # 打开数据文件，读取每行内容
    fr = open(filename)
    array = fr.readlines()[2:len(fr.readlines())-2]
    
    for i in range(len(array)):
        line = array[i]
        line = line.strip()[2:-2]
       
        for j in range(28):
            returnMat[0,28*i+j] = int(line[j]) 
    return returnMat
    
if __name__=="__main__":
    img2vector('0.txt')
    print 'Done'
