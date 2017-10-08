# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:05:34 2017

@author: jsx
实现：指定目录下的txt矩阵文件转化为灰度图像
并添加噪声

"""
from PIL import Image
import numpy as np
import os

files = os.listdir('E:\\5')
for f in files:
    fname = os.path.splitext(f)
    data = np.empty((40,36))
    data = np.loadtxt(f)
    '''添加噪声'''
    #noise = np.random.normal(2,0.5,(40,36))
    #dataNoise = data + noise
    #np.savetxt('1.txt',dataNoise,fmt=['%s']*dataNoise.shape[1],newline='\n')
    '''print dataNoise'''
    img = Image.fromarray(data)
    if (img.mode!='L'):
        img = img.convert('L')
    imgPath = os.getcwd()+'\\'+'Pictures'
    if (os.path.exists(imgPath)==False):
        os.mkdir(imgPath)
    imgName = str(int(fname[0]))+'.bmp'
    #imgName = '1'+'_'+str(int(fname[0]))+'.bmp'
    img.save(imgPath + '\\' +imgName)

print 'Done'
