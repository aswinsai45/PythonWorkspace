import pickle
file = open('try.dat', 'rb')
l1 = []
while True:
    admn = input("Enter admission number: ")
    name = input('Enter name: ')
    fname = input("Enter father's name: ")
    mname = input("Enter mother's name:")
    add = input('Enter address: ')
    l1.append(admn)
    l1.append(name)
    l1.append(fname)
    l1.append(mname)
    l1.append(add)
    pickle.dump(l1, file)
    s = input('Do you want to stop? [y/n]: ')
    if s == 'y' or s == 'y':
        print('Stopping..')
        break
s = pickle.load(file)
print(s)
