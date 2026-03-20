n=list(map(int, input().split()))
p=[1, 1, 2, 2, 2, 8]

def min(x):
    print(-int(n[x])+int(p[x]), end="")

for i in range(0, 6):
    min(i)