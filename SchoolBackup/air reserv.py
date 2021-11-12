import os.path
import shutil

print("Welcome to FlightBook")

action = input('What would you like to do?\n 1. Book a ticket\n 2. Retrieve a ticket\n 3. Cancel a ticket?\n '
               'Available commands are "book", "cancel", "retrieve": ')

if action == str('retrieve') and str('Retrieve'):
    bpass = input('Enter boarding pass number here: ')
    file_exist = os.path.exists('C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/' + bpass)
    if file_exist:
        pass
    else:
        print('Booking Cancelled/Not Found')
        exit()

    file = open('C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/' + bpass, 'r')
    s = file.read()
    print(s)

elif action == str('book') and str('Book'):
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

elif action == str('cancel') and str('Cancel'):
    bpassc = input('Please enter boarding pass number here: ')

    shutil.move('C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/' + bpassc, 'C:/Users/aswin/PycharmProjects'
                                                                                      '/SchoolProject/BookingConf'
                                                                                      '/Cancelled')
    print('Done! Ticket ' + bpassc + ' has been cancelled')
