
import operator

if __name__ == "__main__":
	l1 = ["1", "2"]
	l2 = [1, 2]
	print zip(l1, l2)
	print sorted(zip(l1,l2), key = lambda t: -t[1])
	for i in zip(l1, l2):
		print i
	for (i,j) in zip(l1, l2):
		print j


