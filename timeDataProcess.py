# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 23:21:44 2017

@author: jsx
读取指定目录下 的txt（仅有一列）文件，并将其转化为一个数据矩阵，
然后再将之转化为bmp图片，另存在一个新的目录下
"""
import numpy
import os
from PIL import Image

def fileProcess(filePath):
    files = os.listdir(filePath)
    for file in files:
        if os.path.isdir(file):
            continue
        f = os.path.join(filePath,file)
        fr = open(f)
        lines = fr.readlines()
        list = []
        for line in lines:
            line = line.split()
            a = map(float,line)
            list.append(a)
        #print list
        data = numpy.array(list).reshape(20,18)
        #print data
        img = Image.fromarray(data)
        frName = os.path.split(file)
        imgName = frName[1].split('.')[0]+'.bmp'
        #print frName[1].split('.')[0]
        newPath = os.getcwd()+'image'
        if (os.path.exists(newPath)):
            pass
        else:
            os.mkdir(newPath)
        if (img.mode != 'L'):
            img = img.convert('L')
        
        img.save(newPath+'\\'+imgName)
        
        
if __name__ == '__main__':
    filePath = 'K:\\3'
    fileProcess(filePath)
    
    print '...Done...'
    
    
