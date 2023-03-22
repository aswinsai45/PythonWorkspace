l1 = [7, 4, 3, 6]

for i in range(len(l1) - 1):  # 0,1,2
    for j in range(len(l1) - 1):  # 0,1,2
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print(l1)
