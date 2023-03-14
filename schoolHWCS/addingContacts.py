f = open('crying.text', 'w')
wr = "class xii ends soon\nbatch 23'"

f.write(wr)

f.close()

f = open('crying.text','r')
r = f.readline()
b = f.read(2)
print(r,b,sep= ' ')