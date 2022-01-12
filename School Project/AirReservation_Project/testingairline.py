import datetime
import random

listofairlines = ['Air India', 'United Airlines', 'Emirates', 'Etihad Airways', 'Qatar Airways']
airline = input("Enter your desired Airline's name here: ")
if airline in listofairlines:
    pass
else:
    print("Airline Unavailable/Incorrect. Please try again" + '\n')
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

print('\nYou have chose this airline - ', airline)
print('The available times of flights are: -')
randh = random.randint(1, 23)
randm = random.randint(0, 59)
ti = datetime.time(randh, randm, 0)
print(str(ti))

randh1 = random.randint(1, 23)
randm1 = random.randint(0, 59)
ti1 = datetime.time(randh1, randm1, 0)
print(str(ti1))

randh2 = random.randint(1, 23)
randm2 = random.randint(0, 59)
ti2 = datetime.time(randh2, randm2, 0)
print(str(ti2))

fltime = input('Type in any of the time shown above to book your flight: ')

times = (str(ti), str(ti1), str(ti2))

if fltime in times:
    var = ('You have chose the time - ', fltime)
    var1 = ('Your flight will now be booked with', airline + 'on' + fltime)
else:
    flch = input('Sorry, time not available.. Do you want to try again?[Y or N]: ')
    if flch == 'Y' or 'y':
        print('INCORRECT INPUTS WILL NOW BE EXITED')
        randh = random.randint(1, 23)
        randm = random.randint(0, 59)
        ti = datetime.time(randh, randm, 0)
        print(str(ti))

        randh1 = random.randint(1, 23)
        randm1 = random.randint(0, 59)
        ti1 = datetime.time(randh1, randm1, 0)
        print(str(ti1))

        randh2 = random.randint(1, 23)
        randm2 = random.randint(0, 59)
        ti2 = datetime.time(randh2, randm2, 0)
        print(str(ti2))

        fltime = input('Type in any of the time shown above to book your flight: ')

        times = (str(ti), str(ti1), str(ti2))

        if fltime in times:
            print('You have chose the time - ', fltime)
            print('Your flight will now be booked with', airline + 'on' + fltime)
        else:
            print('Sorry, incorrect format, please restart')
            exit()
    elif flch == 'N' or 'n':
        print('Okay, you will now be exited')
        exit()

# VAR AND VAR 1 ARE TIME AND AIRLINE