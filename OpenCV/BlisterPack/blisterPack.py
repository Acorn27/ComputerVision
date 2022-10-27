import cv2 as cv
import numpy as np
from scipy import signal

img = cv.imread('blisterPack.jpg', cv.IMREAD_COLOR)
blur = cv.GaussianBlur(img, (5,5), 0)
canny = cv.Canny(img, 150, 250)

lines = cv.HoughLinesP(canny, 1, np.pi/180, 20, minLineLength= 30, maxLineGap= 10)

for line in lines:
   x1,y1,x2,y2 = line[0]
   cv.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

rows,cols=img.shape[:2]
alpha = np.arctan(np.abs(y2-y1)/np.abs(x2-x1))
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),alpha,1)
dst = cv.warpAffine(img,M,(cols,rows))

 
cv.imshow('Result',dst)
cv.waitKey(0)
cv.destroyAllWindows()