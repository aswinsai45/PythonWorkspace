import pickle

f = open(r"C:\Users\aswin\OneDrive\Documents\customer.dat", 'rb')

try:
    v = pickle.load(f)
    for i in v:
        print(i, '\t', v[i])
except EOFError:
    print('\nDone!')

