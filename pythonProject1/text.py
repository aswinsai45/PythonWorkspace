f = open('textfile.txt', 'r')
v = f.read()
print(v)

s = '#'
k = s.join(v)
print(k)

m = v.swapcase()
print(m)