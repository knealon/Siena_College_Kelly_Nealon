import numpy as np
import cv2

FRAMES_PER_SECOND = 24
SECONDS_TO_RECORD = 3

FPS_IN_LOOP = 40

MYBUFFER_LEN = FPS_IN_LOOP*2*SECONDS_TO_RECORD

THRESHOLD = 1.8


################################################################################
# Function to record data. Continue recording until we break it manually.
################################################################################
def record_data(camera_number=0):

    # List to store the images.
    images = []
    count = 0
    img = None
    START_OF_IMAGES = 0

    cap = cv2.VideoCapture(0)

    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

    ret,prev = cap.read()

    time_start=time.time()
    # while the user does not press 'esc'
    no_motion = True
    recording_after_trigger = False
    #while time.time()-time_start<SECONDS_TO_RECORD:
    recorded_time_after_trigger = False


    while (cap.isOpened()):
        ret,frame = cap.read()

        if ret==True:

        if icount<MYBUFFER_LEN:
            #print icount
            images.append(img.copy())
        else:
            #print icount
            START_OF_IMAGES = icount%MYBUFFER_LEN
            images[START_OF_IMAGES] = img.copy()
            
            diff = cv2.absdiff(frame,prev)
            matrix = diff.getNumpy()
            mean = matrix.mean()



            #cv2.imshow('frame',frame)
            cv2.imshow('diff',diff)

            #print icount,mean
            if mean>THRESHOLD and icount>20:
                no_motion = False
                recording_after_trigger = True

            if not recording_after_trigger:
                time_start = time.time()

            #'''
            if time.time()-time_start>SECONDS_TO_RECORD:
                break
            #'''



            #out.write(frame)

            prev = frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    #out.release()
    cv2.destroyAllWindows()


################################################################################
################################################################################
def main():

    camera_number = 0
    record_data(camera_number)

################################################################################
################################################################################
if __name__ == "__main__":
    main()


