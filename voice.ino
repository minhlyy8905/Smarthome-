#include <Servo.h>

const int analogInPin = A0;
int sensorValue = 0;               
int servoPin = 3;
Servo servo;
int relay1 = 8;
int relay2 = 9;
String voice;

void setup() {
  Serial.begin(9600);
  servo.attach(servoPin);
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  digitalWrite(relay1, LOW);
  digitalWrite(relay2, LOW);
}

void loop() {
  sensorValue = analogRead(analogInPin);           

if (sensorValue < 600) {
  for (int i = 180; i >= 0; i--) {
    servo.write(i);
    delay(30);
  }
}

  
  if (Serial.available() > 0) {
    voice = Serial.readString();
    voice.trim(); 
    voice.toLowerCase();  
    Serial.println(voice);  

    // Điều khiển relay thông qua lệnh bằng giọng nói
    if (voice == "mở đèn") {
      digitalWrite(relay1, HIGH);
    } 
    if (voice == "tắt đèn đi") {
      digitalWrite(relay1, LOW);
    }
    if (voice == "mở tivi") {
      digitalWrite(relay2, HIGH);
    } 
    if (voice == "tắt tivi") {
      digitalWrite(relay2, LOW);
    }
    if (voice == "xem phim") {
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, HIGH);
    }  
    if (voice == "đi ngủ") {
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, LOW);
    }  
    
    // Điều khiển servo
    if (voice == "servo 0 độ") {
      servo.write(0);
    }
    if (voice == "servo 90 độ") {
      servo.write(90);
    }
    if (voice == "servo 180 độ") {
      servo.write(180);
    }
  }
}
