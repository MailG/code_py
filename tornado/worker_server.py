
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)




if __name__ == "__main__":
	tornado.options.parse_command_line()
	
	print options.port
	tornado.ioloop.IOLoop.instance().start()
