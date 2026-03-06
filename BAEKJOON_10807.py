import sys
count=0

n=int(input(""))

num=list(map(int, sys.stdin.readline().split()))

v=int(input(""))


for i in range(1, n+1):
    if num[i-1]==v:
        count+=1


print(count)