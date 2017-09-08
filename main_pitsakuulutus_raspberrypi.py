import socket
import RPi.GPIO as GPIO
import time

# CLIENT

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

TCP_IP = "10.0.0.5"
TCP_PORT = 12346
BUFFER_SIZE = 1024
MESSAGE = str.encode("Hello, World!")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def kuulutus():
    kuulutusBYTE = str.encode("Kuutluta!!!!")
    s.send(kuulutusBYTE)
    return

while True:
    if GPIO.input(13) == 1:
       print("Button is pressed")
       kuulutus()

    time.sleep(0.5)


data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
