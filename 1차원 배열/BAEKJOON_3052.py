num, t, total=0, 0, 0

k=[]

for i in range(1, 11):
    num=int(input())

    t=num%42
    k.append(t)


for f in range(0, 42):
    s=k.count(f)
    if s>=1:
        total+=1

print(total)