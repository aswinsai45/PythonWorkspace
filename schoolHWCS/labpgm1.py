l = [1, 2, 3, 4, 5, 6]


def search(s):
    v = l[s]
    print(v)


def sum(k):
    t = 0
    for i in range(1, k + 1):
        t = t + i
    print(t)


def delete(d):
    g = l.pop(d)
    print('Element deleted: ', g)
    print(l)


def insert(i):
    e = int(input('Enter element to be inserted at given position: '))
    l.insert(i, e)
    print(l)


print('1. Search \n 2. Sum \n 3. Delete \n 4.Insert')

ch = int(input('Enter your choice: '))
if ch == 1:
    s = int(input('Enter Position to search: '))
    search(s)

elif ch == 2:
    k = int(input('Enter index to sum: '))
    sum(k)

elif ch == 3:
    d = int(input('Enter element position to delete: '))
    delete(d)

elif ch == 4:
    i = int(input('Enter input position: '))
    insert(i)