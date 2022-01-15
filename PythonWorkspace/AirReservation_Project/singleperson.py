import datetime
import random

timeValidator = datetime.date.today()

boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nenter your name: ")
DOB = (input("enter your Date of Birth in dd/mm/yyyy format: "))
validDOB = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()

if validDOB >= timeValidator.today():
    print("Cannot choose a date in the future, -", DOB, "Please try again..\n")
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

    # departure and destinations
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19,\n we suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now enter your Departure Location below\n")
departureCountry = input("Departing Country?: ")
departureCity = input("Departing City?: ")

print("Now enter your Arrival Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")

if str(departureCountry) != str(destinationCountry):
    passportNumber = input("Enter your Passport Number: ")
    passportExpiry = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    passportExpValidation = datetime.datetime.strptime(passportExpiry, "%d/%m/%Y").date()
    if passportExpValidation > travelValidation:
        pass
    else:
        choice = input('Do you have to renew your passport? [Y or N]: ')
        if choice == 'Y' or 'y':
            print('Okay')
            exit()
        else:
            pass
        print('\n' + "Please enter correctly this time or else you will be exited..")
        passportExpiry = (input("Expiry date of passport [dd/mm/yyyy]: "))
        passportExpValidation = datetime.datetime.strptime(passportExpiry, "%d/%m/%Y").date()
        if passportExpValidation > timeValidator.today():
            pass
        else:
            print('\n' + 'Sorry, date invalid, date cannot be in the past', passportExpValidation)
            print('You might want to consider renewing the passport - ', passportNumber)
            print('Please restart and try again')
            exit()
    print(
        "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

    import testingairline

    import Payment

    print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen))
    f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets" + 'AX' + str(boardGen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + passportNumber + '\n' 'Expiry Date : ' + passportExpiry + '\n')
    f.write('Your Journey is on: ' + travelDate + '\n')
    f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + str(flightGen))
    f.write('Departure: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
    f.write(Payment.paid)
    f.write("Your Boarding Pass Number is AX" + str(boardGen) )
    f.close()
    exit()
else:
    pass

print("1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

import testingairline

import Payment

print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen))
f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/ConfirmedTickets" + 'AX' + str(boardGen) , 'w')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' )
f.write('Your Journey is on: ' + travelDate + '\n')
f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + str(flightGen))
f.write('Departure: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
f.write(str(Payment.paid))
f.write("Your Boarding Pass Number is AX" + str(boardGen) )
f.close()
exit()
