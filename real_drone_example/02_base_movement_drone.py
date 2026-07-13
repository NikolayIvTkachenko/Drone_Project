from djitellopy import tello
import time

drone = tello.Tello()
drone.connect()

print(drone.get_battery())

time.sleep(5)

drone.speed = 30
drone.takeoff()

time.sleep(8)
drone.move_forward(30)

time.sleep(3)
drone.move_back(30)

time.sleep(3)
drone.move_left(30)
time.sleep(3)
drone.move_right(30)
time.sleep(3)

drone.rotate_clockwise(90)
time.sleep(3)
drone.rotate_counter_clockwise(90)
time.sleep(3)

drone.land()
drone.end()