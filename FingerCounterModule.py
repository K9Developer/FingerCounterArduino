import HandTrackingModule as htm

class fingerCounter():
    def __init__(self):
        self.detector = htm.handDetector(maxHands=1)
        self.tipIds = [4, 8, 12, 16, 20]

    def getFingerCount(self, img, draw=True):
        lmList,img = self.detector.findPosition(img, draw=True if draw == True else False)

        fingers = []
        if len(lmList) != 0:
            fingers = []

            if lmList[self.tipIds[0]][1] < lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                try:
                    if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                except IndexError:
                    pass
        return (fingers,img)