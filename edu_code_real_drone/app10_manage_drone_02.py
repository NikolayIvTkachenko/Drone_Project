import cv2
import numpy as np
from djitellopy import Tello

start = 0

fly = Tello()
fly.connect()
fly.for_back_velocity = 0
fly.left_right_velocity = 0
fly.up_down_velocity = 0
fly.yaw_velocity = 0

img = np.zeros((512, 512, 3), np.uint8)
direction = 0

while True:
    if start == 0:
        fly.takeoff()
        start = 1
        print("start")
    cv2.imshow("Test Window", img)
    ch = cv2.waitKey(5)

    if ch == 119:
        direction = 3 # w
    if ch == 97:
        direction = 1 # a
    if ch == 100:
        direction = 2 # d
    if ch == 115:
        direction = 4 # s
    if ch == 27:
        direction = -1 # ESC

    if direction == 1:
        fly.yaw_velocity = -30
    elif direction == 2:
        fly.yaw_velocity = 30
    elif direction == 3:
        fly.up_down_velocity = 30
    elif direction == 4:
        fly.up_down_velocity = -30
    elif direction == -1:
        break
    else:
        fly.left_right_velocity = 0
        fly.for_back_velocity = 0
        fly.up_down_velocity = 0
        fly.yaw_velocity = 0

    if fly.send_rc_control:
        fly.send_rc_control(
            fly.left_right_velocity,
            fly.for_back_velocity,
            fly.up_down_velocity,
            fly.yaw_velocity
        )
fly.land()
print(fly.get_battery())

fly.end()
cv2.destroyAllWindows()





