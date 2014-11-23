
import time
import threading
import random

C = threading.Condition
T = threading.Thread


buf = [] 

cond = C()

def product():
	i = 0
	while 1:
		i += 1
		cond.acquire()
		if len(buf) == 10:
			cond.wait()	
		buf.append(i)		
		print "product ", i
		cond.notify()
		cond.release()
		r = random.random()
		time.sleep(r)
	

def custom():
	while 1:
		cond.acquire()
		if not buf:
			print "nothing to custom, wait..."
			cond.wait()
			print "something add to the queue, wake up..."
		print "coustom ", buf.pop(0)	
		cond.notify()
		cond.release()
		time.sleep(random.random())
	

def main():				
	i = threading.Thread(target = product)
	j = threading.Thread(target = custom)

	i.start()
	j.start()
	i.join()
	j.join()
	
	
if __name__ == "__main__":
	main()
