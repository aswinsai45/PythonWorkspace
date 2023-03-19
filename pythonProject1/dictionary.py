d1 = {1: 100, 2: 400, 3: 690, 4: 590}
d2 = {1: 200, 3: 500, 4: 390}
d3 = {}

l1, l2 = [], []

for i in d1:
    l1.append(i)
for j in d2:
    l2.append(j)

commonkey = []

if len(l1) > len(l2):
    for k in l1:
        if k in l1 and k in l2:
            commonkey.append(k)
else:
    for k in l2:
        if k in l2 and k in l1:
            commonkey.append(k)

for key in commonkey:
    d3[key] = d1[key] + d2[key]

print("Counter(", d3, ")")
