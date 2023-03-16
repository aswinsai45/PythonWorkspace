import csv, os


def write():
    f = open('age.csv', 'a', newline="")
    n = input('Enter name: ')
    a = input('Enter age: ')
    v = [n, a]

    w = csv.writer(f)
    w.writerow(v)


def mod():
    f1 = open('age.csv', 'r')
    f2 = open('temp.csv', 'w', newline="")
    r = csv.reader(f1)
    w = csv.writer(f2)

    sr = input('Enter name to change age: ')
    r = csv.reader(f1)
    for i in r:
        if i[0] == sr:
            na = input('Enter new age: ')
            w.writerow([i[0], na])
        else:
            w.writerow(i)
    f1.close()
    f2.close()

    os.remove('age.csv')
    os.rename('temp.csv', 'age.csv')


def display():
    print('\n\n')
    f = open('age.csv', 'r')
    r = csv.reader(f)
    for i in r:
        print(i)
    print('\n\nDone')


write()
write()
write()
display()
mod()
display()
