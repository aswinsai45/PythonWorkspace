import mysql.connector as connector

con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763')
cur = con.cursor(buffered=True)

def createdatabase():
    print()
    try:
        cur.execute('CREATE DATABASE BOOKSTORE;')
        cur.execute('USE BOOKSTORE;')
        con.commit()
        print('Database created successfully')

    except connector.errors.DatabaseError:
        print('Database Already Exists!')

def createtable():
    print()
    try:
        cur.execute('use BOOKSTORE;')
        cur.execute(
            'CREATE TABLE BOOKDETAILS(ISBN bigint, BOOKNAME varchar(30), AUTHOR varchar(30), PUBLISHER varchar(30), YEAR bigint, PRICE float, QTY bigint);')
        con.commit()
        cur.execute(
            'CREATE TABLE CUSTOMERDETAILS(CID bigint, CNAME varchar(30), PHNO bigint, ISBN bigint, PURCHASEDATE date, PURCHASEQTY bigint);')
        con.commit()

        print('Tables created successfully')

    except connector.errors.ProgrammingError:
        print('Tables already exist!')

def insertbook():
    print()
    print('ENTER INTO BOOK DETAILS~')
    isbn = int(input('Enter ISBN: '))
    name = input('Enter Book Name: ')
    auth = input('Enter Author: ')
    pub = input('Enter Publisher: ')
    yr = input('Enter Year: ')
    price = float(input('Enter Price: '))
    qty = input('Enter Quantity: ')

    cur.execute('insert into bookdetails values({}, "{}","{}","{}","{}",{},{})'.format(isbn, name, auth, pub, yr, price, qty))
    con.commit()
def insertcustomer():
    print()
    print('ENTER INTO CUSTOMER DETAILS~')
    cid = int(input('Enter ID: '))
    nmc = input('Enter Customer Name: ')
    ph = int(input('Enter Customer PhoneNum: '))
    isbn = int(input('Enter ISBN: '))
    dt = input('Enter Purchase Date: ')
    prqty = int(input('Enter Purchased Qty: '))


    cur.execute('insert into customerdetails values({},"{}",{},{},"{}",{})'.format(cid, nmc, ph,isbn, dt, prqty))
    con.commit()

def total():
    cur.execute('use bookstore;')
    cur.execute('select cname, isbn, purchaseqty, price, purchaseqty*price as totalprice from bookdetails natural join customerdetails order by cname;')
    v = cur.fetchall()
    for i in v:
        print(i)

def display():
    print()
    cur.execute('use bookstore;')
    print('BOOKDETAILS TABLE~')
    cur.execute('SELECT * FROM BOOKDETAILS;')
    v = cur.fetchall()
    if v:
        for i in v:
            print(i)
    else:
        print('Table bookdetails empty')

    print('CUSTOMERDETAILS TABLE')
    cur.execute('SELECT * FROM CUSTOMERDETAILS;')
    k = cur.fetchall()
    if k:
        for i in k:
            print(i)
    else:
        print('Table customerdetails empty')

print('1. Create Database\n2. Create Tables\n3. Insert Book\n4. Insert Customer\n5. Total Books Purchased\n6. Display Both Tables\n7. Exit')

while True:
    ch = int(input('\nEnter choice: '))
    if ch == 1:
        createdatabase()
    elif ch == 2:
        createtable()
    elif ch == 3:
        cur.execute('use bookstore;')
        cur.execute('select * from bookdetails;')
        o = cur.fetchall()
        if not o:  # if o == [], i.e. o is empty
            for i in range(5):
                insertbook()
        else:
            insertbook()
    elif ch == 4:
        cur.execute('use bookstore;')
        cur.execute('select * from customerdetails')
        k = cur.fetchall()
        if not k:  # if k == [], i.e. k is empty
            for i in range(5):
                insertcustomer()
        else:
            insertcustomer()
    elif ch == 5:
        total()
    elif ch == 6:
        display()
    elif ch == 7:
        print('Thank you')
        break
    else:
        print('Please enter a valid choice')
