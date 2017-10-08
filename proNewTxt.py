# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:44:15 2017

@author: jsx
"""
import numpy as np
import os


files = os.listdir('E:\\5')
for f in files:
    fname = os.path.splitext(f)
    data = np.empty((40,36))
    data = np.loadtxt(f)
    '''添加噪声'''
    noise = np.random.normal(2.5,0.5,(40,36))
    dataNoise = (data + noise)
    for i in range(40):
        for j in range(36):
            dataNoise[i,j]  = int(dataNoise[i,j])
    print dataNoise
    txtName = str(int(fname[0])+600)+'.txt'
    np.savetxt(txtName,dataNoise,fmt=['%s']*dataNoise.shape[1],newline='\n')
