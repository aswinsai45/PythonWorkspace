import datetime
import random

titrd = datetime.date.today()

gen = random.randint(2000, 9000)
randf = random.randint(22523, 92527)

# P(0)

print('ENTER the DETAILS CAREFULLY')
P0 = input("\nEnter Passenger 1's name: ")
DOB = (input("Enter Passenger 1's Date of Birth in dd/mm/yyyy format: "))
dobd = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()

if dobd >= titrd.today():
    print("Cannot choose a date in the future, -", DOB, "\n\nPlease try again//\n")
    chdob = input("Do you want to try again? [Enter Y or N]: ")
    if chdob == 'Y' or 'y':
        print("\nEnter the date correctly this time, or else you will be exited// ")
        DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
        dobd = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()
        if dobd < titrd.today():
            pass
        else:
            print("Cannot choose a date in the future, -", DOB)
            print("Sorry, please restart and try again//")
            exit()
    elif chdob == 'N' or 'n':
        print('Okay, you will now be exited out of the program')
        exit()

else:
    pass

# P(2)

print("PASSENGER 2: ")

print('ENTER THE DETAILS CAREFULLY')
P1 = input("\nEnter Passenger 2's name: ")
DOB1 = (input("enter Passenger 2's DOB in dd/mm/yyyy format: "))
dobd = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()

if dobd >= titrd.today():
    print("Cannot choose a date in the future, -", DOB, "\n\nPlease try again//\n")
    chdob = input("Do you want to try again? [Enter Y or N]: ")
    if chdob == 'Y' or 'y':
        print("\nEnter the date correctly this time, or else you will be exited// ")
        DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
        dobd = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()
        if dobd < titrd.today():
            pass
        else:
            print("Cannot choose a date in the future, -", DOB1)
            print("Sorry, please restart and try again//")
            exit()
    elif chdob == 'N' or 'n':
        print('Okay, you will now be exited out of the program')
        exit()

else:
    pass

# P(3)

print("PASSENGER 2: ")

print('ENTER THE DETAILS CAREFULLY')
P2 = input("\nEnter Passenger 2's name: ")
DOB2 = (input("enter Passenger 2's DOB in dd/mm/yyyy format: "))
dobd = datetime.datetime.strptime(DOB2, "%d/%m/%Y").date()

if dobd >= titrd.today():
    print("Cannot choose a date in the future, -", DOB, "\n\nPlease try again//\n")
    chdob = input("Do you want to try again? [Enter Y or N]: ")
    if chdob == 'Y' or 'y':
        print("\nEnter the date correctly this time, or else you will be exited// ")
        DOB = input("Enter Date of Birth in dd/mm/yyyy format: ")
        dobd = datetime.datetime.strptime(DOB1, "%d/%m/%Y").date()
        if dobd < titrd.today():
            pass
        else:
            print("Cannot choose a date in the future, -", DOB1)
            print("Sorry, please restart and try again//")
            exit()
    elif chdob == 'N' or 'n':
        print('Okay, you will now be exited out of the program')
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
    chtr = input("Do you want to try try again? [Enter Y or N]: ")
    if chtr == 'Y' or 'y':
        TrDate = (input("enter departure date in dd/mm/yyyy format: "))
        trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
        if trdated >= titrd.today():
            pass
        else:
            print('\n' + 'Sorry, date invalid, date cannot be in the past')
            print('Please restart and try again')
            exit()
    elif chtr == 'N' or 'n':
        print('Okay, you will now be exited out of the program')
        exit()

##############################
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19,\n we suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now enter your Departure Location below")
depco = input("Departing Country?: " + '\n')
depci = input("Departing City?: " + '\n')

print("Now enter your Arrival Location below\n")
destco = input("Destination Country?: ")
destci = input("Destination City?: ")

if str(depco) != str(destco):
    # Passenger 1
    pno = input("Enter Passenger 1's Passport Number: ")
    pnex = (input("Enter expiration date of passport [in dd/mm/yyyy format]: "))
    pnext = datetime.datetime.strptime(pnex, "%d/%m/%Y").date()
    if pnext > titrd.today():
        pass
    else:
        print('Please enter N or n if you have to renew your passport')
        chyn = input("\n" + "Invalid date/format. Date cannot be in the past, do you want to try again? [Y or N]")
        if chyn == 'Y' or 'y':
            print('\n' + "Please enter correctly this time or else you will be exited..")
            pnex = (input("Expiry date of passport [dd/mm/yyyy]: "))
            pnext = datetime.datetime.strptime(pnex, "%d/%m/%Y").date()
            if pnext > titrd.today():
                pass
            else:
                print('\n' + 'Sorry, date invalid, date cannot be in the past', pnex)
                print('Please restart and try again')
                print('You might want to consider renewing the passport - ', pno)
                exit()
        if chyn == 'N' or 'n':
            print('Okay, you will now be exited out of the program')
            exit()

    # Passenger 2
    pno1 = input("Enter Passenger 2's Passport Number: ")
    pnex1 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex1, "%d/%m/%Y").date()
    if pnext > titrd.today():
        pass
    else:
        print('Please enter N or n if you have to renew your passport')
        chyn = input("\n" + "Invalid date/format. Date cannot be in the past, do you want to try again? [Y or N]")
        if chyn == 'Y' or 'y':
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
        if chyn == 'N' or 'n':
            print('Okay, you will now be exited out of the program')
            exit()

    # Passenger 3
    pno2 = input("Enter Passenger 3's Passport Number: ")
    pnex2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex2, "%d/%m/%Y").date()
    if pnext > titrd.today():
        pass
    else:
        print('Please enter N or n if you have to renew your passport')
        chyn = input("\n" + "Invalid date/format. Date cannot be in the past, do you want to try again? [Y or N]")
        if chyn == 'Y' or 'y':
            print('\n' + "Please enter correctly this time or else you will be exited..")
            pnex2 = (input("Expiry date of passport [dd/mm/yyyy]: "))
            pnext = datetime.datetime.strptime(pnex2, "%d/%m/%Y").date()
            if pnext > titrd.today():
                pass
            else:
                print('\n' + 'Sorry, date invalid, date cannot be in the past', pnex)
                print('You might want to consider renewing the passport - ', pno2)
                print('Please restart and try again')
                exit()
        if chyn == 'N' or 'n':
            print('Okay, you will now be exited out of the program')
            exit()

    print(
        "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

    import testingairline

    print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(gen))
    f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + 'AX' + str(gen), 'a+')
    f.write('PASSENGER 1- ' + '\n')
    f.write(
        'Name: ' + P0 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + pno + '\n' 'Expiry Date : ' + pnex + '\n')
    f.write('\nPASSENGER 2- ' + '\n')
    f.write(
        'Name: ' + P1 + '\n' + 'Date of Birth: ' + DOB1 + '\n' 'Passport Number: ' + pno1 + '\n' 'Expiry Date : ' + pnex1 + '\n')
    f.write('\nPASSENGER 3- ')
    f.write(
        'Name: ' + P2 + '\n' + 'Date of Birth: ' + DOB2 + '\n' 'Passport Number: ' + pno2 + '\n' 'Expiry Date : ' + pnex2 + '\n')
    f.write('Your Journey is on: ' + TrDate + '\n')
    f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + randf)
    f.write('\nDeparture: ' + depci + ', ' + depco + '  |  ' + 'Destination: ' + destci + ', ' + destco + '\n')
    f.write("\nYour Boarding Pass Number is AX" + str(gen) + '\n')
    f.close()
    exit()
else:
    pass
print(
    "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

import testingairline

print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(gen))
f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + 'AX' + str(gen), 'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + P0 + '\n' + 'Date of Birth: ' + DOB + '\n')
f.write('\nPASSENGER 2: ' + '\n')
f.write(
    'Name: ' + P1 + '\n' + 'Date of Birth: ' + DOB1 + '\n')
# for person 3
f.write('\nPASSENGER 3: ' + '\n')
f.write(
    'Name: ' + P2 + '\n' + 'Date of Birth: ' + DOB2)
f.write('Your Journey is on: ' + TrDate + '\n')
f.write('Airline: ' + testingairline.airline + ' | ' + 'Aircraft Number: ' + randf)
f.write('\nDeparture: ' + depci + ', ' + depco + '  |  ' + 'Destination: ' + destci + ', ' + destco + '\n')
f.write("\nYour Boarding Pass Number is AX" + str(gen) + '\n')
f.close()
exit()
