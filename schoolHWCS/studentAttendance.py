name = tuple()
n = int(input("How many names do you want to enter?: "))
for i in range(0, n):
    enterName = input("Enter names here: ")
    name = name + (enterName,)

print("\nThe names entered in the tuple are:")
print(name)

search = input("\nEnter the name of the student you want to search? ")

if search in name:
    print("The name", search, "is present")
else:
    print("The name", search, "is not present")
