'''
主要实现 对一个数据矩阵 增加一个标签列
'''
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:26:14 2017

@author: jsx
"""
import numpy as np
import os 


def txtToRow(fileName):
    '''
    returnMat = np.zeros((1,1440))
    #fr = numpy.loadtxt(fileName)
    fr = open(fileName)
    for i in range(40):
        lines = fr.readline()
        print len(lines)
        for j in range(36):
            returnMat[0,40*i+j] = int(lines[j])
    return returnMat
    '''
    fr = open(fileName)
    vec = [float(j) for j in fr.read().strip().replace('\n',' ').split(' ')]
    fr.close()
    return vec

def processfiles():
    trainingFiles = os.listdir('./data/train')
    m = len(trainingFiles)
    trainingMat = np.zeros((m,1440))
    labels = np.empty(m)
    for i in range(m):
        fileName = trainingFiles[i]
        fileStr = fileName.split('.')[0]
        fileN = fileStr.split('_')[0]
        labels[i] = fileN
        trainingMat[i,:] = txtToRow('./data/train/%s' % fileName)
    
    return trainingMat,labels
    
def addRow(data,labels):
    dataMat = np.mat(data)
    m,n = dataMat.shape
    dataLabels = np.column_stack((dataMat,labels))
    np.savetxt('dataLabel.txt',dataLabels,fmt='%s',newline='\n')
    return dataLabels
    
    
if __name__ == '__main__':
    data,labels = processfiles()
    addRow(data,labels)
    print '...ok...'
    
        
        
    
