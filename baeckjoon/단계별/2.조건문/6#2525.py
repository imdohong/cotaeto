h, m = map(int, input().split())
time = int(input())

total_min = h * 60 + m + time

if total_min >= 24*60 :
    print(total_min // 60 - 24, total_min % 60)
else :
    print(total_min //60, total_min % 60)

# 다시 풀어볼 문제