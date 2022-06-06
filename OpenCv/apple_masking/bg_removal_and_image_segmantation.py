import cv2 as cv
import numpy as np
import image_opener as ip

# opening all the images from a folder
img_list = ip.allimg(r'apple_masking\apple_image')
img = img_list[7]
cv.imshow( 'im`',img)


# converitn all the images in hsv format and bluring a litte
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# hsv = cv.GaussianBlur(hsv_og,(11,11),0)
cv.imshow("img",img)

# defining color values

# Red
lower = np.array([15,0,0])
upper = np.array([116, 255, 255])

# createing a mask 
mask = cv.inRange(hsv, lower, upper)
mask = cv.bitwise_not(mask)
img = cv.bitwise_and(img , img, mask= mask)
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
lot_blur = cv.GaussianBlur(img1, (11,11),0)
# cv.imshow("mask", lot_blur)


cont, her = cv.findContours(lot_blur, cv.RECURS_FILTER, cv.CHAIN_APPROX_SIMPLE)


i = 0
for cont in cont:
    area = cv.contourArea(cont)
    if area > 1000:
        # cv.drawContours(img, cont, -1, (0, 255, 0), 1)
        x,y,h,w = cv.boundingRect(cont)
        cropped_img = img[y:y+w, x:x+h]
        # cv.imshow("apple_obj",cropped_img)
        name = "apple_obj" + str(i) + ".jpg"
        cv.imwrite(name, cropped_img)
        img = cv.rectangle(img, (x,y), (x+h, y+w), (0,255,0), 2)
        i += 1
    
    



img = cv.imshow("img",img)

cv.waitKey(00)