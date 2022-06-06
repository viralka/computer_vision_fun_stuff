import cv2 as cv
import numpy as np
import image_opener as io

# opened image 
img_list = io.allimg(r'apple_masking\apple_image')
img = img_list[8]
cv.imshow("img",img)

# blur = cv.GaussianBlur(img,(5,5),0)
# cv.imshow("blur",blur)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

contours , heracy = cv.findContours(gray,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contours = sorted(contours, key = cv.contourArea, reverse = True)[:5]

img = cv.drawContours(img, contours[0], -1, (0,255,0), 1)
cv.imshow("contour",img)

# making  the mask
mask = np.zeros(img.shape[:2], dtype = 'uint8')
count = [contours[0]]
cv.drawContours(mask,count, -1, (255,255,255), -1)
cv.imshow("mask",mask)

# imposing the mask on the image
apple = cv.bitwise_and(img, img, mask = mask)
cv.imshow("apple",apple)


cv.waitKey(00)
