import cv2 as cv

# img = cv.imread('Images\\deer.jpg')

# cv.imshow("girl", img)

# cv.waitKey(0)

capture = cv.VideoCapture('Videos\Feeding a black dog.mp4')

istrue = True

while istrue:
    istrue , frame = capture.read()
    cv.imshow('lambs', frame)   

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)