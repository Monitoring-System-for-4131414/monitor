import numpy as np
import cv2
import time,datetime
from app.kernal.Camera import camera

class Vedio:
    def __init__(self):
        self.__url,self.__starttime = camera.start()
        # dingshiqi here

    def startdireact(self):
        #开始直播
        nowtime = time.asctime( time.localtime(time.time()) )
        url = ''
        #creact vedio file here

        return url,nowtime

    def endireact(self):
        #结束直播
        return True

    def startmonitor(self):
        #开始录像，用于启动机器
        return self.__url
    def endmonitor(self):
        #关闭录像，用于定时生成视频文件
        return True
'''

cap = cv2.VideoCapture("output.avi")


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #just turn the picture
        #frame = cv2.flip(frame,0)

        #if test acp delet the window here and test again
        cv2.imshow('frame',frame)
        key = cv2.waitKey(25)
        if key == 27:
            break
    else:
        break
'''