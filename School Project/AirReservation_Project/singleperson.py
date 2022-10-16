import datetime
import random

import mysql.connector

timeValidator = datetime.date.today()


def valid1(x):
    timeValidator = datetime.date.today()
    if x > timeValidator:
        return True
    else:
        print('Cannot choose ', x, 'Please enter date correctly')  # Travel, PassportExp


def valid2(x):
    timeValidator = datetime.date.today()
    if x < timeValidator:
        return True  # DOB
    else:
        print('Cannot choose ', x, 'Please enter date correctly')


boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter your name: ")

while True:
    DOB = (input("Enter your Date of Birth in yyyy-mm-dd format: "))
    validDOB = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
    if valid2(validDOB) == True:
        break

while True:
    travelDate = (input("Enter departure date in yyyy-mm-dd format "))
    travelValidation = datetime.datetime.strptime(travelDate, "%Y-%m-%d").date()

    if valid1(travelValidation) == True:
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

passportNumber = ''
if str(departureCountry) != str(destinationCountry):
    passportNumber = input("Enter your Passport Number: ")
    while True:
        passportExpiry = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
        passportExpValidation = datetime.datetime.strptime(passportExpiry, "%d/%m/%Y").date()
        if valid1(passportExpValidation) == True:
            break

import airline_Timing

import payment

print('Generating ticket..')
print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(boardGen), "~~~")

con = mysql.connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
cur = con.cursor()
cur.execute(
    'insert into journeydetails values ({"p1"},{"dob"},{"bpass"},{"passport"},{"airline"},{"fltime"},{"fldate"},{"flnum"}').format(
    p1= passenger1, dob=DOB, bpass=boardGen, passport=passportNumber, airline=airline_Timing.chosen,
    fltime=airline_Timing.listTime, fldate=travelDate, flnum=flightGen)
con.commit()
