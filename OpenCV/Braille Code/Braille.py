import cv2 as cv

image = cv.imread("braille2.webp", cv.IMREAD_GRAYSCALE)

blur = cv.GaussianBlur(image,(3,3),0)

#work for brilliant spot
b_image1 = cv.threshold(blur,190,255,cv.THRESH_BINARY)[1]
b_image2 = cv.threshold(blur,150,255,cv.THRESH_BINARY_INV)[1]

#final_image = cv.add(image, b_image1)
final_image = cv.subtract(image, b_image2)
final_image = cv.add(final_image, b_image1)

cv.imshow("final", final_image)

cv.waitKey(0)
cv.destroyAllWindows()