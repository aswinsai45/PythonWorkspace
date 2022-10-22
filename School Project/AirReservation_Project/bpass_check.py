import mysql.connector as connector
import datetime



def timeformatter(date):
    d = datetime.datetime.strftime(date, "%Y-%m-%d")
    return d

boardingPass = input('Enter boarding pass number here: ')
con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
cur = con.cursor()
cur.execute('Select * from journeydetails where boardingpass = "{}"'.format(boardingPass))
v = cur.fetchall()

p = 0
for row in v:
    l = []
    for col in row:
        l.append(col)

    print('Name: ', l[0])
    date1 = l[1]
    print('Date of Birth: ', timeformatter(date1))
    print('Boarding Pass Number: ', l[2])
    print('Passport Number: ', l[3])
    print('Departure Location: ', l[4])
    print('Destination Location: ', l[5])
    print('Airline: ', l[6])
    print('Departure Time: ', l[7])
    date2 = l[8]
    print('DepartureDate: ', timeformatter(date2))
    print('Flight Number: ', l[9])
    print('\n\n')

