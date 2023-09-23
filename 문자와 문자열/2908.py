A, B = map(str, input().split())
if A[::-1] < B[::-1]:
    print(B[::-1])
else:
    print(A[::-1])
