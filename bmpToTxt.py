'''
将目录下的所有bmp图片保存为相应的txt文件
'''
import numpy as np
from PIL import Image
import os

def process_file(filePath):
    files = os.listdir(filePath)
    for file in files:
        fname = os.path.splitext(file)
        image = os.path.join(filePath,file)
        bmpData = Image.open(image)
        data = np.array(bmpData)
        newName = fname[0] + '.txt'
        np.savetxt(newName,data,fmt='%s',newline='\n')    
if __name__ == '__main__':
    path = 'E:\\5\\0'
    process_file(path)
    print '...ok...'
        
