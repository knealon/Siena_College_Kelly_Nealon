# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 13:56:40 2014

@author: Kelly
"""

from SimpleCV import Camera, Display, Image

cam=Camera(0)
disp= Display(cam.getImage().size())

stache=Image("mustache.jpg")
mask=stache.createAlphaMask()

while disp.isNotDone():
    img=cam.getImage()
    
    faces=img.findHaarFeatures('face')
    if (faces is not None):
        face=faces.sortArea()[-1]
        myface=face.crop()
        
        noses=myface.findHaarFeatures('nose')
        if (noses is not None ):
            nose=noses.sortArea()[-1]
            
            xmust=face.points[0][0]+nose.x+ (stache.width/2)
            ymust= face.points[0][1]+nose.y+(2*nose.height()/3)
            img=img.blit(stache,pos=(xmust,ymust), mask=mask)
        img.save(disp)