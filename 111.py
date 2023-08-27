def f1(n):
    if n<1:
        return n
    else:
        return f1(n-1)

print(f1(10))