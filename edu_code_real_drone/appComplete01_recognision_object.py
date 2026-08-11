import cv2
import time
import numpy as np
from djitellopy import Tello

fly = Tello()

camera_x = 960
camera_y = 720

work_font = cv2.FONT_HERSHEY_SIMPLEX
white = (255, 255, 255)

dx = 150
dy = 150
start = 0

def velocity_reset():
    fly.left_right_velocity = 0
    fly.for_back_velocity = 0
    fly.up_back_velocity = 0
    fly.yaw_velocity = 0

def callbacks():
    pass

def sliders(hsv1, hsv2, sat1, sat2, val1, val2):
    cv2.namedWindow("Settings")

    cv2.createTrackbar('H_min', 'Settings', hsv1, 255, callbacks)
    cv2.createTrackbar('H_max', 'Settings', hsv2, 255, callbacks)
    cv2.createTrackbar('S_min', 'Settings', sat1, 255, callbacks)
    cv2.createTrackbar('S_max', 'Settings', sat2, 255, callbacks)
    cv2.createTrackbar('V_min', 'Settings', val1, 255, callbacks)
    cv2.createTrackbar('V_max', 'Settings', val2, 255, callbacks)

def hsv_filter(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos('H_min', 'Settings')
    s1 = cv2.getTrackbarPos('H_max', 'Settings')
    v1 = cv2.getTrackbarPos('S_min', 'Settings')
    h2 = cv2.getTrackbarPos('S_max', 'Settings')
    s2 = cv2.getTrackbarPos('V_min', 'Settings')
    v2 = cv2.getTrackbarPos('V_max', 'Settings')

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    thresh_frame = cv2.inRange(hsv, h_min, h_max)
    return thresh_frame

def lines_net(image, in_x, in_y):
    cv2.line(image, (int(camera_x / 2) - in_x, 0), (int(camera_x/2) - in_x, camera_y), white, 2)
    cv2.line(image, (int(camera_x / 2) + in_x, 0), (int(camera_x / 2) + in_x, camera_y), white, 2)
    cv2.line(image, (0, int(camera_y / 2) - in_y), (camera_x, int(camera_y / 2) - in_y), white, 2)
    cv2.line(image, (0, int(camera_y / 2) + in_y), (camera_x, int(camera_y / 2) + in_y), white, 2)

def centroid(image, in_x, in_y):
    cv2.circle(image,(in_x, in_y), 10, (0, 0, 255), -1)
    cv2.line(image, (int(camera_x / 2), int(camera_y / 2)), (in_x, in_y), white, 2)

    text = str(in_x) + " " + str(in_y)

    cv2.putText(image, "Fund!", (50, 50), work_font, 1, white, 2)
    cv2.putText(image, text, (in_x + 50, in_y - 50), work_font, 1, white, 2)

# sliders(18, 44, 56, 174, 149, 255)
sliders(16, 60, 25, 255, 197, 255)

fly.connect()
velocity_reset()

fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame

    thresh = hsv_filter(cv2.flip(work_frame, 1))

    moments = cv2.moments(thresh, 1)

    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 1000:
        xc = int(dM10 / dArea)
        yc = int(dM01 / dArea)
        centroid(thresh, xc, yc)
    else:
        velocity_reset()

    lines_net(thresh, dx, dy)
    cv2.imshow("Result", thresh)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
fly.streamoff()
fly.land()
fly.end()
cv2.destroyAllWindows()





































































