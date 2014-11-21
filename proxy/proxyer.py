
from socket import *
import time
import threading

host = '127.0.0.1'
port = 9090
proxy_target_host = '127.0.0.1'
proxy_target_port = 9091

def target_server():
	target =  socket(AF_INET, SOCK_STREAM)
	target.bind((proxy_target_host, proxy_target_port))
	target.listen(1)	
	conn,addr = target.accept()
	print "target server", addr, " connected"	
	while 1:
		data = conn.recv(1024)
		if not data: break
		conn.sendall(data.upper())
	target.close()

def proxy_server():
	threading.Thread(target = target_server).start()
	s = socket(AF_INET, SOCK_STREAM)
	s_proxy = socket(AF_INET, SOCK_STREAM)

	s_proxy.connect((proxy_target_host, proxy_target_port))

	s.bind((host, port))
	print host, port
	s.listen(1)

	conn, addr = s.accept()
	while 1:
		data = conn.recv(1024)
		if not data: break
		try :
			s_proxy.sendall(data)
			target_data = s_proxy.recv(1024)
			if not target_data:
				print "target close the connect"
				break			
		except:
			print "proxy failed to connect to target"
		conn.sendall(target_data)		
		print "send to client: ", target_data

		
if __name__ == "__main__":
	proxy_server()
