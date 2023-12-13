# image greyscaling 

import numpy as np
import cv2
import matplotlib.pyplot as plt 

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Lion', gray_image)
cv2.waitKey()
