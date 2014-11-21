from socket import *

HOST = '127.0.0.1'    # The remote host
PORT = 9990 # The same port as used by the server
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
print 'Received', repr(data)
while 1:
	indata = raw_input("input command:")	
	s.sendall(indata)
	data = s.recv(1024)		
	print 'Received', repr(data)
s.close()
