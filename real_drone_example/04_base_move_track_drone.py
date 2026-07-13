from djitellopy import tello
import time

drone = tello.Tello()
drone.connect()

dt = 3
distanceCm = 40

drone.set_speed(40)
drone.takeoff()

time.sleep(3 * dt)

for count in range(5):
    drone.move_back(distanceCm)
    time.sleep(dt)
    drone.move_forward(distanceCm+4)
    time.sleep(dt)
    print(count)

drone.land()
time.sleep(dt)
print(drone.get_battery())
drone.end()