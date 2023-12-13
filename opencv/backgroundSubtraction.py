# Morphological operations based on OpenCV are as follows:
# Erosion - we use this methode below
# Dilation
# Opening
# Closing
# Morphological Gradient
# Top hat
# Black hat


image = cv2.imread("image2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

eroded = cv2.erode(gray.copy(), None, iterations=2)
cv2.imshow("Eroded 2 times", eroded)
cv2.waitKey(0)
