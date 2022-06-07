import cv2 as cv
import time 
import numpy as np 
import handTrakingModule as htm



# dimensions of cam
wCam, hCam = 1280, 720


url = r"https://192.168.117.63:8080/video"
cap = cv.VideoCapture(url)
cap.set(3, wCam)
cap.set(4, hCam)
pTime= 0

detector = htm.handDetector()


while(True):
    camera, frame = cap.read() # success , img 
    frame = detector.findHands(frame)
    
    
    
    # for frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    if frame is not None:
        # frame = resizeimg(frame, 1000)
        frame = cv.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv.INTER_CUBIC)
        cv.putText(frame, "FPS: " + str(int(fps)), (10,50), cv.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
        cv.imshow("Frame", frame)
    q = cv.waitKey(1)
    if q==ord("q"):
        break
cv.destroyAllWindows()