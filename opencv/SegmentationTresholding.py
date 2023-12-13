# Segmentation using thresholding
import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE); 
 
# Basic threhold example 

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY); 
cv2.imshow('grey scale image', dst)
cv2.waitKey()
