import cv2
import time
# from cv2 import CascadeClassifier
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

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame
    frame = cv2.flip(work_frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(
        gray,
        scaleFactor=1.1,
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

        if -SET_POINT_X < dX < - TOLERANCE_X:
            print("Вправо")
            right_left_velocity = SPEED_X
        elif TOLERANCE_X < dX < SET_POINT_X:
            print("Влево")
            right_left_velocity = -SPEED_X
        else:
            print("Не леттим вправо/влево")
            right_left_velocity = 0

        if -SET_POINT_Y < dY < - TOLERANCE_Y:
            print("Вверх")
            up_down_velocity = SPEED_Y
        elif TOLERANCE_Y < dY < SET_POINT_Y:
            print("Вниз")
            up_down_velocity = -SPEED_Y
        else:
            print("Не летим вверх.вниз")
            up_down_velocity = 0
        if abs(dX) < SLOWDOWN_THRESHOLD_X:
            right_left_velocity = int(right_left_velocity / 2)
        if abs(dY) < SLOWDOWN_THRESHOLD_Y:
            up_down_velocity = int(up_down_velocity / 2)
        fly.send_rc_control(right_left_velocity, 0, up_down_velocity, 0)
    else:
        print("Нет людей")
        fly.send_rc_control(0, 0, 0, 0)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
print(fly.get_battery())
print(fly.get_flight_time())

fly.land()
fly.streamoff()
fly.end()
cv2.destroyAllWindows()










































