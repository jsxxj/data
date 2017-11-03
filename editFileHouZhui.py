import os
'''
修改文件后缀名
'''

files = os.listdir('.')
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == ".txt":
        newname = portion[0] + ".doc"
        os.rename(filename,newname)

print '...ok...'
