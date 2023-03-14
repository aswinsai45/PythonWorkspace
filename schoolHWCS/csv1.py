import csv
'''
f = open('bro.csv', 'w', newline='')
w = csv.writer(f)
wlist = []
for i in range(3):
    l = list(eval(input('Sequence: ')))
    wlist.append(l)

for i in wlist:
    w.writerow(i)
'''

f = open('bro.csv','r')
r = csv.reader(f)
for i in r:
    print(i)
    