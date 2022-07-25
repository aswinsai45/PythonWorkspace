vow = 'AEIOUaeiou'
NoVowel = []
All = []


def PushNV(N):

    global NoVowel
    for i in N:
        q = 1
        for j in i:
            if j in vow:
                q = 2
                break
        if q == 1:
            NoVowel.append(i)

    print('NoVowel: ', NoVowel)

def pop():
    for i in NoVowel:
        if i:
            print('Popped Element: ', NoVowel.pop())

        else:
            print('Underflow')
            break
    print('Empty Stack')

n = int(input('Num of words to enter?: '))
for i in range(n):
    word = input('Enter word: ')
    All.append(word)

PushNV(All)
pop()
