# Image Resizing 
import numpy as np
import cv2
import matplotlib.pyplot as plt 

image = cv2.imread("image.jpg")
new = cv2.resize(image, (780, 540))
img2 = image
# cv2.resize(image, (780, 540), interpolation = cv2.INTER_LINEAR)
# cv2.INTER_AREA: This is used when we need to shrink an image.
# cv2.INTER_CUBIC: This is slow but more efficient.
# cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.
			
cv2.imshow('old image', image)
cv2.waitKey()
cv2.imshow('new resized image',new )
cv2.waitKey()
# writing the content of new resize image to file 
cv2.imwrite("newimage.jpg", new)
