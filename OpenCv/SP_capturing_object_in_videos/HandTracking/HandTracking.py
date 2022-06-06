import cv2 as cv
import mediapipe as mp 
import time 
import image_opener as io


url = r"https://192.168.29.61:8080/video"
cap = cv.VideoCapture(url)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while(True):
    camera, frame = cap.read()
    frame = io.resizeimg(frame, 1000)

    if frame is not None:
        imgRgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        result = hands.process(imgRgb)
        print(result.multi_hand_landmarks)
        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame,handlms, mpHands.HAND_CONNECTIONS)

        cv.imshow("Frame", frame)
    q = cv.waitKey(5)
    if q==ord("q"):
        break



cv.destroyAllWindows()
