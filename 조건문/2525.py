A,B = map( int, (input().split()))
C=int(input())
A = A + C // 60
B = B + C % 60

if B >= 60:
    B -= 60
    A += 1

if A >= 24:
    A -= 24

print(A, B)