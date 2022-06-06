import pickle
f = open('try.dat', 'rb')
k = pickle.load(f)
f.close()
print(k)
`