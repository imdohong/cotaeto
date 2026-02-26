hour, min = map(int, input().split())
oven = int(input())

min = min + oven

if min >= 60:
    hour = hour + (min // 60)
    min = min % 60 

if hour >= 24:
    hour = hour % 24

print(hour, min)