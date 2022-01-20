import datetime
import random

# Date and Time management
timeValidator = datetime.date.today()

# Random integer boardGenerator for Boarding Pass
boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

# Passenger 1
print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nenter Passenger 1's name: ")
DOB = (input("enter Passenger 1's Date of Birth [dd/mm/yyyy]: "))
validDOB = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()

if validDOB >= timeValidator.today():
    print("Cannot choose a date in the future, -", DOB, "| Please try again..\n")
    print("\nEnter the date correctly this time, or else you will be exited// ")
    DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
    validDOB = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()
    if validDOB < timeValidator.today():
        pass
    else:
        print("Cannot choose a date in the future, -", DOB)
        print("Sorry, please restart and try again//")
        exit()
else:
    pass

# Passenger 2
print("PASSENGER 2: ")

timeValidator = datetime.date.today()

print('ENTER THE DETAILS CAREFULLY')
passenger2 = input("\nEnter Passenger 2's name: ")
DOB2 = (input("enter Passenger 2's DOB in dd/mm/yyyy format: "))
validDOB = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()

if validDOB >= timeValidator.today():
    print("Cannot choose a date in the future, -", DOB, "| Please try again..\n")
    print("\nEnter the date correctly this time, or else you will be exited// ")
    DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
    validDOB = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()
    if validDOB < timeValidator.today():
        pass
    else:
        print("Cannot choose a date in the future, -", DOB2)
        print("Sorry, please restart and try again//")
        exit()
else:
    pass

print('\n DEPARTURE AND DESTINATION: ')
travelDate = (input("enter departure date in dd/mm/yyyy format "))
travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()
if travelValidation >= timeValidator.today():
    pass
else:
    print("Cannot choose a date in the past, -", travelDate + '\n')
    travelDate = (input("enter departure date in dd/mm/yyyy format: "))
    travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()
    if travelValidation >= timeValidator.today():
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
departureCountry = input("Departing Country?: " + '\n')
departureCity = input("Departing City?: " + '\n')

print("Now enter your Arrival Location below\n")
destinationCountry = input("Destination Country?: " + '\n')
destinationCity = input("Destination City?: " + '\n')

# If travelling to a different county, passport is needed


if str(departureCountry) != str(destinationCountry):
    passport1 = input("Enter Passenger 1's Passport Number: ")
    passportExp1 = (input("Enter expiration date of passport [in dd/mm/yyyy format]: "))
    passportExpValidation = datetime.datetime.strptime(passportExp1, "%d/%m/%Y").date()
    if passportExpValidation > travelValidation:
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
        passportExp1 = (input("Expiry date of passport [dd/mm/yyyy]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp1, "%d/%m/%Y").date()
        if passportExpValidation > timeValidator.today():
            pass
        else:
            print('\n' + 'Sorry, date invalid, date cannot be in the past', passportExpValidation)
            print('You might want to consider renewing the passport - ', passport1)
            print('Please restart and try again')
            exit()
    # second chance for Passenger 2
    passport2 = input("Enter Passenger 2's Passport Number: ")
    passportExp2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
    if passportExpValidation > timeValidator.today():
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
        passportExp2 = (input("Expiry date of passport [dd/mm/yyyy]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
        if passportExpValidation > timeValidator.today():
            pass
        else:
            print('\n' + 'Sorry, date invalid, date cannot be in the past', passportExpValidation)
            print('You might want to consider renewing the passport - ', passport2)
            print('Please restart and try again')
            exit()
    print(
            "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

    import testingairline

    import Payment

    # Print in file with passport details

    print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen))
<<<<<<< HEAD
    f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets" + 'AX' + str(boardGen), 'w')
=======
    f = open("C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/" + 'AX' + str(boardGen), 'w')
>>>>>>> 88746f8df7976d65c370e918b5c3fcf90128382f
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + passport1 + '\n' 'Expiry Date : ' + passportExp1 + '\n')
    f.write('\nPASSENGER 2: ' + '\n')
    f.write(
        'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' 'Passport Number: ' + passport2 + '\n' 'Expiry Date : ' + passportExp2 + '\n')
    f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + str(flightGen))
    f.write('Your Journey is on: ' + travelDate + '\n')
    f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
    f.write(Payment.paid)
    f.write("\nYour Boarding Pass Number is AX" + str(boardGen) )
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

print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen))
<<<<<<< HEAD
f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets" + 'AX' + str(boardGen) , 'w')
=======
f = open("C:/Users/aswin/PycharmProjects/PythonWorkspace/SchoolBackup/BookingConf/" + 'AX' + str(boardGen) , 'w')
>>>>>>> 88746f8df7976d65c370e918b5c3fcf90128382f
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' + '\n')
f.write('\nPASSENGER 2: ' + '\n')
f.write(
    'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n')
f.write('Your Journey is on: ' + travelDate + '\n')
f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + str(flightGen))
f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
f.write(Payment.paid)
f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
f.close()
exit()
