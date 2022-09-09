import cv2
import mediapipe as mp
import time

class FaceMeshDetector():

    def __init__(self,
             staticMode = False,
             maxFaces = 2,
             minDetectionCon = 0.5,
             minTrackCon = 0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 2)
    
    def findFaceMesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(imgRGB)
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS,
                                    self.drawSpec, self.drawSpec)
                # for id, lm in enumerate(faceLms.landmark):
                #     # print(lm)
                #     ih, iw, ic = img.shape
                #     x, y = int(lm.x * iw), int(lm.y * ih)
                #     print(id, x, y)                
        return img

    

def main():
    cap = cv2.VideoCapture('Videos/1.mp4')
    #cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceMeshDetector()
    while True:
        succes, img = cap.read()
        img = detector.findFaceMesh(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS:{int(fps)}', (20, 80), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 255), 5)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
