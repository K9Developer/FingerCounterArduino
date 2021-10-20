// Arduino IDE: 
// File -> Examples -> 04.Communication -> PhysicalPixel

const int p1 = 8;
const int p2 = 7;// pin the LED is attached to
const int p3 = 4;
const int p4 = 12;
const int p5 = 2;
int incomingByte;      // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
  pinMode(p5, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, LOW);
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    
    if (incomingByte == '1') {
      digitalWrite(p1, HIGH);
    } else if (incomingByte == '2') {
      digitalWrite(p1, LOW);
    }

    if (incomingByte == '3') {
      digitalWrite(p2, HIGH);
    } else if (incomingByte == '4') {
      digitalWrite(p2, LOW);
    }

    if (incomingByte == '5') {
      digitalWrite(p3, HIGH);
    } else if (incomingByte == '6') {
      digitalWrite(p3, LOW);
    }

    if (incomingByte == '7') {
      digitalWrite(p4, HIGH);
    } else if (incomingByte == '8') {
      digitalWrite(p4, LOW);
    }

    if (incomingByte == '9') {
      digitalWrite(p5, HIGH);
    } else if (incomingByte == '0') {
      digitalWrite(p5, LOW);
    }
    
  }
}
