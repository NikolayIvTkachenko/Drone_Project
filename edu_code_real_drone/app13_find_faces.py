import cv2
#from cv2 import CascadeClassifier

face_cascade = cv2.CascadeClassifier('faces/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
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

cap.release()
cv2.destroyAllWindows()

