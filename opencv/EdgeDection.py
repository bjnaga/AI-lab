# Edge Detection using sobel algorithm
import numpy as np
import cv2
import matplotlib.pyplot as plt 

img_blur = cv2.GaussianBlur(image,(3,3), sigmaX=0, sigmaY=0) 
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis

sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey()
