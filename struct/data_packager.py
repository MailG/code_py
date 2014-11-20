import struct as S
class Header(object):
	''' tcp header '''
	def __init__(self):
		self.head_fmt = '!II'
		self.head_len = S.calcsize(self.head_fmt)
		pass
	def packageData(self, txt_data):		
		txt_len = len(txt_data)
		struct_fmt = self.head_fmt + str(txt_len) + "s"
		self.message_length = S.calcsize(struct_fmt)
		return S.pack(struct_fmt,self.message_length, 0, txt_data) 	
	def parseData(self, bin_data):
		total_len = len(bin_data)
		if total_len < self.head_len:
			raise ValueError		
		struct_fmt = self.head_fmt + str(total_len - self.head_len) + 's'	
		return S.unpack(struct_fmt, bin_data)



if __name__ == "__main__":
	h = Header()	
	json_data = '{"hello": "world"}'
	data = h.packageData(json_data)
	print data
	print h.parseData(data)
	
			

