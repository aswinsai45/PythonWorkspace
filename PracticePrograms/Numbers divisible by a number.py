num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))
num3 = int(input("Enter number 3 "))
num4 = int(input("Enter number 4 "))
num5 = int(input("Enter number 5 "))

div = int(input("Enter your divisor "))

num = num1, num2, num3, num4, num5
for nums in num:
    if nums % div == 0:
        print(nums)