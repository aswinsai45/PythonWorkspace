import pickle

f = open('tempprac.dat', 'wb+')

dic1 = {145: "hello", 253: "wow:"}

pickle.dump(dic1, f)

f.seek(0)

dic2 =
try:
    v = pickle.load(f)
    print(v)
except EOFError:
    print('done')
