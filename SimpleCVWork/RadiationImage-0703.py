# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 11:56:35 2014

@author: Kelly
"""

from SimpleCV import Camera, Color, Display
from sys import exit
from time import sleep

cam= Camera(1)
previous=cam.getImage()


disp= Display(previous.size())

while not disp.isDone():
    current=cam.getImage()
    motion=current.findMotion(previous)
    count=0
    for m in motion:
        m.draw(color=Color.WHITE,normalize=False)
        outputFile="radiation_%d.jpg" %(count)
        current.save(outputFile)
        print "Saving %s" % (outputFile)
        count+=1
        sleep(1)
        if count>=8:
            exit(0)
           
        
    
    