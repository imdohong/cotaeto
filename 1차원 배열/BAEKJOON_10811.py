import sys
ba=[]

n, m=map(int, input().split())

ba=[0]*n

for j in range(0, n):
    ba[j]=j+1


for i in range(1, m+1):
    a, b=map(int, input().split())
    
    if abs(b-a)%2==0:
        c=(a+b)//2
        for p in range(0, (b-a)//2+1):
            if (c-1)+p > b-1 or (c-1)-p < a-1:
                break
            else:
                ba[c-1-p], ba[c-1+p]=ba[c-1+p], ba[c-1-p]

    else:
        c1=(a+b)//2
        c2=(a+b)//2+1
        for t in range(0, sys.maxsize, 1):
            if (c2-1)+t > b-1 or (c1-1)-t < a-1:
                break
            else:
                ba[c1-1-t], ba[c2-1+t]=ba[c2-1+t], ba[c1-1-t]


print(*ba)