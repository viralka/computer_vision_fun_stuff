import cv2 as cv

img = cv.imread('Images\girl.jpg')

cv.imshow("girl", img)

cv.waitKey(0)