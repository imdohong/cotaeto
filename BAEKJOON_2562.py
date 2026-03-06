a=[]
for i in range(0, 9):
    num=int(input())
    a.append(num)

print(a(max))

max=max(a)

for k in range(0, 9):
    if a[k]==max:
        print(k+1)
    