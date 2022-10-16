import numpy as np
import cv2 as cv
img  = cv.imread('2cell.jpg', cv.IMREAD_GRAYSCALE)
b_img = cv.threshold(img, 150,255,cv.THRESH_BINARY)[1]
cv.imshow('Raw image',b_img)

# diatance transform
dist_img = cv.distanceTransform(b_img, cv.DIST_L2, 3)
cv.normalize(dist_img, dist_img,0,1,cv.NORM_MINMAX) # convert to maxtrix from 0 to 1 -> %
cv.imshow('Distance image', dist_img)

print(dist_img.dtype)
print(np.max(dist_img)) # distance with the number of pixel

out = cv.threshold(dist_img, 0.8, 1, cv.THRESH_BINARY)[1]
cv.imshow('After thres',out)


cv.waitKey()
cv.destroyAllWindows()