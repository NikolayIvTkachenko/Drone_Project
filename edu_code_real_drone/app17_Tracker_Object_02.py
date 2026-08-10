import cv2
import time
from djitellopy import Tello

work_font = cv2.FONT_HERSHEY_SIMPLEX
work_color = (0, 255, 0)
red = (255, 0, 0)

fly = Tello()
fly.connect()
fly.streamon()
fly.takeoff()
time.sleep(8)
fly.move_up(90)
time.sleep(3)
def draw_box(img, in_bbox):
    x, y, w, h = int(in_bbox[0]), int(in_bbox[1]), int(in_bbox[2]), int(in_bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), work_color, 3, 3)
    cv2.putText(img, "Tracking", (100, 75), work_font, 0.7, work_color, 2)

# cap = cv2.VideoCapture(0)
# success, frame = cap.read()

frame_read = fly.get_frame_read()
frame = frame_read.frame

tracker = cv2.TrackerMOSSE_create()
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create()
# tracker = cv2.TrackerMedianFlow_create()
# tracker = cv2.TrackerCSRT_create()

bbox = cv2.selectROI("Tracking", frame, False)
print(bbox)
tracker.init(frame, bbox)

while True:
    timer = cv2.getTickCount()
    frame_read = fly.get_frame_read()
    frame = frame_read.frame

    success, bbox = tracker.update(frame)
    print(bbox)

    if success:
        draw_box(frame, bbox)
    else:
        cv2.putText(frame, "Lost", (100, 75), work_font, 0.7, red, 2)
    cv2.rectangle(frame, (15, 15), (200, 90), work_color, 2)
    cv2.putText(frame, "Fps: ", (20, 40), work_font, 0.7, work_color, 2)
    cv2.putText(frame, "Status:", (20, 75), work_font, 0.7, work_color, 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    cv2.putText(frame, str(int(fps)), (75, 40), work_font, 0.7, work_color, 2)
    cv2.imshow("Tracking", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if int(timer/1000) & 2 == 0:
        print(fly.get_flight_time())
print(fly.get_battery())
fly.land()
fly.streamoff()
fly.end()

cv2.destroyAllWindows()


































