import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import image_opener as io


def test(x):
    pass


# opened image 
# img_list = io.allimg(r'apple_masking\apple_image')
# img = img_list[8]
img = cv.imread(r"apple_masking\apple_image\ad2.jpg")
# img = cv.resize(image,(700,672))
# cv.imshow("img",img)

# making window 
cv.namedWindow("window")
cv.resizeWindow("window", 700, 700)



# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
prams = cv.SimpleBlobDetector_Params()


# creating trackbars
cv.createTrackbar("Thresh_min", "window", 0, 255, test)
cv.createTrackbar("Thresh_max", "window", 255, 255, test)

cv.createTrackbar("color", "window", 0, 1,test)

cv.createTrackbar("circular_min", "window", 0, 100, test)
cv.createTrackbar("circular_max", "window", 100, 100, test)

cv.createTrackbar("inertialRations_min", "window", 0, 100, test)
cv.createTrackbar("inertialRations_max", "window", 100, 100, test)

cv.createTrackbar("area_min", "window", 0, 100000, test)
cv.createTrackbar("area_max", "window", 1000, 100000, test)

cv.createTrackbar("distance", "window", 0, 100000, test)




while(1):
    # cv.imshow("slide bars",img)
    k = cv.waitKey(1) & 0xFF

    if k == 26:
        break

    # filtering data
    prams.minThreshold = cv.getTrackbarPos("Thresh_min", 'window')
    prams.maxThreshold = cv.getTrackbarPos("Thresh_max", 'window')

    #filter by color values
    prams.filterByColor = 1
    prams.blobColor = cv.getTrackbarPos("color", 'window')

    # filtering by circularity values
    prams.filterByCircularity = True
    prams.minCircularity = cv.getTrackbarPos("circular_min", 'window')/100
    prams.maxCircularity = cv.getTrackbarPos("circular_max", 'window')/100

    # filtering by inertialRations
    prams.filterByInertia = True
    prams.minInertiaRatio = cv.getTrackbarPos("inertialRations_min", 'window')/100
    prams.maxInertiaRatio = cv.getTrackbarPos("inertialRations_max", 'window')/100

    #filter by area values
    prams.filterByArea = True
    prams.minArea = cv.getTrackbarPos("area_min", 'window')
    prams.maxArea = cv.getTrackbarPos("area_max", 'window')

    # filter by distance between the blobls
    prams.minDistBetweenBlobs = cv.getTrackbarPos("distance", 'window')

    # set up the thing
    detector = cv.SimpleBlobDetector_create(prams)

    # Detect blobs
    Keypoints = detector.detect(img)

    print("Number of blobs found: ", len(Keypoints))


    # Draw blobs
    img_with_blobs = cv.drawKeypoints(img, Keypoints, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    plt.imshow(img_with_blobs)
    img_with_blobs = cv.resize(img_with_blobs,(700,672))
    cv.imshow("img_with_blobs", img_with_blobs)
    # cv.waitKey(10)


cv.destroyAllWindows()




