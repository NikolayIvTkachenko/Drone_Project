import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    succes, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow('BGR', frame)
    cv2.imshow('RGB', rgb)
    cv2.imshow('BLUE', frame[:, :, 0])
    cv2.imshow('BLUE', frame[:, :, 1])
    cv2.imshow('BLUE', frame[:, :, 2])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

