# program to capture from the webcam

import cv2

cam = cv2.VideoCapture(0)
result, image = cam.read() 

if result:
    cv2.imshow("captured picure",image)
    cv2.waitKey()
else:
    print("no image found")
