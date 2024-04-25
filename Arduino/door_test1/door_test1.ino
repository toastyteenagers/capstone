int const doorPin = 13;

void setup() {
  pinMode(doorPin, OUTPUT);
}

void loop() {
  digitalWrite(doorPin, HIGH);
  delay(2000);
  digitalWrite(doorPin, LOW);
  delay(2000);
}
