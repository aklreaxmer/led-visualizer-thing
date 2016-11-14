import ImageGrab
import serial
import sys
import pyaudio
import time
import wave
import audioop

r_sum = 0
g_sum = 0
b_sum = 0

ser = serial.Serial('COM5')
p = pyaudio.PyAudio()

#"Stereo Mix" must be enabled in windows settings. input_device_index = the Stereo Mix index
#format,rate, etc. are dependent on sound card and desired settings
stream = p.open(format=pyaudio.paInt16, channels=2, rate=30000,
		input=True, frames_per_buffer=2048, input_device_index=1)

while True:

	'''RGB'''
	#grab screen and get bounding box
	image = ImageGrab.grab()
	pixels = image.load()
	bbox = image.getbbox()
	#iterate over pixels in screen
	for y in range(0, bbox[3]-10, 10):
		for x in range(0, bbox[2]-10, 10):
			#sum rgb values
			r_sum = r_sum + pixels[x,y][0]
			g_sum = g_sum + pixels[x,y][1]
			b_sum = b_sum + pixels[x,y][2]
	
	'''AUDIO'''
	#get 2048 frames and calculate "RMS" (a measure of volume)
	data = stream.read(2048)
	vol = audioop.rms(data, 2)
	#map RMS volume values to (0,255) brightness level for LEDs
	vol_mapped = (int)((float(vol) / float(3000)) * 255)
	if vol_mapped > 255:
		vol_mapped = 255
		
	'''SERIAL'''
	#send data to serial as bytes (chars)
	ser.write('R') # start byte
	#averages for r, g, and b, then audio volume
	ser.write(chr(r_sum / (bbox[2]*bbox[3]/10)))
	ser.write(chr(g_sum / (bbox[2]*bbox[3]/10)))
	ser.write(chr(b_sum / (bbox[2]*bbox[3]/10)))
	ser.write(chr(vol_mapped))

	#reset sums
	r_sum = 0
	g_sum = 0
	b_sum = 0
	time.sleep(.01)
