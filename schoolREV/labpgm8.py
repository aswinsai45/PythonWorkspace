import os
import pickle

dic1 = {}

print('1. Enter data \n 2. Search with Phone Number \n 3. Modify a record \n 4. Display all the records\n')


def enter():
    f1 = open('customer.dat', 'ab')
    while True:
        num = int(input('Enter customer Phone Number (or "0" to exit): '))
        if num == 0:
            print('Done!\n')
            break
        name = input('Enter customer name: ')
        dic1[num] = name
    pickle.dump(dic1, f1)

    f1.close()


def search():
    f1 = open('customer.dat', 'rb')
    f1.seek(0)
    v = pickle.load(f1)
    s = int(input('Enter customer Phone Number: '))
    q = 1
    for i in v:
        if i == s:
            q = 2
            print("Customer name: ", v[s])
    if q == 1:
        print('Not found')
    print('Done! \n')

    f1.close()


def mod():
    f1 = open('customer.dat', 'rb')
    f2 = open('temp.dat', 'wb')
    f1.seek(0)

    dic2 = {}
    q = 0
    x = int(input('Enter Phone Num: '))
    v = pickle.load(f1)
    for i in v:
        if i == x:
            q = 1
            newname = input('Enter New Name: ')
            dic2[x] = newname
        elif i != 0:
            q = 1
            dic2[i] = v[i]
        if q == 0:
            print('Record not found')
    pickle.dump(dic2, f2)

    f1.close()
    f2.close()

    os.remove('customer.dat')
    os.rename('temp.dat', 'customer.dat')


def display():
    try:
        f1 = open('customer.dat', 'rb+')
        f1.seek(0)
        v = pickle.load(f1)
        for i in v:
            print(i, '\t', v[i])
    except EOFError:
        print('Done! \n')


while True:
    ch = input('Enter your choice (or "exit" to exit): ')
    if ch == '1':
        enter()
    elif ch == '2':
        search()
    elif ch == '3':
        mod()
    elif ch == '4':
        display()
    elif ch == 'exit':
        print('Thank you')
        break
