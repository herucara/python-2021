import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT * FROM customers")
#print(c.fetchone([2]))
#c.fetchmany(3)
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
