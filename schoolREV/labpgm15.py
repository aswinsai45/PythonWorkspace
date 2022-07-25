import random
ODD_Q, EVEN_Q = [], []

def enq():
    r = random.randint(1,500)
    if r % 2 == 0:
        if r not in EVEN_Q:
            EVEN_Q.append(r)
        else:
            enq()
    else:
        if r not in ODD_Q:
            ODD_Q.append(r)
        else:
            enq()

def deq_odd():
    if ODD_Q:
        print(ODD_Q.pop(0))
    else:
        print('Underflow')

def srEVEN_Q():
    if EVEN_Q:
        sr = int(input('Enter search value: '))
        q = 1
        for i in EVEN_Q:
            if i == sr:
                q = 2
                print('Value Present')
        if q == 1:
            print('Value not present')
    else:
        print('Underflow')

def display():
    print('1. Display Even\n2. Display Odd')
    ch1 = int(input('Enter your choice: '))
    if ch1 == 1:
        if EVEN_Q:
            for i in EVEN_Q:
                print(i)
        else:
            print('Underflow')
    elif ch1 == 2:
        if ODD_Q:
            for i in ODD_Q:
                print(i)
        else:
            print('Underflow')
    else:
        print('Please enter a valid choice')
print('1.Enqueue\n2. Dequeue from ODD\n3. Search from EVEN\n4. Display respectively\n5. Exit')
while True:
    ch = int(input('Enter your choice here: '))
    if ch == 1:
        enq()
    elif ch == 2:
        deq_odd()
    elif ch == 3:
        srEVEN_Q()
    elif ch == 4:
        display()
    elif ch == 5:
        print('\nThank You')
        break
    else:
        print('PLease enter a valid choice')
