import csv, os

l1 = []


def add():
    f = open('course.csv', 'a')
    w = csv.writer(f)
    while True:
        id = int(input('\nEnter course ID (or "0" to exit): '))
        if id == 0:
            break
        name = input('Enter course name: ')
        faculty = input('Enter faculty group: ')
        fee = float(input('Enter fee for the course: '))

        w.writerow([id, name, faculty, fee])


    f.close()


def read():
    f = open('course.csv', 'r')
    f.seek(0)
    q = 0
    r = csv.reader(f)
    for row in r:
        if row:
            q = 2
            print(row)

    if q == 0:
        print('Empty. Please enter some values')

    f.close()


def search():
    f = open('course.csv', 'r')
    f.seek(0)
    r = csv.reader(f)
    q = 1

    sr = input('Enter course ID to search: ')
    for i in r:
        if i:
            if i[0] == sr:
                q = 2
                print(i)
    if q == 1:
        print('Record not found')

    f.close()


def update():
    f = open('course.csv', 'r')
    f.seek(0)
    f2 = open('temp.csv', 'w')
    r = csv.reader(f)
    w = csv.writer(f2)

    q = 1

    sr = input('Enter Course ID to search for updation: ')
    print('\n\t~~MODIFICATION OPERATIONS~~\n1. Name\n2. Faculty\n3. Fees\n4. Exit') # cid, cname, faculty, fees
    ch = int(input('Enter your choice: '))

    if ch == 1:
        for i in r:
            if i:
                if i[0] == sr:
                    q = 2
                    new = input('Enter new name: ')
                    l1 = [i[0], new, i[2], i[3]]
                    w.writerow(l1)

                elif i[0] != sr:
                    q = 2
                    w.writerow(i)


    elif ch == 2:
        for i in r:
            if i:
                if i[0] == sr:
                    q = 2
                    newn = input('Enter New faculty: ')
                    l1 = [i[0], i[1], newn, i[3]]
                    w.writerow(l1)
                elif i[0] != sr:
                    q = 2
                    w.writerow(i)



    elif ch == 3:
        for i in r:
            if i:
                if i[0] == sr:
                    q = 2
                    fee = int(input('Enter new fee: '))
                    l1 = [i[0], i[1], i[2], fee]
                    w.writerow(l1)
                elif i[0] != sr:
                    q = 2
                    w.writerow(i)

    elif ch == 4:
        q = 2
        print('Thank You')


    if q == 1:
        print('Not found')

    f.close()
    f2.close()

    os.remove('course.csv')
    os.rename('temp.csv', 'course.csv')


def delete():
    f = open('course.csv', 'r')
    f2 = open('temp.csv', 'w')

    q = 1
    r = csv.reader(f)
    w = csv.writer(f2)
    delete = int(input('Enter Course ID to delete: '))

    for i in r:
        if i:
            if i[0] == str(delete):
                q = 2

            elif i[0] != str(delete):
                q = 2
                w.writerow(i)

    if q == 1:
        print('Record not found')

    f.close()
    f2.close()

    os.remove('course.csv')
    os.rename('temp.csv', 'course.csv')

    print('Completed')


print('1. add\n2. read\n3. search\n4. update\n5. delete\n6. Exit')
while True:
    ch = int(input('Enter your choice here: '))
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
    elif ch == 6:
        print('Thank you')
        break
    else:
        break
