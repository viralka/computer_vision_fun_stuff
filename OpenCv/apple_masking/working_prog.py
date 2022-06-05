import cv2 as cv
import numpy as np
import image_opener as ip

# opening all the images from a folder
img_list = ip.allimg(r'apple_masking\apple_image')
img = img_list[5]
# cv.imshow( 'im`',img)

# converitn all the images in hsv format and bluring a litte
hsv_og = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hsv = cv.GaussianBlur(hsv_og,(5,5),0)

# defining color values

# Red
lower_r = np.array([0, 100, 20])
upper_r = np.array([10, 255, 255])

# createing a mask 
mask = cv.inRange(hsv, lower_r, upper_r)
# cv.imshow("mask", mask)

# finding the conture 
contours, hierarchy = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow("img",img)

# now finding area in the contours
area = cv.contourArea(contours[0])
print(area)

cv.waitKey(2200)