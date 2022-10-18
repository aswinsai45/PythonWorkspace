import datetime
import mysql.connector as connector
import itertools

con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
cur = con.cursor()
cur.execute('Select * from journeydetails where boardingpass = 3389 ')
v = cur.fetchall()

l = []

# length = [8]
#
# modlist = [list(itertools.islice(l, elem))
#         for elem in length]
for row in v:
    for col in row:
        l.append(col)
#

# print(l)
print()
print()


l = []
l2 = []
def passengerlist(l, n=8):
    global l2
    for j in range(0, len(l), n):
        l2 = l[j:j + n]
    l = l2
    print(l)

passengerlist(l)




# length = 8
# modlist = [list(itertools.islice(l, elem))
#         for elem in length]
# print(modlist)
# def timeformatter(date):
#     d = datetime.datetime.strftime(date, "%Y-%m-%d")
#     print(d)
#
# date = l[1]
# timeformatter(date)


# print(l[1])
# date = l[1]
# d = datetime.datetime.strftime(date, "%Y-%m-%d")
#
# print(d)
#
