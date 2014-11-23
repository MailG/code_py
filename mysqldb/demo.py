
import MySQLdb

def select_demo(): 
	try:
	    conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='test',port=3306)
	    cur=conn.cursor()
	    cur.execute('select * from user')
	    cur.close()
	    conn.close()
	except MySQLdb.Error,e:
	     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert_demo():
 
	try:
	    conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
	    cur=conn.cursor()
	     
	    cur.execute('create database if not exists test')
	    conn.select_db('test')
	    cur.execute('create table test(sn int,info varchar(20))')
	     
	    value=(1,'abc')
	    cur.execute('insert into test values(%s,%s)',value)
	     
	    values=[]
	    for i in xrange(5):
		values.append((i,'abce '+str(i)))
		 
	    cur.executemany('insert into test values(%s,%s)',values)
	 
	    cur.execute('update test set info="abcde" where id=3')
	 
	    conn.commit()
	    cur.close()
	    conn.close()
	 
	except MySQLdb.Error,e:
	     print "Mysql Error %d: %s" % (e.args[0], e.args[1])	

