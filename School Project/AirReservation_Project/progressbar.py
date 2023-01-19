import time
from time import sleep

def progress(percent=0, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    star = width * percent // 100
    dot = width - star

    print('\r[', star *'*', dot *'.', ']', f" {percent:.0f}%", sep='', end='', flush=True)

print('This will take a moment')
for i in range(101):
    progress(i)
    time.sleep(0.01)
# Newline so command prompt isn't on the same line
print()

"""def progress(percent = 0, width=30):
    star = width * percent//100
    dot = width - star

    print("\r[",star*'*',dot*'.',"]", flush=True, sep = '',end = '')
    
for i in range(101):
    progress(i)
    sleep(0.1)"""

print('Hello World')
print('Hello \rWorld')
