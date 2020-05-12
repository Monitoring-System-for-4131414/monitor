"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""""
import numpy as np
import cv2
#use the camera from local
cap=cv2.VideoCapture(0)

#define the codec and creact VeidioWriter object
#user FourCC code
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #just turn the picture
        #frame = cv2.flip(frame,0)

        #write the flipped frame
        out.write(frame)

        #if test acp delet the window here and test again
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#Release evething if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()