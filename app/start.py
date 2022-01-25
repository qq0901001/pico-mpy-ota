import time
from machine import Pin, PWM, Timer

VER = '1.0'

led = Pin(25, Pin.OUT)

#
def tick(timer):
    global led
    led.toggle()
    print ('Version:' + VER)

#
tim = Timer()
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
