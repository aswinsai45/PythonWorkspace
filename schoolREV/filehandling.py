import pickle
f = open('xii.dat', 'wb')

e = input('Enter here: ')
p = input('Enter price: ')
na = input('name: ')

pickle.dump((e,p,na) , f)

'''try:
    while True:
        v = pickle.load(f)
        print(v)
except:
     pass'''
