import datetime
import random

listofairlines = {1: 'Air India', 2: 'United Airlines', 3: 'Emirates', 4: 'Etihad Airways', 5: 'Qatar Airways',
                  6: 'IndiGo', 7: 'SpiceJet',
                  8: 'Vistara Airlines'}

pr = ''

print('The available airlines are: ', '\n', listofairlines)

while True:
    airline = int(input("Enter airline Index: "))
    print('You have chose: ' + listofairlines[airline])
    if airline in listofairlines.keys():
        break
    else:
        print("Airline Unavailable/Incorrect. Please try again")

print('\nThe available times of flights are: ')

timelist = []
for i in range(3):
    randh = random.randint(1, 23)
    randm = random.randint(0, 59)
    ti0 = datetime.time(randh, randm, 0)

    timelist.append(str(ti0))

times = {}
k = 0
for i in timelist:
    k = k + 1
    times[k] = i

print(times)

print('\nType in any of the index shown above to book your flight: ')

chosen = ''

while True:
    userEnter = int(input("Enter the index: "))
    if userEnter == 1:
        pr = "AI"
    elif userEnter == 2:
        pr = "UA"
    elif userEnter == 3:
        pr = "EK"
    elif userEnter == 4:
        pr = "EY"
    elif userEnter == 5:
        pr = "QTR"
    elif userEnter == 6:
        pr = "6E"
    elif userEnter == 7:
        pr = "SG"
    elif userEnter == 8:
        pr = "UKV"
    listTime = times[userEnter]
    print(listTime)
    if userEnter in times.keys():
        print('You have chose the time: ', listTime)
        chosen = listofairlines[airline]
        print('\nYour flight will now be booked with', chosen, 'at ', listTime)
        break
    else:
        print('\nSorry, time not available. Try Again. ')
