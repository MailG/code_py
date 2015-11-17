
import logging

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)    

def main():
	setup_logger('hello', 'hello.log')
	setup_logger('world', 'world.log')
	l = logging.getLogger('hello')
	o = logging.getLogger('world')
	l.info('OK')
	o.info('OK')

if __name__ == "__main__":
	main()

