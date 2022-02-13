import datetime
timeValidator = datetime.date.today()
# while True:
#     travelDate = (input("Enter departure date in dd/mm/yyyy format "))
#     travelValidation = datetime.datetime.strptime(travelDate, "%d/%m/%Y").date()
#
#     if travelValidation < timeValidator.today():
#         print("Cannot choose a date in the past, -", travelDate + '\n')
#     else:
#         break

# while True:
#     passportExpiry = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
#     passportExpValidation = datetime.datetime.strptime(passportExpiry, "%d/%m/%Y").date()
#     if passportExpValidation > timeValidator:
#         break
#     else:
#         print('\nCannot Choose date in the past -', passportExpiry, 'Try again\n')

while True:
    passportExp2 = (input("Enter expiration date of passport in dd/mm/yyyy format: "))
    passportExpValidation = datetime.datetime.strptime(passportExp2, "%d/%m/%Y").date()
    if passportExpValidation > timeValidator:
        break
    else:
        print('\n' + "Please Enter correctly this time or else you will be exited..")