import datetime
import random

timeValidator = datetime.date.today()

boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

# P(0)

print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter Passenger 1's name: ")
DOB = (input("Enter Passenger 1's Date of Birth in dd/mm/yyyy format: "))
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

# P(2)

print("PASSENGER 2: ")

print('Enter THE DETAILS CAREFULLY')
passenger2 = input("\nEnter Passenger 2's name: ")
DOB2 = (input("Enter Passenger 2's DOB in dd/mm/yyyy format: "))
validDOB = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()

if validDOB >= timeValidator.today():
    print("Cannot choose a date in the future, -", DOB, "\n\nPlease try again//\n")
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

# P(3)

print("PASSENGER 2: ")

print('Enter THE DETAILS CAREFULLY')
P2 = input("\nEnter Passenger 2's name: ")
DOB2 = (input("Enter Passenger 2's DOB in dd/mm/yyyy format: "))
validDOB = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()

if validDOB >= timeValidator.today():
    print("Cannot choose a date in the future, -", DOB, "Please try again..\n")
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
travelDate = (input("Enter departure date in dd/mm/yyyy format "))
travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()
if travelValidation >= timeValidator.today():
    pass
else:
    print("Cannot choose a date in the past, -", travelDate + '\n')
    travelDate = (input("Enter departure date in dd/mm/yyyy format: "))
    travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()
    if travelValidation >= timeValidator.today():
        pass
    else:
        print('\n' + 'Sorry, date invalid, date cannot be in the past')
        print('Please restart and try again')
        exit()
##############################
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19,\n we suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now Enter your Departure Location below")
departureCountry = input("Departing Country?: " + '\n')
departureCity = input("Departing City?: " + '\n')

print("Now Enter your Arrival Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")

if str(departureCountry) != str(destinationCountry):
    # Passenger 1
    passport1 = input("Enter Passenger 1's Passport Number: ")
    passportExp1 = (input("Enter expiration date of passport [in dd/mm/yyyy format]: "))
    passportExpValidation = datetime.datetime.strptime(passportExp1, "%d/%m/%Y").date()
    if passportExpValidation > timeValidator.today():
        pass
    else:
        print('Please Enter N or n if you have to renew your passport')
        choice = input("Do you have to renew your passport? [Y or N]")
        if choice == 'Y' or 'y':
            print('Okay')
            exit()
        else:
            pass
        passportExp1 = (input("Expiry date of passport [dd/mm/yyyy]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp1, "%d/%m/%Y").date()
        if passportExpValidation <= timeValidator.today():
            print('\n' + 'Sorry, date invalid, date cannot be in the past', passportExp1)
            print('You might want to consider renewing the passport - ', passport1)
            print('Please restart and try again')
            exit()
    # Passenger 2
    passport2 = input("Enter Passenger 2's Passport Number: ")
    passportExp2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
    if passportExpValidation > timeValidator.today():
        pass
    else:
        print('Please Enter N or n if you have to renew your passport')
        choice = input('Do you have to renew your passport? [Y or N]: ')
        if choice == 'Y' or 'y':
            print('Okay')
            exit()
        else:
            pass
        print('\n' + "Please Enter correctly this time or else you will be exited..")
        passportExp2 = (input("Expiry date of passport [dd/mm/yyyy]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
        if passportExpValidation > timeValidator.today():
            pass
        else:
            print('\n' + 'Sorry, date invalid, date cannot be in the past', passportExpValidation)
            print('You might want to consider renewing the passport - ', passport2)
            print('Please restart and try again')
            exit()
    # Passenger 3
    passport3 = input("Enter Passenger 3's Passport Number: ")
    passportExp3 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    passportExpValidation = datetime.datetime.strptime(passportExp3, "%d/%m/%Y").date()
    if passportExpValidation > timeValidator.today():
        pass
    else:
        print('Please Enter N or n if you have to renew your passport')
        choice = input('Do you have to renew your passport? [Y or N]: ')
        if choice == 'Y' or 'y':
            print('Okay')
            exit()
        else:
            pass
        print('\n' + "Please Enter correctly this time or else you will be exited..")
        passportExp3 = (input("Expiry date of passport [dd/mm/yyyy]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp3, "%d/%m/%Y").date()
        if passportExpValidation > timeValidator.today():
            pass
        else:
            print('\n' + 'Sorry, date invalid, date cannot be in the past', passportExpValidation)
            print('You might want to consider renewing the passport - ', passport3)
            print('Please restart and try again')
            exit()

    import airline_Timing

    import payment

    print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen))
    f = open("\nC:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf" + 'AX' + str(boardGen), 'a+')
    f.write('PASSENGER 1- ' + '\n')
    f.write(
        'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + passport1 + '\n' 'Expiry Date : ' + passportExp1 + '\n')
    f.write('\nPASSENGER 2- ' + '\n')
    f.write(
        'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' 'Passport Number: ' + passport2 + '\n' 'Expiry Date : ' + passportExp2 + '\n')
    f.write('\nPASSENGER 3- ')
    f.write(
        'Name: ' + P2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' 'Passport Number: ' + passport3 + '\n' 'Expiry Date : ' + passportExp3 + '\n')
    f.write('Your Journey is on: ' + travelDate + '\n')
    f.write('Airline: ' + airline_Timing.airline + ' | ' + 'Aircraft Number: ' + str(flightGen)+ '|')
    f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
    f.write(payment.paid)
    f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
    f.close()
    exit()
else:
    pass

import airline_Timing
import payment

print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen))
f = open("\nC:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf" + 'AX' + str(boardGen), 'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n')
f.write('\nPASSENGER 2: ' + '\n')
f.write(
    'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n')
# for person 3
f.write('\nPASSENGER 3: ' + '\n')
f.write(
    'Name: ' + P2 + '\n' + 'Date of Birth: ' + DOB2)
f.write('Your Journey is on: ' + travelDate + '\n')
f.write('Airline: ' + airline_Timing.airline + ' | ' + 'Aircraft Number: ' + str(flightGen)+ '|')
f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
f.write(payment.paid)
f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
f.close()
exit()
