# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 12:00:41 2014

@author: Kelly
"""

from SimpleCV import Camera, Color, Display, VideoStream
import time

# Imports to treat command line arguments 
import sys
from sys import argv
import getopt
from subprocess import call


cam= Camera(1)
previous=cam.getImage()





disp= Display(previous.size())

while not disp.isDone():
    current=cam.getImage()
    motion=current.findMotion(previous)
    for m in motion:
        m.draw(color=Color.RED,normalize=False)
        main(camNR, width, height, outname)
        
    current.save(disp)

    previous=current 
    
    
#WEBCAM CAPTURE
def main(cameraNumber, camWidth, camHeight, outputFile):
    BUFFER_NAME = 'motiontest.avi'

    # create the video stream for saving the video file
    #vs = VideoStream(fps=24, filename=fname, framefill=True)
    vs = VideoStream(fps=24, filename=BUFFER_NAME, framefill=True)

    # create a display with size (width, height)
    disp = Display((camWidth, camHeight))

    # Initialize Camera
    cam = Camera(cameraNumber, prop_set={"width": camWidth, "height": camHeight})

    # while the user does not press 'esc'
    while disp.isNotDone():
        # KISS: just get the image... don't get fancy
        img = cam.getImage()

        #img.show()

        # write the frame to videostream
        vs.writeFrame(img)

        # show the image on the display
        img.save(disp)

    # Finished the acquisition of images now Transform into a film
    #self.makefilmProcess = Process(target=self.saveFilmToDisk, args=(BUFFER_NAME, outputFile))
    #self.makefilmProcess.start()
    saveFilmToDisk(BUFFER_NAME, outputFile)


#def saveFilmToDisk(self, bufferName, outname):
def saveFilmToDisk(bufferName, outname):
    # construct the encoding arguments
    params = " -i {0} -c:v mpeg4 -b:v 700k -r 24 {1}".format(bufferName, outname)

    # run avconv to compress the video since ffmpeg is deprecated (going to be).
    call('avconv'+params, shell=True)


if __name__ == '__main__':
    HELP_MSG = '''record.py [options]

        -c &lt;cam NR&gt;   If you know which cam you want to use: set it here, else the first camera available is selected 

        -x &lt;cam Width&gt;    The width of camera capture. Default is 640 pixels
        --width

        -y &lt;cam Height&gt;   The height of camera capture. Default is 480 pixels
        --height

        -o &lt;output&gt;       The name of the output file. Default is the timestmp
        --output    

        -h &lt;help&gt;     Show this message
        '''


    camNR = 1
    width = 640
    height = 480
    outname = 'output_{0}.mp4'.format(time.ctime().replace(" ", "_"))     

    try:
        opts, args = getopt.getopt(argv,"hx:y:o:c:",["width=","height=", "output="])
    except getopt.GetoptError:
        print HELP_MSG
        sys.exit(2)

    # Get the specified command line arguments  
    for opt, arg in opts:
        if opt == '-h':
            print HELP_MSG
            sys.exit()
        elif opt in ("-x", "--width"):
            width = arg
        elif opt in ("-y", "--height"):
            height = arg
        elif opt in ("-c"):
            camNR = arg
        elif opt in ("-o", "--output"):
            outname = arg



