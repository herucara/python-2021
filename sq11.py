import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#create a table
c.execute("""INSERT INTO (
	   first_name text,
	   last_name text,
	   email text
	   )""")

many_customers = [
                   ('wes', 'bronw', 'wes@bronw.com'),
                   ('steph', 'keiw', 'steph@keiw.com'),
                   ('dan', 'plas', 'dan@plas.com'),
                   ('wes', 'bronw', 'edre@bronw.com'),
                   ('ber', 'bronw', 'berw@bronw.com'),
                   ('klaas', 'qwer', 'klot@gmail.com'),
                   ('prada', 'warew', 'prad@gmail.com'),
                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


#DATATYPE
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

conn.commit()












#closeour connection
conn.close()

import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT * FROM customers") #c.execute("SELECT * FROM customers WHERE last_name = 'elder'")
#print(c.fetchone([2]))               #c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
#c.fetchmany(3)                       #execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
#print(c.fetchall())

items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("------" + "\t\t--------")
for item in items:
    print(item[0] + "\t\t" + item[2])



#print("command execute sucsefully...")

#DATATYPE
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

conn.commit()

#closeour connection
conn.close()






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
c.execute("SELECT rowid * FROM customers ORDER BY rowid DESC")
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

