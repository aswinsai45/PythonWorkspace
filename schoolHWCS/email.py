n = int(input("How many emails do you want to add?: "))

print('Enter "stop" to stop the program')
i = 0
while i < n:
    email = str(input("Enter email ID: "))
    tup1 = email.__add__(email)

    i = i + 1

    print(tup1)

