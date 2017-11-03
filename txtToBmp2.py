# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 10:25:21 2017

@author: Administrator

定义函数实现 将指定目录下的TXT文件，转化为bmp图片，并保存到新的文件目录中 

"""

from PIL import Image
import numpy as np
import os

def txtToBmp(filePath):
    files = os.listdir(filePath)
    for file in files:
        if os.path.isdir(file):
            continue
        #print file
        data = np.loadtxt(file)
        img = Image.fromarray(data)
        if (img.mode != 'L'):
            img = img.convert('L')
        fileName = os.path.splitext(file)
        imgName = str(int(fileName[0])) + '.bmp'
        newPath = os.getcwd() + '\\' + 'newImage'
        if (os.path.exists(newPath)==False):
            os.mkdir(newPath)         
        img.save(newPath + '\\' + imgName)
        

if __name__ == '__main__' :     
    filePath = "E:\\5"
    txtToBmp(filePath)
    print '...Done...'
    
