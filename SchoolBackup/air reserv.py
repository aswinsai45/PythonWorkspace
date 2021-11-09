import datetime
import random

titrd = datetime.date.today()

print("Welcome to Aires Booking")
ch = int(input("Enter the number of passengers travelling "))

if ch == 1:
    gen = random.randint(2000, 9000)
    print('Enter your details')
    P0 = input("enter your name: ")
    DOB = (input("enter your Date of Birth in dd/mm/yyyy format: "))
    dobd = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()
    if dobd > titrd.today():
        print("DOB cannot be selected in the future, you have chose ", DOB)
        exit()
    else:
        pass
    TrDate = (input("enter departure date in dd/mm/yyyy format "))
    trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
    if trdated >= titrd.today():
        pass
    else:
        print("Cannot choose a date in the past", TrDate)
        exit()

    pno = input("Enter your Passport Number: ")
    pnex = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex, "%d/%m/%Y").date()
    if pnext >= titrd.today():
        pass
    else:
        print("Renew your passport and try again")
        exit()
    # departure and destinations
    print("Available Departure and Destination Locations are: " '\n' + '1. USA' + '\n' + '2. Canada' + '\n' + '3. '
                                                                                                              'Mexico' + '\n' + '4. UK' + '\n' + '5. India' + '\n')
    print('Departure/Arrival to limited countries due to Covid -19,\nwe suggest checking travel guidelines of the '
          'country you will be travelling to before booking your ticket')
    li0 = [1, 2, 3, 4, 5]
    dep = input('Where are you departing from?')
    if dep not in li0:
        print('Choose a valid country number of the country you wish to travel')
    else:
        pass
    dest = input('Where do you wish to travel?: ')
    if dest not in li0:
        print('Choose a valid country number of the country you wish to travel')
    else:
        pass
    f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + str(gen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + P0 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + pno + '\n' 'Expiry Date : ' + pnex + '\n')
    f.write('Your Journey is on: ' + TrDate + '\n')
    f.write('Departure: ' + dep + '|' + 'Destination: ' + dest)
    f.write("Your Boarding Pass Number is AX" + str(gen) + '\n')
    f.close()
    exit()
############# if CH2
if ch == 2:
    gen = random.randint(2000, 9000)
    P1 = input("Enter Name of Passenger 1: ")
    DOB1 = (input("enter your Date of Birth in dd/mm/yyyy format "))
    dobd = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()
    if dobd > titrd.today():
        print("DOB cannot be selected, you have chose ", DOB1)
        exit()
    else:
        pass
    TrDate = (input("enter departure date in dd/mm/yy format "))
    trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
    if trdated >= titrd.today():
        pass
    else:
        print("Cannot choose date", trdated)
        exit()

    pno1 = input("Enter your Passport Number: ")
    pnex1 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex1, "%d/%m/%Y").date()
    if pnext >= titrd.today():
        pass
    else:
        print("Renew your passport and try again")
        exit()
    # P2 CH2
    P2 = input("Enter Name of Passenger 2: ")
    DOB2 = (input("enter your Date of Birth in dd/mm/yyyy format "))
    dobd = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()
    if dobd > titrd.today():
        print("DOB cannot be selected, you have chose ", DOB2)
        exit()
    else:
        pass
    TrDate = (input("enter departure date in dd/mm/yy format "))
    trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
    if trdated >= titrd.today():
        pass
    else:
        print("Cannot choose date", trdated)
        exit()

    pno2 = input("Enter your Passport Number: ")
    pnex2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex2, "%d/%m/%Y").date()
    if pnext >= titrd.today():
        pass
    else:
        print("Renew your passport and try again")
        exit()
    f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + str(gen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(P1 + '\n' + DOB1 + '\n' + pno1 + '\n' + pnex1 + '\n')
    f.write('PASSENGER 2: ' + '\n')
    f.write(
        P2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' + 'Passport Number: ' + pno2 + '\n' + 'Expiry Date: ' + pnex2 + '\n')
    f.write('\n' + 'Travel Info: ')
    f.write('Journey Date: ' + TrDate + '\n')
    f.write("Your Boarding Pass Number is AX" + str(gen))
    f.close()