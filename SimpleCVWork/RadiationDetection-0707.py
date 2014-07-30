# -*- coding: utf-8 -*-
"""
Created on Mon Jul 07 10:09:01 2014

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
    blobs=current.findBlobs()
    blobs.show(width=5)