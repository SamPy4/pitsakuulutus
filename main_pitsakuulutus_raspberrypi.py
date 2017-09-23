import socket
import RPi.GPIO as GPIO
import time, sys, os

# CLIENT

BUTTON = 6  # Main button
LED1   = 11 # Red "won't send"-led
LED2   = 5  # Green "will send"-led
LED3   = 19 # White/yellow progress PWM led

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

PWM1 = GPIO.PWM(LED3, 100)  # pin, frec
PWM1.start(0)

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
    kuulutusBYTE = str.encode("kuulutus;{}".format(time.time()))
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
painaika = 50 # /10 = sec
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

    if time.time() - last_time_kuulutettu  >= spamminesto:
        GPIO.output(LED1, False)
        GPIO.output(LED2, True)
    else:
        GPIO.output(LED1, True)
        GPIO.output(LED2, False)

    if GPIO.input(BUTTON) == 1:
        # print("Button is pressed!!!")

        if x+1<=painaika: x += 1  # Lisätään x:ää jos se ei ylitä rajaa

        PWM1.ChangeDutyCycle(x*4/5)  # Kirkastaa lediä x saa olla maksimissaan 100.0
        print(x)

        if time.time() - last_time_kuulutettu  >= spamminesto and x == painaika:
            PWM1.ChangeDutyCycle(0)

            last_time_kuulutettu = time.time()
            print("Pyyntö lähetetty")
            kuulutus()
        else:
            pass
            #print("Ei voi kuuluttaa vielä")
    else:
        PWM1.ChangeDutyCycle(0)
        x = 0
        #print("Zeroed:", x)

    #print("\n", data.decode(), "\n")

    time.sleep(0.1)   # Estää overflown, päivittää clientiä .1sec välein
