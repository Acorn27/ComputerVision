import numpy as np
import cv2 as cv

# read image ass gray
img = cv.imread("C:\\Users\\tmmh2\\Downloads\\Small_holes.jpg", cv.IMREAD_GRAYSCALE)

#convert to binary
b_img = cv.threshold(img,150,255,cv.THRESH_BINARY)[1]

cv.imshow('Binary image',b_img)

#create Kernel/element
kernel_sq = np.array([[1,1,1],
                      [1,1,1],
                      [1,1,1]],dtype=np.uint8)

# cv.getStructuringElement (shape, ksize, anchor = new cv.Point(-1, -1))
# shape is one the shpe of cv.MorphShape
# Size is the size of structuring element, anchor position, default to [-1,-1]
# [-1,-1] mean anchor is at the center
kernel = cv.getStructuringElement(cv.MORPH_CROSS,(7,7))
kernel2 = cv.getStructuringElement(cv.MORPH_CROSS,(7,7),(0,0))

# cv erode need two element, the original image and structuring element or kernel(decide the nature of the operation)
# erode has more input than this, who do not shown is left to default
out1 = cv.erode(b_img, kernel, iterations=1)    
out2 = cv.erode(b_img, kernel2, iterations=1)

cv.imshow('after morphology1',out1)
cv.imshow('after morphology2',out2)

cv.waitKey(0)
cv.destroyAllWindows()