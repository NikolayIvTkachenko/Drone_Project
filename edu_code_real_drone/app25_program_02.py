from djitellopy import Tello
import cv2
import time

fly = Tello()
fly.connect()
# ключае работу с площадками
fly.enable_mission_pads()
# задаем какой камерой их детектить
# 0-нижней 1-фронтальной 2-обеими

fly.set_mission_pad_detection_direction(0)

print(fly.get_battery())

fly.takeoff()
time.sleep(6)

fly.go_xyz_speed_mid(100, 0, 100, 30, -2)
time.sleep(5)

fly.rotate_clockwise(180)
time.sleep(5)

fly.go_xyz_speed_mid(-100, 0, 100, 30, 8)
time.sleep(5)
fly.land()
fly.end()

