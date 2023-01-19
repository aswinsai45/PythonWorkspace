s = "welcome2cs"
n = len(s)
m = ""
for i in range(0, n):
    if (s[i] >= 'a' and s[i] <= 'm'):
        m = m + s[i].upper()
    elif s[i] >= 'n' and s[i] <= 'z':
        m = m + s[i - 1]
    elif (s[i].isupper()):
        m = m + s[i].lower()
    else:
        m = m + '&'
print(m)
