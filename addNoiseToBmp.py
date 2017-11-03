# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:39:42 2017

@author: jsx
对指定目录下的图片bmp文件 添加高斯噪声，并另存为一个目录
"""
from PIL import Image
import os
import numpy as np

def process_file(filePath):
    files = os.listdir(filePath)
    for file in files:
        
        fname = os.path.splitext(file)
        fimage = os.path.join(filePath,file)
        imgData = Image.open(fimage)
        fbmp = np.array(imgData)
        noise = np.random.normal(1,0.5,(40,36))
        data = fbmp + noise
        img = Image.fromarray(data)
        if (img.mode!='L'):
            img = img.convert('L')
        newName = int(fname[0].split('_')[0])+1
        imgName = str(newName)+'_' + fname[0].split('_')[1] + '.bmp'
        newImgPath = os.getcwd()+"\\"+"newExpandImage"
        if (os.path.exists(newImgPath)):
            pass
        else:
            os.mkdir(newImgPath)
        img.save(newImgPath+"\\"+file)
        
        
        
if __name__ == '__main__':
    filePath = "E:\\5\\expandImage\\"   
    process_file(filePath)

    print 'Done'
