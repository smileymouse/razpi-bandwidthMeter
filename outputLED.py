import sys
import time
from neopixel import *

# Read percentage value passed to script when called.
input = sys.stdin.readline().rstrip('\n')
percents = input.split(',')
dlPercent = float(percents[0])+0.5
ulPercent = float(percents[1])+0.5

dlMax = int(dlPercent * 0.55)
ulMax = 120 - int(ulPercent * 0.55)
print dlMax,ulMax

# LED Strip configuration:
LED_COUNT   = 120 # Number of LED Pixels. 
LED_PIN     = 18 # GPIO Pin connected to the pixels
LED_FREQ_HZ = 800000 # LED signal frequency in hertz
LED_DMA     = 5 # DMA Channel to use for generating signal
LED_INVERT  = False # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration as defined above.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)

# Intialize the library.
strip.begin()

# Specifying what color should be set depending on LED position
"""LED COLORS ARE (RED, GREEN, BLUE)"""
def blank(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(0,0,0))
	strip.show()

def dlWheel(led):
#	DOWNLOAD Section

#	"""If current LED is less than position 23 Should be Green w/Fade to Yellow"""
	if led < 23:
		return Color(led * 4, 255, 0)
#	"""If current LED is between 24 and 35 Should be Primarly Yellow"""
	elif led < 40:
		return Color(led*13, 255-led*2, 0)
#	"""If current LED is above 35 Should be RED faded from Yellow"""
	else:
		return Color(255, 110-led*2+5, 0)

def ulWheel(led):
#	UPLOAD Section
#	"""If current LED is """
	if led < 80:
		return Color(255, led*2-128, 0)
#	"""If current LED is """
	elif led < 95:
		led -= 70
		return Color(128-led*2, led*6, 0)
#	"""If current LED is """
	else:
		led -= 97
		return Color(128 - led *5 , 255, 0)

def rainbowCycle(strip):
	for i in range(dlMax):
		strip.setPixelColor(i, dlWheel(i))

	for i in range(120,ulMax-1,-1):
		strip.setPixelColor(i, ulWheel(i))


# Create percentage array to assign colors to LEDs



#
blank(strip)
rainbowCycle(strip)
strip.setPixelColor(13,Color(0,0,255))
strip.setPixelColor(27,Color(0,0,255))
strip.setPixelColor(41,Color(0,0,255))
strip.show()
#


# Update the strip with the buffered values.
# strip.show()
