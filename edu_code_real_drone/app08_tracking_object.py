import cv2
import time
import numpy as np

from djitellopy import Tello

work_font = cv2.FONT_HERSHEY_SIMPLEX

white = (255, 255, 255)
red = (0, 0, 255)
hsv_min = np.array((18, 56, 149), np.uint8)
hsv_max = np.array((44, 174, 255), np.uint8)
fly = Tello()
fly.connect()

print(fly.get_battery())

fly.takeoff()
time.sleep(8)

fly.move_up(50)
fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame

    img = cv2.flip(work_frame, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    moments = cv2.moments(thresh, 1)

    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 1000:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)

        cv2.circle(thresh, (x, y), 10, (0, 0, 255), -1)
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

        text = str(x) + " " + str(y)
        xd = x + 50
        yd = y + 50

        cv2.putText(img, "Find!", (50, 50), work_font, 1, red, 2)
        cv2.putText(img, text, (xd, yd), work_font, 1, red, 2)

    cv2.imshow("Result", cv2.resize(thresh, (640, 480)))
    cv2.imshow("Source", cv2.resize(img, (640, 480)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fly.streamoff()
fly.land()
fly.end()
cv2.destroyAllWindows()
































