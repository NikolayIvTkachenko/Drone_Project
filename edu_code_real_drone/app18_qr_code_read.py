import cv2
import numpy as np
from pyzbar.pyzbar import decode

work_font = cv2.FONT_HERSHEY_SIMPLEX
work_color = (255, 0, 255)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    for barcode in decode(frame):
        work_data = barcode.data.decode('utf-8')
        print(work_data)

        points = np.array([barcode.polygon], np.int32)
        cv2.polylines(frame, [points], True, work_color, 5)
        rect = barcode.rect
        print(rect)
        cv2.putText(frame, work_data, (rect[0], rect[1]), work_font, 0.9, work_color, 2)

    cv2.imshow("Result", frame)
    key = cv2.waitKey(5)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

