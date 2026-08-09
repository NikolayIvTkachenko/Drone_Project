import cv2
#from cv2 import CascadeClassifier
from djitellopy import Tello

def callback():
    pass

fly = Tello()

fc = cv2.CascadeClassifier('faces/haarcascade_frontalface_default.xml')

cv2.namedWindow("Frame")
cv2.createTrackbar("Neighbours", "Frame", 5, 20, callback)
cv2.createTrackbar("ScaleFactor", "Frame", 1, 10, callback)

fly.connect()
fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame
    frame = cv2.flip(work_frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    nb = cv2.getTrackbarPos("Neighbours", "Frame")
    sf = cv2.getTrackbarPos("ScaleFactor", "Frame")

    faces = fc.detectMultiScale(
        gray,
        scaleFactor=1 + sf / 10,
        minNeighbors=nb
    )

    print("Количество лиц: ", len(faces))
    print(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), -1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

fly.streamoff()
fly.end()
cv2.destroyAllWindows()

