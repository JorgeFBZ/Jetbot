# install yolo_reqirements.txt

import cv2 as cv
from ultralytics import YOLO

model = YOLO("yolov12n.pt")

camera = cv.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)15/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv.CAP_GSTREAMER)

while True:
    ret, frame = camera.read()
    if ret:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv.imshow("inference", annotated_frame)
    if cv.waitKey(1) == ord("q"):
        break
    else:
        break
camera.release()
cv.destroyAllWindows()
