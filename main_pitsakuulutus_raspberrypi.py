import socket
#import RPi.GPIO as GPIO
import time, sys, os

# CLIENT

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try:
    TCP_IP = "192.168.8.101"
    TCP_PORT = 12345
    BUFFER_SIZE = 1024
    MESSAGE = str.encode("Hello, World!")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print("Connected to {}:{}".format(TCP_IP, TCP_PORT))
    def restart_client():
        """Restarts the client. """
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def reconnect():
        """ Restarts the client program in hope of a new connection """
        print("Restarting...")
        s.close()
        print("Client closed")
        print("3sec safety wait")
        time.sleep(3) # 3sec waiting because server must be up before client
        print("Done, now restarting")
        restart_client()
        # try:
        #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     s.connect((TCP_IP, TCP_PORT))
        #     print("reconnected")
        # except:
        #     print("reconnection failed")
        # return

    def kuulutus():
        kuulutusBYTE = str.encode("kuulutus")
        s.send(kuulutusBYTE)
        return

    def valmis():
        """ Välkyttää ledejä tai jotain """
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
           reconnect()

        print("\n", data.decode(), "\n")

        if data.decode() == "valmis":
           valmis()

        time.sleep(0.1)   # Estää overflown, päivittää clientiä .1sec välein



    print ("received data:", data)

except:
    raise
    reconnect()
