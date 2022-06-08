import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import image_opener as ip



def test(x):
    pass
# looping over all images 

found_valiable = {}
i = 0
while True:
    # making window
    cv.namedWindow("window")
    cv.resizeWindow("window", 700, 400)

    # creating trackbars

    cv.createTrackbar("Ksize", "window", 50, 400, test)
    cv.createTrackbar("sigma", "window", 1, 1000, test)
    cv.createTrackbar("theta", "window", 0, 180,test)
    cv.createTrackbar("lambda", "window", 5, 180, test)
    cv.createTrackbar("gamma", "window", 40, 100, test)
    cv.createTrackbar("phi", "window", 0, 100,test)

    while True:

        k = cv.waitKey(1) & 0xFF

        

        # filtering data

        ksize = cv.getTrackbarPos("Ksize", 'window')
        sigma = cv.getTrackbarPos("sigma", 'window')/10
        theta = cv.getTrackbarPos("theta", 'window')*(np.pi/180)
        lambd = cv.getTrackbarPos("lambda", 'window')*(np.pi/180)
        gamma = cv.getTrackbarPos("gamma", 'window')/100
        phi = cv.getTrackbarPos("phi", 'window')/100

        # print(type(gamma))

        kernel = cv.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma,phi,ktype= cv.CV_32F)

        # plt.imshow(kernel)
        cv.imshow("kernel",kernel)
        

        if k == 27:
            found_valiable[i] = (ksize, sigma, theta, lambd, gamma, phi)
            i += 1
            break


    

    cv.waitKey(2200)
    cv.destroyAllWindows()
    break

print(found_valiable)
