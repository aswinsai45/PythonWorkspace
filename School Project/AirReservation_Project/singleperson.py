import datetime
import random

timeValidator = datetime.date.today()

boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter your name: ")

while True:
    DOB = (input("Enter your Date of Birth in dd/mm/yyyy format: "))
    validDOB = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()
    if validDOB >= timeValidator.today():
        print("\nCannot choose a date in the future, -", DOB, "Please try again..\n")
    else:
        break

while True:
    travelDate = (input("Enter departure date in dd/mm/yyyy format "))
    travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()

    if travelValidation < timeValidator.today():
        print("\nCannot choose a date in the past, -", travelDate + '\n')
    else:
        break


# departure and destinations
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19. We suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now Enter your Departure Location below\n")
departureCountry = input("Departing Country?: ")
departureCity = input("Departing City?: ")

print("Now Enter your Arrival Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")

if str(departureCountry) != str(destinationCountry):
    passportNumber = input("Enter your Passport Number: ")
    while True:
        passportExpiry = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
        passportExpValidation = datetime.datetime.strptime(passportExpiry, "%d/%m/%Y").date()
        if passportExpValidation > timeValidator:
            break
        else:
            print('\nCannot Choose date in the past -', passportExpiry, 'Try again\n')


    import airline_Timing

    import payment

    print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")
    f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(boardGen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + passportNumber + '\n' 'Expiry Date : ' + passportExpiry + '\n')
    f.write('Your Journey is on: ' + travelDate + '\n')
    f.write('Airline: ' + airline_Timing.listofairlines[airline_Timing.airline] + ' | ' + 'Aircraft Number: A380X' + str(flightGen) + '|')
    f.write('Departure: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')

    f.write("Your Boarding Pass Number is AX" + str(boardGen))
    f.close()
    exit()

import airline_Timing
import payment

print('Generating ticket..')

print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")
f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(boardGen) , 'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + passenger1 + '\n' + 'Date of Birth: ' + DOB + '\n' )
f.write('Your Journey is on: ' + travelDate + '\n')
f.write('Airline: ' + airline_Timing.listofairlines[airline_Timing.airline] + ' | ' + 'Aircraft Number: A380X' + str(flightGen) + '|')
f.write('Departure: ' + departureCity + ', ' + departureCountry + '  |  ' + 'Destination: ' + destinationCity + ', ' + destinationCountry + '\n')

f.write("Your Boarding Pass Number is AX" + str(boardGen))
f.close()
exit()
