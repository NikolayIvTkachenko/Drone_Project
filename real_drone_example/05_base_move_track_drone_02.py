from djitellopy import tello
import time

drone = tello.Tello()
drone.connect()

dt = 3
distanceCm = 50

drone.set_speed(40)
drone.takeoff()

time.sleep(3 * dt)

for i in range(2):
    for j in range(4):
        drone.move_forward(distanceCm)
        time.sleep(dt)
        if j < 3:
            drone.rotate_counter_clockwise(90)
            time.sleep(dt)
    drone.rotate_clockwise(90)
    time.sleep(dt)

drone.land()
print(drone.get_battery())
drone.end()



