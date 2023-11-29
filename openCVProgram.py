# Using OpenCV python library capture an image and perform the following image processing
# operations:
# a) Image Resizing
# b) Blurring of Image
# c) Grayscaling of image
# d) Scaling and rotation
# e) Edge Detection
# f) Segmentation using thresholding
# g) Background subtraction
# h) Morphological operation

import cv2


image = cv2.imread("image.jpg")
new = cv2.resize(image, (780, 540))

# cv2.resize(image, (780, 540), interpolation = cv2.INTER_LINEAR)
# cv2.INTER_AREA: This is used when we need to shrink an image.
# cv2.INTER_CUBIC: This is slow but more efficient.
# cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.
			
cv2.imshow('old image', image)
cv2.waitKey()
cv2.imshow('new resized image',new )
cv2.waitKey()
cv2.imwrite("newimage.jpg", new)
