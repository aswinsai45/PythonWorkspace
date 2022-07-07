file = open('text1.txt', 'w+')
w = input('Write here: ')
file.write(w)
file.seek(0)
# file.close()
# file = open('text1.txt', 'r')

vow = 'AEIOUaeiou'
dig = '0123456789'
con = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'


def TextFile(file):
    fr = file.read()
    for i in fr:
        print(i)

TextFile(file)