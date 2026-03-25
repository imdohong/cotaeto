n, m = map(int, input().split())
basket = []
for i in range(1, n+1):
    basket.append(i)

for k in range(0, m):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)

# 다시 풀어 볼 문제
    



