import pickle

f1 = open('customer.dat', 'rb')
f1.seek(0)
v = pickle.load(f1)
s = int(input('Enter customer Phone Number: '))
q = 1
for i in v:
    if i == s:
        q = 2
        print("Customer name: ", i)
    elif q == 1:
            print('Not found')

    print('Done! \n')

print(v)

f1.close()