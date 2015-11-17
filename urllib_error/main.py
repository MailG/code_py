
import urllib2



def main():
	try:
		out = urllib2.urlopen(urllib2.Request("http://www.moceye.com/faef"), timeout = 5)
		for i in out:
			print i
	except urllib2.HTTPError as e:
		if e.code == 404:
			print '404 got'
		if e.code == 416:
			status = 'download miss data'
			print status

		else:
			print 'http error'
	
	

if __name__ == "__main__":
	main()
