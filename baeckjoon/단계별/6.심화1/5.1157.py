import sys
input = sys.stdin.readline

word = input().rstrip()
alphabet = []
count =[]

for i in range(ord('a'), ord('z')+1):
    alphabet.append(i)
    
for i in alphabet:
    for j in word:
        if i == ord(j):
            count[alphabet.index(i)] += 1


print(count)
        