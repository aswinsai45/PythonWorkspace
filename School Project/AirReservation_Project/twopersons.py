import datetime
import random

# Date and Time management
timeValidator = datetime.date.today()

# Random integer boardGenerator for Boarding Pass
boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

# Passenger 1
print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter Passenger 1's name: ")
while True:
    DOB = (input("Enter Passenger 1's Date of Birth in dd/mm/yyyy format: "))
    validDOB = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()
    if validDOB >= timeValidator.today():
        print("\nCannot choose a date in the future, -", DOB, "Please try again..\n")
    else:
        break

# Passenger 2
print("PASSENGER 2: ")

passenger2 = input("\nEnter Passenger 2's name: ")
while True:
    DOB2 = (input("Enter Passenger 2's Date of Birth in dd/mm/yyyy format: "))
    validDOB = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()
    if validDOB >= timeValidator.today():
        print("\nCannot choose a date in the future, -", DOB2, "Please try again..\n")
    else:
        break

print('\n DEPARTURE AND DESTINATION: ')
while True:
    travelDate = (input("Enter departure date in dd/mm/yyyy format "))
    travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()

    if travelValidation < timeValidator.today():
        print("\nCannot choose a date in the past, -", travelDate + '\n')
    else:
        break


# Departure and Arrival
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19. We suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now Enter your Departure Location below\n")
departureCountry = input("Departing Country?: ")
departureCity = input("Departing City?: " )

print("Now Enter your Arrival Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")

# If travelling to a different county, passport is needed


if str(departureCountry) != str(destinationCountry):
    passport1 = input("Enter Passenger 1's Passport Number: ")
    while True:
        passportExp1 = (input("Enter expiration date of passport [in dd/mm/yyyy format]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp1, "%d/%m/%Y").date()
        if passportExpValidation > travelValidation:
            break
        else:
            print('\nCannot choose date in the past - ', passportExp1, 'Try Again')

    # second chance for Passenger 2
    passport2 = input("Enter Passenger 2's Passport Number: ")
    while True:
        passportExp2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
        passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
        if passportExpValidation > travelValidation:
            break
        else:
            print('\n', 'Cannot choose date in the past - ', passportExp1, 'Try Again')

    import airline_Timing

    import payment

    # Print in file with passport details

    print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")
    f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(boardGen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + passport1 + '\n' 'Expiry Date : ' + passportExp1 + '\n')
    f.write('\nPASSENGER 2: ' + '\n')
    f.write(
        'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' 'Passport Number: ' + passport2 + '\n' 'Expiry Date : ' + passportExp2 + '\n')
    f.write('Airline: ' + airline_Timing.listofairlines[airline_Timing.airline] + ' | ' + 'Aircraft Number: A380X' + str(flightGen)+ '|')
    f.write('Your Journey is on: ' + travelDate + '\n')
    f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
    f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
    f.close()
    exit()

import airline_Timing

import payment

# Print in file without passport details

print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")
f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(boardGen) , 'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' + '\n')
f.write('\nPASSENGER 2: ' + '\n')
f.write(
    'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n')
f.write('Your Journey is on: ' + travelDate + '\n')
f.write('Airline: ' + airline_Timing.listofairlines[airline_Timing.airline] + ' | ' + 'Aircraft Number: A380X' + str(flightGen)+ '|')
f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
f.close()
exit()
