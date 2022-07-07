import datetime
import random

listofairlines = {1: 'Air India', 2: 'United Airlines', 3: 'Emirates', 4: 'Etihad Airways', 5: 'Qatar Airways',
                  6: 'IndiGo', 7: 'SpiceJet',
                  8: 'Vistara Airlines'}

print('The available airlines are: ', '\n', listofairlines)

while True:
    airline = int(input("Enter airline Index: "))
    print('You have chose: ' + listofairlines[airline])
    if airline in listofairlines.keys():
        break
    else:
        print("Airline Unavailable/Incorrect. Please try again" )

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

print('Type in any of the index shown above to book your flight: ')

# fltime = input(('Enter 1 for: ' + str(ti0) + 'Enter 2 for :' + str(ti2) + 'Enter 3 for: ' + str(ti2)) + ":~")

while True:
    userEnter = int(input("Enter the index: "))
    listTime = times[userEnter]
    print(listTime)
    if userEnter in times.keys():
        print('You have chose the time - ', listTime)
        print('Your flight will now be booked with', listofairlines[airline], 'at ', listTime)
        break
    else:
        print('Sorry, time not available. Try Again. ')

