tuple0 = [1, 2, 3, 4, 5]
dep = input('Where are you departing from?: ')
if int(dep) not in tuple0:
    print('Choose a valid country number and please restart')
    exit()
else:
    pass
dest = input('Where do you wish to travel?: ')
if int(dest) not in tuple0:
    print('Choose a valid country number of the country you wish to travel')
    exit()
else:
    pass
