"""
:param
    none
:return
    none
use camera to make vedio
"""""
import numpy as np
import cv2
import time, datetime


class Camera:


    def __init__(self):
        self.__starttime =  time.asctime( time.localtime(time.time()) )
        #set the url
        self.__urlarr = [self.__url]
        self.__switch = False

    def start(self):
        'return starttime'
        #creact a vedio file here

        #write frame to every file in uelarr
        while(self.__switch == True):
            # write frame
            break

        return self.__starttime

    def turnOn(self):
        self.__switch = True

    def turnOff(self):
        self.__switch = False

    def isOn(self):
        return self.__switch

    def setstarttime(self,newstarttime):
        self.__starttime = newstarttime
        return True

    def seturl(self,newurl):
        self.__url = newurl
        return True

    def getstarttime(self):
        return self.__starttime

    def geturl(self):
        return self.__url
    
    def allframe(self):
        #return the current frame
        pass

camera = Camera()
'''

# use the camera from local
cap = cv2.VideoCapture(0)

# define the codec and creact VeidioWriter object
# user FourCC code
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # just turn the picture
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        # if test acp delet the window here and test again
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release evething if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
'''
