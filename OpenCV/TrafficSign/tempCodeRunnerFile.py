import cv2 as cv
import numpy as np

#load image
img = cv.imread('trafficSign.jpg', cv.IMREAD_COLOR)
blur = cv.GaussianBlur(img, (5,5), 0)

#detect red color
hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

low_thres = (160,100,100)
high_thres = (180,255,255)

b_img = cv.inRange(hsv, low_thres, high_thres)
cv.imshow("binary image", b_img)