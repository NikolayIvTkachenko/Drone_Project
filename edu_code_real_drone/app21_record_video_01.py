import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30.0
size = (width, height)

four_cc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/test_video.avi', four_cc, fps, size)

while True:
    success, frame = cap.read()
    cv2.imshow("Recording...", frame)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

