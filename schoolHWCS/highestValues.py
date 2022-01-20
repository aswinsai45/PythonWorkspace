values = list()

n = int(input("How many values do you eant to enter?: "))
i = 0
while i in range(0, n):
    nums = int(input("Enter number: "))
    values = values + list((nums,))

    i = i+1

values.sort()

print("Highest value: ", values[-1])
print("Lowest value: ", values[0])
