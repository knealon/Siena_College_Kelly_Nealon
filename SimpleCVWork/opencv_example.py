import numpy as np
import cv2


cap = cv2.VideoCapture(0)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

ret,prev = cap.read()
while (cap.isOpened()):
    ret,frame = cap.read()

    if ret==True:

        diff = cv2.absdiff(frame,prev)

        #cv2.imshow('frame',frame)
        cv2.imshow('diff',diff)

        prev = frame

        #out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
#out.release()
cv2.destroyAllWindows()


