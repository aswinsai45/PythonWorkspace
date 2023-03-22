def Display(l):
    L2 = []
    for n in l:
        if n % 2 == 0:
            L2.append(n)
    return L2, "hi bro"


l = [100, 228, 333, 432, 509, 60, 787, 800, 967]
print(Display(l))
