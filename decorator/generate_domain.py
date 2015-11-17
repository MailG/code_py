
import unittest 
def gen_domain_list(domain):

	if len(domain) == 0:
		return None
	common_index = 0
	
	common_index = domain.find('.')
	print domain, common_index

def main():
	gen_domain_list("www.bc.ade.da.com")
