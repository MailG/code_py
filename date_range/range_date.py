
import os
import datetime
import time


def date_range(date_fmt, start_date_str, range_len, interval_day = 1):
	date_start_time = time.strptime(start_date_str, date_fmt)
	print date_start_time
	interval_date = datetime.timedelta(days = interval_day)

	for i in xrange(range_len):
		date_start_time = date_start_time + interval_date	
		yield time.strftime(time.mktime(date_start_time))
def test():
	start_date_str = "20150828"
	for i in date_range("%Y%m%d",  start_date_str, 10):
		print i
		pass


if __name__ == "__main__":
	test()
