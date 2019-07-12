import subprocess
from subprocess import call
from signal import pause
from gpiozero import Button

     
def process():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print("Resetting now")
    
button = Button(2)
print("press the button to Reset")
button.when_pressed = process

pause()

process()
         
     