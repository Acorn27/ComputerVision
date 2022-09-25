import cv2 as cv
import numpy as np

#read gray image
image = cv.imread("C:\\Users\\tmmh2\\Downloads\\rice.jpg", cv.IMREAD_GRAYSCALE)

#convert to binary
b_image = cv.threshold(image, 120, 255, cv.THRESH_BINARY)[1]

#show image
cv.imshow("Binary", b_image)


#get erode kernel
erode_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
dilate_kernel = cv.getStructuringElement(cv.MORPH_DILATE, (5,5))

#get output image
dilate_image = cv.dilate(b_image, dilate_kernel, iterations=1)

erode_image = cv.erode(dilate_image, erode_kernel, iterations=2)

cv.imshow("Dilate", dilate_image)
cv.imshow("Final Erode", erode_image)

cv.waitKey(0)
cv.destroyAllWindows()

