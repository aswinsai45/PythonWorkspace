file = open('poem.txt', "r")
lines = 0
content = file.read()
def line():
    global lines
    coList = content.split("\n")

    for i in coList:
        lines = lines+i

    print("This is the number of lines in the file ", lines)

def count():
    occur = content.count('the')
    print('Number of word "the" used: ', occur)

def sentence():
    sentences = content.split('.')
    print('Number of sentences: ', sentences)

print('\n 1. Count Lines \n 2. Count "the" \n 3. Count Sentences\n')
ch = int(input('Enter your choice: '))
if ch == 1:
    line()
elif ch == 2:
    count()
elif ch == 3:
    sentence()
else:
    print('Please enter a valid choice')