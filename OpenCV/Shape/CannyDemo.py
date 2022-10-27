import cv2 as cv
import numpy as np
from scipy import signal

img = cv.imread('noise1.jpg', cv.IMREAD_GRAYSCALE)
blur = cv.GaussianBlur(img, (9,9), 0)
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])
out = signal.convolve2d(blur, kernel, mode = 'same')
out = out.astype(np.uint8) #convert to uint8
canny = cv.Canny(out, 150, 250)

cv.imshow('Canny',canny)
cv.waitKey(0)
cv.destroyAllWindows()