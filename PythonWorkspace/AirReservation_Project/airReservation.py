import os.path
import shutil

print("Welcome to FlightBook")

action = input('What would you like to do?\n 1. Book a ticket\n 2. Retrieve a ticket\n 3. Cancel a ticket?\n '
               'Available commands are "book", "cancel", "retrieve": ')

# Showing available commands

# retrieves a ticket
if action == str('retrieve'):
    boardingPass = input('Enter boarding pass number here: ')
<<<<<<< HEAD
    file_exist = os.path.exists('C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets' + boardingPass)
=======
    file_exist = os.path.exists('C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/' + boardingPass)
>>>>>>> 88746f8df7976d65c370e918b5c3fcf90128382f
    if file_exist:
        pass
    else:
        print('Booking Cancelled/Not Found')
        exit()

<<<<<<< HEAD
    file = open('C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets' + boardingPass, 'r')
=======
    file = open('C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/' + boardingPass, 'r')
>>>>>>> 88746f8df7976d65c370e918b5c3fcf90128382f
    s = file.read()
    print(s)

# Books a Ticket
elif action == str('book'):
    pass
    ch = int(input("\nEnter the number of people travelling [up-to 3]: "))
    if ch == 1:
        import singleperson
    elif ch == 2:
        import twopersons
    elif ch == 3:
        import threepersons
    elif ch > 3:
        print("Sorry unavailable as of now. Thanks for understanding!")
        exit()

# Moves a ticket to a cancelled folder
elif action == str('cancel'):
    boardingPassCancel = input('Please enter boarding pass number here: ')

<<<<<<< HEAD
    shutil.move('C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets' + boardingPassCancel, 'C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/CancelledTickets')
=======
    shutil.move('C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/' + boardingPassCancel, 'C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/Cancelled')
>>>>>>> 88746f8df7976d65c370e918b5c3fcf90128382f
    print('Done! Ticket ' + boardingPassCancel + ' has been cancelled')
    exit()
elif print('Sorry command not available'):
    exit()
