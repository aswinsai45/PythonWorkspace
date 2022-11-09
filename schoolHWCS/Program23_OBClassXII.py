import mysql.connector as connector

con = connector.connect(user='root', password='mySQL1234$s-10763', host='localhost')
cur = con.cursor(buffered=True)

def createdatabase():
    print()
    try:
        cur.execute('CREATE DATABASE CUSTOMER;')
        cur.execute('USE CUSTOMER;')
        con.commit()
        print('Database has been created successfully')
    except connector.errors.DatabaseError:
        print('Database already exists')


def createtables():
    print()
    try:
        cur.execute('use customer;')
        cur.execute('CREATE TABLE CUSTOMERDETAILS(CID BIGINT, CNAME varchar(30), ADDRESS varchar(50), PHONENO bigint);')
        cur.execute(
            'CREATE TABLE PURCHASEDETAILS(PID bigint, PURCHASEDATE date, NumITEMS bigint, TOTALAMOUNT float, CID bigint);')
        con.commit()
        print('Tables have been created successfully')
    except connector.errors.ProgrammingError:
        print('Tables already exist')


def insertdata():
    print()
    print('Inserting into CUSTOMER DETAILS~')
    cid = int(input('Enter ID: '))
    cname = input('Enter customer name: ')
    address = input('Enter address: ')
    phone = int(input('Enter phone: '))

    print()
    print('Inserting into PURCHASE DETAILS~')
    pid = int(input('Enter product ID: '))
    dt = input('Enter date [yyyy-mm-dd]: ')
    nit = int(input('Enter quantity: '))
    total = float(input('Enter total price: '))

    cur.execute('INSERT INTO CUSTOMERDETAILS VALUES({}, "{}", "{}", {})'.format(cid, cname, address, phone))
    cur.execute('INSERT INTO PURCHASEDETAILS VALUES({}, "{}", {}, {}, {})'.format(pid, dt, nit, total, cid))
    con.commit()


def searchdata():
    print()
    cid = int(input('Enter CID for search: '))
    date = input('Enter purchase date [dddd-mm-yy]: ')

    cur.execute('select * from purchasedetails natural join customerdetails where cid = {} and purchasedate = "{}"'.format(cid, date))
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Record not found')


def displaydata():
    print()
    print('Customer Details')
    cur.execute('SELECT * FROM CUSTOMERDETAILS;')
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Table Empty\n')

    print()
    print('Purchase Details')
    cur.execute('SELECT * FROM PURCHASEDETAILS;')
    k = cur.fetchall()
    if k:
        for i in k:
            print(i)
    else:
        print('Table Empty')


print('1. Create Database\n2. Create Tables\n3. Insert Data\n4. Search Data\n5. Display Info from Both tables\n6. Exit')
while True:
    ch = int(input('\nEnter choice: '))
    if ch == 1:
        createdatabase()
    elif ch == 2:
        createtables()
    elif ch == 3:
        cur.execute('use customer')
        cur.execute('select * from customerdetails')
        o = cur.fetchall()
        cur.execute('select * from purchasedetails')
        k = cur.fetchall()

        if not k and not o:
            for i in range(5):
                insertdata()
        else:
            insertdata()
    elif ch == 4:
        searchdata()
    elif ch == 5:
        displaydata()
    elif ch == 6:
        print('Thank you')
        break
    else:
        print('Please enter a valid choice')
