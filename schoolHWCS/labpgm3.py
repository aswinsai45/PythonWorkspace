file = open('poem.txt', "r")
lines = 0
content = file.read()

print(content)
1
def line():
    l = 0
    coList = content.split("\n")
    for i in coList:
        l = l + 1

    print("This is the number of lines in the file ", l)


def count():
    occur = content.count('the')
    print('Number of word "the" used: ', occur)


def sentence():
    sentences = content.split('.')
    s = len(sentences)
    print('Number of sentences: ', s)


print('\n 1. Count Lines \n 2. Count "the" \n 3. Count Sentences\n')
while True:
    ch = int(input('Enter your choice: '))
    if ch == 1:
        line()
    elif ch == 2:
        count()
    elif ch == 3:
        sentence()
    else:
        print('Please enter a valid choice')
