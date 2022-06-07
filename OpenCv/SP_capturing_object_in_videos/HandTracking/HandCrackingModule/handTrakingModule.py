import cv2 as cv
import mediapipe as mp 
import time 
# import image_opener as io


class handDetector():
    def __init__(self, mode= False, maxHands = 2, modelComplexity=1, detectionCon = 0.5, tracksCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.tracksCon = tracksCon
        self.modelComplexity = modelComplexity

        # using inbuild methord
        self.mpHands = mp.solutions.hands
        # self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.tracksCon)
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.tracksCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,frame, draw=True):
        if frame is not None:
            imgRgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            self.result = self.hands.process(imgRgb)
            # print(result.multi_hand_landmarks)
            if self.result.multi_hand_landmarks:
                for handlms in self.result.multi_hand_landmarks:
                    if draw== True:
                        for id, lm in enumerate(handlms.landmark):

                            # print(id,lm)
                            h, w,c = frame.shape
                            cx , cy = int(lm.x*w), int(lm.y*h)
                            print(id,cx,cy)

                            if id == 4: # each id is equal some specific point in the hand
                                cv.circle(frame, (cx,cy),25,(255,0,255), cv.FILLED)
                    else: 
                        pass

                    self.mpDraw.draw_landmarks(frame,handlms, self.mpHands.HAND_CONNECTIONS)

                    return frame

    def findPosition(self,frame, handNo=0, draw = True):
        lmlist = []

        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo] 

        
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w,c = frame.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                # print(id,cx,cy)
                lmlist.append([id,cx,cy])
                if draw:
                # if id == 4: # each id is equal some specific point in the hand
                    cv.circle(frame, (cx,cy),25,(255,0,255), cv.FILLED)
            
        return lmlist


# cv.destroyAllWindows()

def video_capture(url, size = 1000):
    # load the video from the phone 
    cap = cv.VideoCapture(url)
    # frame = io.resizeiAmg(frame, 1000)
    return cap


def main():
    pTime = 0
    cTime = 0
    cap = video_capture(r"https://192.168.29.61:8080/video")
    detector = handDetector()


    while True:
        camera, frame = cap.read()
        img = detector.findHands(frame)

        lmList = detector.findPosition(img)

        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps  = 1/(cTime-pTime)
        pTime = cTime 

        cv.putText(frame, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        cv.imshow("Frame", frame)
        q = cv.waitKey(1) 

    

if __name__ == "__main__":
    main()


