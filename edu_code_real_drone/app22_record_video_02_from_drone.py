import cv2
import time
from djitellopy import Tello

fly = Tello()

size = (960, 720)
four_cc = cv2.VideoWriter_fourcc(*'XVID')
# four_cc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0

out = cv2.VideoWriter('videos/work_video.avi', four_cc, fps, size)

fly.connect()
fly.streamon()
fly.takeoff()

time.sleep(5)

while True:
    frame_read = fly.get_frame_read()
    frame = frame_read.frame

    cv2.imshow('Recording...', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
fly.land()
fly.streamoff()
fly.end()

cv2.destroyAllWindows()