import mysql.connector as connector

con = connector.connect(user = 'root', password = 'mySQL1234$s-10763', host = 'localhost', database = 'prog21')
cur = con.cursor()

cur.execute('SELECT * FROM STATIONARY WHERE Price < 10;')
v = cur.fetchall()
for i in v:
    print(i)
