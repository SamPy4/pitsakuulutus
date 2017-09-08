import socket, time, os, sys

# SERVER

TCP_IP = "10.0.0.5"
TCP_PORT = 12346
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

print("bind ok, waiting connection...")
s.listen(1)

print("Accepting...")
conn, addr = s.accept()

print ('Connection address:', addr)

def restart_server():
    """Restarts the server. """
    python = sys.executable
    os.execl(python, python, * sys.argv)

def reconnect():
    #restart_server()

    try:
        print("Reconnecting...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Connecting...")
        s.connect((TCP_IP, TCP_PORT))

        print ('Connection address:', addr)
        time.sleep(1)
    except:
        return

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

while 1:
    data = haeData()

    if data.decode() == "kuulutus":
        kaynnistaKuulutus()
        conn.send(str.encode("valmis"))

    if not data:
        break

    print ("received data:", data.decode())
    #conn.send(data)  # echo
conn.close()
