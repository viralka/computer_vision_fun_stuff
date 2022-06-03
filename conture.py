import cv2 as cv

image = cv.imread("Images\deer.jpg")
img = cv.resize(image,(450,672))
# cv.imshow("OG", img)


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

canny = cv.Canny(gray, 40, 80)
cv.imshow("canny", canny)

contour, hierarchy = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contour are python list of all the contours in the image
# hierarchy outher most is is high in haracy the inner is low in haracy 


cv.waitKey(2200)