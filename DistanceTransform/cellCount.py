from ast import Sub
from email.mime import image
from msilib.schema import Binary
import cv2 as cv
import numpy as np

kernel = np.ones((2,2),np.uint8)


img = cv.imread("D:\\Download\\cell2.png", cv.IMREAD_GRAYSCALE)
#cv.imshow("Original", img)

deteced_edge = cv.Canny(img, 50, 250)
#cv.imshow("edge", deteced_edge)


cnts,_= cv.findContours(deteced_edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
sub_img = list()
#idx = 0
for c in cnts:
	x,y,w,h = cv.boundingRect(c)
	if w>150 and h>150:
		cropped = img[y:y+h, x:x+w]
		#cv.imshow('cropped', cropped)
		#cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		sub_img.append(cropped)
		#idx = idx + 1
		#print(idx)

current_image = 5
cv.imshow('original', sub_img[current_image])

#b_img = cv.threshold(sub_img[current_image], 200,255,cv.THRESH_BINARY)[1]
b_img = b_img = cv.threshold( sub_img[current_image],0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
cv.imshow('Raw image',b_img)

# diatance transform
dist_img = cv.distanceTransform(b_img, cv.DIST_L1, 3)
cv.normalize(dist_img, dist_img,0,1,cv.NORM_MINMAX) # convert to maxtrix from 0 to 1 -> %
cv.imshow('Distance image', dist_img)

print(dist_img.dtype)
print(np.max(dist_img)) # distance with the number of pixel

out = cv.threshold(dist_img, 0.3, 1, cv.THRESH_BINARY)[1]


cv.imshow('After thres',out)

cv.waitKey(0)
cv.destroyAllWindows()