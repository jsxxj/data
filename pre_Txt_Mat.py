# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:26:14 2017

@author: jsx

将指定目录下的TXT文件 合并成为大的数据文件 
最后一列 为该条数据文件的标签

"""
import numpy as np
import os 


def txtToRow(fileName):
    fr = open(fileName)
    #vec = [str(j) for j in fr.read().strip().replace('\n',' ')]
    #vec = [str(j) for j in fr.read().strip().replace('\n',' ').split(' ')]
    vec = [float(j) for j in fr.read().strip().replace('\n',' ').split(' ')]
    fr.close()
    return vec

def processfiles():
    trainingFiles = os.listdir('./data/timeSeris/9-train/')
    m = len(trainingFiles)
    trainingMat = np.zeros((m,1440))
    labels = np.empty(m)
    for i in range(m):
        fileName = trainingFiles[i]
        fileStr = fileName.split('.')[0]
        fileN = fileStr.split('_')[0]
        labels[i] = fileN
        trainingMat[i,:] = txtToRow('./data/timeSeris/9-train/%s' % fileName)  
    return trainingMat,labels
    
def addRow(data,labels):
    dataMat = np.mat(data)
    m,n = dataMat.shape
    dataLabels = np.column_stack((dataMat,labels))
    np.savetxt('timeData.txt',dataLabels,fmt='%s',newline='\n')
    return dataLabels
    
def processRawData():
    rawData = os.listdir('./data/timeSeris/raw/')
    m =len(rawData)
    rawDataMat = np.zeros((m,1440))
    for i in range(m):
        fileName = rawData[i]
        rawDataMat[i,:] = txtToRow('./data/timeSeris/raw/%s' % fileName) 
    np.savetxt('rawData.txt',rawDataMat,fmt='%s',newline='\n')
    return rawDataMat
       
if __name__ == '__main__':
    data,labels = processfiles()
    addRow(data,labels)
    processRawData()
    print '...ok...'
    
        
        
    
