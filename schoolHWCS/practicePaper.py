# li1 = list(eval(input('Enter to a list: ')))
# li2 = list(eval(input('Enter to a list: ')))
# if len(li1) != len(li2):
#     print('Cannot compare, lists are of unequal length')
#     exit()
# else:
#     pass
# for i in range(len(li1)):
#     if li1[i] == li2[i]:
#         pass
#     else:
#         print('The items are unequal. ', i)
#         break

d1 = {}
d2 = {}
keys1 = eval(input('Enter a number: '))
keys2 = eval(input('Enter a number: '))
vals = eval(input('Enter element: '))
vals2 = eval(input('Enter element: '))
d1[keys1] = vals
d2[keys2] = vals2
if keys1 == keys2:
    print([keys1])
