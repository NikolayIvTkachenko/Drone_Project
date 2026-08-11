from djitellopy import Tello
import cv2
import time

fly = Tello()

fly.connect()

print(fly.get_battery())
print(fly.get_current_state())
print(fly.get_highest_temperature())
print(fly.get_lowest_temperature())

dt = 5

fly.takeoff()
time.sleep(dt)
fly.go_xyz_speed(0, 0, 40, 30)
time.sleep(dt)

for i in range(4):
    fly.go_xyz_speed(120, 0, 0, 30)
    time.sleep(dt)
    fly.rotate_clockwise(180)
    time.sleep(dt)

fly.land()
fly.end()