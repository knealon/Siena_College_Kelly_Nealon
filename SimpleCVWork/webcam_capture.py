# Import the parts we need from SimpleCV
from SimpleCV import Camera, VideoStream, Display

# This import is just to create the video (if you want to do something meanwhile)
#from multiprocessing import Proce
# To give the correct name to the output file
import time

# Imports to treat command line arguments 
import sys
from sys import argv
import getopt
from subprocess import call



def main(cameraNumber, outputFile):
    BUFFER_NAME = 'ipython1.avi'

    # create the video stream for saving the video file
    #vs = VideoStream(fps=24, filename=fname, framefill=True)
    #vs = VideoStream(fps=24, filename=BUFFER_NAME, framefill=True)
    vs=VideoStream(filename=BUFFER_NAME)
    # create a display with size (width, height)
    disp = Display()

    # Initialize Camera
    cam = Camera(cameraNumber)
    time_start=time.time()
    # while the user does not press 'esc'
    while time.time()-time_start<10:
    # Finally let's starte
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
    #width = 640
    #height = 480
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
    
    main(camNR, outname)
   



#covert to MP4- huge file. 