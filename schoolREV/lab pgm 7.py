name = open('text1.txt', 'w+')
def TextFile(name):
    w = input('Write here into the file: ')
    name.write(w)
    name.seek(0)
    re = name.read()
    v = 0
    d = 0
    c = 0
    s = 0
    vow = "AEIOU"
    con = "BCDFGHJKLMNPQSTVXZRWY"
    reupper = re.upper()
    for i in reupper:
        if i in vow:
            v = v+1
        elif i in con:
            c = c+1
        elif i >='0' and i<='9':
            d = d+1
        else:
            s = s+1
    print('Num of vowels: ', v)
    print('Num of consonants: ', c)
    print('Num of digits: ', d)
    print('Num of special characters: ', s)

TextFile(name)

