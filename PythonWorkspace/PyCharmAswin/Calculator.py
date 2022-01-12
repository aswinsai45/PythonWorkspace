print("Available operations are 'add', 'subtract', 'multiply', 'divide'")

num1 = input("Enter your first value ")
num2 = input("Enter your second value ")


operation = input("Which operation do you want to perform? ")

if operation == 'add':
    sum = float(num1) + float(num2)
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

elif operation == 'subtract':
    difference = float(num1) - float(num2)
    print('The difference of {0} and {1} is {2}'.format(num1, num2, difference))

elif operation == 'multiply':
    product = float(num1) * float(num2)
    print('The product of {0} and {1} is {2}'.format(num1, num2, product))

elif operation == 'divide':
    quotient = float(num1) / float(num2)
    print('The quotient of {0} and {1} is {2}'.format(num1, num2, quotient))

print("Thank You for Using our Calculator")
