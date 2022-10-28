from gettext import bind_textdomain_codeset
import cv2 as cv
import numpy as np

#load image
img = cv.imread('trafficSign.jpg', cv.IMREAD_COLOR)
blur = cv.GaussianBlur(img, (5,5), 0)

#detect red color
hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# max hsv in openCV is(0-180,0,255,0-255)
# min-max hsv in matlab is (0-1)
low_thres = (160,100,100)
high_thres = (180,255,255)

b_img = cv.inRange(hsv, low_thres, high_thres)
cv.imshow("binary image", b_img)
contours, hierarchy = cv.findContours(b_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
n = 1
for c in contours:
    x,y,w,h = cv.boundingRect(c)
    roi = img[y:y+h, x:x+w]
    canny = cv.Canny(roi, 150, 150)
    text = 'roi' + str(n)
    cv.imshow(text,canny)
    n += 1

cv.waitKey(0)
cv.destroyAllWindows()


