from struct import pack

import cv2
import FingerCounterModule
import HandTrackingModule as htm
import serial
ser = serial.Serial('COM5', 9600)
cap = cv2.VideoCapture(0)
fingerM = FingerCounterModule.fingerCounter()
while True:
    success, img = cap.read()
    fingers, image = fingerM.getFingerCount(img=img)
    if fingers == []:
        fingers = [0,0,0,0,0]
    if fingers[0] == 1:
        ser.write(b'1')
    else:
        ser.write(b'2')

    if fingers[1] == 1:

        ser.write(b'3')
    else:
        ser.write(b'4')

    if fingers[2] == 1:
        ser.write(b'5')
    else:
        ser.write(b'6')

    if fingers[3] == 1:
        ser.write(b'7')
    else:
        ser.write(b'8')

    if fingers[4] == 1:
        ser.write(b'9')
    else:
        ser.write(b'0')
    cv2.imshow("Image", image)
    cv2.waitKey(1)
ser.close()
exit(0)

