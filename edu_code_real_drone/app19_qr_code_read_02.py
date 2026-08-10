# В файле data.txt записать строки дуоступа, которые должен содержать содержимое в QR коде

import cv2
import numpy as np
import time
from djitellopy import Tello
from pyzbar.pyzbar import decode

fly = Tello()

work_font = cv2.FONT_HERSHEY_SIMPLEX

with open('QR_code/data.txt') as file:
    data_list = file.read().splitlines()

fly.connect()
time.sleep(1)

fly.streamon()
time.sleep(4)

# fly.takeoff()
# time.sleep(8)
# fly.move_up(80)
# time.sleep(2)

for i in range(20):
    no_auth = True
    while no_auth:
        frame_read = fly.get_frame_read()
        frame = frame_read.frame

        for barcode in decode(frame):
            # print(barcode.data)
            # print(barcode.type)
            work_date = barcode.data.decode('utf-8')
            print(work_date)

            if work_date in data_list:
                output = 'Accessed!'
                no_auth = False
                work_color = (0, 255, 0)
            else:
                output = 'Access denied!'
                work_color = (0, 0, 255)

            points = np.array([barcode.polygon], np.int32)
            print(points)

            cv2.polylines(frame, [points], True, work_color, 5)
            rect = barcode.rect

            print(rect)

            cv2.putText(frame, work_date, (rect[0], rect[1]), work_font, 0.9, work_color, 2)

    cv2.imshow("Result", frame)
    key = cv2.waitKey(5)
    if key == 27:
        break
print(fly.get_battery())
print(fly.get_flight_time())
# fly.land()
fly.land()
fly.streamoff()
fly.end()
cv2.destroyAllWindows()