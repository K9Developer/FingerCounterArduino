// Sets up the led pins for each finger
const int p1 = 8;
const int p2 = 7;
const int p3 = 4;
const int p4 = 12;
const int p5 = 2;
int incomingByte;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pins as an output:
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
  pinMode(p5, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

// Loops through the code below
void loop() {

  // Sets the builtin led to off if no data is sent
  digitalWrite(LED_BUILTIN, LOW);

  // Checks if data is available to read
  if (Serial.available() > 0) {
    
    // Sets the var incomingByte to the bytes that were sent to the Arduino
    incomingByte = Serial.read();

    // If 1 was sent by the pyhton program the p1 LED will turn on. if 2 was sent turn p1 LED off
    if (incomingByte == '1') {
      digitalWrite(p1, HIGH);
    } else if (incomingByte == '2') {
      digitalWrite(p1, LOW);
    }

    // If 3 was sent by the pyhton program the p2 LED will turn on. if 4 was sent turn p2 LED off
    if (incomingByte == '3') {
      digitalWrite(p2, HIGH);
    } else if (incomingByte == '4') {
      digitalWrite(p2, LOW);
    }

    // If 5 was sent by the pyhton program the p3 LED will turn on. if 6 was sent turn p3 LED off
    if (incomingByte == '5') {
      digitalWrite(p3, HIGH);
    } else if (incomingByte == '6') {
      digitalWrite(p3, LOW);
    }

    // If 7 was sent by the pyhton program the p4 LED will turn on. if 8 was sent turn p4 LED off
    if (incomingByte == '7') {
      digitalWrite(p4, HIGH);
    } else if (incomingByte == '8') {
      digitalWrite(p4, LOW);
    }

    // If 9 was sent by the pyhton program the p5 LED will turn on. if 0 was sent turn p5 LED off
    if (incomingByte == '9') {
      digitalWrite(p5, HIGH);
    } else if (incomingByte == '0') {
      digitalWrite(p5, LOW);
    }
    
  }
}
