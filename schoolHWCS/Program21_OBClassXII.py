import mysql.connector as connector

con = connector.connect(user = 'root', password = 'mySQL1234$s-10763', host = 'localhost', database = 'prog21')
cur = con.cursor()

try:
    cur.execute('CREATE TABLE STATIONERY(S_ID VARCHAR(10), STATIONERYNAME VARCHAR(50), COMPANY VARCHAR(30), PRICE BIGINT);')
    con.commit()
    print('Table created successfully')
except:
    print('Table already exists, passing..')

print()

for i in range(5):
    S_ID = input('Enter S_ID: ')
    StationaryName = input('Enter Name: ')
    Company = input('Enter Company: ')
    Price = int(input('Enter Price: '))
    cur.execute('INSERT INTO STATIONERY VALUES("{}","{}","{}",{})'.format(S_ID, StationaryName, Company, Price))
    con.commit()
    print()


cur.execute('SELECT * FROM STATIONARY WHERE Price < 10;')
v = cur.fetchall()
for i in v:
    print(i)
