from djitellopy import tello
import time

dt = 0.5
i = 0

drone = tello.Tello()
drone.connect()

while i < 5:
    print(drone.get_battery())
    time.sleep(dt)

    print(drone.get_acceleration_x())
    time.sleep(dt)

    print(drone.get_acceleration_y())
    time.sleep(dt)

    print(drone.get_acceleration_z())
    time.sleep(dt)

    print(drone.get_barometer())
    time.sleep(dt)

    print(drone.get_distance_tof())
    time.sleep(2 * dt)

    i = i + 1

drone.end()
