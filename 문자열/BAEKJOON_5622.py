a = input("")
sum = 0

for i in range(len(a)):
    if a[i] in 'ABC':
        sum += 3
    elif a[i] in 'DEF':
        sum += 4
    elif a[i] in 'GHI':
        sum += 5
    elif a[i] in 'JKL':
        sum += 6
    elif a[i] in 'MNO':
        sum += 7
    elif a[i] in 'PQRS':
        sum += 8
    elif a[i] in 'TUV':
        sum += 9
    elif a[i] in 'WXYZ':
        sum += 10
    else:
        sum += 11

print(sum)