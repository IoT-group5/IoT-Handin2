void setup() {
  Serial.begin(9600);
}
void loop() {
  uint32_t startTime = millis();
  uint32_t i = 0;

  while (true) {
    uint32_t t = millis();
    delay(10); //artificial delay to simulate a workload
    uint32_t outputDelay = startTime + (100 * i) - t;
    if (outputDelay > 0) {
      delay(outputDelay);
    }
    Serial.println(outputDelay);
    i++;
  }
}
