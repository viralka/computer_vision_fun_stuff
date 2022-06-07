import cv2 as cv
import time 
import numpy as np
import handTrakingModule as htm

url = r"https://100.109.200.153:8080/video"
cap = cv.VideoCapture(url)
ptime= 0


detector = htm.handDetector()

while(True):
    camera, frame = cap.read()
    frame = cv.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv.INTER_CUBIC)

    # for frame rate
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime


    if frame is not None:

        frame = detector.findHands(frame)

        # writing frame on the screen
        frame = cv.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv.INTER_CUBIC)
        cv.putText(frame, "FPS: " + str(int(fps)), (10,50), cv.FONT_HERSHEY_COMPLEX,1,(255,0,255),3)
        cv.imshow("Frame", frame)


    q = cv.waitKey(1)
    if q==ord("q"):
        break
cv.destroyAllWindows()