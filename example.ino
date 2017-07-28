// SPI oscilloscope
volatile uint8_t scope[4];
volatile uint8_t scope_ch = 1;

void setup(){
  // SPI slave for debugging via USBTinyISP
  SPCR = _BV(SPE) | _BV(SPIE);
}

SIGNAL(SPI_STC_vect) {
  // send next channel
  SPDR = scope[scope_ch];
  scope_ch++;
  scope_ch &= 0b11;
}

void loop() {
  // update channel data
  scope[0] = analogRead(1);
  scope[1] = millis();
  scope[2] = 42;
  scope[3] = 0;
}
