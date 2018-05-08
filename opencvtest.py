#!/usr/bin/python
"""
This program is demonstration for face and object detection using haar-like features.
The program finds faces in a camera image or video stream and displays a red box around them.

Original C implementation by:  ?
Python implementation by: Roman Stanchak, James Bowman
"""
from time import sleep

import cv2




faceCascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/3.4.1_2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
#For reading from a .mp4, avi, etc
video_capture = cv2.VideoCapture("videoplayback.mp4")
#video_capture = cv2.VideoCapture(0) For reading from the camera


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        #Here is when faces are detected (Key frames)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)




    # Display the resulting frame
    frame_copy = cv2.flip( frame, 1)
    cv2.imshow('Video', frame_copy)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()