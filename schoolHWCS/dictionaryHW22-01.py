n = int(input('Enter upto what number to create the dictionary with squares: '))
dic1 = {}
for i in range(0, n):

    squaring = i*i

    f = i, ':', squaring
    dic1[i] = squaring
    n = n + 1
print(dic1)
