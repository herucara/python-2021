import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


#update records
#c.execute("""UPDATE SET first_name = 'bob'
#	        WHERE last_name = 'elder'
 #   """)
#c.execute("""UPDATE SET first_name = 'bob'
#	        WHERE rowid = 1
 #   """)
#c.execute("DELETE FROM customers WHERE rowid = 6")
#order by
c.execute("SELECT rowid * FROM customers where last_name like 'br%' and rowid = 3")


#many_customers = [
#                   ('wes', 'bronw', 'wes@bronw.com'),
#                   ('steph', 'keiw', 'steph@keiw.com'),
#                   ('dan', 'plas', 'dan@plas.com'),
#                   ('wes', 'bronw', 'edre@bronw.com'),
#                   ('ber', 'bronw', 'berw@bronw.com'),
#                   ('klaas', 'qwer', 'klot@gmail.com'),
#                   ('prada', 'warew', 'prad@gmail.com'),
#                ]
#c.execute("SELECT rowid * FROM customers ORDER BY rowid")
#conn.commit()

#query the database
##print(c.fetchone([2]))
#c.fetchmany(3)
#print(c.fetchall())

items = c.fetchall()
for item in items:
	print(item)





#print("command execute sucsefully...")

#DATATYPE
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#conn.commit()

#closeour connection
conn.close()



mport sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


#update records
#c.execute("""UPDATE SET first_name = 'bob'
#	        WHERE last_name = 'elder'
 #   """)
#c.execute("""UPDATE SET first_name = 'bob'
#	        WHERE rowid = 1
 #   """)
#c.execute("DELETE FROM customers WHERE rowid = 6")
#order by
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid LIMIT 6")


many_customers = [
                   ('wes', 'bronw', 'wes@bronw.com'),
                   ('steph', 'keiw', 'steph@keiw.com'),
                   ('dan', 'plas', 'dan@plas.com'),
                   ('wes', 'bronw', 'edre@bronw.com'),
                   ('ber', 'bronw', 'berw@bronw.com'),
                   ('klaas', 'qwer', 'klot@gmail.com'),
                   ('prada', 'warew', 'prad@gmail.com'),
                ]
c.execute("SELECT rowid * FROM customers ORDER BY rowid")
conn.commit()

#query the database
##print(c.fetchone([2]))
#c.fetchmany(3)
#print(c.fetchall())

items = c.fetchall()
for item in items:
	print(item)





#print("command execute sucsefully...")

#DATATYPE
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#conn.commit()

#closeour connection
conn.close()
