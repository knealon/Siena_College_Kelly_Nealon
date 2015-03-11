import numpy as np
import cv2
import time
from collections import deque

#cap = cv2.VideoCapture('jellyfish_video.mp4')
cap = cv2.VideoCapture('cosmicrays.mp4')
w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
print w,h

#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#fgbg = cv2.createBackgroundSubtractorMOG2()

fourcc = cv2.cv.CV_FOURCC(*'XVID')
#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
fourcc = cv2.cv.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc, 20, (w,h),True)
#out = cv2.VideoWriter('output.avi',-1, 24, (w,h),True)



ret, prev = cap.read()
icount = 0
#image_buffer = []
image_buffer = deque([])
while(cap.isOpened()):
    ret, img = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(img,prev)

    prev = img

    #print diff.shape
    diff = diff[200:600:1,200:800:1]
    #print diff.shape
    mean = diff.mean()
    #s = sum(sum(sum(diff)))

    cv2.imshow('img',img)
    #cv2.imshow('img',img[200:600:1,200:800:1])
    #cv2.imshow('diff',diff)

    print icount,mean#,s

    if mean<0.05:
        print "TRIGGER -------------------"
        #cv2.imshow('diff',img)

    time.sleep(0.10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    icount += 1

cap.release()
out.release()
cv2.destroyAllWindows()
