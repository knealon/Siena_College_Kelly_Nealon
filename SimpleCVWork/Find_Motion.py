# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:55:10 2014

@author: Kelly
"""

# Find motion
#pg 204

from SimpleCV import Camera, Color, Display

cam= Camera(0)
previous=cam.getImage()

disp= Display(previous.size())

while not disp.isDone():
    current=cam.getImage()
    #motion=current.findMotion(previous,method='BM') # Robust but slow.
    motion=current.findMotion(previous,method='LK')
    # We should learn about the ``window" kwarg.
    #motion=current.findMotion(previous,method='HS',window=11)
    #motion=current.findMotion(previous,method='HS',window=4)
    #motion.draw()
    #print motion
    for m in motion:
        m.draw(color=Color.RED,normalize=False)
        
    current.save(disp)
    
    #current.show()
    previous=current 
