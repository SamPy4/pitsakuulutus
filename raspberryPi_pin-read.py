import RPi.GPIO as GPIO
import time


button = 13
led1   = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(led1, GPIO.OUT)


def kuulutus():
    time.sleep(4)
    print("Done")


state = 0

print("Next comes loop")
while True:
    
    if GPIO.input(13) == 1:
        state =  1 - state
        print("Button is pressed")
        time.sleep(0.3)
#        kuulutus()

        
    if state == 1:
        GPIO.output(6, True)
    if state == 0:
        GPIO.output(6, False)
            
    time.sleep(0.1)
