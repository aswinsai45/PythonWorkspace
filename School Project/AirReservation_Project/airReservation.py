import os.path


print("\n\nWelcome to FlightBook, how can we help you today?: \n")

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
    file_exist = os.path.exists(
        'C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/' + boardingPass)
    if file_exist:
        pass
    else:
        print('Booking Cancelled/Not Found')
        exit()

    file = open('C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/' + boardingPass, 'r')
    s = file.read()
    print(s)

# Cancels a ticket

elif userEnter == 3:
    print("~~You have chose to cancel a ticket~~")
    boardingPassCancel = input('Please enter boarding pass number here: ')
    os.remove(
        'C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/' + boardingPassCancel)
    print('Done! Ticket ' + boardingPassCancel + ' has been cancelled')
    exit()
else:
    print('Sorry command not available. Try Again')
    exit()
