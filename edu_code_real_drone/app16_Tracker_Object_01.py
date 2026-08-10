import cv2
work_font = cv2.FONT_HERSHEY_SIMPLEX
work_color = (0, 255, 0)
cap = cv2.VideoCapture(0)
ok1, frame = cap.read()

tracker = cv2.TrackerMOSSE_create() # Cannot find reference 'TrackerMOSSE_create' in '__init__.pyi'
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)

while True:
    timer = cv2.getTickCount()
    ok1, frame = cap.read()

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    cv2.putText(frame, str(int(fps)), (75, 40), work_font, 0.7, work_color, 2)
    cv2.imshow("Tracking", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break