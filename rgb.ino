#include "FastLED.h"
#define NUM_LEDS 30
#define DATA_PIN 3

CRGB leds[NUM_LEDS];

int R,G,B,BR; //Red, green, blue, and brightness values
char data[4];

void setup() {
    //setup led strand
    FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
    Serial.begin(9600);
    
}

void loop() {
  if(Serial.available() > 3) {
    byte in = Serial.read();
    //if the byte read is the "start byte" 'R', read in 4 more values (R, G, B, BR)
    if(in == 'R') {
      Serial.readBytes(data, 4);
      R = data[0];
      G = data[1];
      B = data[2];
      BR = data[3];
  }
}
  //set every pixel to R,G,B
  for(CRGB & pixel : leds) {
    pixel.r = R;
    pixel.g = G;
    pixel.b = B;
    
  }
  FastLED.setBrightness(BR);
  FastLED.show();
  delay(50);
}

