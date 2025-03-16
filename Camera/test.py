# Script to check camera feed and Yolo inference

import cv2 as cv

# camera = cv.VideoCapture(0)
camera = cv.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)15/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv.CAP_GSTREAMER)

while True:
    ret, frame = camera.read()
    cv.imshow("Camera", frame)
    if cv.waitKey(1) == ord("q"):
        break
camera.release()
cv.destroyAllWindows()
