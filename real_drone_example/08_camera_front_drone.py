import numpy as np
import cv2
from djitellopy import tello
import time

drone = tello.Tello()
drone.connect()
drone.streamoff()


print(drone.get_battery())

time.sleep(3)
drone.takeoff()
time.sleep(8)

drone.move_up(50)

drone.streamon()
while True:
    frame_read = drone.get_frame_read()
    my_frame = frame_read.frame

    cv2.imshow("Result", my_frame)
    ch = cv2.waitKey(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

drone.streamoff()
drone.land()
drone.end()
cv2.destroyAllWindows()