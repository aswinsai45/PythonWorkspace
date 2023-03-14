import pickle

f = open('bro.dat', 'wb')
wr = 'hello everyone this is Sai Aswin here to tell you about computers'
pickle.dump(wr,f)

f.close()

k = open('bro.dat', 'rb')
try:
    while True:
        v = pickle.load(k)
        print(v)
except:
    pass
