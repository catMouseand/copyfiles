import os
import shutil
def copyFile(oldpaths,newpaths):
    paths=os.listdir(oldpaths)
    j=0
    for path in paths:
        j+=1
        if j % 5 ==0:
            path = oldpaths + '/' + path
            shutil.copy(path,newpaths)

if __name__=='__main__':
    path='/home/h437/PycharmProjects/20191012Mobilenet/tensorflow_models_learning-master/dataset/train/'
    dirs=os.listdir(path)
    i=0
    for file in dirs:
        filename='/home/h437/PycharmProjects/20191012Mobilenet/tensorflow_models_learning-master/dataset/val'+'/'+"{:0>5d}".format(i)
        os.mkdir(filename)
        newfileDir=filename
        oldfileDir=path+"{:0>5d}".format(i)
        copyFile(oldfileDir,newfileDir)
        i += 1
        if i>=42:
            break

