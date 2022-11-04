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
        cur.execute('CREATE TABLE "CUSTOMER DETAILS"(CID BIGINT, CNAME varchar(30), ADDRESS varchar(50), PHONENO bigint);')
        cur.execute('CREATE TABLE "PURCHASE DETAILS"(PID bigint, PURCHASEDATE date, NO.ITEMS bigint, TOTALAMOUNT float, CID bigint);')
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

    cur.execute('INSERT INTO "CUSTOMER DETAILS" VALUES({}, "{}", "{}", {})'.format(cid, cname, address, phone))
    cur.execute('INSERT INTO "PURCHASE DETAILS" VALUES({}, "{}", {}, {}, {})'.format(pid, dt, nit, total, cid))
    con.commit()

def searchdata():
    print()
    cid = int(input('Enter CID for search: '))
    date = input('Enter purchase date: ')

    cur.execute('select * from "purchase details" where cid = {} and purchasedate = "{}")'.format(cid, date))
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Record not found')

def displaydata():
    print()
    print('Customer Details\n')
    cur.execute('SELECT * FROM "CUSTOMER DETAILS";')
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Table Empty')

    print()
    print('Purchase Details\n')
    cur.execute('SELECT * FROM "PURCHASE DETAILS";')
    k = cur.fetchall()
    if k:
        for i in k:
            print(i)
    else:
        print('Table Empty')


print('1. Create Database\n2. Create Tables\n3. Insert Data\n4. Search Data\n5. Display Info from Both tables\n6. Exit')
while True:
    ch = int(input('Enter choice: '))
    if ch == 1:
        createdatabase()
    elif ch == 2:
        createtables()
    elif ch == 3:
        o = cur.fetchall()
        if not o:       #if o == [], i.e. o is empty
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
