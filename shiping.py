import cv2
img_root="F:\\2Master_Thesis\\Lane_detection\\self_video\\self_data\\self_data_jpg\\"
#img_root='F:\\2Master_Thesis\\Lane_detection\\self_video\\01_r\\01_r\\'
fps=20
size=(3384,1710)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.CV_FOURCC('M','J','P','G')
videoWriter = cv2.VideoWriter('F:/31.avi',fourcc,fps,size)
for i in range(600,2001):
    print(img_root+'01_'+str(i)+'.jpg')
    frame = cv2.imread(img_root+'01_'+str(i)+'.jpg')
    print(frame)
    videoWriter.write(frame)
videoWriter.release()




