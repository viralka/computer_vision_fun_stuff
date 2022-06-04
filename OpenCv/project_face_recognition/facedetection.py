import cv2 as cv
import image_resized as ir


img_list =ir.allimg(r"C:\Users\mridu\Desktop\agnext\Agnext\OpenCv\Images")


for img in img_list:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('gray',gray)

    haar_cascade = cv.CascadeClassifier('project_face_recognition\haar_face.xml')

    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    print(f"Number of faces detected: {len(face_rect)}")

    for (x,y,w,h) in face_rect:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    cv.imshow("dected faces", img)
    cv.waitKey(2200)


