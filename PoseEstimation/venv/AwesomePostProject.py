import cv2
import mediapipe as mp
import time
import PoseModule as pm


cap = cv2.VideoCapture('PoseVideos/2.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
            print(lmList[14])
            #Se da la información del punto #14
            #Para dibujar un círculo en el punto 14 en específico
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 10, (255,0,0), cv2.FILLED) 

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), 
                cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)