import socket
#import RPi.GPIO as GPIO
import time, sys, os

# CLIENT

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try:
    TCP_IP = "192.168.1.38"
    TCP_PORT = 1234
    BUFFER_SIZE = 1024
    MESSAGE = str.encode("Hello, World!")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    def restart_client():
        """Restarts the server. """
        python = sys.executable
        os.execl(python, python, * sys.argv)

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

        # if GPIO.input(13) == 1:
        #    print("Pyyntö lähetetty")
        #    kuulutus()
        cmd = ":"
        cmd =input(">>>")

        if cmd == "":
            kuulutus()

        try:
           data = s.recv(BUFFER_SIZE)
        except:
           print("Disconnected")
           #connect()

        print("\n", data.decode(), "\n")

        if data.decode() == "valmis":
           valmis()

        time.sleep(0.1)

    s.close()

    print ("received data:", data)

except:
    raise
    restart_client()
