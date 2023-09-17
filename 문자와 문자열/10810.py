S = input() 


positions = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}


for i, char in enumerate(S):
    if positions[char] == -1:
        positions[char] = i


for char in positions.values():
    print(char, end=' ')
