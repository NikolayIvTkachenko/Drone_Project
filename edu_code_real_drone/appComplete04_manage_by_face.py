import cv2
import time
#from cv2 import CascadeClassifier
from djitellopy import Tello

TOLERANCE_X = 30
TOLERANCE_Y = 30

SLOWDOWN_THRESHOLD_X = 100
SLOWDOWN_THRESHOLD_Y = 100
SPEED_X = 20
SPEED_Y = 20
SET_POINT_X = 960 / 2
SET_POINT_Y = 720 / 2

fly = Tello()

fc = cv2.CascadeClassifier('faces/haarcascade_frontalface_default.xml')

fly.connect()
fly.streamon()
fly.takeoff()
time.sleep(8)
fly.move_up(80)
time.sleep(2)

errorY_old = 0
Ui = 0
Kp = 0.2
Ki = 0
Kd = 0.5
K_brake = 0.5

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame
    frame = cv2.flip(work_frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR5552GRAY)
    faces = fc.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )
    print(len(faces))

    if len(faces) > 0:
        x = faces[0, 0]
        y = faces[0, 1]
        w = faces[0, 2]
        h = faces[0, 3]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), -1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        dX = x + w / 2 - SET_POINT_X
        dY = y + h / 2 - SET_POINT_Y

        errorY = int(dY * K_brake)
        Up = Kp * errorY
        Ud = Kd * (errorY - errorY_old)
        Ui = Ui + Ki * errorY
        SPEED_Y = -int(Up + Ui + Ud)
        errorY_old = errorY

        if abs(SPEED_Y) > 40:
            SPEED_Y = 0
        fly.send_rc_control(0, 0, SPEED_Y, 0)
    else:
        print("Not human")
        fly.send_rc_control(0, 0, 0, 0)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

print(fly.get_battery())
print(fly.get_flight_time())

fly.land()
fly.streamoff()
fly.end()
cv2.destroyAllWindows()



































