import cv2 as cv
import numpy as np
from scipy import signal

img = cv.imread('poly2.png', cv.IMREAD_COLOR)

canny = cv.Canny(img, 100, 200)

contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for c in contours:
   poly = cv.approxPolyDP(c,7,True)
   if poly.shape[0] == 4:
        cv.polylines(img, poly, True, (0,0,255), 3)


cv.imshow('Canny',img)
cv.waitKey(0)
cv.destroyAllWindows()