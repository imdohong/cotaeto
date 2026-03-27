import sys
input = sys.stdin.readline

cro_alphabet = ["c=", "c-", "dz=", "d-", 
            "lj", "nj", "s=", "z="]

count = 0
i = 0
word = list(input().rstrip())

while i < len(word):
    if i+2 < len(word) and word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=':
        count +=1
        i += 3
        continue
    
    if i+1 < len(word):
        target = word[i] + word[i+1]
        if target in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
            count += 1
            i += 2
            continue
        
    count += 1
    i += 1

print(count)


'''
cro_alphabet = ["c=", "c-", "dz=", "d-", 
            "lj", "nj", "s=", "z="]

word = input().rstrip()

for s in cro_alphabet:
    word = word.replace(s, "!")

print(len(word))


'''
# 다시 풀어 볼 문제
# replace 메서드 활용 가능