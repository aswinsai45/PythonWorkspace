import datetime
import random

timeValidator = datetime.date.today()

boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

# P(1)

print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter Passenger 1's name: ")
while True:
    DOB1 = (input("Enter Passenger 1's Date of Birth in dd/mm/yyyy format: "))
    validDOB = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()
    
    if validDOB >= timeValidator.today():
        print("Cannot choose a date in the future, -", DOB1, "Please try again..\n")
    else:
        break

# P(2)

print("PASSENGER 2: ")

print('Enter THE DETAILS CAREFULLY')
passenger2 = input("\nEnter Passenger 2's name: ")
while True:
    DOB2 = (input("Enter Passenger 2's DOB in dd/mm/yyyy format: "))
    validDOB = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()
    
    if validDOB >= timeValidator.today():
        print("Cannot choose a date in the future, -", DOB2, "\n\nPlease try again//\n")
    else:
        break

# P(3)

print("PASSENGER 3: ")

print('Enter THE DETAILS CAREFULLY')
passenger3 = input("\nEnter Passenger 3's name: ")
while True:
    DOB3 = (input("Enter Passenger 3's DOB in dd/mm/yyyy format: "))
    validDOB = datetime.datetime.strptime(DOB3, "%d/%m/%Y").date()

    if validDOB >= timeValidator.today():
        print("Cannot choose a date in the future, -", DOB3, "Please try again..\n")
    else:
        break

print('\n DEPARTURE AND DESTINATION: ')
travelDate = (input("Enter departure date in dd/mm/yyyy format "))
travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()
while True:
    if travelValidation >= timeValidator.today():
        break
    else:
        print("\nCannot choose a date in the past, -", travelDate + '\n')
##############################
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19. We suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now Enter your Departure Location below")
departureCountry = input("Departing Country?: ")
departureCity = input("Departing City?: ")

print("Now Enter your Arrival Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")

if str(departureCountry) != str(destinationCountry):
    # Passenger 1
    passport1 = input("Enter Passenger 1's Passport Number: ")
    while True:
        passportExp1 = (input("Enter expiration date of passport [in dd/mm/yyyy format]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp1, "%d/%m/%Y").date()
        if passportExpValidation > travelValidation:
            break
        else:
            print('\nCannot choose date in the past -', passportExpValidation, 'Try Again')

    # Passenger 2
    passport2 = input("Enter Passenger 2's Passport Number: ")
    while True:
        passportExp2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
        passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
        if passportExpValidation > travelValidation:
            break
        else:
            print('\nCannot choose date in the past -', passportExpValidation, 'Try Again')
    # Passenger 3
    passport3 = input("Enter Passenger 3's Passport Number: ")
    while True:
        passportExp3 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
        passportExpValidation = datetime.datetime.strptime(passportExp3, "%d/%m/%Y").date()
        if passportExpValidation > travelValidation:
            break
        else:
            print('\nCannot choose date in the past -', passportExpValidation, 'Try Again')

    import airline_Timing

    import payment

    print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")
    f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(boardGen), 'a+')
    f.write('PASSENGER 1- ' + '\n')
    f.write(
        'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB1 + '\n' 'Passport Number: ' + passport1 + '\n' 'Expiry Date : ' + passportExp1 + '\n')
    f.write('\nPASSENGER 2- ' + '\n')
    f.write(
        'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' 'Passport Number: ' + passport2 + '\n' 'Expiry Date : ' + passportExp2 + '\n')
    f.write('\nPASSENGER 3- ')
    f.write(
        'Name: ' + passenger3 + '\n' + 'Date of Birth: ' + DOB3 + '\n' 'Passport Number: ' + passport3 + '\n' 'Expiry Date : ' + passportExp3 + '\n')
    f.write('Your Journey is on: ' + travelDate + '\n')
    f.write('Airline: ' + airline_Timing.listofairlines[airline_Timing.airline] + ' | ' + 'Aircraft Number: A380X' + str(flightGen)+ '|')
    f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')
    
    f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
    f.close()
    exit()

else:
    pass

import airline_Timing
import payment

print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")
f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(boardGen), 'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB1 + '\n')
f.write('\nPASSENGER 2: ' + '\n')
f.write(
    'Name: ' + passenger2 + '\n' + 'Date of Birth: ' + DOB2 + '\n')
# for person 3
f.write('\nPASSENGER 3: ' + '\n')
f.write(
    'Name: ' + passenger3 + '\n' + 'Date of Birth: ' + DOB3)
f.write('Your Journey is on: ' + travelDate + '\n')
f.write('Airline: ' + airline_Timing.listofairlines[airline_Timing.airline] + ' | ' + 'Aircraft Number: A380X' + str(flightGen)+ '|')
f.write('\nDeparture: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')

f.write("\nYour Boarding Pass Number is AX" + str(boardGen))
f.close()
exit()
