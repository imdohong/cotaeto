import sys 
n, x=map(int, input().split())

a=list(map(int, sys.stdin.readline().split()))

for i in range(0, n):
    if a[i]<x:
        print(a[i], end=" ")