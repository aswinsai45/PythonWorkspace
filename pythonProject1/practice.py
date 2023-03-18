import pickle

# [name,admn,[5submarks indiv.]]

top = []


def insert():
    f = open('student.dat', 'wb')
    while True:
        n = input('enter student name: ')
        admn = int(input('Enter student admn num: '))
        marks = list(eval(input('Enter marks 5 subs in sequence :')))

        v = [n, admn, marks]
        pickle.dump(v, f)
        cnt = input('cnt? y/n: ')
        if cnt == 'n':
            break

    f.close()


def marks():
    global top
    f = open('student.dat', 'rb')
    try:
        while True:
            r = pickle.load(f)
            if r[2][0] + r[2][1] + r[2][2] + r[2][3] + r[2][4] > 490:
                print(r)
    except:
        print('\nFinished')





marks()