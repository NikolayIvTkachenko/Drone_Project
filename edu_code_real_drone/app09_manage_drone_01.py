import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
direction = 0

while True:
    cv2.imshow("Test Window", img)
    ch = cv2.waitKey(5)

    if ch == 119:
        direction = 1
    if ch == 97:
        direction = 2
    if ch == 100:
        direction = 3
    if ch == 115:
        direction = 4
    if ch == 27:
        direction = -1
    if ch == 0:
        direction = 0


    if direction == 1:
        print(direction)
    elif direction == 2:
        print(direction)
    elif direction == 3:
        print(direction)
    elif direction == 4:
        print(direction)
    if direction == -1:
        break

cv2.destroyAllWindows()
