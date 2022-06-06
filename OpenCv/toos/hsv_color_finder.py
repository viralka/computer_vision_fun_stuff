import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(0)
# img = cv2.imread('IMG_20201224_12304.jpg')


#img = cv2.imread('wheat-upper1.png')
img = cv2.imread(r"C:\Users\mridu\Desktop\agnext\Agnext\OpenCv\apple_masking\apple_image\apple111.jpg")

new_rows = int(img.shape[0]/2)
new_cols = int(img.shape[1]/2)
img = cv2.resize(img, (new_cols,new_rows), fx=0.5, fy=0.5)

cv2.namedWindow('Colorbars')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','Colorbars',ilowH,179,callback)
cv2.createTrackbar('highH','Colorbars',ihighH,179,callback)

cv2.createTrackbar('lowS','Colorbars',ilowS,255,callback)
cv2.createTrackbar('highS','Colorbars',ihighS,255,callback)

cv2.createTrackbar('lowV','Colorbars',ilowV,255,callback)
cv2.createTrackbar('highV','Colorbars',ihighV,255,callback)



img2 = np.copy(img)
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
while(1):
    # ret, frame = cap.read()
    ilowH = cv2.getTrackbarPos("lowH", "Colorbars")
    ihighH = cv2.getTrackbarPos("highH", "Colorbars")
    ilowS = cv2.getTrackbarPos("lowS", "Colorbars")
    ihighS = cv2.getTrackbarPos("highS", "Colorbars")
    ilowV = cv2.getTrackbarPos("lowV", "Colorbars")
    ihighV = cv2.getTrackbarPos("highV", "Colorbars")

    
    
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    cv2.imshow('mask', mask)

    img2 = np.copy(img)
    img2[mask == 0] = 0

    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#    hsv2[:,:,2] = gray

    

    cv2.imshow('frame', img2)
#    cv2.imshow('hsv', hsv2)

#    cv2.imshow('gray', gray)
    # print(ilowH, ihighH,  ilowS, ihighS,  ilowV, ihighV )

    
    if(cv2.waitKey(1) & 0xFF == 27):# ord('q')):
        break


cv2.destroyAllWindows()



