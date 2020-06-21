print("The available options are 'add','subtract', 'multiply' and 'divide")

num1 = input("Enter your first number ")
num2 = input("Enter your second number ")

operation = input("WTF dou want boii? ")

if operation == 'add':
    sum = float(num1) + float(num2)
    print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

elif operation == 'subtract':
    difference = float(num1) - float(num2)
    print("The difference of {0} and {1} is {2}".format(num1, num2, difference))

elif operation == 'multiply':
    product = float(num1) * float(num2)
    print("The product of {0} and {1} is {2}".format(num1, num2, product))

elif operation == 'divide':
    quotient = float(num1) / float(num2)
    print("The quotient of {0} and {1} is {2}".format(num1, num2, quotient))
