import csv

f = open('bankacc.csv')
r = csv.reader(f)

sr = int(input('Number to check: '))

f.seek(0)

k = 0


for row in r:
    if k != 0:
        num = row[0]
        if num == str(sr):
            print('found')
    else:

        k = k+1
