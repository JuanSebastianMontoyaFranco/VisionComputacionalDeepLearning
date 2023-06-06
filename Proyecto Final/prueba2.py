import cv2
import os
vid = cv2.VideoCapture("C:\\Users\\jsm21\\Desktop\\Proyecto VC\\video2.mp4")
if not os.path.exists('newdir'):
    os.makedirs('newdir')

cf = 0

while (True):
    succes, frame = vid.read()
    if succes:
        cv2.imshow("output", frame)
        cv2.imwrite("./newdir/frame" + str(cf) + '.jpg', frame)
        cf += 1
    else:
        break
vid.release()
