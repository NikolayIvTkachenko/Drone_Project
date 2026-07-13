from djitellopy import tello
import time

drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.speed = 30
drone.takeoff()

time.sleep(8)
drone.flip_forward()
time.sleep(3)
drone.flip_back()

print(drone.get_flight_time())

time.sleep(3)
drone.land()
time.sleep(3)
drone.end()