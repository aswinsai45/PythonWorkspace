bpass = input('enter boardingpass number: ')
file = open('C:/Users/aswin/PycharmProjects/SchoolProject/BookingConf/' + bpass, 'r')
s = file.read()
print(s)
