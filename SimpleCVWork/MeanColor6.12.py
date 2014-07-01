# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 13:20:24 2014

@author: Kelly
"""

from SimpleCV import Camera, Display
import time

#if mean color exceeds this amount, do something(record, print, idk)
threshold=10

cam=Camera(1)
previous=cam.getImage()

disp=Display(previous.size())

while not disp.isDone():
    #Get another frame and compare with previous
    current= cam.getImage()
    diff=current-previous
        #convert to matrix and get mean color
    matrix=diff.getNumpy()
    mean=matrix.mean()
    print mean
    #show on screen
    diff.save(disp)
    
    #check if change
    if mean >= threshold:
       print "Motion Detected"
    
    # waitfor 1 second
    #time.sleep(1)
    previous=current