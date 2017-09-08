import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def own_exit():
    GPIO.cleanup()
    print("cleaned")
    exit()
    
def kuulutus():
    time.sleep(4)
    own_exit()
    pass

while True:
    if GPIO.input(13) == 1:
       print("Button is pressed")
       kuulutus()

    print("Loop")

    time.sleep(0.5)
