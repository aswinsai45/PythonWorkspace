import datetime
import random

titrd = datetime.date.today()

print("Welcome to Aires Booking")
ch = int(input("Enter the number of passengers travelling "))

if ch == 1:
    gen = random.randint(2000, 9000)
    randf = random.randint(2252, 9252)
    print('Enter your details')
    P0 = input("enter your name: ")
    DOB = (input("enter your Date of Birth in dd/mm/yyyy format: "))
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
    pno = input("Enter your Passport Number: ")
    pnex = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    pnext = datetime.datetime.strptime(pnex, "%d/%m/%Y").date()
    if pnext > titrd.today():
        pass
    else:
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
                exit()
        if chyn == 'N' or 'n':
            print('Okay, you will now be exited out of the program')
            exit()

        # departure and destinations
    print(
        '\n' + 'Departure/Arrival to limited countries due to Covid -19,\n we suggest checking with the guidelines of '
               'the place you are travelling to\n')

    print("Now enter your Departure Location below\n")
    depco = input("Departing Country?: " + '\n')
    depci = input("Departing City?: " + '\n')

    print("Now enter your Arrival Location below\n")
    destco = input("Destination Country?: ")
    destci = input("Destination City?: ")

    print("Now choose your desired Airline" + '\n'
          "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

    listofairlines = ['Air India', 'United Airlines', 'Emirates', 'Etihad Airways', 'Qatar Airways']
    airline = input("Enter your desired Airline's name here: ")
    if airline in listofairlines:
        pass
    else:
        print("Airline Unavailable/Incorrect. Please try again"+ '\n')
        print("Now choose your desired Airline" + '\n'
                                                  "1. Air India" + '\n' + "2. United Airlines" + '\n' + "3. Emirates" + '\n' + "4. Etihad Airways" + '\n' + "5. Qatar Airways" + '\n')

        listofairlines = ['Air India', 'United Airlines', 'Emirates', 'Etihad Airways', 'Qatar Airways']
        print("Enter Airline name correctly this time or else you will be exited.." + '\n')
        airline = input("Enter your desired Airline's name here: ")
        if airline in listofairlines:
            pass
        else:
            print("Sorry, Incorrect again. Please restart and try again")
            exit()

    print("YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(gen))
    f = open("C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/" + 'AX' + str(gen), 'a+')
    f.write('PASSENGER 1: ' + '\n')
    f.write(
        'Name: ' + P0 + '\n' + 'Date of Birth: ' + DOB + '\n' 'Passport Number: ' + pno + '\n' 'Expiry Date : ' + pnex + '\n')
    f.write('Your Journey is on: ' + TrDate + '\n')
    f.write('Departure: ' + depci + ', ' + depco + '  |  ' + 'Destination: ' + destci + ', ' + destco + '\n')
    f.write("Your Boarding Pass Number is AX" + str(gen) + '\n')
    f.close()
    exit()
