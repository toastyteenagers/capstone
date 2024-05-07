int const ctrlPin = 3;
int const doorPin = 13;
volatile int buttonState = 0;
volatile int latchState = 0;
unsigned long buttonPressedTime = 0;
unsigned long latchFireTime = 0;

void setup() {
  pinMode(ctrlPin, INPUT);
  pinMode(doorPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  buttonState = digitalRead(ctrlPin);

  if (buttonState == HIGH && latchState == 0) {
    Serial.println("Button Pressed: wait 1.1sec");
    buttonPressedTime = millis();
    latchState = 1;
  }

  if (latchState == 1 && millis() - buttonPressedTime >= 1000) {
    Serial.println("Fire latch");
    digitalWrite(doorPin, HIGH);
    latchFireTime = millis();
    latchState = 2;
  }

  if (latchState == 2 && millis() - latchFireTime >= 1000) {
    Serial.println("Close latch");
    digitalWrite(doorPin, LOW);
    latchState = 3;
  }

  // Reset latch state if button released after the cycle is complete
  if (latchState == 3 && buttonState == LOW) {
    latchState = 0;
  }
}
