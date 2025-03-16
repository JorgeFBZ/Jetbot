# Script to check camera feed and Yolo inference

import cv2 as cv

camera = cv.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv.CAP_GSTREAMER)

if not camera.isOpened():
    print("Error al conectar con la cámara.")

cv.namedWindow("Camera", cv.WINDOW_AUTOSIZE)
while True:
    ret, frame = camera.read()
    cv.imshow("Camera", frame)
    if cv.waitKey(1) == ord("q"):
        break
cv.destroyAllWindows()
camera.release()
