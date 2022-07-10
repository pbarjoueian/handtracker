from math import floor

import alsaaudio
import cv2

from HandTackingModule import HandDetector

am = alsaaudio.Mixer()

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)


def main():
    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)  # With Draw

        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmarks points
            bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
            centerPoint1 = hand1["center"]  # center of the hand cx,cy
            handType1 = hand1["type"]  # Hand Type Left or Right

            fingers1 = detector.fingersUp(hand1)

            if len(hands) == 2:
                hand2 = hands[1]
                lmList2 = hand2["lmList"]  # List of 21 Landmarks points
                bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
                centerPoint2 = hand2["center"]  # center of the hand cx,cy
                handType2 = hand2["type"]  # Hand Type Left or Right

                fingers2 = detector.fingersUp(hand2)

                # with draw
                length, info, img = detector.findDistance(
                    centerPoint1, centerPoint2, img
                )

                # Mute system if detected a clap
                if 75 <= length <= 195:
                    am.setvolume(0)

            else:
                # Picking up the thumb and index finger from the land mark list
                thumb_tip, index_finger_tip = lmList1[4], lmList1[8]

                # Dropping the z index
                thumb_tip.pop(2)
                index_finger_tip.pop(2)

                # with draw
                length, info, img = detector.findDistance(
                    thumb_tip, index_finger_tip, img
                )

                # Set volume percentage by hand gestures
                volume_percentage = floor((length * 100) / 180)
                volume_percentage = (
                    volume_percentage if volume_percentage <= 100 else 100
                )
                volume_percentage = volume_percentage if volume_percentage > 5 else 5
                am.setvolume(volume_percentage)

        # with draw
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
