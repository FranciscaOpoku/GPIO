from gpiozero import LED, Button
from signal import pause
from time import sleep


Red = LED(17)
Yellow = LED(27)
Green = LED(22)
button = Button(2)

def toggle_lights():
    Yellow.on
    sleep(4)
    Green.off
    Red.on
    sleep(10)
    Green.on
    
def toggle_green():
    Green.on
    Red.off
    Yellow.off
button.when_pressed = toggle_lights
button.when_released = toggle_green

pause()

