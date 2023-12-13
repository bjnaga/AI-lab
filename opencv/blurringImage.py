# blurring image
import numpy as np
import cv2
import matplotlib.pyplot as plt 

#  normalized box filter
# cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT
# Again, you can change the kernel size 
# gausBlur = cv2.GaussianBlur(img, (5,5),0)  
# Again, you can change the kernel size 
# gausBlur = cv2.GaussianBlur(img, (5,5),0)  
# bilFilter = cv2.bilateralFilter(img,9,75,75) 

blurimage = cv2.blur(image, (50,50))  
cv2.imshow('blurred  image', blurimage)
cv2.waitKey()
