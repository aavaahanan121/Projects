#include <Arduino.h>

const int Trig = 5;
const int Echo = 6;

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
}

void loop() {
    digitalWrite(Trig, LOW);
    delayMicroseconds(300);
    digitalWrite(Trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(Trig, LOW);
    duration = pulseIn(Echo, HIGH);
    distance = duration * 0.0343 / 2;
    if(distance <= 30){
      Serial.print(1);
    }else{
      Serial.print(0);
    }
}