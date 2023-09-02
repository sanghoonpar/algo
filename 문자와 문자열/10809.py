S=str(input())
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x=0
b=str()
for i in range(26):
    if a[x] in S:
        x+=1
        b+=str(x)
    elif a[x] in S:
        x+=1
        b+="-1"
print(b)