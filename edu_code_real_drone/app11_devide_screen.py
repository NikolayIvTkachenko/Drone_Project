import cv2
import numpy as np

def callback(argument):
    pass

work_font = cv2.FONT_HERSHEY_SIMPLEX
white = (255, 255, 255)
dx = 80
dy = 70

cap = cv2.VideoCapture(0)

cv2.namedWindow("Settings")

# Hue - тон
# Saturation - насыщенность
# Value - интенсивность
cv2.createTrackbar('H_min', 'Settings', 18, 255, callback)
cv2.createTrackbar('S_min', 'Settings', 56, 255, callback)
cv2.createTrackbar('V_min', 'Settings', 149, 255, callback)
cv2.createTrackbar('H_max', 'Settings', 44, 255, callback)
cv2.createTrackbar('S_max', 'Settings', 174, 255, callback)
cv2.createTrackbar('V_max', 'Settings', 255, 255, callback)

while True:
    succes, work_farme = cap.read()
    img = cv2.flip(work_farme, 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos('H_min', 'Settings')
    s1 = cv2.getTrackbarPos('S_min', 'Settings')
    v1 = cv2.getTrackbarPos('V_min', 'Settings')
    h2 = cv2.getTrackbarPos('H_max', 'Settings')
    s2 = cv2.getTrackbarPos('S_max', 'Settings')
    v2 = cv2.getTrackbarPos('V_max', 'Settings')

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    thresh = cv2.inRange(hsv, h_min, h_max)
    moments = cv2.moments(thresh, 1)

    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 1000:
        xc = int(dM10 / dArea)
        yc = int(dM01 / dArea)

        cv2.circle(thresh, (xc, yc), 10, (0, 0, 255), -1)
        cv2.line(thresh, (320, 240), (xc, yc), white, 2)

        text = str(xc) + " " + str(yc)

        cv2.putText(thresh, "Find!", (50, 50), work_font, 1, white, 2)
        cv2.putText(thresh, "Find!", (xc + 50, yc - 50), work_font, 1, white, 2)

    cv2.line(thresh, (320 - dx, 0), (320 - dx, 480), white, 2)
    cv2.line(thresh, (320 + dx, 0), (320 + dx, 480), white, 2)
    cv2.line(thresh, (0, 240 - dy), (640, 240 - dy), white, 2)
    cv2.line(thresh, (0, 240 + dy), (640, 240 + dy), white, 2)

    cv2.imshow("Result", thresh)
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()








