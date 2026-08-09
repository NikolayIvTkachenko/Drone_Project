import numpy as np
import sys
import cv2

from djitellopy import Tello

fly = Tello()
fly.connect()
fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    image = frame_read.frame

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    edged = cv2.Canny(gray, 10, 250)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 100))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Closed', closed)

    cnts = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    total = 0

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
    print("Find = ", total)

    cv2.imshow("Video", image)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
# cap.release()
