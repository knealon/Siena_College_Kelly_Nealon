# Import the parts we need from SimpleCV
from SimpleCV import Camera, VideoStream, Display
import skimage

# This import is just to create the video (if you want to do something meanwhile)
#from multiprocessing import Proce
# To give the correct name to the output file
import time

# Imports to treat command line arguments 
import sys
from sys import argv
import getopt
from subprocess import call

from time import time,ctime


def main(cameraNumber, camWidth, camHeight, outputFile):

    BUFFER_NAME = 'cloud3.avi'
    vs = VideoStream(fps=24, filename=BUFFER_NAME, framefill=True)

    disp = Display((camWidth, camHeight))
    cam = Camera(cameraNumber, prop_set={"width": camWidth, "height": camHeight})

    # while the user does not press 'esc'
    start_time = time()
    count = 0
    while disp.isNotDone():
        # KISS: just get the image... don't get fancy
        img = cam.getImage()
        print type(img)

        skimage.io.push(img)

        #img.show()

        # write the frame to videostream
        vs.writeFrame(img)

        # show the image on the display
        img.save(disp)

        current_time = time()
        if current_time-start_time>=5:
            outputFile = "testing_chunk_%d.mp4" % (count)
            print "Saving %s" % (outputFile)
            saveFilmToDisk(BUFFER_NAME, outputFile)
            start_time = time()
            count += 1



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


    camNR = 0
    width = 640
    height = 480
    outname = 'output_{0}.mp4'.format(ctime().replace(" ", "_"))     

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

    # Finally let's start
    main(camNR, width, height, outname)



#covert to MP4- huge file. 
