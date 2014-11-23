import threading as T
import time

def job(n):
	while n > 0:
		print n
		n = n - 1
		time.sleep(5)
		

a = T.Thread(target = job, args=(10,))

a.start()

a.join()
print "done"


