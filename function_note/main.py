

def g(*args):
	print "g args", args

def fun(*args):
	print "args ", args
	g(*args)
	g(args)


def main():
	fun('1', '2', '3')	

main()
