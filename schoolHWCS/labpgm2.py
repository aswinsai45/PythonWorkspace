def studentReport(dic1):
    for i in dic1.keys():
        print(i, sum(dic1.get(i)))

dic1 = {}
n = int(input('How many students to add?: '))
for i in range(1, n + 1):
    name = input('Enter name: ')
    marks = list(eval(input('Enter marks: ')))
    dic1[name] = marks

print(dic1)

studentReport(dic1)
