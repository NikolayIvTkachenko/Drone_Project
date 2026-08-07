import cv2
import numpy as np

work_font = cv2.FONT_HERSHEY_SIMPLEX

white = (255, 255, 255)
red = (0, 0, 255)

cap = cv2.VideoCapture(0)

hsv_min = np.array((18, 56, 149), np.uint8)
hsv_max = np.array((44, 174, 255), np.uint8)

while True:
    success, work_frame = cap.read()
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

        cv2.putText(img, "Find!", (50, 50), work_font, 1, red, 2)
        cv2.putText(thresh, "Find!", (50, 50), work_font, 1, white, 2)
        cv2.putText(img, text, (x + 50, y - 50), work_font, 1, red, 2)
        cv2.putText(thresh, text, (x + 50, y - 50), work_font, 1, white, 2)

    cv2.imshow("Result", cv2.resize(thresh, (640, 480)))
    cv2.imshow("Source", cv2.resize(img, (640, 480)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






