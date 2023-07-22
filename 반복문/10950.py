T=int(input())
a=0
while a<T:
    A,B = map( int, (input().split()))
    print(A+B)
    a=a+1
    if a==T:
        break