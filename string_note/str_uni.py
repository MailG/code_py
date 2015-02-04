
def demo():
	
	a_map = dict(h=u"hello", w="world")
	try:
		sum_str = a_map['h'] + a_map['w']
		print sum_str 
	except Exception as e:
		print "error sum_str = a_map['h'] + a_map['w'] , ", e

	try:
		other_str = "%s %s" % tuple(list(a_map))
		print other_str
	except Exception as e:
		print "error other_str = %s, %s % list(sum_str) ", e

demo()
