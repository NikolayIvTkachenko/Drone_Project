import cv2
import time
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

work_font = cv2.FONT_HERSHEY_SIMPLEX

with open('QR_code/data.txt') as file:
    data_list = file.read().splitlines()

text = [ ]

f = open('QR_code/whoWas.txt', 'w')
welcome = ""

while True:
   for i in range(10):
       no_auth = True
       while no_auth:
           success, frame = cap.read()
           for barcode in decode(frame):
               work_data = barcode.data.decode('utf-8')
               print(work_data)

               if work_data in data_list:
                   output = 'Accessed!'
                   no_auth = False
                   work_color = (0, 255, 0)
                   welcome = work_data
                   print(welcome)
               else:
                   output = "Access denied!"
                   work_color = (0, 0, 255)

               points = np.array([barcode.polygon], np.int32)

               cv2.polylines(frame, [points], True, work_color, 5)

               rect = barcode.rect
               cv2.putText(frame, work_data, (rect[0], rect[1]), work_font, 0.9, work_color, 2)

           cv2.imshow("Result", frame)
           cv2.waitKey(1)
   if welcome in text:
       print("Человек уже есть")
   else:
       text.append(welcome)
       f.write(welcome + "\n")
       print("Welcome")

   key = cv2.waitKey(5)
   if key == 27:
       break

f.close()
print("Write")
cap.release()
cv2.destroyAllWindows()




