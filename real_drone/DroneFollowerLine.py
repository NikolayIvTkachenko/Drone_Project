import cv2

cap = cv2.VideoCapture(0)

def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    


while True:
    _, img = cap.read()
    img = cv2.resize(img, (480, 360))

    thresholding(img)

    cv2.imshow("Output", img)
    cv2.waitKey(1)