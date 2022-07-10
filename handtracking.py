import time
import cv2

from HandTackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right

        # print(len(lmList1),lmList1)
        # print(bbox1)
        # print(centerPoint1)
        
        fingers1 = detector.fingersUp(hand1)
        
        # length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        # length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right

            fingers2 = detector.fingersUp(hand2)

            # print(fingers1, fingers2)
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)

            # with draw
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)

            if 75 <= length <= 195:
                length=300
                print("Mute")
        else:
            # Picking up the thumb and index finger from the land mark list
            thumb_tip, index_finger_tip = lmList1[4], lmList1[8]

            # Dropping the z index
            thumb_tip.pop(2)
            index_finger_tip.pop(2)

            # with draw
            length, info, img = detector.findDistance(thumb_tip, index_finger_tip, img)
            if length <= 7:
                print(length)
                print("Voume down")

    # with draw
    cv2.imshow("Image", img)
    cv2.waitKey(1)
