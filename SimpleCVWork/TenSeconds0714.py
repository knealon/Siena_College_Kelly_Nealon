# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 11:29:33 2014

@author: Kelly
"""

from SimpleCV import Camera, Display, Image
import time

cam = Camera()
threshold = 5.0 # if mean exceeds this amount do something
time_start = time.time()

while time.time() - time_start < 10:
    previous = cam.getImage() #grab a frame
    time.sleep(0.5) #wait for half a second
    current = cam.getImage() #grab another frame
    diff = current - previous
    matrix = diff.getNumpy()
    mean = matrix.mean()

    diff.show()

    if mean >= threshold:
            print "Motion Detected"