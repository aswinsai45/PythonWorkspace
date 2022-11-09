import mysql.connector as connector

con = connector.connect(host='localhost', user='root', password='mySQL1234$s-10763')
cur = con.cursor()


def createdatabase():
    print()
    try:
        cur.execute('create database FLIGHTRESERVATION')
        con.commit()
        print('Database has been created successfully')
    except connector.errors.DatabaseError:
        print('Database already exists')

def createtables():
    print()
    try:
        cur.execute('use flightreservation;')
        cur.execute('create table flightdetails(FL_NO varchar(10), AIRLINENAME varchar(30), SOURCE varchar(30), DESTINATION varchar(30), NO_FLIGHTS bigint, NO_STOPS bigint)')
        con.commit()

        cur.execute('create table passengerdetails(PID bigint, PASSENGERNAME varchar(30), FL_NO varchar(10), JOURNEYDATE date, TICKETPRICE float, TRAVELCLASS varchar(30))')
        con.commit()
        print('Tables have been created successfully')
    except connector.errors.ProgrammingError:
        print('Tables already exist')

def insertflight():
    print()
    fln = input('Enter Flight Number (str): ')
    air = input('Enter Airline: ')
    source = input('Enter Source: ')
    dest = input('Enter Destination: ')
    num_flight = int(input('Enter Num of Flights: '))
    stops = int(input('Enter Num of stops: '))

    cur.execute('insert into flightdetails values("{}","{}","{}","{}",{},{})'.format(fln,air,source,dest,num_flight,stops))
    con.commit()

def insertpassenger():
    print()
    pid = int(input('Enter ID: '))
    name = input('Enter Passenger Name: ')
    flnum = input('Enter Flight Number (str): ')
    dt = input('Enter journey date in yyyy-mm-dd: ')
    pr = float(input('Enter ticket price: '))
    typeclass = input('Enter Class: ')

    cur.execute('insert into passengerdetails values({},"{}","{}","{}",{},"{}")'.format(pid,name,flnum,dt,pr,typeclass))
    con.commit()

def delete():
    print()
    fln = input('Enter Flight Number(str): ')
    cur.execute('delete from flightdetails where fl_no = "{}"'.format(fln))
    con.commit()
    cur.execute('delete from passengerdetails where fl_no = "{}"'.format(fln))
    con.commit()

def deletepermanent():
    print()
    cur.execute('drop table passengerdetails')
    cur.execute('drop table flightdetails')

    con.commit()

print('1. Create Database\n2. Create Tables\n3. Insert FlightDetails\n4. Insert PassengerDetails\n5. Cancel Ticket\n6. DELETE BOTH TABLES!\n7. Exit')

while True:
    ch = int(input('\nEnter Choice: '))
    if ch == 1:
        createdatabase()
    elif ch == 2:
        createtables()
    elif ch == 3:
        cur.execute('select * from flightdetails')
        v = cur.fetchall()
        if not v:
            for i in range(5):
                insertflight()
        else:
            insertflight()
    elif ch == 4:
        cur.execute('select * from passengerdetails')
        k = cur.fetchall()
        if not k:
            for i in range(5):
                insertpassenger()
        else:
            insertpassenger()
    elif ch == 5:
        delete()
    elif ch == 6:
        deletepermanent()
    elif ch == 7:
        print('Thank You')
        break
    else:
        print('Please enter a valid choice')