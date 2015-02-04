import socket
import sys


def send_file(filename, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', int(port)))
	s.listen(1)
	conn, addr = s.accept()
	print addr, " connected"
	buf = 1024
	with open(filename, 'rb') as f:
		data = f.read(buf)
		print "----"
		print data
		while len(data):
			conn.sendall(data)
			data = f.read(buf)
	s.close()	
	

send_file(sys.argv[1], sys.argv[2])
