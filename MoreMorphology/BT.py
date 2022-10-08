from array import array
import numpy as np
import cv2 as cv

img = cv.imread('anchor.png', cv.IMREAD_GRAYSCALE)
b_img = cv.threshold(img,150,255,cv.THRESH_BINARY)[1]
cv.imshow('Binary image',b_img)

width = img.shape[1]
heigh = img.shape[0]
print(width)
print(heigh)

#cut image for letter a)
mean_x = np.mean(b_img, axis = 0)
print(type(mean_x))
mean_y = np.mean(b_img, axis = 1)

x_left = np.min(np.where(mean_x>0))
x_right = np.max(np.where(mean_x>0))
x1 = np.min(np.where((mean_x>0) & (mean_x<125)))
x2 = np.max(np.where((mean_x>0) & (mean_x<125)))
print(x_left,x_right,x1,x2)

y_bot = np.min(np.where(mean_y>0)) 
y1 = np.min(np.where(mean_y>150))
y2 = np.max(np.where(mean_y>0))
print(y_bot,y1,y2)

#create a black image
black = np.zeros((heigh,width),dtype=np.uint8) 
black[y1:y2,x_left:x1] = 255
black[y1:y2,x2:x_right] = 255

#cut image for letter b)
black1 = np.zeros((heigh,width),dtype=np.uint8) 
black1[y_bot:y2,x_left:x1] = 255
black1[y_bot:y2,x2:x_right] = 255

#create Kernel/element
kernela = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
kernelb = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
kernelc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(31,31),(-1,-1))

#close morphology
out1 = cv.dilate(b_img, kernelc, iterations=1)
out2 = cv.morphologyEx(out1,cv.MORPH_CLOSE, kernelc, iterations=1)
cv.imshow('Letter c)',out2)

out3 = cv.erode(black, kernela, iterations=10)
cv.imshow('Letter a)',out3)

out4 = cv.erode(black1, kernelb, iterations=35)
out5 = cv.dilate(out4, kernelc, iterations=1)
out6 = cv.morphologyEx(out5,cv.MORPH_CLOSE, kernelc, iterations=1)
cv.imshow('Letter b)',out6)

cv.waitKey(0)
cv.destroyAllWindows()