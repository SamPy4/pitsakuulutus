import socket
import RPi.GPIO as GPIO
import time, sys, os

# CLIENT

BUTTON = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

TCP_IP = "192.168.1.38"
TCP_PORT = 12346
BUFFER_SIZE = 1024

print("Connecting...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print("Connected to {}:{}".format(TCP_IP, TCP_PORT))

def restart_client():
    """Restarts the client. """
    python = sys.executable
    os.execl(python, python, * sys.argv)

def reconnect():
    s.close()

    sleep(10)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print("Connected to {}:{}".format(TCP_IP, TCP_PORT))


def kuulutus():
    kuulutusBYTE = str.encode("kuulutus")
    s.send(kuulutusBYTE)
    return

def disconnected():
    x = 0
    while x <= 3:
        print("Disconnect try: %i" % x)
        try:
            s.send(str.encode("connection"))
            x = 3
            break
        except:
            x += 1
            print("Connection request %i" % x)
            time.sleep(3)

    if x <= 3: disconnected = False
    else:      disconnected = True

    return disconnected


def valmis():
    """ Välkyttää ledejä tai jotain """
    pass


# Estää ihmisiä rämppäämästä nappia
spamminesto = 15 # sekuntia
last_time_kuulutettu = time.time() - spamminesto
x = 0
print("loop started")

while True:
    # if disconnected():
    #     reconnect()

    # print("Reciveing data")
    # data = s.recv(BUFFER_SIZE)
    # print("Data recieved")
    #
    # print("Sending data")
    # s.send(str.encode("loop"))
    # print("Data sent")

    if GPIO.input(BUTTON) == 1:
        print("Button is pressed!!!")
        x += 1

        if time.time() - last_time_kuulutettu  >= spamminesto and x == 10:
            last_time_kuulutettu = time.time()
            print("Pyyntö lähetetty")
            kuulutus()
        else:
            x = 0
            print("Ei voi kuuluttaa vielä")

    #print("\n", data.decode(), "\n")

    time.sleep(0.1)   # Estää overflown, päivittää clientiä .1sec välein
