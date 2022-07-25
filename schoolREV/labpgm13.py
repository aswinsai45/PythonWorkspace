PRODUCT = {}
stack = []


def add_dict():
    global PRODUCT
    pid = int(input('Enter Product ID: '))
    pname = input('Enter product name: ')
    price = float(input('Enter price: '))

    v = [pname, price]
    PRODUCT[pid] = v

    print("Don't forget to Push!")

def push():
    global stack
    for i in PRODUCT:
        v = [i, PRODUCT.get(i)]
        stack.append(v)


def pop():
    if stack:
        print('Popped element: ', stack.pop())
    else:
        print('Underflow')


def peek():
    if stack:
        print(stack[-1])
    else:
        print('Underflow')


def search():
    if stack:
        sr = int(input('Enter ID to search: '))
        q = 1
        for i in stack:
            if i[0] == sr:
                q = 2
                print(i)
        if q == 1:
            print('Not found')
    else:
        print('Underflow')


def display():
    if stack:
        for i in stack:
            print(i)
    else:
        print('Underflow')


print('1. Add to Dictionary\n2. Push\n3. Pop\n4. Peek\n5. Search\n6. Display\n7. Exit')

while True:
    ch = int(input('\nEnter you choice: '))
    if ch == 1:
        add_dict()
    elif ch == 2:
        push()
    elif ch == 3:
        pop()
    elif ch == 4:
        peek()
    elif ch == 5:
        search()
    elif ch == 6:
        display()
    elif ch == 7:
        print('\nThank you')
        break
    else:
        print('Please enter a valid choice')
