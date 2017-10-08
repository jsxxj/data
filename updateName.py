# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:57:43 2017

@author: jsx
功能：
批量修改指定文件目录下的文件名称，同时加上某个数字
备注：
需要注意的是：py程序 需要和 文件 在同一个目录
"""

import os
import sys

files = os.listdir('E:\\hand')
for name in files:
    a = os.path.splitext(name)
    if a[1] == '.txt':
        b = int(a[0])
        c = int(b-140)
        #newname = '2'+'_'+str(b)+'.bmp'
        newname = str(c)+'.txt'
        print name,newname
        os.rename(name,newname)

print 'Done'
