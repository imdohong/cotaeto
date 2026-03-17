h, m = map(int, input().split())

if m >= 45:
    if h > 0:
        print(h, (m-45))
    else:
        print(0, (m-45))
else :
    if h > 0:
        print((h-1), m + 15)
    elif h == 0:
        print(23, m + 15)
        
# 다시 풀어볼 문제