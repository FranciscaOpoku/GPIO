from gpiozero import LED, Button
from signal import pause
from time import sleep


Red = LED(17)
Yellow = LED(27)
Green = LED(22)
button = Button(2)

while True:
    Red.on
    sleep(4)
    Red.off
    sleep(1)
    
    Yellow.on
    sleep(4)
    Yellow.off
    sleep(1)
    
    Green.on
    sleep(4)
    Green.off
    sleep(1)
    
    Red.on
    Green.on
    Yellow.on
    sleep(10)
    

