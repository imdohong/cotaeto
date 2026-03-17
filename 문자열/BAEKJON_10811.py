m, n = map(int, input().split())

num = [i for i in range(1, m + 1)]

for _ in range(n):
    i, j = map(int, input().split())
    
    num[i-1:j] = num[i-1:j][::-1]

print(*num)