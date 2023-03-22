import pickle

f = open('write.dat', 'wb+')
v = [['sai', 'bro'], ['bobs', 'raja']]
f.seek(0)

pickle.dump(v, f)
f.seek(0)
try:
    while True:
        r = pickle.load(f)

except:
    pass
