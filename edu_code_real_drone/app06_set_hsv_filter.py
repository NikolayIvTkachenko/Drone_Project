import cv2
import numpy as np
import time

from djitellopy import Tello

def callback(argument):
    pass

cv2.namedWindow("Result")
cv2.namedWindow("Setting")

cv2.createTrackbar('H_min', 'Settings', 18, 255, callback)
cv2.createTrackbar('S_min', 'Settings', 56, 255, callback)
cv2.createTrackbar('V_min', 'Settings', 149, 255, callback)
cv2.createTrackbar('H_max', 'Settings', 44, 255, callback)
cv2.createTrackbar('S_max', 'Settings', 174, 255, callback)
cv2.createTrackbar('V_max', 'Settings', 255, 255, callback)

fly = Tello()
fly.connect()
fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame

    frame = cv2.resize(work_frame, (480, 360))
    cv2.imshow("Source", frame)

    img = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos('H_min', 'Settings')
    s1 = cv2.getTrackbarPos('S_min', 'Settings')
    v1 = cv2.getTrackbarPos('V_min', 'Settings')
    h2 = cv2.getTrackbarPos('H_max', 'Settings')
    s2 = cv2.getTrackbarPos('S_max', 'Settings')
    v2 = cv2.getTrackbarPos('V_max', 'Settings')

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    thresh = cv2.inRange(hsv, h_min, h_max)

    cv2.imshow("Result", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fly.streamoff()
fly.end()
cv2.destroyAllWindows()











