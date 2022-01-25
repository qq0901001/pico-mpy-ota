import machine
import utime

VER = '1.0'

led_onboard = machine.Pin(2, machine.Pin.OUT)

while True:
    print ('Version:' + VER)
    led_onboard.value(1) 
    utime.sleep_ms(500) 
    led_onboard.value(0) 
    utime.sleep_ms(500) 

    

