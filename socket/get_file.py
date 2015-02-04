
from socket import *
import sys
HOST = sys.argv[1]    # The remote host
PORT = int(sys.argv[2])# The same port as used by the server
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
with open('abc.tar.gz', 'wb') as f:
	data = s.recv(1024)
	while len(data):
		print "----"
		f.write(data)
		data = s.recv(1024)

	
