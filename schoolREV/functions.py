print('1. horizontal\n2. Vertical\n3. Continuous\n4. Alpha L\n5. Alpha R\n6. Inv Py')
while True:
    ch = int(input('Enter choice: '))
    n = int(input('Enter rows: '))
    if ch == 1:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(i, end=' ')
            print()
    elif ch == 2:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    elif ch == 3:
        s = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(s, end=' ')
                s = s + 1
            print()
    elif ch == 4:
        for i in range(1, n + 1):
            c = 65
            for j in range(1, i + 1):
                print(chr(c), end=' ')
                c = c + 1
            print()
    elif ch == 5:
        for i in range(n):
            c = 65
            for j in range(1, n - i):
                print(" ", end="")
            for k in range(i + 1):
                print(chr(c), end="")
                c = c + 1
            print()
    elif ch == 6:
        for i in range(1, n + 1):
            for j in range(0, i):
                print(" ", end="")
            t = 2*n-(2*i-1)
            for j in range(1, t+1):
                if i == 1 or j == 1 or j == t:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
