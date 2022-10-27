import mysql.connector as connector

username = 'AdminBreeze'
password = 'Admin000'

userin = input('Enter username: ')
passin = input('Enter password: ')

if not (userin == username and passin == password):
    print('Username/Password incorrect for Admin')
    exit()

con = connector.connect(host='localhost', user='root', passwd='mySQL1234$s-10763', database='tickets')
cur = con.cursor(buffered=True)

print('\n1. Retrieve All Reservations\n2. Cancel a Reservation\n3. Search for a Reservation\n4. Clear All Reservations\n5. Exit Admin Mode')

while True:
    ch = int(input('Enter your choice:'))
    if ch == 1:
        cur.execute('SELECT * FROM JOURNEYDETAILS;')
        v = cur.fetchall()
        if not v == []:
            for i in v:
                print(i)
        else:
            print('No Active Bookings till now.')

    elif ch == 2:
        boardingPassCancel = input('Please enter boarding pass number here: ')
        con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
        cur = con.cursor(buffered=True)
        cur.execute('select * from journeydetails where boardingpass = "{}"'.format(boardingPassCancel))
        v = cur.fetchall()
        if v == []:
            print('BoardingPass Incorrect/Not Found')

        else:
            cur.execute('delete from journeydetails where boardingpass = "{}"'.format(boardingPassCancel))
            con.commit()
            print('Successfully Cancelled Ticket :(')

    elif ch == 3:
        sr = input('Enter Boarding Pass to Search: ')
        cur.execute('SELECT * FROM JOURNEYDETAILS WHERE boardingpass = "{}"'.format(sr))
        v = cur.fetchall()
        print('ALL RESERVATIONS UNDER ', sr)
        for i in v:
            if i:
                print(i)
            else: print('No Booking Found')

    elif ch == 4:
        print('This action cannot be undone. ')
        conf = input('DELETE ALL RESERVATIONS? [Y/N]: ')
        if conf == 'Y' or conf == 'y':
            cur.execute('DELETE FROM JOURNEYDETAILS;')
            con.commit()
            print('DELETED ALL BOOKINGS')
        elif conf == 'N' or conf == 'n':
            print('Exiting menu')
            break
        else:
            print('Invalid input')
    elif ch == 5:
        print('Exiting Admin Mode')
        break
    else:
        print('Incorrect Input.. Exiting')
        break

