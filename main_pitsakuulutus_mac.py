import socket, time, os, sys
from qlab_handler import qlab_GO

# SERVER

class server():
    def __init__(self):
        # TCP_IP must be server IP
        self.TCP_IP = "192.168.1.38"  # public IP "192.168.1.00"
        self.TCP_PORT = 12346
        self.BUFFER_SIZE = 20  # Normally 1024, but we want fast response


        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket init")
        self.s.bind((self.TCP_IP, self.TCP_PORT))

        print("Bind ok, waiting connection...")
        self.s.listen(1)   # Waiting only 1 connection

        print("Accepting...")
        self.conn, addr = self.s.accept()

        print ('Connection address:', addr)


    def restart_server(self):
        """ Restarts the program. """
        print("Restarting server...")
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def reconnect(self):
        self.s.close()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket init")
        self.s.bind((self.TCP_IP, self.TCP_PORT))

        print("Bind ok, waiting connection...")
        self.s.listen(1)   # Waiting only 1 connection

        print("Accepting...")
        self.conn, addr = self.s.accept()

        print ('Connection address:', addr)

    def kaynnistaKuulutus(self):
        """ ITSE KUULUTUKSEN KÄYNNISTYS """
        print("KUULUTETAAAAN: Pitsatilauksien pitsat ovat haettavissa :)")
        qlab_GO()
        return

    def disconnected(self):
        x = 0
        while x <= 3:
            try:
                self.conn.recv(self.BUFFER_SIZE)
                break
            except:
                x += 1
                print("Connection request %i" % x)
                time.sleep(3)

        if x <= 3: disconnected = False
        else:      disconnected = True

        return disconnected

    def run(self):

        print()
        # The main loop starts here
        while True:
            # if self.disconnected():
            #     self.reconnect()

            #self.conn.send(str.encode("loop"))

            print("Listening data")
            data = self.conn.recv(self.BUFFER_SIZE)
            data = data.decode().split(";")

            if data[0] == "kuulutus":
                if time.time() - float(data[1]) <= 10:
                    print()
                    print("passed time", time.time() - float(data[1]), "s")
                    self.conn.send(str.encode("Action: Kuulutetaan\n"))
                    self.kaynnistaKuulutus()
                    self.conn.send(str.encode("Done"))

            try:
                print ("Received data:", data[0], data[1])
                continue
            except:
                pass
                #print ("Received data:", data)

if __name__ == "__main__":
    s = server()
    s.run()
