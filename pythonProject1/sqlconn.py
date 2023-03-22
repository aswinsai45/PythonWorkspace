import mysql.connector as connector

con = connector.connect(host = 'localhost', username = 'root', password = 'mySQL1234$s-10763')
cur = con.cursor()

def create():
    try:
        cur.execute('drop database sqlconn;')
        cur.execute('CREATE DATABASE SQLCONN;')
        cur.execute('USE SQLCONN;')
        cur.execute('CREATE TABLE NAMEFAV(Name varchar(30), Favitem varchar(30));')
    except connector.errors.DatabaseError:
        print('Database exists!')

    con.commit()
def insert():
    while True:
        n = input('Enter name: ')
        fav = input('Enter fav food: ')

        cur.execute('insert into namefav values("{}","{}");'.format(n, fav))
        cnt = input('cnt? y/n: ')
        if cnt == 'n':
            break
    con.commit()

def display():
    cur.execute('use sqlconn;')
    cur.execute('select * from namefav;')
    v = cur.fetchone()
    if v:
        for i in v:
            print(i)
    else:
        print('table empty')


display()

con.close()
