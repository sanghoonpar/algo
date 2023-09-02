T=int(input())
for i in range(T):
    R,S=map(str,input().split())
    R=int(R)
    for i in S:
        P=(str(i)*R)
        print(P,end="")
    print()
