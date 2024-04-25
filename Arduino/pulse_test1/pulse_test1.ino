int const analogPin = A0;
int transmittance = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  transmittance = analogRead(analogPin);
  Serial.println(transmittance);
}
