import cv2
import HandTrackingModule as htm
import time

cap = cv2.VideoCapture(0)
pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img = cv2.flip(img,1)
    lmList = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        cv2.line(img, (lmList[0][1],lmList[0][2]), (lmList[1][1],lmList[1][2]), (0,0,0),10)
        cv2.line(img, (lmList[1][1],lmList[1][2]), (lmList[2][1],lmList[2][2]), (0,0,255),10)
        cv2.line(img, (lmList[2][1],lmList[2][2]), (lmList[3][1],lmList[3][2]), (255,255,0),10)
        cv2.line(img, (lmList[3][1],lmList[3][2]), (lmList[4][1],lmList[4][2]), (0,0,0),10)

        cv2.line(img, (lmList[0][1],lmList[0][2]), (lmList[5][1],lmList[5][2]), (255,0,0),10)
        cv2.line(img, (lmList[5][1],lmList[5][2]), (lmList[6][1],lmList[6][2]), (0,0,255),10)
        cv2.line(img, (lmList[6][1],lmList[6][2]), (lmList[7][1],lmList[7][2]), (255,255,0),10)
        cv2.line(img, (lmList[7][1],lmList[7][2]), (lmList[8][1],lmList[8][2]), (0,0,0),10)
        cv2.line(img, (lmList[5][1],lmList[5][2]), (lmList[9][1],lmList[9][2]), (255,0,0),10)
        cv2.line(img, (lmList[9][1],lmList[9][2]), (lmList[10][1],lmList[10][2]), (0,0,255),10)
        cv2.line(img, (lmList[10][1],lmList[10][2]), (lmList[11][1],lmList[11][2]), (255,255,0),10)
        cv2.line(img, (lmList[11][1],lmList[11][2]), (lmList[12][1],lmList[12][2]), (0,0,0),10)

        cv2.line(img, (lmList[9][1],lmList[9][2]), (lmList[13][1],lmList[13][2]), (255,0,0),10)
        cv2.line(img, (lmList[13][1],lmList[13][2]), (lmList[14][1],lmList[14][2]), (0,0,255),10)
        cv2.line(img, (lmList[14][1],lmList[14][2]), (lmList[15][1],lmList[15][2]), (255,255,0),10)
        cv2.line(img, (lmList[15][1],lmList[15][2]), (lmList[16][1],lmList[16][2]), (0,0,0),10)
        cv2.line(img, (lmList[13][1],lmList[13][2]), (lmList[17][1],lmList[17][2]), (255,0,0),10)
        cv2.line(img, (lmList[17][1],lmList[17][2]), (lmList[18][1],lmList[18][2]), (0,0,255),10)
        cv2.line(img, (lmList[18][1],lmList[18][2]), (lmList[19][1],lmList[19][2]), (255,255,0),10)
        cv2.line(img, (lmList[19][1],lmList[19][2]), (lmList[20][1],lmList[20][2]), (0,0,0),10)
        cv2.line(img, (lmList[17][1],lmList[17][2]), (lmList[0][1],lmList[0][2]), (255,0,0),10)


        # cv2.line(img, (lmList[0][1],lmList[4][2]), (lmList[8][1],lmList[8][2]), (255,0,0),10)
        # cv2.line(img, (lmList[8][1],lmList[8][2]), (lmList[12][1],lmList[12][2]), (0,0,0),10)
        # cv2.line(img, (lmList[12][1],lmList[12][2]), (lmList[16][1],lmList[16][2]), (255,255,0),10)
        # cv2.line(img, (lmList[16][1],lmList[16][2]), (lmList[20][1],lmList[20][2]), (0,0,0),10)
        # cv2.line(img, (lmList[20][1],lmList[20][2]), (lmList[19][1],lmList[19][2]), (0,0,0),10)
        # cv2.line(img, (lmList[19][1],lmList[19][2]), (lmList[18][1],lmList[18][2]), (255,255,0),10)
        # cv2.line(img, (lmList[18][1],lmList[18][2]), (lmList[17][1],lmList[17][2]), (0,0,0),10)
        # cv2.line(img, (lmList[17][1],lmList[17][2]), (lmList[0][1],lmList[0][2]), (0,250,255),10)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()