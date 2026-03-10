import sys
ba=[]

n, m=map(int, input().split())

ba=[0]*n

for j in range(0, n):
    ba[j]=j+1


for i in range(1, m+1):
    a, b=map(int, input().split())
    
    if (a-b)%2==0:
        c=(a+b)/2
        for p in range(1):
            if c+p>=b:
                break
            else:
                ba[c-p]=ba[c+p]

    elif (a-b)%2!=0:
        c1=(a+b)/2-0.5
        c2=(a+b)/2+0.5
        for t in range(0, sys.maxsize, 1):
            if c2+t>=b:
                break
            else:
                ba[c1-t]=ba[c2+t]


print(*ba)