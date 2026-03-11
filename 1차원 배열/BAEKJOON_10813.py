n, m=map(int, input().split())

here=[]
here=[0]*n
for i in range(0, n):
    here[i]=i+1

for j in range(1, m+1):
    a, b=map(int, input().split())
    here[a-1], here[b-1]=here[b-1], here[a-1]


print(*here)