import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

name = 'Boris' # replace with your name
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # load the face detection model

cam = PiCamera()
cam.resolution = (512, 304)
cam.framerate = 10
rawCapture = PiRGBArray(cam, size=(512, 304))

img_counter = 0

while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert image to grayscale for face detection
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5) # detect faces
        
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2) # draw a red rectangle around each detected face
            img_name = "dataset/unfamiliar/image_{}.jpg".format(img_counter) # save the photo in the unfamiliar faces directory
            cv2.imwrite(img_name, image)
            print("Unfamiliar face detected and saved as {}".format(img_name))
            img_counter += 1
            
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/{}/image_{}.jpg".format(name, img_counter)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
