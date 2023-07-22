n = int(input())

for i in range(n):
    word, word_1 = input().split()
    for j in word_1:
        print(j*int(word), end='' )
    print()