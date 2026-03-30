import sys
input = sys.stdin.readline

n = int(input())
count = n

for i in range(n):
    word = input().rstrip()
    for j in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                count -= 1
                break

print(count)

# 런타임 에러. 다시 풀어 볼 문제. 조건 이해 정확히 할 것.
