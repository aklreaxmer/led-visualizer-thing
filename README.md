# led-visualizer-thing
Two-fold visualization program for an LED strip. Displays computer screen's average color, and adjusts brightness according to audio output.

<h3>Python</h3>
Uses ImageGrab to compute average color of screen, Pyaudio to compute volume of audio output, and sends data over serial to Arduino

<h3>Arduino</h3>
Uses <a href="https://github.com/FastLED/FastLED">FastLED</a> library for Arduino to control a WS2812B LED strip.
