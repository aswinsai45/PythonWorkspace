import os.path
import shutil

print("Welcome to FlightBook")

action = input('What would you like to do?\n 1. Book a ticket\n 2. Retrieve a ticket\n 3. Cancel a ticket?\n '
               'Available commands are "book", "cancel", "retrieve": ')

# Showing available commands

# retrieves a ticket
if action == str('retrieve'):
    boardingPass = input('Enter boarding pass number here: ')
    file_exist = os.path.exists('C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/' + boardingPass)
    if file_exist:
        pass
    else:
        print('Booking Cancelled/Not Found')
        exit()

    file = open('C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/' + boardingPass, 'r')
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

    shutil.move('C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/' + boardingPassCancel, 'C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/Cancelled')
    print('Done! Ticket ' + boardingPassCancel + ' has been cancelled')
    exit()
elif print('Sorry command not available'):
    exit()
