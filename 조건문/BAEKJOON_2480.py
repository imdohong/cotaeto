a, b, c=map(int, input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b or a==c:
    print(1000+a*100)
elif b==c:
    print(1000+100*c)
else:
    if a>b and a>c:
        print(100*a)
    elif b>c and b>a:
        print(100*b)
    else:
        print(100*c)