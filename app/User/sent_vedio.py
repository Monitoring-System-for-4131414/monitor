import numpy as np
import cv2

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