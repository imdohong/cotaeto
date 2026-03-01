a, b = map(int, input().split())
c, d = map(int, input().split())

while(b%a == 0 and d%c == 0):
    if b%a !=0 :
        a = a // a
        b = b // a
    if d%c !=0 :
        c = c//c
        d = d//c

e = b * d
f = a * d + c * b
print(e, f)