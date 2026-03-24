# Selena Zhang, 2575286626
# Alexandra Sierra, 4136096472

import Adafruit_MCP3008 as mcp3008
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO  
import time

print("hello world")

# standard mode is BCM - GPIO config
GPIO.setmode(GPIO.BCM)

# software SPI config
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8

# setting pins
LED = 17
GPIO.setup(LED, GPIO.OUT)        # LED

dark_thres = 300;   # darkness threshold
sound_thres = 500;  # sound threshold

def blinkLED(num, dur):
    for i in range(num):
        GPIO.output(LED, 1)
        time.sleep(dur)
        GPIO.output(LED, 0)
        time.sleep(dur)

def readLight():
    start = time.monotonic()
    last = start

    while time.monotonic() - start < 5:
        now = time.monotonic()
        if now - last >= 0.1:
            adc = mcp3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
            light = adc.read_adc(0)
            
            # Darkness threshold for light
            if light > dark_thres:
                print("Light:", light)
            else:
                print("Dark:", light)
            last = now

def readSound():
    start = time.monotonic()
    last = start

    while time.monotonic() - start < 5:
        now = time.monotonic()
        if now - last >= 0.1:
            adc = mcp3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
            sound = adc.read_adc(1)
            print("Sound:", sound)

            # Tapping threshold for sound
            if sound > sound_thres:
                GPIO.output(LED, 1)
                time.sleep(0.1)
                GPIO.output(LED, 0)

            last = now


while True:

    # blink LED 5 times w/ on off intervals of 500 ms
    blinkLED(5, .500)

    # for 5 sec, read output of Grove light sensor with intervals of 100 ms, print raw value and "Dark" / "light"
    readLight()
        
    # blink LED 4 times w/ on off intervals of 200 ms
    blinkLED(4, .200)
    
    # for 5 sec, read output of Grove sound sensor with intervals of 100 ms, print raw value. if sound sensor is tapped, LED turns on for 100 ms
    readSound()



    
