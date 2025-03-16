# Script to check camera feed and Yolo inference

import cv2 as cv

camera = cv.VideoCapture(0)

# Get image shape
# f_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))
# f_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))

while True:
    ret, frame = camera.read()
    cv.imshow("Camera", frame)
    if cv.waitKey(1) == ord("q"):
        break
camera.release()
cv.destroyAllWindows()
