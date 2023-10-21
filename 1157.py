s=input()
s=s.upper()
table = dict()
for i in s:
    if i not in table:
            table[i] = 1
    elif i in table:
            table[i] += 1
Table = sorted(table.items(), reverse=True, key=lambda item: item[1])
if len(Table)<2:
    print(s[0])
else:
    a=Table[0]
    b=Table[1]
    if a[1]==b[1]:
        print("?")
    else:
        print(a[0])
