import pickle
import os


print("\n 1. Enter course details \n 2. Search fee \n 3. Delete course \n 4. Display All")


def enter():
    f = open('course.dat', 'ab')
    l1 = []
    while True:
        id = int(input('Enter course ID (or "0" to exit): '))
        if id == 0:
            break
        name = input('Enter course name: ')
        faculty = input('Enter faculty group: ')
        fee = float(input('Enter fee for the course: \n'))

        l1.append([id, name, faculty, fee])
    for i in l1:
        pickle.dump(i, f)

    f.close()

def searchfee():
    try:
        f = open('course.dat', 'rb')
        v = pickle.load(f)
        f.seek(0)
        srname = input('Enter course name to search: ')
        var = 0
        for i in v:
            if i[1] == srname:
                var = 1
                print('The fee for the course is: Rs.', i[3])
        if var == 0:
            print('Course not found')
    except EOFError:
        print('Completed')


def deletecourse():
    f = open('course.dat', 'rb')
    f2 = open('temp.dat', 'wb')

    l2 = []
    f.seek(0)
    delid = int(input('Enter course ID to delete: '))
    v = pickle.load(f)
    var = 0
    for i in v:
        if i[0] == delid:
            var = 1
        elif i[0] != delid:
            l2.append(i)
            pickle.dump(l2, f2)
    if var == 0:
        print('Course not found')

    os.remove('course.dat')
    os.rename('temp.dat', 'course.dat')


def displaycourse():
    try:
        f = open('course.dat', 'rb')
        f.seek(0)
        v = pickle.load(f)

        for i in v:
            print(i)
    except EOFError:
        print('completed')


while True:
    ch = input('Enter your choice: ')
    if ch == '1':
        enter()
    elif ch == '2':
        searchfee()
    elif ch == '3':
        deletecourse()
    elif ch == '4':
        displaycourse()
    elif ch == 'exit':
        print('Thank you')
        break
