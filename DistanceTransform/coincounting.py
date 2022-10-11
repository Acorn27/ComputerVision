import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:\\Download\\coin.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# filter
gray = cv.GaussianBlur(gray, (3,3), 0)
# threshold to obtain binary image
b_img = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

dist_img = cv.distanceTransform(b_img, cv.DIST_L2, 3)
cv.normalize(dist_img,dist_img,0,1, cv.NORM_MINMAX)
seed = cv.threshold(dist_img, 0.7, 255,cv.THRESH_BINARY )[1]

contours, hierachy = cv.findContours(seed.astype(np.uint8),cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print('so objects = ', len(contours))
for index,cnt in enumerate(contours):
    (x,y), radius = cv.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)  
    text = '#' + str(index+1)
    cv.putText(img, text,center, cv.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)

cv.imshow('image', img)
cv.imshow('output', seed)
cv.waitKey(0)
cv.destroyAllWindows()