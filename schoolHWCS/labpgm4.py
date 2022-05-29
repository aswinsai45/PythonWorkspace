file = open('text1.txt', 'r+')
w = input('Write here: ')
file.write(w)
# file.close()
# file = open('text1.txt', 'r')
vow = 'AEIOUaeiou'
dig = '0123456789'
con = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
v = 0
d = 0
s = 0
c = 0

for line in file:
    for char in line:
        if char in vow:
            v = v + 1

        elif char in dig:
            d = d + 1

        elif char in con:
            c = c + 1

        else:
            s = s + 1

print('Vowels: ', v)
print('Digits: ', d)
print('Consonants: ', c)
print('Special Characters: ', s)
