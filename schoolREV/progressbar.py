
import time
def progress(percent=10, width=30):

    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes* '*', blanks* ' ', ']', f'{percent: .0f}%', sep='',
        end='', flush=True)

for i in range(101):
    progress(i)
    time.sleep(0.1)


'''1. The code defines a function called "progress" which takes two parameters - percent and width.

2. The function calculates how many hashes (lines) will fit in the given width, and then calculates how many blanks will be left over.

3. The function prints out a progress bar, with the given percentage and width.

4. The code loops through a range of numbers, and calls the "progress" function with each number.

5. The code waits for a tenth of a second before moving on to the next number.'''