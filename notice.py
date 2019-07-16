from gpiozero import Button
from signal import pause
import requests

button = Button(17)

def call():
    r =requests.get("https://maker.ifttt.com/trigger/button_click/with/key/ot-0PLFkI_lfbXl3YBmcRCkBkwc-wfkx85ipObB26bp")
    print("Thank you, message sent")

print("Press button to send")
button.when_pressed = call

pause()
call()
