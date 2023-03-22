import csv

with open('summa.csv','r', newline="") as f:
    r = csv.reader(f)
    w = csv.writer(f)

    for i in r:
        print(i)