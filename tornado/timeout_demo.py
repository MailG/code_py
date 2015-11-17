
import tornado
import time
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

all_job = []
test_job_num = 10

def get_queue():
	# do sync job	
	# get 10 schedule job
	job = range(test_job_num)
	print "job is ",job, " processing job"
	process(job)  
	pass


def process(job):
	# calculate what to do
	for i in job:
		call_http_async(i)
	pass
				

def call_http_async(i):

	
	http_client = AsyncHTTPClient()
	
	http_client.fetch("http://moceye.com", request_timeout = 1, callback=lambda x:on_res(i, x))
	pass	


def on_res(i, response):
	if response.error:
		print response.error
	print response.body
	all_job.append(i)
	print "on_res :" ,len(all_job), "job ", all_job
	if len(all_job) == test_job_num:
		tornado.ioloop.IOLoop.instance().stop()
		
	

def main():

	def on_timeout(num):
		print "do something"		
		get_queue()
		#tornado.ioloop.IOLoop.instance().add_timeout(time.time()+num,  lambda: on_timeout(num))  

	num = 1 #60s  

	tornado.ioloop.IOLoop.instance().add_timeout(time.time()+num,  lambda: on_timeout(num))  
	tornado.ioloop.IOLoop.instance().start()		





if __name__ == "__main__":
	main()
