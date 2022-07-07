import pickle, os

f1 = open('customer.dat', 'wb+')
f2 = open('temp.dat', 'wb+')
dic1 = {}

print('1. Enter data \n 2. Search with Phone Number \n 3. Modify a record \n 4. Display all the records')


def enter():
    while True:
        num = int(input('Enter customer Phone Number: '))
        name = input('Enter customer name: ')
        dic1[num] = name
        pickle.dump(dic1, f1)

        cnt = input('Do you want to continue?: ')
        if cnt == 'n' or cnt == 'N':
            print('Done! Thank you!')
            break


def search():
    while True:
        num = int(input('Enter customer Phone Number: '))
        for i in dic1:
            if i == num:
                print("Customer name: ", dic1[i])
        cnt = input('Do you want to continue?: ')
        if cnt == 'n' or cnt == 'N':
            print('Done! Thank you!')
            break


def mod():
    readnum = int(input('Enter Phone Number to change name: '))
    newname = input('Enter new name: ')
    try:
        f1.seek(0)
        q = 0
        readb = pickle.load(f1)
        for i in readb:
            if i == readnum:
                q = 1
            if i != readnum:
                pickle.dump((i, dic1[newname]), f2)
            elif q == 0:
                print('Record not found')

    except EOFError:
        print('Operation completed')

    f1.close()
    f2.close()

    os.remove('customer.dat')
    os.rename('temp.dat', 'customer.dat')


def display():
    f1 = open('customer.dat')
    try:
        v = pickle.load(f1)
        print(v)
    except EOFError:
        print("\n completed")


while True:
    ch = int(input('Enter your choice (or "exit" to exit): '))
    if ch == 1:
        enter()
    elif ch == 2:
        search()
    elif ch == 3:
        mod()
    elif ch == 4:
        display()
    elif ch == 'exit':
        print('Thank you')
        break
