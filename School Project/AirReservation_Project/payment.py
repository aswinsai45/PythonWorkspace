import datetime
import random

price = random.randint(12542, 50000)

print('\nYour ticket price will be: ₹', price)

print('Now, please pay with your Debit/Credit Card here')

nameOnCard = input('Name on Card: ')
card_number = str(input('16- Digit Credit/Debit card number: '))
cardLength = len(card_number)
if cardLength == 16:
    pass
else:
    print('Invalid Number, try again: ')
    card_number = int(input('16- Digit Credit/Debit card number: '))
    if cardLength == 16:
        pass
    else:
        print('Sorry, you have entered incorrectly for the 2nd time. You will now be exited. Please restart')
        exit()
cardExp = input('Enter expiry date [dd/mm/yyyy]:')
cardValidation = datetime.datetime.strptime(cardExp, "%d/%m/%Y").date()
if cardValidation > datetime.date.today():
    pass
elif cardValidation == datetime.date.today():
    print("Don't forget to renew your card!")
else:
    print("Cannot choose a date in the past, -", cardExp + '\n')
    print("Try again")
    cardExp = input('Enter expiry date [dd/mm/yyyy]:')
    cardValidation = datetime.datetime.strptime(cardExp, "%d/%m/%Y").date()
    if cardValidation >= datetime.date.today():
        pass
    else:
        print('\n' + 'Sorry, date invalid, Renew your card')
        print('Please restart and try again')
        exit()
cvvCard = str(input("Enter 3 digit card's cvv: "))
if len(cvvCard) == 3:
    pass
else:
    print('Invalid CVV, try again')
    cvvCard = str(input("Enter 3 digit card's cvv: "))
    if len(cvvCard) == 3:
        pass
    else:
        print('Invalid CVV for the 2nd time, you will now be exited. please restart')
        exit()

paid = print('Paid by: ', nameOnCard + ' | ' + 'Card Number:' + card_number + ' | ' + 'Transaction Approved for ' + '| ' + ('₹' + str(price)))
