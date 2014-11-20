import data_packager as D
import socket
import argpraser
import logging
import sys

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

if __name__ == "__main__":
				
	ip = ''	
	input_data = '{}'
	port = 34506

	HOST = ip    # The remote host
	PORT = port# The same port as used by the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	
	d = D.Header()	
	s.sendall(d.packageData(input_data))
	
	data = s.recv(2048)
	s.close()
	print "return", repr(data)
