import cv2
import numpy as np
import time

from djitellopy import Tello

fly = Tello()
fly.connect()
fly.streamoff()

print(fly.get_battery())
time.sleep(3)
fly.takeoff()
time.sleep(8)

fly.move_up(50)
fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame
    cv2.imshow('Result', work_frame)
    ch = cv2.waitKey(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fly.streamoff()
fly.land()
fly.end()
cv2.destroyAllWindows()


