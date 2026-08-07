import cv2
from djitellopy import Tello

fly = Tello()
fly.connect()
fly.streamon()

while True:
    frame_read = fly.get_frame_read()
    work_frame = frame_read.frame

    gray = cv2.cvtColor(work_frame, cv2.COLOR_RGB2GRAY)

    cv2.imshow('Source', work_frame)
    cv2.imshow('GRAY', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fly.streamoff()
fly.end()
cv2.destroyAllWindows()


