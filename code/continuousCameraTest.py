#a simple test to see if we can take pictures with the webcam:

import time 

import_start = time.clock()
print("Importing cv2:")

import cv2

import_time = time.clock() - import_start
print("time to import:", import_time)

camera_port = 0
n_img = 10
im_speed = 1  #seconds

#Number of frames to throw away 
ramp_frames = 6
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
warmup_start = time.clock()
camera = cv2.VideoCapture(camera_port)
warmup_time = time.clock() - warmup_start
print("time to warmup:",warmup_time)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
	for i in range(ramp_frames):
		# read is the easiest way to get a full image out of a VideoCapture object.
		retval, im = camera.read()
	return im
 
capture_time = []
store_time = []

for i in range(n_img):
	print("Taking image..."+str(i))
	# Take the actual image we want to keep
	
	capture_start = time.clock()
	camera_capture = get_image()
	capture_time.append( time.clock() - capture_start)
	
	#file = "test_image"+str(i)+".png"
	file = "test_image.png"

	# A nice feature of the imwrite method is that it will automatically choose the
	# correct format based on the file extension you provide. Convenient!
	store_start = time.clock()	
	cv2.imwrite(file, camera_capture)
	store_time.append( time.clock() - store_start)

	#imwrite and get_image are both a bit slow, the easiest thing is to use a delay:
	time.sleep(im_speed)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)

print(	"Capture time per img:",sum(capture_time)/n_img,
	"store time per img:",sum(store_time)/n_img)
