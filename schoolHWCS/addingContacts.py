names = dict()
i = 0

n = int(input("How many names and numbers do you want to enter?: "))
while i in range(0, n):
    nameDictionary = str(input("Enter name: "))
    numberDictionary = str(input("Enter phone number: "))
    nameStore = ("Name: ", nameDictionary) + ("Number: ", numberDictionary)
    names = names + nameStore
    i = i + 1

print(names)
