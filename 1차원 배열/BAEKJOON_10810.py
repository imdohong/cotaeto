import sys 
here=[]

n, m=map(int, sys.stdin.readline().split())

for k in range(0, n):
    here[k]=0

for i in range(1, m+1):
    a, b, x=map(int, input().split())
    here[a, b+1]=x


print(*here)
