# blurring image
import numpy as np
import cv2
import matplotlib.pyplot as plt 

blurimage = cv2.blur(image, (50,50))  
cv2.imshow('blurred  image', blurimage)
cv2.waitKey()
