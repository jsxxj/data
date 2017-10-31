# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:30:30 2017

@author: jsx
"""
import os

files = os.listdir(".")
for filename in files:
    portion = os.path.splitext（filename)
    if portion[1] == ".ifox":
        newname = portion[0] + ".mp4"
        os.rename(filename,newname)
    
    
