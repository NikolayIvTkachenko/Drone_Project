from djitellopy import tello
import KeyActionModule as kp
#from time import sleep
import time
import cv2
import numpy as np
import math


#PARAMETERS
fSpeed = 117/10  # Forwae Speed in cm/s
aSpeed = 360/10  # Angular Speed Degrees/s
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval

x, y = 500, 500
a = 0
yaw = 0

kp.init()

drone = tello.Tello()
drone.connect()

global img
print(drone.get_battery())

drone.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    d = 0
    global yaw, x, y

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
        yaw += aInterval

    elif kp.getKey("d"):
        yv = speed
        yaw -= aInterval

    if kp.getKey('q'):
        drone.land()
        time.sleep(3)

    if kp.getKey('e'):
        drone.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'DataSource/Pictures/{time.time()}.jpg', img)
        time.sleep(0.3)

    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))

    return [lr, fb, ud, yv]

def drawpoints():
    cv2.circle(img, (300, 500), 20, (0, 0, 255), cv2.FILLED)


while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    drawpoints()

    cv2.imshow("Output", img)
    cv2.waitKey(1)
