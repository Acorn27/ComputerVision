import cv2 as cv
import numpy as np

# read gray image
image = cv.imread("C:\\Users\\tmmh2\\Downloads\\rice.jpg", cv.IMREAD_GRAYSCALE)

#convert to binary
#thresh, b_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
#thresh, b_image = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# we can not find the suitable thresh for the entire image, even with otsu method
# link to otsu: https://www.youtube.com/watch?v=jUUkMaNuHP8&t=189s

# apaptive threshold finding
b_image = cv.adaptiveThreshold (image, 255.0, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 51, -20.0)
cv.imshow("Binary", b_image)

# erode
erode_image = cv.erode(b_image, cv.getStructuringElement(cv.MORPH_ERODE, (4,4)), iterations=1)
cv.imshow("Erode", erode_image)
contours,_= cv.findContours(erode_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.drawContours(image, contours, -1, (0, 0, 255), 2)

count = 1
for contour in contours:
    x,y,w,h = cv.boundingRect(contour)
    cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    text = '#' + str(count)
    count += 1
    cv.putText(image, text, (x,y), cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)


cv.imshow("Pass", image)
cv.waitKey(0)
cv.destroyAllWindows()


