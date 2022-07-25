l1 = []


def push():
    global l1
    num = int(input('Enter employee number: '))
    name = input('Enter employee name: ')
    des = input('Enter Designation: ')
    salary = float(input('Enter Salary: '))

    t1 = (num, name, des, salary)
    l1.append(t1)


def pop():
    if l1 != []:
        print('Popped item: ', l1.pop())
    else:
        print('Underflow, Please enter some values')


def peek():
    if l1:
        print('Ready to pop(peek): ', l1[-1])
    else:
        print('Underflow. Please enter some values')


def display():
    if l1:
        for i in l1:
            print(i)
    else:
        print('Underflow. Please enter some values')


print('1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit')

while True:
    ch = int(input('\nEnter your choice: '))
    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        print('Thank you')
        break
