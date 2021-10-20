import cv2
import FingerCounterModule
import serial

# Sets up arduino and finger counter module
ser = serial.Serial('COM5', 9600)
cap = cv2.VideoCapture(0)
fingerM = FingerCounterModule.fingerCounter()

# Loops though every frame
while True:

    # Gets the finger array and reads the image
    success, img = cap.read()
    fingers, image = fingerM.getFingerCount(img=img)

    # Sends the arduino the signals
    if fingers == []:
        fingers = [0,0,0,0,0]

    # If thumb is open then send 1 to the arduino if not send 2 to the arduino
    if fingers[0] == 1:
        ser.write(b'1')
    else:
        ser.write(b'2')

    # If index finger is open then send 3 to the arduino if not send 4 to the arduino
    if fingers[1] == 1:

        ser.write(b'3')
    else:
        ser.write(b'4')

    # If middle finger is open then send 5 to the arduino if not send 6 to the arduino
    if fingers[2] == 1:
        ser.write(b'5')
    else:
        ser.write(b'6')

    # If ring finger is open then send 7 to the arduino if not send 8 to the arduino
    if fingers[3] == 1:
        ser.write(b'7')
    else:
        ser.write(b'8')

    # If little finger is open then send 9 to the arduino if not send 0 to the arduino
    if fingers[4] == 1:
        ser.write(b'9')
    else:
        ser.write(b'0')

    # Shows the image
    cv2.imshow("Image", image)
    cv2.waitKey(1)

