# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:55:10 2014

@author: Kelly
"""

# Find motion
#pg 204

from SimpleCV import Camera, Color, Display

cam= Camera(1)
previous=cam.getImage()


disp= Display(previous.size())

while not disp.isDone():
    current=cam.getImage()
    motion=current.findMotion(previous)
    for m in motion:
        m.draw(color=Color.RED,normalize=False)
        
    current.save(disp)
    
    previous=current 