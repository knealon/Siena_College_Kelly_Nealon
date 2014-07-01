# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:42:49 2014

@author: Kelly
"""

#pg 34 and pg 109
#turn on camera. Start start showing image
#get pixel values, turn them into a matrix
#compare matrix to one acquired previously
#if more than 10% different, write message that says 'CHANGE'
#try to save image at that time?

from SimpleCV import Camera, VideoStream, Display, ImageSet
import numpy as np
# Imports to treat command line arguments 
import sys

import time
    
cam=Camera(1)
img1=cam.getImage()
img1.save
img1.show()
time.sleep(5)
img2=cam.getImage()
img2.show()

diff=img1-img2
diff.show()


#camImages=ImageSet()
#maxImages=10


matrix=diff.getNumpy()
flat=matrix.flatten()
num_change=np.count_nonzero(flat)
percent_change=float(num_change)/float(len(flat))
print(percent_change)
if percent_change> .3:
    print('CHANGE')
    time.sleep(3)
else:
    print('Nothing')
    #for counter in range(maxImages):
       # img=cam.getImage()
       # camImages.append(img)
       # img.show()
        
       # time.sleep(5)
   # camImages.save(verbose=True)
    