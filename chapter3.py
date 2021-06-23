import cv2
import numpy as np

img = cv2.imread("Resources/Auto.png")
print(img.shape)

imgResize = cv2.resize(img,(400,180))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resized",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)
