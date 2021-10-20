import HandTrackingModule as htm

class fingerCounter():
    def __init__(self):
        # Calls the HandTrackingModule and sets the tipIds to the tips of the fingers' ids
        self.detector = htm.handDetector(maxHands=1)
        self.tipIds = [4, 8, 12, 16, 20]

    def getFingerCount(self, img, draw=True):

        # Get the finger positions and the img
        lmList,img = self.detector.findPosition(img, draw=True if draw == True else False)

        fingers = []
        if len(lmList) != 0:
            fingers = []

            # Thumb
            # If the x of tip of the finger (thumb) is smaller than the lowest bone of the thumb
            if lmList[self.tipIds[0]][1] < lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                try:
                    # If the y of tip of the finger is smaller than the lowest bone of the finger
                    if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                except IndexError:
                    pass

        # Return the finger array and the image array
        return (fingers,img)