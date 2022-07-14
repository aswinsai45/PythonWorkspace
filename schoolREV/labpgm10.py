import csv, os


def add():
    f = open('bankacc.csv', 'a')
    w = csv.writer(f)
    while True:
        num = int(input('Enter acct. number: '))
        name = input('Enter name: ')
        add = input('Enter address: ')
        ph = int(input('Enter Phone Number: '))
        bal = float(input('Enter balance: '))

        w.writerow([num, name, add, ph, bal])

        cnt = input('Do you want to continue?[Y/N]: ')
        if cnt == 'n' or cnt == 'N':
            print('\nDone!\n')
            break
    f.close()


def read():
    f = open('bankacc.csv', 'r')
    f.seek(0)

    r = csv.reader(f)
    for row in r:
        if row:
            print(row)
    f.close()


def search():
    f = open('bankacc.csv', 'r')
    f.seek(0)
    r = csv.reader(f)
    q = 1

    sr = int(input('Enter acct. Number to search: '))
    for i in r:
        if i == []:
            pass
        elif i[0] == str(sr):
            print(i)
            q = 2
    if q == 1:
        print('Record not found')

    f.close()


def update():
    f = open('bankacc.csv', 'r')
    f.seek(0)
    f2 = open('temp.csv', 'w')
    r = csv.reader(f)
    w = csv.writer(f2)

    q = 1

    sr = int(input('Enter acct. Number to search for updation: '))

    for i in r:
        if i != []:

            print('\n\t~~MODIFICATION OPERATIONS~~\n1. Name\n 2. Address\n3. Phone\n4. Balance')
            ch = int(input('Enter your choice: '))

            if ch == 1:
                if i[0] == sr:
                    q = 2
                    new = input('Enter new name: ')
                    l1 = [i[0], new, i[2], i[3], i[4]]
                    w.writerow(l1)
                if i[0] != sr:
                    q = 2
                    w.writerow(i)


            elif ch == 2:
                if i[0] == sr:
                    q = 2
                    newad = input('Enter new address: ')
                    l1 = [i[0], i[1], newad, i[3], i[4]]
                    w.writerow(l1)
                if i[0] != sr:
                    q = 2
                    w.writerow(i)


            elif ch == 3:
                if i[0] == sr:
                    newph = int(input('Enter new phone: '))
                    l1 = [i[0], i[1], i[2], newph, i[4]]
                    w.writerow(l1)
                if i[0] != sr:
                    q = 2
                    w.writerow(i)

            elif ch == 4:
                if i[0] == sr:
                    q = 2
                    newbal = float(input('Enter new balance: '))
                    l1 = [i[0], i[1], i[2], i[3], newbal]
                    w.writerow(l1)
                if i[0] != sr:
                    q = 2
                    w.writerow(i)

    if q == 1:
        print('Record not found')

    f.close()
    f2.close()

    os.remove('bankacc.csv')
    os.rename('temp.csv', 'bankacc.csv')

def delete():
    f = open('bankacc.csv')
    f2 = open('temp.csv', 'w')

    q = 1
    r = csv.reader(f)
    w = csv.writer(f2)
    delete = int(input('Enter account number to delete: '))


    for i in r:
        if i[0] == str(delete):
            q = 2

        elif i[0] != str(delete):
            q = 2
            w.writerow(i)

        elif q == 1:
            print('Record not found')
            break


    f.close()
    f2.close()

    os.remove('bankacc.csv')
    os.rename('temp.csv', 'bankacc.csv')

    print('Completed')

print('1. add\n 2. read\n 3. search\n 4. update\n 5. delete')
while True:
    ch = int(input('Enter your choice: '))
    if ch == 1:
        add()
    elif ch == 2:
        read()
    elif ch == 3:
        search()
    elif ch == 4:
        update()
    elif ch == 5:
        delete()

print('Thank you')
