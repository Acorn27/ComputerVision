
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


img = cv.imread("D:\\Download\\Car_license.jpg", cv.IMREAD_GRAYSCALE)
#cv.imshow('Original', img)


b_img = cv.threshold(img,150,255,cv.THRESH_BINARY_INV)[1]
cv.imshow("Binary", b_img)


contours,_= cv.findContours(b_img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

count = 1
for contour in contours:
    area = cv.contourArea(contour)
    if (area > 25000 and area < 60000):

        x,y,w,h = cv.boundingRect(contour)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text = '#' + str(count)
        count += 1
        cv.putText(img, text, (x,y), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)


cv.imshow("Pass", img)
cv.waitKey(0)
cv.destroyAllWindows()
