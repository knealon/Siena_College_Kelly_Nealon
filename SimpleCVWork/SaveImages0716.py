# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 10:41:25 2014

@author: Kelly
"""

## TAKE 5 PHOTOS, EACH 2 SECONDS APART, WHEN ESCAPE IS NOT PRESSED

from SimpleCV import Camera, Display
from sys import exit
from time import sleep

cam= Camera(1)
current=cam.getImage()
count=0
while count<5:
   current=cam.getImage()
   outputFile="image_%d.jpg" % (count)
   current.save(outputFile)
   print "Saving %s" %(outputFile)
   count+=1
   sleep(2)
   if count>=5:
       exit()
           
        
    
    