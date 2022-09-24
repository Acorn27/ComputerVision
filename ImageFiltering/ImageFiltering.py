from skimage import io, img_as_float
import numpy as np
import cv2

img = img_as_float(io.imread("C:\\Users\\tmmh2\\Downloads\\noise1.jpg", as_gray = True))


#5 by 5 array, use float to avoid round off error
#divide by 15 to find average
#there are various other filter bilt-in in openCV
kernel = np.ones((5,5), np.float32)/25

#gaussian kernel
gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                             [1/8, 1/4, 1/8],
                             [1/16, 1/8, 1/16]])
my_own_kernel = np.array([[1/9, 1/9, 1/9],
                          [1/9, 1/9, 1/9],
                          [1/9 ,1/9, 1/9]])

#depth of -1 mean source and output have the same depth
#in this case float64 and float64
conv_using_cv2 = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_CONSTANT)
#conv_using_cv2 = cv2.filter2D(img, -1, gaussian_kernel, borderType=cv2.BORDER_CONSTANT)
#conv_using_cv2 = cv2.filter2D(img, -1, my_own_kernel, borderType=cv2.BORDER_CONSTANT)

cv2.imshow("Original", img)
cv2.imshow("cv2 filter", conv_using_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()