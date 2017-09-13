import socket, time, os, sys

# SERVER

# TCP_IP must be server IP

def restart_server():
    """Restarts the server. """
    python = sys.executable
    os.execl(python, python, * sys.argv)

try:
    TCP_IP = "10.1.134.124"  # public IP "192.168.1.00"
    TCP_PORT = 1234
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))

    print("bind ok, waiting connection...")
    s.listen(1)

    print("Accepting...")
    conn, addr = s.accept()

    print ('Connection address:', addr)

    def reconnect():
        #restart_server()
        try:
            print(tries)
            if tries == 10:
                restart_server()

            print("Reconnecting...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            print("Connecting...")
            s.connect((TCP_IP, TCP_PORT))

            print ('Connection address:', addr)
            time.sleep(1)
        except:
            print(tries)
            return
        print(tries)

    def haeData():
        while True:
            try:
                data = conn.recv(BUFFER_SIZE)
                break
            except: # socket.error as e:
                print()
                reconnect()
                # if e.errno == e.errno.ECONNRESET:
                #     print("No data recieved!!!")
                # else:
                #     raise
        return data

    def kaynnistaKuulutus():
        """ ITSE KUULUTUKSEN KÄYNNISTYS """
        print("KUULUTETAAAAN: Pitsatilauksien pitsat ovat haettavissa :)")
        time.sleep(4)
        return

    spamminesto = 15 # sekuntia
    last_time_kuulutettu = time.time() - spamminesto
    while True:
        data = haeData()

        if data.decode() == "kuulutus":
            if time.time() - last_time_kuulutettu  >= spamminesto:
                last_time_kuulutettu = time.time()
                kaynnistaKuulutus()
                continue
            else:
                conn.send(str.encode("Ei voi kuuluttaa vielä\n"))
            conn.send(str.encode("valmis"))

        if not data:
            break

        print ("received data:", data.decode())
        #conn.send(data)  # echo
    conn.close()

except:
    restart_server()
