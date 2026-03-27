import sys
input = sys.stdin.readline

word = []
n = int(input())
count = n

for i in range(n):
    word.append(input().rstrip())

for s in word:
    while i < len(s):
        if (i - 1 > 0 and i + 1 < len(s)) and (s[i -1] != s[i] and s[i] != s[i+1]):
            count -= 1
            continue

print(count)

# 아직 못 풀었음
