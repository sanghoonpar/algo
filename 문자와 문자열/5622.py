1
a=str(input())
2
x=0
3
s=0
4
while s<int(len(a)):
5
    if "A" in a[s] or "B" in a[s] or "C" in a[s]:
6
        x+=3
7
    elif "D" in a[s] or "E" in a[s] or "F" in a[s]:
8
        x+=4
9
    elif "G" in a[s] or "H" in a[s] or "I" in a[s]:
10
        x+=5
11
    elif "J" in a[s] or "K" in a[s] or "L" in a[s]:
12
        x+=6
13
    elif "M" in a[s] or "N" in a[s] or "O" in a[s]:
14
        x+=7
15
    elif "P" in a[s] or "Q" in a[s] or "R" in a[s] or "S" in a[s]:
16
        x+=8
17
    elif "T" in a[s] or "U" in a[s] or "V" in a[s]:
18
        x+=9
19
    elif "X" in a[s] or "Y" in a[s] or "Z" in a[s] or "W" in a[s]:
20
        x+=10
21
    s+=1
22
print(x)
