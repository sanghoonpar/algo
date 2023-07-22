T=int(input())
x=1
for i in range(T):
    A,B = map( int, (input().split()))
    print("Case #",int(x),": ",int(A)," + ",int(B)," = ",int(A+B), sep='')
    x=x+1

