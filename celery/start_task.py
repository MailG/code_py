
from tasks import sendmail
import time

while 1:
	a = sendmail.delay("abc")
	time.sleep(1)
	if a.ready():
		print a.get() 
	
