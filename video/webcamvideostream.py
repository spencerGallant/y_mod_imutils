# import the necessary packages
from threading import Thread
import cv2

class WebcamVideoStream:
	def __init__(self, src, w, h, fps):
		# initialize the video camera stream and read the first frame
		# from the stream
		self.stream = cv2.VideoCapture(src)
		#set withdth * height

		
		self.stream.set(cv2.CAP_PROP_CONVERT_RGB, False)
		self.stream.set(cv2.CAP_PROP_FOURCC, 0x59565955)
		self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
		self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
		self.stream.set(cv2.CAP_PROP_FPS, 30)

		#get width/height/framerate and print it
		print("fps: ", self.stream.get(cv2.CAP_PROP_FPS) , " width: " , self.stream.get(cv2.CAP_PROP_FRAME_WIDTH) , " height: " , self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
		
		(self.grabbed, self.frame) = self.stream.read()

		# initialize the variable used to indicate if the thread should
		# be stopped
		self.stopped = False

	def start(self):
		# start the thread to read frames from the video stream
		t = Thread(target=self.update, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		# keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return

			# otherwise, read the next frame from the stream
			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		# return the frame most recently read
		return self.frame

	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True
