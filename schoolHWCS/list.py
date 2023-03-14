def insert():
    print()
    global l
    ele = int(input('Enter element to insert: '))
    pos = int(input('Enter position: '))
    if pos == 0:
        l = [ele]+l
        print(l)

    else:
        l1 = l[:pos]
        l2 = l[pos:]
        l = l1 + [ele] + l2
        print(l)

l = list(eval(input('Enter numbers in list: ')))
while True:
    insert()