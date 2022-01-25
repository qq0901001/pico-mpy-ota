import machine
import utime

# 
version = ''
# 
f = open('/version.txt')
if f :
    version = f.read()

led_onboard = machine.Pin(2, machine.Pin.OUT)

while True:
    print ('Version:' + version)
    led_onboard.value(1) 
    utime.sleep_ms(200) 
    led_onboard.value(0) 
    utime.sleep_ms(1000) 

    

