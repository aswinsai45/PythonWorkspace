import pickle

f = open('tempprac.dat', 'rb')

dic1 = {145: "hello", 253: "wow"}

v = pickle.load(f)

s = int(input('Enter to search: '))


for i in v:
    if i == s:
        print('Name: ', dic1.get(i))
