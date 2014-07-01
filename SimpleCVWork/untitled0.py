# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 13:01:59 2014

@author: Kelly
"""

from SimpleCV import Camera, VideoStream
import time

cam=Camera()
#display=Display()
while(1):
    img=cam.getImage()
   # img.drawText("Hello World!")
    #img.save(display)
   # time.sleep(5)
    img.show()
    vs = VideoStream("untitled.avi")
