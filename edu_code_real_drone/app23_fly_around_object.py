import cv2
import numpy
import time

from djitellopy import Tello

size = (960, 720)
four_cc = cv2.VideoWriter_four_cc(*'XVID')
fps = 30.0

out = cv2.VideoWriter('videos/work_test_01.avi', four_cc, fps, size)

fly = Tello()
rl_velocity = 0
fb_velocity = 0

ud_velocity = 0
yaw_velocity = 0

fly.connect()
print(fly.get_battery())

fly.takeoff()
time.sleep(8)

fly.move_up(90)
time.sleep(3)

fly.streamon()

frame_read = fly.get_frame_read()
frame = frame_read.frame

cv2.imshow("Recording...", frame)

time.sleep(3)
timer_old = int(time.time())
timer = 0
print(timer_old)

while timer < 13:
    timer = int(time.time()) - timer_old
    frame_read = fly.get_frame_read()
    frame = frame_read.frame

    cv2.imshow("Recording...", frame)
    out.write(frame)

    yaw_velocity = -55
    rl_velocity = 30

    fly.send_rc_control(rl_velocity, fb_velocity, ud_velocity, yaw_velocity)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fly.send_rc_control(0, 0, 0, 0)
time.sleep(1)

fly.land()
fly.streamoff()

print(fly.get_battery())
print(fly.get_flight_time())

fly.end()

out.release()
cv2.destroyAllWindows()





























