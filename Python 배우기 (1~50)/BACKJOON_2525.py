a,b = map(int, input().split())
c= int(input())
total = b+c
a += total//60
b = total%60
if a>=24:
    a-=24
print(a,b)