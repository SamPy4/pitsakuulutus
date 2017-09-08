import socket

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
while 1:
    data = conn.recv(BUFFER_SIZE)

    if not data:
        break

    print ("received data:", data)
    conn.send(data)  # echo
conn.close()
