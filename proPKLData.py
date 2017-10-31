# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:55:04 2017

@author: jsx
"""
import os
import numpy
from PIL import Image
from pylab import *
import cPickle

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.png')]
    
def trainSet(path):
    x = []
    trainLabel = []
    Label = os.listdir(path)
    m = len(Label)
    for i in range(m):
        fileName = Label[i]
        file = fileName.split('.')[0]
        #classNumStr = int(file.split('_')[0])
        classNumStr = int(file[4:6])-37
        trainLabel.append(classNumStr)
        
    len_data = 0
    img_path = get_imlist(path)
    for j in range(len(img_path)):
        x.append(img_path[j])
    len_data = len_data + len(img_path)
    
    d = len_data
    trainData = numpy.empty((d,40*36))
    
    while d>0:
        '''将三通道转变成为灰度图像'''
        img = Image.open(x[d-1]).convert('L')
        img_ndarray = numpy.asarray(img,dtype='float64')/256
        trainData[d-1] = numpy.ndarray.flatten(img_ndarray)
        d = d-1
    
    return trainData,trainLabel

def validSet(path):
    x = []
    validLabel = []
    Label = os.listdir(path)
    m = len(Label)
    for i in range(m):
        fileName = Label[i]
        file = fileName.split('.')[0]
        classNumStr = int(file[4:6])
        #classNumStr = int(file.split('_')[0])
        validLabel.append(classNumStr)
        
    len_data = 0
    img_path = get_imlist(path)
    for j in range(len(img_path)):
        x.append(img_path[j])
    len_data = len_data + len(img_path)
    
    d = len_data
    validData = numpy.empty((d,40*36))
    
    while d>0:
        '''将三通道转变成为灰度图像'''
        img = Image.open(x[d-1]).convert('L')
        img_ndarray = numpy.asarray(img,dtype='float64')/256
        validData[d-1] = numpy.ndarray.flatten(img_ndarray)
        d = d-1
    print validLabel
    return validData,validLabel

def testSet(path):
    x = []
    testLabel = []
    Label = os.listdir(path)
    m = len(Label)
    for i in range(m):
        fileName = Label[i]
        file = fileName.split('.')[0]
        #classNumStr = int(file.split('_')[0])
        classNumStr = int(file[4:6])-37
        testLabel.append(classNumStr)
        
    len_data = 0
    img_path = get_imlist(path)
    for j in range(len(img_path)):
        x.append(img_path[j])
    len_data = len_data + len(img_path)
    
    d = len_data
    testData = numpy.empty((d,40*36))
    
    while d>0:
        '''将三通道转变成为灰度图像'''
        img = Image.open(x[d-1]).convert('L')
        img_ndarray = numpy.asarray(img,dtype='float64')/256
        testData[d-1] = numpy.ndarray.flatten(img_ndarray)
        d = d-1
    
    return testData,testLabel
    
def Pkl(data1):
    write_file = open('E:\\englishHand\\pinYinData-raw.pkl','wb')
    #cPickle.dump(data0,write_file,-1)
    cPickle.dump(data1,write_file,-1)
    #cPickle.dump(data2,write_file,-1)
    write_file.close()

if __name__ == '__main__':
    #data0 = trainSet(r'E:\\englishHand\\pinyin\\train\\')
    data1 = validSet(r'E:\\englishHand\\pinyin\\rawtest\\')
    #data2 = testSet(r'E:\\englishHand\\pinyin\\test\\')
    Pkl(data1)
    print 'ok'
