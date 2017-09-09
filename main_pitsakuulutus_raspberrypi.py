import RPi.GPIO as GPIO
import socket, time

# CLIENT

button1 = 13 # Main button GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# TCP_IP must be the server ip
TCP_IP = "1.0.0.5"   # public ip "192.168.1.00"
TCP_PORT = 12346
BUFFER_SIZE = 1024
MESSAGE = str.encode("Hello, World!")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        print("reconnected")
    except:
        print("reconnection failed")
    return

def kuulutus():
    kuulutusBYTE = str.encode("kuulutus")
    s.send(kuulutusBYTE)
    return

def valmis():
    # Välkyttää ledejä tai jotain
    pass

while True:

    if GPIO.input(button1) == 1:
       print("Pyyntö lähetetty")
       kuulutus()

       try:
           data = s.recv(BUFFER_SIZE)
       except:
           print("Disconnected")
           connect()

       print("\n", data.decode(), "\n")

       if data.decode() == "valmis":
           valmis()

    time.sleep(0.1)


s.close()

print ("received data:", data)
