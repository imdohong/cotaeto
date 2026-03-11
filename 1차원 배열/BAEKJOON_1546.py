n=int(input())

t, total=0,0

num=list(map(int, input().split()))

for i in range(0, n):
    
    if num[i]>=t:
        t=num[i]

for k in range(0, n):
    num[k]=100*num[k]/t
    total+=num[k]

print(total/n)