

cst_domain_set = set()

def load_tls_domain():
	with open('effective_tld_names.dat', 'r') as f:
		for i in f:
			i = i[:-1]
			cst_domain_set.add(i)

def find_domain_bussiness_test(x):
	print find_domain_bussiness(x)

def find_domain_bussiness(domain):
	domain_part = domain.split('.')
	for i in range(len(domain_part)):
		domain_test = ".".join(domain_part[i:])
		if domain_test in cst_domain_set:
			if i == 0:
				return domain
			else:
				return ".".join(domain_part[i-1:])
			 	
	return None

def test():
	load_tls_domain()
	domain_list = [
'www.abc.com',
'www.abc.com.cn',
'www.com',
'afb.gov.cn',
]	
	map(lambda x:find_domain_bussiness_test(x), domain_list)

test()
