#image scaling and roatation
import numpy as np
import cv2
import matplotlib.pyplot as plt 

h, w = image.shape[:2]
center = (w / 2, h / 2)

# mat = cv2.getRotationMatrix2D((h,w), 90, 1)
mat = cv2.getRotationMatrix2D(center, 90, 1)

rotating = cv2.warpAffine(image, mat, (h, w))

cv2.imshow('rotated', rotating)
# cv2.imshow('rotated', mat)

cv2.waitKey()
