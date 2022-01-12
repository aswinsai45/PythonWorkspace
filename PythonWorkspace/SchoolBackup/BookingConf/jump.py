import datetime

titrd = datetime.date.today()

TrDate = (input("enter departure date in dd/mm/yyyy format "))
trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
if trdated >= titrd.today():
    pass
else:
    print("Cannot choose a date in the past, -", TrDate, "\n\nPlease try again//\n")
    print("\nEnter the date correctly this time, or else you will be exited// ")
    TrDate = input("Enter travel date in dd/mm/yyyy format: ")
    trdated = datetime.datetime.strptime(TrDate, "%d/%m/%Y").date()
    if trdated >= titrd.today():
        pass
    else:
        print("Cannot choose a date in the past, -", TrDate)
        print("Sorry, please restart and try again//")
        exit()
