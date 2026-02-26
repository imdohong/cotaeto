hour, min=map(int, input().split())

if min-45<0:
    hour=hour-1
    if hour<0:
        print("23", 15+min)
    elif hour>=0:
        print(hour, 15+min)

elif min-45>=0:
    print(hour, min-45)