import pickle

try:
    f = open('course.dat', 'rb')
    v = pickle.load(f)
    for i in v:
        print(i)
except EOFError:
    print('Done!')
