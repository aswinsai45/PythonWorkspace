import datetime
import random

# Date and Time management
titrd = datetime.date.today()

# Random integer generator for Boarding Pass
gen = random.randint(2000, 9000)
randf = random.randint(22523, 92527)

# Passenger 1
print('ENTER YOUR DETAILS CAREFULLY')
P0 = input("\nenter Passenger 1's name: ")
DOB = (input("enter Passenger 1's Date of Birth [dd/mm/yyyy]: "))
dobd = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()

if dobd >= titrd.today():
    print("Cannot choose a date in the future, -", DOB, "| Please try again..\n")
    print("\nEnter the date correctly this time, or else you will be exited// ")
    DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
    dobd = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()
    if dobd < titrd.today():
        pass
    else:
        print("Cannot choose a date in the future, -", DOB)
        print("Sorry, please restart and try again//")
        exit()
else:
    pass

# Passenger 2
print("PASSENGER 2: ")

titrd = datetime.date.today()

print('ENTER THE DETAILS CAREFULLY')
P1 = input("\nEnter Passenger 2's name: ")
DOB1 = (input("enter Passenger 2's DOB in dd/mm/yyyy format: "))
dobd = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()

if dobd >= titrd.today():
    print("Cannot choose a date in the future, -", DOB, "| Please try again..\n")
    print("\nEnter the date correctly this time, or else you will be exited// ")
    DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
    dobd = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()
    if dobd < titrd.today():
        pass
    else:
        print("Cannot choose a date in the future, -", DOB1)
        print("Sorry, please restart and try again//")
        exit()
else:
    pass

print('\n DEPARTURE AND DESTINATION: ')
TrDate = (input("enter departure date in dd/mm/yyyy format "))
trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
if trdated >= titrd.today():
    pass
else:
    print("Cannot choose a date in the past, -", TrDate + '\n')
    TrDate = (input("enter departure date in dd/mm/yyyy format: "))
    trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
    if trdated >= titrd.today():
        pass
    else:
        print('\n' + 'Sorry, date invalid, date cannot be in the past')
        print('Please restart and try again')
        exit()

# Departure and Arrival
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19,\n we suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now enter your Departure Location below\n")
depco = input("Departing Country?: " + '\n')
depci = input("Departing City?: " + '\n')

print("Now enter your Arrival Location below\n")
destco = input("Destination Country?: " + '\n')
destci = input("Destination City?: " + '\n')

# If travelling to a different county, passport is needed


if str(depco) != str(destco):
    pno = input("Enter Passenger 1's Passport Number: ")
    pnex = (input("Enter expiration date of passport [in dd/mm/yyyy format]: "))
    pnext = datetime.datetime.strptime(pnex, "%d/%m/%Y").date()
    if pnext > trdated:
        pass
    else:
        print('Please enter N or n if you have to renew your passport')
        choice = input('Do you have to renew your passport? [Y or N]: ')
        if choice == 'Y' or 'y':
            print('Okay')
            exit()
        else:
            pass
            print('\n' + "Please enter correctly this time or else you will be exited..")
            pnex = (input("Expiry date of passport [dd/mm/yyyy]: "))
            pnext = datetime.datetime.strptime(pnex, "%d/%m/%Y").date()
            if pnext > titrd.today():
                pass
            else:
                print('\n' + 'Sorry, date invalid, date cannot be in the past', pnext)
                print('You might want to consider renewing the passport - ', pno)
                print('Please restart and try again')
                exit()
    # second chance for Passenger 2
    pno1 = input("Enter Passenger 2's Passport Number: ")
    pnex1 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex1, "%d/%m/%Y").date()
    if pnext > titrd.today():
        pass
    else:
        print('\n' + "Please enter correctly this time or else you will be exited..")
        choice = input('Do you have to renew your passport? [Y or N]: ')
        if choice == 'Y' or 'y':
            print('Okay')
            exit()
        else:
            pass
            print('\n' + "Please enter correctly this time or else you will be exited..")
            pnex1 = (input("Expiry date of passport [dd/mm/yyyy]: "))
            pnext = datetime.datetime.strptime(pnex1, "%d/%m/%Y").date()
            if pnext > titrd.today():
                pass
            else:
                print('\n' + 'Sorry, date invalid, date cannot be in the past', pnext)
                print('You might want to consider renewing the passport - ', pno1)
                print('Please restart and try again')
                exit()
    print(
            "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

    import testingairline

    import Payment

    # Print in file with passport details

    print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(gen))
    f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + 'AX' + str(gen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + P0 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + pno + '\n' 'Expiry Date : ' + pnex + '\n')
    f.write('\nPASSENGER 2: ' + '\n')
    f.write(
        'Name: ' + P1 + '\n' + 'Date of Birth: ' + DOB1 + '\n' 'Passport Number: ' + pno1 + '\n' 'Expiry Date : ' + pnex1 + '\n')
    f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + randf)
    f.write('Your Journey is on: ' + TrDate + '\n')
    f.write('\nDeparture: ' + depci + ', ' + depco + '  |  ' + 'Destination: ' + destci + ', ' + destco + '\n')
    f.write(Payment.paid)
    f.write("\nYour Boarding Pass Number is AX" + str(gen) + '\n')
    f.close()
    exit()

else:
    pass

print(
    "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

# airline selection

import testingairline

# payment options

import Payment

# Print in file without passport details

print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(gen))
f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + 'AX' + str(gen), 'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + P0 + '\n' + 'Date of Birth: ' + DOB + '\n' + '\n')
f.write('\nPASSENGER 2: ' + '\n')
f.write(
    'Name: ' + P1 + '\n' + 'Date of Birth: ' + DOB1 + '\n')
f.write('Your Journey is on: ' + TrDate + '\n')
f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + randf)
f.write('\nDeparture: ' + depci + ', ' + depco + '  |  ' + 'Destination: ' + destci + ', ' + destco + '\n')
f.write(Payment.paid)
f.write("\nYour Boarding Pass Number is AX" + str(gen) + '\n')
f.close()
exit()
