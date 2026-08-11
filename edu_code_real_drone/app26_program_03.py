from djitellopy import Tello
import cv2
import time


fly = Tello()
fly.connect()

fly.enable_mission_pads()
print(fly.get_battery())

fly.takeoff()
time.sleep(6)

fly.go_xyz_speed_yaw_mid(100, 0, 100, 40, a, 2, 8)
time.sleep(5)

fly.land()
fly.end()
