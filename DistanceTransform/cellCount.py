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
		sub_img.append(cropped)

current_image = 3
cv.imshow('original', sub_img[current_image])



cv.waitKey(0)
cv.destroyAllWindows()