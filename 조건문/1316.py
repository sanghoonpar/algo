n=int(input())
a=0

table=list()
#앞에서부터 알파벳 하나씩 확인
# s[0] s[1] s[2] s[3] -> 반복문으로 처리 for i in range(len(s)):
# 1. 처음 나온 알파벳이야 -> 통과 -> 생각해봐
# 2. 처음 안나왔는데
# 2-1. 방금 앞에거랑 같으면 -> 통과 -> i 번쨰면 i-1째랑 비교하면되는거아니야 ? 
# 2-2. 방금 앞에거랑 다르면 -> 안 세 끝 -> else
for i in range(n):
    b=0
    s=input()
    for i in range(len(s)):
        
       
        if s[i] not in table:
            table.append(s[i])
            b+=1
        else:
            if s[i]==table[table.index(s[i-1])]:
                b+=1
    if b==len(s):
        a+=1
print(a)
