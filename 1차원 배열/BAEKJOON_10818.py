import sys

n=int(input(""))

num=list(map(int, sys.stdin.readline().split()))

max=num[0]
for i in range(0, n):
    if max<=num[i]:
        max=num[i]

min=num[0]
for i in range(0, n):
    if min>num[i]:
        min=num[i]

print(min, max)