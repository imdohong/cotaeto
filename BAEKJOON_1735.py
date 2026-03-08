a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a*d + c*b
denominator = b*d

x, y = numerator, denominator
while y != 0:
    x, y = y, x % y
g = x

print(numerator // g, denominator // g)