import time
from djitellopy import Tello
fly = Tello()

dt = 0.5
i = 0
fly.connect()
while i < 5:
    print(fly.get_battery())
    time.sleep(dt)
    print(fly.get_barometer())
    time.sleep(dt)
    print(fly.get_distance_tof())
    time.sleep(2*dt)
    i = i + 1

fly.end()

