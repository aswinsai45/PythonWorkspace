'''f = open('textfile.txt', 'r')
v = f.read()
print(v)

s = '#'
k = s.join(v)
print(k)

m = v.swapcase()
print(m)'''

f = open('textfile2.txt','w')
s = ['sai\n','bro\n','bobs\n']

print(f.writelines(s))
f.close()