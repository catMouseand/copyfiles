from PIL import Image
import os
path='F:\\2Master_Thesis\\Lane_detection\\self_video\\self_data\\self_data\\'
path_jpg='F:\\2Master_Thesis\\Lane_detection\\self_video\\self_data\\self_data_jpg\\'
for i in os.listdir(path):
    im=Image.open(path+i)
    rgb_im=im.convert('RGB')
    i2=i.split('.')
    rgb_im.save(path_jpg+i2[0]+'.jpg')
    print(path_jpg+i+'.jpg')
