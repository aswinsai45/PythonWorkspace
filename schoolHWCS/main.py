n = int(input("How many emails do you want to add?: "))

print('Enter "stop" to stop the program')


class emailloop():
    i = 0
    while i < n:
        email = str(input("Enter email ID: "))
        list1 = list.insert(email)
        i = i + 1

    print(list1)

