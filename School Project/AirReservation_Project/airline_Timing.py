import datetime
import random

listofairlines = {1: 'Air India', 2: 'United Airlines', 3: 'Emirates', 4: 'Etihad Airways', 5: 'Qatar Airways',
                  6: 'IndiGo', 7: 'SpiceJet',
                  8: 'Vistara Airlines'}

print('The available airlines are: ', '\n', listofairlines)

airline = int(input("Enter airline Index: "))

print('You have chose: ' + listofairlines[airline])

if airline in listofairlines.keys():
    pass
else:
    print("Airline Unavailable/Incorrect. Please try again" + '\n')
    print("Now choose your desired Airline correctly this time or else you will be exited..")
    print('The available airlines are: ', '\n', listofairlines)
    airline = input("Enter your desired Airline's name here: ")
    if airline in listofairlines.keys():
        pass
    else:
        print("Sorry, Incorrect again. Please restart and try again")
        exit()

print('\nYou have chose this airline - ', airline)
print('The available times of flights are: -')
randh = random.randint(1, 23)
randm = random.randint(0, 59)
ti0 = datetime.time(randh, randm, 0)

randh1 = random.randint(1, 23)
randm1 = random.randint(0, 59)
ti1 = datetime.time(randh1, randm1, 0)

randh2 = random.randint(1, 23)
randm2 = random.randint(0, 59)
ti2 = datetime.time(randh2, randm2, 0)

# fltime = input('Type in any of the time shown above to book your flight: ')
times = {1: str(ti0), 2: str(ti1), 3: str(ti2)}

print(times)

print('Type in any of the time shown above to book your flight: ')

# fltime = input(('Enter 1 for: ' + str(ti0) + 'Enter 2 for :' + str(ti2) + 'Enter 3 for: ' + str(ti2)) + ":~")

userEnter = int(input("Enter the index: "))

listTime = times[userEnter]

print(listTime)

if userEnter in times.keys():
    print('You have chose the time - ', listTime)
    print('Your flight will now be booked with', listofairlines[airline])
else:
    flch = input('Sorry, time not available.. Do you want to try again?[Y or N]: ')
    if flch == 'Y' or 'y':
        print('INCORRECT INPUTS WILL NOW BE EXITED')

        # fltime = input('Type in any of the time shown above to book your flight: ')

        print(times)
        listTime = int(input("Enter the index: "))

        if userEnter in times.keys():
            print('You have chose the time - ', listTime)
            print('Your flight will now be booked with', listofairlines[airline])
        else:
            print('Sorry, input incorrect, please restart')
            exit()
    elif flch == 'N' or 'n':
        print('Okay, you will now be exited')
        exit()

# # VAR AND VAR 1 ARE TIME AND AIRLINE
