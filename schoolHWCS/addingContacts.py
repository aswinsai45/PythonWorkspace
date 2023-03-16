import pickle, os

def write():
    f = open('binpract.dat','wb')
    name = input('Enter Name: ')
    age = int(input('Enter age: '))

    v = [name,age]
    pickle.dump(v,f)
    f.close()
def read():
    f = open('binpract.dat','rb')
    try:
        while True:
            v = pickle.load(f)
            print(v)
    except:
        print('\nDone')

def mod():
    f = open('binpract.dat', 'rb')
    try:
        while True:
            v = pickle.load(f)
            print(v[0])

    except:
        print('done!')

mod()