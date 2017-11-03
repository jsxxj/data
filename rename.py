import os
def rename(path):
    filelist = os.listdir(path)
    for file in filelist:
        oldFile = os.path.join(path,file)
        if os.path.isdir(oldFile):
            continue
        fileName = os.path.splitext(file)[0]
        fileType = os.path.splitext(file)[1]
        newName = '0' + '_' +fileName + fileType
        '''
        newPath = os.getcwd()+'\\'+'newtxt'
        if (os.path.exists(newPath)==False):
            os.mkdir(newPath)
        '''
        newFile = os.path.join(path,newName)
        os.rename(oldFile,newFile)
        
if __name__ == '__main__':
    path = "E:\\5\\txt"
    rename(path)
