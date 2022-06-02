import cv2 as cv

# img = cv.imread('Images\\deer.jpg')

# cv.imshow("girl", img)

# cv.waitKey(0)

capture = cv.VideoCapture('Videos\Lambs eating grass.mp4')

while True:
    istrue , frame = capture.read()
    cv.imshow('lambs', frame)   

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)