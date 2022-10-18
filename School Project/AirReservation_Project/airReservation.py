import mysql.connector as connector
import datetime

print("\n\nWelcome to FlightBook, how can we help you today?: \n")


def timeformatter(date):
    d = datetime.datetime.strftime(date, "%Y-%m-%d")
    return d


# l = []
# l2 = []
# def passengerlist(l, n=8):
#     global l2, ll
#     for j in range(0, len(l), n):
#         l2 = l[j:j + n]
#     l = l2
#
# passengerlist(l)


action = {1: "Book a ticket", 2: "Retrieve a ticket", 3: "Cancel a ticket"}

print(action)
userEnter = int(input("\nEnter the Index: "))
dictAccess = action[userEnter]
print(dictAccess)

# Books a Ticket
if userEnter == 1:
    print('~~You have chose to book a ticket~~')
    ch = int(input("\nEnter the number of people travelling [up-to 3]: "))
    if ch == 1:
        import singleperson
    elif ch == 2:
        import twopersons
    elif ch == 3:
        import threepersons
    else:
        print("Sorry unavailable as of now. Thanks for understanding!")
        exit()

# retrieves a ticket
elif userEnter == 2:
    print('~~You have chose to retrieve a ticket~~')
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

        print('Name = ', l[0])
        date1 = l[1]
        print('Date of Birth: ', timeformatter(date1))
        print('Boarding Pass Number: ', l[2])
        print('Passport Number: ', l[3])
        print('Airline: ', l[4])
        print('Departure: ', l[5])
        date2 = l[6]
        print('DepartureDate: ', timeformatter(date2))
        print('Flight Number: ', l[7])
        print('\n\n')



# Cancels a ticket

elif userEnter == 3:
    print("~~You have chose to cancel a ticket~~")
    boardingPassCancel = input('Please enter boarding pass number here: ')
    con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
    cur = con.cursor()
    cur.execute('delete from journeydetails where boardingpass = "{}")'.format(boardingPassCancel))

else:
    print('Sorry command not available. Try Again')
    exit()
